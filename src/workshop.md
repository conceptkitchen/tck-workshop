# THE WORKSHOP
## Ask, Don't Micromanage
### Build an agent for your recruiting workflow

**Instructor:** RJ Moscardon, The Concept Kitchen
**Runtime:** 2 hours, hands on keyboards for about half of it.
**Room:** Recruiters and talent professionals.
**Prereq:** None. Bring a laptop and any AI chat tool you already pay for or use free.

---

## THE PREMISE

Nineteen people in this room answered one question before tonight: *what's your biggest recruiting challenge today?*

Here is some of what came back, in your words, uncleaned:

> *"Time."*
> *"Sourcing."*
> *"Time management with sourcing."*
> *"Finding the time to build up and manage a qualified pipeline."*
> *"balancing volume & quality responses"*
> *"Maintaining contacts"*
> *"Responding to candidates"*
> *"Automation on various processes"*

One of you wrote the whole diagnosis out yourself:

> *"We have no ATS because our applicant and hiring volume is small. I know our manual process (collecting resumes in a career inbox, saving the docs, adding name to a spreadsheet) is a super simple process to automate with a workflow but I've been trying and can use some help"*

That person named the problem, named the shape of the fix, tried it, and got stuck. That is not a knowledge gap. That is a **setup** gap.

**Here is the frame for the next two hours.** Almost every problem on that list has the same shape: a fixed amount of you, against a volume that does not care. More effort does not fix that. A better tool does not fix that either, or the person above would already be done.

**The setup makes you the bottleneck.** Tonight you change the setup.

**Your background doesn't matter here.** Technical, non-technical, never touched any of this. The whole goal is to make it relatable enough that you walk out thinking critically about what you're asking for. That's how you get the most out of the technology. Not the tool. The asking.

> **Anybody can cook.** You don't need a culinary degree to make a great meal. You need to know what you want, how to ask for it, and how to taste as you go.

---

## LEARNING OUTCOMES

By the end, you can:

1. **Say what an agent actually is** in one sentence, and name the six pieces it's built from
2. Diagnose *why* an AI response was useless (it's almost never the AI)
3. Run the **RECIPES** framework to structure any request
4. **Manage by asking, not telling.** Treat the AI as the expert and ask what it thinks instead of dictating steps
5. Use the **flip** to make AI interview you instead of guessing at you
6. Apply **six question types** to interrogate your own thinking
7. Build a reusable **expert** by asking questions until a person shows up
8. Turn corrections into **permanent rules** so the same mistake never happens twice
9. Stand up a working setup on your own machine, with your own account, that outlives tonight

---

## MODULE 0 — THE FOUNDATION
### *"An agent is a model that can use tools, running in a loop until the job is done."*
**Time:** 15 min | **Metaphor:** Knowing what's in the kitchen before you cook

Everybody is talking about agents. Almost nobody says what one actually **is**. That gap is why this feels like hype instead of something you could use on Monday.

You cannot ask well for a thing you cannot picture. So before any of the asking, here is the picture.

---

### First, the confusion to clear

**A chatbot talks.** You type, it types back. That's the whole interaction. It cannot open your career inbox. It cannot save a resume to a folder. It cannot add a row to your spreadsheet or put a hold on a calendar. It generates words.

**An agent is that same model with two things added:**

1. **It can take actions.** (tools)
2. **It keeps going on its own,** step after step, instead of stopping after one reply. (the loop)

> **The one-sentence version: an agent is a language model that can use tools, running in a loop until it finishes a job.**

That's it. Everything else is detail.

A chatbot answers a **question**. An agent is given a **goal** and goes and accomplishes it.

---

### The building blocks

Six pieces. None of them require a degree to understand.

| The piece | What it actually is | In your kitchen |
|---|---|---|
| **The brain** | The model. All it does is predict text. It has no hands and no memory. | The cook. Skilled, and standing there with nothing. |
| **The hands** | Tools. The model doesn't reach into your inbox. It writes a structured request that says *"use the inbox tool,"* and the software around it does that and hands the result back. | The knives, the pans, the oven. |
| **The counter** | The context window. Everything it can see at one moment. It has a hard limit. | Counter space. You cannot put the whole pantry on it. |
| **The house rules** | The system prompt. Who it is, how it behaves, what it never does. | The rules of your kitchen, posted on the wall. |
| **The recipe box** | Files it can read. The model has no memory between sessions. It remembers what's written down. | The binder of recipes you keep annotating. |
| **The loop** | Think, act, look at the result, decide again. Repeat until done. | Taste, adjust, taste again. |

**The one that surprises people: the model has no memory.** Not a little memory. None. Every single turn, the whole conversation gets handed back to it again. That is why **Module 4** matters so much. If a correction isn't written down somewhere it can read, the correction dies when you close the tab.

**And the one that unlocks the most: the model never actually touches anything.** It asks. The software around it acts. Which means the entire question of "what can my agent do?" is really the question **"what have I given it access to?"**

---

### The landscape: four ways to build one

Same loop every time. The only variable is how much of it you assemble yourself.

| Tier | What you do | Who it's for |
|---|---|---|
| **1 — No code** | Fill out forms, drag blocks around. | Fastest start, tightest ceiling. |
| **2 — Low code** | Wire steps together, drop in a little logic. | Automations that outgrew tier 1. |
| **3 — Agent harness** ← **tonight** | Someone else built the loop. You bring the rules, the files, and the tools. | **This room.** |
| **4 — Write it yourself** | Build the loop in code, line by line. | Engineers with a reason to. |

**We are at tier 3 tonight,** and that is a deliberate choice, not a beginner's compromise. The loop is a solved problem. Nobody is paying you to rebuild it. What nobody can do for you is decide **what to ask it and what to give it access to.** That is the whole rest of this workshop.

**Take-home:** tier 1 and tier 2 tools are in the handout if you want to compare. Tier 4 is not homework.

---

> ### 🔵 BREAKOUT A — Name your loop
> **Time:** 8 min | **Groups of 3 or 4. Turn your chairs.**
>
> 1. **Around the table, each person names one recruiting task you currently run by hand that is obviously a loop.** Something with the shape: *check, decide, do, check again.* The career-inbox problem from THE PREMISE is one. So is chasing a candidate who's gone quiet.
> 2. **Pick ONE from your table** to carry through the rest of tonight. You will build for it in Module 3 and report on it at the end.
> 3. **Write it on the card.** One sentence.
>
> **Facilitator:** don't let a table stall on picking the "best" one. Any real one works. Every table has an answer inside 90 seconds.

---

## MODULE 1 — THE ORDER
### *"Vague in, garbage out."*
**Time:** 8 min | **Metaphor:** Ordering at the counter

**The problem**
Walk into a kitchen and say "make me food." You'll get food. Technically correct, completely useless. That's not the kitchen failing. That's the order failing.

**The reframe**
AI doesn't give bad answers. It gives *accurate answers to vague questions.*

Ask it to "write a job description" and you get a job description. Beige, interchangeable, and you'll rewrite it anyway. That round trip cost you fifteen minutes and produced nothing you didn't already have.

**Teach: RECIPES**, the recipe card for any request

| Letter | Element | Ask Yourself |
|--------|---------|--------------|
| **R** | Role | Who should AI be? What expertise do I need? |
| **E** | Examples | Can I show it what "good" looks like? |
| **C** | Context | What background does it need for THIS task? |
| **I** | Instructions | What exactly do I want produced? |
| **P** | Parameters | Constraints? Format? Length? What to avoid? |
| **E** | Energy | What tone should this have? |
| **S** | Sanity-check | Should it ask me questions before starting? |

**When to use what**
- Quick question → **R + I**
- Candidate email or InMail → **R + C + I + P + E**
- Anything you'll do more than twice → **all 7**, especially **S**
- Scorecards, rubrics, JD mapping → **C + I + P**

**🔪 EXERCISE 1.1 — "Fix the Order" (7 min)**
Write the worst prompt you used this week. The one that gave you something you threw away. Rewrite it with RECIPES. Run both. Compare side by side.

**Takeaway:** *You don't need a better AI. You need a better order.*

---

## MODULE 2 — THE CONVERSATION
### *"It's the expert. Ask it what it thinks."*
**Time:** 15 min | **Metaphor:** Tasting as you cook

*This is the foundation. Everything after it is built on this module.*

**The problem with Module 1**
RECIPES assumes you know what you want. Most of the time you don't. Every prompting guide says "add more detail." You cannot add detail you don't know is missing.

The fix isn't a better instruction. It's a conversation. And a conversation goes **both directions.**

---

### DIRECTION 1 — You ask it
#### *The manager move*

Most people prompt like they're giving orders. Do this. Write that. Make it shorter.

You already know this is the wrong way to run a person. A good manager doesn't micromanage. He sets the goal and the standard, then asks the expert what *they* think, because they're the expert. You hired them for their judgment. Use it.

Same thing here. Stop telling it what to do. Start asking it what it thinks.

| Instead of telling it | Ask it |
|---|---|
| "Write me a 3-step sourcing plan." | "You're the expert here. How would you approach this search?" |
| "Use this outreach structure." | "What structure would you use, and why?" |
| "Make this InMail shorter." | "What's not earning its place in here?" |
| "Do it this way." | "What would you do differently than what I just described?" |
| "Here's my plan, execute it." | "Here's my plan. What am I missing?" |

**Why this beats commanding**
You still set the goal. You still hold the standard. But now the expert generates the plan and **you're editing instead of writing.** That's less brain power for a better result. You go from producing to directing.

That's the whole payoff: a better plan, a better strategy, and clear steps to take, with expert guidance instead of your own guessing.

---

### DIRECTION 2 — It asks you
#### *The flip*

Now the other way. Add this to the end of any request:

> **"Before you start, ask me questions that would help you do this better."**

That's the **S** in RECIPES, and it's worth more than the other six letters combined. It flips the direction. Now the AI pulls context out of your head that you never thought to say out loud.

Try it on an intake you're dreading. It will ask you the things you'd normally find out in week three.

**Put both together and you have a conversation.** You ask it what it thinks. It asks you what it needs. Nobody in that exchange is pretending to have all the answers. That's the setup, and everything good comes out of the setup.

---

**Then go deeper: the Socratic method**

Socrates never told anyone the answer. He asked until they found it themselves. The Greeks called it *maieutics*, literally **midwifery**. You don't deliver the idea. You help it get born.

**The six types**

| # | Type | Purpose | Key Prompt |
|---|------|---------|-----------|
| 1 | **Clarification** | Define the real problem | "What do I actually mean by [X]?" |
| 2 | **Probe Assumptions** | Surface hidden beliefs | "What am I assuming that might not be true?" |
| 3 | **Probe Evidence** | Demand proof | "How do I know this is true?" |
| 4 | **Explore Perspectives** | Break your frame | "Steelman the opposite position." |
| 5 | **Probe Implications** | Think 3 steps ahead | "If this works, then what?" |
| 6 | **Question the Question** | Test the framing | "Is this even the right question?" |

**Regular prompting vs. asking**

| Regular | Socratic |
|---------|----------|
| Assumes the problem is framed right | Questions the framing itself |
| Seeks answers | Seeks better questions |
| Makes you faster | Makes you smarter |
| Confirms your thinking | Surfaces what's missing |
| One step ahead | Three steps ahead |

**A note on discomfort:** the moment you realize you don't actually know something is called *aporia*. It feels like failure. It's the point. It's the taste test that saves the dish.

**🔪 EXERCISE 2.1 — "The Reverse Interview" (12 min)**
Pick a real thing on your desk. A req you can't fill, a pipeline you can't keep warm, a hiring manager you can't get straight answers from. Run both directions on it.

1. **You ask it:** *"You're the expert on this. How would you approach [X], and what would you do differently than I would?"*
2. **It asks you:** *"I'm deciding whether to [X]. Don't advise me. Ask me the five questions I should be asking myself."*

Answer them out loud to the person next to you. Notice which direction surfaced the thing you hadn't thought of.

**Takeaway:** *Stop giving orders. Start having a conversation. Ask the expert what it thinks, and let it ask you what it needs.*

---

## ☕ BREAK — 5 min

---

## MODULE 3 — THE BRIGADE
### *"A persona isn't a costume. A persona is a question."*
**Time:** 12 min | **Metaphor:** Staffing your kitchen

**The problem**
You've asked good questions. But you're still getting one perspective, the AI's default, averaged, safe voice. Generic in, generic out.

**The kitchen answer**
No real kitchen hires "a cook." A kitchen hires a **butcher**, a **saucier**, a **pastry chef**, an **expeditor**. Same ingredients, four completely different reads on what to do with them. That's a **brigade**.

**The build move**
Don't tell the AI to "act like an expert." Ask it questions until a *person* shows up. Then write that person down.

**What actually defines a person**
Not the job title. Not the bio. **The question they can't stop asking.**

- A copywriter asks: *"Does the first line earn the second?"*
- A CFO asks: *"What does this cost us if it works?"*
- A sourcer asks: *"Who already works somewhere this problem is solved?"*
- A chef asks: *"What's already in the fridge?"*

That question is the **Lens**. The Lens *is* the expert. Everything else is decoration.

**The build sheet** *(the spine. A production expert carries more fields, but these seven do the work.)*

| Field | What it is |
|-------|-----------|
| **Name + Emoji** | So you can call them fast |
| **Role** | One line |
| **Lens** | ⭐ **The question they always ask.** Write it in quotes. |
| **Expertise** | What they actually know |
| **Blind spots** | What they get wrong, so you know when to overrule them |
| **Anti-patterns** | What they must never do |
| **Defers to** | Who outranks them and when |

**Why asking and staffing are the same technique**
- **Type 4 (Explore Perspectives) *is* the brigade.** It goes deeper, because you inhabit the perspective instead of just hearing about it.
- **Type 6 (Question the Question) is what a good outsider does.** "Are we even in the right room?"
- **Types 2 and 3 (Assumptions and Evidence) are what the CFO and the skeptic do automatically.** Build them in once and you never have to remember to ask again.

**🔪 EXERCISE 3.1 — "Build the Setup" (18 min)**

**Pick one thing on your bottleneck list.** Sourcing. Follow-up. The scorecard. The inbox with the resumes in it.

1. Ask: *"Who should be in the room to help me build this?"*
2. **Interview whoever shows up.** Use the six questions. Do not take the first answer.
3. Then ask: *"Now tell me what to build, and what I'm missing."*
4. Fill the build sheet. Save it in a file. That file is the asset, not the chat.

**You are not building the thing tonight. You're building the setup that builds it.**

Whatever you're making, answer this one before you stop:

> ### **What's the one question this thing answers for me, every time?**

For an expert that's their Lens. For a workflow it's the purpose. For a tool it's the job. Same field, three names. If you can't answer it, you don't have a spec yet. You have a wish.

**Takeaway:** *You don't prompt a thing into existence. You interview one into existence.*

---

> ### 🔵 BREAKOUT B — Build one expert for your table's loop
> **Time:** 10 min | **Same groups. One laptop open per table is enough.**
>
> Take the loop your table picked in Breakout A and build **one Lens** for it, together.
>
> 1. **Name the person you'd hire** for that loop. Not a job title. The one thing they'd always catch.
> 2. **Interview them into existence** using the move from this module. Let the AI ask the table questions. Answer out loud, as a table, so you hear each other disagree.
> 3. **Land on their one question.** The thing this Lens asks about everything it sees.
>
> **Done looks like:** one sentence you could hand to the table next to you and they'd know exactly who it is.
>
> **Facilitator:** the disagreement inside the table is the point. When two recruiters at one table define "qualified" differently, that's the exact ambiguity the Lens has to settle.
>
> **If a table has no working laptop, say this and move on:** *"Do it out loud. One of you plays the expert, the rest interview them. You'll get the same answer, you'll just get it faster."* The interview is the exercise. The laptop is a convenience. The setup module hasn't run yet, so expect at least one table here.

---

## MODULE 4 — THE LOOP
### *"Correcting out loud."*
**Time:** 8 min | **Metaphor:** The recipe card you keep annotating

**The problem**
The AI gets it wrong. Almost everyone does the same thing: retry with different words. That's re-rolling the dice. Nothing was learned. It'll happen again next week, and the week after.

**The move**
Don't retry. **Say why it was wrong.** Then make the correction permanent.

Not: *"no, try again"*
But: *"That was wrong because ___. Going forward, when I ___, you should ___. Write that down."*

**Why this compounds**
Every correction becomes a rule. Every rule is a mistake you refuse to have twice. Do that for a year and you don't have a prompt. You have a *system with a memory.*

**Real example, mine**
I texted my AI one word: "Hi." I was standing at the stove, just saying hello. It came back with a task list and three things I hadn't done yet.

I told it: *I said hello. That's all that was.*

So we wrote a rule: **greeting gets a greeting.** If he says hi, say hi back. The rest can wait.

It has never done it again. Not because the model improved. Because the correction became permanent.

**🔪 EXERCISE 4.1 — "Write Rule One" (7 min)**
Find one thing your AI does that annoys you. Write it in this format:

> **Rule:** [The behavior, stated positively]
> **Trigger:** [When this applies]
> **Why:** [The specific time it went wrong]

Paste it into your system prompt, custom instructions, or project file. That's your first line of source code.

**Takeaway:** *Prompting is a transaction. Correcting out loud is a relationship.*

---

## MODULE 5 — THE SETUP
### *"Get it off the chat window and onto your machine."*
**Time:** 12 min, hands on keyboards | **Metaphor:** Your own kitchen, not a rented one

Everything so far works in any chat box. This part makes it persist.

A chat window forgets you. A setup remembers you. The difference is where the files live.

**What we're standing up: OpenClaw**
An open agent runtime, signed in with an account you already have. It reads a folder of files you control, which means your Lenses, your rules, and your corrections load every time instead of getting re-explained every time.

**Why OpenClaw specifically**
- **It's free.** No metered API bill that grows while you learn.
- **It runs on a subscription you may already pay for**, rather than per-token billing. Nobody should watch a token meter run while they're learning.
- **It's model-agnostic.** OpenAI, Google Gemini, or Claude. Bring whatever you already have. You do not buy anything new tonight.
- **It's OS-agnostic.** Mac or Windows. Both work in this room.
- **Nothing here runs on my account.** You walk out owning it.

**Two install paths, same steps**

| | Path | When | Why this one |
|---|---|---|---|
| **1** | **Your own laptop** | In the room, tonight | Fastest to a working setup. You leave with it running. |
| **2** | **Google Cloud** | Walked on screen, finish at home | Runs when your laptop is closed. Same steps, different machine. |

Both paths are in the handout, written out step by step. We do **path 1 live** because 12 minutes gets a whole room to a working laptop install and it does not get a whole room through a cloud console. I demo **path 2 on screen** during the same block so you have seen every step before you try it.

**The one rule for this block:** if you get stuck, raise a hand and keep going to the next step. Do not sit stuck and quiet. The person next to you probably hit the same wall ninety seconds ago.

---

## CLOSING

> ### 🔵 BREAKOUT C — Report back
> **Time:** 8 min | **One sentence per table, out loud, to the whole room.**
>
> **The format, and hold people to it:**
>
> > *"Our loop was **\_\_\_\_**. Our expert asks **\_\_\_\_**."*
>
> That's the whole report. Two blanks. No preamble.
>
> **Why this is the last thing we do:** you are about to hear seven or eight versions of your own job, described by people who sit in different seats than you. Some table is going to name a loop you didn't know was a loop. Take that one home too.
>
> **Facilitator:** cut anyone who goes past two sentences, warmly. The constraint is what makes the room hear all of them.

---

### The arc

0. **Know what it is** → A model, tools, a loop. No magic.
1. **Order better** → RECIPES
2. **Have the conversation** → Ask the expert what it thinks. Let it ask you what it needs.
3. **Staff the kitchen** → Experts built from questions
4. **Keep the notes** → Correcting out loud
5. **Own the room** → A setup on your machine that remembers all four

---

### BUILD YOUR OWN BRIGADE

You built one expert tonight. Here's what happens when you build twelve.

**A brigade is a roster of Lenses.** Each one is a file. Each file is a person defined by the question they always ask. That's the whole architecture.

```
your-setup/
  experts/
    sourcer.md        Lens: "Who already works somewhere this is solved?"
    skeptic.md        Lens: "What breaks first?"
    writer.md         Lens: "Does the first line earn the second?"
    numbers.md        Lens: "What does this cost us if it works?"
  rules.md            Every correction you ever made, permanent
```

**How you call it.** Once the files exist, you stop writing prompts and start naming who you want in the room.

- **One expert** when you know whose judgment you need. *"Sourcer, read this req."*
- **A panel** when you don't. Three or four Lenses on the same problem, each answering in their own voice, then you decide.
- **An outsider on purpose.** Add someone with no business being in the meeting. The Lens that doesn't fit is the one that catches what everyone else agreed to overlook.

**Why a panel beats one answer.** Four Lenses on the same question will disagree. That disagreement is the product. When three of them independently land on the same thing, that's not consensus theater, that's a signal you can act on. When one of them objects and the others can't answer the objection, you just found the flaw before it cost you.

**The part nobody tells you:** the brigade gets good from the corrections, not from the writing. Every time an expert gets it wrong and you say why, that expert gets sharper. The roster is the skeleton. The correction log is the muscle.

**Start with two.** One expert for the thing you do most, one skeptic to argue with them. Add the third when you notice you keep wishing someone else were in the room.

**Say this out loud when the folder exists.** Everything before this module was about asking better in the moment. This module is what makes the moment better before you open your mouth. Four modules of technique, and it still comes down to the same thing.

> It's all in the setup.

---

### WHAT ELSE THIS SAME MOVE BUILDS

You didn't learn a workflow tonight. You learned the setup that produces workflows. Same three steps every time: interview until a person shows up, write them down, correct them out loud.

Here's what that same move builds against the list you gave me:

| You said | The same move builds |
|---|---|
| *"We have no ATS... resumes in a career inbox, adding name to a spreadsheet"* | An intake that reads the inbox, pulls the fields, and writes the row. Your process, automated, not somebody's product. |
| *"Sourcing"* · *"Engaging passive talent"* | A sourcer with a Lens, a saved search brief, and a first-pass screen you edit instead of write |
| *"Time management with sourcing"* | The screen runs first, you review second. You stop being step one. |
| *"Responding to candidates"* · *"Maintaining contacts"* | A follow-up log that knows who's gone cold and drafts the next touch in your voice |
| *"balancing volume & quality responses"* | A rubric expert that scores against your bar, so volume stops costing quality |
| *"Interview questions and scorecards mapped to the JD"* | A scorecard built by interviewing your own hiring manager through the AI, then reused every req |
| *"Understanding how to reach HMs with the right info at the right time"* | Staged summaries instead of one wall of process at kickoff |
| *"Automation on various processes"* | Whichever one costs you the most Fridays. Pick that one first. |

**Pick exactly one.** Not the most interesting one, the most repeated one. The move only pays off on things you do again.

---

### THE ONE THING TO DO TOMORROW

Add ten words to your next request:

> *"Before you start, ask me questions that would help you do this better."*

Then six more when it answers:

> *"You're the expert. What would you do?"*

### THE ONE THING TO REMEMBER

I said at the top that your background doesn't matter, and I meant it. Nothing tonight needed a degree. It needed better questions.

> Vague in, garbage out. Clear in, magic out.
> **Anybody can cook.**

---

## STAY IN TOUCH

If you want help turning one of these into something that actually runs, or you want the brigade built for your team instead of just for you, that's the work I do.

> ### **hi@concept.kitchen**

Bring me the bottleneck. Not the tool question. The bottleneck.

**The Concept Kitchen**

---

## FACILITATOR NOTES

**The clock, 2 hours**

| Time | Block | Mode |
|---|---|---|
| 0:00 | Open. Their words, the bottleneck frame, the premise | Talk |
| 0:06 | **Module 0, the foundation. What an agent is, the six blocks, the four tiers** | Talk |
| 0:20 | **🔵 Breakout A, name your loop** | Groups |
| 0:28 | Module 1, the order, RECIPES off the table fast | Talk |
| 0:36 | Module 2, the conversation. Both directions, six types | Talk |
| 0:49 | **Ex 2.1, The Reverse Interview** | Hands |
| 1:00 | Break | |
| 1:05 | Module 3, the brigade, the Lens, the build sheet | Talk |
| 1:15 | **Ex 3.1 + 🔵 Breakout B, build one expert per table** | Groups |
| 1:31 | Module 4, the loop, correcting out loud | Talk |
| 1:36 | **Ex 4.1, Write Rule One** | Hands |
| 1:40 | **Module 5, the setup, install on their own machine** | Hands |
| 1:52 | **🔵 Breakout C, report back**, then the CTA | Groups |
| 2:00 | End | |

Talk is 68 minutes of 120. **Hands and groups are 47.** Break is 5.

**What got cut to fit Module 0 and the breakouts, and why.** The previous clock was already at exactly 120. Module 0 plus three breakouts is +41 minutes, so 41 had to come out.

- **Ex 1.1, Fix the Order, is cut.** Breakout A absorbs it. A table naming its own loops out loud is the same muscle as fixing a vague order, and it does double duty by setting up Breakouts B and C. Ex 1.1 was already named the most replaceable block on the old clock.
- **Ex 3.1 is not cut, it is converted.** It becomes a table build instead of a solo build, so Breakout B costs zero additional minutes. Same 16 minutes, more voices in it.
- **Every teach block is trimmed 1 to 3 minutes.** Module 2 from 15 to 13, Module 3 from 12 to 10, Module 4 from 8 to 5.
- **Module 5 keeps its full 12 and stays hands-on.** Non-negotiable. It's the only block that outlives the room.

**If the room is still running long,** the cut order is: Module 4's teach down to 3 (the rule template survives, the framing goes), then Breakout C from 8 to 5 by taking only half the tables. **Never Ex 3.1 and never Module 5.**

**Breakouts are a spine, not a spice.** A and B and C are the same tables, the same loop, carried the whole night. If you cut A, B and C lose their subject and you should cut all three. Do not run B alone.

**Groups of 3 or 4, formed once, at Breakout A.** Do not re-form them. Nineteen respondents means five or six tables. Say the number out loud when you form them so nobody ends up in a pair or a group of seven.

**The real teaching window is not the room booking.** People trickle in for the first fifteen and start looking at phones near the end. Assume the block is longer than the workshop and start the actual teach once bodies are seated, not on the minute.

**One live install path only.** Module 5 teaches the laptop path live because everyone has a laptop in front of them. The cloud path goes in the handout as take-home. Two live paths in a room this size means the room splits into people who are done and people who are stuck, and the stuck ones stop participating. If RJ wants both live, the block needs to grow, not compress.

**Nothing runs on my credentials.** No demo that depends on my accounts, my tokens, or my usage cap. Free and agnostic is the whole selling point, and a live demo running on a metered account I'm paying for contradicts the pitch in front of the room.

**The frame is "the setup makes you the bottleneck," never "you are the bottleneck."** Framed as *you are*, it's an accusation and the room closes. Framed as *the setup makes you*, it's a relief and the room leans in. Same fact, opposite outcome. Do not improvise this line.

**Two people on that survey are not in the main cluster.** One wrote *"not enough open roles or hard to define the hiring road-map"*, which is not a workflow problem. One wrote *"Finding a recruiter who will take my call"*, which means they're on the hiring side, not the recruiting side. If either of them is in the room, the tools menu leaves them with nothing. Have one line ready for each.

**The moment that always lands:** the Reverse Interview. People visibly change posture when the AI starts asking *them* questions. Protect Ex 2.1. If it's going well, let it run long and take the time out of Module 3's teach.

**Do not** oversell outcomes or promise income results. Position against gatekeeping, never against a competitor.

**Materials**
- The handout, one page, two sides. Front: the question sequence for Ex 3.1. Back: the build sheet as a worked example, plus the cloud install steps.
- RECIPES cheat sheet
- Their own laptop, their own AI account

---

*The Concept Kitchen. Anybody can cook.*

---

## Sources
- claim: title "Ask, Don't Micromanage" · subtitle "Build an agent for your recruiting workflow"
  source: title is RJ-confirmed (Telegram, Aug 20 2026), "dont change the name of the url. that's the one we want to use". Subtitle restates the Luma registration title in CONTEXT-INBOX.md:55-73, "Let's build an agent! For your recruiting workflow." Unified across deck, workshop, and notes per RJ's "unify" (Telegram, Aug 20 2026).
- claim: closing callback "It's all in the setup" at the end of Module 5
  source: retired deck title, repurposed not deleted. Was the slides.md H1 through Aug 20 06:48 AM. Moved to the end of Module 5 so it reads as a payoff line rather than a heading.
- claim: MODULE 0 exists at all · the foundation runs before any demo
  source: RJ-confirmed (Telegram voice note, Aug 20 2026), verbatim: "i do want to keep some foundation stuff which is there which is asking the questions... i like how he set up the foundation but we are not using his examples we're going to use my examples." Captured CONTEXT-INBOX.md:22-29. Second RJ message, Aug 20 2026: "what i care about is his explanation for an agent and the foundation he lays down, which is what I want incorporated into my workshop."
- claim: SCAFFOLDING of Module 0 (definition → building blocks → tiers) is borrowed from the reference transcript
  source: context/reference-transcript-FULL-VERBATIM.txt, structure only. Per RJ's explicit instruction the ORDER is borrowed and every EXAMPLE is replaced. The kitchen metaphor, the recruiting framing, the "what have I given it access to" turn, and all analogies are RJ's / this workshop's, not the source's.
- claim: "an agent is a language model that can use tools, running in a loop until it finishes a job"
  source: context/reference-transcript-FULL-VERBATIM.txt:11, near-verbatim. This is a definition, not an example, so it carries over intact per the scaffolding/examples split.
- claim: the model has no hands and no memory
  source: context/reference-transcript-FULL-VERBATIM.txt:83 ("it has no hands, it has no memory") and :189 ("the model itself has no memory on its own")
- claim: tools = the model emits a structured request, surrounding software executes it ("the hands")
  source: context/reference-transcript-FULL-VERBATIM.txt:50 (tool calling as "the first ability... to take actions in the real world") and :89 (tool calling as "the hands of the model")
- claim: the context window is a hard limit on what it can see at once ("the counter")
  source: context/reference-transcript-FULL-VERBATIM.txt:129-135
- claim: the system prompt is where the rules are set ("the house rules")
  source: context/reference-transcript-FULL-VERBATIM.txt:159-165
- claim: agent harness = someone else built the loop, you supply rules/files/tools
  source: context/reference-transcript-FULL-VERBATIM.txt:127, :296, :596
- claim: four tiers, no-code → low-code → agent harness → write it yourself
  source: context/reference-transcript-FULL-VERBATIM.txt:23, :284, :380, :596
- claim: "we are at tier 3 tonight"
  source: RJ-confirmed (Telegram voice note, Aug 20 2026), verbatim: "we are going to change the example and demos to have people set up on OpenClaw both on Google Cloud provider and on their laptop." OpenClaw is a tier-3 harness, so tier 3 is where the room sits by RJ's own tooling choice.
- claim: BREAKOUTS A, B, and C exist · the room works in groups
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "there's no break up into fucking groups like i asked for." Group work was an explicit ask; the three breakout placements (after Module 0, inside Module 3, and as the closing report-back) are Clawdia's structural proposal, NOT RJ-specified. RJ has not yet reviewed the placement or the timings.
- claim: the revised 120-minute clock (68 talk / 47 hands and groups / 5 break)
  source: computed from the module timings in this document, Aug 20 2026. Adding Module 0 (15) and three breakouts (26) cost +41 min, absorbed by cutting Ex 1.1, converting Ex 3.1 into Breakout B, and trimming M2 15→13, M3 12→10, M4 8→5. Module 5 was protected at its full 12. UNVERIFIED against a live run; no rehearsal has happened.
- claim: 19 recruiter bottlenecks quoted verbatim in THE PREMISE and the tools menu
  source: context/recruiter-bottlenecks.md:34-53 (RJ-supplied, Telegram drop 5, Aug 20 2026)
- claim: the "no ATS / career inbox / spreadsheet" respondent named the problem and got stuck
  source: context/recruiter-bottlenecks.md:49, verbatim, quoted not paraphrased
- claim: cluster shape — sourcing (6), time (4), comms (4), process (3), stakeholder (2), other-side (1)
  source: context/recruiter-bottlenecks.md:64-71 (counted from the raw list, not inferred)
- claim: two responses fall outside the main cluster (hiring roadmap, "recruiter who will take my call")
  source: context/recruiter-bottlenecks.md:86-93
- NOTE: no claim in this doc is drawn from what the survey OMITS. The survey asked one question
  ("What's your biggest recruiting challenge today?") and its silences measure nothing.
  See context/recruiter-bottlenecks.md:13-27 scope warning. CLAUDE.md Rule 57.
- claim: runtime is 2 hours, lecture stays short, added time is hands-on not more talk
  source: RJ-confirmed (Telegram voice note, drop 1, Aug 20 2026), verbatim: workshop grows to
  two hours, the lecture stays short, the added time is not more lecture
- claim: attendees set up the runtime themselves, on their own machine, not on RJ's bot
  source: RJ-confirmed (drop 1), verbatim: "it's not ready for deployment"
- claim: five agnosticism requirements (free, subscription auth, model-agnostic, OS-agnostic, tool-agnostic)
  source: RJ-confirmed (drop 8), verbatim: "since thsi shit is free and though, my set up keeps
  it free with claudse subwcription, i canteach people free stuff like if they have open ai or
  google gemini or claude this way it's agnostic especially if they have mac or windows."
- claim: OpenClaw and Google Cloud named explicitly in Module 5, two install paths
  source: RJ-confirmed (Telegram voice note, drop 1, Aug 20 2026), verbatim: "we are going to
  change the example and demos to have people set up on OpenClaw both on Google Cloud provider
  and on their laptop." Captured CONTEXT-INBOX.md:58-62 and :310-320.
- claim: path 1 (laptop) runs LIVE in the room, path 2 (Google Cloud) is demoed on screen + handout
  source: NOT RJ-specified. RJ said "both." This split is Clawdia's structural decision against
  the 12-minute Module 5 clock, surfaced to RJ Aug 20 2026 per CLAUDE.md Rule 46. Both paths are
  written out step by step in the handout. RJ has not yet approved the split.
- claim: tools menu placement at the END, framed as what the foundation builds
  source: RJ-confirmed (drop 10b), verbatim: "but towarsd the end as to, these are some tools
  you can build with with the foundation laid out today"
- claim: closing "build your own brigade" section + hi@concept.kitchen CTA for lead capture
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "i do want a section at the end for
  people who want to learn more about how to build their own brigade... they can reach me at
  hi@concept.kitchen CTA for me to get more leads at the end."
- claim: RECIPES 7-part table and "when to use what"
  source: projects/concept-kitchen/course/TCK-curriculum/resources/module-1-prompt/session-1.3-recipes-framework/recipes-cheatsheet.md
- claim: six question types and key prompts
  source: skills/brigade/SKILL.md:28-36
- claim: regular vs Socratic contrast table
  source: projects/concept-kitchen/course/TCK-curriculum/02-RIFF/06-socratic-method.md
- claim: type 4 IS the brigade, type 6 is the outsider, types 2+3 are CFO/skeptic
  source: skills/brigade/SKILL.md:38-42
- claim: persona defined by Lens = a quoted question; build sheet fields
  source: skills/brigade/SKILL.md Expert File Template (7 of 18 fields selected for scope)
- claim: a panel of Lenses disagreeing is the product; convergence is signal
  source: skills/brigade/RULES.md §1 WAR MODE (panel structure, non-obvious/contrast picks)
- claim: "maieutics" = midwifery, "aporia" = productive not-knowing
  source: standard classical-philosophy terminology (general knowledge, no specific stake)
- claim: "greeting gets a greeting" story
  source: CLAUDE.md Rule 48, burned Aug 14 2026, RJ's actual correction
- claim: "Vague in, garbage out. Clear in, magic out." / "Anybody can cook"
  source: CLAUDE.md TCK Brand Voice section
- claim: THE PREMISE background-agnostic line and the closing callback
  source: RJ-confirmed (Telegram, Aug 15 2026), verbatim: "i dont care what your back ground is.
  my whole goal is to make this relatable to help people think critically to get the most out of
  using the technology"
- claim: the manager move, asking the expert instead of telling it
  source: RJ-confirmed (Telegram, Aug 15 2026), verbatim: "me asking the questions to the agent
  instead of prompting or demanding or telling it what to do. It's the expert, what do you think."
- claim: "a good manager doesn't micromanage"
  source: RJ-confirmed (Telegram, Aug 15 2026), verbatim: "a better manager asks questions and
  doesnt micromanage"
- claim: the payoff framing, edit the expert's plan instead of writing your own
  source: RJ-confirmed (Telegram voice note, Aug 15 2026), verbatim: "a better plan and strategy
  and steps to take with expert guidance"
- NOTE: the Luma event link appears NOWHERE in this document, on any surface, by RJ's explicit
  instruction (Aug 20 2026). Its absence is correct, not a gap. See CONTEXT-INBOX.md banned block.
