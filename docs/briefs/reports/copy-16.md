# Copyedit: Chapter 16, Inside the press

File: `book/chapters/16-inside-the-press.md`

## Status

REVISE. Three blocks: one watchlist sighting ("lands", 72, where it is
not press's name for anything; the Chapter 8, 12, and 13 precedent) and
two one-line closers (338 and 357). `press check` passes the whole book
(exit 0). Its jargon audit names one inspect term in this file,
"honest" (165), which sits inside a verbatim quotation of the ledger and
is accepted.

Counts by severity: blocks 3, should 28, may 23, fact 2 (items 55 and
56).

Most frequent rules broken: two ideas (17, counting the items that
carry it beside another rule), wrong term (12, counting the watchlist
block), hidden actor (6).

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 38 findings (406 sentences, average 11.8 words, max 45).

- Sentence length at 6 (the In-this-chapter list, merged by the
  counter), 50, 58, 60 (fig-alt), 283 (fig-alt), and 342 (filename list
  run together): accepted. None is running prose over 30 words.
- Sentence length at 98 and 106: accepted. The Tip is one 25-word
  imperative. 106 is three sentences under 30.
- Sentence length at 116 (the footnote): a real finding (item 13).
- Sentence length at 377: the footnote marker merges two sentences.
  Each is under 30 words; the first is item 31.
- Paragraph length and `-ing` forms at 52, 62, and 285: accepted. They
  are `<!-- art: -->` directions, not printed. ("centred" at 52 is
  British, but the comment never reaches print.)
- Paragraph length at 23: accepted. The paragraph has six sentences; the
  counter splits the quoted "There is no book in here."
- Paragraph length at 129: a real finding (item 16).
- Passive "is forbidden" (74), "are stated" (86), "are unstated" and "be
  overtrusted" (165), "is only proven" (250): accepted. All are inside
  verbatim quotations of press's documentation.
- "Verifying" (72, quoted law), "Contributing" (355, a heading),
  "beginning" (361), "alternating" and "branching" (art comments):
  accepted.
- "verify" (74, 179, 240, 361, 371): accepted under the 80 percent rule.
  The word names the target and the script.
- "therefore" (204, 338): period-correct and allowed by the contract.
  338 is a block for another reason (item 2).
- Phrasal verb "go through" (110): accepted. It is plain.
- Vague association at 283 and 287: accepted. Both are "linked to",
  which is the receipt chain's own phrase.
- Semicolon at 381: the index comment, not prose. The chapter has no
  prose semicolon outside quotations (Table 16.4 and 170 to 172 are
  verbatim ledger text).

Also accepted on reading:

- Second person and present tense hold throughout. There is no "I" and
  no "we".
- Dry understatement appears at 74 ("last week's PDF"), 114 ("`alice`
  must find another word for hers"), 129 ("while the gate reported
  nothing"), 252 ("without a word"), and footnote 275. None is in a
  heading.
- Six admonitions (98, 146, 178, 234, 254, 373), all imperative and one
  or two sentences each. Item 19 and item 52 concern repetition, not
  form.
- Five footnotes, each an aside. Footnote 82 converts the epoch value
  (1784160000 is 2026-07-16 00:00 UTC), and the body does not need it.
- Era spellings: "filename" (90, 172) and "Web site" (265) are correct.
  No "Unix", "e-mail", "manpage", "appendixes", or "toward" occurs. The
  two American-spelling slips are items 7 and 23.
- The editions are named by press's names, and each is glossed by its
  writer or in parentheses at 70.
- Exit statuses (Table 16.2), list numbers in Example 16.2, and version
  numbers are digits correctly.
- The verbatim quotations at 301 ("not by code", "not a missing
  feature") have a not-X-but-Y shape, but they are press's text and stay.
- `printshop` as the CI host matches the cast in *docs/continuity.md*.

## Findings

1. "Every edition lands in *dist/* under the slug, as *alice.pdf*,
   *alice.epub*, and the rest." (72)
   Rule: wrong term (watchlist: "lands"). Severity: blocks.
   Fix: "The press writes every edition into *dist/* under the slug, as
   *alice.pdf*, *alice.epub*, and the rest."

2. "The press therefore keeps its own verification, containment,
   artifact graph, config validation, and release gate out of an
   extension's reach." (338)
   Rule: one-line closer (it restates the list two sentences above, and
   "artifact graph" is a forbidden synonym for the registry).
   Severity: blocks.
   Fix: delete the sentence. The paragraph ends on "An extension can
   depend on a sealed capability but must never claim one." (see
   item 48).

3. "A warning in prose alone is not enough." (357)
   Rule: one-line closer (it restates the ROADMAP quotation before it,
   and the second law in the next paragraph says it again).
   Severity: blocks.
   Fix: delete the sentence. The paragraph ends on the ROADMAP
   quotation.

4. "Use it when a traceback names a module you have not met." (25)
   Rule: perfect tense. Severity: should.
   Fix: "Use it when a traceback names a module you do not know."

5. "The title, the slug, the sentinels, the banned words, the front
   matter, and the art all live in the book repository." (23)
   Rule: wrong term ("banned words" is a forbidden synonym; the thing is
   the house rules' banned patterns). Severity: should.
   Fix: "The title, the slug, the sentinels, the banned patterns, the
   front matter, and the art all live in the book repository."

6. "Nothing inside the frame talks to the operating system directly, and
   the section "The adapters boundary" later in this chapter explains
   how the press holds that line." (48)
   Rule: two ideas. Severity: should.
   Fix: "Nothing inside the frame talks to the operating system directly.
   The section "The adapters boundary" later in this chapter explains how
   the press holds that line."

7. "A stack of labelled bands for the press's module areas..." (50,
   `fig-alt`)
   Rule: era spelling (American). Severity: should.
   Fix: "A stack of labeled bands for the press's module areas..."

8. "An unknown target prints `unknown target: X` with a suggestion and
   exits with status 2." (54)
   Rule: hidden actor (the target does not print; the press does).
   Severity: should.
   Fix: "For an unknown target, the press prints `unknown target: X`
   with a suggestion and exits with status 2."

9. "Rendering resolves each prefix against the install or the book
   repository and drops an optional file that the book does not have."
   (68)
   Rule: hidden actor. Severity: should.
   Fix: "`render_defaults` resolves each prefix against the installed
   press or the book repository, and it drops an optional file that the
   book does not have."

10. "The press sets `SOURCE_DATE_EPOCH` to `1784160000` unless you set it
    yourself, and the source zip stamps every member with one fixed
    timestamp." (80)
    Rule: two ideas (and condition first). Severity: should.
    Fix: "Unless you set `SOURCE_DATE_EPOCH` yourself, the press sets it
    to `1784160000`. The source zip stamps every member with one fixed
    timestamp."

11. "*yamlio.py* calls itself "the single YAML door", and every read or
    write of a YAML file in the press passes through it." (92)
    Rule: two ideas. Severity: should.
    Fix: "*yamlio.py* calls itself "the single YAML door". Every read or
    write of a YAML file in the press passes through it."

12. "The ledger records this as `INV-graph-no-stale`, one of its critical
    invariants." (74; also "The ledger names this `INV-cli-exit-code`"
    at 132 and "under `INV-art-key-never-stored`" at 144)
    Rule: wrong term (the ledger and *invariant* are used three times
    before 152 defines them in italic). Severity: should.
    Fix: at 74, "The invariant ledger, which the section "Invariants"
    later in this chapter describes, records this as
    `INV-graph-no-stale`, one of its critical entries." Leave 132 and
    144 as they are once 74 points forward.

13. "Without the quotes, a later read would turn the string `3` into a
    number and the string `true` into a boolean, and a field typed as
    text would then fail the model." (116, footnote)
    Rule: sentence over 30 words (31), and two ideas. Severity: should.
    Fix: "Without the quotes, a later read would turn the string `3` into
    a number and the string `true` into a boolean. A field typed as text
    would then fail the model."

14. "Its HTTP client gives every request a 30-second timeout and a cap on
    the bytes it will read, and it retries failed requests." (122)
    Rule: two ideas. Severity: should.
    Fix: "Its HTTP client gives every request a 30-second timeout and a
    cap on the bytes it will read. The client also retries failed
    requests."

15. "A gate searches the modules outside *adapters/* for direct use of
    the three modules, and the receipt chain includes a layer named
    `boundary`." (124)
    Rule: two ideas ("receipt chain" is also used here before the
    section "Trust receipts" introduces it). Severity: should.
    Fix: "A gate searches the modules outside *adapters/* for direct use
    of the three modules. The trust receipts, later in this chapter,
    also include a layer named `boundary`."

16. The sidebar paragraph "The adapters boundary keeps every process
    start..." (129), eight sentences in one paragraph.
    Rule: paragraph over six sentences (one topic per paragraph).
    Severity: should.
    Fix: break before "The fix, in version 2.3.1, had two parts." The
    first paragraph tells the failure (five sentences), the second the
    fix (three sentences).

17. "The ledger names this `INV-cli-exit-code`, and the selftest shows it
    with a tool that exits 43: the press exits 43 as well." (132)
    Rule: two ideas. Severity: should.
    Fix: "The ledger names this `INV-cli-exit-code`. The selftest shows
    it with a tool that exits 43, and the press exits 43 as well."

18. "It runs 29 checks in a fixed order, and the test suite parametrizes
    pytest over the same list." (204)
    Rule: two ideas. Severity: should.
    Fix: "It runs 29 checks in a fixed order. The test suite parametrizes
    pytest over the same list."

19. "**Tip:** Run `press selftest` from a clone of the press repository
    whenever you change the press. A run from a book's environment skips
    every check that reads repository files." (235)
    Rule: the admonition repeats the paragraph above it (style guide
    8.1). Severity: should.
    Fix: delete the Tip. The paragraph at 232 already says both things.
    The chapter keeps five admonitions.

20. "The *quality gate* is celebrimbor's gate as the press configures
    it, and *scripts/verify.sh* runs it with `celebrimbor gate`." and
    "It needs Python 3.11 or later, and no book ever installs it at run
    time." (240)
    Rule: two ideas (both sentences). Severity: should.
    Fix: "The *quality gate* is celebrimbor's gate as the press
    configures it. *scripts/verify.sh* runs it with `celebrimbor gate`."
    and "It needs Python 3.11 or later. No book ever installs it at run
    time."

21. "A *ratchet* is a floor recorded in a baseline file, and the gate
    fails when a measurement falls below its floor." (242)
    Rule: two ideas (a definition and a behavior). Severity: should.
    Fix: "A *ratchet* is a floor recorded in a baseline file. The gate
    fails when a measurement falls below its floor."

22. "*producers.yaml* is the producer ledger, and its pending entries
    carry `review_by` dates." (248)
    Rule: wrong term (a *producer* is never defined; the reader meets
    the word only in the quotation at 250), and two ideas.
    Severity: should.
    Fix: "*producers.yaml* is the *producer ledger*, the list of modules
    that write an artifact and the verifier that inspects each one. Its
    pending entries carry `review_by` dates." (fact: see fact checker for
    the gloss.)

23. "...and cancelled every job on it within a second..." (275, footnote)
    Rule: era spelling (American). Severity: should.
    Fix: "GitHub retired that runner in the middle of a release and
    canceled every job on it within a second, with "configuration not
    supported"."

24. "Trust receipts are the mechanism that enforces the second sentence."
    (279)
    Rule: wrong term (first use of the term, not italic and not defined;
    the definition comes at 287). Severity: should.
    Fix: "A *trust receipt* records that a layer of proof ran and passed,
    and trust receipts enforce the second sentence." Then 287 begins
    "Verification requires a complete chain..." (see item 25).

25. "Verification requires a complete chain, with "every layer present,
    contiguous, and linked to its predecessor"." (287)
    Rule: hidden actor. Severity: should.
    Fix: "`press.receipts verify` requires a complete chain, with "every
    layer present, contiguous, and linked to its predecessor"."

26. "When a three-part tag arrives, the release contract builds the
    wheel..." (289; also "every three-part tag stays immutable" at 379)
    Rule: wrong term (the vocabulary's name is "immutable tag").
    Severity: should.
    Fix: "When an immutable tag such as `v3.0.2` arrives, the release
    contract builds the wheel, downloads both receipts, and assembles
    them." At 379: "so `main` stays open and every immutable tag stays
    fixed."

27. "`invariants` lists the guarantees it takes on, and `proofs` names a
    proof for each." (336)
    Rule: wrong term ("guarantee" is a forbidden synonym for invariant).
    Severity: should.
    Fix: "`invariants` lists the invariants it takes on, and `proofs`
    names a proof for each."

28. "Conformance refuses six faults, each with a located reason: ..."
    (340)
    Rule: hidden actor. Severity: should.
    Fix: "The conformance gate refuses six faults, each with a located
    reason: a collision, an unsupported contract, an unknown dependency,
    a sealed claim, an unproven obligation, and a malformed manifest."

29. "At the time of this writing, the press supports one contract major,
    `SUPPORTED_CONTRACT_MAJORS = (2,)`, and no runtime loads extensions."
    (344)
    Rule: two ideas. Severity: should.
    Fix: "At the time of this writing, the press supports one contract
    major, `SUPPORTED_CONTRACT_MAJORS = (2,)`. No runtime loads
    extensions."

30. "If it cannot, write a checker or a verifier that refuses the broken
    result." (359; also step 2 at 366, "as a checker or verifier if you
    cannot")
    Rule: wrong term ("the checker" is reserved for `press check`; a new
    rule is a check inside it). Severity: should.
    Fix: "If it cannot, write a check for the checker or a verifier that
    refuses the broken result." Step 2: "Write the guard, as a generator
    if you can and as a check or a verifier if you cannot."

31. "The press repository's `main` branch takes direct pushes by design,
    and the checks bite at the release boundary." (377)
    Rule: two ideas ("bite" is also idiom). Severity: should.
    Fix: "The press repository's `main` branch takes direct pushes by
    design. The checks stop a change at the release boundary instead."

32. "...and the paragraphs below follow its arrows for the Alice book."
    (58)
    Rule: meta-narration. Severity: may.
    Fix: "@fig:end-to-end-data-flow draws the whole path for the Alice
    book."

33. "The design profile, the aesthetic, and the front matter become TeX
    fragments under *build/*. All three streams meet in
    `build.book_inputs`..." (64)
    Rule: hidden actor, and synonym rotation ("kinds of input", then
    "streams"). Severity: may.
    Fix: "The build turns the design profile, the aesthetic, and the
    front matter into TeX fragments under *build/*. All three kinds of
    input meet in `build.book_inputs`, which hands one assembled set of
    inputs to everything after it."

34. "`gen_index` writes the subject index into *build/generated/*, and
    the build treats it as one more appendix." (66)
    Rule: two ideas. Severity: may.
    Fix: "`gen_index` writes the subject index into *build/generated/*.
    The build treats the index as one more appendix."

35. "It also discovers the chapter files." (104)
    Rule: synonym rotation (64 says `booklib.chapter_files` "finds" them).
    Severity: may.
    Fix: "It also finds the chapter files."

36. "Every later stage reads the same values, and no stage can quietly
    adjust a field for the stages after it." (106)
    Rule: wrong term ("stage" is on the target's never-list, and a
    reader can take it for one). Severity: may.
    Fix: "Every later module reads the same values, and no module can
    quietly adjust a field for the modules after it."

37. "It indents mappings by 2, sequences by 4, and the dash by 2." (112)
    Rule: numbers under ten in prose (a measurement keeps digits only
    with its unit). Severity: may.
    Fix: "It indents mappings by 2 spaces, sequences by 4, and the dash by
    2."

38. "It matches the words api key, secret, token, password, and bearer,
    in any case, and the opening line of an armored private key." and
    "The press refuses a dedication that contains the word "secret", with
    exit status 4, and `alice` must find another word for hers." (114)
    Rule: code typography (the matched words are literals and need
    quotation marks), and two ideas in the second sentence.
    Severity: may.
    Fix: "It matches the words "api key", "secret", "token", "password",
    and "bearer", in any case. It also matches the opening line of an
    armored private key." and "The press refuses a dedication that
    contains the word "secret", with exit status 4. `alice` must find
    another word for hers." (Keep the understatement as its own
    sentence.)

39. "Toolchain strictness keys on `PRESS_TOOLCHAIN`, which the toolchain
    image sets, and never on the ambient `CI` variable." (144)
    Rule: noun stack and the action in the verb ("keys on" also collides
    with "image-model keys" one sentence earlier). Severity: may.
    Fix: "The press decides how strict to be about the toolchain from
    `PRESS_TOOLCHAIN`, which the toolchain image sets, and never from the
    ambient `CI` variable."

40. Table 16.3, the Meaning column: "The property in one sentence.",
    "The test or fixture that shows the enforcement works.", "The known
    edges of the property, in plain words." (158 to 161)
    Rule: table cells hold sentences, not fragments (style guide 3.7).
    Severity: may.
    Fix: "It states the property in one sentence." "It names the test or
    fixture that shows the enforcement works." "It states the known edges
    of the property, in plain words." (The Statement cell keeps its
    example sentence after the first.)

41. "`contract_mirror` requires *AGENTS.md* to equal *CLAUDE.md* below
    the heading. `docs` requires the three generated documents to match
    their sources." (228)
    Rule: rhythm (both facts are stated at 94, in a chapter that quotes
    "Facts are stated once"). Severity: may.
    Fix: "`contract_mirror` and `docs` are the two checks of the section
    "One statement of each fact" earlier in this chapter."

42. "The backfill found a vacuous test. A test of the title tie passed
    with no filter at all, because pandoc ties `Mr.` itself.
    `PRESS_LUA_COV_DIR` names the directory where a development run
    writes its Lua coverage." (252)
    Rule: wrong term ("vacuous" is reserved for press's "vacuous
    witnesses"; "title tie" is never defined), and two topics in one
    paragraph. Severity: may.
    Fix: "The backfill found a test that proved nothing. A test of the
    tie after a title such as `Mr.` passed with no filter at all,
    because pandoc writes that nonbreaking space itself." Move the
    `PRESS_LUA_COV_DIR` sentence after the Warning, or into the list of
    ratchets at 246.

43. "The `quality` job in *selftest.yml* writes a receipt, uploaded as
    `receipt-quality`, and the integration gate writes
    `receipt-integration`." (289)
    Rule: hidden actor ("uploaded"). Severity: may.
    Fix: "The `quality` job in *selftest.yml* writes a receipt and
    uploads it as `receipt-quality`. The integration gate writes
    `receipt-integration`."

44. "The terminal release receipt names two digests..." (291)
    Rule: wrong term ("terminal" reads as the machine in a book of
    sessions). Severity: may.
    Fix: "The final release receipt names two digests: the digest of the
    built wheel and the digest of the pinned toolchain image."

45. "An extension adds an entry to one of five data registries, and the
    press selects the entry by its id." (303; also the "Registry" column
    of Table 16.6)
    Rule: wrong term ("the registry" is reserved for `registry.py`).
    Severity: may.
    Fix: "An extension adds an entry to one of five data tables, and the
    press selects the entry by its id." Head the table column "Where it
    lives".

46. "`kind` names the surface it registers into, and `contract-major`
    names the contract its author targeted. `provides` lists the exact
    names it claims in that registry, and `requires` lists names it
    depends on, from the core or from itself." (336)
    Rule: two ideas (twice). Severity: may.
    Fix: "`kind` names the surface it registers into. `contract-major`
    names the contract its author targeted. `provides` lists the exact
    names it claims on that surface. `requires` lists the names it
    depends on, from the core or from itself."

47. "Both `press pdf` and `python -m press pdf` arrive there, and the
    route table looks the target up in the catalog." (54)
    Rule: two ideas. Severity: may.
    Fix: "Both `press pdf` and `python -m press pdf` arrive there. The
    route table then finds the target in the catalog."

48. "An extension may depend on a sealed capability but may never claim
    one." (338)
    Rule: honest modals. Severity: may.
    Fix: "An extension can depend on a sealed capability but must never
    claim one."

49. "The contract says that "A future runtime that *loads* extensions
    will reuse exactly this gate."" (344)
    Rule: quotation run into the sentence with a capital. Severity: may.
    Fix: "The contract says: "A future runtime that *loads* extensions
    will reuse exactly this gate.""

50. "`INV-graph-no-stale` shows a finished scar." (361)
    Rule: rhythm (third full telling of the same invariant, after 74 and
    176). Severity: may.
    Fix: keep the example, and cut the restated failure:
    "`INV-graph-no-stale`, met earlier in this chapter, shows a finished
    scar. The ledger entry
    names the enforcement, names its proof, and states its limit, the
    command-line path only."

51. Steps 1, 4, 5, and 6 (365, 368, 369, 370) each give two imperatives.
    Rule: one imperative per step (style guide 3.6). Severity: may.
    Fix: steps 1, 4, and 6 are one action each and may stay. Split step
    5 in two: "Add the scar to the scars list in *CLAUDE.md*." and "Copy
    the same change into *AGENTS.md*, below the heading."

52. "**Warning:** Do not call a verifier module directly on *dist/* to
    check a book. Run the verify target from the command line, so that
    the press rebuilds what it inspects." (179)
    Rule: the admonition repeats the paragraph above it.
    Severity: may (it adds the imperative, which the paragraph lacks).
    Fix: keep the Warning, and end the paragraph at 176 on "...skips the
    rebuild." The Warning then carries the consequence alone.

53. The sidebar "The import the gate did not see" (127 to 129) runs 133
    words.
    Rule: sidebar length (style guide 3.5, 150 to 400 words).
    Severity: may.
    Fix: no wording change required; when item 16 splits it, one more
    sentence on how the gap was found would bring it to length (fact:
    see fact checker for what to add).

54. "...and `verify_pdf --profile print` inspects it. Then `gen_coverwrap`
    draws the cover wrap in TikZ through latexmk, and `verify_coverwrap`
    inspects that." (78)
    Rule: rhythm (three "inspects" in two sentences, and "it"/"that"
    rotation). Severity: may.
    Fix: "Then `gen_coverwrap` draws the cover wrap in TikZ through
    latexmk, and `verify_coverwrap` inspects the wrap."

55. "*hostile/collision.yaml* claims `pdf`, *version.yaml* targets major
    99, and *sealed.yaml* claims `core-verification`. *unproven.yaml*
    has `proofs: []`, and *malformed.yaml* gives `contract-major` as the
    string `"two"`." (342)
    Fact: see fact checker. 340 names six faults, and 342 names five
    hostile fixtures. Confirm whether an unknown-dependency fixture
    exists and, if so, name it.

56. "*src/press/quality_checks.py* registers 29 press domain checks with
    the gate." (242)
    Fact: see fact checker. The selftest also runs 29 checks (204). If
    both counts are right, the coincidence deserves a clause so the
    reader does not take them for one list; if not, correct one.
