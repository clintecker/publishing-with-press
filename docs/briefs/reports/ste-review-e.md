# STE80 review: Appendix E, Glossary

File: `book/appendices/e-glossary.md`. Diff: `git diff HEAD -- book/appendices/e-glossary.md` (14 hunks, all read).

Status: **REVISE**. Blocks: 0. Should: 1.

1. **Line 213, frontispiece (Terms; should).**
   - Old: "on an even page, facing the chapter that follows"
   - New: "on an even page, opposite the chapter that follows"
   - What went wrong: "facing" is not a gerund here; it names the bookmaking relation of a verso to its recto, and the chapter that owns the term uses it. Chapter 5 says the frontispiece takes an even page "so it faces the chapter that follows" (table, line 163) and that it "sits on the verso of an opening and faces the chapter title on the recto" (line 187); facts-E item 31 says "a plate on a verso facing a chapter opening". "Opposite" is looser (it does not say the two pages form one opening) and puts the glossary out of agreement with Chapter 5. The S8 lead should have been declined, or resolved with the chapter's own verb.
   - Corrected: ": The *placement* that gives an illustration a cleared leaf (see *leaf*) on an even page, so it faces the chapter that follows (Chapter 5)."

## Hunks checked and passed

- Line 21, appendix file: the new rule "starts with one lowercase letter and a hyphen and ends in `.md`" is exactly the glob Chapter 3 states, `[a-z]-*.md` (line 382: "a single lowercase letter, a hyphen, and anything ending in `.md`"). "The rest" was the glob's `*`; "starts with ... ends in" carries it, and the entry now parallels *chapter file* (line 75). No fact lost.
- Line 210, front matter: naming press as the actor agrees with Chapter 10 ("The press generates two parts inside the book ...", line 22). The old participle was already unconditional, so the edit neither adds nor drops the conditions in Table 10.5.
- Line 474, sources companion: agrees with Chapter 1 line 270 ("The press generates *alice-sources.md*") and Chapter 10 line 388 ("a Markdown file that the press publishes beside the book") and with the vocabulary ("the generated `dist/<slug>-sources.md`").
- Lines 12, 153, 168, 171, 237, 321, 327, 375, 438, 480: structure only. Each actor named is the one the owning chapter names (the desk derives evidence states, Chapter 15 line 103; the press draws the EAN-13, Chapter 12 line 231). The migration hunk keeps "first ... afterward" order. No code span, path, command, identifier, number, or head term changed; no sentinel occurs in the file; no paragraph approaches 190 words; definition-list markup is intact.
