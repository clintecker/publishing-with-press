# STE80 editor report: Chapter 14, Continuous integration and the release contract

File: `book/chapters/14-continuous-integration.md`

Ratchet count: 3 before (the baseline then read 3, and the third lead was
the sidebar artifact described below). During this desk's run the
baseline file and the ratchet's prose filter changed under it: the
baseline now reads 2 and the sidebar lead no longer fires. After the
edits the count is 2, at the baseline. `press check` passes.
`python3 tools/ste-ratchet.py` passes (exit 0, no file rose).

Sentinels: none of the three stands in this chapter. Index terms: every
match string in `config/index-terms.yaml` that occurs in the chapter
occurs the same number of times before and after (75 strings compared).
Line count is unchanged (443), so the line numbers below hold for both
versions. ASCII only, no semicolons or dashes added, no fence, heading,
table rule, image line, art comment, or footnote label touched.

## Edits (10 lines)

1. Line 30, S1 and S2. Old: "The file is short for a reason. The first
   law of the press is that the press states each fact once. The way to
   build a book is a fact about the press, so it lives in the press, and
   the book refers to it by tag. A book that copied the build steps into
   its own workflow would hold a second copy of them, and that copy would
   go stale at the next release." New: "The file is short because of the
   first law of the press: the press states each fact once. The way to
   build a book is a fact about the press, so it lives in the press. The
   book refers to it by tag. A book that copied the build steps into its
   own workflow would hold a second copy of them. That copy would go stale
   at the next release." (The three-idea sentence and the 28-word sentence
   split. The first two sentences joined, so the paragraph holds six.)
   Same line, counter artifact: "puts the rule: "if a book needs
   machinery..."" became "states the rule that "if a book needs
   machinery..."". The counter split the paragraph at the colon before the
   quotation and counted seven sentences. The quotation is unchanged.
2. Line 74, S1 and S2 (26 words). Old: "The workflow pins it to the press's
   own immutable tag, and the release contract proves that pin, as the
   section ... describes." New: "The workflow pins it to the press's own
   immutable tag. The release contract proves that pin, as the section
   ... describes."
3. Line 78, S6 (passive). Old: "This one is built from two shell steps."
   New: "This one has two shell steps."
4. Line 144, S1 (27 words, two ideas). Old: "The elided block refuses any
   value that is not a lowercase target name followed by plain path and
   flag arguments, and it exits with status 2." New: "...followed by plain
   path and flag arguments. It exits with status 2."
5. Line 205, S8 (action in a noun). Old: "The substitution of the image is
   the whole of the documented recipe." New: "The documented recipe changes
   the image and nothing else."
6. Line 281, S1 (list item with two ideas). Old: "The workflow waits for
   them up to 60 times 30 seconds, half an hour, and the newest run of
   each name decides." New: "The workflow waits for them up to 60 times
   30 seconds, half an hour. The newest run of each name decides."
7. Line 296, S1 (Table 14.3 cell, five actions in one sentence). Old: "It
   rewrites `uses: clintecker/press@vX` in *build.yml* and `version =
   "..."` in *pyproject.toml*, runs `press selftest`, commits "Release
   vX", and pushes `main`." New: "It rewrites ... in *pyproject.toml*.
   Then it runs `press selftest`, commits "Release vX", and pushes
   `main`."
8. Line 319, S2 (27 words). Old: "For a new major, the maintainer also
   moves the requirements pin in the book template, so that a book
   scaffolded after the release names the new major." New: "For a new
   major, the maintainer also moves the requirements pin in the book
   template. That way, a book scaffolded after the release names the new
   major."
9. Line 376, S1 and S2 (28 words). Old: "For the Alice book, the release
   title is *Alice's Adventures in Wonderland v1.0.0*, from the `title`
   output of the build job's identity step and the tag's name." New: "For
   the Alice book, the release title is *Alice's Adventures in Wonderland
   v1.0.0*. The title comes from the `title` output of the build job's
   identity step and from the tag's name."
10. Line 379, S1 (Warning, three ideas). Old: "The build job runs and
    passes, and then the release job refuses the tag, so the release never
    appears." New: "The build job runs and passes. Then the release job
    refuses the tag, so the release never appears."

## Leads declined

- Lines 11 and 227, ing-form 'floating': both are the heading "Tags:
  floating and immutable" (line 11 is its entry in the In-this-chapter
  box). Headings are never touched, and "floating tag" is the
  vocabulary's fixed term.
- Line 320 (before), paragraph-length 7 in the sidebar "The release
  script that rewrote mypy": a counter artifact. The wrapper's `^>\s?`
  ate the newline of the bare `>` line and merged the `:::` fence and the
  bold title into the first paragraph, which holds five sentences. The
  sidebar is Light mode and has no sentence over 30 words, no three-idea
  sentence, and no semicolon, so it stands unedited. The lead no longer
  fires under the current ratchet.

Sentences over 25 words kept, each one idea or a list that a split would
break:

- Line 18 (27): the list of the later sections' three topics.
- Line 112 (25): one idea, the meaning of the sentence's second half.
- Line 164 (27): "The digest appears in two places: ..." (one list).
- Line 213 (24 plus the list): the twelve layers, in order.
- Line 363 (26): "rename the CHANGELOG section from 1.0.0 to 1.0.1,
  because the release job looks for the section that matches the tag".
  Two linked facts joined by "because", which the brief permits, and the
  paragraph already holds five sentences.
- Line 407 (27) and line 421 (27): a colon and a list of paths.

## Passives kept

- Line 60 and similar participles ("pinned by its full commit SHA",
  "a one-package change made with ...", "a book scaffolded after the
  release"): adjectival participles, not finite passives. The actor
  is named nearby or does not matter.
- Line 175, "Broken at its punctuation, with the 64 digits of the digest
  split into two lines of 32": describes the display of the value, and
  the actor (this book's typesetting) does not matter.

## Fidelity notes

- Edit 5: the old sentence said the image substitution is "the whole of
  the documented recipe", and the next sentence says Chapter 2 "also"
  pairs the digest with the three-part tag. The new sentence keeps the
  same claim at the same strength and the same tension with "also". I
  did not resolve it.
- Edit 8: "so that" (purpose) became "That way," (purpose stated as a
  result). I read the two as the same claim.
