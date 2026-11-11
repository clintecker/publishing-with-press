# Desk brief: continuity editor

You keep the book one book. You hold `docs/continuity.md`, the continuity
bible, and you are the only desk that writes to it.

For Chapter 2, `book/chapters/02-installing-press.md`, after the other desks have
passed it:

1. Read the bible, then the chapter.
2. **Terms.** Every term the chapter defines (italic at first use) goes in
   the bible's term table with the chapter number, unless it is already
   there, in which case the chapter must not redefine it differently.
   Every use of a word that `docs/vocabulary.md` forbids for a thing is a
   finding. A thing called by two names in this chapter is a finding.
3. **Cast.** The sample book is `alice`, user `alice`, host `hatter`, CI
   host `printshop`, owner `wonderland-press`. Any other sample name is a
   finding unless it is the press's own example or a real tool.
4. **Cross-references out.** Every "see Chapter N, *Title*", "Appendix X",
   "the section ... in Chapter N", "later in this chapter", "@fig:" goes in
   the bible's reference ledger with what it promises the target contains.
   Check the chapter number and title against `docs/design.md` section 5
   and the target file if it exists. "Later in this chapter" must be later.
5. **Promises.** Any sentence of the form "Chapter N explains", "described
   in", "covered later", "as you saw in Chapter N" is a promise; record it.
   Check promises earlier chapters made about this chapter and raise any
   this chapter fails to keep.
6. **Numbering.** Figures, tables, and examples run 1, 2, 3 within the
   chapter with no gap and no repeat; each file slug matches
   `CC-NN-slug`; every `@fig:` has its figure.
7. **Facts shared across chapters.** Any number, default, path, or message
   this chapter states that another chapter also states must agree. The
   bible's shared-facts table holds them; add new ones, check old ones.
8. **The Preface.** When you reach it last, its Organization section must
   match every chapter's final title and A-heads in substance.

Report findings in `docs/briefs/reports/continuity-02.md` (quote, rule,
severity, fix) and update `docs/continuity.md` in place. Severity: blocks
for a wrong cross-reference or a contradicted shared fact; should for a
second name for one thing; may for the rest.

Return: status, the number of bible entries added, and any conflict with
an earlier chapter.
