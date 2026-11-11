# Re-review: Chapter 1, Introduction

Scope: `book/chapters/01-introduction.md` after Revision 1, checked against
every blocks and should finding in `facts-01.md`, `dev-01.md`, `copy-01.md`,
and `type-01.md`. Also checked against the writer's Revision section in
`report-01.md`, the last thirty lines of `docs/production-ledger.md`, and
facts-01 S1 to S5. Line numbers refer to the chapter as it stands (310 lines).

Runs:

- `press check`: exit 1. No error names this file. The failing term is
  `rewrite: 'authoritative'` in `05-figures-and-plates.md:75`, which is not
  this chapter's. The only diagnostic for 01 is `inspect: 'spine'` at 274:170,
  where "computed spine" is literal (the cover wrap). Accepted.
- `ste_check.py`: 52 findings, 338 sentences, average 13.4 words. The
  residuals are the art directives, verbatim quotations (the laws, the
  third-law passives, *CONTRIBUTING.md*), heading gerunds, the index
  comment, and period-correct "whether" and "therefore". The three
  `paragraph-length` flags at 43, 48, and 227 (8, 8, and 14 sentences) are
  not prose. They are the checker reading each image line and its `art:`
  comment as one paragraph, which confirms open item B1 below.

The fact file does not grade its findings. I treated every Unsupported,
Contradicted, Drifted, and Missing item as a should, and graded
Contradicted 1 and 2 (captured output that is not the capture) as blocks.

## Open items

### Blocks

**B1. No blank line between an image and its `art:` comment (four places).**
The ledger's correction requires one blank line between the image line and
its comment: "an image followed on the next line by a comment is a Para,
not a Figure". The writer's report says the comments "now follow their image
lines". They do, but on the very next line every time:

- line 3 to 4 (frontispiece, `{place=frontispiece}`)
- line 43 to 44 (`#fig:pipeline-overview`)
- line 48 to 49 (`#fig:the-stack`)
- line 227 to 228 (`#fig:ten-minute-tour`)

None of the four becomes a Figure, so none gets a number, a caption, or a
List of Figures entry. The frontispiece is included: `figure-numbering.lua`
does its `place=frontispiece` placement on the Figure element, so as a Para
it loses its verso placement as well. The brief said to leave the
frontispiece lines alone. That instruction predates the spacing rule, and
adding a blank line changes neither line.

Fix: `python3 tools/space-art-comments.py book/chapters/01-introduction.md`
(it inserts four blank lines).

### Shoulds

**S1. Every fence is untagged (six fences).** Lines 129, 145, 159, 175,
211, and 234 open with a bare fence. The ruling says every fence is tagged
`text`, because an untagged fence is plain verbatim with no breaklines and
runs off the measure. Fix: `python3 tools/tag-fences.py
book/chapters/01-introduction.md`.

**S2. Two code lines over 64 columns.**

- Line 134 (65 columns):
  `  press config set description "A girl falls down a rabbit hole."`
  Fix: shorten the value, for example
  `  press config set description "A girl falls into Wonderland."`
- Line 235 (65 columns):
  `$ git remote add origin https://github.com/wonderland-press/alice`
  Fix: break it with a continuation:
  `$ git remote add origin \` and on the next line
  `    https://github.com/wonderland-press/alice`

  Line 132 is exactly 64 columns, which is within the limit.

**S3. "the Web editions" (line 198, Table 1.1, row `typeset`).**
`docs/vocabulary.md` lists "the web edition" among the names not to use, and
the chapter elsewhere uses the press's own names. Quote: "The PDF, the EPUB,
the Web editions, the text, and the DOCX all built." Fix: "The PDF, the
EPUB, the Single-leaf and Chapter editions, the text, and the DOCX all
built." (The capture's own line says `web`, so the code block stays as it
is.)

**S4. TeX and pandoc appear unglossed at first mention (dev P1).** Line 19:
"You never write a line of TeX or type a pandoc command to get them." This
is the first mention of each name. The gloss for pandoc comes 18 lines later
(line 37). TeX never gets its own gloss: line 39 calls LuaLaTeX "the TeX
engine", which assumes that the reader knows TeX. The design's reader "does
not know TeX or pandoc". Fix (line 19): "You never write a line of TeX, the
typesetting language behind the print PDF, or a build command to get
them." Line 37 then stays the first mention of pandoc, with its gloss in
place.

## Finding table

### Fact desk (facts-01.md)

| Desk | No. | Status | Note |
|---|---|---|---|
| facts | U1 slug | resolved | S5: `press new alice` writes `slug: "alice"`. Lines 73 and 139 say so. |
| facts | U2 checker rules | resolved | S4 4.1 has the curly quotes and the under-190 law. Line 35 is accurate. |
| facts | U3 Python, poppler | resolved | S5 gives Python 3.10 through 3.14 and poppler (`pdftoppm`). Line 46 is consistent. |
| facts | U4 image name, watchlist | resolved | S4 12.4 gives the image name. Line 153 glosses the watchlist. |
| facts | U5 sentinels | resolved | S4 3.3: "in the source and in every artifact". Line 278. |
| facts | U6 drop cap as house | resolved | Line 281: opt-in, "The house default is no drop cap at all" (S5). |
| facts | U7 11.5 percent sidebar | resolved | Sidebar line 94 has "a dropped cover and a clipped cover". Line 98 has "now checks the cover on page 1". |
| facts | U8 "tell you so" | resolved | Cut (line 117). |
| facts | U9 every example from 3.0.2 | resolved | Cut. |
| facts | U10 CI install, tag convention | resolved | Paragraph cut. Line 286 words the tags without the convention. |
| facts | U11 "sealed" | resolved | Gone (line 31). |
| facts | U12 minor glosses | declined-accepted | `target` is the book's vocabulary. S3 shows pandoc writing each format. The ROADMAP sentence is cut. |
| facts | C1 Example 1.2 `ls` | resolved | Example 1.3 (lines 211 to 223) matches S1 entry for entry, with the slug substituted. |
| facts | C2 Figure 1.3 panel 3 | resolved | Line 228 gives eleven lines exactly. |
| facts | D1 README quote ending | resolved | Line 29 ends with an elision. |
| facts | D2 "only in the tags" | resolved | Moot (cut). |
| facts | D3 "inside the image" | resolved | Line 105: "In a container". |
| facts | D4 trust ladder | resolved | Moot (cut). |
| facts | D5 `press pages` | resolved | Line 225. |
| facts | D6 typography of a valid book | resolved | Line 286. |
| facts | D7 who pins the image | resolved | Line 286: "the press's reusable workflow". |
| facts | D8 public date | resolved | Line 63: "The ROADMAP records". |
| facts | D9 vacuous footnote | resolved | Moot (cut). |
| facts | D10 dependency edges | resolved | Line 89 quotes the notes. |
| facts | D11 42-word stub | resolved | Line 139: "a one-paragraph preface". |
| facts | M1 how `press all` ends | resolved | Example 1.2 lines 186 to 188 match S3 verbatim, with the slug substituted. |
| facts | M2 full sequence | resolved | Line 167. |
| facts | M3 print pack not built | resolved | Line 274. |
| facts | M4 `verify-min-pages` default | resolved | Line 278. |

### Developmental desk (dev-01.md)

| Desk | No. | Status | Note |
|---|---|---|---|
| dev | P1 tool glosses | partly open (S4) | pandoc (37), Lua filter (37), LuaLaTeX (39), latexmk (39), poppler (46), and epubcheck (41) are all glossed. TeX, and pandoc's first mention at line 19, are not. |
| dev | P2 line 45 split | resolved | Lines 51 and 53. The pin sentence is dropped. |
| dev | P3 scar defined late | resolved | Defined at line 57, before line 81. |
| dev | P4 Table 1.1 | resolved (equivalent) | The table now explains the lines that Example 1.2 shows. Line 153 names the two elided check lines. |
| dev | P5 verification shown | resolved | Example 1.2 shows `verify` and `your book is ready`. Line 205 quotes the PDF verifier and ties it to the sidebar. |
| dev | P6 workflow file, retry reason | resolved | Line 232 (*book.yml*). Line 247: "The image is public, so no permission is missing" (S4 12.4). |
| dev | P7 `site/` | resolved | Lines 262 and 270. |
| dev | P8 forward references | resolved | Line 139 has "source archive". Line 157 has "a comment". |
| dev | P9 `press pages` | resolved | Line 225. |
| dev | R1 laws internals | resolved | The invariant, the trust tiers, and the grep warning are cut. |
| dev | R2 history trivia | resolved | Lines 57 to 63. |
| dev | R3 versions section | resolved | One paragraph plus the tip (lines 286 to 290). |
| dev | O1 payoff | resolved | Line 19 gives directory in, every edition out, no TeX, every file opened and checked. The Alice note moved to the tour. |
| dev | O2 opening of "What press is" | resolved | The README's first sentence leads. The lowercase name is in a footnote. The profiles are one pointer to Chapter 9. |
| dev | O3 warning under B-head | resolved | Prose comes first (line 167). |
| dev | N1 Figure 1.3 placement | resolved | Line 225 refers to it again at the point where it appears. |

### Copy desk (copy-01.md)

| Desk | No. | Status | Note |
|---|---|---|---|
| copy | 1 "ships" (blocks) | resolved | Line 105: "carries". Line 81 keeps "ship" inside the verbatim scar quote, which is correct. |
| copy | 2, 3 edition, manuscript first use | resolved | Line 19. |
| copy | 4 the house before definition | resolved | Line 31 rewritten. |
| copy | 5 house rules | resolved | Line 35. |
| copy | 6 Manuscript edition | resolved | Line 37. |
| copy | 7 artifact | resolved | Line 41. |
| copy | 8 homemade | resolved | Line 41. |
| copy | 9 split paragraph | resolved | Lines 51 and 53. |
| copy | 10 | resolved | Moot (cut). |
| copy | 11 design profiles | resolved | Line 59. |
| copy | 12, 13 two ideas | resolved | Line 63. |
| copy | 14 | resolved | Moot (cut). |
| copy | 15 italic filenames | resolved | Lines 71, 75, 89, 94, 111, 115. |
| copy | 16 | resolved | Line 73. |
| copy | 17 scar | resolved | Line 57. |
| copy | 18, 19 | resolved | Moot (cut). |
| copy | 20 refuse to fails | resolved | Line 98. |
| copy | 21 | resolved | Line 103. |
| copy | 22 | resolved | Moot (cut). |
| copy | 23 e-books | resolved | Line 109. |
| copy | 24 color | resolved | Line 111. |
| copy | 25 filenames, editions | resolved | Line 117. |
| copy | 26, 27 known-bad fixture | resolved | Line 155. |
| copy | 28 | resolved | Line 157. |
| copy | 29 warning imperative | resolved | Line 170. |
| copy | 30 plates | resolved | Line 250. (Note: "fourteen engraved plates" at line 61 comes earlier and is roman. It is ordinary English and was in the first draft unflagged, so it is not counted.) |
| copy | 31 "raw source" | resolved | Line 263. |
| copy | 32 | resolved | Line 272. |
| copy | 33 cover wrap | resolved | Line 274. |
| copy | 34 to 38 | resolved | Moot (cut or reworded, line 286). |
| copy | 39 condition first | resolved | Line 289. |
| copy | 40 hidden actor | resolved | Line 294. |
| copy | 41, 42 desk, workflows | resolved | Line 296. |
| copy | 43 two conventions | resolved | Line 300. |

### Type desk (type-01.md)

| Desk | No. | Status | Note |
|---|---|---|---|
| type | 1 filmstrip archetype | resolved / declined-accepted | The panels are now stacked vertically. Panel 3 runs to eleven lines against the eight to nine asked for. The decline holds, because the fact desk required the real `ls`. |
| type | 2 chapter cross-references | resolved | Lines 239 and 272. |
| type | 3 appendix titles | resolved | Line 298. |
| type | 4 table separators | resolved | Lines 194 and 258. Table 1.1's first column now holds short tokens. |
| type | 5 color | resolved | Line 111. |
| type | index note | resolved | "dist directory" is at line 41. "build directory" is at line 276. |

### Rules added after the first draft

| Rule | Status | Note |
|---|---|---|
| `art:` after image, one blank line | **open (blocks)** | B1. All four are adjacent. |
| fences tagged `text` | open (should) | S1. Six bare fences. |
| code lines at most 64 columns | open (should) | S2. Lines 134 and 235. |
| edition names per *vocabulary.md*, glossed once | resolved except S3 | Table 1.2 glosses all eight with their formats. Line 198 has "Web editions". |
| drop cap not the house default | resolved | Line 281. |
| `press all` builds pages | resolved | Lines 167, 197, and 225. |
| payoff on the first two pages | resolved | Lines 19 to 41. |
| each tool named in a clause at first mention | partly open | S4. |

## Read as a newcomer

The chapter now reads cleanly for someone who has never heard of press. The
first paragraph gives the payoff. By line 41 the reader knows the input, the
outputs, the toolchain, and why verification matters. The tour runs
scaffold, check, build, and publish without a gap.

Two small things are not counted as findings, and the writer may take them
or leave them:

- Example 1.2 and Table 1.1 say "7 editions" right before Table 1.2 lists
  eight. The Source edition is the one left out of the agreement check. A
  clause in the `verify` row would head off the question: "Seven editions
  agree with the manuscript. The source archive is checked as an archive."
- Line 33 says "package docstring", a Python term this reader may not know.
  "the package's own description" would do.

## Verdict

**REVISE.** There are five open items: one blocks (B1) and four shoulds
(S1 to S4). B1 alone sends the chapter back. All four figures, the
frontispiece included, currently build as plain paragraphs.

B1, S1, and S2 are mechanical: two tool runs and two line edits. S3 and S4
are one-sentence edits. No re-run of the desks is needed. A rerun of
`space-art-comments.py`, `tag-fences.py`, and the column check closes it.
