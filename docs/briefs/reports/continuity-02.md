# Continuity report: Chapter 2, *Installing press*

Desk: continuity editor. Chapter read: `book/chapters/02-installing-press.md`
(current working tree). Cross-checked against the drafts of Chapters 1, 3,
and 4, `docs/vocabulary.md`, `docs/design.md` section 5, briefs 11, 14, 15,
and facts 14 and 15. The chapter was not edited.

Status: **one blocking finding** (a contradicted shared fact with Chapter 3),
one should, six mays. Every promise earlier chapters make about Chapter 2 is
kept. The bible (`docs/continuity.md`) now holds 54 new entries: 13 terms,
19 shared facts, 21 cross-references and promises, 1 numbering row.

## Findings

### 1. The composite action is defined as what a book's CI calls (blocks)

- Quote (l.134): "The *composite action*, the piece of the press that a
  book's CI calls, installs press from the action's own checkout"
- Quote (l.291): "the *reusable workflow*, the workflow file a book's CI
  calls"
- Against Chapter 3 (l.560): "The reusable workflow pins the composite
  action and the toolchain image, so the book never names either one."
- Rule: shared facts must agree (brief item 7); one gist per term.
- Problem: the scaffolded *book.yml* calls the reusable workflow, which
  runs the composite action. Chapter 2 gives both pieces the same gist, and
  the composite action's gist contradicts Chapter 3.
- Fix (l.134): "The *composite action*, the piece of the press that the
  reusable workflow runs to install it, installs press from the action's
  own checkout, never with pip from Git."

### 2. "The project" as a second name for the press (should)

- Quotes: l.25 "The project tests 3.10 through 3.14."; l.33 "what the
  project's own tests run", "the project's continuous integration (CI)";
  l.333 "The project's own CI also runs Python 3.12 on macOS 15"; l.343
  "the project makes no claim", "the project does not test them".
- Rule: one name per thing (vocabulary, "the press" for the institution).
  The same chapter says "the press's own full verification script" and
  "the press proves on every release" for the same body.
- Fix: "the press" in each place ("The press tests 3.10 through 3.14.",
  "the press's continuous integration (CI)", "the press makes no claim").

### 3. "could not execute" (may)

- Quote (l.224): "the command was present but could not execute."
- Rule: vocabulary, *run* (never execute).
- Fix: "the command was present but could not run."

### 4. "the pinned toolchain container" (may)

- Quote (l.325): "It runs press inside the pinned toolchain container
  against a book."
- Rule: vocabulary, *the toolchain image* (not "the container" except in a
  sentence about Docker).
- Fix: "It runs press against a book inside the pinned toolchain image."

### 5. The operator's commands called targets (may)

- Quote (l.165): "the *operator*, the targets such as `press improve` that
  hand work to an agent."
- Rule: l.138 (and Chapter 1) defines a target as a command that builds,
  checks, or verifies; `press improve` does none of the three.
- Fix: "the *operator*, the commands such as `press improve` that hand work
  to an agent."

### 6. Libertine and Libertinus across Chapters 1 and 2 (may; raise in Chapter 1)

- Quote, Chapter 1 (l.46): "pandoc, LuaLaTeX, latexmk, the Libertine
  fonts, epubcheck ..."
- Quote, Chapter 2 (l.186): "TeX Live includes Libertinus, the typeface of
  the house PDF."
- Rule: shared fact (house PDF typeface). Chapter 2 is right (facts-01,
  facts-B: `'' keeps Libertinus`).
- Fix (Chapter 1, at its own pass): "the fonts (Libertinus for the PDF,
  with the Libertine keyboard face)". No change to Chapter 2.

### 7. The toolchain image used before its definition (may)

- Quote: "toolchain image" appears roman at l.19, 77, 192, 212, 216; it is
  italic and defined at l.266.
- Rule: vocabulary, first use italic and defined in the same sentence.
- Fix: none needed if the copy desk accepts l.19's "which this chapter
  describes later" as the forward pointer; otherwise move the italic and
  gist to l.19.

### 8. Figure order differs from design.md and brief-02 (may)

- The chapter numbers 2.1 tools-in-the-build, 2.2 doctor-report, 2.3
  local-versus-container (dev ruling 4, reading order). `docs/design.md`
  section 5 and brief-02 still list the doctor report as 2.1. Numbering
  inside the chapter is clean: no gap, no repeat, slugs match, every
  `@fig:` has its figure. The PNGs for 2.1 and 2.2 do not exist yet.
- Fix: update design.md section 5, row 2, so the List of Figures and
  Preface checks do not misfire later.

## Promises

Incoming (all kept): Chapter 1 l.51 (both install routes), l.302 (the
toolchain on `hatter`); Chapter 3 l.449 (installation in full, the
editable install), l.465 (the toolchain for a full build).

Outgoing and open, for the target chapters' writers:

- **Chapter 14 must show where the toolchain image digest is found**
  (l.315: "Chapter 14 shows where to find the digest."). The reader needs
  the `image:` line of the press's *build.yml* at the pinned three-part
  tag, the `@sha256:` value to substitute for `:latest` in Example 2.6, and
  the matching press tag. Per facts-14 item 341, the digest is not in the
  release notes; it lives in the build.yml pin and the release receipt.
  Chapter 14 must also deliver l.134 (the composite action in detail).
- Chapter 15 must show the desk's doctor panel (l.262). facts-15 supports
  it; brief-15 does not mention it.
- Chapter 15 must describe the operator commands (l.165); Chapter 11 the
  API keys and `press art commission` (l.248).

Cast: clean. Only `alice`, `hatter`, `printshop`, `~/alice`, and the
press's own Alice example appear.
