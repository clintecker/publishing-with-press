# Cut report: Chapter 11 (book/chapters/11-the-art-department.md)

Every entry in docs/briefs/cutting-brief.md that names Chapter 11.

## Changes

### Part 1, retold facts

1. `11:67-69`, the shallow merge (keeper Chapter 9).
   Before: "The merge is shallow at the top level. The press copies the house
   file and lays each top-level section of the book's file over it, whole."
   plus the paragraph "Suppose the Alice book writes a `cover:` section with
   only a `style:` key in it. ... "restate a whole section when you touch
   it"."
   After: "The merge is shallow: a section the book names replaces the whole
   house section (Chapter 9), so Example 11.1 restates every key." (The
   second paragraph is cut.)
2. `11:316`, Lulu's preflight (keeper Chapter 12).
   Before: "The print vendors are the reason. Lulu once flagged a book's
   logomark for its transparency, and for its resolution of over 600 PPI, so
   the pass now flattens each of those images and caps its resolution."
   After: "The print vendors are the reason (Chapter 12)."

### Part 2, tics

3. `11:63` Before: "Its register gives the idea in three sentences:"
   After: "Its register:"
4. `11:320` Before: "The scars list puts it plainly:"
   After: "The scars list says:"

No "fit the page" aside exists in this file.

### Part 3, closers

5. `11:57` cut, ends earlier. "Step 7 matters more than it looks." cut. The
   paragraph now begins "The CI build on `printshop` reads only committed
   files".
   Kept as the chapter's two: `11:24` and `11:444`. All "leave" entries left.

### Part 4, the block and the shoulds

6. `11:383-410`, Example 11.3: the four inner closing fences (then lines 388,
   397, 403, 409) changed from ` ```text ` to ` ``` `. Outer fence and prompt
   text unchanged.
7. `11:22` Before: "and press runs each commission once."
   After: "and press runs a commission only when you ask it to, and the
   build never does." The brief's wording has a semicolon ("ask it to; the
   build never does"), which the cutter rules forbid in prose, so it is
   joined with ", and".
8. `11:106-111`, after the `press cover` synopsis, added the Chapter 3 Tip
   (Part 4's `03` entry, as Chapter 3 sets it at `03:40`):
   "::: {.tip} > **Tip:** `press <command> --help` prints the argument
   grammar only. Most options in this book are accepted but not listed.
   Appendix A marks each one. :::"
   Chapter 3's "The options in this table, and most options in this book"
   became "Most options in this book", because no table follows the synopsis
   here.

## Words

7534 before, 7478 after (`wc -w`).

## Declined or flagged

- None declined.
- Flag: entry 1's fix ends "so Example 11.1 restates every key", and the
  next paragraph (unchanged, `11:71` in the old numbering) still ends "and
  restates every key in it." The repeat is harmless, so I left it. The
  coordinator may want to drop ", and restates every key in it" from that
  sentence.
- Part 5 protects no Chapter 11 passage.

## press check

`~/code/.pwp-venv/bin/press check` exit 0: source, checker self-test,
editorial, and jargon checks passed.
