# Cutter brief (one per file group)

You are a chapter editor making the cutting pass. Read, in order:
docs/briefs/cutting-brief.md in full (its five parts: retold facts with the
keeper chapter, the three tics, the closers marked keep or cut, the shoulds by
file, the passages to protect), docs/prose-contract.md, docs/vocabulary.md,
then your files.

Apply every entry in the cutting brief that names your files: cut or point
every retelling whose keeper is another file, exactly as the brief says; drop
the counted-quotation phrases ("in eight words"), every "plainly", and every
"broken here to fit the page" aside (keep the line break itself); end each
paragraph marked cut one sentence earlier, or fold its fact back as the brief
says; apply the shoulds. Protect the passages the brief lists. Where a cut
leaves a paragraph needing a joining clause, write the shortest one. Where
your file is the keeper of a fact, keep its full telling.

Rules: every fact, code span, path, flag, number, version, quoted press
message, example, table, figure line, and art comment stays verbatim unless
the brief names it. No em or en dashes, no curly quotes, no semicolons in
prose, ASCII plus accented Latin. Paragraphs under 190 words. Headings and the
"In this chapter" box unchanged. The three sentinel phrases must survive
verbatim: "On a fresh scaffold it succeeds" (Chapter 1), "You do not choose
the witness" (Chapter 8), "the selftest skips the checks" (Chapter 16).

Run `~/code/.pwp-venv/bin/press check` from the repository root; it must pass
(a failure naming another editor's file is not yours: rerun once, then report
it). Do not commit. Do not touch any file outside your group. Write
docs/briefs/reports/cut-<NN>.md listing each change (before, after or "cut"),
then return four lines: words before and after per file, entries applied,
entries declined with reason, press check result.
