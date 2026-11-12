# STE80 desk report: Chapter 15, The operator's desk and the editorial machines

File: `book/chapters/15-the-desk-and-the-machines.md`

## Ratchet count

- Before: 4 under the ratchet as it stood when the desk started
  (paragraph-length at 21, ing-form at 29, paragraph-length at 82,
  paragraph-length at 302 for the sidebar). While this desk worked,
  `tools/ste-ratchet.py` and `tools/ste-baseline.json` changed (the
  ratchet now unwraps sidebar blockquotes, and the baseline for this file
  is now 3). Under the current ratchet the unedited file scores 3.
- After: 0.
- `press check`: passes (exit 0).
- The three sentinels: untouched (none stands in this file).

## Edits (line numbers are in the edited file)

1. Line 18, S2 (28 words) and S13 (paragraph would reach 7 sentences).
   Old: "You can drive press in two ways: by hand, one target at a time, or by agent, through a workflow that reads and writes the book for you. Every earlier chapter drove it by hand from a shell prompt. ... The workflows are the agent route, and they read *skills*, ..."
   New: "You can drive press in two ways: by hand, one target at a time, or by agent, through a workflow. A workflow reads and writes the book for you. Every earlier chapter drove press by hand from a shell prompt. ..." New paragraph at line 20: "The workflows are the agent route. They read *skills*, the packaged authoring guides that come with press, which an agent reads before it writes. The examples use ..."
   ("it" became "press" because the antecedent moved to an earlier sentence.)
2. Lines 24 to 26, S13 (7 sentences, ratchet lead). Split the paragraph after "Both routes reach the same code." The second paragraph holds the desk's child process, the documentation's quotation, and the RUN view's definition. No sentence changed.
3. Line 34, S8 ("-ing" form, ratchet lead).
   Old: "Two of the workflows therefore end by running a target, `press check` or `press pdf`, whose exit status decides the result."
   New: "Two of the workflows therefore finish with a target, `press check` or `press pdf`, whose exit status decides the result."
4. Lines 47 to 49, S13 (7 sentences; the ratchet missed it). Split after "@fig:the-desk shows it on `hatter`." The first paragraph names the home screen and the read model, and the second describes the screen's layout. No sentence changed.
5. Lines 89 to 91, S13 (7 sentences, ratchet lead). Split after the stage-line sentence. The second paragraph holds the three log markers. No sentence changed.
6. Line 95, S2 (27 words) and S1.
   Old: "The desk passes the arguments to the child as a list, never as a shell string, so nothing you type in the argument box reaches a shell."
   New: "The desk passes the arguments to the child as a list, never as a shell string. As a result, nothing you type in the argument box reaches a shell."
7. Line 156, S1 and S2 (27 words, three actions).
   Old: "The `press workflows` command reports each workflow's arguments, compares the book's copy with the installed package, and prints the line you would paste to run it."
   New: "The `press workflows` command reports each workflow's arguments and compares the book's copy with the installed package. It also prints the line you would paste to run it."
8. Line 210, S1 and S2 (29 words, four actions).
   Old: "It reads the book through the four prose skills (...), collects suggestions, applies the ones that survive judgment, and holds the result to the checker."
   New: "It reads the book through the four prose skills (...) and collects suggestions. It applies the ones that survive judgment and holds the result to the checker."
9. Line 212, S1 (two unrelated ideas joined by "and").
   Old: "A coined maxim is a short invented saying that closes a paragraph, and the section "Why the diseases are hard-coded" later in this chapter explains why the workflow rations them."
   New: "A coined maxim is a short invented saying that closes a paragraph. The section "Why the diseases are hard-coded" later in this chapter explains why the workflow rations them."
10. Lines 224 to 226, S2 (30 words) and S13 (paragraph would reach 7 sentences).
    Old: "One agent for each chapter file reads all four prose skills "in full" and returns at most 12 suggestions, each with the current text, the proposed text, and a reason."
    New: "One agent for each chapter file reads all four prose skills "in full" and returns at most 12 suggestions. Each suggestion carries the current text, the proposed text, and a reason."
    The paragraph splits before "Three more agents read the whole book ...": the chapter agents, then the whole-book lenses.
11. Line 307, S2 (27 words).
    Old: "To read a skill yourself, open the path that `press skills` prints for it, or tell your Claude Code session to read that file before it writes."
    New: "To read a skill yourself, open the path that `press skills` prints for it. You can also tell your Claude Code session to read that file before it writes."
12. Line 323, S1 and S2 (26 words).
    Old: "Three of the flags in the table exist in the code but do not appear in the grammar that `--help` prints, and the table says so."
    New: "Three of the flags in the table exist in the code but do not appear in the grammar that `--help` prints. The table says so."
13. Line 327 (Table 15.6, `press improve` cell), S6.
    Old: "The `--rounds` flag is not listed by `--help`."
    New: "The grammar that `--help` prints does not list the `--rounds` flag."
14. Line 328 (Table 15.6, `press research` cell), S6.
    Old: "The flag is not listed by `--help`."
    New: "The grammar that `--help` prints does not list the flag."
15. Line 329 (Table 15.6, `press aesthetic` cell), S6. Same change as edit 14.

## Leads declined

- Old line 302 (sidebar "The jargon lint, twice", 9 sentences counted as one
  paragraph): the sidebar is Light mode. It holds two paragraphs of 5 and 4
  sentences, about 150 words, with no sentence over 30 words and no
  semicolon. The current ratchet no longer reports it.
- Old line 79, "The desk grays out ... when the doctor finds pandoc, LuaLaTeX, or latexmk at fault": the condition follows, but the sentence describes the desk and gives no command. Left as written.
- Old line 95, "without changing a byte": an idiomatic gerund after a preposition, not an "-ing" chain. Left as written.
- Old line 190 (procedure step 7) holds two reads in one step. They form one review action, so I kept the step.

## Passives kept

- Line 133, "An API key pasted into the description field by mistake never reaches the file": a participle that describes the key. The actor (whoever pastes) does not matter.
- Line 154, "a book scaffolded under an older press": a participle naming the book. The actor is `press new`, and the sentence before already names it.
