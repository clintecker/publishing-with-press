# Desk brief: STE80 reviewer

You review the STE80 editor's changes to `book/chapters/13-registrations.md` for fidelity and for
voice. The editor was allowed to change how sentences are built and
nothing else. Your job is to prove that is all that changed.

Read `docs/skills/ste80-humanizer/SKILL.md` "Fidelity rules" and
`docs/prose-contract.md` first. Then take the diff:

    git diff HEAD -- book/chapters/13-registrations.md

Read every hunk. For each changed passage, compare old and new and
answer:

1. **Facts.** Is any fact added, lost, weakened, or strengthened? A dropped
   qualifier ("by default", "at the time of this writing", "unless"), a
   rounded number, a "may" that became "does", a condition that moved
   after its command. Severity blocks. Check against
   `docs/briefs/facts/facts-13.md` where the fact file covers it.
2. **Verbatim material.** Any code span, command, path, flag, key,
   message, quotation, identifier, sentinel, or index term altered.
   Severity blocks. The sentinels are "You do not choose the witness",
   "On a fresh scaffold it succeeds", "the selftest skips the checks".
3. **Voice.** A passage in Light mode (Preface, sidebar, anecdote,
   epigraph) rewritten beyond the three permitted fixes. A run of same-
   length sentences where the old paragraph varied. An understatement
   flattened. Severity should.
4. **Terms.** A term changed against `docs/vocabulary.md`. Severity should.
5. **Markup.** Anything `press check` would refuse, a paragraph that grew
   past 190 words, a blockquote split in two. Severity blocks.

Write `docs/briefs/reports/ste-review-13.md`: one numbered list, each
item the old text, the new text, what went wrong, the severity, and the
corrected sentence. Quote, number, fix. Do not rewrite passages that are
merely different from how you would have done it.

Do not edit any file under `book/` or `config/`. Do not commit.

Return: status (APPROVED or REVISE), counts by severity, and the single
worst finding.
