# STE80 editor report: Chapter 12, The print pack

File: `book/chapters/12-the-print-pack.md`

Ratchet count: 10 before (baseline 10, from the ratchet as it stood when
this desk started), 2 after. During the desk's work, `tools/ste-ratchet.py`
changed under it: rerun on the untouched HEAD text, the current ratchet
reports 8, not 10. It no longer joins the sidebar into one paragraph or
reports the 35-word line at 490. Against either figure, the file now
stands at 2. `press check` passes (exit 0). `python3 tools/ste-ratchet.py`
passes (no file rose).

Mode: Humanize for body prose, admonitions, table cells, and footnotes.
Light for the sidebar "The barcode that crowded its quiet zone" (no edit:
no sentence over 30 words, none with three ideas, no semicolon). No fence,
code span, quotation, command, path, YAML key, press message, figure line,
art comment, heading, or footnote label changed.

Sentinels: none of the three stands in this chapter (0 before, 0 after).
Index terms: every match string in `config/index-terms.yaml` occurs in the
chapter the same number of times before and after (scripted count).

## Edits (line numbers in the edited file)

1. L72, S1. Old: "The check `check_profile_seals` recomputes every digest and turns red when one disagrees, so a profile's geometry cannot change inside a release without a visible reseal." New: "The check `check_profile_seals` recomputes every digest and turns red when one disagrees. A profile's geometry therefore cannot change inside a release without a visible reseal."
2. L88, S1. Old: "The press generates its installed copy from it, and *docs/PROVIDER-DATA.md* gives the rule: "Never edit it by hand."" New: "The press generates its installed copy from it. The file *docs/PROVIDER-DATA.md* gives the rule: "Never edit it by hand."" ("The file" keeps the sentence from opening on a path.)
3. L105, S1. Old: "That makes it a sound default for a book with no shop chosen yet, and it also means the house spine is no real provider's spine." New: "That makes it a sound default for a book with no shop chosen yet. It also means that the house spine is no real provider's spine."
4. L137, S1 and S2 (30 words). Old: "The `constant` shape and the `ppi-table` shape both read `print.paper`, so a white book and a cream book get different spines at KDP, at IngramSpark, and on the house provider." New: "The `constant` shape and the `ppi-table` shape both read `print.paper`. A white book and a cream book therefore get different spines at KDP, at IngramSpark, and on the house provider."
5. L153, S10 (ratchet lead, phrasal verb). Old: "Run it when you want to look at the interior before any verifier reads it, for example after you move a figure." New: "Run it when you want to examine the interior before any verifier reads it, for example after you move a figure."
6. L157, S1 (three actions and a reason). Old: "It builds the interior, runs the print verifier on it, and then builds and verifies the cover wrap, because the Alice book has *assets/cover.jpg*." New: "It builds the interior and runs the print verifier on it. Then it builds and verifies the cover wrap, because the Alice book has *assets/cover.jpg*."
7. L159, S1. Old: "Its own targets do, and the *commerce gate* (the last step of `press all`) builds it in a book that enables print ordering." New: "Its own targets do. The *commerce gate* (the last step of `press all`) also builds it in a book that enables print ordering."
8. L165/167, S13 (ratchet lead, 7 sentences). Split at the turn from code to the second source of color. The new paragraph starts "Another source is a colored cover plate". No words changed.
9. L173, S1 and S3 (condition first). Old: "It needs the cover art at *assets/cover.jpg*, and without it the press refuses the target with `coverwrap needs assets/cover.jpg`." New: "It needs the cover art at *assets/cover.jpg*. Without it, the press refuses the target with `coverwrap needs assets/cover.jpg`."
10. L177, S1. Old: "The press fixes the bleed at `BLEED_IN = 0.125`, which the source calls "universal across print vendors", and every provider in the ledger declares the same 0.125in." New: "The press fixes the bleed at `BLEED_IN = 0.125`, which the source calls "universal across print vendors". Every provider in the ledger declares the same 0.125in."
11. L195/197, S13 (ratchet lead, 7 sentences). Split after "For a hardcover, they depend on the provider." The new paragraph holds the Lulu and IngramSpark figures.
12. L197, S1. Old: "The Lulu casewrap in Table 12.4 comes out 0.25in taller and 0.25in wider than its margins, hinges, trim, and spine alone give, and that difference is the two deltas." New: "The Lulu casewrap in Table 12.4 comes out 0.25in taller and 0.25in wider than its margins, hinges, trim, and spine alone give. That difference is the two deltas."
13. L221, S1. Old: "On a soft cover it also runs out through the bleed on the outer edge, so for the house example *assets/cover.jpg* fills 6.125 by 9.25 inches." New: "On a soft cover, it also runs out through the bleed on the outer edge. For the house example, *assets/cover.jpg* therefore fills 6.125 by 9.25 inches."
14. L223/225, S13. Split after "Any lettering on the front, the title included, belongs in *assets/cover.jpg* itself." The first paragraph places things on the panels. The second covers the field, the spine text, and the pointer to Chapter 11. Needed because edit 15 would make the paragraph 7 sentences.
15. L225, S1 (three ideas). Old: "On a printed cover, the press lays down a cloth-colored field, RGB (201,191,191), and for a `linen` cover it drops that field, since the cloth is real." New: "On a printed cover, the press lays down a cloth-colored field, RGB (201,191,191). For a `linen` cover, it drops that field, since the cloth is real."
16. L225, S8 (noun for verb). Old: "Chapter 11, *The art department*, covers the making of the cover art itself." New: "Chapter 11, *The art department*, tells how to make the cover art itself."
17. L252 (Warning), S1. Old: "The check digit shows only that the number is well formed, and nobody can correct a cover printed with the wrong book's ISBN." New: "The check digit shows only that the number is well formed. Nobody can correct a cover printed with the wrong book's ISBN." (The Warning is now three sentences.)
18. L306, S10 (ratchet lead, phrasal verb). Old: "...so the message tells you which check to look at." New: "...so the message tells you which check to examine."
19. L325, S1 (29 words). Old: "The ledger gives each researched shop a *disposition*, one of `primary`, `secondary`, `hosted-candidate`, `candidate`, or `not-fit`, and it scores each one on 11 capabilities, such as `api` and `one_copy_pod`." New: "...or `not-fit`. It also scores each one on 11 capabilities, such as `api` and `one_copy_pod`."
20. L388, S1. Old: "The full value lives in the manifest file that the gate writes, and that is where you copy it from for the record." New: "The full value lives in the manifest file that the gate writes. You copy it from there for the record."
21. L388/390, S13 (ratchet lead, 7 sentences, 8 after edit 20). Split at the turn from where the id appears to what it hashes. The new paragraph is "The id is a sha256 hash over the production facts only: ..." with the sentence that follows it.
22. L396, S1. Old: "It builds and verifies the files and writes a checklist, and you do the uploads and the account work at the shop." New: "It builds and verifies the files and writes a checklist. You do the uploads and the account work at the shop."
23. L488, S1. Old: "Whether a provider is legally the seller is a question for you and the provider's own terms, so confirm it before you publish the link." New: "Whether a provider is legally the seller is a question for you and the provider's own terms. Confirm it before you publish the link."
24. L503-509, S13 (ratchet lead, 8 sentences). The four footnote definitions stood on consecutive lines, so the counter read them as one paragraph. A blank line now separates them, as in Chapter 7. No words changed, and the labels are unchanged.

## Leads declined

- L51, ing-form "binding": a noun ("an unsupported trim, binding, or ink combination"), the print choice of Table 12.1.
- L419, phrasal verb "look at": "a first look at what a channel will ask" uses "look" as a noun. No phrasal verb is present.
- L181, 30 words (at the ceiling, not over it; a lead only under the old ratchet's 25-word line): "The wrap runs left to right in seven bands: ..." The sentence is one idea with a seven-item list in band order. A split would separate the list from its order.
- The sidebar "The barcode that crowded its quiet zone" (L259-265): the old ratchet counted it as one paragraph of 8 sentences. Light mode applies, and the sidebar is two paragraphs of 2 and 6 sentences, about 140 words. No sentence there is over 30 words, has three ideas, or has a semicolon. The current ratchet no longer reports it.
- Old L490/493, 35 words: a counter artifact under the old ratchet. The quotation ends with its period inside the quotes, so the counter joined "It does not "..."" to the next sentence. The real sentences are 4 words plus the quotation, and 16 words. The current ratchet no longer reports it.

## Passives kept

- L151, "It is set two-sided, with mirrored margins." The next paragraph names the actors (pandoc and latexmk). Naming them here would repeat that sentence.
- L19, "an interior and a cover, each built to the shop's own numbers", and L72, "a short digest of its contents, recorded in *profile-seals.yaml*": participial modifiers that describe the artifact. The actor (the press) is clear or does not matter.
- L257, "A book with no ISBN yet, and not declared for retail": the actor is you, and the sentence is about the book.

## Unsure, or outside this desk's remit

- Edit 7 adds "also". Edit 2 adds "The file". Edit 20 adds "there". Each is a joint and adds no fact.
- Edit 16: "covers the making of" became "tells how to make". The scope is the same, the making of the cover art.
- Not changed (a quotation, so outside the desk): Table 12.9, the `kdp` row (L414), has unbalanced double quotes. The second, third, and fourth items lack their opening quote marks: `"KDP account with tax interview completed", Category selections (2 allowed; note 10 keyword slots)", Pricing ...`. The quoted text also holds a semicolon. A copyeditor should restore the three opening quotes against press's source.
- L159 calls the commerce gate "the last step of `press all`". The vocabulary reserves "target" and bans "step" for a target. The gate may not be a target, so the desk left the word alone. It is a question for the vocabulary owner.
