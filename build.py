#!/usr/bin/env python3
"""
Build the TCK workshop site.

Source of truth: the markdown in src/.
Output: static HTML in public/.

Two things never reach a public page:
  1. The `## Sources` block, which is the internal fact-check audit trail (Rule 39).
  2. The `**Speaker note:**` lines on the deck. Those are backstage instructions.
     They get lifted out of the deck and appended to the speech page, which is
     unlisted, so RJ has notes and slides in one place and the room never sees
     the wiring.
"""

import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "public"

PAGES = [
    {
        "slug": "slides",
        "file": "slides.md",
        "nav": "Slides",
        "title": "The Deck",
        "kicker": "One idea per slide",
        "blurb": "The deck. Big type, one idea at a time, so the room is looking at you instead of reading ahead.",
        "body_class": "deck",
        "listed": True,
    },
    {
        "slug": "workshop",
        "file": "workshop.md",
        "nav": "Workshop",
        "title": "The Workshop",
        "kicker": "2 hours, more of it you working than me talking",
        "blurb": "The full run. Eight blocks, start to finish. Your bottleneck goes on the board in the first fifteen minutes and you build for it in the last thirty.",
        "body_class": "workshop",
        "listed": True,
    },
    {
        # Unlisted. Not in the nav, not on the home page. RJ gets the URL directly.
        "slug": "notes",
        "file": "speech.md",
        "nav": "Notes",
        "title": "Speaker Notes",
        "kicker": "One thumb, dim room",
        "blurb": "",
        "body_class": "teleprompter",
        "listed": False,
    },
]

SOURCES_BLOCK = re.compile(r"\n#{1,3}\s*Sources\b.*", re.IGNORECASE | re.DOTALL)
INTERNAL_BLOCK = re.compile(
    r"\n(?:---\n\s*)?#{1,3}\s*(?:DESIGN NOTES|FACILITATOR NOTES)\b.*?(?=\n---\n|\Z)",
    re.IGNORECASE | re.DOTALL,
)
SLIDE_HEADING = re.compile(r"^##\s+(.*)$")
SPEAKER_NOTE = re.compile(r"^\*\*Speaker note:\*\*\s*(.*)$")


def pull_internal(text: str) -> tuple[str, str]:
    """Pull production-only blocks out of the public render and hand them back.

    Sources is the fact-check audit trail and gets dropped outright. DESIGN NOTES
    and FACILITATOR NOTES are RJ's own material, so they come off the public page
    and get re-attached to the unlisted notes page instead of thrown away.
    """
    harvested = []
    for block in INTERNAL_BLOCK.findall(text):
        harvested.append(block.lstrip().removeprefix("---").lstrip())
    return strip_internal(text), "\n\n---\n\n".join(harvested)


def strip_internal(text: str) -> str:
    """Remove production-only blocks from the public render.

    Sources is the fact-check audit trail. DESIGN NOTES and FACILITATOR NOTES
    are instructions to whoever is building and running the room. None of the
    three are for the people sitting in the seats.
    """
    text = INTERNAL_BLOCK.sub("\n", text)
    return SOURCES_BLOCK.sub("\n", text).rstrip() + "\n"


def clean_punctuation(text: str) -> str:
    """No em dashes ship on anything with RJ's name on it. Hard rule.

    The drafts use them as heading separators. Swap for a middot, which is a
    real separator instead of a dash doing a separator's job.
    """
    text = re.sub(r"\s+[—–]\s+", " \u00b7 ", text)
    return text.replace("—", ",").replace("–", ",")


def lift_speaker_notes(text: str):
    """Pull the speaker notes out of the deck.

    A note starts at `**Speaker note:**` and runs until the slide ends, so a
    note can be a paragraph or a list of talking points. RJ reads these off a
    phone in a dim room, and bullets scan where a wall of text doesn't.

    Returns (deck_without_notes, notes_markdown). The notes keep the slide
    heading they belong to so they're readable on their own.
    """
    lines = text.split("\n")
    kept, notes = [], []
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        m = SLIDE_HEADING.match(line)
        if m:
            heading = m.group(1).strip()
        note = SPEAKER_NOTE.match(line)
        if not note:
            kept.append(line)
            i += 1
            continue

        body = [note.group(1).strip()]
        i += 1
        while i < len(lines) and not lines[i].startswith(("---", "#")):
            body.append(lines[i])
            i += 1
        block = "\n".join(body).strip()
        notes.append(f"### {heading}\n\n{block}\n")

    # Collapse the blank-line pairs the removed notes left behind.
    deck = re.sub(r"\n{3,}", "\n\n", "\n".join(kept))
    if not notes:
        return deck, ""
    body = "\n".join(notes)
    return deck, f"\n---\n\n## SLIDE NOTES\n\n{body}"


def to_html(text: str) -> str:
    html = markdown.markdown(
        clean_punctuation(text),
        extensions=["extra", "sane_lists", "nl2br"],
    )
    # Timecode beats become their own anchor chips instead of inline bold.
    return re.sub(
        r"<strong>\[(\d+:\d+)\s*(?:—|-|&mdash;)?\s*([^\]]*)\]</strong>",
        r'<p class="beat"><span class="clock">\1</span><span class="cue">\2</span></p>',
        html,
    )


def shell(*, title, nav_slug, content, kicker="", body_class="") -> str:
    nav = "\n".join(
        '        <a href="/{slug}.html"{cls}>{label}</a>'.format(
            slug=p["slug"],
            label=p["nav"],
            cls=' class="here"' if p["slug"] == nav_slug else "",
        )
        for p in PAGES
        if p["listed"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#F7F3EC" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#14110F" media="(prefers-color-scheme: dark)">
<title>{title}</title>
<meta name="description" content="Ask, don't micromanage. An AI workshop by RJ Moscardon, The Concept Kitchen.">
<link rel="stylesheet" href="/style.css">
<script>
  // Applied before paint so the stage never flashes white.
  (function () {{
    var t = localStorage.getItem("tck-theme");
    if (t) document.documentElement.setAttribute("data-theme", t);
  }})();
</script>
</head>
<body class="{body_class}">
<header class="bar">
  <a class="mark" href="/">
    <span class="mark-dot"></span>
    <span class="mark-text">The Concept Kitchen</span>
  </a>
  <nav>
{nav}
  </nav>
  <button id="theme" type="button" aria-label="Switch between light and dark">Dark</button>
</header>

<main>
{f'<p class="kicker">{kicker}</p>' if kicker else ''}
{content}
</main>

<footer>
  <div class="tck-lockup">
    <img src="/assets/tck-logo.png" alt="The Concept Kitchen">
    <span class="tck-lockup-text">the concept <span>kitchen</span></span>
  </div>
  <p>Ask, Don't Micromanage &middot; AI Workshop, August 20, 2026</p>
  <p>RJ Moscardon</p>
</footer>

<script>
  var btn = document.getElementById("theme");
  function paint() {{
    var dark = document.documentElement.getAttribute("data-theme") === "dark";
    btn.textContent = dark ? "Light" : "Dark";
  }}
  btn.addEventListener("click", function () {{
    var dark = document.documentElement.getAttribute("data-theme") === "dark";
    var next = dark ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("tck-theme", next);
    paint();
  }});
  paint();
</script>
</body>
</html>
"""


def write_page(page, html) -> None:
    (OUT / f"{page['slug']}.html").write_text(
        shell(
            title=f"{page['title']} | The Concept Kitchen",
            nav_slug=page["slug"],
            content=html,
            kicker=page["kicker"],
            body_class=page["body_class"],
        )
    )
    flag = "" if page["listed"] else "  (unlisted)"
    print(f"  built public/{page['slug']}.html{flag}")


def build_index() -> None:
    cards = "\n".join(
        f"""    <a class="card" href="/{p['slug']}.html">
      <span class="card-kicker">{p['kicker']}</span>
      <h2>{p['title']}</h2>
      <p>{p['blurb']}</p>
      <span class="card-go">Open</span>
    </a>"""
        for p in PAGES
        if p["listed"]
    )
    content = f"""<section class="lede">
  <h1>The best manager you ever had<br><em>didn't tell you what to do.</em></h1>
  <p class="sub">They asked you one question that made you better at your own job. That is the entire skill of working with AI, and almost nobody does it.</p>
</section>

<section class="cards">
{cards}
</section>

<section class="pull">
  <p>Walk into a kitchen and say &ldquo;make me food.&rdquo; You'll get food. Technically correct, completely useless.</p>
  <p class="pull-tag">That is not the kitchen failing. That is the order failing.</p>
</section>

<section class="one-move">
  <h2>If you take one thing home</h2>
  <p>Put this at the end of your next prompt, whatever you were already going to ask it:</p>
  <blockquote class="move">Before you start, ask me questions that would help you do this better.</blockquote>
  <p class="after">One sentence, and it stops guessing and starts interviewing you. It pulls out the context that was in your head the whole time, that you never thought to say out loud.</p>
</section>
"""
    (OUT / "index.html").write_text(
        shell(title="Ask, Don't Micromanage | The Concept Kitchen",
              nav_slug="", content=content, body_class="home")
    )
    print("  built public/index.html")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "style.css", OUT / "style.css")
    # Brand art for the title cards. Source of truth is src/assets, mirrored into
    # public/ so the deck can reference /assets/... on the live site.
    shutil.copytree(SRC / "assets", OUT / "assets", dirs_exist_ok=True)
    print("building:")
    print(f"  copied {len(list((OUT / 'assets').iterdir()))} assets")

    notes = ""
    internal = []
    for page in PAGES:
        raw, pulled = pull_internal((SRC / page["file"]).read_text())
        if pulled:
            internal.append(pulled)
        if page["slug"] == "slides":
            raw, notes = lift_speaker_notes(raw)
        elif page["slug"] == "notes":
            raw = raw + notes
            if internal:
                raw += "\n\n---\n\n" + "\n\n---\n\n".join(internal)
        write_page(page, to_html(raw))

    build_index()
    print("done.")


if __name__ == "__main__":
    main()
