# Controlled vocabulary: one term per thing

Every writer uses these words for these things, for the whole book. The
left column is the only word; the right column names the words that are
not used for it. First use of each term in a chapter is italic and
defined in the same sentence; afterwards it is roman.

| Use this | For | Never these |
|---|---|---|
| press | the package and command; lowercase in prose and code; capitalised as "Press" only where it opens a sentence, like any word; the command itself is always constant width `press` | the press tool, the pipeline (as a name) |
| the press | the same thing spoken of as an institution ("the press refuses") | it/the system |
| book repository | the directory with `config/metadata.yaml` | project, repo (in prose), book folder |
| the manuscript | the chapters and appendices under `book/` | the source, the content, the text (for the files) |
| chapter file / appendix file | one Markdown file | section file, document |
| target | a `press` command that builds, checks, or verifies | task, step, stage, job, goal |
| edition | one published form of the book | format (use only for a file format such as PNG), output, version |
| the Print edition (PDF), the Circulating edition (EPUB), the Single-leaf edition (the self-contained HTML), the Manuscript edition (the stitched Markdown), the Telegraphic edition (plain text), the Office edition (DOCX), the Chapter edition (the reader site and its zip), the Source edition (the source zip) | press's own names for the editions, from its landing page; use the name, glossed once per chapter with its format in parentheses | the PDF edition, the Markdown edition, the text edition, the web edition, the e-book |
| artifact | a file or directory in `dist/` that the registry names | output, product, deliverable, build |
| the registry | the artifact graph in `registry.py` | the graph, the DAG, the table |
| the catalog | the typed command table | the command list, the menu |
| verifier | a `verify_*` module or the check it runs | validator, checker (reserved for `press check`), test |
| the checker | `press check` and its four passes | linter, validator, verifier |
| house rules | `config/house-rules.yaml` | style rules, lint config |
| the house | press's default design and law | the default theme, the stock look |
| the watchlist | the jargon term list | banned words, the blocklist |
| known-bad fixture | a file that must be rejected | negative test, bad example |
| sentinel | a `verify-sentinels` phrase | marker, canary, probe |
| witness | a text the verifiers require every edition to carry: a sentinel, the title, the manuscript witness line, a chapter witness line | fingerprint, signature, marker |
| the Alice book | the book's sample: user alice's full novel, slug `alice` | the Alice example, the sample book (after first use), Alice's book |
| the press's own three-chapter Alice example | press's gallery example `examples/alice-in-wonderland`, chapters 1 to 3 plus one appendix, 23 pages; the source of every real capture; after first mention in a chapter, "the three-chapter example" | the Alice example, the gallery Alice, the demo |
| the Pages bundle | the directory `dist/pages/` | the pages directory, the site bundle |
| the Pages site | what GitHub Pages serves from the bundle | the Web site, the landing site |
| vacuous witnesses | press's own phrase, in its refusal, for sentinels or a page floor too weak to prove anything (an empty sentinel list, a one-page floor); quote it only where press's message is quoted | weak sentinels, placeholder sentinels |
| release witnesses | press's own term for the release floor: at least two sentinels and `verify-min-pages` of 24 or more, enforced under `PRESS_RELEASE=1` | release requirements, release gate (reserved for the commerce gate) |
| plate | an unnumbered illustration in the List of Plates | woodcut (except when naming the idiom), picture, image (use image for the file) |
| figure | a numbered informative illustration ("Figure 5.2") | diagram (use only for the kind `.diagram`), graphic, illustration (use for the general class) |
| placement | where a figure sits (`inline`, `wrap-inner`, `wrap-outer`, `plate`, `full-bleed`, `frontispiece`) | position, layout, float |
| measure | the width class (`full-measure`, `half-measure`, `third-measure`) | width, size, column |
| wrap | text flowing beside a figure | runaround (give once as the trade name), float |
| set piece | `::: cascade`, `::: verse`, `::: tail` | special block, custom div |
| chapter opening | the drop cap and its style | initial, lettrine (give once), drop cap (use for the `drop-cap` style only) |
| scene break | the `***` thematic break | section break |
| ornament | the scene-break glyph (rule, asterism, fairy-dust) | decoration, flourish |
| decoration | an image marked `decorative=true`: empty alt, never numbered, never listed | ornament, dingbat |
| profile / design profile | a sealed interior geometry (`house-6x9` and the rest) | trim preset, layout, theme |
| provider | a print vendor spec (`house`, `lulu`, `kdp`, `ingramspark`) | printer (reserved for the machine or shop), vendor, service |
| the print pack | print interior, cover wrap, checklists | print mode, print build |
| cover wrap | the back-spine-front PDF | jacket, full cover, wraparound |
| the toolchain | pandoc, LuaLaTeX, latexmk, fonts, epubcheck, poppler | the stack, dependencies, prerequisites |
| the toolchain image | `ghcr.io/clintecker/press-toolchain` | the container, the Docker image (except when the sentence is about Docker) |
| the composite action | `action.yml` | the GitHub Action, the plugin |
| the reusable workflow | `build.yml` | the pipeline, the CI config |
| the release contract | the workflow that proves a tag | the release check, release CI |
| floating tag / immutable tag | `v3` / `v3.0.2` | moving tag, major tag, pinned tag (use "pin" for the act) |
| the aesthetic | `config/aesthetic.yaml` and its merge | theme, style config, look |
| art target | the `--as` value of `press art accept` and the `[targets]` of `press art commission` (cover, plate, logomark, portrait); press's own synopsis word, so keep it, always with "art" in front | target (reserved for a CLI command), kind, slot |
| commission | a prompt for an image model, in `art/commissions.md` | prompt (use for the text itself), request |
| intake | what `press art accept` does | import, ingest, acceptance (use for the record) |
| alpha master | a plate kept as ink on transparency | transparent PNG, master file |
| the table of authorities | the ledger `config/authorities.yaml` and the claims it holds | the authorities file, the sources ledger, the citations |
| the sources companion | the generated `dist/<slug>-sources.md`, the Sources edition's companion document | the authorities document, the sources appendix, the bibliography |
| the logomark | the imprint device, `assets/press-logo.png` | the logo, the imprint logo, the press mark (the pilcrow is press's own mark, a different thing) |
| leaf | one sheet of the book, two pages (the trade sense); a cleared leaf is a page a figure has to itself | page (when the sheet is meant), column |
| the paper column | the reader site's framed column that holds the text, styled as a sheet | the leaf, the sheet, the measure (reserved for a figure's width class) |
| height cap | the per-profile limit on a figure's rendered height (the `figure-cap` key); 6.3 in on the house profile | figure cap (say the key name once), image cap |
| the desk | `press desk` | the TUI, the dashboard, the UI |
| workflow | a packaged agent procedure | pipeline, automation, playbook |
| skill | a packaged authoring guide | prompt, guide, doc |
| operator | `press improve`, `press research`, `press aesthetic` | runner, driver, headless mode |
| scar | a production failure turned into a guard | lesson, gotcha, footgun |
| invariant | an `INV-` ledger entry | guarantee, rule, contract (reserved for the release contract and the extension contract) |
| the quality gate | the celebrimbor gate | CI checks, the ratchet (use for a floor) |
| refuse / refusal | what press does when it stops with a message | error out, reject (use for fixtures and intake) |
| fail | what a check, a pass, a verifier, or a build does when its result is red; ordinary English, allowed for any of them | error, break |
| checker self-test | the checker's second pass, which proves each fixture trips its rule (press prints `Checker self-test passed`) | checking the checkers (as a name; fine as a description), the fixture pass, selftest (that is `press selftest`, press's own test suite) |
| run | what you do with a command | execute, invoke, fire |
| directory | a folder | folder |
| Web site, Web page, the Web, e-mail, filename, manpage, appendixes, Unix | spellings | website, email, file name, man page, appendices, UNIX |
