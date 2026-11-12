# Indexer report

## Result

- `config/index-terms.yaml`: 249 flat terms, every one verified to match prose
  (code spans, blocks, and image lines stripped) before the build; zero
  zero-hit terms.
- `press check` passes (source checks, checker self-test, editorial checks,
  jargon check). `press pdf` builds (exit 0) and generated
  `build/generated/f-index-of-subjects.md`; I read the generated entries.
- The `<!-- index: ... -->` comments (and the blank line before each) are removed
  from chapters 00 to 16. No other file under `book/` was touched; Appendixes
  A and E and the colophon were left alone.

## Shape

Candidates came from all 17 chapter comments (about 560 unique), merged by
singular and plural and by alias. Compound entries use the period-index form:
"figures, numbering of", "figures, placement of", "EPUB, identifier of",
"major versions, design", "widows and runts", "tail (set piece)", "desk, the",
"registry (the artifact graph)". Commands and filenames appear as typed.
Added from my own reading: Lulu, IngramSpark, KDP, KOMA-Script, Tenniel,
Carroll, Lewis, woodcut, barcode, hyphenation, small caps, grayscale, Ubuntu,
macOS, Homebrew, Pillow, pypdf, PyPI, Dependabot, TikZ, environment variables,
table of contents, page count.

## Terms cut, and why

- Zero prose hits (the word occurs only inside code spans): acceptance record,
  dot-key notation, microtype, module map, sha- tag, and about 40 candidates
  that are typed only as code (`press art accept`, `press pdf`, `render_defaults`,
  `PRESS_TOOLCHAIN`, `INV-graph-no-stale`, `house-6x9`, `scrbook`, and the like).
  Where a command is also described in prose it stays (for example `press check`,
  `press doctor`, `press isbn`).
- Too common to help a reader (a locator in nearly every chapter): press, edition,
  target, manuscript, artifact, claim, figure, plate, plates, EPUB, pandoc,
  LuaLaTeX, toolchain, verifier, checkers, book repository, Alice example,
  print pack, chapter file, dist directory, GitHub, Python, and the commands'
  generic words. Chapter-specific compounds replace them.
- Wrong sense: catalog (library catalog versus the press's catalog), prompt,
  tail, measure, trim, safety, workflow-in-general, operator (it matched the
  chapter 15 title cross-references), generic "checking".
- Duplicates folded: "EPUB identifier" into "EPUB, identifier of", "figure
  numbering" into "figures, numbering of"; "engraving" cut as generic.

## Loose matches (for the managing editor)

- "registry (the artifact graph)": matches "the registry", but chapter 14's
  "container registry" is excluded only by its wording; ch 2 mentions a tag
  registry in passing.
- "desk, the": hits cross-references to the chapter 15 title ("The operator's
  desk") in chapters 0, 3, 7, 10, 11 as well as real uses.
- "margins", "provider", "skills", "placement"/"figures, placement of": plain
  words that carry their sense in context but hit prose in other senses
  occasionally (provider in chapter 3, margin of a paperback in 12).
- "cascade" matches only "a cascade", so the CSS cascade in chapter 9 is not
  indexed under it.
- "scar", "front matter", "design profile", "art department", "ISBN",
  "sentinel", "workflows", "toolchain image", "metadata.yaml": 14 to 17 locators
  each once Appendixes A to E count; kept because each names a core concept, but
  the entries are long.
- Appendix A and E locators will shift when those appendixes are revised; the
  index regenerates on every build, so no action is needed unless a term loses
  its only hit there (none does: every term has a chapter hit).
- The index appendix lands as Appendix F (first free letter after E); the
  colophon (Z) is also scanned and contributes locators (Z) to a few terms.
