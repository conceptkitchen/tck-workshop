# Asking Questions to Get What You Want

Workshop materials for the AI workshop on August 16, 2026.
RJ Moscardon, The Concept Kitchen.

**Live:** see the Vercel deployment for this repo.

## What's here

| Page | What it is |
|---|---|
| `/` | The one move, and links to everything |
| `/speech.html` | The 3 minute talk, marked with timecodes. Built to read off a phone. |
| `/slides.html` | 10 slides with speaker notes. Short run marked at the bottom. |
| `/syllabus.html` | Full workshop. Runs at 3, 30, 60, or 90 minutes. |

## How it works

`src/*.md` is the source of truth. `build.py` renders it to static HTML in `public/`.

```
python3 build.py
```

Two things happen on the way out:

1. The internal `## Sources` fact check block is stripped from the public render.
2. Em dashes are swapped for real separators. Hard rule, no exceptions.

## Editing

Edit the markdown in `src/`, run `python3 build.py`, commit. Never hand edit `public/`.
