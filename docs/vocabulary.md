# Controlled vocabulary: one term per thing

Every writer uses these words for these things, for the whole book. The
left column is the only word; the right column names the words that are
not used for it. First use of each term in a chapter is italic and
defined in the same sentence; afterwards it is roman.

| Use this | For | Never these |
|---|---|---|
| press | the package and command; lowercase in prose and code | Press (except at a sentence start), the press tool, the pipeline (as a name) |
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
| witness | the manuscript or chapter witness line | fingerprint, signature |
| vacuous witnesses | press's own phrase, in its refusal, for sentinels or a page floor too weak to prove anything (an empty sentinel list, a one-page floor); quote it only where press's message is quoted | weak sentinels, placeholder sentinels |
| release witnesses | press's own term for the release floor: at least two sentinels and `verify-min-pages` of 24 or more, enforced under `PRESS_RELEASE=1` | release requirements, release gate (reserved for the commerce gate) |
| plate | an unnumbered illustration in the List of Plates | woodcut (except when naming the idiom), picture, image (use image for the file) |
| figure | a numbered informative illustration ("Figure 5.2") | diagram (use only for the kind `.diagram`), graphic, illustration (use for the general class) |
| placement | where a figure sits (`inline`, `wrap-inner`, `wrap-outer`, `plate`, `full-bleed`, `frontispiece`) | position, layout, float |
| measure | the width class (`full-measure`, `half-measure`, `third-measure`) | width, size, column |
| wrap | text flowing beside a figure | runaround (give once as the trade name), float |
| set piece | `::: cascade`, `::: verse`, `::: tail` | special block, custom div |
| chapter opening | the drop cap and its style | initial, lettrine (give once), drop cap (use for the `drop-cap` style only) |
| scene break | the `***` thematic break | section break, ornament (use for the glyph) |
| profile / design profile | a sealed interior geometry (`house-6x9` and the rest) | trim preset, layout, theme |
| provider | a print vendor spec (`house`, `lulu`, `kdp`, `ingram`) | printer (reserved for the machine or shop), vendor, service |
| the print pack | print interior, cover wrap, checklists | print mode, print build |
| cover wrap | the back-spine-front PDF | jacket, full cover, wraparound |
| the toolchain | pandoc, LuaLaTeX, latexmk, fonts, epubcheck, poppler | the stack, dependencies, prerequisites |
| the toolchain image | `ghcr.io/clintecker/press-toolchain` | the container, the Docker image (except when the sentence is about Docker) |
| the composite action | `action.yml` | the GitHub Action, the plugin |
| the reusable workflow | `build.yml` | the pipeline, the CI config |
| the release contract | the workflow that proves a tag | the release check, release CI |
| floating tag / immutable tag | `v3` / `v3.0.2` | moving tag, major tag, pinned tag (use "pin" for the act) |
| the aesthetic | `config/aesthetic.yaml` and its merge | theme, style config, look |
| commission | a prompt for an image model, in `art/commissions.md` | prompt (use for the text itself), request |
| intake | what `press art accept` does | import, ingest, acceptance (use for the record) |
| alpha master | a plate kept as ink on transparency | transparent PNG, master file |
| the desk | `press desk` | the TUI, the dashboard, the UI |
| workflow | a packaged agent procedure | pipeline, automation, playbook |
| skill | a packaged authoring guide | prompt, guide, doc |
| operator | `press improve`, `press research`, `press aesthetic` | runner, driver, headless mode |
| scar | a production failure turned into a guard | lesson, gotcha, footgun |
| invariant | an `INV-` ledger entry | guarantee, rule, contract (reserved for the release contract and the extension contract) |
| the quality gate | the celebrimbor gate | CI checks, the ratchet (use for a floor) |
| refuse / refusal | what press does when it stops with a message | fail (use for a verifier result), error out, reject (use for fixtures and intake) |
| run | what you do with a command | execute, invoke, fire |
| directory | a folder | folder |
| Web site, Web page, the Web, e-mail, filename, manpage, appendixes, Unix | spellings | website, email, file name, man page, appendices, UNIX |
