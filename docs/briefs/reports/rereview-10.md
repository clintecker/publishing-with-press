# Re-review: Chapter 10, Front matter, the index, and the table of authorities

File: `book/chapters/10-front-matter-index-authorities.md` (424 lines, 5,148 words by `press wordcount`, +14 percent, inside the 15 percent band). Line numbers refer to the revised file.

**Verdict: APPROVED.** 0 open blocks, 2 open shoulds.

## Mechanical checks

- `press check`: exit 0. No finding names this file. The editorial checks and the checker self-test passed.
- `tools/ste_check.py`: 22 findings, all accepted. The four semicolons sit inside verbatim press quotations (223, 296, 380) or the index comment (424). The passive "are stated" (20) is the quoted first law. The `-ing` hits at 192, 342, and 410 are A-heads, B-heads, or Chapter 8's title. The "has fixed" hit (301) is an adjective. The four "therefore" hits fall under the 80 percent rule. The long-sentence hits are the In-this-chapter box (6), the figure lines (123, 125, 263), a footnote marker joining two sentences (162), the index comment (424), and three prose sentences at the 30-word ceiling (81, 301, 308). The paragraph-length hits at 125 and 263 are art comments.
- Fences: all ten are tagged `text`. No line inside a fence is longer than 64 columns.
- Figures: both image lines (123, 261) have one blank line and then their `art:` comment (125, 263).
- Footnotes: all five labels carry the `10-` prefix.
- Sidebar (301): six sentences.
- Example 10.1 matches the scaffold in facts-10 line for line in the lines it keeps, and each cut is marked with `...`. The prose at 39 says what was left out.

## Findings

Fact desk: Unsupported (U), Contradicted (C), and Drifted (D). Missing 1 and 2 were mays. Missing 1 was applied (292). The writer declined Missing 2 for an accepted reason, and Example 10.6 now shows the declared-file `ambiguous` form.

| Desk | No. | Status | Note |
|---|---|---|---|
| Facts | U1 | resolved | Line 190 and Figure 10.1 follow S1. Five generated pages are fed by the two config files. Contents, List of Plates, and List of Figures sit in a gray "from elsewhere" group fed by pandoc's toc and the TeX header, each list only with plates or numbered figures. |
| Facts | U2 | resolved | `BOOK_PUBLISHER` and the environment-variable sentence are gone. |
| Facts | U3 | resolved | Table 10.3 says only "the year". Line 141 points to Chapter 3, which says how the year is found (facts-03 `date` row, Ch 3 line 187). |
| Facts | U4 | resolved | The landing-page sentence is cut. |
| Facts | U5 | resolved | Line 386 names `dist/alice-sources.md`. Line 408 uses the fact file's "download, with the label". The build-timing claim is cut. |
| Facts | U6 | resolved | Sidebar: "eight editions", per the edition-names ruling. |
| Facts | U7 | resolved | Line 209 lists the generated pages (S1 pages 1 to 6). Line 211 is the softened advice. The invented cap duty is gone. |
| Facts | U8 | resolved | Line 382. |
| Facts | U9 | resolved | The typed-model clause is cut. |
| Facts | U10 | resolved | Line 246: "refuses". |
| Facts | U11 | **open (should)** | "Counting from one" is cut from the prose. But the examples still number from 1, and the fact file does not support that. See open item 1. |
| Facts | U12 | resolved | S2 applied. Example 10.2 sets `date`. Line 180: no registrations, no logo. Line 308: "no ledger yet". |
| Facts | U13 | resolved | The roman footnote is softened. "The press calls" is in Table 10.1. The golden-copy line, "therefore passes", and "book's own order" are cut. The Victorian gloss, the devil footnote, the colophon footnote, and the 1865 sample data are accepted. |
| Facts | C1 | resolved | Line 267. `turtle` now carries the boundary rule. `mock turtle` misses because the pattern has a space and the text has a hyphen. |
| Facts | C2 | resolved | Tip (375): "notices when a claim leaves its chapter". Table 10.7 limits `moved` to entries that declare a `file`. |
| Facts | D1 | declined-accepted | The breaks stay, with the disclosures at 255, 286, and 359. The type desk accepted this (type should 2). |
| Facts | D2 | resolved | The tail `(see docs/CONFIGURATION.md)` is restored (250), and the line break is disclosed. |
| Facts | D3 | resolved | Line 145: "a space and 'or,'". |
| Facts | D4 | resolved | Table 10.4: "at 1.7 inches". |
| Facts | D5 | resolved | Line 103: "The four commands on the first line", which matches Example 10.2. |
| Facts | D6 | resolved | Line 265: "every image line". |
| Facts | D7 | resolved | Line 162: "from the book's own files". |
| Dev | C1 | resolved | Line 22: two parts inside the book, one document beside it. |
| Dev | C2 | resolved (equivalent) | Example 10.7 shows the companion's shape, with the fact file's fields in angle brackets. Line 402 describes the Alice result. There is no rendered sample because the fact file does not give one, and the writer was right not to invent it. |
| Dev | P1 | resolved | The tip (116) now covers trimmed or adopted metadata. It agrees with line 107. |
| Dev | P2 | resolved | Example 10.5 has two entries. Example 10.6's entries 1 and 2 are those two. |
| Dev | P3 | resolved | `\maketitle` is cut (121). `titlepage` is glossed. The warning comes after the cap paragraph and names the failure ("a build that never finishes"). The word "third" is still unexplained, but it is the scar's own wording and the fact file gives no more. |
| Dev | P4 | declined-accepted | Line 209 says plainly that the override is LaTeX the author writes and must hold every page they want. The fact file has no skeleton, so declining to invent one is right. |
| Dev | P5 | resolved | Example 10.2 sets `date`. Line 113 says what reads it. |
| Dev | P6 | resolved | Lines 141 and 211 use the design titles. |
| Dev | R1 | resolved | The page looks appear once (188). Table 10.2 cells say what each key holds. |
| Dev | R2 | resolved | `INV-front-matter-golden`, the `%<<if>>` markers, `BOOK_PUBLISHER`, and the print-assets path are cut. The second-rule history is a footnote (`10-rules`). |
| Dev | R3 | resolved | Table 10.2 no longer gives page positions. Line 65 points to Table 10.4. |
| Dev | O1 | resolved | Line 16 puts the index after the last chapter and the ledger in a separate document. |
| Dev | N1 | resolved | Line 275 names Example 10.4. |
| Copy | 1 | resolved | The closer is deleted. The paragraph ends at "therefore has no hits" (265). |
| Copy | 2 | resolved | Line 336: "shows that". |
| Copy | 3 | resolved | Tip at 226. "Fallback" is gone. |
| Copy | 4 | resolved | The phrase is cut as unsupported (U11). |
| Copy | 5 | resolved | Line 209: "stay in the book repository and has no effect". |
| Copy | 6 to 12 | resolved | American spellings: acknowledgments, color, labeled, period, exclamation point. The YAML key `acknowledgements` stays as code. |
| Copy | 13 | resolved | Line 20: "the Print edition, the PDF". |
| Copy | 14 | resolved | "The `press config` command". *target* no longer appears. "Four commands" is correct. |
| Copy | 15 | resolved | *invariant* is cut along with the golden line. |
| Copy | 16 | resolved | *artifact* is italic and defined (386). |
| Copy | 17 | resolved | *verifier* is italic and defined (410). "Proves" is gone. |
| Copy | 18 | resolved | Line 188. |
| Copy | 19 | resolved | Line 184. The history and "provider" are gone. |
| Copy | 20 | resolved | Line 219: second person. |
| Copy | 21 | resolved | The sidebar uses the edition names and has six sentences. |
| Copy | 22 | resolved | The sentence is cut (U9). |
| Copy | 23 | resolved | Line 180 is split. |
| Copy | 24 | resolved | The sentence is cut. |
| Copy | 25 | resolved | Line 372. The tip no longer repeats it. |
| Copy | 26, 27 | resolved | Lines 182 and 288. No perfect tense. |
| Copy | 28 | resolved | Line 275. |
| Copy | 29 to 31 | resolved | The Meaning cells in Tables 10.2, 10.3, 10.4, and 10.6 are sentences. So are the cells in Tables 10.1, 10.5, and 10.7. |
| Copy | 32 | resolved | Line 194: "conditions", "tests them". |
| Type | B1 | resolved | A blank line now sits between line 123 and line 125. |
| Type | B2 | resolved | A blank line now sits between line 261 and line 263. |
| Type | S1 | resolved | Example 10.1 is excerpted, with every line 64 columns or fewer, and the cut is disclosed (39). |
| Type | S2 | resolved | Still true. Example 10.4's message is two fitted lines of the one press line (286). |
| Type | S3 | resolved | The Figure 10.2 directive says "no taller than the house figure cap". |
| Re-review | new | **open (should)** | An `-ing` rider at 292. See open item 2. |

## Open items

**1. Example 10.6 (and the shape errors at 251 to 252) shows details the fact file does not support.** (Facts U11; the writer's residual uncertainty.)

Quote (352, 355 to 356): "entry 1: missing, ..." and "entry 2: ambiguous, "illustrations by John Tenniel" appears 2 times in book/chapters/00-preface.md; lengthen the fragment". At 251: "entry 3: term is missing or empty".

facts-10 gives only `entry N:` and `<file>`. It does not say that N counts from 1 or that `<file>` prints the `file:` value as written. The block is presented as the press's output, not as a shape. I checked the press source, and both details are correct. In `src/press/gen_authorities.py`, line 174 has `enumerate(entries, start=1)` and lines 139 to 140 print `declared`, the raw `file:` value. In `src/press/config_schema.py`, line 444 numbers the index entries from 1 the same way.

Fix: no chapter change. The managing editor appends a supplement S3 to `docs/briefs/facts/facts-10.md` with those two facts and their source lines. If the editor does not want to add the supplement, the writer adds one sentence before Example 10.6: "The entry numbers and the path below show the form of the messages."

**2. An `-ing` rider at 292, which the copy desk did not see.**

Quote (292): "Because `press add appendix` hands out letters counting down from `z-`, the index usually sorts before the appendixes you write."

Rule: `-ing` rider (one-sighting list, as with copy item 4).

Fix: "Because `press add appendix` hands out letters from `z-` downward, the index usually sorts before the appendixes you write."

## Reader's notes (may, not counted)

- The sidebar (301) glosses "the Print edition, the PDF" a second time after line 20. The ruling asks for one gloss per chapter. A sidebar can stand alone, so this can stay. To keep strictly to the ruling, the sidebar could say "only the Print edition has fixed pages".
- Read as a whole, the chapter flows. The two figure directives agree with the prose. Examples 10.5, 10.6, and 10.7 now tell one connected story about the ledger, so the reader can check every fault against an entry they have seen.
