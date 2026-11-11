# Continuity report: Chapter 3, *The shape of a book repository*

Desk: continuity editor. Chapter read: `book/chapters/03-the-shape-of-a-book.md`
(working tree, after its desks and the second re-review). Cross-checked
against Chapters 2 and 4 (committed, final), the drafts of Chapters 1, 6, 7,
8, 9, 10, and 12 where they share facts with Chapter 3 or make promises
about it, `docs/vocabulary.md`, `docs/design.md` section 5, and
`docs/production-ledger.md`. The chapter was not edited.

Status: **PASS; the chapter itself is clean.** Its cross-references, numbering,
and markup are clean, and it keeps every promise earlier chapters make about
it. The three blocking findings are in other chapters that contradict facts
Chapter 3 defines: the sample book's sentinels (Chapter 6), its description
(Chapter 1), and Chapter 3's own title (Chapter 10). Chapter 3 has one should
and four mays of its own. Two more findings (one should, one may) belong to
Chapters 6, 10, and 12.

The bible (`docs/continuity.md`) now holds 37 new entries: 7 terms, 12
shared facts, 17 cross-references and promises, and 1 numbering row. Another
19 existing entries citing Chapter 3 are confirmed or corrected (4 terms, 12
shared facts, 3 ledger line numbers). Several facts this pass would have added
were already logged by the Chapter 1 pass, which ran at the same time; those
rows were confirmed, not duplicated.

Chapter 3 is the defining chapter for the sample book's config, so where a
later or earlier draft disagrees with it, the fix goes to the other chapter.

## Findings

### 1. Chapter 6 gives the Alice book different sentinels (blocks; fix in Ch. 6)

Quote, Ch. 3 l.222: "For Alice we will use two lines of verse from the middle
of their chapters, "Twinkle, twinkle, little bat" and "she made some tarts"."
Ch. 3 l.243 sets exactly those two with `press config set ... --json`, and
Ch. 8 l.109 to 111 repeats them ("the two sentinels that Chapter 3 set with
`press config set`", l.106), as does Figure 8.3 (l.485, 487).

Quote, Ch. 6 l.365 to 372: "Example 6.10 shows the sentinels of the Alice book,
two clauses from the middles of Carroll's sixth and seventh chapters." The
example lists `"We're all mad here."` and `"Why is a raven like a
writing-desk?"`.

Rule: shared fact (the sample book's sentinels). Severity: blocks.

Fix (Ch. 6): replace the two entries in Example 6.10 with
`"Twinkle, twinkle, little bat"` and `"she made some tarts"`, and the lead-in
with "two lines of verse from the middles of Carroll's seventh and eleventh
chapters". (The bat verse is in chapter VII, the Mad Tea-Party; the tarts
verse is read out in chapter XI, Who Stole the Tarts?, not at its start.)
Keep `verify-min-pages: 24`, which agrees.

### 2. Chapter 10 cites Chapter 3 by a wrong title (blocks; fix in Ch. 10)

Quote, Ch. 10 l.171: "The landing page reads the same field and stacks the
clauses as well, as Chapter 3, *The shape of a book*, mentions."

Rule: cross-reference title against design.md section 5. Severity: blocks.

Fix (Ch. 10): "as Chapter 3, *The shape of a book repository*, mentions." The
promise itself is kept (Table 3.3, l.185, the `subtitle` row).

### 3. Chapter 1 gives the Alice book a different description (blocks; fix in Ch. 1)

Quote, Ch. 3 l.331 to 332, Example 3.5: `press config set description "A girl
follows a rabbit underground and argues with all."`

Quote, Ch. 1 l.137, Example 1.1: `press config set description "A girl falls
into Wonderland."`

Rule: shared fact (the sample book's metadata values). Both chapters set
the same field of the same book on its first day (Ch. 6 l.56 says it was
set "on its first day"). Severity: blocks.

Fix (Ch. 1, whose pass is running now): use Ch. 3's string in Example 1.1.
Related, for the Ch. 1 pass only: Ch. 1 runs `press new alice` with no
`--owner`, so its scaffold keeps `repository` and `site-url` commented out
(Ch. 3 Table 3.1), and with no `--author`, so the byline comes from
`git config user.name`. Example 1.1 then sets the author with `press config
set`, so the two chapters reach the same author. If the tour later pushes to
`wonderland-press` or relies on `site-url`, it needs the `--owner` flag or a
`press config set site-url`.

### 4. "the typed model" in Chapters 6 and 10 for Chapter 3's *book model* (should; fix in Ch. 6, 10)

Quote, Ch. 3 l.126: "The press reads the file through its *book model*, the
typed set of rules it holds for every field." Ch. 6 l.388: "The typed model's
default is 40". Ch. 10 l.101: "the typed model checks each value".

Rule: one name for one thing. Severity: should.

Fix: "the book model" in Ch. 6 l.388 and Ch. 10 l.101, and add `book model`
to `docs/vocabulary.md` (never "the typed model", "the schema"). Design.md's
Ch. 16 row says "the typed book model", which agrees.

### 5. Two names for the press's gallery example inside Chapter 3 (should)

Quote, l.500: "the press's own gallery example, a three-chapter Alice with one
appendix"; Example 3.10 caption, l.502: "press all on the gallery Alice, in
part".

Rule: a thing called by two names in this chapter; the cast ruling calls it
"the press's own Alice example" or "the Alice example" (Ch. 6 l.408, Ch. 8
Example 8.1). Severity: should.

Fix: l.500 "the press's own Alice example, three chapters and one appendix";
caption "press all on the press's own Alice example, in part".

### 6. "page floor" used in Chapter 3 without its definition (may)

Quote, l.228: "The page floor is the second knob."

Rule: per-chapter italic first use. Ch. 6 l.386 and Ch. 8 l.63 define *page
floor*; Ch. 3 is the first chapter to rely on the term. Severity: may.

Fix: "The *page floor*, the fewest pages the PDF may have, is the second
knob."

### 7. Example 3.3 cuts the word it is quoted for (may)

Quote, l.230: "It refuses draft knobs as *vacuous witnesses*". Example 3.3's
first line ends "and its witnesses ...", so the word "vacuous" is cut from the
quoted message. Vocabulary: quote *vacuous witnesses* "only where press's
message is quoted". Ch. 8 l.82 says Chapter 3 "calls these vacuous witnesses
and shows the refusal". Severity: may.

Fix: fold the first line instead of cutting it, as Ch. 6 Example 6.11 does
("this is a release build (PRESS_RELEASE=1) and its witnesses" / "    are
vacuous:").

### 8. `top-level-division` stated for every edition (may)

Quote, l.406: "It sets pandoc's `top-level-division` to `chapter`, so every
level-one heading (`#`) in the manuscript starts a chapter".

Rule: shared fact (pandoc dialect): `top-level-division: chapter` is in the
pdf, epub, and print defaults only (continuity-04, finding 5, against Ch. 4
l.50). The conclusion holds in every edition; the stated mechanism does not.
Severity: may.

Fix: "In the PDF and the EPUB it sets pandoc's `top-level-division` to
`chapter`, and in every edition a level-one heading starts a chapter."

### 9. "cross-repo token" (may)

Quote, l.491: "a private book needs no cross-repo token."

Rule: vocabulary, "repo (in prose)". It is not the book repository, and the
phrase is the press's own (its *CLAUDE.md*). Severity: may.

Fix: "cross-repository token", or leave it as the press's phrase.

### 10. Chapter 12's "Alice example" is neither Alice (may; fix in Ch. 12)

Quote, Ch. 12 l.111: "that page for the Alice example on the house provider:
a 6 by 9 perfect-bound book of 200 pages on cream stock" (also l.218).

Rule: cast ruling. The press's Alice example has 23 pages, and Ch. 3 Example
3.5 sets the sample book to `print.paper white`. Severity: may.

Fix (Ch. 12): call it a hypothetical ("a 6 by 9 perfect-bound book of 200
pages on cream stock, such as the full Alice novel would be on cream"), or
drop "the Alice example".

## Facts logged as shared (Chapter 3 defines them)

- The sample book's sentinels: "Twinkle, twinkle, little bat" and "she made some
  tarts" (3, 8; Ch. 6 conflicts, finding 1).
- The page floor: model default 40, template 1, release minimum 24; the sample book
  sets 24 once its chapters exist (1, 3, 6, 8: all agree).
- The release witnesses and their refusal under `PRESS_RELEASE=1`, set by CI on a
  tag starting with `v` (1, 3, 6, 8: agree).
- Sentinel matching: exact case, with curly and straight quotes treated as equal (3, 6, 8).
- The scaffold's metadata values, and the sample book's values after setup. Ch. 10's
  later `copyright`, `publisher` ("Wonderland Press"), `publisher-place` ("Oxford"),
  and double subtitle follow on from Ch. 3 without contradicting it. Ch. 1's
  description conflicts (finding 3).
- Required keys: the model needs `title`, `author`, and `slug`; with front matter it
  also needs `copyright`, `publisher`, and `publisher-place`; the checker also
  requires `description` (3, 6 l.56, 10 l.126: agree).
- Print defaults (`house-6x9`, `house`, `perfect-bound`, `paperback`, model
  paper `cream`; the house chapter opening is `none`, lines 3), and the year from
  the date (EPUB date, RSC-005, roman numerals), are also logged as shared.
- Other facts logged as shared: the self-test count of 19, the wordcount rules,
  `press render` at 160 dpi, the Telegraphic edition at 80 columns, the Pages
  setting and the "Initialize containers" rerun, the Makefile, and `BOOK_ROOT`.
  Ch. 7 l.150 says the press sets `BOOK_ROOT` for its subprocesses, which is
  compatible with Ch. 3 l.110.

## Provisional entries confirmed

Every bible entry that cited Chapter 3 from the Chapter 2 and Chapter 4
passes was checked against the chapter as it stands:

- Confirmed: the terms *chapter file*, *appendix file*, and *sentinel*. Also
  confirmed: install channel, editable install, toolchain image identity (public;
  pulled with no secret), image pin, missing local epubcheck, how CI installs
  press, who a book's CI calls, `press all` and the print pack, release and tags,
  paragraph law, glyph law, dash and quote law, sentinel placement (now l.225),
  chapter-opening settings, discovery and sorting, and `press add chapter`.
- Resolved, no longer violated by Ch. 3: the fence tag (all 17 fences are `text`);
  the image, blank line, and art comment (l.76 to 78, 394 to 396, 609 to 611);
  code line width (no fenced line over 64 columns).
- Line numbers updated in the ledger: 3 (l.449) is now l.484, 3 (l.465) is
  now l.500, and 3 (l.605) is now l.641. All three are kept.

## Promises checked

Promises made about Chapter 3, all kept: Ch. 1 l.142 (the scaffold file by
file), Ch. 2 l.299, 361, 389, Ch. 4 l.30, Ch. 7 l.232 (the identity fields:
Table 3.3), Ch. 8 l.82 (vacuous witnesses and the refusal: Example 3.3) and
l.106 (the sentinels set with `press config set`: l.243), Ch. 9 l.135 (a book
names its profile in its metadata: Table 3.5), and Ch. 10 l.171 (the stacked
subtitle on the landing page: Table 3.3, but wrong title, finding 2).

Promises Chapter 3 makes: Ch. 6 (four passes, known-bad fixtures), Ch. 8,
Ch. 9 (aesthetic, profiles, chapter openings), Ch. 10 (front matter, index
terms, authorities), Ch. 11 (commissions), and Ch. 12 (print fields, direct
print ordering, publish checklists): kept in draft. Ch. 13, 14, 15, and 16
are stubs: open. The three "later in this chapter" references (l.70, 106,
128) all point later.

## Numbering

Figures 3.1 `03-01-scaffold-tree`, 3.2 `03-02-how-files-sort`, 3.3
`03-03-dist-after-all`: no gap, no repeat, slugs match `CC-NN-slug`, every
`@fig:` (l.74, 390, 607, 615) has its figure, order matches design.md.
Tables 3.1 to 3.6 and Examples 3.1 to 3.12, no gap. Five short uncaptioned
fences (l.23, 242, 274, 412, 543), none referred to by number.
