# STE80 review: Chapter 3, The shape of a book repository

File: `book/chapters/03-the-shape-of-a-book.md`, against
`git diff HEAD`. All 34 edits read hunk by hunk.

Status: REVISE. Blocks 0, should 2.

Checks run: `press check` passes (self-test, editorial, jargon).
`python3 tools/ste-ratchet.py` exits 0. No paragraph in prose exceeds
190 words. The diff holds no sentinel, and every code span, path, flag,
key, and message is unchanged. The quotation from the template
("pick 2-4 phrases ... not a common word)") still matches
`press/src/press/data/template/config/metadata.yaml` character for
character. Moving the period outside the closing quotation mark is
correct because the quotation ends at "word)".

## Findings

1. Edit 14, L134 (should: the edit changed what a pronoun refers to,
   which misstates a fact).
   Old: "After `site-url`, the real file goes on with the verification
   knobs, which the section "Verification knobs" later in this chapter
   shows, and with commented lines for print and registrations. It ends
   with a commented block for direct print ordering, the last part of
   Example 3.2."
   New: "After `site-url`, the real file goes on with the verification
   knobs and with commented lines for print and registrations. The
   section "Verification knobs" later in this chapter shows the knobs.
   It ends with a commented block for direct print ordering, the last
   part of Example 3.2."
   What went wrong: the new sentence puts "The section" between "the
   real file" and "It". "It ends with a commented block" now reads as the
   section ending with that block. The block ends the file, and it is
   the last part of Example 3.2.
   Corrected: "The file ends with a commented block for direct print
   ordering, the last part of Example 3.2."

2. Edit 5, L68 (should: the rule is now weaker).
   Old: "A slug must match the pattern `[a-z0-9][a-z0-9-]*`: lowercase
   letters, digits, and hyphens, starting with a letter or a digit."
   New: "A slug must match the pattern `[a-z0-9][a-z0-9-]*`. It holds
   lowercase letters, digits, and hyphens, and it starts with a letter or
   a digit."
   What went wrong: the colon gloss sat under "must" and listed the only
   characters allowed. In a sentence of its own, "It holds" can mean only
   that these characters may occur, and "it starts" describes instead of
   requiring. The pattern still gives the full rule, but the plain-English
   gloss lost "only" and "must".
   Corrected: "A slug must match the pattern `[a-z0-9][a-z0-9-]*`. It can
   hold only lowercase letters, digits, and hyphens, and it must start
   with a letter or a digit."

## Flagged edits judged sound

- Edit 30, the `.gitignore` sentences moved up in "What Git gives the
  press". Accepted. The zip holds only the files Git tracks, and
  `.gitignore` keeps *build/* and *dist/* untracked, so the "therefore"
  now follows the facts it depends on. No fact moved to a case where it
  is false: the outside-a-repository case in the next paragraph still
  says "less *build/*, *dist/*, and caches", which matches facts-03
  (excluded dirs `.git`, `__pycache__`, `build`, `dist`). Edit 29's
  active rewrite keeps both cases exactly, including "archives nothing
  until Git tracks its files". Each paragraph has one topic: what the
  zip holds, and the zip before `git init`.
- Edit 15, Table 3.3 `date` cell: "beginning 1 or 2" to "that begins
  with 1 or 2". Same fact.
- Edit 16, Table 3.3 `rights` cell. "instead" keeps the EPUB exception.
  The cell still says pandoc receives the value everywhere else, and
  that the EPUB carries the press's own `--metadata rights=` value.
- Edits 17 and 18, the epubdate paragraph. "extracts ... from" matches
  the footnote's own verb, and "pulls ... out of" meant the same thing.
  Splitting off "The same date gives the title page its roman numerals"
  keeps both outputs and the "never type the year twice" consequence.
  The footnote marker did not move.
- Edit 20, "including" to "among them". Same scope: one line for every
  known config file, and the absent optional files are among them.
  "including" was a preposition, not an -ing rider, so the change was
  not needed. It is harmless, and I left it.

Every other edit (1-4, 6-13, 19, 21-28, 31-34) only splits a sentence
or swaps a verb. Each keeps its facts, qualifiers, and identifiers. No
Light-mode passage (sidebar, anecdote, epigraph) was touched. Every
term follows `docs/vocabulary.md`.
