# Fact check: Chapter 12, The print pack

Chapter: `book/chapters/12-the-print-pack.md`. Fact file:
`docs/briefs/facts/facts-12.md` (sections 10.1 to 10.10, 6.7, shared
context, 19, 20). Nothing committed; no other file edited.

Status: **blocks** (2 contradicted, 9 unsupported). Most of the chapter checks
clean: every table of numbers (12.1 to 12.10), Examples 12.1 to 12.4 and
12.6, the spine widths, the wrap sizes, the EAN-13 arithmetic (total 93,
check 7; 11 guard modules plus 84 is 95), the eleven-point checklist (verbatim),
the forbidden-key list, the `press publish` strings, and the commerce refusals
all match the file.

## The writer's four readings

1. **The commerce block is in `config/metadata.yaml`.** Supported, by
   facts-03 section 3.3: the scaffold's metadata template carries "the full
   commented commerce block", and the field table lists
   `commerce.print-ordering.*`.
2. **No house safety value.** Confirmed: the house row reads "0.125" alone,
   and section 20 B.4 says provider `safety` values "are declared but unused".
   The prose handles this correctly. Figure 12.1 does not (Unsupported 5).
3. **No `check_selection` refusal text.** Confirmed. The chapter gives only
   the fact that the checker refuses and where the message comes from, which
   is exactly what section 10.1 says. Supported. (The "few seconds" next to it
   is a separate problem: Unsupported 3.)
4. **`590 x wrap_h px` read as 590 pixels per inch of wrap height.**
   Acceptable. `wrap_h` is in inches (section 10.5 formulas), and the logo
   cap backs the reading: 649 px / 1.1in = 590 PPI. Keep it. The file does
   not say which edge of the cover art the cap measures, but the line 282
   claim that both caps fall under 600 PPI holds either way.

## 1. Unsupported (severity: blocks)

1. Line 180-184, captured output presented as a session:
   "`no assets/cover.jpg; interior verified, wrap not built`". This is not in
   facts-12, which I searched for "wrap not built" and "no assets/cover.jpg;".
   Section 10.9 step 1 supports the behaviour ("if `assets/cover.jpg`
   exists"), but not the text. The line *is* in facts-07 section 7 and in
   facts-08: "Without a cover it prints `no assets/cover.jpg; interior
   verified, wrap not built`", and the chapter matches it character for
   character. Fix: add that line to facts-12, or cut the block back to the
   behaviour: "writes ... `dist/<slug>-coverwrap.pdf` ... if
   `assets/cover.jpg` exists".
2. Line 192: "A fence with a language tag gets syntax highlighting, and the
   highlighting prints in coloured ink. The verifier then fails the whole
   interior with `print profile: colored ink on pages [N]` ... Another source
   is a coloured cover plate in a hand-written *tex/title-page.tex*." None of
   this is in facts-12. I searched for "colored ink", "syntax highlight", and
   "title-page.tex". Facts-04 supports the fence half ("A language-tagged
   fence puts coloured ink on the page ... `print profile: colored ink on
   pages [N]`"). Facts-08 supports the plate half with the full message:
   "`print profile: colored ink on pages [...] (a colored cover plate in a
   hand-authored tex/title-page.tex belongs on the wrap; supply
   tex/title-page-print.tex without it)`". Fix: carry those lines into
   facts-12, or cut the paragraph to the file's "It lifts the print
   verifier's single-ink rule" (section 10.2).
3. Line 51: "You learn that KDP makes no dust jacket in the few seconds the
   checker takes". The file has no timing. Section 20 C says: "Build
   timings. Only the first-run font scan is described." Fix: cut "in the few
   seconds the checker takes" and keep "before any render" (section 10.1).
4. Line 176: "It has mirrored margins, so the wide margin is always at the
   gutter." The file says only "Print interior PDF (mirrored margins, black
   ink)" (section 10.10). The only margin values in the file are in section
   20 B.1 (`inner=0.88in,outer=0.58in`, which "may" override every profile),
   and those are listed as a possible bug, "not verified by a build". Fix:
   "It has mirrored margins."
5. Figure 12.1 art comment, line 115: "A dashed line inside each panel
   labelled 'safety'" on the *house* wrap. The file gives the house provider
   no safety value ("0.125" alone, section 10.4). Section 20 B.4 also says
   provider `safety` values "are declared but unused", so no press wrap
   honours a safety line. Fix: drop the safety line and label from the
   figure, or label it as a provider's declared figure that the press does
   not apply.
6. Line 292 and Figure 12.3 (line 296): "The press verifies the print pack in
   a fixed order", with a chain running `verify_coverwrap` -> "press
   publish" -> "edition manifest" -> "qualification" -> "commerce gate". The
   file gives no such single sequence, and it does not put `press publish`
   upstream of the manifest. Section 10.8 says: "At the end of `press all`
   the gate builds `print` and `coverwrap` and computes the manifest. It then
   requires a passed inspection for this `edition_id`." `press publish` is a
   separate target (section 10.10). Fix: take `press publish` out of the
   gate chain (draw it as a branch off the verified wrap), and soften "a
   fixed order" to the gate's own order as the file states it.
7. Line 236: "A wrap that comes out the wrong size never reaches *dist/*."
   The file says only "then the mediabox is checked within 0.01in" (section
   10.5). Fix: cut the sentence, or say "the press checks the mediabox
   against the computed layout within 0.01in".
8. Line 70: "A typing error in a profile name costs you one run of the
   checker." The file gives the message, "An unknown id fails with `unknown
   print profile '<id>'; available: ...`" (section 10.2), but not which
   command raises it. Fix: "An unknown id fails with ..." with no command
   named. (The "lists the six ids in place of the dots" gloss reads
   `available: ...` fairly.)
9. Line 287, Tip: "The filter that redirects the manuscript's images never
   reads a hand-written TeX file." The file gives the advice ("A custom
   `tex/title-page-print.tex` should point its logo at
   `build/print-assets/`", section 10.7) but not this reason. Fix: keep the
   advice and cut the reason, or soften it to "`print-safe-images.lua`
   points interior images there" (section 10.7).

Note, not counted: line 499, "as it is when CI builds a release tag", is not
in facts-12, but facts-03 section 3.3 supports it ("CI sets it on
`refs/tags/v*`").

## 2. Contradicted (severity: blocks)

1. Line 117: "*docs/PROVIDER-DATA.md* gives the rule in four words: 'Never
   edit it by hand.'" The quoted rule has five words. Fix: "in five words",
   or "gives the rule plainly".
2. Table 12.4, `lulu`, casewrap row (line 225): "because the board margin
   and the hinge add to both the width and the height." This disagrees with
   the file's layout (section 10.5, the chapter's own Example 12.3):
   `inner = hinge + flap + strip` enters only
   `wrap_w = 2 * margin + 2 * inner + 2 * panel_w + spine`, while
   `wrap_h = 2 * margin + trim_h + height_delta`. The hinge widens the wrap
   only. Corrected wording: "because the board margin adds to both the width
   and the height, and the hinge adds to the width."

## 3. Drifted (severity: should)

1. Line 80, presented as a quotation: "the 6x9 house geometry, byte-for-byte,
   ...". The file reads "the 6×9 house geometry" (section 10.2). Restore the
   multiplication sign inside the quote.
2. Line 57: "the six profiles that press 3.0.2 carries". This is a version
   claim without "at the time of this writing". Fix: "the six profiles that
   press carries at the time of this writing" (or keep 3.0.2 with the hedge).
3. Line 178: "Three targets build the interior." Section 10.10 says
   `press publish` "rebuilds and verifies four artifacts", the print interior
   among them, and section 10.8 says the commerce gate "builds `print` and
   `coverwrap`". Fix: drop the count, or name `press publish` as well (the
   gate is already covered at line 186).
4. Line 36: "The provider changes only the arithmetic of the cover." The
   provider also carries the catalog that refuses trims, bindings, and page
   counts: section 10.4's Bindings, Trims, and Page bounds columns, line 51,
   and the chapter's own Table 12.3. Fix: "The provider changes the cover's
   arithmetic and what the shop will make."
5. Line 432 against line 178: step 1 says "because the book has
   *assets/cover.jpg*", but line 178 runs "the Alice example without cover
   art". The fact file allows both cases. The chapter should say which state
   the example is in at each point, for example "once the book has
   *assets/cover.jpg*".
6. Line 240: "0.5in up from the bottom edge". The file says "0.5in up"
   (section 10.5) and does not say whether that is from the trim or the
   bleed edge. Fix: "0.5in up".

Captured-output check: Example 12.5 matches section 10.6's success line
character for character, except for the line breaks, which the text discloses
("broken here across lines to fit the page"). Examples 12.6 and 12.7 are
reformatted YAML (results expanded one per line, the comment moved, `privacy`
folded with `>-`). Both parse to the file's values, and neither is presented
as captured output. The `profile_lifecycle` block leaves out the `usage:`
prefix and wraps one line, but it is presented as a synopsis, not as output.
The verify-print block is Unsupported 1.

## 4. Missing (severity: may)

1. Table 12.5, Resolution row: "No image may exceed 600 PPI, as `pdfimages`
   reports it." Section 10.6 item 5 reads "via `pdfimages`, otherwise a
   note", and section 20 B.14 says doctor does not check `pdfimages` and "its
   absence silently softens two checks to notes". A reader whose wrap
   verifies without `pdfimages` needs to know that the resolution check did
   not run.
2. Section 20 B.3. Example 12.1 makes the Alice book 5 by 8, but the
   `publish` checklist trim and the coverwrap back-text width "read the
   legacy `metadata.trim`, defaulting to 6×9", so "their back-cover text box
   may overrun into the spine". A non-6×9 author would want the hedge, worded
   as a caution, not as a feature.
3. Section 20 B.6: "Page-count bounds are checked only inside cover-wrap
   generation." Table 12.3 lists page bounds per provider, and a reader may
   assume `press check` enforces them on a coverless book.

## Worst finding

Contradicted 2. Table 12.4 says the Lulu hinge adds to the wrap's height, but
the chapter's own Example 12.3 (from the file) puts the hinge in `inner`,
which enters only `wrap_w`. A reader working the arithmetic from the chapter
gets a different answer from the one the table explains.
