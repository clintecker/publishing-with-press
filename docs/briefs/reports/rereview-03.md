# Re-review: Chapter 3, The shape of a book repository

File: `book/chapters/03-the-shape-of-a-book.md` (613 lines, revised). Read
against the four desk reports, the writer's "Revision" section in
`report-03.md`, the ledger's last forty lines, and facts-03 S1 to S3 (plus
facts-01 S1 and S3 for the `press all` material). Line numbers refer to the
revised file.

**Verdict: REVISE.** 3 open blocks, 6 open shoulds.

## Mechanical checks

- `press check`: the source pass and the self-test are green. The editorial
  pass fails only on `09-the-house-design.md` (two run-ups and a 216-word
  paragraph) and `11-the-art-department.md` (a 281-word paragraph). None of
  the failures is in this file. The jargon pass did not run, because the
  editorial pass failed first.
- `ste_check.py`: 43 findings, 513 sentences, max 45. Every residual is the
  same kind the writer and copy desk explained: the box, headings and
  captions (`-ing`), the joined image and art lines (76, 360, 574, which
  the checker counts as one paragraph because of the missing blank line
  below), the index comment, quoted press text (semicolons at 103, 408,
  438), "therefore"/"however", the subjunctive at 67, and the quoted
  "Facts are stated once". No prose sentence is over 30 words, and there
  is no prose semicolon.
- Code lines: none is over 64 columns. Pass.
- Fences: all 17 fences are untagged. Open (S-1).
- `art:` comments: all three come after their image lines, but each sits
  on the very next line with no blank line between. Open (B-1).
- Commerce block (Example 3.2): every word of the opening comment matches
  S2 (checked by joining the lines and comparing). It is rewrapped at 64
  columns, four long lines are cut with ` ...`, and line 127 tells the
  reader both. Both hedges are present at line 173: no `press qualify`
  command exists (record it by hand in *config/qualification.yaml*), and
  provider-as-seller is press's model, which the publisher must confirm.
  The 64-column ruling allows excerpts, and the rewrap is disclosed, so I
  accept this as an equivalent.
- `press add` (Example 3.6): S1 verbatim except the `cat` line, which is
  cut with `...` and disclosed. The full placeholder text is given in prose
  at 408. Pass.
- Sentinels and the 24-page floor are no longer set on day one. Lines 239
  to 246 show them as what `alice` sets later and give the reason. Pass.
- Edition names: the landing-page names are used throughout, but three
  of them appear before they are glossed. Open (S-4).
- Gallery Alice captures: the `ls dist/` listing is fine, because facts-01
  S1 allows the slug substitution. The `press all` run is the gallery
  example presented as the reader's own book. Open (B-2).

## Findings table

| Desk | No. | Status | Note |
|---|---|---|---|
| Facts | U1 | resolved | 117 "each of them is optional" |
| Facts | U2 | resolved | 199 |
| Facts | U3 | resolved | 219, no "because" clause |
| Facts | U4 | resolved | 326 |
| Facts | U5 | resolved | 456 |
| Facts | U6 | resolved | 581 |
| Facts | U7 | resolved | INV paragraph cut; footnote kept |
| Facts | U8 | **open** | introduced as commands, but the fix added an unsupported claim (S-2, S-3) |
| Facts | C1 | resolved | Example 3.6 is S1; pool-of-tears is now a hypothetical |
| Facts | C2 | resolved | 267, "only" dropped |
| Facts | C3 | resolved | 277 exception; 326 "the config files" |
| Facts | D1 | resolved (equivalent) | rewrapped and cut, disclosed at 127; hedges at 173 |
| Facts | D2 | resolved | 346, 358 follow S3 |
| Facts | D3 | resolved | directive uses *a-/c-index-of-subjects.md* |
| Facts | D4 | resolved | 500 |
| Facts | D5 | resolved | 277 |
| Facts | D6 | resolved | Table 3.3 `date` |
| Facts | D7 | resolved | 320 |
| Facts | D8 | resolved | 454, 458 |
| Facts | D9 | resolved | 229 |
| Facts | M1 | resolved | 239 to 246 |
| Facts | M2 | resolved | 504, 562 |
| Facts | M3 | resolved | 383 |
| Facts | M4 | resolved, new error | the hedge is present; the cross-reference is wrong (S-6) |
| Facts | M5 | resolved | 97 matches the scaffolded CLAUDE.md laws |
| Dev | C1 | resolved | Default columns in Tables 3.3 to 3.5 |
| Dev | C2 | **open** | the `get` session output is not from the fact file (B-3) |
| Dev | C3 | resolved | 70 weakened |
| Dev | P1 | resolved | knobs deferred |
| Dev | P2 | resolved | `cd alice` in Example 3.1 |
| Dev | P3 | **open** | the run is shown, but as the wrong book (B-2) |
| Dev | P4 | resolved | 125 defines *book model* |
| Dev | P5 | resolved | 518; no branch step invented |
| Dev | P6 | resolved | S1 capture |
| Dev | P7 | resolved | 326 |
| Dev | R1 | resolved | 599 to 601, prose by failure |
| Dev | R2 | resolved | 117 to 119 |
| Dev | R3 | resolved | globs inline at 344 |
| Dev | R4 | resolved | |
| Dev | N1 | resolved | directive filenames match the prose |
| Dev | box | **open (new)** | In-this-chapter box no longer matches the A-head (S-5) |
| Copy | 1 (blocks) | resolved | 500 "comes with the press" |
| Copy | 2 to 4 | resolved | 500 (fact wording), 17, 70 |
| Copy | 5 | declined-accepted | the fact desk's "each of them is optional" governs |
| Copy | 6 to 11 | resolved | 119, 179, 219, 219, 224, 261 |
| Copy | 12 | resolved in text | the editor still needs to add a "vacuous witness" entry to `docs/vocabulary.md` |
| Copy | 13 to 20 | resolved | |
| Copy | 21 | resolved (equivalent) | the Tip is cut |
| Copy | 22 to 27 | resolved | |
| Copy | 28 | resolved | `press art commission` is a real command (facts-03 §20 A.16) |
| Type | B1 to B7 | resolved | all code at 64 columns or fewer |
| Type | S1, S2 | declined-accepted | page breaks; recheck at the final build with figures |
| Type | S3, S4 | resolved | separators widened |
| Type | S5 | resolved | remote URL on its own line |
| Type | S6 | resolved | Python block gone |
| Type | S7 | resolved | 13 and 12 rows |
| Ledger | art spacing | **open** | B-1 |
| Ledger | fence tag | **open** | S-1 |
| Ledger | edition gloss | **open** | S-4 |

## Open items

### Blocks

**B-1. `art:` comments have no blank line after the image line** (lines
76/77, 360/361, 574/575). For example:

```text
![The dist directory after press all](assets/woodcuts/03-03-dist-after-all.png){...}
<!-- art: ARCHETYPE tree. ...
```

Under the ledger's correction, pandoc reads all three as plain paragraphs,
not figures. Fix: `python3 tools/space-art-comments.py
book/chapters/03-the-shape-of-a-book.md`.

**B-2. Example 3.9 presents the gallery Alice run as the reader's book**
(lines 465 to 498). Quote: "With the preface, one chapter, and two
appendixes in place, `alice` runs `press all`" and "The four files are the
preface, the chapter, and the two appendixes." The capture is facts-01 S3,
press's gallery example `alice-in-wonderland`. Its four files are
*01-down-the-rabbit-hole*, *02-the-pool-of-tears*,
*03-a-caucus-race-and-a-long-tale*, and *z-about-this-edition*. It has no
preface, its PDF has 23 pages, and its two sentinels are already set. The
example also renames `alice-in-wonderland` to `alice` in the `stitched`
and `Verified archives` lines. Facts-01 S1 allows that substitution only
for the `ls dist/` listing. The ledger rules that gallery captures are
quoted as such. Fix:
- Introduce the run as "the same run on press's own gallery example, a
  three-chapter Alice with one appendix".
- Keep its `alice-in-wonderland` names in the `press all` lines, or state
  the rename.
- Replace the four-files sentence with "The four files are its three
  chapters and its appendix."
- The `ls dist/` part may stay as `alice` under S1.

**B-3. The `press config get` session is not supported by the fact file**
(lines 292 to 301). Quote: "It prints a string as it stands and a list as
JSON. For a field with no value, it says so:" and the session lines
`["Lewis Carroll"]` and `subtitle: not set`. The writer took these from
`config_cli.py`. Neither facts-03 nor facts-B has any `get` output. Fix:
ask the editor for a captured `get` session, or cut the outputs. Keep one
sentence: "To read a field back, run `press config get` with the field's
name."

### Should

**S-1. Every fence is untagged** (17 fences, starting at line 23). The
ledger rules that every fence is tagged `text`. Fix: run
`tools/tag-fences.py` on the file.

**S-2. "Each `set` prints the change it makes to the file, which we leave
out."** (line 279). The fact file has no capture of `set` output, so this
is from the source and unsupported. Fix: cut the sentence, or ask the
editor for a capture.

**S-3. "If you add `--dry-run`, it prints the same change and writes
nothing."** (line 279). The facts mention `--dry-run` only as a flag
missing from `--help` (§20 A.23), with no behavior. Fix: cut it, or ask the
editor for a capture.

**S-4. Edition names appear before their gloss.** Quotes: line 70 "explains
what the Source edition needs from Git"; line 219 "the PDF, the EPUB, or
the Telegraphic edition"; line 498 "stitches the Manuscript edition, packs
the Source edition". The gloss arrives only at 579 to 581. The
vocabulary rule is to gloss once per chapter, at first use, with the format
in parentheses. Fix: at 70, "the Source edition (the source zip)". At 219,
"the Telegraphic edition (plain text)". At 498, "the Manuscript edition
(the stitched Markdown)". Then trim the later glosses to match.

**S-5. The In-this-chapter box no longer matches the A-head.** Line 13
reads "What Git has to do with it", and the A-head at 516 (mandated by the
brief) reads "What git has to do with it". Fix: line 13 becomes "What git
has to do with it". The B-head at 529, "What git gives the press", may
also take "Git" by the markup rule, because it is not mandated.

**S-6. The publish checklists cross-reference is wrong.** Line 589: "other
targets write the publish checklists that Chapter 13 describes." Brief 12
puts "Publish checklists" in Chapter 12, *The print pack* (its A-head 10).
Fix: "that Chapter 12 describes".

## Reading at the terminal

Steps in order: `press new` and `cd`, then `config set`, `validate`,
`press add`, `press all`, `ls dist/`, `wordcount`, and `git`. Each can be
run in the order given. The sentinel and page-floor commands are clearly
marked for later. Points for the editor, not counted:

- `press config validate` (Example 3.5): the reader has three config
  files. The facts do not say whether the command prints a line for an
  absent file, so the reader cannot predict three lines or six. A capture
  on the Alice state would settle it.
- `press wordcount` (line 506) is labelled "on a fresh scaffold". By then
  the reader has a chapter and two appendixes, so their output has four
  file lines and differs from the page. It is labelled honestly. A
  sentence ("yours now lists the new files too") would help.
- `press all` runs before `git init` (Example 3.9 before 3.10). The press
  quick start does the same, but the gallery capture was taken in a git
  checkout. §20 A.26 says the Source edition depends on tracked files, and
  that is still unverified. If the editor can capture `press all` in an
  untracked directory, either confirm the order or move Example 3.10
  first, as the README's `git init && make all` sequence does.
- `git push -u origin main` assumes the branch is `main`. Dev P5 said not
  to invent a step, so I leave it alone.
