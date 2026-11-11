# Report: Chapter 4, Writing the manuscript

File: `book/chapters/04-writing-the-manuscript.md`

## Status

DONE_WITH_CONCERNS (concerns are small; listed below).

## Word count

`press wordcount`: 5,718 (target 6,000; inside 15 percent). Prose-only
estimate (code, tables, comments stripped): about 4,450 words in about
270 sentences, average about 16.3 words. The rest is examples, tables,
captions, and art directives.

## Gates

- `press check`: no finding names this file. The run still fails on
  paragraph-length errors in 01, 02, and 03 (other writers' files; rerun
  once, same result).
- Paragraphs: the three figure `art:` comments plus their image lines
  count as one paragraph each to the checker; first drafts of the
  directives tripped the 190-word law and were cut to fit (about 110 to
  130 words each). The same failure is what currently breaks 01 to 03.
- Plate: the two plate lines are byte-identical to the stub, moved to the
  end of "Headings and chapters".
- Note: at the time I finished, HEAD (`d3a3c72` or an earlier commit by
  another hand) already contained an intermediate version of this file.
  I did not commit; the working tree holds the final version.

## Figures

- 4.1 `@fig:page-anatomy` (page anatomy): one 6 by 9 page in outline with
  eight numbered margin circles (running head, folio, chapter title,
  section heading, body text, footnote, blockquote box, numbered figure
  and caption); key given in the prose.
- 4.2 `@fig:set-pieces` (before/after, three frames): the same four lines
  of "Alice's Right Foot, Esq." as cascade (stepped), verse (one indented
  edge), and tail (S-curve, shrinking type), labelled (a) to (c) beneath.
- 4.3 `@fig:scene-break-ornaments` (matrix): rows rule, asterism,
  fairy-dust by columns PDF, Reader; only the rule differs (diamond
  between tapering hairlines on the reader).

Tables 4.1 to 4.5, Examples 4.1 to 4.9, one sidebar (war story 22),
three warnings, three tips, three footnotes. Every numbered item is
referred to before it appears.

## Facts I needed and left out

- The checker's exact message for em dash, en dash, and curly quotes in
  prose (the known-bad output suggests the glyph message fires for
  dashes, but the fact file does not say); I named no message.
- Whether prose rules skip inline code spans (only fenced code is
  stated); I made no claim.
- The 21 small words of the title-case test; the example is built to
  hold whether or not "In" is on the list.
- The `config set` dotted-key form `chapter-opening.style` comes from the
  key listing in facts-03/B, not from a captured session.
- Which chapter covers sentinels: I pointed to Chapter 8, *Verifying the
  artifacts*; the fact file says "§3.3 and §6" of the fact base. Please
  check against the final 03 and 08.
- `raised-cap` left out (renders as `drop-cap`, listed as bug B7). The
  txt/docx lack of drop caps and scene-break ornaments, and the Markdown
  edition's raw `:::` source, left out (B9, B10).

## Contradictions

- The glyph law range U+00C0 to U+017F includes the multiplication and
  division signs (the fact file says so); `docs/markup.md` lists the
  multiplication sign as forbidden. The chapter states the press law.
- `typographic-spacing.lua` ties after the section sign and the pilcrow,
  but the glyph law forbids both in book prose. I listed only the
  typable reference forms.
- `docs/markup.md` puts the `art:` comment before the image line; the
  fact file (4.2) describes it after the image. I followed markup.md.

## ste_check residuals (36 findings), with defence

- sentence-length over 25: tables, the In-this-chapter list, art
  comments, abbreviation lists (Mr., Dr., p.), and sentences the tool
  fuses across a colon before a code block or across a footnote marker.
  By my own count no prose sentence exceeds 30 words except where those
  fusions occur.
- semicolon: in the plate and figure `art:` comments, in the quoted
  checker message `(the law is under 190; split it)` inside a code span,
  and in the index comment. None in prose.
- passive "is Markdown", progressive "is trailing": false positives
  (copula plus noun; "trailing whitespace").
- `-ing` forms: headings and chapter titles (Checking, Verifying,
  Writing, Referring) and the term "trailing whitespace".
- "therefore" (allowed by the prose contract), "identical" (art comment),
  phrasal verb "look at" (sidebar, "look at the proof").
- paragraph-length over 6 sentences: the art comments only.
