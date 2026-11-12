# Re-review: Chapter 14, Continuous integration and the release contract

File: `book/chapters/14-continuous-integration.md` (437 lines, revised, 5,633 words).
Against: `facts-14.md`, `dev-14.md`, `copy-14.md`, `type-14.md`, the Revision
section of `report-14.md`, facts-14 S1 and S2, the production ledger, and the
two rulings for this pass (a new three-part tag after a refused first tag; one
sentence on the Actions tab). Not committed. The chapter was not edited.

**Verdict: REVISE.** Open: 1 blocks, 1 should (2 items). Both are one-sentence
fixes. Everything else is resolved or declined for a reason that holds.

## Checks run

- `press check`: fails on two Chapter 12 plates (`12-01-cover-wrap-anatomy.png`,
  `12-02-spine-math.png` never referenced). Neither names this file. No other
  message.
- `tools/ste_check.py`: 28 findings, 426 sentences, average 11.7, max 51 (the
  index comment). All are accepted classes (verbatim quotations, "therefore",
  -ing in terms and titles, the three art directives, the index comment) except
  line 413, a real paragraph of seven sentences (open item 2). The writer's
  report says paragraph length fires only on the art directives. That is not
  so.
- Fences: 12 opened, all `text`. No line inside a fence over 64 columns.
- Figure files: `14-01-ci-topology.png`, `14-02-resolving-v3.png`,
  `14-03-release-state-machine.png` all exist. The image paths match, and
  `#fig:resolving-v3` (14.2) and `#fig:release-state-machine` (14.3) now agree
  with the order of appearance. Every `art:` comment follows its image line
  after one blank line (lines 34/36, 235/237, 306/308).
- Footnotes: `14-pillow`, `14-main`, `14-macos`, `14-migrate`. Each is
  referenced once and defined once.
- Spelling: no "centre", "cancelled", "half way", "labelled", "colour".

## Findings table

| Desk | No. | Sev. | Status | Note |
|---|---|---|---|---|
| Fact | U1 | blocks | resolved | Fresh-machine claims cut. L38 is the file's wording. |
| Fact | U2 | blocks | resolved | site.zip reason cut. L63 quotes the step. |
| Fact | U3 | blocks | resolved | Moved-tag and token rationale cut (L74). |
| Fact | U4 | blocks | resolved | "This one is built from two shell steps" (L78). |
| Fact | U5 | blocks | resolved | Ubuntu 24.04, kept as a Chapter 2 cross-reference (L122). |
| Fact | U6 | blocks | resolved | Docker pull semantics cut. The digest pins bytes (L160). |
| Fact | U7 | blocks | resolved | Example 14.4 is S1's recipe with the `image:` value substituted and elided (`sha-...@sha256:...`), pointing back to Example 14.3. No `git show \| sed`. The only other change is a declared line break inside the double quotes, and bash removes it. |
| Fact | U8 | blocks | resolved | Download clause cut (L217). |
| Fact | U9 | blocks | resolved | "a separate change to *build.yml*" (L319). |
| Fact | U10 | blocks | resolved | Later-commits clause cut. "anchored, and it runs with `count=1`" (L326). |
| Fact | U11 | blocks | resolved | "The value turns on the release checks". The floor numbers are admissible under S2 (L333, L336). |
| Fact | U12 | blocks | resolved | Bundle contents are admissible under S2 (facts-01 3.5). The verifier and permission claims are cut, and the Pages setting is reduced to a Chapter 3 cross-reference (L384, L388). The title at L376 is the Alice book's metadata (facts-01/04/10). |
| Fact | D1 | should | resolved | Ubuntu. |
| Fact | D2 | should | resolved | The digest is in two places, the pin and the receipt (L164). |
| Fact | D3 | should | resolved | "release published" has a fail arc into "stopped". "built" is glossed "checks run on the release commit", which matches the fact file's "on that SHA" and is an acceptable form of "checks awaited". |
| Fact | D4 | should | resolved | Both quotes are credited to the maintainer's guide (L291, L312), glossed once at L30 as the press's *CLAUDE.md*. |
| Fact | D5 | should | resolved | `v3.0.3`, labeled as a next release (L312). |
| Fact | D6 | should | resolved | The CHANGELOG message is now prose with no `$version` and no fold (L374). |
| Fact | D7 | should | resolved | Example 14.5 is cut. The new refusal block (L357) is shortened only with `...`. |
| Fact | D8 | should | resolved | "the tui wheel" (L287). |
| Fact | D9 | should | resolved | "it states the reason" (L44). |
| Fact | D10 | should | resolved | Hedged (L433). |
| Fact | D11 | should | resolved | "would read" (L144). |
| Dev | P1 | should | resolved | One sentence on the Actions tab (L351), as ruled. The two runs from one push are explained (L353). |
| Dev | P2 | should | **open (blocks)** | The refusal is shown and a new tag is advised, as ruled. The recovery as written fails a second time. See open item 1. |
| Dev | P3 | should | resolved | The `--require-hashes -r` line is in Example 14.1 (L101 to L102). |
| Dev | P4 | should | resolved | Pointer to "Release builds" (L66). |
| Dev | P5 | should | resolved | The receipt paragraph defers to the release contract section (L217). |
| Dev | P6 | should | resolved | B-head "The press's tag grammar", the caption "The press's own release tag grammar", and "Your book's CI treats any tag that starts with `v` as a release" (L251 to L263). |
| Dev | P7 | should | resolved | L390 claims only the link form and the attached *dist/* files. |
| Dev | P8 | should | resolved | The appositive is gone. |
| Dev | R1 | should | resolved | The guard is down to one sentence plus the refusal (L144 to L152). The regex walk-through and the `read -r -a` paragraph are gone. |
| Dev | R2 | should | resolved | The reason appears once (L112). The warning is the instruction only (L115). |
| Dev | R3 | should | resolved | "Release builds" now carries a release-day B-head, the two runs, the refusal, and recovery. |
| Dev | N1 | should | resolved | Example 14.5 is gone. "The plan" (L411 to L413) describes the plan in prose and does not name v4. L409's "always the current major plus one" is fact 12.6's rule, not the B.21 capture. |
| Dev | N2 | should | resolved | The files are renamed to the order of appearance (14-02 resolving, 14-03 state machine), and the paths and slugs agree. The brief and the design row still name the old files. That is for the managing editor. |
| Copy | 1 | blocks | resolved | The bold-label list is a plain list, each step led by its subject (L279 to L283). |
| Copy | 2 | should | resolved | "the Alice book" (L18). |
| Copy | 3 | should | resolved | One name for the press's *CLAUDE.md*: "the maintainer's guide" after the gloss at L30. |
| Copy | 4 | should | resolved | "contract" is kept for the release contract (L160, L229, L231, L249). |
| Copy | 5 | should | resolved | "the container registry", glossed with *ghcr.io* (L32), also in the art directive and the alt text. |
| Copy | 6 | should | resolved | "upload bundle", defined once (L54), used at L50, L64, L282, L283, L353, L386. |
| Copy | 7 | should | resolved | *release contract* is defined in italic at first use (L217). |
| Copy | 8 | should | resolved | `press selftest` (L253, L296, L423). |
| Copy | 9 | should | resolved | "floating tag" (L267, L270). |
| Copy | 10 | should | resolved | "Two jobs" (L386). |
| Copy | 11 to 13 | should | resolved | No perfect tense at the cited places. |
| Copy | 14 to 16 | should | resolved | Each sentence is split. |
| Copy | 17 | should | resolved | The sentence is cut along with U1. |
| Copy | 18 to 20 | should | resolved | "you" (L225, L249, L394). |
| Copy | 21 | should | resolved | The tip is above the procedure (L335). |
| Copy | 22, 23 | should | resolved | "halfway", "canceled", and "Center" (may 41). |
| Copy | 24 | should | resolved | The sidebar is two paragraphs. |
| Type | 1 | should | declined-accepted | The caption sat at a page foot. There is no source fix, and the text before it reflowed. Recheck Example 14.4's caption and fence at the next PDF build. |
| Type | 2 | should | resolved | The two pip lines are broken with a declared backslash (L80, L99 to L105). The digest is split 32/32 with the sentence saying so (L175 to L182). This covers all three 64-column lines. |
| Type | 3 | should | resolved | The files are renamed (see N2). |
| Type | 4 | should | resolved | The state machine is in two snaking rows, four over three (L308). |
| Re-review | new | should | **open** | L413 has seven sentences. See open item 2. |

## Open items

### 1. The recovery tag has no CHANGELOG section (blocks; completes Dev P2)

Quote (L363): "A tag names one commit, so the fixed commit needs a tag of its
own, such as `v1.0.1`. Push it, and the tag run starts again from the
beginning."

The author made a `1.0.0` section in step 1 (L343). The release job extracts
the section headed `## [version]` for the tag, "If the section is missing,
the job stops" (L374; fact file 12.3, release job step 2). So `v1.0.1` with
only a `[1.0.0]` section passes the build job and then stops in the release
job. An author who follows the chapter on release day fails twice. The chapter
contradicts its own L374.

Fix (keeps the ruled new-tag advice): "To recover, set two sentinels and the
page floor with `press config set`, as Chapter 3 shows. Rename the CHANGELOG
section to 1.0.1, and commit both changes on `main`. A tag names one commit,
so the fixed commit needs a tag of its own, `v1.0.1`. Push it, and the tag run
starts again from the beginning."

### 2. A paragraph of seven sentences (should)

Quote (L413): "The plan begins with the major the book pins ... The last line
of the plan repeats the rule of the dry run." The paragraph has seven
sentences, against a limit of six, and "also" appears twice in a row ("It
also says ... The plan also names ...").

Fix: break the paragraph before "The plan also names any override", and drop
that sentence's "also": "The plan names any override that the design profile
does not govern: ..."

## Read as the author on release day (not counted)

The section works. The tip comes first, then the three steps, then where to
watch, then what the two runs do, then the refusal and the way back. Apart
from item 1, the release-day path is sound. These mays are not counted:

- L353, last sentence ("The tag run builds the same commit, with the release
  checks turned on.") repeats the sentence before it. Cut it.
- L355 cites Example 6.11, which shows `N`. Chapter 3's Example 3.3 shows
  exactly the `0` and `1` values printed here, so "Example 3.3 in Chapter 3"
  would be the closer citation.
- Example 14.4 installs `press@v3`, and the tip right after it (L208) says to
  read the digest at the exact three-part tag you install. L205 tells the
  reader to use `v3.0.2` in place of `v3`, so this is consistent, and S1
  allows only the image substitution inside the example. A reader may still
  stumble on it. Leave it as it is, or move the sentence at L205 ahead of the
  example.
- Sidebar L324: "the table's `python_version` setting contains the text
  `version = "` as well" is derived from the string itself, not quoted. It is
  true by inspection, so it is accepted.
