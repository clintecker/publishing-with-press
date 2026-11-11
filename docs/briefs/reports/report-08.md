# Report: Chapter 8, Verifying the artifacts

File: `book/chapters/08-verifying-the-artifacts.md`

## Word count

`press wordcount`: 6765 (target 6,000; within 15 percent, upper bound 6,900).
The count includes tables, examples, captions, and the art directives.

## Shape

- Nine A-heads in the brief's order; B-heads under the PDF, formats,
  archives, and witnesses sections.
- Plate lines moved to after the orientation paragraph, unchanged.
- Tables 8.1 to 8.7, Examples 8.1 to 8.4, Figures 8.1 to 8.3, each
  referenced before it appears.
- Sidebar: war story 5, "Links that overshoot" (151 words), set in the
  PDF verifier section beside the list-link check. Uses the code version
  (`caption`'s `hypcap=true`), per contradiction A.4.
- Four tips, three warnings. Four footnotes (renderer fallback scar,
  `CI=false`, fixed archive timestamp, window overlap).

## Figures

- **8.1 `what-each-verifier-inspects`** (matrix): 13 check rows by 5
  verifier columns with filled dots; the dot map is in the directive.
  Mapping choices: sentinels in verify_pdf, verify_formats, verify_pages,
  and print; link resolution in verify_pdf, verify_pages (references),
  and print; "witnesses" means the manuscript/chapter witness, so
  verify_formats only. Sentinels row shaded so the reader sees it first.
- **8.2 `rebuild-edges`** (data-flow, left to right): the five verify
  commands, arrows to exactly the artifacts the fact file's
  which-command-rebuilds-what list names, verifiers in italic under each
  command, a dashed conditional arrow for the cover wrap.
- **8.3 `verify-run`** (terminal): no captured verify run exists in the
  fact file, so the panel shows `$ press verify`, `...`, and
  `missing text sentinel in PDF: Twinkle, twinkle, little bat` (the
  verbatim message with the Alice sentinel from Chapter 3 in `<s>`).

## Facts I needed and left out

- No captured `press verify` or `press verify-formats` session, so the
  success lines appear only in their template form (Examples 8.1, 8.2)
  with placeholders, never with invented numbers.
- Whether `verify_pdf` stops at the first failed check or reports all is
  not stated; the chapter says only that it runs checks in a fixed order.
- How a chapter witness is chosen is not stated; the chapter says each
  chapter has one and stops there.
- Which line is the Alice manuscript witness is unknown; not given.
- The coverwrap checks are summarized in two sentences and deferred to
  Chapter 12, as the fact file defers them to its section 10.6.

## Contradictions and hazards handled

- A.4 hypcap: followed the code.
- A.5 the image cap: "per profile, 6.3in on the house 6 by 9".
- A.9 min-pages: model default 40, template 1, release 24.
- B.11 (`verify-formats` reads a possibly stale PDF): described as a
  limit with a tip to run `press all`, not as a feature.
- B.12 (verify-print builds print twice): not mentioned.
- B.14 (doctor does not check pdfimages): not asserted; the chapter says
  only that the cover check softens to a note without `pdfimages`, and
  advises installing all of poppler.
- Chapter 1 quotes the sentinel failure as `sentinel ... not found`; that
  wording is not in this fact file. This chapter uses the verbatim
  `missing text sentinel in PDF: <s>`. The editor may want Chapter 1
  aligned.

## Checker results

- `press check`: fails only on other writers' files (Chapter 2 plate
  references and two editorial findings in Chapter 2). Nothing names
  this file. `press style` reports nothing for Chapter 8.
- Jargon lint (house allow list, quotes included): no findings.
- `ste_check.py` residuals, all defended:
  - Passives at lines 24 and 26 (ste numbering) and 427: verbatim
    quotations of the third law, CONTRIBUTING, and ARCHITECTURE.
  - Semicolons: the plate directive (untouchable), and verbatim quotes of
    the CLAUDE.md scar and the `INV-graph-no-stale` limitation, and the
    index comment.
  - Paragraph-length and sentence-length on the three `art:` directives
    and the index comment (directives are illustrator briefs, each under
    150 words).
  - Sentence-length of 29 to 30 on a handful of prose sentences, all at or
    under the 30 ceiling; the 32-word hit is the In-this-chapter list.
  - "therefore", "verify", "-ing" forms in headings and gerunds: allowed
    by the prose contract's 80 percent rule.
- One code line exceeds 72 columns: the verbatim `press doctor` line for
  epubcheck in Example 8.4 (75 columns). Wrapping it would alter captured
  output, so I kept it.

## Revision

Word count after revision: 6662 (`press wordcount`; target 6,000, band
5,100 to 6,900). `press check` and `press style` name nothing in this
file. The remaining `press check` failures are in Chapters 2 and 12.

### Rulings applied

1. Examples 8.1 and 8.2 now show the real S1 and S2 runs with the slug
   changed to `alice`, timing elided, long lines broken (and the prose
   says so). Both are attributed to "the press's own three-chapter Alice
   example", which renders 23 pages. A sentence after Example 8.1 says
   that example's floor is 1 and a release build would refuse it, and
   that the manual's sample `alice` (the full novel) sets 24 once its
   twelve chapters exist. The archives success line is quoted in the
   archives section, and `archived 12 files` illustrates the excluded
   directories. The chapter witness is defined from S3 at first use (the
   reader-site check), and the manuscript witness now lists S3's
   character set. S3's long-code-line hazard is a new Warning.
2. The "first words" rule is gone. "Reading a failure" now starts from
   the command that ran (Figure 8.2), the `press all` order, and Table
   8.1 where a message names the artifact.
3. The no-stale paragraph names the `verify-formats` exception, and
   Figure 8.2's directive adds a dotted "reads, does not rebuild" arrow.
   The `press all` Tip lists the four verifiers and sends the reader to
   `press verify-print` for the print interior and wrap. The doctor
   paragraph says `press doctor` does not check `pdfimages`. Body and Tip
   both say that two checks soften to notes without it.
4. Copy blocks fixed ("lands", "ships", "every surface"). "guarantees"
   became an invariant definition, "lesson" became scar, "measure" went
   with the cut sentence, "the source" became "the press's source".
   American spelling throughout, art directive included. Numbers under
   ten spelled out. The Warning split into three sentences.
5. Page floor defined in Table 8.2. TeX vocabulary: `\mainmatter` replaced
   by a book-terms explanation. The sidebar glosses *float* and calls
   hyperref the link package and caption "the package that sets
   captions". "Authoring sandbox" cut from the body ("unless a helper
   renderer is present"). Commerce defined in one sentence with a pointer
   to Chapter 12. Detector self-test is one paragraph plus the messages,
   with the thresholds in a footnote. Figure 8.1: the prose now names
   five verifier runs (the print profile as the fifth), matching the
   columns, and points `verify_coverwrap` to Chapter 12. Alt text says
   "five verifier runs".
6. All three `art:` comments come after their image lines with one blank
   line between (`space-art-comments.py` had nothing left to insert).
   Every fence is tagged `text`. No code line exceeds 64 columns. The
   doctor epubcheck row is elided with `...`, and the caption text says
   so. The added `$ press doctor` prompt is gone.

### Other desk findings resolved

- Fact desk: 11.5 percent story reduced to the source's facts; tools
  sentence no longer says printers use poppler; `PRESS_RELEASE` described
  as marking a release build, not who sets it; the `PRESS_TOOLCHAIN`
  sentence follows the fact file; "sentinel list starts empty" cut;
  reader zip sentence no longer mentions the Pages deploy; "always"
  dropped from the machine-fault list and the pdfinfo parse message
  hedged; the blank-page Warning no longer claims a blank page is the
  first sign of the hang; Tip at the sentinel paragraph now points at
  `press verify-formats` and "counts" the chapters, not names them;
  verifier success line generalized; "List of plates" label quoted; "on
  every verify run"; "whatever last built it"; "a likely cause"; break
  notices added to every broken message; `BROKEN` optional tool sentence
  added; E explained (six named editions plus the PDF through
  `pdftotext`); `press all` summary pointed to Example 1.2 in Chapter 1
  (the `press all` line has non-ASCII glyphs, so I did not quote it).
  Low-stakes glosses: dropped "something overrode the house geometry",
  "every page is an image", the 20-percent reason, the proofreader
  sentence, "where the registry says", the file-naming advice in Table
  8.7. Kept "pandoc curls the quotes" (Chapter 3 says the same) and
  Table 8.5's readings of the four failure names, which only restate the
  names.
- The sample book's sentinels ("Twinkle, twinkle, little bat", "she made
  some tarts") now belong explicitly to the full novel, as Chapter 3 set
  them, not to the three-chapter example. The quoted title in capitals
  is gone.
- Dev R2: the sentinels-in-four-places paragraph cut to its inference
  and a cross-reference. R3: signpost folded into a clause. R4: pages
  checks regrouped by condition (always, `site-url`, commerce). P6: the
  profile split is stated once. N3: Chapter 2 cross-reference added.
- Example 8.3 (two missing-epubcheck messages) is now an unnumbered
  fragment holding only the toolchain message, because Example 8.2
  carries the captured local warning. The doctor report became Example
  8.3.
- To stay in the band I cut repetition: the edges paragraph that restated
  Figure 8.2, the "early/middle/late" summary, the timestamp footnote, the
  24-word window illustration (the footnote keeps the arithmetic), and
  two rows of Table 8.7.

### Mays declined

- Copy 35 (the plate caption's -ing): the plate lines are fixed by the
  brief. That one belongs to the art desk.
- All other copy mays (23 to 34) were accepted.

### Residual ste_check findings

As before: passives and semicolons inside verbatim quotations (third
law, CONTRIBUTING, ARCHITECTURE, the CLAUDE.md scar, the invariant
limit), the plate directive, the three `art:` directives and the index
comment. The one remaining "had" was removed. No prose sentence exceeds
30 words outside the In-this-chapter list.

## Revision 2

Word count: 6742 (`press wordcount`). `press check` passes with
nothing naming this file.

1. Footnote labels prefixed with `tools/prefix-footnotes.py`:
   `8-detector`, `8-fallback`, `8-ci-false`, `8-window`.
2. Chapter witnesses: "stitches four files, its three chapters and an
   appendix, so it has four chapter witnesses."
3. "Reading a failure" no longer points at Figure 8.2 for verifiers. It
   names in prose the verifiers each target runs (`press verify`,
   `press verify-formats`, `press pages`, `press verify-print`). The
   Figure 8.2 directive is unchanged.
4. One name: "the Alice example" is the full novel throughout, and "the
   press's own three-chapter Alice example" is the gallery excerpt. The
   opener now says that the real runs in Examples 8.1 and 8.2 come from
   the three-chapter example. Lines 106 and 206 use "the Alice example".
5. Edition names: glossed once in the "Artifacts as objects" verifier
   paragraph: Print (the reading PDF), Circulating (EPUB), Single-leaf
   (the self-contained HTML), Manuscript (the stitched Markdown),
   Telegraphic (plain text), Office (DOCX), Chapter (the reader site and
   its zip), Source edition (the source zip). After that the names
   replace the format names in Table 8.1, the `verify-formats` build
   list, the formats verifier opening, and Table 8.3's Edition column.
   File-level references (the EPUB package, the HTML file, *dist/alice.pdf*,
   the PDF's text) keep the format name, because they speak of the file
   and not the edition. The A-head "Archives and the source edition"
   keeps the brief's wording.
6. Also fixed: the seven-editions sentence had said `pdftotext` was
   present "on `hatter`", but the S2 capture comes from the
   three-chapter example, not from `alice`'s workstation. It now says
   "on the machine that ran the example". The paragraph in "Reading a
   failure" split to stay at six sentences or fewer.

## Revision 3

Continuity pass applied: the full novel is "the Alice book" throughout
(opener, Table 8.1 and its caption, the profile and sentinel sentences,
the page-floor sentence), and the captures stay "the press's own
three-chapter Alice example". *dist/pages* is "the Pages bundle", and
"the Pages site" now means only what the deploy serves (Table 8.1, the
pages section, the `press all` Tip and paragraph, Figure 8.2's alt
text). Mays applied: line 82 quotes Example 3.3's refusal
(`this is a release build (PRESS_RELEASE=1) and its witnesses are
vacuous:`) and drops my own use of the phrase. Example 8.3 opens with
`$ press doctor`. The pages verifier's third group is now *print
ordering*, and "commerce gate" stays as the gate's own name. Table 8.3
gives the ISBN as `urn:isbn:` and the number, as Chapters 7 and 13 do.
`press check` passes with nothing naming this file.
