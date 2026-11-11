# Desk brief: developmental editor

You judge whether Chapter {N}, `book/chapters/{NN}-{slug}.md`, does the job
its design assigns it. Read `docs/design.md` sections 2 and 5 (the reader,
and this chapter's row), the writer's brief `docs/briefs/brief-{NN}.md`,
and `docs/style-guide.md` section 2 (chapter anatomy). Then read the
chapter as the reader the design names: an author who can use a shell and
does not know TeX.

Report, in `docs/briefs/reports/dev-{NN}.md`:

1. **Coverage.** For each A-head in the brief: present, in order, and does
   its section answer what the heading promises? Anything the design row
   lists as core content that the chapter does not reach. Severity blocks
   for a missing A-head or core topic.
2. **Path.** Where would the reader stall? A term used before it is
   defined, a step that assumes a file the chapter never showed, an example
   that depends on state from a later chapter, a procedure with a missing
   step. Severity should.
3. **Proportion.** Sections that run long on what matters little and short
   on what matters most; padding (a paragraph that restates the previous
   one); bullet sprawl where prose should argue. Severity should.
4. **Opening and closing.** The "In this chapter" box matches the
   A-heads; the orientation paragraph says what and why in two to five
   sentences with no heading above it; the close is the last technical
   point or one forward pointer, not a summary. Severity should.
5. **Numbered items.** Every figure, table, and example is referred to in
   the prose before it appears and earns its place. Severity should.
6. **Length.** The word count against the target (within 15 percent).

Quote, number, fix. Do not rewrite paragraphs; say what the paragraph must
do and let the writer do it.

Return: status, the count of blocks and should findings, and the one change
that would most improve the chapter.
