# Fact check: Chapter 3, The shape of a book repository

I checked `book/chapters/03-the-shape-of-a-book.md` against `docs/briefs/facts/facts-03.md`. That covers sections 3.1 to 3.5 and 17.3, the Shared context (1.4, 19, 20), and the managing editor's supplement (S1 to S3). Line numbers refer to the chapter.

**Code blocks.** I compared each code block with `diff` against the fact file, after changing `demo` to `alice`.

- These match byte for byte: Example 3.2 (preface), 3.6 (`press config validate`), 3.8 (Makefile, recipe line tab-indented in both files), 3.9 (requirements.txt), 3.12 (book.yml), the wordcount capture, and the two `glob` lines.
- Example 3.1 matches, with `/…/` set as `/.../` (allowed elision).
- Example 3.10 matches. Its `...` stands for the two `note:` lines.
- Example 3.3 matches the template through `#   retail: false`. Its `author`, `publisher`, `repository`, and `site-url` lines were reconstructed from the substitution rules. They now agree with the verbatim lines in S1.
- Example 3.4 fills in the template's `N` with 0 and 1. The fact file gives that message as a template, not a capture, so this is acceptable for a hypothetical. See Drifted 9.
- Example 3.7 is a reconstruction, and S1 contradicts it. See Contradicted 1.

## 1. Unsupported

1. **Optional files degrade gracefully.** Line 122: "each consumer of an optional file builds without it." I searched for degrade, graceful, and optional, and found nothing. The fact file lists the files (17.3, "Other book files") but never says that every consumer works without them. Fix: cut the clause, or soften it to the file's own terms: "Each is optional."
2. **Why the scaffold fills the front-matter fields.** Line 213: "The scaffold fills `copyright`, `publisher`, and `publisher-place` for that reason." The file gives the facts but not the motive: the three fields are "Required with front matter", and front-matter.yaml's "PRESENCE turns on generated front matter". Fix: "The scaffold fills `copyright`, `publisher`, and `publisher-place`, which the model requires once front matter is on."
3. **Why quotes are equated.** Line 233: "because pandoc curls the quotes you type." The file says only "curly and straight quotes are equated". Fix: cut the "because" clause.
4. **The six lines of `press config validate`.** Line 322: "It checks every config file the book has against its model and prints one line per file. Example 3.6 shows its output for a book that has all six." The capture is a bare six-line output. The file never says that the book had all six files, or whether `validate` prints a line for a file that is absent. A fresh scaffold has only three of them. Fix: "Example 3.6 shows its output", and drop "every config file the book has" and "for a book that has all six". For the model claim, see Contradicted 3.
5. **The sidebar's privacy and secrets.** Line 456: "A book repository is often private while its author drafts" and "The book's CI needs no secret for the press at all." The file says only "A private book needs no cross-repo token". Fix: "Because the action installs the press from its own checkout, a private book needs no cross-repo token."
6. **Table of authorities "never inside it".** Line 559: "which the press publishes beside the book and never inside it." Section 3.5 says only "`<slug>-sources.md` # Table of authorities (only with config/authorities.yaml)". Fix: "which the press publishes as a separate file in *dist/*."
7. **The invariant ledger "that its tests prove".** Line 414. The file names `INV-add-no-clobber` and says the ledger lives in `.celebrimbor/invariants.yaml` (20.A.3), but it never describes the ledger as properties the tests prove. This is low stakes. Fix: "a named entry in the press's invariant ledger, in this case `INV-add-no-clobber`."
8. **The silent `press config set` session.** Example 3.5 shows six `set`/`unset` commands with no output. The writer's report admits the output format is unknown, and the file captures none. Showing no output tells the reader the commands print nothing. Fix: present the six lines as commands only, with no output implied (for example, introduce them as "the commands" rather than a session), or get a capture.

## 2. Contradicted

1. **Example 3.7 and its prose (lines 384 to 406).** The chapter's reconstruction shows no output from `press add`, adds `the-pool-of-tears` and `also-by`, puts glossary at `x-`, and lists *book/appendices* before *book/chapters*. S1, the real capture, reads:

   ```text
   $ press add chapter "Down the rabbit-hole"
   created book/chapters/01-down-the-rabbit-hole.md
   $ press add appendix about-the-author
   created book/appendices/z-about-the-author.md
   $ press add appendix glossary
   created book/appendices/y-glossary.md
   $ ls -1 book/chapters book/appendices
   book/chapters:
   00-preface.md
   01-down-the-rabbit-hole.md

   book/appendices:
   y-glossary.md
   z-about-the-author.md
   $ cat book/chapters/01-down-the-rabbit-hole.md
   # Down the rabbit-hole

   Write this part here. This placeholder paragraph only exists so the file is valid Markdown that builds; delete it and begin.
   ```

   Fix:
   - Replace Example 3.7 with S1 verbatim. The `cat` is optional, but it proves the heading and the stub.
   - Change line 384 to "adding the first chapter and two pieces of back matter, then listing the two directories."
   - Line 406, "The second gets `# The pool of tears`, sentence-cased from the bare slug", has no capture behind it. Either cut it, or keep the rule as prose and drop the claim about the example: "A bare slug such as `the-pool-of-tears` would get the heading `# The pool of tears`."
   - Also say that `press add` prints `created <path>` for each file.

2. **Legacy `trim` "only" checked.** Line 272: "An older book that still carries a `trim` mapping keeps it, but the press only checks it against the profile". Section 20.B.3: "The landing page's PDF row, the `publish` checklist trim, and the coverwrap back-text width all read the legacy `metadata.trim`". Section 20.A.17: "`art accept --as cover` reads `metadata.trim` (default 6×9), not the profile." Other code paths do read the legacy mapping, so "only" is false. These are bug-like items, so do not document them as features. Fix: drop "only": "the press checks it against the profile and refuses the metadata when the two disagree."
3. **Every write validated by "the same typed model".** Line 282: "Before `press config set` touches a byte on disk, it runs the new value through the same typed model that validates a build." Section 17.3 (Validation) says "Every write is validated by the real typed model for its file ... `aesthetic.yaml` has no validator." Table 3.6 routes the whole aesthetic block through `press config`, so the claim is false for those fields. Line 322 ("checks every config file the book has against its model") has the same flaw. Fix: add "except for *config/aesthetic.yaml*, which has no validator", and in line 322 say "checks the config files".

## 3. Drifted

1. **Example 3.3's elided commerce block (lines 137 and 185).** The writer did not have S2. Fix: replace `...` with a blank line and the S2 block verbatim:

   ```text
   # Direct print ordering: a reader-facing "Order a print copy" link to a
   # provider-hosted checkout (Lulu, Peecho, a Bookvault store, ...). The
   # provider is the seller of record and owns payment, tax, fulfillment,
   # and support; this block holds only URLs and a name, never a credential
   # or a price. Enable it once the edition is qualified (press qualify).
   # A policy link is optional: give a URL to link your own hosted page, or
   # omit it and press generates an honest page on your book site. Add
   # policies: {support,privacy,refund} text to append your own words.
   # commerce:
   #   print-ordering:
   #     enabled: true
   #     edition: paperback
   #     storefront-url: "https://www.lulu.com/shop/..."
   #     seller-of-record: "Lulu"     # who the reader actually buys from
   #     support-url: "https://example.test/support"   # optional; omit to generate
   #     # privacy-url / refund-url omitted -> press generates those pages
   #     policies:
   #       privacy: "We keep no reader data; the provider handles your order."
   ```

   The prose must then hedge two lines of it.
   - "(press qualify)": 20.A.25 says "There is no `press qualify` command. The qualification is recorded by hand in `config/qualification.yaml`."
   - "The provider is the seller of record" and `seller-of-record: "Lulu"`: 20.A.12 says "Do not assert that Lulu is legally the seller of record. Say press's *model* is provider-as-seller and the publisher must confirm."

   Without the block, line 137's "long commented block" is fine. With it, add one sentence after the example covering both points.
2. **Index position (lines 347 and 359; S3 ruling).** Line 347 says the press merges "chapters, then appendixes, then the generated subject index". Line 359 stops at "By filename, *a-* sorts ahead of all three." S3: "the generated index file is usually lettered `a-` and therefore sorts first among the appendices in the merged book. State the mechanism; do not call it a bug." Fix: after line 359's filename sentence, add "so in the merged book the index usually comes first among the appendixes." Make line 347 consistent with it, for example: "chapters, then appendixes sorted by filename letter, with the generated subject index lettered among them."
3. **Art directive for Figure 3.2: the index filename.** Line 361 has "a-index.md" and "c-index.md". The file says `build/generated/<letter>-index-of-subjects.md`, and the chapter itself says *a-index-of-subjects.md* (line 580). Fix: "a-index-of-subjects.md" and "c-index-of-subjects.md".
4. **"before it judges your manuscript".** Line 478: "which proves the checker still works before it judges your manuscript." The captured order puts "Source checks passed: 1 ordered Markdown files" *before* "Checker self-test passed". Fix: "which proves the checker still works on known-bad input."
5. **"A value that would break the build never reaches the file."** Line 282. The model refuses invalid values, but a value can pass the model and still fail a build. A sentinel that is absent from the text is one example: "`sentinel ... not found`", 3.4. Fix: "A value the model refuses never reaches the file."
6. **The date year.** Table 3.3, `date`: "the first four-digit year". The file says "The first `1xxx`/`2xxx` year". Fix: "the first year (a four-digit number beginning 1 or 2)".
7. **Structured fields as "a list".** Line 316. Section 17.3 describes `qualification` as "physical-inspection records (schema_version + inspections)", which is a mapping, not a list. Fix: "holds data too rich for one command line".
8. **Sidebar: "the exact ref the book's workflow names".** Lines 454 and 458. The book's workflow names `build.yml@v3`, and build.yml "hardcodes the press action ref". The file says "the installed press is pinned to the exact action ref". Fix: "checks out the press at the action ref that the press's reusable workflow pins". Line 460's "It forbids" is acceptable: the file cites CLAUDE.md as the source of the rationale.
9. **Example 3.4 framed as a capture of "a fresh Alice book".** The file's text is a template with `N`. Filling in 0 and 1 follows the template, but the reader should not take it for a capture, because by Example 3.5 the Alice book no longer has those values. Fix: "Example 3.4 shows the refusal a freshly scaffolded book draws", and keep the filled numbers.

## 4. Missing

1. **The sequence in Example 3.5 would fail a build.** Example 3.5 sets the two Alice sentinels and `verify-min-pages 24` while the book holds only the preface stub (chapters arrive in Example 3.7). The file says the sentinels are "proven present in the source and in every artifact", and it lists "`sentinel ... not found`" among the common first-run refusals (3.4). A reader who runs `press check` or `press all` right after Example 3.5 gets a refusal, and a 24-page floor fails a stub PDF. Fix: move those two commands after the chapters exist, or add a sentence warning that they will refuse until the manuscript contains the phrases and reaches 24 pages. Rated may per the brief, but I would treat it as should.
2. **Common first-run refusals** (3.4, from QUICKSTART §6): `pandoc is required`, a style or jargon failure, `sentinel ... not found`, the font-scan "hang", and CI dying at "Initialize containers" (retry). "A first local build" covers only the font scan.
3. **`press add` prints `created <path>`** (S1). This is covered by the fix for Contradicted 1.
4. **The publish checklists.** Line 567 names `press pcn` and `press onix` as the registration targets' outputs but omits "the publish checklists (§10)". Also, 20.B.13: `press all` does not build `print` or `coverwrap`, "but the commerce release gate (ordering-enabled books only) does". A one-clause hedge on "The `press all` target makes none of these" would be accurate.
5. **The scaffolded CLAUDE.md house laws.** These are verbatim in 3.1. Table 3.2 mentions "the house laws" without saying what they are. One sentence listing them would orient the reader (no dashes, straight quotes, paragraphs under 190 words, sentinels survive, known-bad fixtures stay rejected).
