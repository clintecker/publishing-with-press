# STE80 review: Chapter 14, Continuous integration and the release contract

File: `book/chapters/14-continuous-integration.md`
Diff: `git diff HEAD -- book/chapters/14-continuous-integration.md`, 10 lines (30, 74, 78, 144, 205, 281, 296, 319, 376, 379).

Status: REVISE. Blocks 0, should 1.

`press check` passes (exit 0). No code span, command, path, flag, key, quotation, identifier, or number changed in any hunk. No sentinel stands in this chapter. No touched paragraph is in Light mode or near the word cap (the longest, line 30, holds 96 words and six sentences). No blockquote, fence, or table rule moved.

## Findings

1. Line 205.
   Old: "The substitution of the image is the whole of the documented recipe."
   New: "The documented recipe changes the image and nothing else."
   What went wrong: "substitution" said that the recipe swaps one image reference for another (the paragraph above: "replace `:latest` with the value of the `image:` line"). "changes the image" can also read as "alters the image", and in a section whose point is that the digest fixes the image's bytes, that reading is false. The fidelity rule "Do not make words vaguer" applies. Strength is otherwise kept: "nothing else" matches "the whole of". The tension with the next sentence ("Chapter 2 also pairs the digest with the three-part press tag") is inherited from the old text, and the editor flagged it correctly. It is not a new defect.
   Severity: should.
   Corrected sentence: "The documented recipe replaces the image and nothing else."

## Edits checked and accepted

- Line 30, "puts the rule:" to "states the rule that" before the quotation. The quoted words are byte-identical ("if a book needs machinery, the machinery belongs here"), still inside the quotation marks, and their lowercase opening reads correctly after "that". Chapter 16 line 23 quotes the same words after "states the other half of the rule:", so the verb now matches the book's usage. Accepted. The joined first sentence ("short because of the first law of the press: the press states each fact once") makes explicit a link the old "for a reason" plus the next sentence already made. No fact added.
- Line 319, "so that" to "That way,". The old clause gave the purpose of moving the requirements pin. "That way," states the same purpose as a result of the step, at the same strength, with no modal added or lost. "For a new major" still governs the first sentence, and the second sentence depends on it, so the condition is not lost. Accepted.
- Lines 74, 144, 281, 379: plain splits at ", and". No fact or order changed.
- Line 78: "is built from two shell steps" to "has two shell steps". Same count, same referent (the composite action). Accepted.
- Line 296 (Table 14.3 cell): "Then it runs" keeps the order of the five actions. The table row is still one line. Accepted.
- Line 376: the added "from" before "the tag's name" only repeats the preposition. Both sources of the title stay. Accepted.
