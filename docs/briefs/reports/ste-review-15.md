# STE80 review: Chapter 15, The operator's desk and the editorial machines

File: `book/chapters/15-the-desk-and-the-machines.md`
Diff: `git diff HEAD -- book/chapters/15-the-desk-and-the-machines.md` (15 edits, as reported in `docs/briefs/reports/ste-15.md`)

Status: APPROVED. Blocks: 0. Should: 1.

`press check` passes (exit 0). No code span, command, path, flag, quotation, or identifier changed. No sentinel stands in this file, and none was introduced. No paragraph grew. Every split leaves its topic sentence first, and no sidebar, tip, or blockquote was touched.

## Findings

1. Line 34 (edit 3). Severity: should.
   Old: "Two of the workflows therefore end by running a target, `press check` or `press pdf`, whose exit status decides the result."
   New: "Two of the workflows therefore finish with a target, `press check` or `press pdf`, whose exit status decides the result."
   What went wrong: "finish with" is a phrasal verb, which S10 asks the editor to replace, not introduce. It can also read as "be done with a target" rather than "run a target as the last step". The edit also breaks the parallel with the next sentence, "The other two end in an audit by another agent." The old "by running" is a gerund after a preposition, not an "-ing" chain, the same case the editor declined at old line 95 ("without changing a byte"). The fact survives, so this does not block.
   Corrected: "Two of the workflows therefore run a target last, `press check` or `press pdf`, whose exit status decides the result." (Reverting to the old sentence is equally acceptable.)

## Checked and passed

- Edit 1 (line 18 to 20). "drove it by hand" became "drove press by hand". This is correct and necessary: after the split, the nearest noun before "it" is "the book" ("A workflow reads and writes the book for you"), so "it" would have pointed at the book. "press" is the referent of the old "it" ("You can drive press in two ways"). The restrictive clause "a workflow that reads and writes the book for you" became the statement "A workflow reads and writes the book for you"; the claim was already general in the old sentence, so nothing is strengthened. The new paragraph "The workflows are the agent route. They read *skills*, ..." keeps "they" bound to the workflows.
- Edit 11 (line 307). The Claude Code session option now stands in its own sentence: "You can also tell your Claude Code session to read that file before it writes." No fact moved. The split also removes a scope fault in the old sentence, where "To read a skill yourself" governed the option in which the agent does the reading. "that file" refers back to "the path that `press skills` prints", as it did before.
- Edits 13 to 15 (Table 15.6). The three cells now read "The grammar that `--help` prints does not list the flag." (the `press improve` cell names `--rounds`, which is right because `--apply` is listed). This matches facts-15 item 23 ("exist in code but not in `--help`") and the lead-in sentence at line 323, so the four statements now use one term (S11). Flags, commands, and the path *config/aesthetic.yaml* are unchanged. The pipe table still parses.
- Edits 2, 4, 5, 10 (paragraph splits). No sentence changed; each new paragraph opens on its topic.
- Edits 6, 7, 8, 9, 12 (sentence splits). Every fact, number ("at most 12", "four arguments"), quotation ("in full", "Why the diseases are hard-coded"), and footnote marker (`[^15-popen]`) survives in place.
