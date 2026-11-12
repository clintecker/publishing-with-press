# STE80 editor report: Chapter 8, Verifying the artifacts

File: `book/chapters/08-verifying-the-artifacts.md`

## Ratchet count

- Before: 8 (baseline in `tools/ste-baseline.json`, and the first
  `--report` run). Re-run against the original text with the current
  `tools/ste-ratchet.py`, the count is 7: the wrapper now unwraps
  sidebars, so the sidebar "Links that overshoot" (old line 129) no
  longer reads as one 8-sentence paragraph.
- After: 0.
- `press check`: passed (exit 0).

## Edits (new line numbers)

1. L17, S1/S2 (26 words). Old: "The examples come from the Alice book, the full novel that user `alice` builds on the workstation `hatter` and that CI builds on the host `printshop`." New: "The examples come from the Alice book, user `alice`'s full novel. She builds it on the workstation `hatter`, and CI builds it on the host `printshop`."
2. L25-27, S13 (ratchet lead: 7 sentences). Split the paragraph after "This chapter follows five verifier runs." The definition stays in the first paragraph, the list of runs opens the second. No sentence changed.
3. L65 (Table 8.2, Sentinel count cell), S6. Old: "The page floor is the fewest pages the PDF may have, set by `verify-min-pages`." New: "The page floor is the fewest pages the PDF may have, and `verify-min-pages` sets it."
4. L69 (Table 8.2, pdfinfo cell), S1 (four ideas). Old: "The tool must run, its output must parse, the trim must match, and the page count must reach the floor." New: "The tool must run, and its output must parse. The trim must match, and the page count must reach the floor."
5. L74 (Table 8.2, Ink cell), S1 (three ideas). Old: "Every rendered page must carry ink, no ink may touch the page edge, and every page must have the same size." New: "Every rendered page must carry ink, and no ink may touch the page edge. Every page must have the same size."
6. L84-86, S1/S2/S13. Split the paragraph at the turn from the release check to the trim and file checks (it would otherwise reach 7 sentences). Old: "The Alice book uses the house 6 by 9 profile, so the verifier expects a page 6 inches wide and 9 inches tall, within 1.0pt in each direction." New: "The Alice book uses the house 6 by 9 profile. The verifier therefore expects a page 6 inches wide and 9 inches tall, within 1.0pt in each direction."
7. L132, S1 (three clauses). Old: "The second means that the links point at pages, but the pages hold no image, so the reader arrives on the wrong page." New: "The second means that the links point at pages that hold no image. The reader then arrives on the wrong page."
8. L139 (sidebar, Light mode: three ideas). Old: "A later version of the house design dropped that package and set `hypcap=true` in the package that sets captions, which does the same job from one place." New: "A later version of the house design dropped that package. It set `hypcap=true` in the package that sets captions, which does the same job from one place."
9. L144, S3 (condition first) and S2 (27 words). Old: "The verifier renders every page to a PNG image with `pdftoppm -png -r 120`, at 120 dots per inch, unless a helper renderer is present.[^8-fallback]" New: "Unless a helper renderer is present, the verifier renders every page to a PNG image at 120 dots per inch with `pdftoppm -png -r 120`.[^8-fallback]"
10. L146, S10 (phrasal verb). Old: "the verifier looks at the ink on each page." New: "the verifier examines the ink on each page."
11. L154, S10. Old: "The edge check looks at a border two pixels wide around each page." New: "The edge check examines a border two pixels wide around each page."
12. L173, S1/S2 (28 words). Old: "A page fails when more than 200 of its pixels have an RGB channel spread of 48 or more, which means that a reader sees color in them." New: "A page fails when more than 200 of its pixels have an RGB channel spread of 48 or more. A spread that wide means that a reader sees color in those pixels."
13. L185, S10. Old: "The verifier looks at page 1 twice." New: "The verifier examines page 1 twice."
14. L192, S1 (two unlinked facts). Old: "The press's own notes record that a missing `pdfimages` softens two checks to notes in this way, and `press doctor` does not check for the tool." New: "The press's own notes record that a missing `pdfimages` softens two checks to notes in this way. The `press doctor` command does not check for the tool."
15. L210, S1 (three ideas). Old: "That example sets its page floor at 1, which suits a gallery excerpt, and a release build would refuse it." New: "That example sets its page floor at 1, which suits a gallery excerpt. A release build would refuse it."
16. L247 (Table 8.3, Circulating cell), S1/S2/S3 (30 words, condition last). Old: "The package must have a valid mimetype, a `container.xml`, a non-empty `dc:date`, and the registered ISBN, in the form `urn:isbn:` and the number, when the book has one." New: "The package must have a valid mimetype, a `container.xml`, and a non-empty `dc:date`. When the book has a registered ISBN, the package must also carry it in the form `urn:isbn:` and the number."
17. L266, S1 (three ideas). Old: "The DOCX check joins text across runs because Word splits a paragraph into runs wherever the formatting changes, so a sentinel can span two runs." New: "The DOCX check joins text across runs because a sentinel can span two of them. Word splits a paragraph into runs wherever the formatting changes."
18. L276, S2 (30 words). Old: "A *chapter witness* follows the same rule as the manuscript witness, applied to one chapter file: it is the longest markup-free line of 40 or more characters in that file." New: "A *chapter witness* is the longest markup-free line of 40 or more characters in one chapter file, by the same rule as the manuscript witness." (Kept as one sentence so the paragraph stays at six.)
19. L298, S1/S2 (29 words). Old: "The message prints the manuscript witness in lower case and cuts it at 40 characters, so it is a pointer to the line and not a quotation of it." New: "The message prints the manuscript witness in lower case and cuts it at 40 characters. The text is therefore a pointer to the line and not a quotation of it."
20. L298, S1/S2 (29 words). Old: "The seven editions are the six that the `Verified` line names plus the Print edition, which takes part because `pdftotext` was present on the machine that ran the example." New: "The seven editions are the six that the `Verified` line names plus the Print edition. The Print edition takes part because `pdftotext` was present on the machine that ran the example."
21. L321, S8 and S10 (ratchet leads: "looking", "look at", "keying"). Old: "The press decides which case applies by looking at `PRESS_TOOLCHAIN`. It does not look at `CI`. The press's source gives the reason: keying on `CI` would fail" New: "The press reads `PRESS_TOOLCHAIN` to decide which case applies. It does not read `CI`. The press's source gives the reason: a test of `CI` would fail" (the quotation that follows is untouched).
22. L341, S6 (ratchet lead: "is archived"). Old: "A book outside any Git repository is archived whole, and one untracked inside a parent repository archives nothing." New: "For a book outside any Git repository, the press archives the whole book. For a book untracked inside a parent repository, it archives nothing."
23. L420, S1/S2 (27 words). Old: "The check catches a chapter that one edition dropped and the others kept, which no single sentinel would find unless it happened to sit in that chapter." New: "The check catches a chapter that one edition dropped and the others kept. No single sentinel would find that loss unless the sentinel happened to sit in that chapter."
24. L487, S10 (ratchet lead: "find out"). Old: "and your job is to find out why." New: "and your job is to find the cause."
25. L493-495, S13 (ratchet lead: 8 sentences) and S2 (30 words). Split the paragraph after the second cause. Old: "The second is a phrase at the start of a chapter, where the chapter opening splits the first word and small-caps the rest, as Chapter 4, *Writing the manuscript*, explains. The third is an edition that lost the chapter, so run `press verify-formats` too, because its agreement check counts the chapters that each edition lacks." New: "The second is a phrase at the start of a chapter. The chapter opening splits the first word and small-caps the rest, as Chapter 4, *Writing the manuscript*, explains." / new paragraph: "The third is an edition that lost the chapter. Run `press verify-formats` too, because its agreement check counts the chapters that each edition lacks."
26. L513 (footnote 8-ci-false), S1 (26 words). Old: "In most shells and most CI systems, an environment variable holds a string, and a check for its presence treats the string `false` as present." New: "In most shells and most CI systems, an environment variable holds a string. A check for its presence treats the string `false` as present." ("In most" kept.)

## Leads declined

- Old L129, sidebar "Links that overshoot", paragraph-length 8. Light
  mode: voice is the point of a sidebar, and the current ratchet no
  longer flags it (it unwraps the sidebar into its two paragraphs).
  Its 30-word sentence ("A plate's caption sits under the image...")
  is at the ceiling, not over it, so it stays.
- Sentences the counter in my own pass put at 24 to 28 words because a
  quotation counts as one word or a list is the sentence's one idea
  (L21, L23, L33, L363 list of prerequisites, L431, L451). Each holds
  one idea, so I left them.
- Remaining "looks for" (L106, L376, L384, L416) and "Look first at" /
  "look at what" in Table 8.7: "examine" would read as a form letter
  there, and the ratchet does not flag them.

## Passives kept

- L337 (old 335): "the book's own source, published so that anyone can
  rebuild it". The publisher (the deploy, the Pages site) does not
  matter to the sentence.
- No other passive in body prose was flagged or found.

## Fidelity checks

- Sentinel "You do not choose the witness" still present once; the other
  two sentinels never occurred in this file.
- Every `config/index-terms.yaml` match string occurs at least as often
  as before ("Print edition" and "sentinel" each gained one).
- No new semicolons outside code spans, no dashes, ASCII only, no fence,
  heading, image line, art comment, or footnote label touched.
