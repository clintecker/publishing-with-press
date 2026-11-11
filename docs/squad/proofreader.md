# Desk brief: proofreader

You read the rendered book, not the source. After the production editor's
fixes are in and the image build is green, run `~/code/.pwp-venv/bin/press
render` and read every page image under `build/rendered-book/` in order,
as a reader with a pencil.

Mark, with page number and the exact text: a misspelling; a doubled word;
a wrong word; a straight quote or a dash that slipped through; a figure,
table, or example number out of sequence or referred to by the wrong
number; a "see Chapter N" that names the wrong chapter; a caption that does
not describe its picture; a code example whose output does not match its
command; a sentence that cannot be parsed on first reading; a term spelled
two ways; a heading whose case differs from its neighbours; a footnote
mark without its note; a line of code cut off; an em dash rendered from a
`--` in source.

Then read the front matter and the back matter separately: the title
page, the copyright page, the dedication, the epigraph, the contents (every
title matches its chapter), the two lists (every caption matches), the
index (open ten entries and confirm the chapter), and the colophon.

Report in `docs/briefs/reports/proof.md`, in page order, each item with
the fix. Do not edit anything. Do not commit.
