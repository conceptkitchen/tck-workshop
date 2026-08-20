# Context Inbox — Workshop v2 Redesign

Running capture of RJ's incoming context for the workshop rebuild.
**Status: RECEIVING. RJ said "wait for all my context first. I will say when I'm done."**
Nothing gets built or changed until he says done, then we run **full war** to review.

> ### ⏰ THIS SHIPS TODAY — Thursday Aug 20, 5:00 PM PDT
> Verified live from the Luma API at 5:07 AM. **11.9 hours of runway** from capture time.
> RJ is a listed co-host. This is not a future project.

---

## Drop 1 — Voice note, Aug 20 2026, ~5 AM (166s)

### Format change
- Workshop grows from **30 minutes → 2 hours**
  - RJ said "three hours actually two hours" and self-corrected to two. Recorded as **2 hours**.
- **Lecture portion stays short.** The added time is not more lecture.
  - Open question for war: what fills the remaining time — hands-on? demos? build blocks? RJ hasn't said yet.

### What survives from v1
- **Keep the foundation section**, specifically **the asking-questions material.**
- This is the only part explicitly marked "keep" so far.

### Incoming: a transcript from someone else
- RJ likes **how that person set up the foundation** (the structure).
- **We are NOT using that person's examples.** RJ's examples replace them.
- RJ will send the **full transcript**, and will give **his own examples separately, after.**
- So: borrow the scaffolding, swap every example.

### Incoming: event partner's flow + syllabus
- RJ will send **how his event partner wants the flow.**
- Applies to **the syllabus already sent.**
- **Changes are coming to it.** Current syllabus is not final.

### Big change: the demo subject
- **NOT using RJ's bot.** Not using RJ's own setup.
  - Reason given: **"it's not ready for deployment."** They wanted to, it isn't ready.
- **Instead: attendees set up OpenClaw themselves.**
- **Two deployment targets, both taught:**
  1. **Google Cloud** (RJ said "Google Cloud provider")
  2. **Their own laptop**
- So the demo shifts from *watch RJ's thing* → *you set up your own thing, two ways.*

### Audience
- **Recruiters.** Restated explicitly in this drop.

### Incoming: Luma link
- RJ will send it.

---

## Drop 2 — Telegram, Aug 20 2026, ~5:05 AM

### 🔴 THE EVENT IS TODAY

Pulled live from the Luma API (`api.lu.ma/url?url=ujthsr31`), not from memory:

| Field | Value |
|---|---|
| **Event** | Let's build an agent! For your recruiting workflow. |
| **Start** | **Thursday, August 20 2026, 5:00 PM PDT** |
| **End** | Thursday, August 20 2026, 8:00 PM PDT |
| **Block length** | **3 hours** (RJ's content plan is 2 hrs — 1 hr of margin/mingle) |
| **Where** | San Francisco, Union Square. Exact address `guests-only`. |
| **Hosts** | Mabel Liang, Petros Hong, **RJ Moscardon**, Christopher Carew |
| **Calendar** | Talent AI Lounge — https://talentailounge.co/ |
| **Positioning** | "Where forward-thinking hiring leaders gather to explore the future of hiring." |
| **Waitlist** | Enabled |
| **Guest list** | Hidden (`show_guest_list: false`). API returns `guest_count: 0` — that is Luma **suppressing** the number publicly, **NOT** a real count. Do not cite it. |

- Luma: https://luma.com/ujthsr31
- Live site: https://tck-workshop.vercel.app/

**Note:** the Luma block is **3 hours**, matching RJ's first spoken number before he
self-corrected to two. The 2 hrs is likely content, 3 hrs is the room.

### Apify — direct build order (not part of the "wait" context)
- RJ **has an Apify account.**
- `rjmoscardon@gmail.com` is **already connected on Apify.**
- Wants a **live demo** during the workshop, either:
  1. **Google Maps business scraper** (find businesses), or
  2. **Send an email** through the connected Gmail
- Asked for the **CLI installed.** ✅ Done — `apify-cli 1.8.0`.

### Incoming: the reference transcript ✅ RECEIVED (partial)
- Saved to `context/reference-transcript-agents-101.md` with structural analysis.
- Subject: "what is an AI agent" explainer. Deflates the magic, then rebuilds from parts.
- **Cuts off mid-sentence at 6:01** ("you can give the agent a tool"). Rest may still be coming.
- Core line worth stealing: *"An AI agent is simply just a language model that can use tools
  that's running in a loop until it finishes a job."*
- Structure = chatbot-vs-agent confusion cleared FIRST, then blocks:
  LLM (brain) → tool calling (hands) → agent harness → context window → system/user/assistant
  roles → no-memory-by-default → vector DB.
- **RJ's examples replace every example in it.**

---

## Drop 3 — Telegram, Aug 20 2026, ~5:12 AM

### Transcript continuation, 6:04 → 11:50 — ⚠️ LOST, then ✅ RECOVERED in drop 7

RJ sent the next chunk. **A context compaction ate it before it hit disk.** It was marked as a
gap rather than reconstructed from memory. **RESOLVED Aug 20 ~5:40 AM (drop 7)** — RJ re-sent the
complete transcript as a FILE. Verbatim now at `context/reference-transcript-FULL-VERBATIM.txt`
lines 228–468.

What the segment covers:
- **RAG / vector DB** closes out the 6:01 sentence
- **The agent loop** — think → act → observe, cycling until goal. Closes the loop opened at 0:22.
- **The four-tier landscape** — no-code → low-code → agent harnesses → full code, tiered by
  *"how much of that agent you're going to be building yourself."* Tier 1 tools named:
  Lindy, Gumloop, Stack AI, Relevance AI, Botpress, GenSpark, Voiceflow, OpenAI agent builder.
  ~~**Tiers 2 and 3 tool lists did not survive.**~~ ✅ **Recovered from drop 4** — Tier 2 is
  n8n, Flowise, Langflow, Dify, Activepieces, KNIME. Tier 3 is **OpenClaw**, Hermes, Letta.
- **Four decisions constant across all tiers:** platform/framework, model, context engineering,
  control flow + tools
- **DataCamp sponsor segment** — ⛔ strip, not our content
- **Tier 1 demo starts** on GenSpark, cuts at 11:50 on "research the top AI and tech YouTubers in 2026"

---

## Drop 4 — Telegram, Aug 20 2026, ~5:20 AM

### Transcript 11:50 → 17:37 ✅ VERBATIM

Picks up completing the sentence drop 3 cut on: *"...research the top AI and tech YouTubers
in 2026 / right now that are covering AI agents."* Saved to
`context/reference-transcript-agents-101.md` Part 3, full raw text preserved.

**Also recovered the two tool lists that drop 3's compaction had destroyed.** Those cells in
the tier table are filled in now, sourced from verbatim text rather than reconstructed.

What the segment covers:
- **Tier 1 verdict** — the GenSpark demo lands, then he names its ceiling out loud:
  *"we don't have a lot of configuration, we don't have that much control, and it's really
  fairly basic."* This is the move that makes the whole ladder work. Every tier's demo ends
  by naming what it can't do, which becomes the reason to climb to the next one.
- **Tier 2 — Low code.** n8n, Flowise, Langflow, Dify, Activepieces, KNIME. Defined by feel,
  not by a spec: *"a drag and drop editor... but it's not working like fully in an IDE."*
  Demoed in n8n with Perplexity + Wikipedia attached and conversation memory on.
- **⛔ Wispr Flow sponsor plug, 13:41 → 14:34.** Disclosed partnership. Strip.
- **Tier 3 — Agent harness.** 🔴 **OpenClaw and Hermes named as the two leaders.** Letta
  named for long-term memory. The framing: *"instead of building an agent from multiple
  parts, you just install a complete, already powerful agent and then you customize it."*
- **Tier 2 vs Tier 3 tradeoff** closes the segment — harness if you want production-ready and
  can absorb setup, n8n if you want a reliable consistent flow.

Ends at 17:37. Tier 4 (full code) still ahead.

> ### 🔴 OpenClaw is named in the source transcript
> At **15:02** he puts OpenClaw as one of the two leading Tier 3 agent harnesses.
> The transcript RJ wants to borrow structure from already builds the exact frame the
> new workshop needs. See war question #7.

---

## Drop 5 — Telegram, Aug 20 2026, ~5:30 AM

Two pieces in one message. RJ closed with *"There's more context hold please."* **Still holding.**

### 5a. Transcript 17:41 → 21:21 ✅ VERBATIM — **THE VIDEO ENDS HERE**

Saved to `context/reference-transcript-agents-101.md` Part 4. Tier 4 full code + the
"How to Pick" close.

- **Tier 4 is the X-ray, not the recommendation.** He writes the loop in Python specifically
  so he can point back down the ladder: *"that's what's happening behind the scenes in all of
  those frameworks that we looked at. Same thing, the main loop."*
- **Same prompt, all four tiers.** *"go study the top AI YouTubers in 2026"* run four times.
  The constant task is what makes the tiers comparable.
- **🔴 OpenClaw named a SECOND time**, in the final verdict at 20:38: *"If you want a
  genuinely powerful agent that you can use for yourself that works in production... use a
  harness like Open Claw or Hermes agent."*
- **Closes on permission, not mastery:** *"even me as a technical guy, a lot of times I reach
  for something that's a lot easier to use because it's faster and I don't need the full
  control."*
- Also name-drops **Claude Code** (garbled as "a cloud code") inside the no-code tier.

### 5b. 🔴 RECRUITER BOTTLENECKS — 19 verbatim survey responses

**New context type. First audience data received.** Saved to `context/recruiter-bottlenecks.md`,
verbatim with typos preserved.

Answer to *"What's your biggest recruiting challenge today?"* Counted clusters: sourcing 6,
time 4, comms/follow-through 4, process/tooling 3, stakeholder mgmt 2, wrong-side-of-desk 1.

Three things worth flagging, **observation only**:
1. One respondent already diagnosed their own problem, tried to build it, and got stuck:
   *"I know our manual process... is a super simple process to automate with a workflow but
   I've been trying and can use some help."*
2. Two responses aren't tooling problems at all — *"not enough open roles"* and *"Finding a
   recruiter who will take my call"* (that person is hiring, not recruiting).
3. ~~**Nobody asked what AI is.** Every response is a named operational bottleneck.~~
   🔴 **RETIRED Aug 20 2026.** Argument from silence. The survey asked one question about
   bottlenecks. It never asked about AI, so the absence measures nothing. RJ, verbatim:
   *"i know i only gave you their bottle necks, and that's on purpose. duh they didnt ask
   about agent because we'll be tellin gthem in the workshop."* The dataset is deliberately
   scoped. **Every response is a named operational bottleneck** stands on its own as a
   description of the 19 answers. The inference drawn from the silence does not.

---

## Waiting on RJ (not to be chased — he's sending them)

- [x] ~~Luma link~~ — **received**
- [x] ~~Transcript 0:00 → 6:01~~ — **verbatim**
- [x] ~~Transcript 11:50 → 17:37~~ — **verbatim (drop 4)**
- [x] ~~Transcript 17:41 → 21:21 END~~ — **verbatim (drop 5). Transcript is complete.**
- [x] ~~Audience data~~ — **19 recruiter bottlenecks received (drop 5)**
- [x] ~~RE-PASTE 6:04 → 11:50~~ — **RESOLVED drop 7.** RJ sent the FULL transcript as a file.
      **The transcript is now 100% complete, 0:00 → 21:21, zero gaps.**
- [x] ~~**Apify API token**~~ — **received drop 6.** CLI authed as `conceptkitchen`, token in
      OS keyring, `credentials/ACCOUNTS.md` updated.
- [ ] **"There's more context hold please"** — RJ said more is coming. Holding.
- [ ] RJ's own examples (to replace that person's examples)
- [ ] Event partner's desired flow
- [ ] Syllabus changes
- [ ] RJ's "I'm done" signal → **then run full war**

---

## Drop 6 — Telegram, Aug 20 2026, ~5:36 AM

**Apify credentials.** User ID `ytt7rJpzMyzh7q4eY` + personal API token. Unblocks the drop-2
build order. CLI authed (`apify info` → conceptkitchen), token stored in the macOS keyring,
`credentials/ACCOUNTS.md` row added same-turn (Rule 44).

Security: the relay auto-saves every exchange, so the token had already been written in plaintext
to `memory/sessions/2026-08-20-telegram-live.md`, a git-tracked file. Repo verified PRIVATE (no
public leak), file backed up, token redacted, 0 matches remaining, line count unchanged.

🔴 **Constraint found:** `GET /v2/users/me` returns `plan: FREE`, `maxMonthlyUsageUsd: 5`.
~20 recruiters running live scrapers against a $5/mo cap is a failure point. **Observation only.
Not a proposal.** → war question.

Demo NOT built. The demo choice depends on the workshop shape RJ hasn't finalized.

---

## Drop 7 — Telegram, Aug 20 2026, ~5:40 AM

**THE FULL TRANSCRIPT, AS A FILE.** *"here look at this since you said it cut off."*

Saved permanently at `~/.claude-relay/knowledge/full-transcript-example-workshop.txt`.
Copied to `context/reference-transcript-FULL-VERBATIM.txt`. 853 lines, 29,371 bytes, 0:00 → 21:21.

**This closes the last gap in the transcript.** Recovered from 6:04 → 11:50: RAG named at 6:08,
the full agentic-loop narration 6:23–7:11, the four constant decisions verbatim 8:03–8:18, the
DataCamp sponsor block 8:25–9:49, the Tier 1 GenSpark demo 9:52–11:47.

**Authoritative chapter map extracted** (from the transcript's own embedded headers, not inferred) —
9 chapters, per-section durations, in `context/reference-transcript-agents-101.md`.
Headline number: **the foundation runs 8:25, 40% of the video, before a single demo.**

**Lesson:** two compactions destroyed chat-pasted context on this project. A file in
`~/.claude-relay/knowledge/` is immune. For large context going forward: file, not paste.

---

## Drop 8 — Telegram, Aug 20 2026, ~5:50 AM

### 8a. Recruiter bottlenecks — RE-SENT

RJ re-sent the same 19 responses. **Verified identical** to what was captured in drop 5 at
`context/recruiter-bottlenecks.md`. No new audience data, no diff. Nothing to reconcile.

### 8b. 🔴 WHY OPENCLAW — RJ's rationale, verbatim

> *"We're also using openclaw since thsi shit is free and though, my set up keeps it free with
> claudse subwcription, i canteach people free stuff like if they have open ai or google gemini
> or claude this way it's agnostic especially if they have mac or windows."*

Four constraints in one sentence. These read as **requirements**, not preferences:

1. **Free.** OpenClaw itself costs nothing.
2. **His setup stays free on a Claude subscription** — subscription auth, not metered API billing.
   Nobody watches a token meter run during a live demo.
3. **Model-agnostic.** Attendee brings whatever they already pay for: OpenAI, Google Gemini, or
   Claude. The workshop does not require anyone to buy anything new.
4. **OS-agnostic.** Mac or Windows. Both have to work in the room.

Closed with: *"there's more context please wait."* **Still holding.**

---

## Open questions to raise during full war (do NOT ask before he's done)

1. Two hours total with a short lecture — what's the shape of the rest? Hands-on setup time is the obvious candidate given the OpenClaw pivot, but RJ hasn't specified.
2. "Google Cloud provider" — confirm GCP specifically, and whether attendees need billing enabled (a real friction point for a room of recruiters with no cloud accounts).
3. Live setup in a room of non-technical people is the highest-risk part of any workshop. Needs a fallback path.
4. Does the existing site's structure survive the 30min → 2hr expansion, or does it need re-architecting?
5. The transcript's four-tier ladder (no-code → low-code → harnesses → full code) structurally
   rhymes with the OpenClaw pivot — "here's the landscape, here's your rung, now stand it up."
   Worth testing as the spine of the back half. **Observation only. Not a proposal.**
6. The transcript's four constant decisions (platform, model, context, control flow) are the
   most portable idea in it and survive any example swap. Candidate for the recruiter version.
7. **The transcript names OpenClaw at 15:02** as a Tier 3 agent harness, with the framing
   *"I'm not building this agent loop. It already exists... my job is kind of just to extend
   it, customize it, give it the right instructions, and connect any tools that I need."*
   That is a ready-made on-ramp to the OpenClaw setup block. The source material already
   argues for the thing RJ is pivoting to. **Observation only. Not a proposal.**
8. Every tier in the transcript ends by naming its own ceiling, which is what earns the climb.
   If the recruiter version only teaches one rung, the ceiling-naming move has nothing to
   hand off to. Worth deciding whether the ladder shows up at all or just the rung.
   **Observation only. Not a proposal.**
9. **The transcript's audience and RJ's audience were asked different questions.** The
   transcript answers *"what is an agent and which tier should I use."* The 19 recruiters
   were asked *"what's your biggest recruiting challenge today"* and every one of them named
   an operational bottleneck. Borrowing the structure means deciding what the structure is
   carrying. **Observation only.**
   🔴 **AMENDED Aug 20 2026.** The original said *"and none asked what AI is"* and concluded
   the two audiences *"want different things."* Both retired — argument from silence off a
   survey that never asked. Two different questions produce two different answer sets. That
   is all this compares.
10. **The transcript's close and RJ's setup block point the same direction.** His final
    verdict sends "want something genuinely powerful that works in production" to a harness,
    naming OpenClaw. RJ's session has attendees standing up OpenClaw on Google Cloud and on
    their own laptop. The source material argues for the destination. **Observation only.**
11. **RJ said the lecture stays short and the added time is not more lecture.** The 19
    bottlenecks are 19 concrete tasks in the audience's own words. Noting the adjacency
    without proposing what fills the time. **Observation only.**
12. **The foundation RJ said to keep runs 8:25 in the source — 40% of the video before a
    single demo.** Now measurable from the complete chapter map. "Keep the foundation" and
    "lecture stays short" are both direct instructions from RJ; in the source material they
    pull opposite directions. Not resolving it here. **Observation only. Not a proposal.**
13. **7:08 is the hinge:** *"everything else from here that I'm going to show you is really
    just a different way of building this type of loop."* One sentence converts the entire
    back half from four separate topics into four views of one idea already understood.
    The cheapest structural move in the transcript. **Observation only.**
14. **The source argues for RJ's format, in the sponsor block of all places (8:40):**
    *"You can watch me explain agents all day, and you're probably gonna forget most of it by
    tomorrow. / The stuff only sticks when you actually build it yourself."* The person whose
    structure RJ is borrowing says the lecture doesn't stick. **Observation only.**
15. **Apify is on the FREE plan, $5/mo hard usage cap.** If any live segment has ~20 recruiters
    running scrapers on RJ's account, that cap is the failure point. A fact the war needs on
    the table before any Apify-dependent block is designed. **Observation only. Not a proposal.**
16. **Drop 8's "free and agnostic" principle collides with #15.** RJ's stated rationale is that
    attendees use what they already pay for and buy nothing new. Any block that runs on RJ's
    credentials is off-principle before the cap is even reached — the cap is the second problem,
    not the first. **Observation only. Not a proposal.**
17. **Agnostic multiplies the setup surface.** 3 providers (OpenAI / Gemini / Claude) × 2 OSes
    (Mac / Windows) = 6 possible setup paths live in one room, and RJ has said attendees stand
    OpenClaw up on **both** Google Cloud and their own laptop. Noting the combinatorics without
    proposing how to handle them. **Observation only.**
18. **RJ's rationale is a constraint the source transcript does not carry.** The transcript's
    Tier 3 pitch at 15:02 is architectural — *"I'm not building this agent loop. It already
    exists."* RJ's is economic and practical: free, bring your own key, works on your OS. Same
    destination, different argument. Borrowing his structure means deciding which argument the
    structure carries. **Observation only.**

---

## Standing note

Prior standing constraint "workshop is OFF" is **REVERSED as of this voice note.**
Workshop is back ON, redesigned, 2 hours, OpenClaw-centered, recruiter audience.
