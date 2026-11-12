# Cut report: 07-building-the-editions.md

Words: 7061 before, 6869 after. `press check`: passed.

## Changes

1. `07:45` (retold, edition names; keepers Preface and Table 1.2).
   Before: "The press's landing page gives the editions names of their own. The reading editions are the Print edition (the PDF), ... and the Source edition (the source zip). The rest of this chapter calls ..."
   After: "The rest of this chapter calls the PDF, the EPUB, the single-file HTML, and the reader site by their formats, as the targets do. It uses the press's names for the Manuscript, Telegraphic, Office, and Source editions."

2. `07:59` (fit-the-page tic).
   Before: "Example 7.1 shows the line for the single-file HTML, broken across lines to fit the page."
   After: "Example 7.1 shows the line for the single-file HTML."

3. `07:214-218` (retold, font scan; keeper Chapter 2).
   Before: "The first LuaLaTeX run on a new machine spends several minutes on a font scan, and it looks like a hang. It is not one." and the Tip "Run `press pdf` on a new machine well before you need the PDF, and leave it alone until it finishes."
   After: cut (both).

4. `07:339` (retold, verify-formats exception; keeper Chapter 8).
   Before: "Every verify target rebuilds the artifacts it verifies before it verifies them, and the command line offers no way around that. The one exception is `press verify-formats`, which reads an existing *dist/alice.pdf* into its cross-edition agreement check without rebuilding it."
   After: "Every verify target rebuilds the artifacts it verifies before it verifies them (one exception, Chapter 8), and the command line offers no way around that."
   (The pointer sits before the "and" clause so it attaches to the rebuild rule, not to "no way around that".)

5. `07:343-345` (retold, warning on the same fact).
   Before: Warning "Do not call a verifier module from your own script to save time. Run the `press` target instead, so the rebuild happens first."
   After: cut. The invariant paragraph at `07:341` is kept whole.

6. `07:351-355` (retold, cover-wrap message; keeper Chapter 12).
   Before: "Without a cover, it stops after the interior and says so:" plus the block `no assets/cover.jpg; interior verified, wrap not built`.
   After: "Without a cover, it stops after the interior and says so." (block cut)

7. `07:367` (maxim, cut, ends earlier).
   Before: "The deletion comes first on purpose. In the words of the press's architecture notes, ..."
   After: "In the words of the press's architecture notes, ..."

8. `07:420` (maxim, cut, ends earlier).
   Before: "The check step matters more than it looks. The known-bad fixtures run ..."
   After: "The known-bad fixtures run ..."

9. `07:433` (fit-the-page tic).
   Before: "The press prints that message on one line, broken here to fit the page. A book that enables print ordering gets the gate."
   After: "A book that enables print ordering gets the gate."

10. `07:440` (same rule, not itemised in the brief).
    Before: "That message is also one line in the log. When the release build sets ..."
    After: "When the release build sets ..."
    Reason: the brief's rule that a message shown on several lines carries no aside about the page (the Preface states the convention once); with change 9 made, "also" no longer had an antecedent.

11. `07:509` (footnote moved in from Chapter 3, `[^3-wordcount]`, per the wordcount entry; Chapter 7 is the keeper).
    Before: "... so the `art:` comment beside every figure counts toward the total. If you write ..."
    After: "... counts toward the total.[^7-wordcount] If you write ..." with
    "[^7-wordcount]: The counter matches words with the pattern `\b[\w'-]+\b`, so a hyphenated compound or a contraction counts as one word."
    The Chapter 3 editor removes `[^3-wordcount]` from 03; that file was not touched here.

## Kept as the brief directs

- `07:143` and `07:339` closers (the chapter's two maxims).
- Leaves at `07:47`, `07:72`, `07:80`, `07:295`, `07:422`, `07:440` (pointer clause), `07:444`, `07:456`.
- Keeper passages: sidebar "The lists that would not converge" (`07:206-212`), "Generated inputs" (`07:359-369`), "What press all leaves out" (`07:442-448`), "Counting the words" (`07:496-509`), Table 7.2 and `[^7-epoch]`.

## Declined

None.
