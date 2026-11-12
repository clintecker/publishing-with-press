# STE80 review: Chapter 11, The art department

File: `book/chapters/11-the-art-department.md`, `git diff HEAD`. All 16 edits
in `docs/briefs/reports/ste-11.md` read hunk by hunk against the old text,
`docs/briefs/facts/facts-11.md`, and `docs/vocabulary.md`. `press check`
passes on the edited file. No paragraph is over 190 words, and no blockquote
is split.

Status: REVISE. Blocks: 1. Should: 0.

1. Tip, old line 112 (editor's edit 6).
   - Old: "Most options in this book are accepted but not listed."
   - New: "The commands accept most of the options in this book, but the help does not list them."
   - What went wrong: the scope of "most" moved. In the old sentence, "most"
     counts the options that are accepted *and* unlisted; every option in
     the book is accepted. In the new sentence, "most" qualifies "accept", so
     it says that some options in this book are not accepted. That is a
     changed fact: the book documents options that exist in code (facts-11,
     discrepancy 23, "all exist in code but not in `--help`"). "The help" is
     also a vaguer name for the `--help` output that the sentence before
     names.
   - Severity: blocks (fact changed).
   - Corrected: "The `--help` output does not list most options in this book, but the commands accept them."

## Checked and cleared

- Edit 8, old line 222 (three refusals as a list). The order is the same as
  the old sentence and as facts-11 ("not declared", data kind, no `art:`
  description). "The last refusal" in the next paragraph still points at the
  missing `art:` directive, and its quoted message is the #225 message for
  that case. The code span `.chart` / `.diagram` and `art:` are intact.
  `press check` accepts the list.
- Edit 4, old line 22. "can only use" to "can therefore use only": the scope
  of "only" is unchanged (the files), and "therefore" carries the old "so".
  No loss.
- Edit 16, old line 525. The `[^11-imagen]` marker moved to "straight to
  OpenAI or Google." The footnote gives the OpenAI and Gemini endpoints, so
  it explains that sentence. Its last sentence (the Imagen comment) is about
  Gemini and still reads correctly from there. Label and footnote text are
  unchanged.
- Edit 12. `[^11-upscayl]` stays on the sentence that names *Upscayl.app*,
  which its text explains. "first" adds no fact; the search order is the
  same as facts-11.
- Edit 7. The new sentence puts the title, the author, and the woodcut in
  the wide cream band. That matches facts-11 (middle band: title, author,
  and woodcut), so the old ambiguity resolved the right way.
- Edits 1, 2, 3, 5, 9, 10, 11, 13, 14, 15: no fact, qualifier, number, code
  span, path, or quotation changed. "may differ by at most 45" keeps its
  modal. Index terms (commission, art department, intake, flat-ground test,
  art target) keep their spelling.
- Sentinels: none of the three appears in this file.
