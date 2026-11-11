# Typesetter report: Chapter 6, Checking the manuscript

Status: findings. 3 blocks, 27 should.

press check: FAILED on another file (not this chapter). Message:
"book/chapters/02-installing-press.md:315: assistant vocabulary" and
":317: staging: run-up". The editorial pass stops there, so the jargon pass
never ran and this chapter was not proven by it; the source checks and the
self-test passed. No diagnostic names this file.

press pdf: PASSED (exit 0) once 19 missing figure PNGs (1362x800 white) were
created as placeholders; they are deleted again. Chapter occupies PDF pages
94-112 (printed 87-103ish). No heading at a page foot, no table wider than
the measure, no blockquote box over a page, no hooked code line (all fences
are untagged, so none can wrap).

## Blocks (3)

1. Quote: line 38, `<!-- art: ARCHETYPE pipeline, left to right. ...` sits
   BEFORE the image line 39 (`![The checker guards every build target]...`).
   Rule: the `art:` comment goes on the line immediately after the image; a
   comment before the image belongs to nothing. Fix: swap the two lines.
2. Same fault, line 97 art comment above image line 98
   (`![A known-bad fixture's round trip ...`). Fix: swap.
3. Same fault, line 454 art comment above image line 455
   (`![A passing press check on hatter]...`). Fix: swap. (Also leave no blank
   line between image and comment.)

## Should (27)

Untagged fences (16). Rule: every fence is tagged `text`; run
`tools/tag-fences.py`. Opening fences at lines 82, 104, 187, 225, 245, 271, 285, 308, 332,
361, 394, 421, 437, 463, 502, 510 (all 16 fences in the file).
Fix: tag each ```text.

Code lines over 64 columns (8; none over 80). Rule: at most 64.
- 105: 66, `<fixture>: expected rule '<rule>' did not fire (<up to 3 others or`
- 107: 67, `<fixture>: no checker rejected a known-bad fixture (and it declares`
- 291: 66, `  responsibilities meet here?,Literal material use; precise domain`
- 292: 66, `  term; deliberate metaphor,user seed,Name the interface or shared`
- 362: 66, `config/house-rules.yaml: banned pattern '<p>' is not a valid regex`
- 444: 66, `Checker self-test passed: 19 known-bad fixtures each tripped their`
- 445: 67, `    declared rule, known-good fixture accepted, 2 extra diagnostics`
- 470: 65, `  - book/chapters/01-down-the-rabbit-hole.md: paragraph 9 has 212`
Fix: rewrap at 64 with a continuation indent (the fences are already
folded and labelled as folded in the prose; just move the break earlier).
Note 444-445 and 470 must stay consistent with the type-12 figure text
(fig 6.3 brief wraps at 72, that is fine as an image).

Example caption separated from its fence (3 occurrences in PDF). Rule: an
example caption must not be stranded from its fence.
- Example 6.6 (line 283): caption at the page foot, fence on the next page.
- Example 6.14 (line 500): caption last on the page, `$ press check && git
  commit ...` first on the next.
- Example 6.9 (line 359): caption plus one line on one page, remainder on
  the next (fence split; acceptable only if a short fence is kept together).
Fix: these depend on final pagination; after the line and fence fixes,
rebuild and recheck. If still stranded, shorten the preceding paragraph or
move the sentence referring to the example.

Non-issues checked and clean: In this chapter box matches the nine A-heads;
tip/warning/sidebar forms (2 tips or warnings plus 1 sidebar, sidebar 165
words as one paragraph); examples numbered 6.1 to 6.15 in sequence with
bold caption directly above the fence; tables 6.1 to 6.7 with header row,
proportioned separator, `Table: Table 6.N.` caption after; figures: path
form, `#fig:`, `.diagram`, `full-measure`, fig-alt differs from caption,
captions sentence case no period, `@fig:` reference precedes each image,
art paragraph plus image 177/177/164 words (under 190); no figure is a
wrap; terminal panel brief fits 72 columns; no figure brief is a matrix or
tree over 14 rows; headings sentence case, no digit, no two in a row, none
typed numbers; footnote labels unique (first-expect, generated, law-date,
twocopies); index comment last, 24 flat terms; no trailing whitespace, no
non-ASCII, no dashes.
