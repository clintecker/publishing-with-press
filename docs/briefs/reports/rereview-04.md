# Re-review: Chapter 4, Writing the manuscript

File: `book/chapters/04-writing-the-manuscript.md` (437 lines, working tree).
Against: `facts-04.md`, `dev-04.md`, `copy-04.md`, `type-04.md`, the Revision
section of `report-04.md`, the last twenty lines of `docs/production-ledger.md`,
and supplements S1 to S3 of `docs/briefs/facts/facts-04.md`.

## Verdict

**REVISE.** 1 open blocks, 3 open should (4 open items in all). Every desk
finding but one is resolved or properly declined; the open block is a Code
section fact that the ledger's latest fence ruling now contradicts.

## Specific checks

| Check | Result |
|---|---|
| Every `art:` comment follows its image line | Yes: 46/47, 98/99, 329/330, 348/349. |
| Figure files numbered in order of appearance | Yes: 04-01 page anatomy (46), 04-02 scene-break ornaments (329), 04-03 set pieces (348). |
| Tables section carries S2 | Yes (219, 221): no numbering filter, caption above, centered small italic, no automatic label, caption element in HTML/EPUB, no List of Tables, number typed into the caption, 72-column width rule. |
| Code section carries S2 | Yes (229 to 241): Source Code Pro smaller, wrap with hook, pygments in color, style unchangeable, language tag colors print and `verify-print` message verbatim, untagged/`text` black, reading-PDF verifier does not check ink, inline code exempt, smart typography leaves code alone. But see O1: the later ledger ruling narrows S2's wrap claim. |
| Sentinel cross-reference names Ch 6 and Ch 8 | Yes (202). "proves them in the finished editions" rather than the ruling's "finished PDF"; accepted, since facts-08 checks sentinels in every edition. |
| "every rendered edition" with the Markdown exception | Yes: exception stated once (40); "every rendered edition" at 49, 138, 405, 409; 22 now "every edition it builds" (parse claim, true). |
| `press check` | No finding names this file. Source checks pass (23 files); the editorial failure names only `02-installing-press.md:315, 317`. |
| `ste_check.py` | 44 findings, all in the accepted classes (In-this-chapter list, art and index comments, headings, "Figure 4.1" split, honorific list, "trailing", "therefore", "identical", "look at"). The paragraph-length hit at 96 is the "Figure 4.1" split (six sentences). Exceptions: 161 (O4). |
| Read as a reader | Definitions now precede use (chapter file 18, checker 75, glyph law 103, jargon lint 183, sentinel 202, chapter opening 258, scene break 315, set pieces 344, tie 409). No figure cited by an old number. The added advice paragraphs (161, 171, 179, 196, 225, 250, 291, 413) state no unsupported press fact; "no separate setting for endnotes" (171) is facts 4.1 line 20. |

## Findings table

R = resolved, D = declined-accepted, O = open.

### Fact desk

| No. | Finding | Status |
|---|---|---|
| 1.1 | Footnote label scope | R (179, from S2) |
| 1.2 | Alice example claims | R (S1 supports three chapters, drop cap, fairy-dust, cascade, tail, dialogue opener; 2.1/2.1.1 cut; Example 4.4 is Carroll's text, not a claim about the example's files) |
| 1.3 | "before any build begins" | R (103) |
| 1.4 | `press config set chapter-opening.style` | R (facts-03 lines 199, 418 and facts-B line 29 list the key; 270) |
| 1.5 | Minor glosses | O for the 72-character tip (see O2); rest R (75, 223 now from facts 4.1 line 28, t cut, Lobster replaced) |
| 2.1 | Sentinels to wrong chapter | R (202) |
| 2.2 | "every edition" vs Markdown | R (22, 40, 138, 409) |
| 3.1 | Reference forms read as exhaustive | R ("forms such as", 411) |
| 3.2 | 190 boundary | R (157) |
| 3.3 | Short-heading reason | R (88) |
| 3.4 | "at least two digits" | R (51) |
| 3.5 | Bringhurst's rule source | R (433) |
| 3.6 | Lua test footnote | R (435) |
| 3.7 | No-break space row | R (row removed) |
| 4.1 | Markdown edition set pieces | R (40, single exception per ruling 5) |
| 4.2 | txt/docx drop caps and scene breaks | R (291, 338) |
| 4.3 | `raised-cap` | R (270) |
| 4.4 | Appendix letters, index position | R (65, pointer to Ch 10) |

### Developmental desk

| No. | Finding | Status |
|---|---|---|
| C1 | Figure 4.1 drop cap and callouts | R (44, 46/47: ten callouts, drop cap "A") |
| C2 | Table numbering | R (219) |
| C3 | Language tags, highlighting, inline code | R (231 to 241) |
| P1 | Defaults path | R (22) |
| P2 | YAML metadata block | R (30) |
| P3 | `{.unlisted}` | R (cut) |
| P4 | `lines` knob | R (265 states only the default) |
| P5 | Jargon lint undefined | R (183) |
| P6 | Epigraph attribution | R (185) |
| P7 | "takes them in turn" | R (44) |
| P8 | Glyphs in Example 4.2 | D (ledger ruling: glyphs stay verbatim in code; typesetter saw them render) |
| P9 | Identifier attribute | R (96) |
| R1 | Set pieces outweigh tables/code | R (Table 4.5 cut; Tables and Code grown) |
| R2 | Audit directories | R (153) |
| R3 | Trailing whitespace three times | R (163, 239; tip 166 trimmed) |
| R4 | Recap | R (cut; 417 keeps the one fact) |
| R5 | TeX internals | R (macros cut; the yfonts/yinit name at 307 and the sidebar's `\caption*`/`\mbox` are war-story or font facts, acceptable) |
| R6 | Byte-for-byte line | R (cut) |
| N1 | Figure file order | R (ruling 2) |
| N2 | Figure 4.1 placement | R (head of "Headings and chapters") |

### Copy desk

| No. | Finding | Status |
|---|---|---|
| 1 to 4 (blocks) | lands, lands, ships, ships | R (185, 287, 18, 258) |
| 5 | Tail paragraph over six sentences | R (383/385) |
| 6 | Hidden actor, patterns | R (folded into 153) |
| 7 | Hidden actor, screen readers | R (338) |
| 8 | "command line checks" | R (270) |
| 9, 10, 11 | fail -> refuse | R (157, 115, 202) |
| 12 | "the text" | R (202) |
| 13 | honorific | R (411) |
| 14 | *chapter file* first use | R (18) |
| 15 | set pieces before definition | R (31) |
| 16 | chapter opening before definition | R (69) |
| 17 | *checker* defined | R (75) |
| 18, 20, 21 | "the reader" | R (171, 415, 321) |
| 19 | "Web and EPUB editions" | R by equivalent (307 "The EPUB and the reader site"; facts 4.5 says web and EPUB) |
| 22 to 26 | colour, centred, grey (x2), full stop | R (no British spelling left in the file, art comments included) |
| 27 | Warning imperative | R (54) |
| 28 | Recap | R |

### Type desk

| No. | Finding | Status |
|---|---|---|
| 1 | Figure file order | R |
| 2 | Figure 4.1 portrait | R (`place=plate`) |
| 3 | Table 4.2 split across pages | D (page breaks move as chapters 1 to 3 change; recheck at proof) |
| 4 | Sidebar split | D (same; sidebar now shorter; recheck at proof) |
| 5 | Filename face | R (italic filenames and filters) |
| 6 | Six-line epigraph fence | R (four lines) |

### New in re-review

| No. | Finding | Status |
|---|---|---|
| O1 | Untagged-fence wrap claim contradicted by ledger ruling (blocks) | O |
| O3 | Fence line over 64 columns (should) | O |
| O4 | Prose sentence over 30 words (should) | O |

## Open items

**O1 (blocks). The Code section says untagged fences wrap, and advises leaving
fences untagged.** The ledger's last ruling (supersedes "untagged"): "an
untagged fence is verbatim and runs off the page ... every fence is tagged
`text`" (also `docs/markup.md` lines 108 to 112). The chapter says:

- 229: "A line too long for the measure wraps onto the next line, with a hooked
  mark to show the continuation. Nothing runs off the page"
- 233: "We leave every fence in this book untagged, or tag it `text`."

A reader who follows 233 gets code that runs off the measure. Fix: 229, "In a
fence tagged `text`, a line too long for the measure wraps onto the next line,
with a hooked mark to show the continuation. An untagged fence is set
verbatim, and a long line in it runs off the page." 233, "We tag every fence
in this book `text`, so it prints in black and wraps." Optionally 231: "If you
write `text`, the code prints in black" and keep the black claim for untagged
fences only if it still serves.

**O2 (should; fact 1.5, declining reason no longer holds). The 72-character
tip.** 253: "Keep code lines to 72 characters or fewer. The PDF will wrap a longer
line for you". The writer kept 72 as house advice, but the house ruling caps
fences at 64 columns, and only a tagged fence wraps. Fix: "Keep code lines to
64 characters or fewer. A `text` fence wraps a longer line for you, but at the
measure, which is rarely where a reader expects the break."

**O3 (should; ledger 64-column ruling).** 146 is 65 characters: "The Hatter's
watch told the day of the month, and never the hour." Fix: "The Hatter's watch
told the day of the month, but never the hour." (64).

**O4 (should; copy standard, 30-word ceiling).** 161, added in revision, 32
words: "If the paragraph is a single list of things, such as the options of a
command, it probably wants to be a table, which the section "Tables" later in
this chapter describes." Fix: "If the paragraph is a single list of things,
such as the options of a command, it probably wants to be a table. The
section "Tables" later in this chapter describes tables."

## Notes (not counted)

- 202: "the PDF verifier looks for in the finished book" sits beside "proves
  them in the finished editions". facts-08 checks sentinels in every edition;
  "the verifiers look for" would make the two sentences agree.
- 22: "and you build ... and you switch" is a double-and chain (30 words) left
  by copy item 38. "You build a dialect from a base format and a list of
  extensions. Each extension switches on with a plus sign." reads better.
