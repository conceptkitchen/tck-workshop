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
        "kicker": "10 slides, one idea each",
        "blurb": "Ten slides, one idea on each. The short run is marked at the bottom.",
        "body_class": "deck",
        "listed": True,
    },
    {
        "slug": "syllabus",
        "file": "syllabus.md",
        "nav": "Syllabus",
        "title": "The Syllabus",
        "kicker": "3, 30, 60, or 90 minutes",
        "blurb": "The full workshop. Four modules, the RECIPES framework, exercises, and the handout.",
        "body_class": "syllabus",
        "listed": True,
    },
    {
        # Unlisted. Not in the nav, not on the home page. RJ gets the URL directly.
        "slug": "speech",
        "file": "speech.md",
        "nav": "Speech",
        "title": "The Speech",
        "kicker": "3 minutes, out loud",
        "blurb": "",
        "body_class": "teleprompter",
        "listed": False,
    },
]

SOURCES_BLOCK = re.compile(r"\n#{1,3}\s*Sources\b.*", re.IGNORECASE | re.DOTALL)
SLIDE_HEADING = re.compile(r"^##\s+(.*)$")
SPEAKER_NOTE = re.compile(r"^\*\*Speaker note:\*\*\s*(.*)$")


def strip_internal(text: str) -> str:
    """Remove the fact-check Sources block from the public render."""
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

    Returns (deck_without_notes, notes_markdown). The notes keep the slide
    heading they belong to so they're readable on their own.
    """
    kept, notes = [], []
    heading = ""
    for line in text.split("\n"):
        m = SLIDE_HEADING.match(line)
        if m:
            heading = m.group(1).strip()
        note = SPEAKER_NOTE.match(line)
        if note:
            notes.append(f"### {heading}\n\n{note.group(1).strip()}\n")
            continue
        kept.append(line)

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
  <p>Ask, Don't Micromanage &middot; AI Workshop, August 16, 2026</p>
  <p>RJ Moscardon, The Concept Kitchen</p>
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
    print("building:")

    notes = ""
    for page in PAGES:
        raw = strip_internal((SRC / page["file"]).read_text())
        if page["slug"] == "slides":
            raw, notes = lift_speaker_notes(raw)
        elif page["slug"] == "speech":
            raw = raw + notes
        write_page(page, to_html(raw))

    build_index()
    print("done.")


if __name__ == "__main__":
    main()
