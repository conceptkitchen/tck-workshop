# SPEECH · "Ask, Don't Micromanage"
**AI Workshop, Sunday Aug 16, 2026 | 3 minutes | RJ Moscardon**

*~440 words at a relaxed pace = 3:00. Pause where marked. Don't rush the six questions, let the room hear each one.*

*This page is built to read at arm's length, one thumb, in a dim room. No printout, no index cards, no second screen. The page is the notes. Slide notes are at the bottom.*

---

**[0:00 THE HOOK]**

Think about the best manager you ever had.

They didn't stand over your shoulder telling you which keys to press. They asked you one question that made you better at your own job.

*(beat)*

That's the entire skill of working with AI. And almost nobody does it.

**[0:25 THE PROBLEM]**

Most of us treat AI like a vending machine. Put in a request, get a product.

When the product is bad, we do what every guide tells us to do. Add detail. Longer prompt. More specifics.

*(beat)*

That's micromanaging. And it caps the output at whatever you already knew to ask for.

**[0:50 THE KITCHEN]**

Walk into a kitchen and say "make me food." You'll get food. Technically correct, completely useless.

That's not the kitchen failing. That's the order failing.

But the fix isn't a longer order. The fix is letting the kitchen ask you questions.

**[1:15 THE SETUP]**

So here's what I actually do, and it goes both ways.

I set the goal, and I say what good looks like. That part's my job.

Then I ask it: *you're the expert, what do you think you should do?*

And it asks me back: *what do you mean by good?*

*(beat)*

Neither of us guessed. That exchange is the setup, and the setup decided the output before either of us did any work.

You don't get what you want by asking harder. You get it by setting up better.

One sentence you can steal today. Put this at the end of your next prompt:

*"Before you start, ask me questions that would help you do this better."*

**[1:45 THE QUESTIONS]**

That works in both directions. The questions you ask yourself matter just as much.

Two thousand years ago a teacher named Socrates figured out you learn more from a good question than a good answer. He never told anyone what to think. He asked until they got there themselves.

Six questions. You already know all of them.

What do I actually mean by this?

What am I assuming?

How do I know that's true?

What would someone who disagrees say?

If this works, what happens next?

And the big one. Am I even asking the right question?

**[2:15 THE BRIGADE]**

Here's where that got me.

I have about ninety experts I can call on. A copywriter, a CFO, a therapist, a chef.

I didn't write ninety personas. I asked one question, ninety times.

*Who should be in the room for this?*

*(beat)*

That's the same move from a minute ago, just run ninety times. I didn't build them, I interviewed them into existence.

I'm not a developer. No CS degree. I do field work for a living. Six months of that, written down in one text file, plain English, no code. Fifty rules in it now, and every one is a mistake I refused to have twice.

**[2:45 CLOSE]**

I didn't build that. I managed it. I asked better questions than I gave answers.

You can start today, with one sentence.

Anybody can cook.

---

## BACKUP · THE CORRECTION STORY

*~35 seconds. Drop in at 2:15 if you're running fast, or use it to answer "does it actually learn?"*

Last week I texted it one word. Hi.

It came back with a task list and three things I hadn't done yet.

I told it: I said hello. That's all that was.

So we wrote a rule. If he says hi, say hi back.

It got it wrong. I told it why. It's permanent now.

That's the difference between using an AI and managing one. Retrying is re-rolling the dice. Correcting is building something with a memory.

---

## IF THEY ASK "WHERE DO I START?"

One sentence, on your next prompt, whatever you were already going to ask it:

*"Before you start, ask me questions that would help you do this better."*

Answer its questions honestly. That's the whole first lesson.

---

## IF THEY ASK "HOW IS THIS DIFFERENT FROM PROMPT ENGINEERING?"

Prompt engineering is writing a better order. This is hiring better and asking better.

You're not looking for magic words. You're giving something capable enough context to do the work well, the same way you would with a person.

---

## Sources
- claim: "six months" of building
  source: CLAUDE.md ("Born January 29, 2026") · Jan 29 to Aug 16 2026 = 6 months 18 days
- claim: "Fifty rules"
  source: CLAUDE.md numbered Rules 1-50 (Rule 50 added Aug 15 2026; verified `grep -n "^50\. "` = line 1053, no Rule 51). NOTE: `grep -c` on the numbered-rule pattern returns 134, it over-matches nested numbered items. Do not use that count on stage.
- claim: "one text file, plain English, no code"
  source: CLAUDE.md, 29,132 words / 1064 lines, markdown prose (wc)
- claim: "runs my calendar, my finances, my outreach, holds me accountable"
  source: CLAUDE.md (calendar rules, Financial Flywheel, Outreach Pipeline Rules, Rule One Flywheel)
- claim: "not a developer, no CS degree, field work for a living"
  source: USER.md · RJ-confirmed (Telegram, Aug 15 2026)
- claim: "about ninety experts" / "ninety times"
  source: skills/brigade/experts/ filesystem count = 93 files (`ls skills/brigade/experts/*.md | wc -l`) vs skills/brigade/ROSTER.md = "92 experts". Sources conflict by one, so the stage number is hedged to "about ninety." Never state an exact count on stage.
- claim: "Who should be in the room for this?" as the single repeated build question
  source: RJ-confirmed (Telegram, Aug 15 2026), his own description of how the brigade was built
- claim: Socrates asked rather than told, roughly two thousand years ago
  source: general classical-philosophy knowledge, no specific stake
- claim: the six questions
  source: skills/brigade/SKILL.md:28-36 ("The Six Socratic Types"), restated in plain English without the taxonomy labels per RJ's note that the audience does not know the academic terms
- claim: "Before you start, ask me questions that would help you do this better."
  source: projects/concept-kitchen/course/TCK-curriculum/resources/module-1-prompt/session-1.3-recipes-framework/recipes-cheatsheet.md:61 (RECIPES, S = Sanity-check)
- claim: the "Hi" correction story and the resulting rule
  source: CLAUDE.md Rule 48 "Greeting gets a greeting" (burned Aug 14 2026) · memory/sessions/2026-08-14. Profanity removed from the on-stage version per RJ, Aug 15 2026.
- claim: "Anybody can cook"
  source: CLAUDE.md, The Concept Kitchen Brand Voice
- claim: the manager framing (a good manager asks rather than micromanages)
  source: RJ-confirmed (Telegram, Aug 15 2026), his own words
