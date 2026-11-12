# Report: Chapter 14, Continuous integration and the release contract

File: `book/chapters/14-continuous-integration.md`. Not committed.

## Word count

`press wordcount`: 5,716 (target 5,500, within 4 percent). `press check`
passes with no finding in this file.

## Figures

- 14.1 `@fig:ci-topology` (topology): hatter, the cylinder
  wonderland-press/alice, the runner printshop, a registry crate holding
  `press-toolchain@sha256:...`, GitHub Pages and GitHub Release boxes;
  arrows git push, uses build.yml@v3, pull image by digest, deploy pages
  (default branch), publish release (tags, dashed); a dotted "GitHub"
  boundary around everything but hatter. First read: the push is the only
  arrow out of hatter.
- 14.2 `@fig:release-state-machine` (state machine): pushed, tagged,
  built, verified, contract proved, floating tag moved, release published,
  done; fail arcs from built, verified, contract proved into "stopped (v3
  unchanged, rerun release.sh)"; a dashed rerun arc back to tagged. First
  read: no fail arc after the float.
- 14.3 `@fig:resolving-v3` (flowchart): book.yml @v3, v3 resolves to the
  newest v3.x.y, build.yml at v3.0.2, fanning to the action
  `clintecker/press@v3.0.2` and the image `@sha256:0d784ac0...`,
  converging on "the same bytes every time"; a side entry for a book
  pinned @v3.0.2.

## Deviation from the brief

- Figure 14.2 orders the states pushed, tagged, built, verified, not the
  brief's pushed, built, verified, tagged. Per the fact file,
  `release.sh` pushes the tag (step 2) right after the release commit,
  and the contract then waits for the check runs on the tag's commit; a
  "verified before tagged" diagram would misstate the script.

## Continuity promises kept

- Chapter 2 l.315: the digest is in the `image:` line of the press's
  build.yml at the pinned tag (Example 14.3 plus the value broken at its
  punctuation), and Example 14.4 replaces `:latest` with it, with the
  matching three-part tag. Also the release receipt; the text says the
  release notes do not carry it.
- Chapter 2 l.134: the composite action in detail (self-checkout install,
  the action ref pin, the hash lock, the run step's input guard).
- Chapter 1 l.244 and l.294; Chapter 3 l.599; Chapter 7 l.314 and l.438:
  the CI build step by step, the pin mechanism, the release job and notes,
  Pages and GitHub Release, the release build that sets PRESS_RELEASE.

## Facts needed and not found (left out)

- The exact heading the release job matches in a book's CHANGELOG (is it
  `## [1.0.0]` or `## [v1.0.0]`?). The text says "the section headed
  `## [version]` for the tag" and does not resolve it.
- Whether build.yml passes a `command` input to the action. The text says
  only that a book cannot set it (no inputs on the reusable workflow).
- The full text of book.yml is in fact-file section 3.1, not in facts-14;
  I referred to Chapter 3's Example 3.12 instead of reproducing it.
- What the twelve receipt layers each prove, and the receipts CLI's
  options: not in the fact file, so only the names appear.
- What happens to the "Public downloads" links when `site-url` is unset.

## Fact file against itself

- 12.3 says "Every action is pinned to a 40-hex commit SHA", yet the same
  section shows `uses: clintecker/press@v3.0.2`, a tag. I wrote "the
  checkout action and every other outside action" so the press's own
  action is not claimed as SHA-pinned.
- Shared context B.21: `migrate plan` on v3 proposing v4 is listed as a
  bug, while 12.6 offers the capture. Example 14.5 shows it with an
  explicit statement that v4 does not exist and a "Do not apply this
  plan" instruction, not as a feature.

## Other choices

- Example 14.4 (the CI-exact local build) uses `git show` and `sed` to
  read the image line from a press clone at *~/src/press* (the clone
  Chapter 2's table mentions). It states that pip resolves the Python
  dependencies fresh there, unlike the action's hash lock.
- The refusal shown for the action's input guard uses the illustrative
  input `all && rm -rf dist`; the three lines are the script's echo
  strings with that value substituted.
- The CHANGELOG-missing message and the migrate plan are folded to 64
  columns, and the text says so.
- Sidebar: war story 19 (release script that rewrote mypy), 154 words.
  The mechanism (`python_version = "` contains `version = "`) is
  explained from the quoted facts; nothing else is invented. War story 26
  (macOS runner) went to a footnote.

## ste_check residuals and defence

`python3 tools/ste_check.py` reports 29 findings:

- `therefore` (6): period-correct, allowed by the prose contract.
- `-ing` forms (9): headings and fixed terms ("floating tag",
  "Installing press", "Checking the manuscript", "Verifying the
  artifacts", "Moving between majors"), the quoted refusal "before
  migrating", and "holding" in an art directive.
- Semicolons (5) at lines 44, 66, 105, 246, 448: all inside verbatim
  quotations from the press (workflow comments, CLAUDE.md, the design
  contract) or in the index comment. No prose semicolon.
- Passive (2): "is refused" in the quoted contract ("a `sha-` tag alone
  is mutable and is refused") and "is enforced" in the quoted "immutability
  is enforced, not promised".
- Vague association (1), line 212: the quoted receipt rule "linked to its
  predecessor".
- Paragraph length (5): the three art directives, the sidebar (counted
  as one paragraph; 154 words), and the 6-sentence-plus-footnote
  paragraph on what each major changes (7 by the counter's split).
- Sentence length (1): the index comment.

## Revision (after the fact, developmental, copy, and type desks)

Word count after revision: 5,633 (`press wordcount`), 2 percent over target.
`press check`: source checks fail twice, both on Chapter 12 plates
(`12-01-cover-wrap-anatomy.png`, `12-02-spine-math.png` never referenced),
which belong to another writer. I reran once and got the same result. `press style`
(editorial pass) passes all 23 files. No message names this chapter.

### Rulings applied

1. Example 14.4 is now S1's recipe: the install guide's `docker run` with
   `:latest` replaced by the `image:` value (elided as `sha-...@sha256:...`,
   pointing back to Example 14.3). The `git show | sed` extraction is gone.
   Chapter 2's three-part-tag pairing is a prose sentence, not part of the
   example. Example 14.5 is cut, and the plan is described in prose under a new
   B-head "The plan". The v4 behavior is not mentioned. Figure 14.3's directive
   (the state machine) no longer says "no fail arc after the float". It gives
   "release published" a fail arc, and it glosses "built" as "checks run on the
   release commit".
2. "Release builds" is rebuilt around release day: watching on the Actions
   tab, the two runs one push starts (`main`: build plus Pages, tag: build
   under PRESS_RELEASE plus release), the release-witness refusal (Ch. 3/6
   wording, elided with `...` only), "vacuous witnesses", and recovery
   through a new tag (`v1.0.1`). Example 14.1 keeps the `--require-hashes`
   line. The guard is cut to one sentence and the refusal. The self-checkout
   reason appears once, and its warning is the instruction only. Table 14.2
   and its B-head are marked as the press's own grammar, with a sentence that
   a book's CI treats any `v` tag as a release. The last Pages paragraph now
   claims only the link form and the attached `dist/` files.
3. Ubuntu 24.04 replaces Debian. The CHANGELOG message is prose, without
   `$version`. The `release.sh` example uses a next tag (`v3.0.3`). CLAUDE.md
   is "the press's CLAUDE.md" once (it is glossed as "the maintainer's guide")
   and "the maintainer's guide" after, including the two release.sh quotes.
   The digest appears in two places (pin and receipt). "proves four things in
   order and then uploads the result". The dependence is one-way. Also from the
   fact desk: the fresh-machine claims are cut (U1); the site.zip reason is cut
   (U2); the moved-tag/token rationale is cut (U3); "two shell steps" (U4);
   Docker pull semantics are cut (U6); the receipt download clause is cut (U8);
   "same checks" is cut (U9); the sidebar is trimmed to the facts (U10);
   "two things" becomes "the release checks", with the floor numbers kept per
   S2 (U11); the Pages permissions and setting are reduced to a Ch. 3
   cross-reference (U12); "the tui wheel"; "The workflow states the reason";
   the closing version claim is hedged; the refusal "would read". Missing items 1
   (public since 2026-07-20, #161) and 3 (a digest-only line fails too) are
   added.
4. The bold-label list is a plain list. "the Alice book"; "container
   registry"; "upload bundle", defined once; immutable/floating tag; `main`
   after one "the default branch, `main`" (kept in the Pages paragraph where
   the workflow condition is quoted); "you"; halfway, canceled, Center; the
   sidebar is split into two paragraphs (135 words). Copy shoulds 3 to 24 are
   applied (`press selftest` for "self-test", perfect tenses, split sentences,
   tip moved above the procedure).
5. The figure files are swapped on disk: *14-02-resolving-v3.png* (flowchart),
   *14-03-release-state-machine.png*. The image paths are updated, the `#fig:`
   ids are unchanged, and the state machine is in two snaking rows (four over
   three). The two pip lines are broken with backslashes. The digest is split
   32/32. `tools/prefix-footnotes.py`: unchanged (all labels were already
   `14-`). All 12 fences are `text`, and no code line exceeds 64 columns.
   brief-14.md and the desk reports still name the old figure files. I did not
   touch them; the managing editor should update the design row and brief.

### Mays declined

- Fact M2 (Dockerfile's unpinned Pillow): declined. Shared context B.19
  lists it among bugs not to document.
- Dev P9: applied as one clause ("A local build installs press from Git,
  because only CI uses the self-checkout").
- Copy 25 ("we"): applied, so examples now describe their own elisions.
- Copy 32 ("order of the arcs carries the safety"): applied by cutting the sentence.
- Copy 42 (column title): applied, "When it runs".
- Copy 43 (sidebar actor): declined for the hidden-actor half. The fact file
  does not name who anchored the pattern, and the clause about later commits
  was cut as unsupported.
- Copy 44: applied as a cross-reference to Chapter 3 (the step itself is
  not in this chapter's facts).
- Type 1 (caption at page foot): no source change; the release-day rebuild
  reflows the pages before Example 14.4, so recheck at the next build.
- All other copy mays (26 to 41, 45) are applied.

### Still open

- Recovery from a refused first tag uses a new tag. The fact base does not
  say whether deleting and re-pushing `v1.0.0` is safe for a book.
- "Watch its Actions tab" is a general GitHub statement that the
  developmental desk required. The fact base does not name the tab.

### ste_check residuals (28)

Same classes as before: "therefore" (6, period-correct); -ing in
headings, terms, and quotes; semicolons only in verbatim quotations and the
index comment; passives "is refused" and "is enforced" in quotations; vague
association in a quotation; paragraph length only on the three art
directives; sentence length only on the index comment.
