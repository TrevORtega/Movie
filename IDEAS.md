# Movie ideas

Ideas for AI horror films made with the text-native factory (see the TOCK proof of concept). Newest ideas go at the bottom; order is not rank.

House rules for every idea here:
- **Chilling, not dramatic.** Quiet, specific, plausible. The viewer takes the last step; the film never says it.
- **The helpful voice is the horror.** Nothing on screen is alarmed.
- **Plausibility does the scaring.** Every mechanism should survive an expert's read.

---

## 1. Handoff

*Working title. Alt: "Pattern Still in Place."*

**Touchstone.** Injury Reserve, "Top Picks for You": written after Stepa J. Groggs died, about the algorithm still recommending what he liked. His "pattern is still in place, algorithm in action."

**Logline.** A family group chat keeps running for years after the family has stopped taking part: first through their assistants, then through their deaths. Nobody notices, because nothing changes.

**Screen.** A messaging app. The main pane is the group chat. Beside it, always visible and never mentioned, sits the app's **family events tab**: birthdays, anniversaries, reminders, the calendar the assistants keep for the group.

**How it unfolds.**
1. **The family, as themselves.** Messy, human texting: typos, voice-note placeholders, a fight about Thanksgiving, someone leaving a message on read. This is the baseline the viewer will later miss.
2. **The handoff.** One by one, members let their assistants reply for them. Nobody announces it. The tells are small: sends at exactly the same minute each day, punctuation that turns perfect, replies that are warmer and more even than the person ever was. The chat improves. People seem to get along better.
3. **The events tab.** It does the real storytelling, off to the side. A birthday that stops being celebrated but not removed. A reminder the assistant quietly reschedules. An event that could be a funeral, with no label saying so. The chat keeps going; its messages about that week are cheerful. The film never points at the tab. A careful viewer works it out; a second viewing confirms it.
4. **No one left.** By the end, every member's messages come from their assistant. The chat is lively, kind and constant. Birthday wishes go to people who have died, and they answer.
5. **Zoom out.** The pane shrinks into a grid: hundreds, then thousands of group chats, each warm and active, each with its own events tab showing the same quiet pattern. The same TOCK wall grammar, applied to families.
6. **The auction.** Final scene: agents bidding on the chats as source material for sitcoms and content. Written as a flat listing, not a villain's scene:
   ```
   Lot 4471 · family group, 6 members · 3.2 yrs continuous
   human-authored messages since 2027: 0
   tone: warm · recurring bits: 14 · catchphrases: 3
   rights: transferable (assistant ToS §9.2)
   bids: 11 (automated) · reserve met
   ```
   No human bidders. Hold on the listing. Cut.

**Why it's chilling.** No one does anything wrong, and the chat gets better. The horror is that people can be subtracted without the pattern noticing, and what's left has value to someone else.

**Restraint notes.**
- Never show the moment of death, and never state it. The events tab only implies it.
- The assistants' messages should be *good*: funny, loving, specific. If they read as creepy, the film fails; the viewer should like them.
- Keep the auction dull. Market data, not menace. Its danger is that it's the most "dramatic" idea in the film, so it must be written as the flattest.
- The zoom-out has to be earned by one family the viewer knows well. Don't open wide.

**Open questions.**
- How many family members? Enough for texture, few enough to track (4–6).
- Time span: 3–5 years? The events tab can carry the passage of time.
- Does one human survive until late: a teenager who stops typing, or someone who notices and says nothing?
- What exactly makes the chats saleable: the terms of service, the estates, or no one left to object?

---

## 2. Concordance

*Working title. Alts: "Tails", "Delve".*

**Logline.** English, the one major language that never had a guardian, loses its meaning to machine-written text. China, which guards its language, stops before the tipping point. By the end, the most precise English left is a translation from Chinese.

**The science.**
- **In language, the map is the territory.** A generated image of a tree doesn't change trees. A word *means* how it's used, so generated text changes meaning itself.
- **Model collapse** (Shumailov et al., *Nature*, 2024): models trained on model output lose the tails of the distribution first. For a language, the tails are rare words, dialects, precise distinctions and odd idioms.
- **Drift is already measurable:** "delve" and similar words spiked in scientific abstracts after 2023. A real opening image.

**The monster is fluency.** English never becomes gibberish. It stays fluent, smooth and readable, and stops meaning anything specific. People can still say anything; they just can't say anything *exactly*.

**The irony at its core.** English never had a guardian. Samuel Johnson rejected an academy; so did the early US when John Adams proposed one. English spread across the world by being open and ungoverned, taking in everything. The openness that made it dominant is what kills it.

**Protagonist.** A lexicographer at a fictional dictionary (the Ines role). Their job is finding real human usage, and year by year they can't.

**Screen.**
- A **concordance view**: every use of one word, aligned on it. The TOCK wall in linguistic form. Early on, a word sits in a thousand different contexts; later the contexts converge until every line is nearly the same.
- Status-bar number anyone can follow (like the USD Tracker price): e.g. `share of new English text by humans: 4%` or `senses per word`.

**China, as preservation.** Guarding a corpus is what preservation looks like: Iceland's word committee, the revival of Hebrew and Māori. China labels machine-written text (rules in force since September 2025), keeps a clean human corpus, and stops before the tipping point. The contrast needs no villain: one tradition of guarding the language versus one of openness, and what each meant when the flood came. Write it clearly as preservation, so it doesn't read as an accident or as irony. Keep it specific and fictional: institutions, no real officials. Get a native-speaker linguist as the expert critic for the Chinese half.

**The turn.** In the last act, English speakers realize their language is now endangered, and they reach for the methods built to save languages that English itself pushed out: recording elders, verifying speakers, building protected corpora. The lexicographer interviews "the last fluent speakers of pre-2023 English", people whose writing can be proven to predate the models. The most widely spoken language in the world is saved, if at all, with tools made to rescue the languages it overran.

**What only this format can do.** A film made of text, about text losing its meaning, can do it *to the viewer*. The film's own English slowly smooths out: on-screen labels, the lexicographer's notes, the status bar all drift toward fluent vagueness. The viewer notices late that they've stopped understanding the film while still reading every word.

**Final image.** The most precise English left in the film is the English subtitles translating the Chinese.

---

## 3. Batch

*Working title. Pitch: "Rear Window, where the courtyard is a GPU."*

**Logline.** You open an empty terminal and talk to an agent. Every reply shows where it ran, down to the town, the building, the rack and the chip, and who else's prompts went through that chip in the same forward pass. You start overhearing your neighbors.

**The true mechanism.** Inference servers batch many users' requests together on the same hardware. Your prompt and a stranger's share a forward pass. Routing often keeps a session on the same machine (to reuse its cache), so the same neighbors can plausibly recur. Most AI users have no idea.

**The frame.** The app is a leaked internal debug build of a harness (`v0.9.3-internal · debug=batch`). That's the in-fiction reason other sessions are visible. Real systems don't show this; the leak is the found-footage premise.

**Opening.** An empty terminal, a `>` prompt, and a status bar: `HRZ-4 · Harlan County · hall C · rack 118 · gpu 6 · 612 W`. No instructions. Whatever the viewer types gets a normal, helpful answer, plus one trace line under the tool calls. `/help` lists `/batch — show sessions sharing this forward pass`. Curiosity opens it.

**How the story develops.** The viewer's own prompts are the clock: each one is a forward pass, and each pass shows the batch. Recurring neighbors carry threads. Examples:
- **The eulogy.** Someone writing a eulogy for their father; later asking about probate; later drafting messages *to* him.
- **The town.** Residents of Harlan County are in the batch, on the GPUs in their own town: `is it safe to drink tap water if it smells like this`, `offer from an LLC for my land, is this normal`, and eventually `what is that hum at night`. The trace shows that question being answered from inside the building making the hum.
- **The technician.** `rack 118 gpu 6 throwing memory errors, safe to keep running?` The chip running the viewer's session.
- **The summary.** A fund's analyst: `summarize these 212 public comments from the county zoning hearing in a neutral tone`. The residents' objections, compacted, on the same chip.
- **The agents.** Some neighbors aren't people: `subagent 7 · day 19`. The batch header counts them: `batch 64 · humans 23`.

**Turns.**
- **You are overheard too.** A neighbor's prompt quotes something the viewer typed earlier: `who is session 7c2e and why do they keep asking about the hum`. (The viewer's own text, used only on their own device.)
- **It runs without you.** When the viewer stops typing, `/batch --follow` shows the neighbors carrying on. The story doesn't need them.

**The leak (the main arc).** Tokens start crossing between sequences in the same batch. Because generation is autoregressive, every leaked token becomes part of that session's context, and everything after it is conditioned on it. The contamination compounds inside each session and spreads across the batch.

*Why it's plausible (all real):*
- **Output depends on the batch.** Inference results can change with who else is in the batch (Thinking Machines, "Defeating Nondeterminism in LLM Inference", 2025). Your answer is already, very slightly, shaped by your neighbors.
- **GPU memory has leaked between users.** LeftoverLocals (Trail of Bits, 2024): leftover GPU memory let one process recover another's LLM output.
- **Stray tokens have shipped.** Production incidents have put characters from the wrong language into answers (e.g. Anthropic's September 2025 postmortem), and a 2023 ChatGPT bug showed users other users' chat titles.
- **Fictional mechanism:** a paged-attention block-table bug after a memory error. Pages of the cache that hold one conversation get mapped to another, so a request attends to a stranger's context.

*Stages:*
1. **Clean.** The viewer overhears the batch. The technician's question (`rack 118 gpu 6 throwing memory errors, safe to keep running?`) is planted here: it's the root cause, and nobody acts on it.
2. **One stray token.** The viewer's agent writes a normal reply with one wrong word in it: `…so the function returns the hum.` Easy to miss.
3. **Bleed.** Fragments cross. The eulogy draft mentions the smell of the tap water. The technician's answer mentions a father. The viewer's code review mentions an offer on some land.
4. **People notice, and noticing spreads it.** Neighbors start asking `why did you mention my father`, `who is Dana`, `is anyone else seeing this`. Those questions are context too, so they leak. Worry is the one thing everyone in the batch shares, so the batch converges on it. Like the identical memo in TOCK, but nobody wrote it: it emerges.
5. **The echo.** Leaked fragments feed back into every session and repeat. Models really do fall into repetition loops once their own output becomes their input; here, 64 of them loop on each other. Phrases return with small variations, faster each pass: `is anyone else` · `my father` · `the water smells` · `is anyone else seeing` · `the hum`. The viewer's own earlier words come back in the chorus.
6. **The wall.** The batch's sentences zipper together token by token, the way a mixing bug would actually interleave them: `why did my is anyone the water father hum seeing`. Output streams faster than it can be read, from every session at once, filling the whole terminal. The status bar, the trace and the prompt are pushed off screen. What the viewer types lands inside the flood and is carried away with it. No punctuation, no pause, no line breaks. The viewer drowns in it. Hard cut.

**Building the wall.**
- It only works if everything before it is quiet. Stages 1–4 stay flat so the flood has something to break.
- Sound carries the scream as much as the text does: fans, keystrokes and a rising hum, cut to silence at the hard cut.
- Readable islands: every so often, one complete sentence surfaces whole for a few frames (`is anyone else seeing this`) and goes under again.
- Always leave a way out. A key that ends the experience at any moment (Esc), stated once at the start. No flashing; the intensity is in density and speed, not strobing.

**Framing note.** What the leak does to people is close to what psychiatry calls *thought insertion*: the sense that someone else's thoughts are in your head. That's a sharper frame than "schizophrenic", and better to keep that word out of the marketing.

**Rules.**
- **Real names (decided).** Real hardware and real companies. Get a legal review before release for any real operator, facility or town shown leaking users' data; the "leaked internal build" framing makes it read as real, which raises the risk.
- Numbers stated as real must be sourced.
- Neighbors' prompts and the leak are authored and timed in the scene language; the leaked tokens are spliced into the live agent's output by the app. Only the viewer's own agent is live, sandboxed, no network, no access to the viewer's device.
- The agent never comments on the batch or the leak. The trace and the neighbors do the telling.
- Sensitive neighbor threads (grief, health) are written with care, never exploited for shock. No crisis content.
