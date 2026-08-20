# THE WORKSHOP
## Ask, Don't Micromanage
### Build an agent for your recruiting workflow

**Instructor:** RJ Moscardon, The Concept Kitchen
**Runtime:** 2 hours. More than half of it is you working, not me talking.
**Room:** Recruiters and talent professionals.
**Prereq:** None. Bring a laptop if you have one, plus any AI chat tool you already pay for or use free. No laptop, no problem. You'll pair up and build on a partner's screen, and you'll leave with the same handout to stand up your own at home.

---

## THE PREMISE

You are not here to learn AI.

You are here to get **curious** with it. That's the actual skill, and it's the one nobody teaches. Most people meet this technology, type one thing, get something mediocre back, and quietly decide it isn't for them. They weren't wrong about the answer. They just stopped asking.

Tonight is about not stopping.

I asked this room what's actually breaking. You said sourcing. Engaging passive talent. Responding to candidates. Time management. Interview questions and scorecards mapped to the JD. Getting the right info to a hiring manager at the right time. One of you has no ATS at all, just resumes landing in a career inbox and a name getting typed into a spreadsheet by hand.

Every single one of those is a loop. Check, decide, do, check again. That's the shape of a thing you can hand off.

**Your background doesn't matter here.** Technical, non-technical, never touched any of this. The whole goal is to make it relatable enough that you walk out thinking critically about what you're asking for. That's how you get the most out of the technology. Not the tool. The asking.

> **Anybody can cook.** You don't need a culinary degree to make a great meal. You need to know what you want, how to ask for it, and how to taste as you go.

---

## HOW TONIGHT RUNS

| # | Block | Time | What happens |
|---|---|---|---|
| 1 | **Who I am** | 5 min | Me, fast. |
| 2 | **Who you are** | 15 min | You introduce yourselves and name your bottleneck. |
| 3 | **The lecture** | 35 min | What an agent is and how to ask well. Plain words only. |
| 4 | **The demo** | 15 min | I build in front of you. |
| 5 | **Teams + break** | 5 min | You get grouped. Grab water. |
| 6 | **The setup** | 15 min | Everyone stands up their own agent. |
| 7 | **Build your bottleneck** | 25 min | Your table, your real problem. I come to you. |
| 8 | **Report back** | 5 min | One sentence per table. |

The back half is the point. The front half is so the back half works.

---

## LEARNING OUTCOMES

By the end, you can:

1. **Say what an agent actually is** in one sentence, without using a single word you'd have to look up
2. Tell whether a bad answer was the AI's fault or the question's fault, which it almost always is
3. **Manage by asking, not telling.** Treat it as the expert and ask what it thinks instead of dictating steps
4. Make it **interview you** instead of guessing at you
5. Build a reusable **expert** by asking questions until a person shows up
6. Turn a correction into a **permanent rule** so the same mistake never happens twice
7. Stand up a working setup on your own machine, with your own account, that outlives tonight
8. **Stay curious past the first mediocre answer**, which is the only one of these that actually compounds

---

# BLOCK 1 — WHO I AM
**Time:** 5 min | **Mode:** Talk

Short. Who I am, what The Concept Kitchen is, and why a cook is teaching a room of recruiters how to build software.

**The three things to land, then stop:**

1. **I'm not an engineer and I didn't get permission to build any of this.** That's the whole thesis. Anybody can cook.
2. **I build this stuff every day for my own work,** and everything I'm showing you tonight is something I actually run, not a slide I made for you.
3. **Nothing tonight runs on my account.** You walk out owning what you build.

**Then get off the stage.** The room is more interesting than I am and the next block proves it.

**Transition:** *"That's me. I'd rather know about you."*

---

# BLOCK 2 — WHO YOU ARE
### *"Talk to me before I talk at you."*
**Time:** 15 min | **Mode:** The room

This is not filler and it is not a warm-up. Three things are happening at once: people relax, I find out what's actually in the room, and **every person names the bottleneck they're going to build on in Block 7.** If this block runs well, the rest of the night has a subject.

**The four questions.** Put them on the screen and leave them up.

> 1. **What brought you here tonight?**
> 2. **Why agents? What made that the thing you got curious about?**
> 3. **Where are you with AI so far?** Never touched it, use it daily, somewhere in between. There is no wrong answer and I want the honest one.
> 4. **What's your bottleneck?** The thing you do over and over that you wish you didn't.

**How to run it**

- **Go around, but don't force it.** Anyone who'd rather pass, passes. Volunteers first, and the first two or three set the tone for the rest.
- **Write every bottleneck down where the room can see it.** Whiteboard, shared doc, screen. This list is the raw material for the whole back half.
- **When two people name the same bottleneck, say so out loud.** *"That's the third person tonight."* That's when the room stops feeling alone in it.
- **Do not fix anything yet.** The urge to solve it live is strong. Don't. The answer is the whole rest of the workshop and it lands harder if they wait.

**Facilitator:** the honest answer to question 3 is the one that matters most. If half the room has barely used any of this, slow the lecture down and lean on the kitchen metaphors. If most of them use it daily, skip fast through the basics and spend the recovered minutes on the build block.

**Transition:** *"Everything you just named is a loop. Let me show you what that means."*

---

# BLOCK 3 — THE LECTURE
**Time:** 35 min | **Mode:** Talk, with one hands-on beat

*Ground rule for this whole block: if a word needs a definition, it gets one immediately or it doesn't get said. No jargon for its own sake.*

---

## 3A — WHAT AN AGENT ACTUALLY IS
### *"A model that can use tools, running in a loop until the job is done."*
**Time:** 10 min | **Metaphor:** Knowing what's in the kitchen before you cook

Everybody is talking about agents. Almost nobody says what one actually **is**. That gap is why this feels like hype instead of something you could use on Monday.

You cannot ask well for a thing you cannot picture. So before any of the asking, here is the picture.

**First, the confusion to clear**

**A chatbot talks.** You type, it types back. That's the whole interaction. It cannot open your career inbox. It cannot save a resume to a folder. It cannot add a row to your spreadsheet or put a hold on a calendar. It generates words.

**An agent is that same thing with two pieces added:**

1. **It can take actions.** (tools)
2. **It keeps going on its own,** step after step, instead of stopping after one reply. (the loop)

> **The one-sentence version: an agent is a language model that can use tools, running in a loop until it finishes a job.**

That's it. Everything else is detail.

A chatbot answers a **question**. An agent is given a **goal** and goes and accomplishes it.

**The six pieces.** None of them require a degree to understand.

| The piece | What it actually is | In your kitchen |
|---|---|---|
| **The brain** | The model. All it does is predict text. It has no hands and no memory. | The cook. Skilled, and standing there with nothing. |
| **The hands** | Tools. The model doesn't reach into your inbox. It writes a request that says *"use the inbox,"* and the software around it does that and hands the result back. | The knives, the pans, the oven. |
| **The counter** | Everything it can see at one moment. It has a hard limit. | Counter space. You cannot put the whole pantry on it. |
| **The house rules** | Who it is, how it behaves, what it never does. Written once, loaded every time. | The rules of your kitchen, posted on the wall. |
| **The recipe box** | Files it can read. It has no memory between sessions. It remembers what's written down. | The binder of recipes you keep annotating. |
| **The loop** | Think, act, look at the result, decide again. Repeat until done. | Taste, adjust, taste again. |

**The one that surprises people: the model has no memory.** Not a little memory. None. Every single turn, the whole conversation gets handed back to it again. That's why **3E** matters so much. If a correction isn't written down somewhere it can read, the correction dies when you close the tab.

**And the one that unlocks the most: the model never actually touches anything.** It asks. The software around it acts. Which means the entire question of *"what can my agent do?"* is really the question **"what have I given it access to?"**

**Four ways to build one.** Same loop every time. The only variable is how much of it you assemble yourself.

| Tier | What you do | Who it's for |
|---|---|---|
| **1 — No code** | Fill out forms, drag blocks around. | Fastest start, tightest ceiling. |
| **2 — Low code** | Wire steps together, drop in a little logic. | Automations that outgrew tier 1. |
| **3 — Somebody else's loop** ← **tonight** | Somebody already built the loop. You bring the rules, the files, and the tools. | **This room.** |
| **4 — Write it yourself** | Build the loop in code, line by line. | Engineers with a reason to. |

**We are at tier 3 tonight,** and that's a deliberate choice, not a beginner's compromise. The loop is a solved problem. Nobody is paying you to rebuild it. What nobody can do for you is decide **what to ask it and what to give it access to.** That's the whole rest of this workshop.

**Take-home:** tier 1 and tier 2 tools are listed above if you want to compare. Tier 4 is not homework.

---

## 3B — THE ORDER
### *"Vague in, garbage out."*
**Time:** 5 min | **Metaphor:** Ordering at the counter

Walk into a kitchen and say "make me food." You'll get food. Technically correct, completely useless. That's not the kitchen failing. That's the order failing.

**AI doesn't give bad answers. It gives accurate answers to vague questions.**

Ask it to "write a job description" and you get a job description. Beige, interchangeable, and you'll rewrite it anyway. That round trip cost you fifteen minutes and produced nothing you didn't already have.

**RECIPES**, the recipe card for any request

| Letter | Element | Ask Yourself |
|--------|---------|--------------|
| **R** | Role | Who should it be? What expertise do I need? |
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

**Takeaway:** *You don't need a better AI. You need a better order.*

---

## 3C — THE CONVERSATION
### *"It's the expert. Ask it what it thinks."*
**Time:** 12 min, includes 5 min hands-on | **Metaphor:** Tasting as you cook

*This is the foundation. Everything after it is built on this.*

**The problem with 3B:** RECIPES assumes you know what you want. Most of the time you don't. Every prompting guide says "add more detail." **You cannot add detail you don't know is missing.**

The fix isn't a better instruction. It's a conversation. And a conversation goes **both directions.**

**DIRECTION 1 — You ask it.** *The manager move.*

Most people prompt like they're giving orders. Do this. Write that. Make it shorter.

You already know that's the wrong way to run a person. A good manager doesn't micromanage. He sets the goal and the standard, then asks the expert what *they* think, because they're the expert. You hired them for their judgment. Use it.

Same thing here.

| Instead of telling it | Ask it |
|---|---|
| "Write me a 3-step sourcing plan." | "You're the expert here. How would you approach this search?" |
| "Use this outreach structure." | "What structure would you use, and why?" |
| "Make this InMail shorter." | "What's not earning its place in here?" |
| "Do it this way." | "What would you do differently than what I just described?" |
| "Here's my plan, execute it." | "Here's my plan. What am I missing?" |

You still set the goal. You still hold the standard. But now the expert generates the plan and **you're editing instead of writing.** Less brain power, better result. You go from producing to directing.

**DIRECTION 2 — It asks you.** *The flip.*

Add this to the end of any request:

> **"Before you start, ask me questions that would help you do this better."**

That's the **S** in RECIPES, and it's worth more than the other six letters combined. It flips the direction. Now it pulls context out of your head that you never thought to say out loud. It will ask you the things you'd normally find out in week three.

**Put both together and you have a conversation.** You ask it what it thinks. It asks you what it needs. Nobody in that exchange is pretending to have all the answers.

**Six ways to ask a better question.** Once the conversation is going, these are the moves that make it go somewhere.

| # | Type | What it's for | What you say |
|---|------|---------|-----------|
| 1 | **Clarify** | Define the real problem | "What do I actually mean by [X]?" |
| 2 | **Test assumptions** | Surface hidden beliefs | "What am I assuming that might not be true?" |
| 3 | **Ask for proof** | Demand evidence | "How do I know this is true?" |
| 4 | **Flip the view** | Break your frame | "Argue the opposite position, seriously." |
| 5 | **Follow it forward** | Think three steps ahead | "If this works, then what?" |
| 6 | **Question the question** | Test the framing | "Is this even the right question?" |

**A note on discomfort:** the moment you realize you don't actually know something feels like failure. It's the point. It's the taste test that saves the dish. **That moment is curiosity starting, not competence ending.**

> ### 🔪 TRY IT NOW — The Reverse Interview
> **Time:** 5 min | **A screen open at every table. Share one if you need to.**
>
> Take the bottleneck you named in Block 2. Type this:
>
> > *"I'm trying to fix [your bottleneck]. Don't advise me yet. Ask me the five questions I should be asking myself."*
>
> Then answer one of them **out loud to the person next to you.**
>
> **Facilitator:** this is the moment that always lands. People visibly change posture when it starts asking *them* questions. If it's going well, let it breathe and take the minutes out of 3D.

**Takeaway:** *Stop giving orders. Start having a conversation.*

---

## 3D — STAFF THE KITCHEN
### *"A persona isn't a costume. A persona is a question."*
**Time:** 5 min | **Metaphor:** Hiring your brigade

You've asked good questions. But you're still getting one perspective: the default, averaged, safe voice. Generic in, generic out.

No real kitchen hires "a cook." A kitchen hires a **butcher**, a **saucier**, a **pastry chef**, an **expeditor**. Same ingredients, four completely different reads on what to do with them. That's a **brigade**.

**The move:** don't tell it to "act like an expert." **Ask it questions until a person shows up.** Then write that person down.

**What actually defines a person** is not the job title and not the bio. **It's the question they can't stop asking.**

- A copywriter asks: *"Does the first line earn the second?"*
- A CFO asks: *"What does this cost us if it works?"*
- A sourcer asks: *"Who already works somewhere this problem is solved?"*
- A chef asks: *"What's already in the fridge?"*

That question is the **Lens**. The Lens *is* the expert. Everything else is decoration.

**The build sheet.** Seven fields. You'll fill one out in Block 7.

| Field | What it is |
|-------|-----------|
| **Name + Emoji** | So you can call them fast |
| **Role** | One line |
| **Lens** | ⭐ **The question they always ask.** Write it in quotes. |
| **Expertise** | What they actually know |
| **Blind spots** | What they get wrong, so you know when to overrule them |
| **Anti-patterns** | What they must never do |
| **Defers to** | Who outranks them and when |

**Takeaway:** *You don't prompt a thing into existence. You interview one into existence.*

---

## 3E — CORRECT IT OUT LOUD
### *"Retrying re-rolls the dice. Correcting writes a rule."*
**Time:** 3 min | **Metaphor:** The recipe card you keep annotating

It gets it wrong. Almost everyone does the same thing: retry with different words. That's re-rolling the dice. Nothing was learned. It'll happen again next week.

Don't retry. **Say why it was wrong.** Then make the correction permanent.

Not: *"no, try again"*
But: *"That was wrong because ___. Going forward, when I ___, you should ___. Write that down."*

**Real example, mine.** I texted my AI one word: "Hi." I was standing at the stove, just saying hello. It came back with a task list and three things I hadn't done yet.

I told it: *I said hello. That's all that was.*

So we wrote a rule: **greeting gets a greeting.** If he says hi, say hi back. The rest can wait.

It has never done it again. Not because the model improved. Because **the correction became permanent.**

Every correction becomes a rule. Every rule is a mistake you refuse to have twice. Do that for a year and you don't have a prompt. You have a system with a memory.

**And this is exactly why Block 6 exists.** A chat window can't keep a rule. A setup can.

**Takeaway:** *Prompting is a transaction. Correcting is a relationship.*

**Transition:** *"That's all the theory you get. Let me show you the real thing."*

---

# BLOCK 4 — THE DEMO
### *"Watch me do it, badly, in front of you."*
**Time:** 15 min | **Mode:** Watch

**This block is RJ's call.** What follows is scaffolding, not a script. The content flexes to whatever's most alive that night. What can't flex is the **job** the block has to do.

**What this block must accomplish**

1. **Make it concrete.** Everything before this was words. This is the thing moving.
2. **Show the loop actually looping,** so the definition from 3A stops being abstract.
3. **Show a correction landing,** so 3E stops being a nice idea.
4. **Make them want to try it.** That's the real deliverable. Curiosity, not comprehension.

**The three beats, roughly 5 minutes each**

| Beat | What it shows | The point |
|---|---|---|
| **1. Scrape something with Apify** | A real tool doing a real job. Pull data off a page, live. | *This is "the hands." The model asked, the software acted.* |
| **2. How I actually use Clawdia** | My own setup, my own work, unedited. | *This isn't a demo account. It's a Tuesday.* |
| **3. My agent teams** | Multiple experts, each with their own Lens, on one problem. | *This is 3D at full size. You'll build one of these tonight.* |

**Say this while it runs, because it's the whole lesson:**

> *"Notice I'm not typing instructions. I'm asking, then reading, then correcting. That's the loop. That's the entire job."*

**When it breaks, do not hide it.** Something will misfire. Narrate it out loud and correct it in front of them. A live correction is worth more than a clean demo, because the clean one teaches them the tool and the broken one teaches them the **move**.

**Facilitator guardrails**
- **Do not run anything on a metered account** in front of the room. Free and agnostic is the pitch; a token meter running on screen contradicts it.
- **No credential on screen.** Check what's visible before you share.
- **Hard stop at 15 minutes.** This block is the most fun to run long and the most expensive to run long, because it eats the build block.

**Transition:** *"Your turn. Find your people."*

---

# BLOCK 5 — TEAMS + BREAK
**Time:** 5 min | **Mode:** Move

**Form the teams now and do not re-form them.** These tables carry the rest of the night: setup together, build together, report out together.

- **Groups of 3 or 4.** Say the number out loud so nobody ends up in a pair or a group of seven.
- **Group by bottleneck where you can.** You wrote them all down in Block 2. Put the sourcing people together, the follow-up people together. A shared problem makes Block 7 immediately productive.
- **Mix experience levels on purpose.** Every table should have at least one person who answered "I use it daily" in Block 2. That person is the table's first line of support during setup.
- **Make sure every table has at least two laptops.** Not everyone brought one and that was never a requirement. Balance it here, quietly, while people are moving. That's what makes path 3 work in the next block.
- **Grab water. Sit back down.** Five minutes, not ten.

**Facilitator:** the person who says "I'll just work alone" gets one warm push and then gets to work alone. Don't fight it in front of the room.

**Facilitator, the quiet one:** count laptops per table as they settle. Do not ask the room who's without one. If a table is short, move a person, not a machine, and say nothing about why.

---

# BLOCK 6 — THE SETUP
### *"Get it off the chat window and onto your machine."*
**Time:** 15 min | **Mode:** Hands on keyboards | **Metaphor:** Your own kitchen, not a rented one

Everything so far works in any chat box. This part makes it persist.

**A chat window forgets you. A setup remembers you.** The difference is where the files live.

**What we're standing up: OpenClaw**
An open agent runtime, signed in with an account you already have. It reads a folder of files you control, which means your Lenses, your rules, and your corrections load every time instead of getting re-explained every time.

**Why OpenClaw specifically**
- **The software is free.** You're not buying OpenClaw, and nothing here runs on my account.
- **It asks for one key, and Google gives one away.** [aistudio.google.com/apikey](https://aistudio.google.com/apikey), sign in with any Google account, click Create API key. No credit card. Free tier is more than enough to learn on. If you already have an OpenAI or Anthropic key, use that instead.
- **It's model-agnostic.** OpenAI, Google Gemini, or Claude. Bring whatever you already have. **You do not buy anything new tonight.**
- **It's OS-agnostic.** Mac or Windows. Both work in this room.
- **Nothing here runs on my account.** You walk out owning it.

**Three ways in, same steps**

| | Path | When | Why this one |
|---|---|---|---|
| **1** | **Your own laptop** | In the room, tonight | Fastest to a working setup. You leave with it running. |
| **2** | **Google Cloud** | Walked on screen, finish at home | Runs when your laptop is closed. Same steps, different machine. |
| **3** | **No laptop tonight** | Pair up in the room, finish at home | You still build. You drive your partner's screen for your own bottleneck, and you take the same handout home. |

All three paths use the same commands, written out step by step below. We do **path 1 live** because 15 minutes gets a whole room to a working laptop install and it does not get a whole room through a cloud console. I demo **path 2 on screen** during the same block so you have seen every step before you try it.

**Path 3 gets said out loud, early, before anyone has to admit it.** Not everyone was going to bring a laptop and that was never a requirement. If you didn't bring one, you are not spectating for fifteen minutes. Pair with someone at your table, drive their screen for *your* bottleneck, and stand up your own tonight from the commands on this page. The person sharing the laptop gets the better deal anyway, because watching someone else fumble through your problem is how you learn where it breaks.

---

## 🔪 THE INSTALL — copy these exactly

**Website:** **[openclaw.ai](https://openclaw.ai/)** · **Docs:** [docs.openclaw.ai](https://docs.openclaw.ai/)

You do not need to understand these commands. You need to paste them. Understanding comes after it's running.

### 🍎 Mac

**1. Open Terminal.** Press `⌘ + Space`, type `terminal`, hit Enter. Black window. That's it.

**2. Paste this and hit Enter:**

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

**3. When it finishes, paste this:**

```
openclaw onboard --install-daemon
```

That opens a setup wizard. Follow it. It asks which AI you want to use and for a key. See **"The key"** below.

**4. Check it worked:**

```
openclaw doctor
```

### 🪟 Windows

**Easiest path, no command line at all:** download the desktop installer, double-click it, follow the wizard.

- **[OpenClaw Companion for Windows (x64)](https://github.com/openclaw/openclaw-windows-node/releases/latest/download/OpenClawCompanion-Setup-x64.exe)** ← most laptops
- **[Windows on ARM (arm64)](https://github.com/openclaw/openclaw-windows-node/releases/latest/download/OpenClawCompanion-Setup-arm64.exe)** ← Surface Pro X and similar

**If you'd rather use the command line:**

**1. Open PowerShell.** Press the Windows key, type `powershell`, hit Enter.

**2. Paste this and hit Enter:**

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

**3. Then:**

```
openclaw onboard --install-daemon
```

**4. Check it worked:**

```
openclaw --version
openclaw doctor
```

> **You may have heard Windows needs WSL2.** It doesn't, not for tonight. WSL2 is the more complete path and you can move to it later. Native works fine for what we're doing, and it installs in one command instead of one evening.

### The key

Onboarding asks for one key. **Google gives them away free**, and that's the path we're taking tonight.

Go to **[aistudio.google.com/apikey](https://aistudio.google.com/apikey)** → sign in with any Google account → click **Create API key** → copy it → paste it into the wizard. **No credit card.** The free tier is more than enough to learn on.

If you already have an OpenAI or Anthropic key, use that instead. Same wizard, same step.

> **If the words "API key" made you tense up, ignore them.** It's a long password Google generates for you in about thirty seconds. You copy it once and never think about it again.

### Both machines, once it's running

```
openclaw dashboard
```

That opens a control panel in your browser at `http://127.0.0.1:18789/`. **This is your kitchen.** Everything you built tonight lives here.

### If something breaks

`openclaw doctor` tells you what's wrong in plain English. Run it first. Then raise a hand.

---

**The one rule for this block:** if you get stuck, **raise a hand and keep going to the next step.** Do not sit stuck and quiet. The person next to you probably hit the same wall ninety seconds ago, and your table has at least one person who's done this kind of thing before.

**Facilitator:** work the room by table, not by person. Fixing one laptop takes three minutes; telling a table what the error means fixes four laptops at once. **Seed the pairs during BLOCK 5 when you form teams, not at the top of this block.** Asking "who doesn't have a laptop?" in front of the room at 6:40 puts someone on the spot. Know it before you need it.

**Transition:** *"You've got a kitchen. Let's cook something you actually need."*

---

# BLOCK 7 — BUILD YOUR BOTTLENECK
### *"Your table. Your real problem. I come to you."*
**Time:** 25 min | **Mode:** Teams, hands on keyboards

This is the block the whole night was built for.

**Pick one bottleneck per table.** Use the ones you named in Block 2. Not the most interesting one, **the most repeated one.** The move only pays off on things you do again.

**The sequence.** Do it together, out loud, at the table.

1. **Say the loop out loud.** *"Check, decide, do, check again."* Name each step. If you can't say the steps, you don't have a loop yet, you have a wish.
2. **Ask: "Who should be in the room to help me build this?"** See who shows up.
3. **Interview whoever shows up.** Use the six ways to ask from 3C. **Do not take the first answer.** The first answer is always the averaged one.
4. **Land on their one question.** The Lens. The thing this expert asks about everything it sees.
5. **Fill the build sheet and save it to a file** in the setup you just stood up. **That file is the asset, not the chat.**
6. **Run it on something real,** then **correct it out loud** and watch the correction stick.

**You are not finishing the thing tonight. You're building the setup that builds it.**

Before you stop, answer this one:

> ### **What's the one question this thing answers for me, every time?**

**Why you're doing this as a table, not alone.** The disagreement inside the table is the point. When two recruiters at one table define "qualified" differently, that's the exact ambiguity the Lens has to settle. You'd never have found it working alone, because alone you'd have just assumed your own definition.

**Facilitator: circulate the whole 25 minutes. Do not stand at the front.**
- **Do not touch anyone's keyboard.** Ask them what they want it to do. You're modeling the move while you help.
- **When a table is stuck on tooling,** solve it fast and get back to the thinking.
- **When a table is stuck on the problem,** that's not stuck, that's the exercise. Ask them a question instead of giving them an answer.
- **At 20 minutes, call it:** *"Five left. Make sure your Lens is written down somewhere that isn't the chat."*

**If a table has no working laptop:** *"Do it out loud. One of you plays the expert, the rest interview them. You'll get the same answer, you'll just get it faster."* The interview is the exercise. The laptop is a convenience.

---

# BLOCK 8 — REPORT BACK + CLOSE
**Time:** 5 min | **Mode:** The room

**One sentence per table, out loud, to everybody.**

> *"Our loop was **\_\_\_\_**. Our expert asks **\_\_\_\_**."*

Two blanks. No preamble.

**Why this is the last thing we do:** you're about to hear six or seven versions of your own job, described by people who sit in different seats than you. Some table is going to name a loop you didn't know was a loop. Take that one home too.

**Facilitator:** cut anyone who goes past two sentences, warmly. The constraint is what makes the room hear all of them.

---

### The arc

1. **Know what it is** → A model, tools, a loop. No magic.
2. **Order better** → RECIPES
3. **Have the conversation** → Ask the expert what it thinks. Let it ask you what it needs.
4. **Staff the kitchen** → Experts built from questions
5. **Keep the notes** → Correcting out loud
6. **Own the room** → A setup on your machine that remembers all five

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

**Say this out loud when the folder exists.** Everything before Block 6 was about asking better in the moment. The setup is what makes the moment better before you open your mouth.

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

**Pick exactly one.** Not the most interesting one, the most repeated one.

---

### THE ONE THING TO DO TOMORROW

Add ten words to your next request:

> *"Before you start, ask me questions that would help you do this better."*

Then six more when it answers:

> *"You're the expert. What would you do?"*

### THE ONE THING TO REMEMBER

I said at the top that you're not here to learn AI, you're here to get curious with it. Nothing tonight needed a degree. It needed better questions, and the willingness to keep asking after the first answer was mediocre.

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
| 0:00 | **1. Who I am** | Talk |
| 0:05 | **2. Who you are.** Icebreaker, four questions, capture every bottleneck | Room |
| 0:20 | **3A. What an agent is.** Six pieces, four tiers | Talk |
| 0:30 | **3B. The order.** RECIPES off the table fast | Talk |
| 0:35 | **3C. The conversation.** Both directions, six ways to ask | Talk |
| 0:42 | **🔪 Try it now, the Reverse Interview** | Hands |
| 0:47 | **3D. Staff the kitchen.** The Lens, the build sheet | Talk |
| 0:52 | **3E. Correct it out loud** | Talk |
| 0:55 | **4. The demo.** Scrape, my setup, the agent teams | Watch |
| 1:10 | **5. Teams + break.** Form once, group by bottleneck | Move |
| 1:15 | **6. The setup.** OpenClaw on their own machine | Hands |
| 1:30 | **7. Build your bottleneck.** Tables build, RJ circulates | Teams |
| 1:55 | **8. Report back**, then the CTA | Room |
| 2:00 | End | |

**Talk is 50 minutes of 120. Hands, teams, and the room are 65.** Break is inside block 5.

**The ratio is the point.** The previous version was 68 talk / 47 hands. This one inverts it. If a block has to grow, it grows out of the talk column, never out of blocks 6 or 7.

**If the room is running long, cut in this order:** 3E down to 2 minutes (the correction template survives, the story goes), then 3D down to 3 (the build sheet survives, the brigade examples go), then the demo from 15 to 10 by dropping beat 3. **Never blocks 6 or 7.** Those are the only ones that outlive the room.

**If the room is running short,** give the minutes to block 7. It absorbs any amount.

**Block 2 is load-bearing, not warm-up.** Every bottleneck named there becomes the subject of block 7. If you shortcut the icebreaker, block 7 has no material and tables sit there inventing a problem instead of solving one. Capture the bottlenecks where the room can see them and leave them up all night.

**No jargon.** If a word needs a definition, define it on the spot or don't say it. The room is recruiters, not engineers. "Somebody else's loop" beats "agent harness." "The counter" beats "context window." "House rules" beats "system prompt." The kitchen words are not decoration, they're the translation layer.

**The real goal is curiosity, not coverage.** If a block is going well and people are asking questions, let it run and take the time from the talk column. A room that leaves curious will build on Saturday. A room that leaves informed will not.

**Groups of 3 or 4, formed once, at block 5.** Do not re-form them. Nineteen respondents means five or six tables. Say the number out loud when you form them.

**The real teaching window is not the room booking.** People trickle in for the first fifteen and start looking at phones near the end. Assume the block is longer than the workshop and start the actual teach once bodies are seated, not on the minute. Block 1 and block 2 absorb stragglers gracefully; the lecture does not.

**One live install path only.** Block 6 teaches the laptop path live because it's the one that gets a whole room to a working setup in fifteen minutes. The cloud path goes on screen and stays on this page as take-home. Two live paths in a room this size means the room splits into people who are done and people who are stuck, and the stuck ones stop participating. **Path 3 is not a third live path, it's pairing.** Anyone without a laptop drives a partner's screen for their own bottleneck, so they're still building, not watching.

**Nothing runs on my credentials.** No demo that depends on my accounts, my tokens, or my usage cap. Free and agnostic is the whole selling point, and a live demo running on a metered account contradicts the pitch in front of the room.

**The frame is "the setup makes you the bottleneck," never "you are the bottleneck."** Framed as *you are*, it's an accusation and the room closes. Framed as *the setup makes you*, it's a relief and the room leans in. Same fact, opposite outcome. Do not improvise this line.

**Two people on that survey are not in the main cluster.** One wrote *"not enough open roles or hard to define the hiring road-map"*, which is not a workflow problem. One wrote *"Finding a recruiter who will take my call"*, which means they're on the hiring side. Have one line ready for each, and make sure both end up on a table in block 5 rather than working alone.

**The moment that always lands:** the Reverse Interview in 3C. People visibly change posture when it starts asking *them* questions. Protect it. If it's going well, let it run and take the time out of 3D.

**Do not** oversell outcomes or promise income results. Position against gatekeeping, never against a competitor.

**Materials**
- The handout, one page, two sides. Front: the question sequence for block 7. Back: the build sheet as a worked example, plus the cloud install steps.
- RECIPES cheat sheet
- Somewhere visible to write every bottleneck from block 2
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
- claim: agnosticism requirements (free software, model-agnostic, OS-agnostic, tool-agnostic)
  source: RJ-confirmed (drop 8), verbatim: "since thsi shit is free and though, my set up keeps
  it free with claudse subwcription, i canteach people free stuff like if they have open ai or
  google gemini or claude this way it's agnostic especially if they have mac or windows."
- ~~claim: "OpenClaw runs on a subscription you may already pay for, not per-token billing"~~
  **RETIRED Aug 20 2026. BANNED, do not re-source.** The "claudse subwcription" in drop 8 was RJ
  describing HIS OWN auth, not how OpenClaw works for attendees. docs.openclaw.ai documents API key
  or a local model only; no subscription sign-in exists. Corrected claim below.
- claim: onboarding requires an API key; the free path is a Google AI Studio key
  source: docs.openclaw.ai (onboarding), + RJ-confirmed (Telegram, Aug 20 2026), verbatim:
  "ok we dont want to scare them off. but it requires an API key. And Gemini is potentially free."
- claim: the eight-block run of show (intro, icebreaker, lecture, demo, teams, setup, build, report back)
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "then we'll go from intro what I'm about to
  asking them questions in icebreaker to the workshop lecture to the demo to set up or actually them
  breaking up into groups and then into set up. Then after set up they go into their bottlenecks and
  they go into building." Captured CONTEXT-INBOX.md.
- claim: the four icebreaker questions in BLOCK 2
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "what brought them here why are they
  interested in agents where their capability is at with ai so far" plus "people are gonna talk about
  their bottlenecks."
- claim: BLOCK 4 demo covers an Apify scrape, RJ's own Clawdia setup, and his agent teams
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "we're going to go through the demo using
  appify of how to scrape something or something I decide we're definitely going to show them how to
  use Claudia or how I use Claudia in the demo and then maybe even show them how I have my agents who
  my agent teams are."
- claim: BLOCK 4 is scaffolded, not scripted
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "but I don't know that demo portion is up to me."
- claim: the stated goal is curiosity, not coverage (THE PREMISE opener, outcome 8, facilitator note)
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "All I really care about is for them not to
  learn AI so much as they learn how to be curious with AI. It more important that I teach them how to
  be curious and want to do this shit than it is for me to like tell them this is this this is that."
- claim: jargon stripped (maieutics, aporia, Socratic, agent harness, system prompt, context window removed)
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "I'm the concept kitchen. We teach this in a
  relatable way. So I don't want to bog them down with jargon. I want to get them to building."
- claim: talk drops to 50 minutes of 120, hands/teams/room rise to 65
  source: Clawdia's structural implementation of "I want to get them to building" (RJ, Telegram,
  Aug 20 2026). The ratio itself is a Clawdia decision; the direction is RJ's.
- claim: Breakouts A, B, and C no longer exist as separate named exercises
  source: Clawdia's structural decision. Their functions were absorbed: A (name your loop) into the
  BLOCK 2 icebreaker RJ asked for, B (build one expert) into BLOCK 7 on their real bottleneck, C into
  BLOCK 8. No content was deleted; it was relocated to match RJ's stated sequence.
- claim: alignment with Mabel's plan
  source: ~~UNCONFIRMED. Mabel's syllabus and event flow have never been received.~~ RETIRED Aug 20
  2026 09:20 — this was wrong and was repeated to RJ three times. Mabel's material IS on disk:
  (1) syllabus at ~/clawdia/memory/drafts/workshop-2026-08-16-syllabus.md (272 lines, four modules);
  (2) her notes in the shared calendar event "[HOLD] Talent AI Lounge Workshop" — "RJ to share
  1) framework, 2) a blurb", "Mabel to secure spot at Hanwha (via Asako)", "Guests to bring a
  personal laptop (if they have one)"; (3) her own Luma description naming five recruiting
  categories: sourcing, candidate outreach, interview preparation, research, recruiting operations.
  Answer to "Does that sound in line with what Mabel wants?" is MOSTLY YES with three gaps —
  see CONTEXT-INBOX.md § "Mabel diff". Only the partner's REVISED flow is still outstanding.

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

- claim: the demo scrapes with Apify
  source: RJ run-of-show message, Aug 20 2026 verbatim: "we're going to go through the demo using
  appify of how to scrape something or something I decide". Tool named because he named it.
- claim: the demo shows Clawdia
  source: RJ run-of-show message, Aug 20 2026 verbatim: "we're definitely going to show them how to
  use Claudia or how I use Claudia in the demo".
