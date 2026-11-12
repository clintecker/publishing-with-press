# STE80 review: Appendix D, The toolchain

File: `book/appendices/d-the-toolchain.md`, reviewed against
`git diff HEAD` and the editor's report `docs/briefs/reports/ste-d.md`.

Status: **APPROVED**. Blocks 0, should 0.

The diff holds the nine edits the report lists (edits 3 and 4 share one
hunk, as do 5 and 6, and 7 and 8), and nothing else. No fence, code span,
quotation, message, heading, or footnote label changed. The footnote
`[^d-colima]` still sits on the Colima sentence. The sentinels are not in
this file. `press check` exits 0, and `tools/ste-ratchet.py` reports the
file at 1 (the heading "What is untested"), down from 4.

## Findings

None.

## The hard cases, checked

1. **Line 32, `pdfimages`, condition first.** Old: "`pdfimages` comes
   with poppler, and its absence silently softens two checks to notes, so
   install poppler in full." New: "`pdfimages` comes with poppler. If
   `pdfimages` is absent, two checks silently soften to notes, so install
   poppler in full." facts-D (line 85, discrepancy 14): "its absence
   silently softens two checks to notes". "silently", "two", and "notes"
   are kept; "softens" became the intransitive "soften" with no actor
   invented; the advice stays bound to its reason with "so". No finding.
2. **Line 32, the Chrome sentences joined with "but".** Old: "...drives a
   headless Chrome for its layout check. No book needs Chrome." New:
   "...drives a headless Chrome for its layout check, but no book needs
   Chrome." facts-D line 88: Chrome is used only by the press's own docs
   site and "is not needed for books". The contrast "but" states is the
   one the two facts already make; nothing is strengthened. The join keeps
   the paragraph at six sentences after edit 3 added one. No finding.
3. **Line 63, "First," and "Second," added.** Old: "The press repairs
   this in two parts: the image's wrapper (Example D.4) replaces the
   launcher, and the verifier reports a present-but-unrunnable epubcheck
   as a fault in the toolchain, not in your EPUB." New: "The press repairs
   this in two parts. First, the image's wrapper (Example D.4) replaces
   the launcher. Second, the verifier reports ... not in your EPUB."
   facts-D scar 3 names both parts (the `java -jar` wrapper; the
   toolchain-fault report). The enumerators count the "two parts" the
   topic sentence promises; they do not assert an order of operations the
   source lacks, since the two parts are independent and the text claims
   no sequence. "present-but-unrunnable" and Example D.4 are verbatim.
   Observation, not a finding: "Second," lands two short paragraphs after
   "The second is epubcheck", a different count. The topic sentence "in
   two parts" resets the count, so a reader does not cross them.

## The other six, checked

- Line 3: "then ..., then ..." became a second sentence with "It then
  describes"; all three contents kept. "walks through" to "covers" keeps
  the claim (same ground) without narrowing or widening it.
- Line 30: "if" to "whether" matches facts-D line 81.
- Line 61: "it dies" became "The launcher therefore dies", which names the
  antecedent the source means (CLAUDE.md: Ubuntu's epubcheck launcher dies
  at execution) and keeps the causal "so" as "therefore". The quoted
  message "Exec format error" is verbatim.
- Line 167: "The `--rm` flag" adds the word "flag" to a code span that is
  a flag; no fact added. `--break-system-packages` matches facts-D line 97.
- Line 169: the condition "For a build that matches CI" now heads only the
  first sentence, but "as well" ties the second to it. `:latest`,
  `image:`, *build.yml*, and the chapter references are intact.
- Line 173: "the script can mount a book only under `$HOME`" keeps "only"
  and the Colima/macOS condition, now placed first.

Voice: no Light-mode passage in this appendix. Each edited paragraph keeps
a mix of short and long sentences. No term in `docs/vocabulary.md`
changed.
