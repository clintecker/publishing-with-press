# STE80 editor report: Chapter 11, The art department

File: `book/chapters/11-the-art-department.md`. Mode: Humanize for body
prose, the Tip, and list items. The one sidebar ("The five-percent box") was
read in Light mode and left unchanged.

## Ratchet count

- Baseline in `tools/ste-baseline.json`: 13.
- Before, from the first `--report` run: 13.
- Midway through this pass, `tools/ste-ratchet.py` changed under me. It now
  removes footnote markers and unwraps sidebars. Measured with the current
  tool, the untouched file scores 8 (four of the 13 were footnote merges, and
  one was the sidebar).
- After: 3, with the current tool. All 3 are declined false positives (see
  below).
- `press check`: passed (source, checker self-test, editorial, jargon).
- The full ratchet run reports one rise, in
  `book/chapters/14-continuous-integration.md` (2 -> 3). This desk did not
  touch that file.

## Edits (line numbers are from the original file)

1. Line 18, S1: "Press commissions each of these from an image model, takes the result into the book repository in a fixed house format, and refuses a delivery that would print badly." -> "Press commissions each of these from an image model and takes the result into the book repository in a fixed house format. It refuses a delivery that would print badly."
2. Line 22, S1/S2 (36 words, three ideas): "Each picture starts as a *commission*, a prompt for an image model that the book keeps in *art/commissions.md*, and press runs a commission only when you ask it to, and the build never does." -> "Each picture starts as a *commission*, a prompt for an image model that the book keeps in *art/commissions.md*. Press runs a commission only when you ask it to, and the build never does."
3. Line 22, S13 (seven sentences): split the paragraph at "You generate each image..." where the topic turns from what the art department is to where the art is made and who holds the keys.
4. Line 22, S1: "The toolchain image holds no keys, and the press never stores them, so a build on `printshop` can only use the files that `alice` committed from `hatter`." -> "The toolchain image holds no keys, and the press never stores them. A build on `printshop` can therefore use only the files that `alice` committed from `hatter`."
5. Line 69, S10 (phrasal verb): "and spells out each of the section's keys." -> "and states each of the section's keys."
6. Line 112 (Tip), S6 (passive, actor hidden): "Most options in this book are accepted but not listed." -> "The commands accept most of the options in this book, but the help does not list them."
7. Line 132, S2 (27 words): "It prints a single color on cream in three horizontal bands, with the title, the author, and a woodcut of the subject in the wide cream band." -> "It prints a single color on cream in three horizontal bands. The wide cream band holds the title, the author, and a woodcut of the subject."
8. Line 222, S5/S2 (31 words, three conditions): "The command refuses in three cases: when no image line in the manuscript declares the illustration, when the illustration is a data kind (`.chart` or `.diagram`), and when it has no `art:` directive." -> "The command refuses in three cases:" followed by a three-item list: "No image line in the manuscript declares the illustration." / "The illustration is a data kind (`.chart` or `.diagram`)." / "The illustration has no `art:` directive." The order is kept, so "The last refusal" in the next paragraph still points at the missing directive.
9. Line 254, S1 (29 words, a definition plus four actions): "*Intake* is what `press art accept` does to a delivered image: it converts the file to house format, ..." -> "*Intake* is what `press art accept` does to a delivered image. It converts the file to house format, ..."
10. Line 274, S13 (seven sentences): split the paragraph before "Intake checks no minimum pixel count and no DPI." The topic turns from where intake gets the trim to what intake does not check.
11. Line 292, S1 (28 words): "The mean luminance of the top edge and the bottom edge may differ by at most 45, and the same limit holds for the left and right edges." -> "The mean luminance of the top edge and that of the bottom edge may differ by at most 45. The same limit holds for the left and right edges."
12. Line 343, S2 (27 words): "For the upscale, the command looks for `realesrgan-ncnn-vulkan` or `upscayl-bin` on the `PATH`, then for */usr/local/bin/realesrgan-ncnn-vulkan*, and then for the binary inside *Upscayl.app* in */Applications*." -> "For the upscale, the command first looks for `realesrgan-ncnn-vulkan` or `upscayl-bin` on the `PATH`. Then it looks for */usr/local/bin/realesrgan-ncnn-vulkan*, and then for the binary inside *Upscayl.app* in */Applications*." The footnote stays on the Upscayl sentence.
13. Line 354, S10 (phrasal verb): "and it carries on." -> "and it continues."
14. Line 506, S10 (phrasal verb, ratchet lead): "5. Look at each candidate under..." -> "5. Examine each candidate under..."
15. Line 510, S2 (30 words, four-part list after a colon): "The press uses four models, which its code fixes as constants: `gpt-image-2` as the OpenAI flagship, `gpt-image-1` for transparency, `gemini-3-pro-image` as the Gemini flagship, and `gemini-3.1-flash-image` as the Gemini workhorse." -> "The press uses four models, which its code fixes as constants. For OpenAI, `gpt-image-2` is the flagship, and `gpt-image-1` is the model for transparency. For Gemini, `gemini-3-pro-image` is the flagship, and `gemini-3.1-flash-image` is the workhorse."
16. Line 525, S1 (two unrelated facts joined by "and"): "Each request goes from your machine straight to OpenAI or Google, and Gemini takes one request per image.[^11-imagen]" -> "Each request goes from your machine straight to OpenAI or Google.[^11-imagen] Gemini takes one request per image." The footnote marker moved to the sentence that its content (the endpoints) explains. The label is unchanged.

## Leads declined

- Line 64 (now 67), passive "is gilt": a false positive. "The ink is gilt" uses an adjective, not a passive.
- Line 83 (now 86), passive "are prompt": a false positive. "are prompt material" is a predicate noun.
- Line 340 (now 351), "-ing" form "substring": a false positive. The word is a noun.
- Line 291, 39 words, and line 303, sidebar 8 sentences (old tool only): both
  came from the old tool gluing a sentence to its footnote or reading the
  sidebar as one paragraph. The real sentences are all under 25 words. The
  sidebar is Light mode, and none of its sentences is over 30 words, holds
  three ideas, or has a semicolon.
- Sentences of 25 to 29 words left whole because a split would break a list
  or a condition from its result: line 18 (the list of four kinds of art),
  line 150 (the five-source precedence chain), line 274 ("because" clause
  with its cross-reference), line 294 (the two remedies after a colon), and
  line 320 (a fact and its "so" consequence).

## Passives kept

- Line 494: "a missing `GEMINI_API_KEY` stops the run only after the OpenAI images are paid for." Naming the payer would mean choosing between you, your account, and the press. The source does not say, and the sentence is about timing, not about who pays.
- Line 466: "when a feature is hidden": who or what hides the feature in the photograph does not matter.
- No other passive in the edited prose.

## Fidelity notes

- Edit 6: "Most options in this book" is now "most of the options in this book", and "not listed" names its actor as "the help" (the `--help` output that the sentence before it names).
- Edit 4: "can only use" is now "can therefore use only". The scope of "only" stays the same, and "therefore" carries the original "so".
- Sentinel phrases: none of the three appears in this file. Index terms: the edited sentences keep every term they had in its original spelling (intake, alpha master, logomark, commission, art target, art department, flat-ground test, luminance key).
