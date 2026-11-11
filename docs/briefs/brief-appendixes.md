# Brief: the back matter and the preface

Four writers, four dispatches, after the sixteen chapters are final. Each
reads, in order: this brief, its fact file, `docs/prose-contract.md`,
`docs/vocabulary.md`, `docs/markup.md`, `docs/continuity.md` (the bible:
the final chapter titles and the terms the chapters defined), and the
chapters it must agree with. The rules of the chapter brief template
(`TEMPLATE-chapter-brief.md`: no inventing, no dashes, no commits, the
report file, the short status) all apply.

## Appendix A: Command reference (`book/appendices/a-command-reference.md`, facts-A, about 6,000 words)

Heading: `# Appendix A: Command reference {.unnumbered}`. One entry per
command and subcommand in the fact file's catalog, alphabetical by
command, each entry a `## press <command>` heading (sentence case is
automatic) with these run-in parts in this order, as the period's
manual-page shape: **Synopsis** (a code block with the syntax line, `[ ]`
and `|` and `...`), **Description** (one to three sentences), **Options**
(a two-column table, option and meaning, or "None."), **Example** (a short
session), **See also** (chapter and sibling commands). Every flag the fact
file lists appears, including the ones it notes are absent from `--help`
(say "not listed by `--help`" for those). Exit codes and environment
variables close the appendix as two short sections.

## Appendix B: Configuration reference (`b-configuration-reference.md`, facts-B, about 4,000 words)

Heading: `# Appendix B: Configuration reference {.unnumbered}`. One `##`
per file (`config/metadata.yaml`, `config/front-matter.yaml`,
`config/house-rules.yaml`, `config/aesthetic.yaml`, `config/index-terms.yaml`,
`config/authorities.yaml`, `config/cover-styles.yaml`,
`config/illustration-styles.yaml`), then every key as a definition-list
term (**`key`** on its line, the definition indented with `: `): type,
default, meaning, and which chapter explains it. Nested keys as
`print.profile`. Values that `press config list` prints are the authority.

## Appendix C: Messages and refusals (`c-messages.md`, facts-C, about 3,000 words)

Heading: `# Appendix C: Messages and refusals {.unnumbered}`. Grouped by
the command that emits them (`press check`, the build, each verifier,
intake, the print pack, registrations). Each message as a definition term
in constant width exactly as the fact file quotes it (angle-bracket
placeholders kept), then two short paragraphs labelled in bold run-in:
**Cause.** and **Remedy.** Only messages the fact file quotes verbatim.

## Appendix D: The toolchain, platform by platform (`d-the-toolchain.md`, facts-D, about 2,000 words)

Heading: `# Appendix D: The toolchain, platform by platform {.unnumbered}`.
Sections: Debian and Ubuntu (what the toolchain image installs, as the
fact file lists it, with the two Ubuntu scars), macOS with Homebrew and a
TeX distribution (only what the fact file supports; name no version), the
toolchain image itself (how to run a build in it), and what is untested.
No version numbers the fact file does not state.

## Appendix E: Glossary (`e-glossary.md`, facts-E, about 3,000 words)

Heading: `# Appendix E: Glossary {.unnumbered}`. The fact file's terms,
alphabetical, as a definition list with the term in bold, one to three
sentences each, cross-referencing other entries in italic and the chapter
that treats the term. Add any term the continuity bible lists as defined in
a chapter and missing here.

## Colophon (`z-colophon.md`, about 400 words)

Heading: `# Colophon {.unnumbered}`. The plate line and its `art:` comment
at the top stay exactly as they are. Three paragraphs in the museum-label
register of the style guide's section 1.7: first, the animal: "The animal
on the cover of *Publishing with Press* is a common cuttlefish (*Sepia
officinalis*)." followed by four to eight sentences of natural history
(range in the eastern Atlantic and the Mediterranean; mantle to about 45
cm; eight arms and two feeding tentacles; the W-shaped pupil; colour
change through chromatophores; the ink from which the pigment sepia takes
its name; a life of one to two years) with no link drawn to the software.
Second, production: the book was written in Markdown and set by pandoc
and LuaLaTeX under press 3.0.2, the pipeline it describes; the text face
is Libertinus Serif and the code face Source Code Pro; the diagrams were
drawn with Graphviz and Pillow from scripts kept with the manuscript; the
plates and the cover engraving were commissioned from an image model and
finished through the press's own intake; the text was drafted by language
models working from a fact base extracted from the press source and its
documentation, under direction, and checked by a squad of editorial
agents against that fact base. Third, the cover: the design follows the
tradition of the engraved-animal technical manual; the type is [the art
director's report names it]; the band is sepia.

## Preface (`book/chapters/00-preface.md`, about 2,500 words)

Heading: `# Preface {.unnumbered}`. No "In this chapter" box. Two to four
untitled opening paragraphs: why a book about press (one manuscript, every
edition, verified), where press came from (extracted from one book, the
scars), what version this book describes. Then the A-heads in this order:
"Who should read this book"; "Organization of this book" (one short
paragraph per chapter and appendix, bold chapter number and italic title,
verb-first, from the final titles in the bible); "Conventions used in this
book" (the definition list from `docs/style-guide.md` section 7 adapted:
italic, constant width, the `$` and `#` prompts, `[ ]` and `|`, the Tip and
Warning boxes described in words since there are no icons, figure and
table numbering by chapter); "Using code examples"; "How to contact us"
(the repository issue tracker URL from `config/metadata.yaml` and the docs
site; no postal address, no phone); "Acknowledgments" (brisk: the press's
maintainer, the machines, the example book's author Lewis Carroll for the
sample text, and the reader who files the first erratum).
