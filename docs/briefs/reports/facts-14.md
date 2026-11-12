# Fact check: Chapter 14, Continuous integration and the release contract

File checked: `book/chapters/14-continuous-integration.md` (448 lines), against
`docs/briefs/facts/facts-14.md` (§12.1–12.7, §16.6, shared context, §19, §20).
Not committed.

**Status: needs fixes.** Contradicted 0, Unsupported 12, Drifted 11, Missing 3.

## Two questions the desk was asked to judge

- **SHA pins versus `uses: clintecker/press@v3.0.2`.** The file says "Every
  action is pinned to a 40-hex commit SHA" (§12.3) and also shows
  `uses: clintecker/press@v3.0.2` (§12.3, build step 2). Resolution:
  third-party actions are pinned by commit SHA, the press's own action is
  pinned to its immutable three-part tag, and the release contract's pin check
  ("build.yml must contain `uses: clintecker/press@${tag}`", §12.5) proves that
  the tag pins itself. The chapter is correct against this. L72 limits the
  SHA claim to "the checkout action and every other outside action", and L64
  and L230 state the self-pin with the contract as the guard. No finding.
- **The release state order** (pushed, tagged, built, verified, contract
  proved, floating tag moved, published). Checked against the §12.5 table.
  Step 1 commits and "pushes main". Step 2 pushes the three-part tag. Step 3
  waits for the `contract` check, and that check (release-contract.yml steps
  1–4) checks the pins and the image, waits for `quality`/`consumer`/`desk` on
  the tag's SHA ("the newest run of each name decides"), and assembles the
  receipts. Step 4 floats `vN`. Step 5 publishes. So the order is right, and the
  writer was right to deviate from the brief's "verified before tagged". Two
  detail findings on Figure 14.2 are in Drifted (D3).

## 1. Unsupported (blocks)

1. L18 "a machine that keeps nothing of yours between runs" and L38 "GitHub
   gives `printshop` a fresh machine for each run ... and throws the machine
   away at the end." Searched for: fresh, ephemeral, runner lifetime. The file
   gives only `ubuntu-24.04` and the pinned container (§12.3). Fix: cut, or
   reduce to "The build job runs on `ubuntu-24.04` inside the toolchain image".
2. L68 "The reader site already travels in *dist/* as *alice-site.zip*, the
   Chapter edition (the reader site and its zip)". Searched for: site.zip,
   reason for excluding `dist/site`. facts-14 says only "upload `dist/*` except
   `dist/site` and `dist/pages`" (§12.3 step 4). The zip's name and the reason
   for the exclusion are not in it. The appositive also reads as though the zip
   alone were the Chapter edition. Fix: cut the reason, or keep it only as a
   cross-reference to the chapter that has the fact (Ch. 9 Table 9.6 lists
   `-site.zip`), and quote the file: "upload `dist/*` except `dist/site` and
   `dist/pages`".
3. L72 "A tag on another repository can move, and a moved tag would run new
   code on `printshop` with the book's token." The file gives no rationale for
   SHA pins except "because GitHub has no ruleset for it" (§12.3). Fix: soften
   to the general point without "with the book's token" (the build job's token
   is read-only, L44), or cut.
4. L76 "A composite action is a GitHub action built from shell steps, with no
   container or JavaScript of its own." Not in the file, and only partly true
   in general: composite steps may also `uses:` other actions. Fix: "This one
   is built from two shell steps" (true of the verbatim action.yml, §12.2).
5. L117 "because Debian manages the Python inside the image, as Chapter 2
   ... explains". The reason is not in facts-14, and the image is
   `FROM ubuntu:24.04` (§12.4). Fix: cut the reason, or keep the
   cross-reference and say Ubuntu (see D1).
6. L181 "When a reference carries both a tag and a digest, Docker pulls by the
   digest and ignores the tag." Searched for: tag plus digest, pull semantics.
   The file says only "a digest pins bytes" (§19 design rationales) and the
   contract quote. Fix: soften to the file's wording: "The `sha-` tag is
   mutable; a digest pins bytes".
7. L187–204, Example 14.4 (the CI-exact local build): `git show
   v3.0.2:.github/workflows/build.yml | sed -n 's/^ *image: //p'`, then
   `docker run ... pip install --break-system-packages 'press @
   git+https://github.com/clintecker/press@v3.0.2' && cd /book && press all`.
   None of this recipe is in facts-14, and it is presented as working with no
   capture behind it. Untested risks: whether `sed` catches exactly one
   `image:` line; git in the container refusing a bind-mounted repo owned by
   another uid ("dubious ownership"), which the source edition needs; and a
   root-owned `dist/` on a Linux host. Fix: run it on a real book and paste the
   capture, or cut it to the prose instruction the file supports: "replace
   `:latest` with the image line of *build.yml* at the tag you pin". This is
   the worst finding (see below).
8. L216 "which you can download from the release contract's run for a tag in
   the press repository". The file says only "It uploads `release-receipt`"
   (§12.5 step 5). Workflow artifacts expire, so the instruction may fail for an
   older tag. Fix: cut the download clause, or hedge it.
9. L318 "which goes through the same checks as any other commit". Not in the
   file. `main` "takes direct pushes by design (#153). The checks are enforced
   at the release boundary" (§12.5). Fix: "a separate change to build.yml"
   (the file's words) and stop there.
10. Sidebar L323: "in a file that every later release commit touched again",
    and "The pattern is now anchored, so it matches only a line that begins
    with `version`." The file has "once rewrote [tool.mypy]'s
    python_version" and "It is now anchored, with `count=1`" (§19.19; §12.5
    step 1). It does not have the later-commits consequence or the kind of
    anchor. Fix: cut the first clause, and make the second "The pattern is
    now anchored, and it runs with `count=1`".
11. L330 "That value changes two things in `press all`. The press demands its
    *release witnesses*, at least two sentinels and a `verify-min-pages` of 24
    or more ... The commerce gate also stops advising and enforces its
    findings", and Tip L345 ("two sentinels and a page floor of 24"). Searched
    for: PRESS_RELEASE effects, sentinel count, 24. facts-14 has only the
    expression that sets PRESS_RELEASE (§12.3) and "the commerce release gate
    (ordering-enabled books only)" (§20 B.13). The numbers and the claim of
    exactly "two things" are not in it. Fix: make sure the numbers match
    Chapter 6's fact file. Here, cut "two things" to "The value turns on the
    release checks that Chapter 6 ... describes", and soften the Tip to match.
12. Pages section, L364, L372, L376. The Alice title *Alice's Adventures in
    Wonderland* (L364); the bundle contents "the landing page, a copy of the
    reader under *read/*, and every download under *downloads/*. With
    `site-url` set, it also has a sitemap and a *robots.txt*" (L372); the
    verifier "checks that every local reference in it resolves" (L372); "GitHub's
    Pages deploy needs `pages: write` and `id-token: write`" and "set Source to
    GitHub Actions" (L376). None of these is in facts-14. The file has only
    `${SITE_URL}/downloads/<name>` (§12.3), the four permissions (§12.1),
    and "the actual site was crawled" (§1.4 law 3). Fix: keep them as plain
    cross-references to Chapters 1, 3 and 8 without restating the details, or
    have them checked against those chapters' fact files.

## 2. Contradicted (blocks)

None. The chapter handles the relevant §20 items correctly:

- A.2: it uses the digest wording, not "an existing immutable `sha-` tag".
- A.14: L183 says the release notes do not carry the digest, and the receipt does.
- B.21: Example 14.5 is shown as a plan that proposes a v4 that does not
  exist, with "Do not apply this plan", not as a feature.
- A.9: Tip L345's "fresh book's draft settings ... fail on the first tag"
  agrees with the template's `verify-min-pages: 1`.

## 3. Drifted (should)

1. L117 "Debian manages the Python inside the image". The file says
   `FROM ubuntu:24.04` (§12.4). Fix: "Ubuntu".
2. L161 "The digest appears in one place that you can read: the `image:`
   line", then L183 "The release receipt also names the digest". The chapter
   disagrees with itself, and the file has both (§12.3; §12.5 "The terminal
   release receipt names ... the pinned toolchain digest"). Fix: "The easiest
   place to read the digest is the `image:` line ...".
3. Figure 14.2 directive (L307). (a) "The reader should see first that no fail
   arc leaves after 'floating tag moved'" says that step 5 (`gh release`)
   cannot fail. The file says "rerunning after any failure is the recovery
   procedure" (§12.5). Fix: give "release published" a fail arc into a
   rerun (with `v3` already moved), or reword the directive to "no fail arc
   after the float leaves `v3` unmoved". (b) The "built (quality, consumer,
   desk)" gloss puts the check runs after "tagged". The file says the contract
   *waits for* those check runs "on that SHA" (§12.5 step 3). It does not say
   that the tag starts them, and release.sh pushed that SHA to main in step 1.
   Fix: gloss "checks found" or "checks awaited" rather than "built".
4. L290 "Its own description is 'the one release path and a resumable state
   machine'" and L311 "The script's notes say that 'rerunning after any
   failure is the recovery procedure'". The file does not attribute these to
   the script. They sit with the CLAUDE.md "contract" material (§12.5). Fix:
   "The press's guide calls it ...".
5. L313–315 runs `scripts/release.sh v3.0.2`, a tag that is already released.
   The file writes `scripts/release.sh vN.x.y` and `--check-tag vN.x.y`. Fix:
   use `vN.x.y`, or a hypothetical next tag marked as such.
6. L359–361 the CHANGELOG message is shown with a literal `$version`. The file
   gives the source string `no CHANGELOG section for $version; roll
   [Unreleased] before tagging` (§12.3). A reader's run prints the version
   instead. It is also folded. Fix: say that `$version` stands for the tag's
   version, and give it on one line, or say plainly that it is the template.
7. Example 14.5 is folded at seven places. The brief allows only the slug
   change and elision with `...` in a captured block, so the block does not
   match the §12.6 capture character for character. The `$ press migrate`
   prompt line is also an addition (the file does not show the command,
   although `press migrate` is the plan per §12.6). Fix: elide the long tails
   with `...` instead of folding, or get the folding approved as a house
   exception. The same applies to item 6.
8. L286 "the wheel with the `tui` extra runs it headless". The file says "the
   tui wheel runs it headless" (§12.7). Fix: "the tui wheel", unless another
   fact file names an extra.
9. L44 "Its own comment gives the reason". The file gives the quote
   without naming a comment (§12.3). Fix: "The workflow states the reason".
10. L444 "*book.yml* still resolves to `v3.0.2` and its digest". This is a
    version claim with no "at the time of this writing" (L232 has the hedge,
    and this line does not). Fix: add it.
11. L141–147 "For the input `all && rm -rf dist`, the refusal reads:". The
    lines are the script's echo strings with an illustrative value
    substituted, not a capture (writer's report). Fix: "would read", so the
    block is not taken as captured output.

## 4. Missing (may)

1. The toolchain image has been public since 2026-07-20 (#161): "a book under
   any account pulls it with no package grant and no configured secret"
   (§12.4). L181 says it is public but gives no date or issue. Add "at the
   time of this writing" or the date.
2. §20 B.19: "The Dockerfile installs PyYAML (unused) and unpinned Pillow. The
   action reinstalls from the hash lock anyway." This belongs next to Example
   14.4's caveat (L204). A local build in the image starts from the image's
   unpinned Pillow, which supports the chapter's own warning that local
   dependencies can differ.
3. The release contract's pin pattern needs the `sha-` tag *and* the digest
   (`press-toolchain:sha-…@sha256:<64 hex>`, §12.5). So a digest-only image
   line also turns the contract red. L284 explains only the missing-digest
   case. One clause would stop a reader from "simplifying" the image line to
   the digest alone.

Note, outside the lists: L378 says every tagged release "points at downloads
that a push to `main` deploys". Given `${SITE_URL}/downloads/<name>` (§12.3), a
release's links serve whatever `main` deployed last, not the tagged bytes. The
file does not say this either way. Consider a hedge.

## Code blocks against captures

- Example 14.1 (action.yml head and install step): matches §12.2 apart from
  the declared elisions. OK.
- Example 14.2 (run step): matches §12.2 with the comment and the validation
  block elided. OK.
- Example 14.3 and the broken-out image value: the `sha-0a3a99d6...a026` value
  and the digest `0d784ac0...2ca04` match §12.3 exactly. OK.
- The regex at L141 and the pin regex at L395: verbatim. OK.
- `no migration to roll back (no .press/migration-backup.json)`: verbatim. OK.
- The CHANGELOG message: folded (D6).
- Example 14.5: folded and has a prompt added (D7). Otherwise every token
  matches §12.6.
- Example 14.4: no capture exists (U7).

## Worst finding

U7, Example 14.4. It is a runnable recipe for a CI-exact local build, and none
of it is in the fact file: the `git show | sed` digest extraction, `docker run`
with a bind mount, and pip-from-git inside the container. It was never captured,
and it has plausible failure modes (git ownership checks in the container, the
`sed` match, root-owned output). Prove it with a real run or cut it to the
supported instruction.
