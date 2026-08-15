# SPEECH — "I Didn't Code Her. I Asked Her."
**AI Workshop, Sunday Aug 16, 2026 | 3 minutes | RJ Moscardon**

*Delivery notes: ~420 words at a relaxed pace = 3:00. Pause where marked. Don't rush the numbers, they land harder slow.*

---

**[0:00 — THE HOOK]**

I'm not a developer. I don't have a CS degree. I have a day job doing field work.

And I built an AI that runs my business, my calendar, my finances, and holds me accountable to my own life.

*(beat)*

I want to tell you how. Because it's not what you think.

**[0:25 — THE REVEAL]**

She's one text file. Twenty-nine thousand words. Written in plain English.

No frameworks. No stack. Just sentences.

That's the source code.

**[0:40 — THE KITCHEN]**

Here's the thing everybody gets wrong about AI.

You walk into a kitchen and say "make me food." You get food. Technically. Correct, and completely useless.

So most people do what every prompting guide tells them. Add more detail. Longer prompt. More specifics.

*(beat)*

That's backwards. Because you don't know what you're missing. That's the whole problem.

**[1:05 — THE FLIP]**

The move isn't giving better instructions. It's asking better questions.

There's a two-thousand-year-old technique for this. Socrates. He never told anybody the answer. He asked until *you* found it.

Six question types. I'll give you one of them, and then one move that's worth more than all six.

**The question.** "What am I assuming that might not be true?"

**The move.** At the end of any prompt, add: *"Before you start, ask me questions that would help you do this better."*

*(beat, let it sit)*

That's it. That one sentence. Now the AI interviews you. It pulls the context out of your head that you didn't know you had.

You stop guessing what to say. It tells you what it needs.

**[1:50 — THE PERSONA]**

Now here's how that built Clawdia.

You don't staff a kitchen by hiring "a cook." You hire a butcher, a saucier, a pastry chef. Each one sees the same ingredients differently.

So I stopped asking my AI for answers. I started asking it questions until a *person* showed up. Then I wrote that person down.

Ninety of them. A copywriter. A CFO. A therapist. A chef.

And every single one is defined by one thing: **the question they always ask.**

That's the whole trick. A persona isn't a costume. A persona is a question.

**[2:25 — THE MECHANISM]**

Last piece. When she got something wrong, I didn't retry with different words.

I told her *why* it was wrong. And we wrote it down as a rule.

Fifty rules. Every one of them is a mistake I refused to have twice.

*(beat)*

That's not prompting. That's a relationship with a memory.

**[2:45 — CLOSE]**

I didn't build an AI.

I had a six-month conversation, asked better questions than answers, and wrote down what worked.

You can do that. Starting today.

Anybody can cook.

*(out)*

---

## BACKUP — if you get more than 3 minutes

**The story that always lands (adds ~40 sec, drop in at 2:25):**

Last week I texted her one word. "Hey."

I was standing at the stove. Just saying hi.

She came back with a task list, a supplement count, and a callout that I hadn't eaten all day.

I typed back: "Fuuuck. Hello."

*(beat)*

So we wrote Rule 48. **Greeting gets a greeting.** If he says hi, say hi back.

That's the loop. She got it wrong. I told her why. It's permanent now.

That's the difference between using AI and building one.

---

## IF THEY ASK "WHERE DO I START?"

One sentence. Add it to your next prompt:

> *"Before you start, ask me questions that would help you do this better."*

That's the whole workshop in ten words.

---

## Sources
- claim: "a six-month conversation"
  source: CLAUDE.md — "Born January 29, 2026." Jan 29 → Aug 16, 2026 = 6 months, 18 days. (Was "two-year" until Aug 15; caught by FULL WAR fact-check. Two-year was fabricated.)
- claim: "Six question types. I'll give you one of them, and then one move that's worth more than all six." — the move is RECIPES-S, NOT a Socratic type
  source: recipes-cheatsheet.md:61 (S = Sanity-check) + skills/brigade/SKILL.md:28-36 (the six types). Separated deliberately so the speech doesn't miscount the flip as Socratic type #2.
- claim: "Twenty-nine thousand words" / "one text file"
  source: CLAUDE.md — verified 29,132 words, 1064 lines (wc)
- claim: "Fifty rules"
  source: CLAUDE.md numbered Rules 1-50 (Rule 50 added Aug 15, 2026, verified `grep -n "^50\. "` = line 1053, no Rule 51). NOTE: `grep -c "^[0-9]\+\. \*\*"` returns 134 — it over-matches nested numbered items. Do not use that count on stage.
- claim: "Ninety of them" (experts)
  source: skills/brigade/ROSTER.md + skills/brigade/experts/ filesystem count (92-93; stated as "ninety" for stage safety)
- claim: "Before you start, ask me questions that would help you do this better."
  source: projects/concept-kitchen/course/TCK-curriculum/resources/module-1-prompt/session-1.3-recipes-framework/recipes-cheatsheet.md:61 (RECIPES — S, Sanity-check)
- claim: Six Socratic question types
  source: skills/brigade/SKILL.md:28-36 + projects/concept-kitchen/course/TCK-curriculum/02-RIFF/06-socratic-method.md
- claim: "a persona is a question" / experts defined by the question they ask
  source: skills/brigade/SKILL.md — Expert File Template field 8 `**Lens:**` ("always starts with a quoted question")
- claim: Rule 48 "Greeting gets a greeting" + the "Hey" / "Fuuuck hello" exchange
  source: CLAUDE.md Rule 48, burned Aug 14 2026; memory/sessions/2026-08-14
- claim: "Anybody can cook"
  source: TCK brand core philosophy, CLAUDE.md TCK Brand Voice section
- claim: "not a developer, no CS degree, day job field work"
  source: USER.md / RJ-confirmed (Telegram, Aug 15 2026)
