# Ask, Don't Micromanage

Workshop materials for the AI workshop on August 16, 2026.
RJ Moscardon, The Concept Kitchen.

**Live:** see the Vercel deployment for this repo.

## What's here

| Page | What it is |
|---|---|
| `/` | The one move, and links to everything |
| `/slides` | 10 slides, one idea each, plus slide 11 after the credits. |
| `/workshop` | The 30 minute run. Also scales to 60 or 90. |
| `/notes` | **Unlisted.** Speaker notes: the three moves, the 30 minute clock, plus every slide note. Built to read off a phone, one thumb, in a dim room. Not in the nav, not on the home page. The 3 minute speech was retired Aug 15 2026. `/speech` and `/syllabus` redirect here and to `/workshop` so old links don't break. |

## How it works

`src/*.md` is the source of truth. `build.py` renders it to static HTML in `public/`.

```
python3 build.py
```

Three things happen on the way out:

1. The internal `## Sources` fact check block is stripped from the public render.
2. Em dashes are swapped for real separators. Hard rule, no exceptions.
3. `**Speaker note:**` lines are lifted off the public deck and appended to the unlisted speech page as a `## SLIDE NOTES` section. The deck is public. The notes are not.

## Editing

Edit the markdown in `src/`, run `python3 build.py`, commit. Never hand edit `public/`.
