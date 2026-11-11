# Desk brief: fact checker

You check Chapter 14, `book/chapters/14-continuous-integration.md`, against its fact file
`docs/briefs/facts/facts-14.md`. The writer had only that file; so do
you. You do not have the press source and you do not guess.

Read the fact file first, all of it, including the "Shared context" section
at its end (the thirty war stories and the list of contradictions, bugs, and
undocumented things). Then read the chapter once straight through, then a
second time claim by claim.

For every sentence that states something checkable (a command, a flag, a
path, a default, a number, a message, a behaviour, a sequence, a name, a
version, a date, who did what), find it in the fact file.

Report, in `docs/briefs/reports/facts-14.md`, three numbered lists:

1. **Unsupported.** Claims you could not find. Quote the sentence, say what
   you searched for. Severity blocks. The fix is always "cut or soften to
   what the file says", with the file's wording quoted.
2. **Contradicted.** Claims the file states differently, or that appear in
   its contradiction list (section 20). Quote both. Severity blocks. Give the
   corrected wording from the file.
3. **Drifted.** Right in substance, wrong in detail: a flag misspelled, a
   message paraphrased where the chapter presents it as verbatim output, a
   default rounded, "always" where the file says "by default", a version
   claim without "at the time of this writing". Severity should.

Also note, as a fourth list, **Missing**: facts in the file that belong to
this chapter's A-heads and are absent, if a reader would need them. Severity
may.

Code blocks that present captured output must match the fact file's capture
character for character apart from the slug change (`demo` to `alice`) and
elision with `...`. Check them.

Return: status, the counts for each list, and the single worst finding.
