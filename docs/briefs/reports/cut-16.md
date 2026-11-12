# Cut report: 16-inside-the-press.md

Words: 6171 before, 5718 after. `press check`: passed (source, checker self-test, editorial, jargon).
Sentinel "the selftest skips the checks" survives verbatim (line "From an installed wheel, ...").

## Changes

1. `16:23` (tic, word count). Before: "The press's *CLAUDE.md* states the rule in one sentence:" After: "The press's *CLAUDE.md* states the rule:"
2. `16:74` (retold, edition names; keeper Preface/Ch 1). Before: "The EPUB writer makes the Circulating edition (EPUB) ... go to *dist/* without pandoc." (four sentences). After: "The EPUB, HTML, chunked HTML, plain, and DOCX writers make the other five rendered editions. The stitched Markdown and the source zip go to *dist/* without pandoc." (The brief's semicolon became a period, per the no-semicolon rule.)
3. `16:78` (retold, verify-formats exception; keeper Ch 8). Before: "...so a verify target rebuilds the artifacts it verifies. There is one exception. `press verify-formats` reads an existing *dist/alice.pdf* into its cross-edition agreement check without rebuilding it." After: "...so a verify target rebuilds the artifacts it verifies, with the one exception Chapter 8 names."
4. `16:84-86` (retold, SOURCE_DATE_EPOCH; keepers Ch 7, Ch 8). Before: three sentences plus `[^16-epoch]`. After: "Two fixed dates keep the artifacts reproducible: `SOURCE_DATE_EPOCH` (Chapter 7) and the source zip's member timestamp (Chapter 8)." Footnote `[^16-epoch]` cut.
5. `16:100` (retold, jargon lint twice; keeper Ch 15). Before: "One fact lives in two places on purpose. The jargon lint exists ... installed. The `jargon_parity` check requires the two copies to match byte for byte." After: "One fact lives in two places by design: the jargon lint and its copy in the overused-jargon skill (Chapter 15). The `jargon_parity` check requires them to match byte for byte."
6. `16:146` (retold, CI=false; keeper Ch 8). Before: "Chapter 8 gives the reason: a variable set to `CI=false` would still read as true." After: "Chapter 8 gives the reason."
7. `16:167` (maxim, cut, ends earlier). "An invariant without its limits invites you to lean on it where it does not hold." cut.
8. `16:178` (retold, verify-formats exception). "So does the cross-edition agreement check in `press verify-formats`, which reads whatever PDF already sits in *dist/*." cut.
9. `16:180-182` (retold, warning box). "Warning: Do not call a verifier module directly on *dist/* to check a book. ..." cut.
10. `16:226` (retold, 11.5 percent cover; keeper Ch 1). Before: "...output was *right*... a title-page generator shipped a dropped and a clipped cover at 11.5% coverage: the lines ran, the artifact was never inspected." The rule..." After: "...output was *right*." The rule..." Joining fix in the same paragraph, since "that title page" lost its antecedent. Before: "exists because of that title page." After: "exists because of the cover that passed at 11.5 percent (Chapter 1)."
11. `16:250-252` (retold, macos-14; keeper Ch 14). Marker `[^16-macos]` and footnote cut.
12. `16:256-268` (retold, trust receipts; keeper Ch 14). The five prose paragraphs cut to: "Chapter 14 describes the trust receipts, the twelve layers (@fig:trust-tiers), and the release receipt that names the wheel and toolchain digests. The ledger names the complete-chain rule `INV-release-receipt-chain`, and the selftest's `receipt_chain` check exercises it." @fig:trust-tiers, its caption, fig-alt, and art comment kept verbatim in Chapter 16: Chapter 14 does not carry the figure, and this editor may not touch Chapter 14. The figure reference was folded into the first sentence so the figure stays cited.
13. `16:321` (retold, scar defined; keeper Ch 1). "A *scar* is the press's word for a production failure turned into a guard." cut. The section now begins "The fourth law states the policy".
14. `16:354` (tic, plainly). Before: "*CONTRIBUTING.md* puts the point of `press all` plainly:" After: "*CONTRIBUTING.md* puts the point of `press all`:"

## Kept as keeper or protected

- Sidebar "The import the gate did not see" (keeper, `Popen`): full telling kept.
- `16:232` `Mr.` tie test (keeper): full telling kept.
- Maxims kept: `16:116` "`alice` must find another word for hers." and `16:90` "Before you add a list of anything to the press, look for the list that already exists."
- All "leave" entries in part 3 untouched. `16:160` "It states the property in one sentence." stays, as the brief says.

## Declined

- None. One adjustment: the brief's replacement text for `16:74` contained a semicolon, which the cutter rules forbid in prose. It was set as two sentences with the same words.
