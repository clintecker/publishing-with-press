# Cut report: 08-verifying-the-artifacts.md

Words: 7850 before, 7594 after (wc -w).

## Changes

1. `08:17` (maxim, cut with preceding sentence). Before: "A build that exits with status zero tells you that pandoc and LuaLaTeX stopped without complaint. It tells you nothing about the pages inside the PDF. Press therefore opens every artifact it makes, ..." After: "Press opens every artifact it makes, ..."
2. `08:25` (word-counted quotation). Before: "The press ROADMAP puts the same idea in fewer words. Verifiers prove artifacts as objects ..." After: "The press ROADMAP says the same: verifiers prove artifacts as objects ..."
3. `08:27` (retold, 11.5 percent cover, keeper Chapter 1). Before: the full paragraph quoting CONTRIBUTING and retelling the dropped and clipped cover. After: "The press learned this law from the cover that passed at 11.5 percent coverage (Chapter 1), and drew a rule from it: "A producer is only proven by a verifier that rejects a broken artifact." The cover check later in this chapter is that rule at work."
4. `08:135` (maxim, ends earlier). Cut: "The verifier now does it on every verify run, so nobody has to remember." The sidebar now ends at the CLAUDE.md quotation.
5. `08:162` (fit the page). Before: "If they do not, the verifier prints this message, here broken across two lines to fit the page:" After: "If they do not, the verifier prints:"
6. `08:169` (fit the page). Before: "The message names a likely cause. It appears here on three lines to fit the page:" After: "The message names a likely cause:"
7. `08:177` (retold, keeper Chapter 12). Before: "Without a cover, the target prints `no assets/cover.jpg; interior verified, wrap not built` and stops there." After: "Without a cover, the target stops after the interior."
8. `08:181` (fit the page). Before: "If the page renders blank, it prints this message, broken here to fit the page:" After: "If the page renders blank, it prints:"
9. `08:194` (fit-the-page aside, general rule; not listed in the brief). Before: "The slug reads `alice`, and the page breaks the line in three." After: "The slug reads `alice`."
10. `08:252` (fit the page). Before: "Two more messages concern the metadata, the first broken here to fit the page:" After: "Two more messages concern the metadata:"
11. `08:274` (fit the page). Before: "with the slug changed to `alice` and the long lines broken to fit the page." After: "with the slug changed to `alice`."
12. `08:310` (fit the page). Before: "Inside the image, the verifier prints this message instead, broken here to fit the page:" After: "Inside the image, the verifier prints instead:"
13. `08:317` (maxim, fold). Before: "The toolchain image sets `PRESS_TOOLCHAIN`. An ordinary workstation does not." After: "The toolchain image sets `PRESS_TOOLCHAIN`, and an ordinary workstation does not." (The brief's fold uses a semicolon; the no-semicolon rule wins, so ", and" joins the clauses.)
14. `08:390` (fit the page). Before: "When everything passes, the verifier prints its line, broken here to fit the page:" After: "When everything passes, the verifier prints:"
15. `08:420` (fit the page, cut outright). Before: "... counts the missing chapters. It prints as one line, broken here to fit the page:" After: "... counts the missing chapters:" (the colon is the joining mark into the block).
16. `08:447` (retold, commerce gate, keeper Chapter 7). Before: the paragraph giving both gate messages, the PRESS_RELEASE enforcement, and the Example 1.2 pointer. After: "A commerce gate follows the verifiers (Chapter 7)."
17. `08:449` (retold, `book_inputs()`, keeper Chapter 7). Before: the paragraph on `book_inputs()` deleting *build/generated/* and the ARCHITECTURE quotation. After: "The law reaches the generated inputs too: every pandoc build regenerates them first (Chapter 7)."
18. `08:492` (should, hyphenation). Before: "A missing sentinel has three usual causes." After: "A missing sentinel has four usual causes." and appended: "The fourth is a word in the phrase that LuaLaTeX hyphenated at a line end. Choose shorter words or another phrase." (The brief's semicolon became a period.)

## Left as the brief says

- `08:91` and `08:128` maxims kept (the chapter's two). `08:216`, `08:230`, `08:250`, `08:298`, `08:400` left.
- `08:210` left (first statement of the agreement check). `08:433`, `08:439` kept as the keeper of the verify-formats exception. `08:453-455` warning kept.
- `08:317` and `[^8-ci-false]` kept as the keeper of `CI=false`. Sidebar `08:130-136` kept as the keeper of `hypcap`. `08:339` kept for the zip timestamp.
- Protected passage `08:216-230` untouched. The sentinel "You do not choose the witness" survives verbatim.

## Declined

- None declined. Two semicolons the brief wrote into fixes (items 13 and 18) became a comma plus "and" and a period, because the no-semicolon rule applies to prose.

## press check

Passed (exit 0): source, checker self-test, editorial, and jargon checks.
