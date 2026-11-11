# Prose contract: writing less like a model

Source: Dodaios/ste80-humanizer (MIT; Pass 1 catalogue adapted from
blader/humanizer, MIT) compared against what press already ships
(`human-writing` skill, `overused-jargon` skill + watchlist, the
editorial-passes workflow's "named diseases"). Written 2026-11-11.

## What press already has, and what it lacks

| Layer | press today | ste80-humanizer | Gap |
|---|---|---|---|
| Stock words | `overused-jargon` watchlist (54 terms: load-bearing, blast radius, surfaces, lands, ship, verdict...) read by the jargon lint | §12 list (delve, leverage, robust, seamless, crucial, pivotal, showcase, underscore, tapestry, testament, landscape, utilize, meticulous, intricate, additionally) + `word-swaps.md` | Two lists barely overlap. Press's list is *engineering* jargon; the humanizer's is *assistant* vocabulary. A book needs both. |
| Rhetorical tells | editorial-passes `DISEASES`: epigram compulsion (maxim quota), uniform rhythm (X-not-Y, chiasmus, triplets), self-annotation | §1 not-X-but-Y, §2 one-line closers, §3 sayings that sound deep, §4 staged run-up, §5 arguing with no one, §6 forced triads, §9 stacked qualifiers, §13 inflated significance, §15 -ing riders, §18 serves-as/stands-as, §24 heading repeated, §25 writing about the document, §26 re-explaining the reader | Press names 3 diseases; the catalogue names 26, with "act on one sighting" vs "weak alone" weights. The weighting is the useful part: it stops over-correction. |
| Sentence structure | nothing mechanical; `human-writing` says "rhythm follows thought" | Pass 2 (S1-S15): one idea per sentence; 20/25-word caps; condition first; keep articles and "that"; active voice; simple tenses; verb not noun; no -ing chains; honest modals; one term per thing; noun stacks <= 3; one topic per paragraph, <= 6 sentences; procedure apart from description; warning before the step; no semicolons | **The missing layer.** These are exactly the rules of a good technical manual, and none of press's prose tooling checks them. |
| Mechanical check | jargon lint over the CSV; `house-rules.yaml` `banned-patterns` regexes | `scripts/ste_check.py`: passive / perfect / progressive / modal-passive regexes, sentence word counts with STE counting rules (a number+unit, identifier, quoted string = 1 word), tells list, phrasal verbs, strict-mode swaps; exit 1 on findings; `--json` | Press has the hook (`banned-patterns`) but no shipped pattern set for tells and no structural counter. |
| Fidelity | `human-writing` fact ledger (Known / Interpreted / Unknown) | "Keep every fact; keep certainty at its strength; never touch code, paths, numbers, versions; flag contradictions" | Same idea. The humanizer's version is terser and names the edits that drop facts most (§6, §9, §19). Worth quoting in synthesizer prompts. |
| Testing the skill | none | `evals/*/case.yaml` + `graders/*.md` (keeps-all-facts, no-staging-tells, no-semicolons, short-sentences, stays-casual) | A pattern press's prose skills could adopt to prove a revision pass did not flatten or invent. |

## The 80% rule, and where it bends for a 1999 technical book

Karpathy's framing: ask for "80% of the way to ASD-STE100". Keep all of the
structure, only as much of the vocabulary as still sounds natural. For the
O'Reilly-era voice the structure rules stay and three vocabulary rules relax:

- "however", "therefore", "whether" are period-correct and stay.
- "we recommend", "should" for advice stays; the house voice gives advice.
- Average sentence 16-22 words, hard ceiling 30; vary it. STE's 25 is the
  target, not the law, because a 1999 manual breathes a little more.

Never relaxed: one idea per sentence, active voice with a named actor,
simple tenses, no -ing riders, one term per thing, no semicolons, no dashes,
warning before the step, every fact kept at its strength.

## The prompt block (paste into every chapter brief and revision pass)

```text
PROSE CONTRACT

Write like a senior colleague who ran this system in production and is not
selling it. Second person, present tense, plain words. Explain the why and
the history. One understatement every few pages; never a pun in a heading.

Pass 1, do not write these (one sighting is a defect):
- "not X but Y" / "not just X, it's Y" / "This doesn't mean X. It means Y."
- a one-line closer that repeats the paragraph ("That's the real win.")
- a saying dressed as depth ("at its core", "X is the Y of Z")
- a staged run-up ("Let's", "Here's the thing", "dive in")
- arguing with nobody ("To be clear, I'm not saying", "You might think")
- a forced triad; three only when the thing has three parts
- stacked hedges ("could potentially", "in some cases it may")
- the assistant words: delve, leverage, robust, seamless, crucial, pivotal,
  showcase, underscore, tapestry, testament, landscape, utilize, meticulous,
  intricate, additionally, streamline, empower, harness, foster, navigate,
  game-changer, unlock, journey, comprehensive, vibrant, key (adj.)
- inflated significance ("marks a pivotal moment", "the future looks bright")
- an -ing rider bolted to a fact ("..., ensuring", "..., highlighting")
- serves as / stands as / boasts / features / represents, for is / has
- bold labels with colons on every list item; decorative headings
- a heading repeated as the first sentence; text about the document itself
- the engineering jargon on press's watchlist (load-bearing, blast radius,
  footgun, surface(s), lands, ship, verdict, drift, parity, clean, ...)

Pass 2, how every sentence is built:
- one idea per sentence; two linked facts may share one with "and"/"because"
- 16 to 22 words on average, never more than 30; vary the length
- condition first, then the command ("If the check fails, the build stops.")
- active voice; name who acts (press, pandoc, LuaLaTeX, you)
- simple tenses only: present, past, "will", imperative
- the action in the verb: "decide", not "make a decision"; no -ing chains
- honest modals: can, must, will; "may"/"should" only for real uncertainty
  or advice
- one term per thing for the whole book (a "target", never also a "task",
  "step", "stage"); define a term once, in italic, then reuse it
- at most three nouns in a row
- one topic per paragraph, six sentences at most, topic sentence first
- procedure apart from description; a warning before the step it protects
- no semicolons, no em or en dashes; use a period, comma, colon, or
  parentheses

Fidelity:
- every fact from the fact base, at its stated strength; add nothing
- code, commands, paths, flags, YAML keys, numbers, versions verbatim
- a contradiction in the sources is reported in a note, not resolved by
  invention

Era: Unix, e-mail, Web site, filename, manpage, appendixes, "at the time of
this writing", man-page references like make(1). No emoji, no "folks", no
"spin up", no dark terminals.
```

## Mechanical enforcement in the book (press-native)

1. `config/house-rules.yaml` `banned-patterns` carries the one-sighting tells
   as regexes, so `press check` refuses them on every build:

```yaml
banned-patterns:
  '\bnot (just|only|merely|simply) [^.;:]{1,60}\b(but|it is|it'"'"'s)\b': "not-X-but-Y staging (humanizer §1)"
  '\b(Let'"'"'s|Let us) (dive|take a look|explore|break)': "staged run-up (§4)"
  '\b(Here'"'"'s the thing|Honestly\?|Real talk|without further ado)\b': "staged run-up (§4)"
  '\b(To be clear|I'"'"'m not saying|Don'"'"'t get me wrong|One might be tempted)\b': "arguing with no one (§5)"
  '\b(delve|delves|delving|leverag(e|es|ing)|robust|seamless(ly)?|crucial|pivotal|showcas(e|es|ing)|underscor(e|es|ing)|tapestry|testament|utiliz(e|es|ing)|meticulous(ly)?|intricate|streamlin(e|es|ing)|empower(s|ing)?|harness(es|ing)?|foster(s|ing)?|game-changer|unlock(s|ing)?)\b': "assistant vocabulary (§12)"
  '\b(serves|stands|functions|operates) as\b': "avoiding is/has (§18)"
  '\b(boasts|boasting)\b': "sales verb (§18)"
  '\b(it is|it'"'"'s) (important|worth) (to note|noting)\b': "filler (§12)"
  '\b(marks|marked) a (pivotal|crucial|key) (moment|step)\b': "inflated significance (§13)"
  '\b(stands|is) a testament to\b': "inflated significance (§13)"
  '\bthe future looks bright\b': "send-off (§13)"
  '[—–]': "em/en dash (§8); use a period, comma, colon, or parentheses"
  ', (ensuring|highlighting|underscoring|showcasing|fostering|reflecting) \b': "-ing rider (§15)"
  '\b(deep dive|spin up|footgun|under the hood|out of the box)\b': "modern idiom; breaks the 1999 register"
```

   (Semicolons are not banned by regex: code blocks and YAML contain them.
   The structural checker handles prose semicolons.)

2. `tools/ste_check.py` (vendored, MIT, with its notice) runs over every
   chapter in the book's pre-commit and in the writer's loop:
   `python3 tools/ste_check.py chapters/*.md`. Findings are review material,
   not a hard gate: it is a heuristic, and quoted output and tables trip it.
   The hard gate is `press check`.

3. `tests/known-bad/` gets one fixture per pattern family so press proves
   the rules fire (the press rule: every fixture must be rejected on every
   build).

## What press itself should adopt (filed as a GitHub issue)

1. `human-writing` skill, v2.1: add a "Structure" section with S1-S15 at 80%
   and the one-sighting / weak-alone weighting from Pass 1 (credit MIT).
2. Ship an opt-in `ai-tells` pattern set the scaffold can lay into
   `house-rules.yaml` (commented out), and a universal known-bad fixture for
   it.
3. A structural prose lint (sentence length with STE counting rules,
   passive/perfect/progressive/modal-passive, semicolons in prose, noun
   stacks, paragraph length) behind a `house-rules.yaml` knob such as
   `prose-structure: {max-sentence-words: 30, max-paragraph-sentences: 6}`,
   reported like the jargon lint. `ste_check.py` is a working reference.
4. editorial-passes `DISEASES`: add not-X-but-Y, one-line closers, -ing
   riders, stacked hedges, and serves-as verbs, each with the "act on one
   sighting" or "weak alone" weight so synthesizers do not over-correct.
5. Evals for the prose skills in the humanizer's shape: a prompt, a case,
   and graders for keeps-all-facts, no-staging-tells, short-sentences,
   stays-in-register. Press has a mutation ratchet for code and nothing
   equivalent for prose passes.
