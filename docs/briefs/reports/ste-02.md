# STE80 desk report: Chapter 2, Installing press

File: `book/chapters/02-installing-press.md`. Mode: Humanize for body prose,
Light for the sidebar "The first-run font scan". `press check` passes.

## Ratchet count

- Before: 7 (baseline in `tools/ste-baseline.json`: 7)
- After: 6

## Edits (line numbers are in the edited file)

1. Line 15, S1/S2 (26 words, two ideas).
   Old: "The second half is a set of programs that press calls to do the real typesetting and checking, and press does not install those for you."
   New: "The second half is a set of programs that do the real typesetting and checking. Press calls them, but it does not install them for you."
2. Line 33, S2 (28 words).
   Old: "At the time of this writing, the press's continuous integration (CI) runs all five Python releases from 3.10 to 3.14 on Ubuntu, plus Python 3.12 on macOS 15."
   New: "At the time of this writing, the press's continuous integration (CI) runs all five Python releases from 3.10 to 3.14 on Ubuntu. It also runs Python 3.12 on macOS 15."
3. Line 87, S8 ("-ing" form, ratchet lead) and S3 (condition first).
   Old: "You can also install a clone that lives somewhere else by naming its path."
   New: "To install a clone that lives somewhere else, name its path."
4. Line 136, S1/S2/S6 (28 words, an appositive holding a second clause; the workflow named as the actor).
   Old: "The *composite action*, the piece of the press that the reusable workflow runs to install it, installs press from the action's own checkout, never with pip from Git."
   New: "To install press, the reusable workflow runs the *composite action*, a piece of the press itself. The composite action installs press from its own checkout, never with pip from Git."
5. Line 138, S2 (27 words) and S13 (the paragraph would have reached 7 sentences, so it splits at its turn from what CI does to why).
   Old: "That choice keeps a private book working without a token for a second repository, and it pins the installed press to the exact ref of the action."
   New: (new paragraph) "That choice keeps a private book working without a token for a second repository. It also pins the installed press to the exact ref of the action."
6. Line 142, S1 (three actions in one sentence).
   Old: "Press prepares the manuscript, decides what to build and in what order, and hands the work to older, specialized programs."
   New: "Press prepares the manuscript and decides what to build and in what order. Then it hands the work to older, specialized programs."
7. Line 173, S8 ("-ing" rider).
   Old: "A few more programs help press without appearing in the doctor's report."
   New: "A few more programs help press, but the doctor's report does not list them."
8. Line 192, S2 (29 words).
   Old: "An EPUB fault that you see on your own machine costs you a minute, and the same fault that you first see in CI costs you a round trip."
   New: "An EPUB fault that you see on your own machine costs you a minute. The same fault costs you a round trip when you first see it in CI."
9. Line 222, S1 (an appositive nested inside a relative clause).
   Old: "It runs the same toolchain image, pinned by the same digest, that the press's *release contract*, the workflow that proves each press tag, proved."
   New: "It runs the same toolchain image, pinned by the same digest, that the press's *release contract* proved. The release contract is the workflow that proves each press tag."
10. Line 258, S1 (three clauses after a colon).
    Old: "@fig:doctor-report shows the case: `claude` is optional, `press all` does not need it, and the doctor still reports `not ready: claude` and exits 1."
    New: "@fig:doctor-report shows the case. There, `claude` is optional and `press all` does not need it, but the doctor still reports `not ready: claude` and exits 1."
11. Line 301, S1 (three actions in one sentence).
    Old: "The command mounts the book repository at `/book`, installs press inside the container, and runs `press all`."
    New: "The command mounts the book repository at `/book` and installs press inside the container. Then it runs `press all`."
12. Lines 329 and 331, S13 (one topic per paragraph): the paragraph splits between how the script runs (mount, no reinstall) and its arguments and options. No sentence changed in the split.
13. Line 331, S8 ("-ing" form).
    Old: "and `--shell` opens a shell in the container instead of building."
    New: "and `--shell` opens a shell in the container instead of a build."
14. Line 383, S2/S5 (26 words, two options in one sentence).
    Old: "Install it with Homebrew or apt as Examples 2.4 and 2.5 show, or accept the local warning and let the toolchain image run the strict gate."
    New: "Install it with Homebrew or apt, as Examples 2.4 and 2.5 show. You can also accept the local warning and let the toolchain image run the strict gate."

## Leads declined

- Line 35 (ratchet line 34), sentence-length 37: a counter artifact. The footnote reference `[^2-yaml]` follows "stays a string." with no space, so the counter joins two sentences. Each real sentence is under 20 words. Moving the footnote reference would touch markup for no reader benefit.
- Line 98 (ratchet line 97), phrasal verb "check out": the verb is Git's own operation (`git checkout`). A synonym would be less exact.
- Line 192 (ratchet line 191), sentence-length 33: a counter artifact. The quotation ends with its period inside the quotes, so the counter joins it to the next sentence. The real sentences are 12 words plus the quotation, and 20 words.
- Line 363 (ratchet line 362), passive "is broken": "broken" is an adjective (the doctor's `BROKEN` state), not a passive.
- Line 369 (ratchet line 368), paragraph-length 7, the sidebar "The first-run font scan": Light mode. The sidebar is three short paragraphs in print, at about 130 words, under the 190-word limit. No sentence is over 30 words, has three ideas, or carries a semicolon. The counter also folds the sidebar title into the first sentence and splits the scars-list quotation at its colon. Merging sentences to satisfy the count would cost the voice the sidebar is there for.
- Line 386 (ratchet line 382), "-ing" form "including": a preposition, not a verb form.
- Line 196 (Debian section opener), 25 words: at the limit, not over it, and it holds one idea with its reason.

## Passives kept

- Line 222, "pinned by the same digest": a participle that describes the image. The actor (the reusable workflow) is named a section later, and naming it here would add a clause to a sentence this pass shortened.
- Line 226, "the extra items listed after it": the actor is the book itself, and it does not matter.

## Fidelity notes

- Edit 4 changes "the action's own checkout" to "its own checkout", with the composite action as the antecedent. It replaces "the piece of the press that the reusable workflow runs to install it" with "To install press, the reusable workflow runs the composite action, a piece of the press itself". Both facts (the action is part of the press, and the workflow runs it to install press) remain.
- Edit 9 moves the definition of *release contract* from an appositive into the sentence that follows the italic first use. `docs/vocabulary.md` asks for the definition in the same sentence. Here it is in the very next sentence.
- Semicolons remain only inside three quotations from the press's install guide, which stay verbatim.
- The sentinel phrases do not occur in this file. The index terms in the edited sentences ("continuous integration", "composite action", "reusable workflow", "release contract", "toolchain image", "epubcheck") keep their spelling, and `press check` passes with zero-hit index terms enforced.
