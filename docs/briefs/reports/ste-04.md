# STE80 editor report: book/chapters/04-writing-the-manuscript.md

Mode: Humanize for body prose, admonitions, table cells, and footnotes.
Light for the sidebar "A stray asterisk and Fig-ure" (no change: no
sentence over 30 words, none with three ideas, no semicolon). Never for
fences, code spans, quotations, headings, and art comments.

## Ratchet count

- Baseline (`tools/ste-baseline.json`): 8
- Before: 8
- After: 5

`press check` passes (source, checker self-test, editorial, jargon), and
`python3 tools/ste-ratchet.py` exits 0. The three sentinels are intact
(each still occurs once in the book). Every index term in the file keeps
its occurrences ("inline code" and "sentinel" each gain one, none loses
one). No semicolon or dash was added to prose.

## Edits (20 sentence edits; line numbers are in the edited file)

| Line | Rule | Old | New |
|---|---|---|---|
| 18 | S1 (three ideas) | The Alice book, which `alice` keeps on the workstation `hatter`, is the whole novel, and it sets these constructs the same way. | The Alice book, which `alice` keeps on the workstation `hatter`, is the whole novel. It sets these constructs the same way. |
| 44 | S1, S2 (30 words, three ideas) | Because pandoc turns hyphens into dashes, a sentence with two hyphens in it comes out with a dash in it, and the house does not set dashes in prose. | Because pandoc turns hyphens into dashes, a sentence with two hyphens in it comes out with a dash in it. The house does not set dashes in prose. |
| 46 | S1 | The Manuscript edition (the stitched Markdown) is the raw manuscript, stitched together from your chapter files, and no filter runs on it. | The Manuscript edition (the stitched Markdown) is the raw manuscript, stitched together from your chapter files. No filter runs on it. |
| 50-52 | S13 (real lead: 7 sentences), split at the turn from the callouts to who sets what | (one paragraph of 7 sentences) | Paragraph 1 ends at "(9) a footnote." Paragraph 2 starts "An opening page carries no running head". |
| 52 | S1, S2 (28 words) | The house sets the running head and the folio with no markup from you (Chapter 9, *The house design*, describes both), and the drop cap comes from configuration. | The house sets the running head and the folio with no markup from you (Chapter 9, *The house design*, describes both). The drop cap comes from configuration. |
| 89 | S1 (three ideas, 27 words) | In the first heading, the candidates are at least Rabbit, Sends, Little, and Bill, and every one of them starts with a capital, so the checker refuses it. | In the first heading, the candidates are at least Rabbit, Sends, Little, and Bill. Every one of them starts with a capital, so the checker refuses it. |
| 89-91 | S13 (the S1 split made 7 sentences), split at the turn to short headings | (one paragraph) | New paragraph starts "A short heading can pass the test in title case." |
| 94 | S1 (Tip) | Press keeps the title word for word, so a title-case title becomes a title-case heading, and the next `press check` refuses it. | Press keeps the title word for word, so a title-case title becomes a title-case heading. The next `press check` refuses it. |
| 99-101 | S13 (real lead: 7 sentences), S1 | Press numbers figures and lets you cite them by name, but it has no machinery for citing chapters or sections. [...] For a chapter or a section, write the reference in words: "see Chapter 6, *Checking the manuscript*". Chapter 5, *Figures, plates, and illustrations*, covers figure identifiers in full. | Press numbers figures and lets you cite them by name. [...figure sentences unchanged...] Chapter 5, *Figures, plates, and illustrations*, covers figure identifiers in full. / (new paragraph) Press has no machinery for citing chapters or sections. Write such a reference in words: "see Chapter 6, *Checking the manuscript*". |
| 159 | S1, S2 (27 words) | A book can list extra directories for the checker under `audit-dirs` in *config/house-rules.yaml*, and the files there get a lighter battery than the manuscript. | A book can list extra directories for the checker under `audit-dirs` in *config/house-rules.yaml*. The files there get a lighter battery than the manuscript. |
| 192 | S1, S2 (26 words) | The book's own epigraph, [...] in *config/front-matter.yaml* instead, and Chapter 10 describes it. | The book's own epigraph, [...] in *config/front-matter.yaml* instead. Chapter 10 describes it. |
| 203 | S3 (condition first) | Use a plain line block when the breaks matter and the shape does not, as in a postal address inside a letter. | When the breaks matter and the shape does not, use a plain line block, as in a postal address inside a letter. |
| 209 | S1 (three ideas, 27 words) | A claim in *config/authorities.yaml* is an exact fragment of your manuscript, so if you reword its sentence, the claim no longer matches and press refuses the build. | A claim in *config/authorities.yaml* is an exact fragment of your manuscript. If you reword its sentence, the claim no longer matches and press refuses the build. |
| 209-211 | S1, S2 (28 words), S13 (the splits made 8 sentences; split at the turn from index and authorities to sentinels; "Chapter 10 covers the index and the authorities." moved up to close the first paragraph) | A *sentinel* is a phrase in `verify-sentinels` in *config/metadata.yaml* that the verifiers look for in each finished edition, and it must survive every revision word for word. | (new paragraph) A *sentinel* is a phrase in `verify-sentinels` in *config/metadata.yaml* that the verifiers look for in each finished edition. A sentinel must survive every revision word for word. |
| 215 | S1 (three clauses, 25 words) | Each row is a line, a vertical bar separates the cells, and a row of hyphens under the first row marks it as the header. | Each row is a line, and a vertical bar separates the cells. A row of hyphens under the first row marks it as the header. |
| 242 | S10 (phrasal verb) | ...so the problem shows up only when you build the print pack. | ...so the problem appears only when you build the print pack. |
| 250 | S11 (unclear "it" after a sentence about banned patterns) | Pandoc's smart typography leaves it alone, so `--front` in backticks keeps its two hyphens. | Pandoc's smart typography leaves inline code alone, so `--front` in backticks keeps its two hyphens. |
| 298 | S1 (three ideas) | The *chapter-dropcap.lua* filter finds the first eligible paragraph after each `#` heading, and it skips any chapter marked `{.unnumbered}`, so a preface opens with a plain paragraph. | The *chapter-dropcap.lua* filter finds the first eligible paragraph after each `#` heading. It skips any chapter marked `{.unnumbered}`, so a preface opens with a plain paragraph. |
| 320 | S8 (action in the verb) | ...and the *scene-break.lua* filter does the drawing. | ...and the *scene-break.lua* filter draws it. |
| 394 | S1, S2 (27 words) | In the PDF it starts at body size and ends at the smallest size LaTeX offers, and on the reader site it shrinks from 1em to .68em. | In the PDF it starts at body size and ends at the smallest size LaTeX offers. On the reader site it shrinks from 1em to .68em. |
| 420 | S2 (real lead: 31 words), S1 | After an honorific, it ties the honorific to a following capitalized word, for Mr., [...], and Fr. After a reference form, it ties the form to a following digit, for forms such as p., [...], and Eq. | After an honorific, it ties the honorific to a following capitalized word. The honorifics are Mr., [...], and Fr. After a reference form, it ties the form to a following digit. The reference forms include p., [...], and Eq. (both lists verbatim) |
| 424 | S1 (triad of clauses) | The manuscript stays plain prose, the house does the fine work, and the filter leaves ordinary sentences exactly as you typed them, every period included. | The manuscript stays plain prose, and the house does the fine work. The filter leaves ordinary sentences exactly as you typed them, every period included. |
| 424 | S2 (27 words) | You type "Rev. Dodgson" and "p. 42" with ordinary spaces, and the filter keeps each pair on one line in the PDF, the EPUB, and the reader site alike. | You type "Rev. Dodgson" and "p. 42" with ordinary spaces. The filter keeps each pair on one line in the PDF, the EPUB, and the reader site alike. |
| 426 | S1 (three ideas) | The *figure-numbering.lua* filter numbers each figure once, by chapter, and turns every `@fig:` citation into "Figure 4.1" with a link, so press needs no pandoc-crossref. | The *figure-numbering.lua* filter numbers each figure once, by chapter, and turns every `@fig:` citation into "Figure 4.1" with a link. Press therefore needs no pandoc-crossref. |

## Leads declined

- Line 18, passive 'is Markdown': a false lead. "is plain Markdown" is a
  copula with a noun, not a passive.
- Line 248, progressive 'is trailing': a false lead. "The exception is
  trailing whitespace" uses "trailing" as an adjective.
- Line 312, sentence-length 44: a counter artifact. The counter does not
  split after a footnote marker (`it.[^4-hung-quote] On`), so it joins two
  sentences of 21 and 23 words. Each holds one idea. Moving the marker or
  adding "In the PDF" to the second sentence would change what the note
  attaches to or add a fact.
- Line 428, paragraph-length 12: the sidebar, which is Light mode. The
  counter reads the whole blockquote as one paragraph. It is three
  paragraphs of 5, 2, and 4 sentences, about 150 words in all, under the
  190-word law, with no sentence over 30 words and no semicolon.
- Line 431, phrasal verb 'look at': in the sidebar (Light mode, voice).
  "The author could only look at the proof and wonder" loses its tone as
  "examine the proof".

## Passives kept

- Line 22, "a list of extensions, each switched on with a plus sign": the
  plus sign is the means, not an actor, and "you" is already the subject.
- Line 238, "An untagged fence is set verbatim": the paragraph does not say
  which part (the house header or pandoc's LaTeX writer) sets it, so
  naming an actor would add a fact.
- Line 298, "any chapter marked `{.unnumbered}`": the author marks it, and
  the actor does not matter to the sentence.
