# Continuity report: Chapter 8, *Verifying the artifacts*

Desk: continuity editor. Chapter read as it stands after its desks and two
re-review rounds (519 lines). Cross-checked against Chapters 1, 2, 4 (final),
3, 6, 7 (final revision), the later drafts that make promises to Chapter 8
(10, 12, 13), the press source (`verify_formats.py`, `package_source.py`,
`build.py`, `doctor.py`), `docs/vocabulary.md`, and `docs/design.md`
section 5.

Status: **PASS WITH FIXES.** No blocks in Chapter 8; two should, five may.
One block raised against Chapter 7 (finding 3). The chapter obeys the
edition names throughout, keeps every promise made to it (Chapters 2, 3, 4,
6, 7, 10, 12, 13), and its numbering is clean: Figures 8.1 to 8.3
(`08-01-what-each-verifier-inspects`, `08-02-rebuild-edges`,
`08-03-verify-run`) each cited before it appears, Tables 8.1 to 8.7, Examples
8.1 to 8.3, no gap, no repeat. Every fence is tagged `text`, none exceeds 64
columns, and every image is followed by one blank line and its `art:`
comment. It does not fully obey the two Alices ruling (finding 1).

The witnesses and the no-stale law agree across Chapters 3, 6, 7, and 8 on
every value (two sentinels and a floor of 24 under `PRESS_RELEASE=1`;
sentinels exact-case with straight and curly quotes equal; four places a
sentinel is checked; `INV-graph-no-stale`, critical, CLI path only; what each
verify target builds; `press all` verifier order pages, pdf, formats,
archives; `7 editions agree on all 4 chapter witnesses`), with the one
exception in finding 3.

## Findings

### 1. "The Alice example" names the sample novel (should)

Quotes: l.17 "The examples come from the Alice example, which user `alice`
builds on the workstation `hatter` and which CI builds on the host
`printshop`. The real runs in Examples 8.1 and 8.2 come from the press's own
three-chapter Alice example." l.106 "The Alice example, the full novel in
user `alice`'s repository". l.206 "The Alice example itself, the full novel,
sets its floor at 24". Also l.35, the Table 8.1 caption (l.49), l.82.

Rule: the two Alices ruling (bible, fixed cast). "The Alice example" is
reserved for the press's gallery example (`examples/alice-in-wonderland/`);
the book's sample is the whole novel, kept by `alice` on `hatter`. Here one
name covers both, and l.17 sets them side by side. Same fault as Ch. 4
(continuity-04, finding 2).

Fix: call the novel "the Alice book" (Chapter 6's word, l.365, l.388) at
l.17, 35, 49, 82, 106, 206; keep "the press's own three-chapter Alice
example" for the captures (l.17, 194, 274, 427). l.206 then reads "The
Alice book itself, the full novel, sets its floor at 24".

### 2. *dist/pages* is "the Pages site" here, "the page bundle" in Ch. 7 (should)

Quotes: l.363 "The `press pages` target builds the Pages site, the public Web
site of the book, in *dist/pages*." Also l.29, 442, 445.

Rule: one thing, one name. Chapter 7 l.316 separates the two: "The Pages
site is the Web site that GitHub Pages serves from the page bundle." Chapters
1 (l.170, 275) and 3 (l.533) say "the Pages bundle"; Chapter 7 says "the page
bundle". The vocabulary has no row.

Fix: ruling needed. Recommend "the Pages bundle" for *dist/pages/* (Ch. 1, 3)
and "the Pages site" for what GitHub Pages serves (Ch. 7). Chapter 8 then
reads "builds the Pages bundle, the public Web site of the book, in
*dist/pages*" at l.363 and "the Pages bundle" at l.29, 442, 445; l.45 ("the
site that the Pages deploy publishes") already fits. Chapter 7 changes "page
bundle" to "Pages bundle". Add the row to `docs/vocabulary.md`.

### 3. Chapter 7 states the no-stale law without its exception (blocks, against Ch. 7)

Quote, Ch. 7 l.339: "Every verify target rebuilds the artifacts it verifies
before it verifies them." No exception follows in l.339 to 357.

Rule: shared fact (the no-stale law). Chapter 6 l.473 and Chapter 8 l.433
and l.439 both state that `press verify-formats` reads an existing
*dist/alice.pdf* into the agreement check without rebuilding it; Chapter 8
l.210 says that check covers "the Print edition included". The source
agrees (`verify_formats.py` l.274: the PDF joins when the file exists and
`pdftotext` is present). Chapter 7 contradicts both.

Fix (Ch. 7, after l.339): "The one exception is `press verify-formats`: when
`pdftotext` is present, it reads whatever *dist/alice.pdf* exists into its
cross-edition agreement check without rebuilding it. Chapter 8 shows the
edge." Chapter 8 needs no change.

### 4. "vacuous witnesses" used outside the press's message (may)

Quote, l.82: "Chapter 3, *The shape of a book repository*, calls these
vacuous witnesses and shows the refusal."

Rule: vocabulary, `vacuous witnesses`: "quote it only where press's message
is quoted".

Fix: "Chapter 3, *The shape of a book repository*, shows the refusal, which
calls such settings vacuous."

### 5. The vocabulary's "witness" is narrower than Chapter 8 (may; fix the vocabulary)

Quotes: l.400 "The press calls them all witnesses"; Table 8.6 lists
sentinels, title, manuscript witness, chapter witnesses, page floor; l.214
"The three witnesses" (title, sentinels, manuscript witness). Example 8.1,
press's own line: "2 sentinel(s) plus the title as witnesses".

Rule: `docs/vocabulary.md` defines witness as "the manuscript or chapter
witness line". Chapter 8 follows press's own usage, as do Chapters 3 and 6
("release witnesses" = sentinels plus floor). No chapter is wrong; the
vocabulary is.

Fix: change the row to "witness: any evidence a verifier requires of an
artifact (sentinel, title, manuscript witness, chapter witness, page floor);
the manuscript witness and chapter witness are the lines press chooses".

### 6. Example 8.3 opens without its prompt line (may)

Quote, l.470: "press doctor" as the first line of the capture.

Rule: example conventions (`$` then what you type). The line is the
doctor's own header (`doctor.py` l.273); Chapter 2's Figure 2.2 shows
`$ press doctor` above it. Here a reader can take it for a command typed
without a prompt.

Fix: add `$ press doctor` as the first line of Example 8.3.

### 7. *commerce* and "print ordering" (may)

Quote, l.382: "*commerce*, the optional ordering of printed copies from the
book's site".

Rule: one thing, one name across chapters. Chapters 3, 7 (l.426), and 12
(l.186, "Ordering a copy") call the feature "print ordering" and keep
"commerce" for the gate. Chapter 8 defines the feature as *commerce*.

Fix: "The third group concerns *print ordering*, the optional ordering of
printed copies from the book's site, which Chapter 12 describes. A call to
buy must appear exactly when the book enables print ordering".

## Promises kept (incoming)

2 (l.381) reading a failure; 3 (l.535) the verifiers; 4 (l.204) sentinels
proved in the editions; 6 (l.357) both settings proved; 6 (l.473) the edges
target by target (l.433 to 439, Figure 8.2); 7 (l.357) what each verifier
inspects; 7 (l.422) what a missing epubcheck costs (l.310 to 320); 7 (l.513)
opens the artifacts; 10 (l.410) the archive verifier (l.355 to 359); 12
(l.178, 298) the print verifier in full (l.158 to 177); 13 (l.254) the EPUB
identifier check, kept in substance (Table 8.3, l.257; the `urn:isbn:` form
is not named). Bible items due 8: the epubcheck scar (l.323) and
`pdfimages` (l.188, tip l.191), both kept.

## Cross-references out (all correct)

1 *Introduction* (l.25), Example 1.2 (l.447); 3 *The shape of a book
repository* (l.82, 106); 2 *Installing press* (l.465); 4 *Writing the
manuscript* (l.491); 6 *Checking the manuscript* (l.412); 9 *The house
design* (l.509, next chapter); 10 *Front matter, the index, and the table of
authorities* (l.357); 12 *The print pack* (l.31, 177, 382). "Later in this
chapter": l.27 to l.179, l.210 to l.325, l.274 to l.398, all later.
"Earlier": l.412 to l.57. l.459 "the previous section" is the no-stale law,
which gives the order at l.445.
