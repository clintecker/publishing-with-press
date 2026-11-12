# Typesetter report: Appendix B (b-configuration-reference.md)

Builds: `press check` passed (23 files, jargon check clean). `press pdf`
completed once 23 placeholder PNGs (other chapters' figures, missing at
build time) were supplied; they were deleted afterward. Appendix B is
PDF pages 325-338 (printed 316-329). Source has no figures, no
footnotes, no tips/warnings/sidebars; 3 examples (B.1-B.3, all fenced
`text`, all lines at most 64 columns, no trailing whitespace), 1 table
(B.1, caption form correct), index comment present and last.

## Findings

1. Quote: running head "16 Inside the press" and section numbers
   "16.62 config/metadata.yaml", "16.62.1 Identity", ... "16.70 Fields
   kept outside these files". Rule: appendix is `{.unnumbered}`; markup
   guide says appendixes carry no chapter numbers. Severity: should (a
   press layout issue, not fixable in the file; same for Appendix A,
   "16.14 press all"). The `##` and `###` heads of the unnumbered
   appendix inherit chapter 16's counter and continue it. Fix: press
   or house-template change (unnumbered appendix should suppress
   section numbering and reset the running head), or tell the author
   to accept; do not type numbers.
2. Quote: "title Type str, required. The book's title..." Rule: definition
   list with key in bold constant width. Severity: should. In the PDF
   the term runs inline with its definition (bold key, then "Type str"
   on the same line) with no space between entries, so the 50-odd entries
   set as a dense wall, hard to scan. Fix: house template (term on its
   own line or a small gap between entries); markup cannot change it.
3. Quote: "styles.<id>.prompt ... author, and imprint and forbids other
   words" (top of printed p.328, entry begins on 327). Rule: no page
   break inside an entry. Severity: should. Entry split across a page;
   others fall cleanly. Not fixable in the source short of reflow.
4. Quote: contents list. The `##` sections (config/metadata.yaml, etc.)
   do not appear in the contents; only "Appendix B: Configuration
   reference ... 316". Severity: should (toc-depth 1 is the house
   setting; sections reachable only by the PDF outline). Fix: none in
   file.

No heading at a page foot, no table wider than the measure, no code line
wrapped, no box over a page, no caption parted from its fence (Example
B.1 caption and fence sit together on printed p.318).

Counts: blocks 0, should 4.
