#!/usr/bin/env python3
"""
Build the TCK workshop site.

Source of truth: the markdown in src/.
Output: static HTML in public/.

The `## Sources` block at the bottom of each draft is the internal fact-check
audit trail (Rule 39). It gets stripped from the public render.
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
        "slug": "speech",
        "file": "speech.md",
        "nav": "Speech",
        "title": "The Speech",
        "kicker": "3 minutes, out loud",
        "blurb": "The talk itself, marked with timecodes. Built to read off a phone at arm's length.",
        "body_class": "teleprompter",
    },
    {
        "slug": "slides",
        "file": "slides.md",
        "nav": "Slides",
        "title": "The Deck",
        "kicker": "10 slides, one idea each",
        "blurb": "Slide copy plus the speaker note for every one. The short run is marked at the bottom.",
        "body_class": "deck",
    },
    {
        "slug": "syllabus",
        "file": "syllabus.md",
        "nav": "Syllabus",
        "title": "The Syllabus",
        "kicker": "3, 30, 60, or 90 minutes",
        "blurb": "The full workshop. Four modules, the RECIPES framework, exercises, and the handout.",
        "body_class": "syllabus",
    },
]

SOURCES_BLOCK = re.compile(r"\n#{1,3}\s*Sources\b.*", re.IGNORECASE | re.DOTALL)


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


def shell(*, title, nav_slug, content, kicker="", body_class="") -> str:
    nav = "\n".join(
        '        <a href="/{slug}.html"{cls}>{label}</a>'.format(
            slug=p["slug"],
            label=p["nav"],
            cls=' class="here"' if p["slug"] == nav_slug else "",
        )
        for p in PAGES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#F7F3EC" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#14110F" media="(prefers-color-scheme: dark)">
<title>{title}</title>
<meta name="description" content="Asking questions to get what you want. An AI workshop by RJ Moscardon, The Concept Kitchen.">
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
  <p>Asking Questions to Get What You Want &middot; AI Workshop, August 16, 2026</p>
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


def build_page(page) -> None:
    raw = (SRC / page["file"]).read_text()
    html = markdown.markdown(
        clean_punctuation(strip_internal(raw)),
        extensions=["extra", "sane_lists", "nl2br"],
    )
    # Timecode beats become their own anchor chips instead of inline bold.
    html = re.sub(
        r"<strong>\[(\d+:\d+)\s*(?:—|-|&mdash;)?\s*([^\]]*)\]</strong>",
        r'<p class="beat"><span class="clock">\1</span><span class="cue">\2</span></p>',
        html,
    )
    (OUT / f"{page['slug']}.html").write_text(
        shell(
            title=f"{page['title']} | The Concept Kitchen",
            nav_slug=page["slug"],
            content=html,
            kicker=page["kicker"],
            body_class=page["body_class"],
        )
    )
    print(f"  built public/{page['slug']}.html")


def build_index() -> None:
    cards = "\n".join(
        f"""    <a class="card" href="/{p['slug']}.html">
      <span class="card-kicker">{p['kicker']}</span>
      <h2>{p['title']}</h2>
      <p>{p['blurb']}</p>
      <span class="card-go">Open</span>
    </a>"""
        for p in PAGES
    )
    content = f"""<section class="lede">
  <h1>I didn't code her.<br><em>I asked her.</em></h1>
  <p class="sub">Three minutes on the one move that changes what you get out of AI: stop giving better instructions, start asking better questions.</p>
</section>

<section class="cards">
{cards}
</section>

<section class="pull">
  <p>You walk into a kitchen and say &ldquo;make me food.&rdquo; You get food. Technically correct, and completely useless.</p>
  <p class="pull-tag">That is not the kitchen failing. That is the order failing.</p>
</section>

<section class="one-move">
  <h2>If you take one thing home</h2>
  <p>Put this at the end of any prompt:</p>
  <blockquote class="move">Before you start, ask me questions that would help you do this better.</blockquote>
  <p class="after">Now it interviews you. It pulls the context out of your head that you didn't know you had.</p>
</section>
"""
    (OUT / "index.html").write_text(
        shell(title="Asking Questions to Get What You Want | The Concept Kitchen",
              nav_slug="", content=content, body_class="home")
    )
    print("  built public/index.html")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "style.css", OUT / "style.css")
    print("building:")
    for page in PAGES:
        build_page(page)
    build_index()
    print("done.")


if __name__ == "__main__":
    main()
