# Continuity report: Chapter 14, Continuous integration and the release contract

Text read: `book/chapters/14-continuous-integration.md`, 439 lines. Status: PASS
with fixes (0 blocks, 3 shoulds, 3 mays). No cross-reference is wrong, no
shared fact is contradicted, and no earlier chapter's promise about Chapter 14
goes unkept.

## Findings

1. **Quote:** "The Pages site is the Web site that GitHub Pages serves from the book's Pages bundle" (l.384).
   **Rule:** vocabulary row "the Pages site": never "the Web site". Ch. 7 l.316 has the same gloss.
   **Severity:** should. **Fix:** "The *Pages site* is what GitHub Pages serves from the book's Pages bundle, *dist/pages/*." Apply the same change at Ch. 7 l.316 in the sweep.

2. **Quote:** Preface l.64 to 65: "Describes a book's CI, the reusable workflow, the toolchain image pinned by digest, tags, and the release contract."
   **Rule:** brief item 8; the Organization blurb must match the chapter's A-heads in substance. It omits the composite action, receipts, release builds, Pages, and moving between majors.
   **Severity:** should. **Fix:** "Follows a book's CI through the reusable workflow, the composite action, and the toolchain image pinned by digest; explains tags, receipts, and the release contract that proves each press tag; and covers release builds, the Pages site, and moving between majors." (Verb-first, per design.md.)

3. **Quote:** Ch. 16 l.270: "downloads the `receipt-quality` and `receipt-integration` artifacts ... uploads the result as `release-receipt`."
   **Rule:** Ch. 14 l.54 rules that *artifact* is a file the press names in *dist/*; GitHub's kind is an *upload bundle*. Ch. 14 says "upload bundles" for the same three things (l.272 to 290).
   **Severity:** should (second name for one thing across chapters). **Fix:** in Ch. 16 write "upload bundles" at l.270, and gloss it by pointing to Chapter 14.

4. **Quote:** Ch. 14 l.122 "the Python inside the image belongs to Ubuntu 24.04, as Chapter 2 explains"; Ch. 2 l.313 "because Debian manages the image's Python".
   **Rule:** shared facts, "Python in the image". Ch. 1 and Appendix D say the image is Ubuntu 24.04.
   **Severity:** may (Ubuntu is a Debian derivative; the wording differs, the fact does not). **Fix:** Ch. 2 l.313 to say "Ubuntu manages the image's Python".

5. **Quote:** "the release contract proves that pin" (l.74, roman, first use); "The *release contract*, the workflow that proves a press tag" (l.217, italic). Likewise "reusable workflow" (l.18) and "composite action" (l.34, l.62) appear before their italic gloss (l.40, l.78).
   **Rule:** vocabulary header: first use in a chapter is italic and defined in the same sentence.
   **Severity:** may. **Fix:** gloss *release contract* at l.74 ("the *release contract*, the workflow that proves each press tag") and make l.217 roman; for the other two, either accept the intro's forward use (the opening paragraph is orientation, and the headings gloss them) or add one clause at l.18 and l.34.

6. **Quote:** `docs/design.md` section 5, row 14: "14.2 the release state machine ...; 14.3 how a book resolves `@v3`".
   **Rule:** brief item 6 (figures run in appearance order). The chapter now shows the resolution as 14.2 and the state machine as 14.3, and its files follow.
   **Severity:** may. **Fix:** swap 14.2 and 14.3 in design.md (as was done for Chapters 4 and 12).

## Checks that passed

- **Figures.** Images in order: `14-01-ci-topology` (l.34, `@fig:ci-topology`), `14-02-resolving-v3` (l.236, `@fig:resolving-v3`), `14-03-release-state-machine` (l.311, `@fig:release-state-machine`). Each is cited before it appears, each file exists in `assets/woodcuts/`, each caption and fig-alt matches its picture, and the prose before each (l.30, l.232, l.308) says what the figure shows. A blank line precedes each `art:` comment. The stale `dist/site/assets/woodcuts/` copies (14-02 state machine, 14-03 resolution) are untracked build output and will regenerate; they are not a manuscript fault.
- **Numbering.** Tables 14.1 to 14.4 and Examples 14.1 to 14.4 run with no gap and no repeat; footnotes carry the `14-` prefix (`14-pillow`, `14-main`, `14-macos`, `14-migrate`), unique book-wide.
- **Cast.** Only `alice`, `hatter`, `printshop`, `wonderland-press/alice`, `~/alice`, and real tools appear.
- **A-heads.** The "In this chapter" list matches the ten H2s exactly.
- **Terms.** Nothing defined differently from the bible: floating tag, immutable tag, release witnesses (Ch. 6), vacuous witnesses (quoted as press's phrase), artifact/upload bundle, Pages bundle versus Pages site, the reusable workflow, the composite action all agree. No use of "pipeline", "repo", "execute", "invoke", or "folder" in the author's voice (the one "pipeline" is inside a quotation of the maintainer's guide).
- **Cross-references out** (all in the bible's reference ledger now): Chapter 3 and Example 3.12; Chapter 2 and Example 2.6; Example 6.11 and Chapter 6; Chapter 7 (commerce gate); Chapter 3 (config set, Pages bundle, Pages setting); Chapter 8 (Pages verifier). Titles match design.md section 5. Every "later in this chapter" and "the next section" is later.
- **Promises earlier chapters made about Chapter 14**, all kept: Ch. 1 l.244 and l.294; Ch. 2 l.134 and l.315 (digest in build.yml and the receipt, not the notes); Ch. 3 l.599; Ch. 6 l.475; Ch. 7 l.316 and l.440; Ch. 9 l.377; Ch. 16 l.80 and l.110; Appendix A l.779 and l.862; Appendix D l.175; Appendix E l.261. The bible's "Open (stub)" rows are now marked Kept.
- **Shared facts agreeing:** version 3.0.2 with "at the time of this writing"; the four permissions and triggers (Ch. 3 Example 3.12); two sentinels and a floor of 24 (Ch. 3, 6, 16); the refusal message (Example 3.3 and 6.11); twelve receipt layers and three tiers (Ch. 16, word for word); macOS 15 and Python 3.12 (Ch. 2, 16); `quality`, `consumer`, `desk` check names (Ch. 16 Table 16.5); `press migrate` subcommands and files (Appendix A, Ch. 3 l.639); the Pages bundle contents (Ch. 3 l.621).
- **Ch. 3 versus Ch. 14 on the refusal example:** Ch. 3 cites its own Example 3.3 and Ch. 14 cites Example 6.11; both exist and the texts agree. No conflict.

## Bible changes

Eight terms, eleven shared facts, sixteen reference-ledger rows, and one numbering row added (36 entries), plus 13 existing rows updated (5 shared-fact rows "due 14" confirmed, 8 reference rows marked Kept).

Conflicts with earlier chapters: none that block. Ch. 2 l.313 (Debian wording, finding 4), Ch. 7 l.316 ("the Web site", finding 1), and Ch. 16 l.270 ("artifacts", finding 3) need small edits.
