# Publishing with Press: Building Books from Plain Text

A technical manual about [press](https://github.com/clintecker/press),
the build, check, and verify pipeline for books, written in the idiom of
a late-1990s animal book and built by press itself. Sixteen chapters,
five appendixes, a generated index, forty-odd figures, six plates, and a
cuttlefish on the cover.

The manuscript is the plain Markdown under `book/`. Every edition
(the Print edition as PDF, the Circulating edition as EPUB, the
Single-leaf HTML, the Manuscript Markdown, the Telegraphic plain text,
the Office DOCX, the Chapter reader site, and the Source archive) is a
build artifact of that one manuscript. Nothing in `dist/` is checked in.

## Reading it

Once GitHub Pages is enabled for this repository, the reusable press
workflow publishes the landing page, the reader site, and every download
at <https://clintecker.github.io/publishing-with-press>.

To build it yourself, install press 3.0.2 and the toolchain (Appendix D
of the book covers each platform), then from this directory:

```text
$ press check
$ press all
```

`press all` checks the manuscript, builds every edition into `dist/`,
and verifies each artifact: the three sentinel phrases, the page floor,
the cover on page 1, epubcheck, and the rest. The print pack is
`press verify-print` and `press coverwrap`. A build in the pinned
toolchain image is the proof, and `tools/docker-build.sh` runs one.

## What is here

| Path | Holds |
|---|---|
| `book/chapters/`, `book/appendices/` | the manuscript, one file per chapter |
| `config/` | metadata, front matter, house rules, index terms |
| `assets/woodcuts/` | the figures and plates, 8-bit grayscale PNG at 300 dpi |
| `assets/cover.jpg`, `art/` | the cover and its commission record |
| `tools/figures/` | the scripts that draw every numbered figure |
| `docs/` | how the book was made: the design, the style guide, the prose contract, the controlled vocabulary, the continuity bible, the desk briefs, every review report, and the production ledger |
| `tests/known-bad/` | fixtures the checker must reject on every build |

## How it was made

The book was drafted and edited by language models working from a fact
base extracted from the press source and its documentation, under
direction, and checked by a squad of editorial desks (fact checker,
developmental editor, copyeditor, typesetter, continuity editor,
illustrator, art director, indexer, production editor, proofreader)
against that fact base. `docs/production-ledger.md` is the append-only
record of every ruling, and `docs/briefs/reports/` holds every desk's
findings. The press defects the production turned up are filed on the
press issue tracker and listed in the ledger.
