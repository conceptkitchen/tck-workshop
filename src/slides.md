# THE DECK
## Ask, Don't Micromanage
### Build an agent for your recruiting workflow

**AI Workshop, Thursday Aug 20, 2026 | RJ Moscardon, The Concept Kitchen**
**Room: recruiters and talent professionals.**

<section class="titlecard">
  <img src="/assets/flyer-lets-build-an-agent.jpg" alt="Let's Build an Agent. A hands-on workshop to build a personalized agent for your recruiting workflow. The Concept Kitchen x Talent AI Lounge x Apify.">
</section>

<section class="titlecard">
  <img class="titlecard-mark" src="/assets/talent-ai-lounge.jpg" alt="Talent AI Lounge">
  <p class="titlecard-line">Tonight's host community.</p>
</section>

<section class="titlecard">
  <img class="titlecard-mark" src="/assets/hanwha-ai-center.jpg" alt="Hanwha Artificial Intelligence Center">
  <p class="titlecard-line">Where we are. 300 Grant Ave, Suite 500, San Francisco.</p>
</section>

<section class="titlecard">
  <p class="titlecard-hold-mark">APIFY</p>
  <p class="titlecard-line">The tool we run the live demo on.</p>
</section>

<section class="titlecard wificard">
  <p class="wificard-head">Get on the network</p>
  <dl class="wificard-creds">
    <dt>Network</dt>
    <dd>HAC Guest</dd>
    <dt>Password</dt>
    <dd>HACGUEST5F</dd>
  </dl>
</section>

---

## SLIDE 1 · THE HOOK

> # Think about the best manager you ever had.
>
> ### They didn't tell you which keys to press.
>
> ## They asked you one question that made you better at your own job.

**Speaker note:**

*Flat. No hype. Let them picture the person. Don't open on your resume.*

- "Everybody's got one. The manager who made you better without ever telling you what to do."
- "They didn't hand you a checklist. They asked you one question, and you figured out the rest yourself. And you were better at your job after."
- "That's the whole skill of working with AI. That's it. And almost nobody does it."
- **Say this early. Give the room permission before anybody checks out:**
  - "I don't care what your background is. Technical, non-technical, never touched any of this. Doesn't matter here."
  - "My whole goal today is to make this relatable enough that you walk out thinking critically about what you're asking for. That's how you get the most out of the technology."
  - "Not the tool. The asking."
- **The three moves, so they know where I'm taking them:**
  - "One. Ask questions instead of giving orders."
  - "Two. Let the expert help you build the expert."
  - "Three. Once you've got a few of them, put them in a room and let them plan the thing before you touch it."
- "That's the talk."

**Transition:** "So why doesn't it work that way for most of us?"

---

## SLIDE 2 · THE PROBLEM

> # Most of us treat AI like a vending machine.
>
> ### Put in a request. Get a product.
>
> ## Bad product? Every guide says the same thing: add more detail.
>
> **That's micromanaging.**

**Speaker note:**

*Name the feeling. Don't explain it. Everyone here has done this.*

- "We treat it like a vending machine. Put in a request, get a product. Didn't like the product? Put in a longer request."
- "Every prompt guide says the same thing. Be more specific. Add more detail. Add more constraints."
- "So we write a paragraph. Then we write a page. And it's still not what we wanted."
- **The punchline:** "Here's the problem with that. A longer order caps the answer at whatever I already knew to ask for. If I don't know what I'm missing, more words won't find it."
- "In a kitchen we'd call that standing over someone's shoulder telling them how to hold the knife. That's micromanaging."

**Transition:** "Let me show you what that actually sounds like."

---

## SLIDE 3 · THE KITCHEN

> # "Make me food."
>
> ## You'll get food.
>
> ### Technically correct. Completely useless.
>
> **That's not the kitchen failing. That's the order failing.**

**Speaker note:**

*Build this one line at a time. The room already knows this feeling.*

- "Walk into a kitchen and say make me food. You'll get food. Technically correct. Completely useless."
- "That's not the kitchen failing. That's the order failing."
- "AI doesn't really give bad answers. It gives accurate answers to vague questions. Which feels the same from where you're sitting, but it's a completely different problem to fix."
- **The turn:** "And the fix isn't a longer order. The fix is letting the kitchen ask me questions before it starts cooking."
- "Because a good cook asks. How many people? Anybody allergic? Are we eating in ten minutes or two hours?"

**Transition:** "So the fix is learning to ask. We'll get there. But first I owe you an answer to a question this whole industry keeps skipping."

---
## SLIDE 4 · WHO YOU ARE

> # Before I teach you anything, I want to hear you.

**1.** What brought you here tonight?

**2.** Why agents? What made that the thing you got curious about?

**3.** Where are you with AI so far? *Never touched it, use it daily, somewhere in between.*

**4.** What's your bottleneck? *The thing you do over and over that you wish you didn't.*

**Speaker note:**

*Slide stays up the whole 15 minutes. Capture every bottleneck where the room can see it. That list is the raw material for the back half of the night.*

- "I've talked enough. I want to know who's in the room."
- Take five or six out loud, not everyone. Keep it moving.
- "Where are you with AI" gets the honest answer only if you go first. Say the unglamorous version of your own start.
- **Write the bottlenecks on the board.** Whiteboard, easel pad, shared doc on screen. They need to see their own words later.
- **Do not fix anything yet.** Someone will describe a problem you could solve in one sentence. Let it sit. They'll build it themselves in two hours and it will mean more.

**Transition:** "Everything you just said is a loop. Let's talk about what actually runs one."


---

## SLIDE 5 · WHAT AN AGENT ACTUALLY IS

> # A chatbot talks.
>
> ## An agent does.
>
> ### A model that can use tools, running in a loop until the job is done.

**Speaker note:**

*This is the slide that decides whether the rest of the night lands. Say the one-sentence version twice.*

- "Everybody in your feed is saying agent. Almost nobody says what one is. That gap is why this feels like hype instead of something you could use Monday."
- "A chatbot talks. You type, it types back. That's the whole thing. It cannot open your career inbox. It cannot save a resume to a folder. It cannot put a hold on a calendar. It generates words."
- "An agent is that same model with two things added. One, it can take actions. Two, it keeps going on its own instead of stopping after one reply."
- **Say it slowly, then say it again:** "An agent is a language model that can use tools, running in a loop until it finishes a job."
- **The line to leave them with:** "A chatbot answers a question. An agent is given a goal."
- "That's it. Everything after this is detail."

**Transition:** "So what's inside one? Six pieces. None of them need a degree."

---

## SLIDE 6 · THE SIX PIECES

> # It's a kitchen.

| The piece | What it is | In your kitchen |
|---|---|---|
| **The brain** | The model. Predicts text. No hands, no memory. | The cook, standing there with nothing. |
| **The hands** | Tools. It asks for one, the software runs it. | The knives, the pans, the oven. |
| **The counter** | The context window. All it can see right now. | Counter space. It runs out. |
| **The house rules** | The system prompt. Who it is, what it never does. | The rules posted on the wall. |
| **The recipe box** | Files it can read. Its only memory. | The binder you keep annotating. |
| **The loop** | Think, act, look, decide again. | Taste, adjust, taste again. |

**Speaker note:**

*Do not read all six. Point at the table, then land the two that change how they think.*

- "Six pieces. The table's in your handout. I'm going to say two things about it."
- **One, finger on the brain:** "The model has no memory. Not a little. None. Every single turn, the whole conversation gets handed back to it from scratch."
  - "That's why Module 4 matters. If you correct it and that correction isn't written down somewhere it can read, the correction dies when you close the tab."
- **Two, finger on the hands:** "The model never actually touches anything. It writes a request that says use the inbox tool, and the software around it does that and hands back the result."
  - **The unlock:** "Which means what can my agent do is really the question what have I given it access to. That's not a technical question. That's a scoping question. You already do that when you onboard someone."

**Transition:** "Now, there are four different ways to build one of these, and I want you to know where tonight sits."

---

## SLIDE 7 · FOUR WAYS TO BUILD ONE

> # Same loop every time.
>
> ## The only question is how much you assemble yourself.

| Tier | You do | Who it's for |
|---|---|---|
| **1 · No code** | Fill out forms, drag blocks. | Fastest start, tightest ceiling. |
| **2 · Low code** | Wire steps, drop in logic. | Automations that outgrew tier 1. |
| **3 · Agent harness** | Someone built the loop. You bring the rules, files, and tools. | **This room. Tonight.** |
| **4 · Write it yourself** | Build the loop in code. | Engineers with a reason to. |

**Speaker note:**

*The point of this slide is permission. They need to hear that tier 3 is a choice, not a shortcut.*

- "Four tiers. Same loop underneath all of them. The only variable is how much you build yourself."
- **Point at tier 3:** "We're here tonight. And I want to be clear that's a deliberate choice, not a beginner's compromise."
- "The loop is a solved problem. Nobody is paying you to rebuild it."
- **The turn:** "What nobody can do for you is decide what to ask it and what to give it access to. That's the whole rest of tonight."
- "Tier 1 and 2 tools are on the workshop page if you want to compare. Tier 4 is not homework."

**Transition:** "Turn your chairs. First one's on you."

---

## SLIDE 8 · THE RECIPE CARD

> # RECIPES

| | | |
|---|---|---|
| **R** | Role | Who should it be? |
| **E** | Examples | What does "good" look like? |
| **C** | Context | What does it need for THIS task? |
| **I** | Instructions | What exactly do I want? |
| **P** | Parameters | Constraints? Format? Length? |
| **E** | Energy | What tone? |
| **S** | Sanity-check | Should it ask ME questions first? |

**Speaker note:**

*Do NOT teach all seven. You'll lose the room. Point at it, land the S, move.*

- "This is the recipe card. RECIPES. You'll get it as a handout, so don't write it down."
- "Seven parts, but I'm only going to say one thing about it today."
- **Finger on the S:** "Sanity-check. Should it ask ME questions first? That one is worth more than the other six combined."
- **Why this slide is here, and this is the honest part:**
  - "I didn't come up with this because I wanted a better prompt. I came up with it because I kept getting stuff back that wasn't what I meant."
  - "Once I started thinking about structure, what I was really doing was learning how to manage what I ask for clearly. That's a management skill. It's not a tech skill."
  - "And then it went one step further. If I can be clear about one task, I can plan ahead for all of them. That's the thing that turned into the brigade. My team of experts."
- "So the framework isn't the point. The framework is what got me thinking like a manager instead of like a guy typing into a box."

**Transition:** "Let me show you what that S actually looks like in a real conversation."

---

## SLIDE 9 · THE ASK

> **Me:** Here's the goal. Here's what good looks like.
>
> **Me:** *You're the expert. What do you think you should do?*
>
> **It:** *Before I answer, what do you mean by "good"?*
>
> **Me:** *Fair. Here's what I mean.*

> ## You don't get what you want by asking harder.
> ## You get it by setting up better.

> ### **Now I'm editing a plan. Not writing one.**

**Speaker note:**

*One line at a time. HOLD after the third line. That's the room's turn.*

- "Watch what's happening here, because it's four lines and it changes everything."
- **Line by line:**
  - "I set the goal. I say what good looks like. That's my job as the manager. Nobody else can do that part."
  - "Then I ask the expert what THEY think they should do. Because they're the expert. I'm not."
  - "And then it asks me a question back. Most people have never had that happen, because they never left room for it."
  - "So I answer. And now neither of us is guessing."
- "That exchange IS the setup. And the setup decides the output before a single word of the actual work gets written."
- **The payoff, and this is what they came for:** "Here's the part nobody tells you. This is LESS brain power, not more."
  - "The expert generates the plan. I edit it. Editing is a fraction of the work of writing."
  - "And what I walk away with isn't just a better answer. It's a better plan, better steps, with an expert's reasoning attached to it."
- **The one sentence to steal today:** "Before you start, ask me questions that would help you do this better."
- "Put that at the end of your next prompt. Whatever you were already going to ask. It stops guessing and starts interviewing you."

**Transition:** "Now that's them asking me. Here's me asking them."

---

## SLIDE 10 · SIX QUESTIONS

> # Six questions.
> ### You already know them. You've just never asked them out loud.

| Ask the expert | Why |
|---|---|
| **What do you think I'm asking for?** | Catches the mismatch while it's still free. |
| **What am I assuming that you'd push back on?** | Your blind spot is their plain sight. |
| **How do you know that's true?** | Separates what it knows from what it's inventing. |
| **What would someone who disagrees say?** | The objection, before the room hands it to you. |
| **If this works, what happens next?** | Turns an answer into a plan. |
| **Am I asking you the right question?** | Sometimes they've got a better one than you brought. |

**Speaker note:**

*Do NOT say "Socratic method." Do NOT name the six categories. One line of history, then move.*

- "Two thousand years ago a teacher named Socrates figured out you learn more from a good question than a good answer. He never told anybody what to think. He just asked until they got there themselves."
- "That's it. That's all the history you need."
- **The point of this slide:** "Notice every one of these is pointed at the expert. Not at myself. You already ask yourself these in the shower. Asking them OUT LOUD is what turns a tool into a colleague."
- **Read slowly, let each one land. Short on time? Give #2 and #6 only.**
  - "What do you think I'm asking for? If it's building the wrong thing, I want to know in one sentence, not after a page."
  - "What am I assuming that you'd push back on? It'll name the assumption I couldn't see, because I'm the one holding it."
  - "How do you know that's true? That's how I tell the difference between something it knows and something it made up."
  - "What would someone who disagrees say? I'd rather hear the objection in my own kitchen than from the room."
  - "If this works, what happens next? An answer ends. A plan continues. I want the next three steps."
  - "Am I asking you the right question? Half the time the expert has a better one than the one I walked in with. That's the whole reason I hired them."

**Transition:** "So that's move one. Ask instead of order. Move two is where it gets interesting, because now I need more than one expert."

---
## SLIDE 11 · TRY IT NOW

> # Make it interview you.

**Open whatever AI you have on your phone right now.**

Paste this:

> *"I want you to help me with [your bottleneck]. Before you answer, ask me five questions you need answered to do this well."*

Answer the questions. Then let it try.

**Speaker note:**

*5 minutes, hands on phones, no laptops needed. This is the first time tonight they touch it.*

- "Phones out. Whatever you've got. ChatGPT, Gemini, Claude, the one on your phone already."
- The point is not the output. The point is the flip: they stop typing orders and start getting asked.
- **Watch for the face.** Somebody always looks up surprised that it asked something they hadn't thought of.
- "That feeling? That's the whole workshop. Keep it."
- If someone has nothing installed, pair them up. Nobody sits this one out.

**Transition:** "One good conversation gets you one good answer. Now let's get you a whole staff."


---

## SLIDE 12 · STAFF THE KITCHEN

> # No kitchen hires "a cook."
>
> ## Butcher. Saucier. Pastry chef. Expeditor.
>
> ### Same ingredients. Four completely different reads.

**Speaker note:**

*Matter of fact. This is a method slide, not a flex slide.*

- "No real kitchen hires a cook. They hire a butcher, a saucier, a pastry chef, an expeditor."
- "Same ingredients on the table. Four completely different reads on what to do with them."
- "So when I ask one AI to do everything, I'm asking one cook to be the whole kitchen. It'll try. It'll give me the average answer."
- **Connect it to how I built mine:** "I've got about ninety of these now. A copywriter. A CFO. A therapist. A chef."
- "And I want to be clear about how they got there, because this is the part people assume wrong. I didn't prompt them into existence. I interviewed them into existence."

**Transition:** "So what actually makes an expert an expert? It's not what you'd think."

---

## SLIDE 13 · A PERSONA IS A QUESTION

> # Not the job title.
> # Not the bio.
> # **The question they can't stop asking.**

> - Copywriter: *"Does the first line earn the second?"*
> - CFO: *"What does this cost us if it works?"*
> - Therapist: *"What are you avoiding by staying busy?"*
> - Chef: *"What's already in the fridge?"*
> - Sourcer: *"Who already works somewhere this problem is solved?"*

**Speaker note:**

*Build these one at a time. Let them hear the difference between the four.*

- "A persona isn't the job title. It isn't the bio. It's the question they can't stop asking."
- "My copywriter asks does the first line earn the second. Every time. Doesn't matter what I give her."
- "My CFO asks what does this cost us if it WORKS. Not if it fails. If it works."
- "My therapist asks what am I avoiding by staying busy. That one hurts."
- "My chef asks what's already in the fridge."
- "That recurring question is the whole expert. Everything else is decoration."
- **This is move two. Say it as something they can run tonight:**
  - "Don't describe the expert you want. You'll just describe yourself."
  - "Ask the expert you've already got who should be in the room for this. Then interview whoever shows up."
  - "You're not writing a character. You're hiring one. And the interview IS the build."

**Transition:** "Okay. So now I've got a few of them. Here's move three, and this is the one that actually changed how I work."

---

## SLIDE 14 · PUT THEM IN A ROOM

> # I didn't write this talk alone.
>
> ### I asked nine of them to tear it apart.

> **The copywriter cut the flex. The therapist caught the tone.**
> **The chef found the metaphor.**

> ## I spent my time deciding. Not drafting.

**Speaker note:**

*Be honest here. Self-deprecating lands better than impressive. This is the payoff of the whole talk.*

- "I didn't write this talk alone. I asked nine of them to tear it apart before you ever saw it."
- **Be specific about what they caught:**
  - "The first version of this deck was cocky. My copywriter told me so. In those words."
  - "My therapist said the tone would land wrong on a room that doesn't know me."
  - "My chef found the kitchen metaphor. The one that's been running through everything for the last twenty minutes."
- "I didn't write nine drafts. I read nine opinions and made one call."
- **The shift, and say it slow:** "I'm not producing anymore. I'm deciding. And deciding is the part that actually needed me."
- **The correction habit, quickly:**
  - "When one of them gets it wrong, don't hit retry. Retrying just re-rolls the dice."
  - "Say what was wrong, say what to do instead, and tell it to write that down."
  - "That's the difference between a tool and something that has a memory of working with you."

**Transition:** "So now you do it. Back to your table, and build one."

---

## SLIDE 15 · CORRECT IT OUT LOUD

> **Retrying:** *"No, try again."*
>
> **Correcting:** *"That was wrong because ___.
> Going forward, when I ___, you should ___.
> Write that down."*

> ## Retrying re-rolls the dice.
> ## Correcting writes a rule.

> ### **Prompting is a transaction. Correcting is a relationship.**

**Speaker note:**

*8 minutes. This is the compounding module. Slow down on the real example, it's the one they retell.*

- "The AI gets it wrong. Everybody does the same thing. Retype it with different words and hope."
- "That's re-rolling the dice. Nothing got learned. It happens again next week."
- **The move:** "Don't retry. Say WHY it was wrong. Then make the correction permanent."
- **The real example, tell it straight:** "I texted my AI one word. 'Hi.' I was at the stove. Just saying hello. It came back with a task list and three things I hadn't done."
  - "I told it: I said hello. That's all that was."
  - "So we wrote a rule. **Greeting gets a greeting.** If he says hi, say hi back. The rest can wait."
  - "It has never done it again. Not because the model got smarter. Because the correction became permanent."
- **The payoff line:** "Every correction is a mistake you refuse to have twice. Do that for a year and you don't have a prompt. You have a system with a memory."
- **🔪 Ex 4.1, 7 min, Write Rule One.** Format on screen: Rule, positively stated · Trigger, when it applies · Why, the specific time it went wrong.
- "Paste it into your system prompt or your project file. That's your first line of source code."

**Transition:** "Everything I just showed you works in a chat box. Now let's get it off the chat box and onto your machine."

---
## SLIDE 16 · THE DEMO

> # Now watch me actually do it.

**Speaker note:**

*15 minutes. This is RJ's block, live and unscripted. No slide content on purpose, the screen is the demo.*

**What this block has to accomplish:**

- **Scrape something real with Apify.** A tool doing a real job on real data, in front of them. This is "the hands."
- **Show my actual setup, Clawdia.** Not a demo account. A Tuesday. Mess included.
- **Show the agent teams.** Multiple experts, each with their own lens, on one problem. This is what they build in Block 7 at small size.

**Guardrails:**

- No metered API account on screen. They're setting up the free path in 20 minutes and it has to look reachable.
- No credentials, tokens, or keys visible. Check the terminal before you share.
- Hard stop at 15. The build block is where the value is.
- **The deliverable is not comprehension. It's wanting to try it.**

**Transition:** "You've seen mine. Let's get you one."


---
## SLIDE 17 · FIND YOUR TABLE

> # Group up by bottleneck.

> ## 5 minutes. Grab coffee on the way.

**Tables of 3 or 4.** Find people whose bottleneck rhymes with yours.

Screening. Sourcing. Scheduling. Follow-up. Intake.

**Speaker note:**

*Form teams ONCE, right here. They stay in these teams for setup and build. Break happens inside the move so it costs nothing.*

- "Look at the board. Find your people."
- Group by shape of problem, not job title. A recruiter and a coordinator with the same bottleneck belong together.
- **Facilitator: place the stragglers yourself.** Don't let anyone stand.
- **Facilitator: count laptops per table while they settle.** Every table needs at least two. Move a person, not a machine, and say nothing about why. Never ask the room who didn't bring one.
- Coffee and bathroom happen during this. No separate break.

**Transition:** "Everybody seated? Get a screen open at every table. We're building."


---

## SLIDE 18 · YOUR OWN KITCHEN

> # OpenClaw.

> ## A chat window forgets you.
> ## A setup remembers you.

> ### **Free · Your model · Mac or Windows · Your account, not mine**

> # → openclaw.ai

> **Mac.** Open Terminal, paste:
> `curl -fsSL https://openclaw.ai/install.sh | bash`

> **Windows.** Download the installer, double-click it. Or PowerShell:
> `iwr -useb https://openclaw.ai/install.ps1 | iex`

> **Then both:** `openclaw onboard --install-daemon`

> **Every command, the Windows installer link, and a free key if you don't have one: the workshop page.**

> **Three ways in. Same steps.**
> **1. Your laptop** — running before you leave
> **2. Google Cloud** — runs while your laptop is closed
> **3. No laptop tonight** — pair up, drive your partner's screen, finish at home

**Speaker note:**

*15 min, hands on keyboards. This is the module they walk out owning. Do not rush it and do not let a stuck table sit quiet.*

- "Everything so far works in any chat box. This part makes it persist. The thing we're standing up is called **OpenClaw**."
- "A chat window forgets you. A setup remembers you. The difference is where the files live."
- "It reads a folder of files you control. Your Lenses, your rules, your corrections load every time instead of getting re-explained every time."
- **Why this one, and say all four, they're the objections:**
  - "**The software is free.** You're not buying OpenClaw. Nothing here runs on my account."
  - "**It asks for one key, and Google gives one away.** aistudio.google.com/apikey, sign in, click Create. No credit card. If you already have an OpenAI or Claude key, use that instead."
- **Do not say the words "API key" and then pause.** Say "a key, and Google hands them out free" and have the page already up on screen. Half a room hears "API" and quietly decides this isn't for them. Get to the free part in the same breath.
  - "**It's model-agnostic.** OpenAI, Gemini, Claude. Bring whatever you already have. You don't buy anything new tonight."
  - "**It's OS-agnostic.** Mac or Windows. Both work in this room."
  - "**Nothing here runs on my account.** You walk out owning it."
- **The one rule for this block, say it before they start:** "If you get stuck, raise a hand and keep going to the next step. Do not sit stuck and quiet. The person next to you hit the same wall ninety seconds ago."
- **Point at the workshop page and say it out loud: every command is written out there, you do not have to copy anything off this slide.** Laptop first, in the room, tonight. The Google Cloud path is the same steps on a cloud box, so it runs when your laptop is closed. Walk it on screen, let them finish it at home.
- **The key will be the wall.** Onboarding asks for an API key. Anyone without one goes to `aistudio.google.com/apikey`, signs in with any Google account, clicks Create API key. Free tier, no card. Say this before hands go up, not after.
- **The Windows objection you'll hear: "doesn't this need WSL2?"** It does not. Native PowerShell works, and there's a double-click installer. WSL2 is the fuller path and they can move to it later. Do not let a Windows user opt out of the block over this.
- **Say the third one out loud, early, before anyone has to admit it:** "If you didn't bring a laptop, you are not sitting this out. Pair with someone at your table and drive their screen for your bottleneck. Every command is on the workshop page. Stand up your own tonight." Nobody spectates for fifteen minutes.
- **Facilitator:** circulate. Do not narrate from the front for 15 minutes. The room needs hands, not a lecture.

**Transition:** "Kitchen's yours now. Let's hear what everybody built."

---
## SLIDE 19 · BUILD YOUR BOTTLENECK

> # Your loop. Your expert. 25 minutes.

**1.** Take your table's bottleneck. The real one from the board.

**2.** Write **one expert** for it. Who they are, what they refuse to do, what they always check.

**3.** Run it. Give it your actual work.

**4.** **Correct it out loud.** Tell it what it got wrong and why. Watch it change.

**Speaker note:**

*Slide stays up the full 25. This is the longest block of the night and the reason everyone came.*

- "This is the part that matters. I'll be walking."
- **Facilitator, circulate constantly.** Don't hover at the front. Every table gets you at least twice.
- Common stall: writing the expert too generically. "Recruiting expert" does nothing. "Screens for the three things that actually get someone hired here, and refuses to score on years of experience" does everything.
- Second stall: they ask it something and accept the first answer. Push them to correct it once, out loud.
- **At 20 minutes:** "Five left. Get one thing working, not three things perfect."

**Transition:** "Hands up if it did something useful. Tell me what happened."


---
## SLIDE 20 · REPORT BACK

> # What did you build, and what surprised you?

**One table at a time. 30 seconds each.**

- What's your bottleneck?
- What did your expert do?
- What surprised you?

**Speaker note:**

*5 minutes. Fast. This is the proof, in their words, not mine.*

- "Thirty seconds. What was the loop, what did it do, what surprised you."
- **Take the surprises seriously.** That's the curiosity showing up on its own and it's the whole point of the night.
- If something didn't work, say so out loud and name why. A room that only hears wins doesn't believe any of them.
- **Do not let this run long.** Five minutes, then the close.

**Transition:** "Here's the one thing I want you to take home."


---

## SLIDE 21 · THE CLOSE

> # I never wrote a team.
>
> ## I asked questions until I had one good recipe.
>
> ### Then I asked that expert who else the kitchen needed.

> **It answered. That's the brigade.**

> ## I didn't build it. I managed it.
>
> # Anybody can cook.

> ### Want one of your own?
> ### **hi@concept.kitchen** · **concept.kitchen**

**Speaker note:**

*This is the slide people photograph. HOLD it. Tell the story in order and keep it plain.*

- "I never sat down and designed a team. That's not what happened."
- **The story, in order:**
  - "I asked questions until I had one template that worked. One that gave me an expert with a real point of view and the tools to actually act on it."
  - "Then I asked THAT expert who else should be in the room for the next thing."
  - "It told me. I interviewed whoever it named. Wrote them down. Asked again."
  - "One expert became a few. A few became teams. The teams became the brigade."
- "I didn't build it. I managed it. And managing it was asking questions."
- **The free gift, say it out loud, it's the best line I've got:**
  - "Brigade isn't even my word. It's what a kitchen calls its staff. Escoffier named it about a hundred and thirty years ago. Brigade de cuisine."
  - "I didn't know that when I started. I just needed more than one cook."
- "Anybody can cook."
- **The ask. Don't rush it:**
  - "I said at the top I don't care what your background is. I meant it. Nothing I showed you today needed a degree. It needed better questions."
  - "So if you want one of your own, come find me. That's what today was."
  - "And the one thing to do tomorrow, before you even think about building a team. Add one sentence to your next prompt. Before you start, ask me questions that would help you do this better."
- *No Q&A slide. Take questions live off this one.*

---

## SLIDE 22 · POST-CREDITS

> ### *(after the applause)*
>
> # One more thing.

> ## This Saturday I'm putting the whole thing in a park.

> **Dog-a-thon. Aug 22. Presidio Main Parade Lawn.**
>
> **Rescue dogs. An AI hackathon. A vendor village.**
>
> **We're building for real pet care problems, live, with dogs on the grass.**

> ## Come ask questions in person.
>
> ### **luma.com/rklrsomo**

**Speaker note:**

*Wait for the applause to start dying. Then this slide. Say "one more thing" and let them laugh, they'll get the bit. Fifteen seconds. Don't sell it, invite them.*

- "One more thing."
- "This Saturday. Two days from now. I'm putting this whole thing in a park."
- "Dog-a-thon, August 22nd, Presidio Main Parade Lawn. Rescue dogs from Copper's Dream that are actually up for adoption. An AI hackathon building for real pet care problems. And a vendor village."
- "Co-hosted with AI Valley."
- "Come ask questions in person. QR's right there."
- *If someone asks what Pet Zen is: one sentence, point at the QR, do not pitch from the stage.*

---

## DESIGN NOTES

**Do NOT default.** No stock robot imagery, no blue gradient, no three-column icon grid, no "AI" in a circuit-board font.

- **Type:** One typeface, two weights. Huge. If it fits comfortably, it's too small.
- **Palette:** Two colors plus white. Kitchen-warm, not tech-cold.
- **Slides 9 and 16 carry text only.** No decoration. The white space is the design. On 9, the two speakers need to be visually distinct at a glance (weight or indent, not color-coded boxes).
- **Tables (5, 6, 8, 10, 12):** thin rules or no rules. Never boxed cells. Slide 5 is the densest thing in the deck, so it gets the most air.
- **No slide numbers, no logo bug on every slide.** Logo on 1 and 16 only.
- **Build in one line at a time on slides 3, 4, 12, 13** so the room reads with you instead of ahead of you.

- **The three breakout slides (7, 14, 15) are a different object.** They are not talk slides, they are instructions the room reads while working. Same type family, but treat them as a distinct surface: numbered steps, high contrast, readable from the back of the room for a full 8 to 10 minutes. Put a visible timer on them if the venue allows.
- **Slide 17 is a separate build.** It should feel like the deck ended on 16. Black or blank beat between them if the room allows it. The joke is the separation, so don't let 17 look like a continuation of the close.
- **Slide 17 gets a QR code** for `luma.com/rklrsomo`, large, bottom third. Nobody types a URL off a screen.

**The moves, and where they live:**

| Move | Slides |
|---|---|
| 0. Know what the thing actually is | 4, 5, 6 |
| 1. Ask questions instead of giving orders | 1, 2, 3, 8, 9, 10 |
| 2. Let the expert help you build the expert | 11, 12 |
| 3. Put them in a room and let them plan it | 13, 16 |
| Breakouts (the room works, not the speaker) | 7, 14, 15 |

**Inside the 2-hour workshop:** the deck carries the talk, not the whole session. Slides 1 to 3 open. Slides 4 to 6 are Module 0, the foundation. Slide 7 is the first breakout. Slides 8 to 10 run under Modules 1 and 2. Slides 11 to 13 run under Module 3, and 14 is its breakout. Modules 4 and 5 run live with no deck at all. Slide 15 is the report-back, 16 closes. The hands-on blocks happen off the deck, laptops open.

If you're running long, **8 and 11 are the compressible ones.** Never cut 9 or 10, those carry the thesis. Never cut 4, that's the definition the whole night rests on. **Never cut a breakout to save time.** Cutting the room's own work to protect the speaker's material is the exact mistake this workshop is about. If the clock is gone, shorten Module 5 and keep the groups. Slide 17 goes after the close.

---

*The Concept Kitchen · Anybody can cook.*

---

## Sources
- claim: deck resequenced to eight blocks; slides for the icebreaker, the reverse-interview beat,
  the demo, team formation, the build block, and report-back added; BREAKOUT A/B/C retired
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "then we'll go from intro what I'm about to
  asking them questions in icebreaker to the workshop lecture to the demo to set up or actually them
  breaking up into groups and then into set up. Then after set up they go into their bottlenecks and
  they go into building." Also: "i even said this earlier yet what you gave me for v2 follows none of
  this shit fix it NOW."
- claim: SLIDE 4 WHO YOU ARE, the four icebreaker questions
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "what brought them here why are they
  interested in agents where their capability is at with ai so far" and "people are gonna talk about
  their bottlenecks."
- claim: SLIDE 16 THE DEMO has no scripted content
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "but I don't know that demo portion is up to me."
- claim: SLIDE 9 renamed from THE SETUP to THE ASK
  source: Clawdia's decision. "The setup" now names BLOCK 6 (OpenClaw install). Two different things
  could not share a name in the same deck.
- claim: title "Ask, Don't Micromanage"
  source: RJ-confirmed (Telegram, Aug 20 2026), verbatim: "dont change the name of the url. that's the one we want to use just update it". Already the site name in build.py:152, 180, 251. Unified across all three surfaces per RJ's "unify" (Telegram, Aug 20 2026).
- claim: subtitle "Build an agent for your recruiting workflow"
  source: Luma event record in CONTEXT-INBOX.md:55-73, live API pull. Registration title is "Let's build an agent! For your recruiting workflow." on the Talent AI Lounge calendar. Subtitle restates the registration promise so the screen matches the ticket.
- claim: room is recruiters and talent professionals · session is 2 hours
  source: RJ-confirmed (Telegram voice note, drop 1, Aug 20 2026), verbatim: workshop grows to two hours, audience is recruiters. Captured in CONTEXT-INBOX.md.
- claim: date Thursday Aug 20, 2026
  source: `date "+%A, %B %d, %Y"` run Aug 20 2026 · Luma event record in CONTEXT-INBOX.md (start_at 2026-08-20, 5:00 PM PDT)
- claim: slides 4, 5, 6 (what an agent is · the six pieces · the four tiers)
  source: propagated from src/workshop.md MODULE 0 per Rule 51. Underlying sources are context/reference-transcript-FULL-VERBATIM.txt:11 (the one-sentence definition), :83 and :189 (no hands, no memory), :50 and :89 (tool calling as the hands), :129-135 (context window), :159-165 (system prompt), :23, :284, :380, :596 (the four tiers). SCAFFOLDING borrowed, every EXAMPLE replaced, per RJ (Telegram, Aug 20 2026): "i like how he set up the foundation but we are not using his examples we're going to use my examples." The kitchen column of the six-pieces table is this workshop's own metaphor, not the source's.
- claim: slides 7, 14, 15 (the three breakout slides)
  source: propagated from src/workshop.md Breakouts A, B, C per Rule 51. Group work is RJ-confirmed (Telegram, Aug 20 2026): "there's no break up into fucking groups like i asked for." The specific placements, timings, and step wording are Clawdia's structural proposal and have NOT been reviewed by RJ.
- claim: "eight tables at 30 seconds is four minutes" on slide 15
  source: arithmetic only. The table COUNT is an illustration for the facilitator, not a headcount claim. Luma reports guest_count: 0 (suppressed), so actual attendance is UNKNOWN. Do not state a room size on stage.
- claim: Sourcer lens on slide 8, "Who already works somewhere this problem is solved?"
  source: src/workshop.md Module 3 (same example, propagated per Rule 51). Constructed as a demonstration of the Lens pattern for this specific room, not a claim about an existing expert file.
- claim: "about ninety" experts, spoken only on slide 7
  source: skills/brigade/experts/ filesystem count = 93 files (`ls skills/brigade/experts/*.md | wc -l`) vs skills/brigade/ROSTER.md = "92 experts". Sources conflict by one, so the deck states no number and the speaker hedges to "about ninety." Do not state an exact count on stage. NOTE: the "29,132 words / 50 rules / I asked one question 90 times" stats line was CUT from slide 10 on Aug 15, 2026 per RJ ("that's corny").
- claim: the brigade origin story on slide 10 (questions first, then a template producing experts with personas and tools, then asking existing experts who else the kitchen needed, then teams)
  source: RJ-confirmed (Telegram, Aug 15 2026), verbatim: "i asked the war room questions to build the perfect template for me that gives me agents with personas along with their tools. then my agent became several team of agents, the brigade. and it all start by asking questions like asking the other agents to give their input to create a certain expert." CORRECTION NOTE: an earlier version of this deck claimed the brigade was built by asking one question ("Who should be in the room for this?") ninety times, sourced as RJ-confirmed. That attribution was FABRICATED by Clawdia. A grep of the Aug 13-15 session files found the phrase only in Clawdia's own output, never in RJ's turns. RJ corrected it Aug 15, 2026. The real story is recursive, not linear.
- claim: "brigade de cuisine" is Escoffier's kitchen staffing system, roughly 130 years old
  source: general culinary-history knowledge (Auguste Escoffier, Le Guide Culinaire era, 1890s). No specific stake, spoken as an aside. RJ did not name the brigade after it, which is the point of the line.
- claim: the war team review on slide 9 (copywriter cut the flex, therapist caught the tone, chef found the metaphor)
  source: this deck's own full-war review, Aug 15 2026, memory/sessions/2026-08-15-telegram-live.md. Sable flagged the cocky tone, the tone/approachability note came from RJ's own voice note relaying it. Verify the exact three attributions before stage; if unsure, say "nine of them" and describe the notes without assigning each one.
- claim: "less brain power," "editing a plan instead of writing one," "a better plan and strategy and steps to take with expert guidance"
  source: RJ-confirmed (Telegram voice note, Aug 15 2026), his own words describing the payoff
- claim: slide 4 speaker note, that thinking about prompt structure led to managing requests clearly and planning ahead for tasks with the brigade
  source: RJ-confirmed (Telegram, Aug 15 2026), verbatim: "thinking of prompt structure, got me thinking of how to manage what i ask for clearly, and to think of a way to plan ahead for my tasks with my expert brigade of agents"
- claim: RECIPES 7-part table
  source: projects/concept-kitchen/course/TCK-curriculum/resources/module-1-prompt/session-1.3-recipes-framework/recipes-cheatsheet.md:10-18
- claim: "Before you start, ask me questions that would help you do this better."
  source: recipes-cheatsheet.md:61 (RECIPES, S = Sanity-check)
- claim: the six questions
  source: skills/brigade/SKILL.md:28-36 ("The Six Socratic Types"), restated in plain English without the taxonomy labels per RJ's note that the audience does not know the academic terms
- claim: Socrates asked rather than told, roughly two thousand years ago
  source: general classical-philosophy knowledge, no specific stake
- claim: persona defined by `**Lens:**` = "always starts with a quoted question"
  source: skills/brigade/SKILL.md Expert File Template, field 8
- claim: "not a developer, no CS degree, field work for a living"
  source: USER.md · RJ-confirmed (Telegram, Aug 15 2026)
- claim: slide 1 and slide 10 speaker notes, the background-agnostic permission beat and the stated goal of relatability toward critical thinking
  source: RJ-confirmed (Telegram, Aug 15 2026), verbatim: "i dont care what your back ground is. my whole goal is to make this relatable to help people think critically to get the most out of using the technology"
- claim: "Anybody can cook"
  source: CLAUDE.md, The Concept Kitchen Brand Voice
- claim: the manager framing (a good manager asks rather than micromanages)
  source: RJ-confirmed (Telegram, Aug 15 2026), his own words
- claim: design notes reject default patterns (stock robot imagery, gradient, icon grid)
  source: CLAUDE.md Rule 47 + skills/brigade/experts/tastemaker.md (Arden's default test)
- claim: CTA "hi@concept.kitchen · concept.kitchen"
  source: USER.md:23 (hi@concept.kitchen) · DNS verified Aug 15 2026 (concept.kitchen A 185.199.111.153, HTTP 200, MX smtp.google.com) · RJ-confirmed (Telegram voice note, Aug 15 2026)
- claim: Dog-a-thon date "Aug 22" (Saturday)
  source: memory/reference/dogathon-2026-vendor-info.md:37 "August 22, 2026 (Saturday)"
- claim: Dog-a-thon venue "Presidio Main Parade Lawn"
  source: memory/reference/dogathon-2026-vendor-info.md:38 "The House by Edge & Node + Presidio Main Parade Lawn #3, San Francisco"
- claim: rescue dogs, AI hackathon, vendor village, co-hosted with AI Valley
  source: memory/reference/pet-zen-hackathon.md (event format, one-pager v4). Rescue dogs are from Copper's Dream.
- claim: "luma.com/rklrsomo"
  source: memory/drafts/dogathon-vendor-outreach-2026-06-25.md (appears in every vendor email, its own Sources block reads RJ-confirmed Telegram Jun 25 2026) · HTTP 200 verified Aug 15 2026

- claim: the demo scrapes with Apify
  source: RJ run-of-show message, Aug 20 2026 verbatim: "we're going to go through the demo using
  appify of how to scrape something or something I decide". Tool named because he named it.
- claim: the demo shows Clawdia
  source: RJ run-of-show message, Aug 20 2026 verbatim: "we're definitely going to show them how to
  use Claudia or how I use Claudia in the demo".
