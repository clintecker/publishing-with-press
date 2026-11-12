# STE80 editor report: Chapter 7, Building the editions

File: `book/chapters/07-building-the-editions.md`

Ratchet count: 13 before (baseline 13), 6 after. `press check` passes.
`python3 tools/ste-ratchet.py` passes (no file rose).

Sentinels: none of the three stands in this chapter. Index terms: every
match string in `config/index-terms.yaml` occurs in the chapter's prose the
same number of times before and after.

## Edits (17 sentences or paragraphs, line numbers in the edited file)

1. Line 59/61, S13 (paragraph of 7 sentences). Split the paragraph at its
   turn of topic, after "It prints each command before it runs it, with a
   plus sign and a space in front." The new paragraph begins "The captures
   in this chapter come from the press's own three-chapter Alice example".
   No words changed.
2. Line 74, S6 and S1. Old: "The input files follow in book order: the
   chapter files, then the appendix files sorted by letter, with any
   generated appendix, such as the subject index, sorted among them. The
   Alice command carries no generated file." New: "The input files follow
   in book order: the chapter files, then the appendix files sorted by
   letter. The press sorts any generated appendix, such as the subject
   index, among them, and the Alice command carries none." (The join keeps
   the paragraph at six sentences.)
3. Line 82, S1 and S2. Old: "The installed package carries one for each
   family of editions in its *data/defaults/* directory, which is
   *src/press/data/defaults/* in the press repository: `pdf.yaml`, ... and
   `print.yaml`." New: "The installed package carries one for each family
   of editions in its *data/defaults/* directory: `pdf.yaml`, ... and
   `print.yaml`. In the press repository, that directory is
   *src/press/data/defaults/*."
4. Line 84, S1 (ratchet lead, 43 words as counted). Old: "The print
   defaults add a sixth filter, `print-safe-images`, in the middle of that
   chain, and the portable defaults keep only three of the five." New: "The
   print defaults add a sixth filter, `print-safe-images`, in the middle of
   that chain. The portable defaults keep only three of the five."
5. Line 167, S8 (-ing forms). Old: "...that pandoc runs over the document
   between reading the Markdown and writing the edition." New: "...that
   pandoc runs over the document after it reads the Markdown and before it
   writes the edition."
6. Line 169, S6. Old: "Table 7.3 describes the filters in chain order,
   followed by the shared helper file." New: "Table 7.3 describes the
   filters in chain order and then the shared helper file."
7. Line 176 (Table 7.3, `chapter-dropcap.lua` cell), S2 (33 words). Old:
   "...the rest of the first word, and the rest of the text, and sets the
   chapter opening in the PDF and the HTML." New: "...the rest of the first
   word, and the rest of the text. It sets the chapter opening in the PDF
   and the HTML."
8. Line 206, S2 (ratchet lead, 32 words; the lowercase "latexmk" hid the
   sentence boundary). Old: "latexmk runs LuaLaTeX with the `-lualatex`
   option, as many times as the document needs." New: "Then latexmk runs
   LuaLaTeX with the `-lualatex` option, as many times as the document
   needs."
9. Line 275, S6 and S1. Old: "The press writes a short header and then the
   raw manuscript, with every chapter and appendix stitched together in book
   order." New: "The press writes a short header and then the raw
   manuscript. It stitches every chapter and appendix together in book
   order."
10. Line 283, S6 and S3 (ratchet lead, passive "is archived"). Old: "A book
    outside any Git repository is archived whole, and one untracked inside
    a parent repository archives nothing." New: "If the book sits outside
    any Git repository, the press archives all of it. If the book sits
    untracked inside a parent repository, the press archives nothing."
11. Line 291, S2 (ratchet lead, 31 words). Old: "Every artifact that the
    press can build has one entry in *the registry*, the one statement of
    the artifact graph, which lives in *src/press/registry.py* in the press
    repository." New: "Every artifact that the press can build has one
    entry in *the registry*, the one statement of the artifact graph. The
    registry lives in *src/press/registry.py* in the press repository."
12. Line 312, S1. Old: "The Pages bundle, *dist/pages/*, becomes the Pages
    site, the Web site that GitHub Pages serves and that holds the
    downloads, so it is never a download itself." New: "The Pages bundle,
    *dist/pages/*, becomes the Pages site, the Web site that GitHub Pages
    serves. The Pages site holds the downloads, so the bundle is never a
    download itself."
13. Line 335, S8. Old: "...a verifier that reads *dist/* without
    rebuilding it can bless..." New: "...a verifier that reads *dist/* but
    does not rebuild it can bless..."
14. Line 349, S8 (ratchet lead, "calling"). Old: "Before every pandoc
    build, the press generates them again by calling the same function,
    which does three things in order:" New: "Before every pandoc build, the
    press calls the same function to generate them again. That function
    does three things in order:"
15. Line 357, S6 and S1. Old: "It is a standalone document of the claims in
    the book and the sources that warrant them, published beside the book."
    New: "It is a standalone document of the claims in the book and the
    sources that warrant them. The press publishes it beside the book."
16. Line 361, S1 and S2 (ratchet lead, 44 words as counted). Old:
    "@fig:press-all-sequence draws the sequence as a state machine, and
    Example 7.4 shows one real run on the three-chapter example on
    `hatter`, with long lines cut short." New: "@fig:press-all-sequence
    draws the sequence as a state machine. Example 7.4 shows one real run
    on the three-chapter example on `hatter`, with long lines cut short."
17. Line 482, S10 (phrasal verb). Old: "Use them to look over the book a
    page at a time, at a fixed resolution." New: "Use them to examine the
    book a page at a time, at a fixed resolution."

## Leads declined

- Lines 15 and 476, ing-form "counting" in "Rendering, counting, and
  cleaning": a heading and its entry in the In this chapter box. Headings
  are never touched.
- Line 208 to 214 (sidebar "The lists that would not converge"), 8 sentences in
  one paragraph: Light mode. No sentence is over 30 words, none carries
  three ideas, and none has a semicolon. The sidebar is about 140 words,
  under the 190-word limit.
- Line 240, 38 words: a counter artifact. The footnote marker `[^7-rsc]`
  after the period hides the boundary, so the checker joins two sentences
  of about 19 words each. Moving the marker would detach it from the claim
  it annotates.
- Line 355, 32 words: a counter artifact. The quotation ends with its period
  inside the double quotes, so the checker sees no boundary before "An
  index file". The quotation is verbatim, and each real sentence is under
  20 words.
- Line 497, 34 words: a counter artifact, the same footnote-marker case as
  line 240 (`[^7-wordcount]`).

## Also considered and kept

- Short sequences of three or four verbs that share one subject and
  describe one process (Table 7.1 cells for `press all`, `press coverwrap`;
  "`press print` uses `print.yaml`, sets the page two-sided, and adds the
  print-safe filter to the chain"; "The registry builds all nine
  prerequisites, assembles the bundle, and runs the page verifier"; step 4
  of the `press all` walk). Each is under 23 words and reads as one action
  sequence, so I left them.
- Line 478, "throws *build/* and *dist/* away": kept the phrasal verb for
  voice, and the triad there names three targets, so it has three parts.

## Passives kept

None added. Participial adjectives ("sorted by letter", "the flattened
white-ground copy", "long lines cut short") remain where the actor is the
press already named in the sentence or does not matter. No finite passive
remains in the edited sentences.
