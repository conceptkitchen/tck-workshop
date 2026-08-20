# Reference transcript — "What is an AI agent" explainer

**Source:** Sent by RJ, Aug 20 2026 (context drop 2). Third-party video transcript.
**RJ's instruction, verbatim:** *"i like how he set up the foundation but we are not using his examples we're going to use my examples and I will tell you my examples after however I will share you his full transcript"*

**USE:** Borrow the STRUCTURE and the explanatory sequence.
**DO NOT USE:** His examples. RJ supplies his own.

**STATUS: ✅ COMPLETE, 0:00 → 21:21. No gaps.**

🟢 **AUTHORITATIVE SOURCE:** `context/reference-transcript-FULL-VERBATIM.txt` (853 lines, 29,371 bytes).
RJ sent the whole thing as a FILE in drop 7 (Aug 20, ~5:40 AM) — *"here look at this since you
said it cut off."* Permanent copy also at `~/.claude-relay/knowledge/full-transcript-example-workshop.txt`.
**Read the VERBATIM file for exact wording. This file is the derived analysis.**

The old 6:04 → 11:50 gap (lost to a context compaction in drop 3) is **CLOSED**. Recovered in that
range: RAG named at 6:08, the full agentic-loop narration 6:23–7:11, the four constant decisions
verbatim at 8:03–8:18, the DataCamp sponsor block 8:25–9:49, and the Tier 1 GenSpark demo 9:52–11:47.

**Lesson worth keeping:** two compactions destroyed chat-pasted context on this project. A file in
`~/.claude-relay/knowledge/` is immune to compaction. For any large context: send the file, not the paste.

---

## 📐 Authoritative chapter map

Extracted programmatically from the transcript's own embedded section headers — not inferred.

| Start | Section | Runtime | Share |
|---|---|---|---|
| 0:00 | *(cold open)* | 0:52 | 4% |
| 0:52 | **What Are Agents** | 1:01 | 5% |
| 1:53 | **The Key Building Blocks** | **5:22** | **26%** ← longest section in the video |
| 7:15 | **The Landscape/Options** | 1:10 | 5% |
| 8:25 | ~~DataCamp~~ | 1:27 | 7% | ⛔ SPONSOR — strip |
| 9:52 | **Tier 1 — No Code** | 2:45 | 13% |
| 12:37 | **Tier 2 — Low Code** | 2:25 | 11% |
| 15:02 | **Tier 3 — Agent Harness** | 2:42 | 13% | ← OpenClaw named here |
| 17:44 | **Tier 4 — Full Code** | 2:10 | 10% |
| 19:54 | **How to Pick?** | 1:27 | 7% | ← OpenClaw named again (20:38) |
| 21:21 | END | | |

**The foundation (cold open → end of The Landscape) runs 8:25 — 40% of the video before a single
demo appears.** Observation only. Not a proposal.

> ### 🔴 OpenClaw is IN this transcript — TWICE
> **15:02** — named as one of the two leading Tier 3 agent harnesses (with Hermes).
> **20:38** — named AGAIN in the final "How to Pick" verdict: *"If you want a genuinely
> powerful agent that you can use for yourself that works in production... use a harness
> like Open Claw or Hermes agent."*
> The recommendation section of the transcript RJ wants to borrow structure from lands on
> the exact tier his pivot lives in. See Part 4 and war question #7.

---

## Structural skeleton (the part RJ likes)

1. **Open by naming the gap** — everyone talks about agents, nobody explains what one is.
   Calls out the "little brain doing magic" framing as exactly why it feels like hype.
2. **One-sentence honest definition, delivered early**
   > "An AI agent is simply just a language model that can use tools that's running in a loop until it finishes a job."
   Then: "That's it. That's literally all an AI agent is. Everything else is just a small detail."
3. **Promise the payoff** — build the same agent four ways, no-code down to pure Python.
   "By the end you're going to understand agents better than most people posting about them."
4. **Clear the most common confusion first** — chatbot vs agent.
   - Chatbot / plain LLM does ONE thing: it talks. Can't check email, search, book, update a DB.
   - Agent = model + two new abilities:
     - **(a) take actions in the real world** = tool calling
     - **(b) keep going on its own**, step by step, instead of stopping after one reply
   - The line: "A chatbot answers the question. An agent can be told a goal and go actually accomplish it."
   - Payoff line: "Once you understand that, the whole thing stops becoming magic and starts becoming something you can actually build."
5. **Then, and only then, the building blocks:**

   | # | Block | The framing he uses |
   |---|-------|---------------------|
   | 1 | **The LLM** | "the brain" — but immediately deflates it: all it does is predict text. No hands, no memory. A text predictor sitting in a box. |
   | 2 | **Tool calling** | "the hands" — the model does NOT go online. It outputs a structured message that looks like code saying "I want to use this tool." Surrounding code sees it, runs the tool, hands the result back. |
   | 3 | **The agent harness** | The code running the model is what actually executes. "The model decides what to do, but the code that's running this model is what's actually doing the commands." |
   | 4 | **Context window** | "short term working memory" — instructions, conversation, tool calls, tool results. Has a hard limit. Can't dump a whole codebase in. Being smart about what goes in = **context engineering**. |
   | 5 | **System / user / assistant roles** | System prompt = the rules, who it is, how to behave. User = input. Assistant = what the model sends back. "That structure is the backbone of every interaction." |
   | 6 | **No memory by default** | "The model itself has no memory on its own." Every turn you re-send the whole conversation. "It's literally rereading everything that happened every single time." |
   | 7 | **Vector DB / embeddings** | For long-term memory past the context limit. Data → embeddings (numerical representations of meaning) → stored → agent gets a tool to... *[TRANSCRIPT CUTS HERE at 6:01]* |

---

## Why this structure works (for the redesign)

- **Deflation before elevation.** He removes the magic first, then builds the thing back up
  out of parts. The audience never has to un-learn a myth later.
- **The one-sentence definition lands in the first 30 seconds**, before any jargon.
- **Every abstract block gets a body metaphor** (brain / hands) then gets immediately
  corrected so the metaphor doesn't become a new myth.
- **Confusion cleared before content.** Chatbot-vs-agent comes before the building blocks,
  not after.
- Recruiter-relevant: this sequence assumes zero technical background.

---

## Full transcript as received

```
Everybody is talking about AI agents, but almost nobody explains what it is and how you build it.
0:05 You get these videos where people talk about AI agents like they think and reason
0:09 and make decisions like there's some little brain doing a bunch of magic.
0:13 And that's exactly why all of this feels like a lot of hype and not very practical.
0:17 So let me give you the honest one sentence version here, which is that an AI agent is simply
0:22 just a language model that can use tools that's running in a loop until it finishes a job.
0:27 That's it.
0:28 That's literally all in AI agent is everything else is just a small detail.
0:32 So in this video I'm going to break down what's actually happening
0:35 under the hood, the real building blocks and none of the fluff.
0:38 And I'm going to show you how you can build the same age and in four completely different ways,
0:42 from no code all the way down to writing it yourself in pure Python.
0:46 Now, by the end of the video,
0:47 you're going to understand agents better than most people that are posting about them.
0:50 So let's dive in.

What Are Agents
0:52 So first, let's clear up the most common confusion that I see,
0:55 which is the difference between a chat bot and an agent.
0:58 Now regular chat bot, or just a plain language model or LLM can only do one thing.
1:04 It talks okay.
1:05 You send a message, it sends text back.
1:08 Now that's the entire interaction, right?
1:10 It can't check your email, it can't search the web, it can't book anything or update a database.
1:14 It just generates words and predicts text.
1:17 Now, an agent is what you get when you give this model two new abilities.
1:21 Now the first ability is to take actions in the real world, which we call tool calling.
1:26 And the second ability is to keep going on its own.
1:29 So step by step, instead of stopping after just a single reply.
1:33 Now that's the loop that we're talking about.
1:35 So a chatbot answers the question was an agent can be told a goal and then go in.
1:39 Actually accomplish it by taking multiple steps and using the tools provided.
1:43 Now, once you understand that, the whole thing really stops becoming magic and it starts
1:47 becoming something you can actually build because you know the foundation.
1:50 So with that said, let's look at these pieces specifically.

The Key Building Blocks
1:53 Now the first part here is the LM or the brain.
1:56 Now at the center of every agent is a large language model or LM.
2:00 Now this is what we consider the brain.
2:01 But I want to be really clear about what this actually does.
2:04 Now all that a model does is predict text.
2:07 That's literally it.
2:08 You give it some input and it's just predicting what should come next based on how it's been trained.
2:13 Now it has no hands, it has no memory.
2:15 It can't do anything other than just generate text.
2:18 So on its own, it's really just a text predictor that's sitting inside of a box.
2:22 Now the tool calling is the next part, which we can kind of refer to as the hands of the model.
2:27 So how does the brain actually do something.
2:29 Well effectively what it does is it generates text
2:32 that tells whatever software it's working inside of to call a tool.
2:36 So you tell the model ahead of time, hey, there's these tools that you're allowed to use.
2:40 For example, you have access to a web search tool.
2:42 Now when the model wants to search, it doesn't magically go online and search.
2:47 It can't do that. It can just predict text.
2:49 So what it does, is it out puts a structured message that kind of looks like code that says, hey,
2:53 I want to use this search tool.
2:55 Now, what will happen in the background is the code that's running that model.
2:58 We'll see that result. It will run the search tool.
3:01 It will get the result and it will give that back to the model so it can process it.
3:05 So the model reads the result and then it keeps going and it takes multiple steps.
3:10 So all the model is doing
3:11 is just giving text to a system that says, hey, I want to call this thing and it doesn't.
3:15 Now that hand off is essentially the whole way that AI agents work at scale.
3:19 The model decides what to do, but the code that's running this model is
3:23 what's actually doing the commands, triggering the search tools, etc.
3:26 and that's what we call an agent harness.
3:29 Now the context window is the next piece to look at here.
3:31 And that is the working memory of an agent.
3:33 Now the model needs to keep track of what's going on.
3:36 And it does this through something called a context window.
3:38 Now think of this as the model short term working memory.
3:41 It's everything the model can see at one time, like your instructions,
3:45 the conversation tool calls, or the result of a tool call.
3:48 You get the idea.
3:49 But there's a catch here and that's that. This has a limit.
3:52 So you cannot just dump your entire code base or a thousand page
3:55 document into the context, because it can only hold so much.
3:58 As I started to get quite large, being able to hold, for example, a million tokens.
4:02 But even that is not good enough for like a massive enterprise code base.
4:05 So a huge part of building good agents is being smart about what you put in that window.
4:10 And that can be referred to as context engineering.
4:12 Now the next piece to look at is system prompt and message rules.
4:16 So what goes in there?
4:17 Well it's organized into messages with different roles.
4:20 The system prompt is where you set the rules.
4:22 So you tell the agent who it is, how to behave, general rules, things that it should do.
4:27 For example, you can say you are research assistant all we set your sources, then you have user messages.
4:33 Now this is effectively the input from the person or the system.
4:36 And then you also have assistant messages which is what the model sets back.
4:40 So that structure you have system user assistant is kind of the backbone of every interaction.
4:45 And you can pass multiple of these messages.
4:47 So the agent understands okay these are the general instructions.
4:50 This is what the user asked me to do.
4:52 This is what I said in the previous turn.
4:54 The user then asked me this and you get a full log of what's going on in.
4:58 All of that can sit inside of the context,
4:59 but I want you to remember that the model itself has no memory on its own.
5:03 If you don't keep track of the conversation and you ask a model another question,
5:07 it will forget what you said previously
5:09 because it's just not storing that unless it's inside of the context.
5:12 So how does a model remember what actually happened in previous steps?
5:15 Well, it remembers that because you feed that information back in.
5:19 So for every turn or every time you run the model, you send the whole conversation
5:23 far back into the context window.
5:25 Now that's how the agent can stay coherent across multiple steps.
5:28 It's literally rereading everything that happened every single time.
5:32 Now, the issue is that sometimes conversation history can get quite large,
5:35 and it can actually not fit inside of the current context window.
5:39 So that means that you could start forgetting things,
5:41 or you're pruning previous steps, which would lead to poor performance.
5:44 So for longer term memory or giving the agent access to documents
5:47 or different facts, we use something called a vector database.
5:51 Now the short version is that you can take your data and you can convert it into embeddings,
5:54 which are just numerical representations or kind of meaning of data.
5:58 And then you can store them, and then you can give the agent a tool
6:01
```
*[CUTS OFF MID-SENTENCE — verbatim ends here]*

---

# Part 2 — 6:04 → 11:50

> ## ✅ GAP CLOSED — verbatim recovered Aug 20, drop 7
> This section was structure-only after a compaction ate drop 3. RJ re-sent the whole
> transcript as a file. **Verbatim for this range lives at
> `context/reference-transcript-FULL-VERBATIM.txt`, lines 228–468.**
> The skeleton below is kept as the ANALYSIS layer — it's the compressed structural read.
> For exact wording, read the VERBATIM file. Both are correct; they serve different jobs.

**Verbatim highlights recovered in this range:**

- **6:08** — *"This is a super common pattern, and it's called Rag or retrieval augmented generation."*
  RAG gets named explicitly, then framed as *"how agents can answer questions about documents."*
- **6:24** — *"And this is where we can kind of put everything together. / And this is what a lot of people skip."*
  He flags the loop as the thing everyone glosses over, right before explaining it.
- **6:59** — *"Now that's an a gentle loop. Okay. You have an LLM. / You have two calls context and then
  cycling until it finishes what the goal was."* *(auto-caption garble: "a gentle loop" = agentic loop,
  "two calls" = tool calls.)*
- **7:08** — *"everything else from here that I'm going to show you is really just a different way of
  building this type of loop."* ← **the hinge of the whole video.** Foundation ends, tiers begin, and
  he explicitly tells you the tiers are variations on one idea you already understand.
- **7:22** — *"there's kind of four tiers that I've come up with based on how much of that agent you're
  going to be building yourself."*
- **8:03 → 8:18 — the four constant decisions, verbatim:** pick the platform/framework → pick the model
  (GPT, Claude, Gemini) → engineer the context → define control flow and tools. Payoff line:
  *"if you keep that in your head, you're going to be able to build agents in pretty much any platform,
  because those are really the key decisions that you're making."*
- **8:40** *(inside the sponsor block, but this idea is NOT sponsor copy)* — *"You can watch me explain
  agents all day, and you're probably gonna forget most of it by tomorrow. / The stuff only sticks when
  you actually build it yourself."*
  🔴 **The source RJ is borrowing structure from argues for RJ's hands-on format.** Observation only.
  Not a proposal.
- **10:07** — Tier 1 roster: *"you've got things like Lindi Gum, Loop stack, AI relevance, AI bot press,
  things like Gen Spark and Voice Flow... You can even use something like OpenAI's agent builder."*
  *(= Lindy, Gumloop, Stack AI, Relevance AI, Botpress, GenSpark, Voiceflow.)*

## Structural skeleton, continued

6. **Vector DB section closes out** — the 6:01 sentence completes into retrieval-augmented
   generation (RAG). Agent gets a tool to query the embeddings store, pulls back only the
   relevant chunks instead of holding everything in context.

7. **The agent loop** — the payoff on the one-sentence definition from 0:17. Named as a
   three-beat cycle: **think → act → observe**, repeating until the goal is met.
   > "thinking, acting, observing... until it eventually hits the goal"

   > "that's an agentic loop. You have an LLM. You have tool calls, context, and then
   > cycling until it finishes what the goal was"

   Note: this closes the loop he opened at 0:22. The definition is stated first, the
   mechanism is earned six minutes later. That's a deliberate structural choice.

8. **The four-tier landscape** — the spine of the back half. Tiered by *"how much of that
   agent you're going to be building yourself."*

   | Tier | What it is | Named tools |
   |---|---|---|
   | 1 | **No-code** | Lindy, Gumloop, Stack AI, Relevance AI, Botpress, GenSpark, Voiceflow, OpenAI's agent builder |
   | 2 | **Low-code** | n8n, Flowise, Langflow, Dify, Activepieces, KNIME ✅ *recovered from Part 3* |
   | 3 | **Agent harnesses** | **OpenClaw**, Hermes, Letta ✅ *recovered from Part 3* |
   | 4 | **Full code** | pure Python, per the 0:42 promise |

9. **The four decisions that stay constant across all four tiers** — the most portable idea
   in the whole transcript. Whatever tier you're on, you are always making these four calls:
   1. Pick the **platform / framework**
   2. Pick the **model**
   3. **Engineer the context**
   4. Define the **control flow + tools**

10. **Sponsor segment (DataCamp)** — ⛔ **STRIP. Not our content.**
    One line worth noting for its pedagogy, not for reuse:
    > "The stuff only sticks when you actually build it yourself."

11. **Tier 1 demo begins** — walks through GenSpark building a research agent.
    Cuts at 11:50 mid-sentence on *"research the top AI and tech YouTubers in 2026."*

---

## Why Part 2 matters more than Part 1 for the redesign

Part 1 is the foundation RJ said to keep. Part 2 is the part that **structurally rhymes
with the pivot** — the four-tier ladder is a "here's the whole landscape, now pick your
rung" frame, and RJ's change is teaching attendees to stand up OpenClaw two ways.

⚠️ **This is an observation for the war, not a proposal.** Logged, not acted on.

---

# Part 3 — 11:50 → 17:37 ✅ VERBATIM

**Received:** drop 4, Aug 20 2026. Picks up completing the sentence Part 2 cut on.

## Structural skeleton, continued

12. **Tier 1 verdict** — demo the ceiling, then name it honestly. He builds the GenSpark
    agent, shows it working, then immediately undercuts it: *"we don't have a lot of
    configuration, we don't have that much control, and it's really fairly basic."*
    **This is the move that makes the ladder work.** Each tier's demo ends by naming what
    it can't do, which is the reason to climb.

13. **Tier 2 — Low-code.** Defined by feel, not features: *"something that's a little bit
    technical... a drag and drop editor... but it's not working like fully in an IDE."*
    Tools named: **n8n, Flowise, Langflow, Dify, Activepieces, KNIME.** Demos n8n.
    Explicit hedge: *"I'm trying to give you kind of a lay of the land as opposed to a
    specific recommendation."*
    What Tier 2 buys you over Tier 1: system message control, max-turns, attached tools
    (Perplexity for search, Wikipedia for fact-check), **conversation memory**, multi-agent,
    a real loop.

14. **Tier 3 — Agent harness.** 🔴 **The tier RJ's pivot lives in.**
    The definitional line:
    > "instead of building an agent from multiple parts, you just install a complete,
    > already powerful agent and then you customize it for your needs."

    > "the two leading harnesses right now are... **OpenClaw and Hermes**"
    (also names **Letta** for long-term memory focus)

    > "the thing here to watch is that I'm not building this agent loop. It already exists.
    > It's already good. It already has memory and stuff. My job is kind of just to extend
    > it, customize it, give it the right instructions, and connect any tools that I need."

    Demos Hermes: skills, memory, spaces, profiles, to-dos, insights, MCP servers, tools,
    file attach. Creates a `/research-assistant` **skill** from a prompt, invokes it by slash
    command. Result: *"took a little bit longer... but it did do a lot more web searches and
    kind of more critical thinking because the loop here is a little bit better."*

15. **The Tier 2 vs Tier 3 tradeoff, stated plainly** — the closing beat of this section:
    > "if you're going to build something that you want to be more production ready, you're
    > okay with a little bit of setup... then this is a good option. But if you just want a
    > super reliable, consistent flow, probably you go with something more kind of automated
    > like n8n."

## Transcription artifacts (auto-caption garble → actual)

| As transcribed | Actual |
|---|---|
| "Naden" / "edit and" / "an edit and workflow" | **n8n** |
| "flow wise lang flow" | **Flowise, Langflow** |
| "DeFi active pieces, Knime" | **Dify, Activepieces, KNIME** |
| "open Claw" | **OpenClaw** |
| "letter" | **Letta** |
| "Gen Spark" | **GenSpark** |
| "Whisper Flow" | **Wispr Flow** |
| "running on a PS" | running on a **VPS** |

## ⛔ STRIP — sponsor / affiliate content in this section

- **13:41–14:34 Wispr Flow plug.** He breaks the demo to pitch a dictation tool and discloses
  a partnership: *"I do have a partnership with them, so I'll leave a link to the description."*
  Not our content. Cut entirely.
- Repeated *"I have a bunch of tutorials on this on my channel"* — channel promo, cut.

---

## Raw transcript, 11:50 → 17:37

```
11:50
research the top AI and tech YouTubers in 2026
11:53
right now that are covering AI agents.
11:53
Okay, because this is my research assistant
11:55
and we'll just let it run and it should just follow what we told it.
11:58
And we now have an agent that's designed to work specifically how we want.
12:01
Okay. And you can see that it followed the format that we asked you for.
12:04
And then it kind of gave us a response with the sources and the key findings like we wanted here.
12:09
And there you go.
12:09
We have the agent.
12:10
And you'll notice if I scroll up here, it was doing kind of like web searches and using these tools.
12:13
And you can see what it was actually searching in order to find this info.
12:17
So this is definitely the simplest way to make an AI agent.
12:20
But you'll notice that we don't have a lot of configuration, we don't have that much control.
12:24
And it's really fairly basic.
12:26
And to be honest, you can just use a general agent and connect
12:28
some tools to it and you're going to get a pretty similar result.
12:31
So let's go a step down the ladder to something a little bit more advanced, which is where most of
12:35
you are probably going to land. Okay.

Tier 2 - Low Code
12:37
So the next method that we're looking at here is low code.
12:39
Now this can have a lot of different meanings, but for me I typically mean working something
12:44
that's a little bit technical, where you kind of have to have some understanding of what you're doing.
12:48
You're working with like a drag and drop editor.
12:50
You may be able to build in some code blocks or something like that, but it's not working
12:54
like fully in an IDE.
12:56
So the big examples here are going to be platforms like and then flow wise lang flow
13:00
for using the visual editor, DeFi active pieces, Knime.
13:05
There's a bunch of other ones right now.
13:07
Naden is one of the most popular ones.
13:08
So I'm going to show it to you right here.
13:10
And while it's mostly used for automations, it's kind of a simple way for me to show you
13:13
what this would look like.
13:15
Keep in mind, there's so many platforms
13:16
that I'm trying to give you kind of a lay of the land as opposed to a specific recommendation.
13:20
So what I have here is an edit and workflow, okay.
13:23
The idea is that you can send a chat.
13:25
It goes to this research agent which is configured with a bunch of properties.
13:29
You can see there's like a bunch of stuff here. I can open it up.
13:32
You can see the system message, the max number of terms, you know, input that's going in here.
13:36
Right.
13:36
Like you can modify this quite heavily like you can't do inside of something like Gen Spark.
13:41
And then we have these different tools and models and stuff connected up to the research agent.
13:46
So in this case I've connected perplexity.
13:48
This is going to allow me to do a really good high quality web search.
13:51
I've connected Wikipedia so I can go and find the facts if it's accurate from Wikipedia.
13:56
And I've also attached conversation memory so that while I chat with this over time,
14:00
it can store it inside of there. And we don't forget the previous chat.
14:03
So we can kind of iterate on our research.
14:05
So if I want to use this, I can do something like go study the top
14:09
AI YouTubers right now, tell me the ones that are performing the best in 2026.
14:13
And by the way, if you guys are wondering what I'm using to dictate here, using a pretty cool
14:17
tool called Whisper Flow, just want to show you the UI because it's quite cool.
14:21
You can see that I have 163,000 words.
14:23
You can see that I speak much faster than I type, and it's just the best
14:27
AI voice dictation tool really on the market in my opinion.
14:30
I do have a partnership with them, so I'll leave a link to the description
14:33
in case you guys want to check it out
14:34
anyway, so you can see that this is going to give me the response now.
14:37
And if we scroll through here, we get the same kind of research assist
14:40
that we had before where we get the sources and we get actually a very similar result
14:43
that we had previously, as well as the summary. Okay.
14:47
So just kind of a more consistent way to build this where we have a lot more control,
14:51
we build in the tools. We can now go into a more advanced loop.
14:54
We can have multiple agents, and we can build something that's a little bit more consistent
14:58
than something like Gen Spark, where you're kind of just relying on the platform to set it up for you.

Tier 3 - Agent Harness
15:02
So now we move to the third tier, which is the agent harness.
15:06
Now, this one is a little bit different because instead of building an agent from multiple parts,
15:10
you just install a complete, already powerful agent and then you customize it for your needs.
15:15
Now the two leading harnesses right now are kind of agent.
15:18
Platforms are open Claw and Hermes.
15:20
Now there's also letter if you really want one that's focused on long term memory.
15:24
But Hermes agent is one that most people are using.
15:26
So I'm just going to show you kind of a quick demo of how that works.
15:29
Now the thing here to watch is that I'm not building this agent loop.
15:32
It already exists. It's already good.
15:34
It already has memory and stuff.
15:35
My job is kind of just to extend it, customize it,
15:38
give it the right instructions, and connect any tools that I need to use.
15:42
So I'm inside of Hermes.
15:43
This is kind of what the user interface looks like.
15:45
If we go to the left side you can see there's skills, memory spaces, profiles to dos, insights.
15:50
You can connect MCP servers, you can add tools. Right.
15:53
There's a bunch of stuff you can do here.
15:55
You can attach files whatever.
15:57
And you'll notice that what I've done here is I just told it, hey, I want to create a research assistant.
16:02
I used a really similar kind of prompt to what I did in Gen Spark.
16:05
And now what it's done is it's created a skill for me.
16:08
And I can invoke that research assistant by using slash research assistant.
16:11
Now built into this is already a web search that's able to go search the web and give information to me.
16:17
But if I wanted to add Wikipedia, I wanted to add perplexity.
16:20
I wanted to add other tools.
16:21
I would do that directly in Hermes, then instruct the model how to perform.
16:25
And I get kind of this general agent, which can do my specific tasks.
16:29
And this is a really common workflow for people that use agents a lot.
16:32
They build it into something like this,
16:34
because there's a lot of different things that they want to do.
16:36
And again, they're not building the full harness, but they're customizing it to their use case.
16:41
I have a bunch of tutorials on this on my channel.
16:43
I'm just going to show you a quick example.
16:45
So I built this skill called Research Assistant.
16:48
This is a custom skill that we built.
16:50
And same thing I can say go study the top
16:52
AI YouTubers in 2026, the ones that are performing the best on YouTube.
16:56
Okay, if I press enter here, we give it a second.
16:59
It should invoke this skill that we created, which is going to instruct
17:02
it, kind of perform in this manner, and then it should start using
17:05
the web search tool to go and find the information and give us the response.
17:09
Okay, so just finished here.
17:10
Now notably it took a little bit longer than some of the other ones, but it did do a lot
17:13
more web searches and kind of more critical thinking because the loop here is a little bit better,
17:17
and you can see that we get the summary key findings and these sources.
17:21
So if you're going to build something that you want to be more production
17:24
ready, you're okay with a little bit of setup.
17:25
Because Hermes does require installing setting it up, running on a PS for example.
17:29
Then this is a good option to go with.
17:31
But if you just want a super reliable,
17:33
consistent flow, probably you go with something more kind of automated like n8n.
17:37
```
*[ENDS HERE — Tier 4 full-code section presumably follows]*

---

# PART 4 — 17:41 → 21:21 (END) ✅ VERBATIM

**Source:** drop 5, Telegram, Aug 20 2026 ~5:30 AM. The video ends at 21:21.

## Structural skeleton, continued

**16. Tier 4 — Full code.** *"this is where you write the agent yourself in something like
Python and you control every single piece."* He walks the code at a deliberately non-expert
level: *"You don't need to be an engineer to understand this. I'm just going to give you a
high level explanation."* Shows imports, logging, system prompt, tools-as-JSON-objects, a
Fire Crawl web search with manual response parsing, and `run_agent` — the loop itself.

**17. The payoff move of the whole video.** After showing the raw loop he says:
*"that's what's happening behind the scenes in all of those frameworks that we looked at.
Same thing, the main loop."* Tier 4 is not presented as the best tier. It is presented as
the X-RAY. He climbs to full code specifically so he can point back down the ladder and say
*this was always what was underneath.* Everything before it retroactively makes more sense.

**18. He runs the same prompt he's been running all video.** *"go study the top AI YouTubers
in 2026. Tell me who's performing well on YouTube."* One task, four tiers, four times. The
constant task is what makes the tiers comparable. Then narrates the loop out loud as it runs:
*"turn one model requested a tool call... turn two sending the context... And then it
immediately gives us the summary. Now at this point, the model decided it was finished."*

**19. Ties back to the context-engineering thread.** *"I'm engineering the context because I'm
appending these different messages. Notice we talked about user messages assistant messages
system messages... I'm putting all of that into the model and controlling what it can see at
what time."* The concept introduced early gets cashed out in code at the end.

**20. "How to Pick" — the close.** Opens by disclaiming stake: *"I don't really care if you
use any of these tools. I'm not getting paid to promote them."* Then a one-line decision rule
per tier:

| If you... | Use |
|---|---|
| just want something working, not technical | no-code — GenSpark, OpenAI, *"even like a cloud code where you set up your own tools"* |
| need real logic, branching, many services, but don't want to manage a codebase or deploy | low-code — n8n |
| want a genuinely powerful agent for yourself that works in production | 🔴 **harness — OpenClaw or Hermes** |
| need full control, integrating deep into your own product, want to understand every piece | full code — LangGraph |

**21. The thesis, stated last.** *"you're using the same agent, the same LLM and the same loop
underneath all of these, you're just choosing how much of it you want to build yourself versus
how much you want handed to you and the control that you have. So that's really the real
decision."*

**22. Ends on permission, not mastery.** *"even me as a technical guy, a lot of times I reach
for something that's a lot easier to use because it's faster and I don't need the full
control."* The expert publicly choosing the easy tier is what makes the easy tier legitimate
for the audience.

### Transcription artifacts in Part 4
| Garble | Actual |
|---|---|
| "Genspark" | GenSpark |
| "Land Graph" | LangGraph |
| "Open Claw or Hermes agent" | OpenClaw, Hermes |
| "Macomb" | likely Make.com |
| "a cloud code" | Claude Code |
| "force a dilute multiple times" | force a tool call multiple times |
| "give it to the agent as a rule tool" | as a `role: tool` message |
| "GPT four zero" | GPT-4o |
| "Fire Crawl" | Firecrawl |

---

## RAW VERBATIM — Part 4

```
If you want to just a super quick agent to test things out, you can use something like Gen Spark.
17:41
But now let's go to the last option which is full code.
Tier 4 - Full Code
17:44
Now this is where you write
17:45
the agent yourself in something like Python and you control every single piece.
17:50
Now I just want to show you what this looks like, because this obviously gives you the most amount of
17:54
control and also shows you kind of behind the scenes what the loop actually looks like.
17:58
You don't need to be an engineer to understand this.
18:00
I'm just going to give you a high level explanation so you can see that I bring in some imports.
18:04
Right? I have kind of some logging stuff.
18:05
I have my system prompt, what I want it to do, I have tools.
18:09
Notice that the tool is really just in the form of kind of a JSON object.
18:12
And like this is what the tool looks like and how the agent can call it.
18:16
I have this web search where I'm using a tool like Fire Crawl to go and actually
18:20
grab the information that I'm looking for,
18:22
and I'm manually parsing out the response and then giving it to the agent.
18:26
And you can see this run agent.
18:28
This is the full loop where I'm running through multiple turns.
18:31
I'm doing a call seeing if the agent wants to call the tool.
18:33
If it does, I call it, I get the response, I give it to it, and I'm controlling everything you'd see.
18:38
Okay, if it wants to call tools, I'm going to call the tool myself here.
18:42
I'm going to get the response and I'm going to give it to the agent as a rule tool.
18:46
Right. So we can see it.
18:47
And that's what's happening behind the scenes in all of those frameworks that we looked at.
18:51
Same thing, the main loop.
18:53
You get the idea here.
18:54
So if I run this you can see let's go up here.
18:57
I'm going to say go study the top AI YouTubers in 2026.
19:01
Tell me who's performing well on YouTube.
19:03
Okay, let's hit enter and you're going to see that.
19:06
It shows me the full loop running so you can see that it says, okay,
19:09
turn one model requested a tool call wants to search for the top AI YouTubers.
19:13
Let's do a web search. Here's the results that we get.
19:16
Turn two sending the context of GPT four zero.
19:19
And then it immediately gives us the summary.
19:20
Now at this point, the model decided it was finished.
19:22
It didn't need to call any more tools.
19:24
And then it gave us the final answer.
19:26
If you wanted more tools, we would have kept looping.
19:28
And this is that dynamic process that we've engineered and we've built ourself.
19:32
You of course, can force a dilute multiple times.
19:34
You can make it call different tools.
19:36
You can force inject the context.
19:38
And here right, you'll notice like I just want to quickly show you
19:41
that I'm engineering the context because I'm appending these different messages.
19:45
Notice we talked about user messages assistant messages system messages.
19:49
Right.
19:49
Like I'm putting all of that into the model and controlling what it can see at what time.
How to Pick?
19:54
So now that we've looked at all four tiers, the question becomes which should you actually use?
19:58
Now here's my honest take. Right?
20:00
I don't really care if you use any of these tools.
20:02
I'm not getting paid to promote them.
20:03
But if you just want to get something working and you're not technical, use a no code tool.
20:07
Use Genspark, use OpenAI.
20:09
Use even like a cloud code where you set up your own tools and stuff inside of there.
20:12
If you need real logic, branching and connecting to a bunch of services,
20:17
but you don't want to manage a code base, or you don't want to kind of deploy something,
20:21
Then I would use a low code platform, something like n8n.
20:24
There's a lot of other examples Macomb, whatever those are again
20:27
more automation platforms, but they're really good for simple agents.
20:31
If you want a genuinely powerful agent that you can use for yourself that
20:34
works in production and that you can kind of set up and add all of the features
20:38
you want, use a harness like Open Claw or Hermes agent.
20:42
Okay, it's super powerful, and it's not as much work as building something yourself.
20:45
And if you need the full control, you're integrating something deep into your own product,
20:49
or you want to actually understand every single piece, then
20:52
use an AI framework, something like Land Graph and write it in full code.
20:56
That's exactly what we did here.
20:58
I just did it a little bit more manually so you could get the idea.
21:00
Now the point is here that you're using the same age in our LLM and the same
21:04
loop underneath all of these, you're just choosing how much of it
21:07
you want to build yourself versus how much you want handed to you and the control that you have.
21:11
So that's really the real decision.
21:12
And even me as a technical guy, a lot of times I reach for something
21:15
that's a lot easier to use because it's faster and I don't need the full control.
21:19
So that's AI agents explained.
21:21
Let me know what you think in the comments down below and enjoy building your agents.
```
