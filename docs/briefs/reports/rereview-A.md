# Re-review: Appendix A, Command reference

File: `book/appendices/a-command-reference.md` (1,351 lines), re-read
against my report `docs/briefs/reports/facts-A.md`. I checked the blocking
items (Unsupported 1-2, Contradicted 1-6) and Drifted 1-13. Nothing was run
that costs money; I made no edits and no commits.

**Verdict: APPROVED.** Every blocking item and every Drifted item is
resolved. One small note remains, and it does not block.

## Mechanical checks

- Headings: every `##` line ends in ` {-}` (no `###` headings exist).
  `grep -n '^##' | grep -v ' {-}$'` printed nothing.
- Fences: no line inside a fenced block, and no fence line, is wider than 64
  columns (an awk scan over the fenced blocks printed nothing).

## Blocking items

| Item | Status | Where |
|---|---|---|
| U1 candidate `ls` output | Resolved: the `ls` is cut; l.161 now reads "A second run adds new candidates and never overwrites the first ones." | l.161-168 |
| U2 coloured code block | Resolved: the claim is gone; l.1246 says "color on any page makes the verifier refuse the interior". | l.1246 |
| C1 `--front` chapter | Resolved: "*book/chapters/00-<name>.md*, an unnumbered chapter before the numbered ones". | l.31 |
| C2 `press source`, no Git | Resolved: both cases are stated, and the session shows `archived 14 files; ...`, which matches my rerun outside Git. | l.1106-1116 |
| C3 print-safe advice (20.B.2) | Resolved: the two sentences are cut. | l.932-941 |
| C4 lookup "the one command" | Resolved: "It reaches the network, as `press cover`, `press illustrate`, `press art commission`, and `press research` do". | l.729 |
| C5 selftest "one line" | Resolved: "It prints its progress and ends with one success line"; the session now has `...` before that line. | l.1033, 1045-1050 |
| C6 doctor broken optional tool (20.B.14) | Resolved: the sentence is cut. | l.512 |

## Drifted items

1. Wrapping: resolved. Line 15 now states the convention ("where a line of
   output is wider than the page we break it and indent the rest by two
   spaces"), and every wrapped session follows it (art accept, A.1, A.2,
   config list, desk, migrate, A.7, selftest, verify, A.8, pdf, A.9, source).
2. coverwrap message: resolved, `coverwrap needs assets/cover.jpg (the front
   board art)` (l.471).
3. colored-ink message: resolved, `print profile: colored ink on pages
   [...]`, followed by advice about the title page (l.1246).
4. Unknown command: resolved, "and then press names the nearest command it
   knows, when there is one" (l.13).
5. Appendix `--front`: resolved, "it counts up from `a-`" (l.31).
6. Chapter number: resolved, "the number after the highest one in use"
   (l.25).
7. art commission flags: resolved, `--model`, `--count`, and `--photo` are
   each marked "Not listed by `--help`" (l.151-153).
8. Example A.9 path: resolved, `.../alice/...` with the path unbroken
   (l.1303-1306).
9. skills tab: resolved, "A tab separates the name from the path, shown here
   as spaces." (l.1088).
10. cover aspect: resolved, "the ratio of the legacy `trim` field (6 by 9
    unless set), not the profile's", hedged "At the time of this writing"
    (l.118).
11. gradient refusal: resolved, "an opaque single-ink plate" (l.112).
12. `press all` and print: resolved, "unless print ordering is on, when the
    c[ommerce gate builds them]" (l.86).
13. `config list --json`: resolved, "its choices, and its manager" (l.297).

## Note (does not block)

- l.1106: "an empty archive ("zipfile is empty")". Press does not print
  that phrase. It is `unzip -l`'s warning on the empty file; my rerun
  inside a parent repository confirms both the warning and press's own
  `archived 0 files` line. Suggested: "...gets an empty archive (`archived 0
  files`, with a `skipped ... (untracked; publication is for committed
  work)` line per file)". Another option is to say that `unzip -l` reports
  the zipfile is empty.
