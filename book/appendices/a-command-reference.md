# Appendix A: Command reference {.unnumbered}

This appendix describes every command in press's catalog in alphabetical order, as press 3.0.2 has them at the time of this writing. Each entry has the shape of a Unix manpage. It gives a synopsis, a description, the options, a short session on the Alice book (the book's sample, slug `alice`), and the chapter that explains the command in full. In a synopsis, `[ ]` marks an optional part, `|` separates alternatives, and `...` marks a part you may repeat. A word in angle brackets is a value you supply.

Every command also takes `--help` (or `-h`), which prints the command's synopsis and one-line summary from the catalog and then exits. The three global forms are these:

```text
press <command> [arguments]
press <command> --help
press --version
```

`press --version` prints `press 3.0.2`. A bare `press` prints the usage and exits with status 2. A command name press does not know does the same, and then press names the nearest command it knows, when there is one. A few options exist in the code but not in the grammar that `--help` prints. Their entries list them and say "not listed by `--help`".

The sessions run in *~/alice* on `hatter`, and a line of only `...` stands for output we cut. A line that starts with `+` echoes a program press runs. We shorten the long ones, and where a line of output is wider than the page we break it and indent the rest by two spaces. The module command lines for contributors, such as `python3 -m press.receipts`, are not `press` commands. This appendix leaves them out.

## press add {-}

**Synopsis.**

```text
press add chapter|appendix <name> [--front]
```

**Description.** Creates a chapter file in *book/chapters/* or an appendix file in *book/appendices/*, with a heading and a placeholder paragraph. A chapter takes the number after the highest one in use, padded to at least two digits, and an appendix counts down from `z-`. Press refuses to overwrite a file that exists, with exit status 1.

**Options.** Table A.1 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--front` | With `chapter`, this makes *book/chapters/00-<name>.md*, an unnumbered chapter before the numbered ones. With `appendix`, it counts up from `a-` instead of down from `z-`. |

Table: Table A.1. press add options

**Example.** Press lowercases the name for the filename and turns each run of characters other than letters and digits into one hyphen. A title typed in words stays the heading word for word, as in the first command here.

```text
$ press add chapter "Down the rabbit-hole"
created book/chapters/01-down-the-rabbit-hole.md
$ press add appendix about-the-author
created book/appendices/z-about-the-author.md
```

**See also.** Chapter 3, *The shape of a book repository*, and Chapter 4, *Writing the manuscript*. `press new`, `press wordcount`.

## press aesthetic {-}

**Synopsis.**

```text
press aesthetic ["<brief>"] [--overwrite]
```

**Description.** With no argument, this prints the effective aesthetic: a comment naming its source, then the house aesthetic merged with *config/aesthetic.yaml*. The merge is shallow, so a top-level section in the book's file replaces the house section of the same name. With a brief in quotes, press runs the `aesthetic-brief` workflow through the `claude` command to draft *config/aesthetic.yaml*. It then prints `review it: press aesthetic`.

**Options.** Table A.2 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--overwrite` | This lets the drafting workflow replace an existing *config/aesthetic.yaml*. Without it, the workflow refuses to touch the file. Not listed by `--help`. |

Table: Table A.2. press aesthetic options

**Example.** The first command shows the house aesthetic, because the Alice book has no *config/aesthetic.yaml* yet. The second drafts one from a brief.

```text
$ press aesthetic
# effective aesthetic (.../data/aesthetic-house.yaml)
name: Victorian treatise
...
$ press aesthetic "a Victorian nursery book, gilt on red cloth"
...
review it: press aesthetic
```

**See also.** Chapter 9, *The house design*, Chapter 11, *The art department*, and Chapter 15, *The operator's desk and the editorial machines*. `press cover`, `press illustrate`.

## press all {-}

**Synopsis.**

```text
press all
```

**Description.** Runs the whole build: the checker, every edition, the source archive, the Pages bundle, every verifier, and then the commerce gate. A failure in the checker stops the run before press builds any edition. `press all` builds neither the print interior nor the cover wrap. `press print`, `press verify-print`, and `press coverwrap` make them, and the commerce gate builds them when print ordering is on.

**Options.** None.

**Example.** Unless you set `PRESS_RELEASE` and turn on print ordering, the commerce gate only advises. The Alice book has no print ordering, so the gate says so and the run goes on.

```text
$ press all
Source checks passed: 4 ordered Markdown files
...
Verified archives: alice-site.zip, alice-source.zip
...
commerce release gate: print ordering is not enabled; ...
```

**See also.** Chapter 7, *Building the editions*, and Chapter 8, *Verifying the artifacts*. `press check`, `press verify`, `press verify-formats`, `press pages`.

## press art accept {-}

**Synopsis.**

```text
press art accept <file>
                 --as cover|plate:<name>|logomark|portrait
```

**Description.** Takes a finished image into the book through *intake*: press converts the file to the house form, puts it in place, and records the acceptance in *art/commissions.md*. The art target after `--as` decides where the image goes. Press refuses an opaque single-ink plate on a gradient or textured ground, because the luminance key would leave a ghost on the page.

**Options.** Table A.3 lists the four forms of the one option, which you must give.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--as cover` | The image becomes *assets/cover.jpg*. At the time of this writing, its aspect ratio must be within 3 percent of the ratio of the legacy `trim` field (6 by 9 unless set), not the profile's. Press flattens any transparency onto white. |
| `--as plate:<name>` | The image becomes the alpha master *assets/woodcuts/<name>.png*, ink on transparency. The name must match `[a-z0-9][a-z0-9-]*`. |
| `--as logomark` | The image becomes *assets/press-logo.png*. Press extracts the ink of an opaque delivery onto transparency. |
| `--as portrait` | The image becomes *assets/author.jpg*, and press flattens it onto white. |

Table: Table A.3. press art accept options

**Example.** The session takes in the White Rabbit plate that `press illustrate` wrote. The line after the command names the destination and the size in pixels.

```text
$ press art accept build/illustrations/white-rabbit.png \
    --as plate:white-rabbit
accepted plate:white-rabbit: assets/woodcuts/white-rabbit.png
  (1024x1024)
```

**See also.** Chapter 5, *Figures, plates, and illustrations*, and Chapter 11, *The art department*. `press art commission`, `press art enhance`, `press cover`, `press illustrate`.

## press art commission {-}

**Synopsis.**

```text
press art commission [<target>...] [--model openai|gemini]...
                     [--count N] [--photo PATH]
```

**Description.** Sends the prompts in *art/commissions.md* to the image models and writes each result to *art/candidates/*, in a directory per art target, as *<model>-<n>.png*. The candidates number upward and never overwrite one another. The art targets are `cover`, `plate:<name>`, `logomark`, and `portrait`, and the default is all of them. Without *art/commissions.md*, the command refuses with `no commissions.md; run the art-direction workflow first`.

**Options.** Table A.4 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--model` *model* | This chooses an image model, `openai` or `gemini`. Repeat it to name both. The default is both models. Not listed by `--help`. |
| `--count N` | This sets the number of images per art target per model. The default is 1. Not listed by `--help`. |
| `--photo PATH` | This names the portrait's reference photograph, a JPEG or PNG file. The default is *art/author-photo* with any of the extensions *.jpg*, *.jpeg*, or *.png*, and press matches the extension without regard to case. Not listed by `--help`. |

Table: Table A.4. press art commission options

::: {.warning}
> **Warning:** Name the model every time you run this command. Without `--model`, it pays both OpenAI and Gemini for every art target, and it does not ask first.
:::

**Example.** The session asks OpenAI for two candidates of one plate, in *art/candidates/plate-white-rabbit/*. A second run adds new candidates and never overwrites the first ones.

```text
$ press art commission plate:white-rabbit --model openai \
    --count 2
...
```

**See also.** Chapter 11, *The art department*. `press art accept`, `press cover`, `press illustrate`.

## press art enhance {-}

**Synopsis.**

```text
press art enhance [<file>] [--colors N] [--max-edge PX]
```

**Description.** Finishes a plate. The subcommand is not listed by `--help`. Press upscales the image with Real-ESRGAN when it finds an upscaler. It then resamples the image down to the long edge, quantizes it to a few grays, and compresses it into *<stem>.png*. Without a file, it finishes every JPEG and PNG in *assets/woodcuts/*.

**Options.** Table A.5 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--colors N` | This sets the number of grays or colors after quantizing. The default comes from `plates.medium` in the aesthetic: 16 for engraving, woodcut, and line work, 24 for pen and etching, and 64 for wash and watercolor. Not listed by `--help`. |
| `--max-edge PX` | This sets the long edge after resampling, which only ever shrinks the image. The default is 2400 pixels. Not listed by `--help`. |

Table: Table A.5. press art enhance options

**Example.** On a color profile, the quantizing keeps colors instead of grays. A machine with no upscaler gets a message, and press goes on to quantize and compress without it.

```text
$ press art enhance assets/woodcuts/white-rabbit.png
...
$ press art enhance --colors 24
...
```

**See also.** Chapter 5, *Figures, plates, and illustrations*, and Chapter 11, *The art department*. `press art accept`.

## press check {-}

**Synopsis.**

```text
press check
```

**Description.** Runs the checker's four passes in order: the source checks, the checker self-test over the known-bad fixtures, the style audit, and the jargon lint. The first pass that fails stops the run with exit status 1. The jargon lint writes its full audit to *build/jargon-report.txt*. A bare format target such as `press pdf` does not run the checker, but `press all` and CI do.

**Options.** None.

**Example.** Example A.1 shows a passing run. We cut the two notes about extra diagnostics from the dash fixtures. The checker expects those diagnostics.

**Example A.1. press check on a passing manuscript**

```text
$ press check
Source checks passed: 4 ordered Markdown files
...
Checker self-test passed: 19 known-bad fixtures each tripped
  their declared rule, known-good fixture accepted, 2 extra
  diagnostics noted
Editorial checks passed: 4 Markdown files
Jargon check passed: no rewrite-status terms (full audit in
  build/jargon-report.txt)
```

**See also.** Chapter 6, *Checking the manuscript*. `press style`, `press all`.

## press clean {-}

**Synopsis.**

```text
press clean
```

**Description.** Deletes *build/* and *dist/* and prints nothing. The next target rebuilds what it needs from the manuscript and the config.

**Options.** None.

**Example.** Run it when you doubt a leftover file in *build/*.

```text
$ press clean
$ press pdf
...
```

**See also.** Chapter 3, *The shape of a book repository*, and Chapter 7, *Building the editions*. `press all`.

## press config get {-}

**Synopsis.**

```text
press config get <path> [--json]
```

**Description.** Prints the value of one config field, named by its dotted path, such as `print.profile`. A list prints as JSON, and a string prints bare. For a field that is not set, the command prints `<path>: not set` and exits with status 5.

**Options.** Table A.6 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--json` | This prints the value as JSON, so a string comes back in quotes. Not listed by `--help`. |

Table: Table A.6. press config get options

**Example.** The first field is a list, so the value prints as JSON. The second has no value yet, and the command exits with status 5.

```text
$ press config get author
["Lewis Carroll"]
$ press config get registrations.lccn
registrations.lccn: not set
```

**See also.** Chapter 3, *The shape of a book repository*, and Appendix B, *Configuration reference*. `press config list`, `press config set`.

## press config list {-}

**Synopsis.**

```text
press config list [--file <file>] [--json]
```

**Description.** Prints every field the book model knows, one to a line, with its path, its type, and a line of help. A field that you cannot write says so and names what to change instead. The field `trim`, for example, is immutable and comes from `print.profile`.

**Options.** Table A.7 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--file <file>` | This lists only the fields of one config file, named by its path from the book root, such as `config/house-rules.yaml`. Not listed by `--help`. |
| `--json` | This prints a JSON array instead, with each field's path, file, kind, type, help, whether it is required, its choices, and its manager. Not listed by `--help`. |

Table: Table A.7. press config list options

**Example.** The session lists the three fields of the house rules file, each with its path, its type, and its help.

```text
$ press config list --file config/house-rules.yaml
  banned-patterns  mapping   regex -> label; applied by the
    style audit
  jargon-allow     list[str] watchlist terms this book may use
  audit-dirs       list[str] extra directories to lint beyond
    book/
```

**See also.** Chapter 3, *The shape of a book repository*, and Appendix B, *Configuration reference*. `press config get`, `press config validate`.

## press config set {-}

**Synopsis.**

```text
press config set <path> <value> [--json] [--dry-run]
```

**Description.** Writes one field after the book model checks the new value, and prints a unified diff of the change to the file. Give a list or a mapping as JSON. The command exits with status 3 for an unknown or unwritable field and with status 4 for a value the model refuses.

**Options.** Table A.8 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--json` | This reads the value as JSON. Lists and mappings need it. Not listed by `--help`. |
| `--dry-run` | This prints the diff, then `(dry run: nothing written)`, and writes nothing. Not listed by `--help`. |

Table: Table A.8. press config set options

**Example.** A boolean takes `true`, `yes`, `on`, or `1`, and `false`, `no`, `off`, or `0`. Example A.2 sets the two sentinels and then tries to set the trim, which press refuses.

**Example A.2. press config set, accepted and refused**

```text
$ press config set verify-sentinels \
    '["Twinkle, twinkle, little bat", "she made some tarts"]' \
    --json
...
$ press config set trim 5x8
trim is not writable through `press config`: trim is not set
  directly; choose it with print.profile
$ echo $?
3
```

**See also.** Chapter 3, *The shape of a book repository*, and Appendix B, *Configuration reference*. `press config unset`, `press config validate`.

## press config unset {-}

**Synopsis.**

```text
press config unset <path> [--dry-run]
```

**Description.** Removes one field from its file and prints the diff. The field then takes the book model's default, where the model has one.

**Options.** Table A.9 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--dry-run` | This prints the diff, then `(dry run: nothing written)`, and writes nothing. Not listed by `--help`. |

Table: Table A.9. press config unset options

**Example.** Example A.3 previews the diff when you remove the scaffold's placeholder subtitle.

**Example A.3. press config unset with a dry run**

```text
$ press config unset subtitle --dry-run
--- a/metadata.yaml
+++ b/metadata.yaml
@@ -1,5 +1,4 @@
 title: "alice"
-subtitle: "A subtitle"
 author:
   - "Lewis Carroll"
 date: "First edition, 2026"
(dry run: nothing written)
```

**See also.** Chapter 3, *The shape of a book repository*. `press config set`.

## press config validate {-}

**Synopsis.**

```text
press config validate [--json]
```

**Description.** Checks every config file against the book model and reports each file on its own line, the absent optional files included, as `ok` or with its problems. Any failure makes the command exit with status 4.

**Options.** Table A.10 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--json` | This prints a JSON object that maps each file to its list of problems, which is empty for a file that passes. Not listed by `--help`. |

Table: Table A.10. press config validate options

**Example.** Example A.4 shows the Alice book with every file in order.

**Example A.4. press config validate**

```text
$ press config validate
config/metadata.yaml: ok
config/house-rules.yaml: ok
config/front-matter.yaml: ok
config/aesthetic.yaml: ok
config/index-terms.yaml: ok
config/authorities.yaml: ok
```

**See also.** Chapter 3, *The shape of a book repository*, and Appendix B, *Configuration reference*. `press config list`, `press check`.

## press cover {-}

**Synopsis.**

```text
press cover [--style <id>] [--subject <text>] [--print] | --list
```

**Description.** Builds a cover prompt from a named style and the book's metadata and sends it to OpenAI's `gpt-image-2`. Press writes the image to *build/cover/cover.png* and prints the `press art accept` line for the next step. Without `OPENAI_API_KEY`, it prints the prompt instead, so that you can give it to an image model elsewhere.

**Options.** Table A.11 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--style <id>` | This chooses one of the ten packaged styles, or a style from the book's *config/cover-styles.yaml*. |
| `--subject <text>` | This says what the cover shows. Without it, press takes `cover.subject` from the aesthetic, then the metadata `description`, then `cover.emblem`. |
| `--print` | This prints the prompt and sends nothing. Not listed by `--help`. |
| `--list` | This prints each style with a one-line note and exits. |

Table: Table A.11. press cover options

**Example.** The style comes from `--style`, then from `cover.style` in the aesthetic, then from the default `penguin-tri-band`. This session runs on `hatter` without a key.

```text
$ press cover --style victorian-clothbound \
    --subject "a rabbit, a pocket watch, a rabbit-hole"
# no OPENAI_API_KEY set; emitting the prompt to run elsewhere.
...
```

**See also.** Chapter 11, *The art department*. `press art accept`, `press art commission`, `press aesthetic`.

## press coverwrap {-}

**Synopsis.**

```text
press coverwrap
```

**Description.** Builds the print interior, reads its page count, and then generates and verifies the cover wrap, *dist/alice-coverwrap.pdf*. The wrap is one page with the back, the spine, and the front. Press computes the width of the spine. It needs *assets/cover.jpg* and the metadata `title`, `author`, `publisher`, and `publisher-place`.

**Options.** None.

**Example.** With a print ISBN in the config, the wrap carries its EAN-13 barcode. Without the cover image, the command refuses, as it does here.

```text
$ press coverwrap
...
coverwrap needs assets/cover.jpg (the front board art)
```

**See also.** Chapter 12, *The print pack*, and Chapter 13, *Registrations*. `press print`, `press verify-print`, `press isbn`.

## press desk {-}

**Synopsis.**

```text
press desk
```

**Description.** Opens the desk in the terminal: the book's identity, a table of artifacts and their state, the toolchain line, and the doctor's findings. The keys run a target (`p`), open the setup wizard (`w`), refresh the screen (`r`), and quit the desk (`q`). The desk needs the `tui` extra and a terminal. If either is missing, it exits with status 2, because it never draws into a pipe.

**Options.** None.

**Example.** Without the extra, the command prints the line that installs it and exits with status 2.

```text
$ press desk
press desk needs the optional interface: pip install
  'press[tui]'
$ echo $?
2
```

**See also.** Chapter 2, *Installing press*, and Chapter 15, *The operator's desk and the editorial machines*. `press doctor`.

## press doctor {-}

**Synopsis.**

```text
press doctor
```

**Description.** Checks every program and key the press can use, and prints one line per capability with its state: `ok`, `absent`, `MISSING`, `BROKEN`, `warn`, or `unset`. A tool is `BROKEN` when it is present but fails both `--version` and `-v` within 15 seconds. The command exits with status 0 when the machine is ready and 1 when it is not.

**Options.** None.

**Example.** The last line reads `this machine can make books`, or `not ready:` followed by the tools to fix. Example A.5 shows the start and the end of a report on `hatter`.

**Example A.5. press doctor on a ready machine**

```text
$ press doctor
press doctor
  [     ok] pandoc     every build target
  [     ok] lualatex   PDF and print builds
...
this machine can make books
$ echo $?
0
```

**See also.** Chapter 2, *Installing press*, and Appendix D, *The toolchain, platform by platform*. `press desk`.

## press docx {-}

**Synopsis.**

```text
press docx
```

**Description.** Builds the Office edition (DOCX), *dist/alice.docx*, with pandoc and the portable defaults. Like every format target, it needs the toolchain and does not run the checker first.

**Options.** None.

**Example.** The Telegraphic edition uses the same portable defaults file.

```text
$ press docx
+ pandoc --defaults=~/alice/build/defaults/portable.yaml ...
```

**See also.** Chapter 7, *Building the editions*. `press txt`, `press verify-formats`.

## press epub {-}

**Synopsis.**

```text
press epub
```

**Description.** Builds the Circulating edition (EPUB), *dist/alice.epub*, with *assets/cover.jpg* as its cover image when the file exists. Press writes the year from the metadata `date` into *build/epub-metadata.xml*, because epubcheck rejects the empty `dc:date` that pandoc writes. The target only builds. `press verify-formats` runs epubcheck.

**Options.** None.

**Example.** The Circulating edition takes its rights line from the metadata `copyright`, `publisher`, and `publisher-place`.

```text
$ press epub
+ pandoc --defaults=~/alice/build/defaults/epub.yaml ...
```

**See also.** Chapter 7, *Building the editions*, and Chapter 8, *Verifying the artifacts*. `press verify-formats`.

## press figures {-}

**Synopsis.**

```text
press figures
```

**Description.** Prints, as a JSON array, every figure the manuscript declares, one object per image. Each object holds the file, the image path, the caption, the kind, the style, the directive and its description, and the placement fields. `press illustrate` and the `art-direction` workflow read the figures through this command instead of parsing the Markdown themselves.

**Options.** None.

**Example.** Example A.6 shows the start of the entry for one plate.

**Example A.6. press figures**

```text
$ press figures
[
  {
    "file": "book/chapters/01-down-the-rabbit-hole.md",
    "src": "assets/woodcuts/white-rabbit.png",
    "caption": "The White Rabbit",
    "kind": "plate",
    ...
```

**See also.** Chapter 5, *Figures, plates, and illustrations*, and Chapter 11, *The art department*. `press illustrate`.

## press html {-}

**Synopsis.**

```text
press html
```

**Description.** Builds the Single-leaf edition, the self-contained HTML file *dist/alice.html*, which carries its images and styles inside it.

**Options.** None.

**Example.** pandoc builds the file with its `self-contained` setting, and press then adds labels to the table cells.

```text
$ press html
+ pandoc --defaults=~/alice/build/defaults/html.yaml ...
```

**See also.** Chapter 7, *Building the editions*. `press site`, `press verify-formats`.

## press illustrate {-}

**Synopsis.**

```text
press illustrate <name> [--style <id>] [--subject <text>]
                 [--from <image>] [--print] | --list
```

**Description.** Commissions one square plate or illustration from OpenAI's `gpt-image-2`, writes *build/illustrations/<name>.png*, and prints the `press art accept` line for it. Without `--subject`, press uses the `art:` comment of the figure whose image file has the stem `<name>`. It refuses a figure the manuscript does not declare, a `.chart` or `.diagram` figure, and a figure with no `art:` description.

**Options.** Table A.12 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--style <id>` | This chooses one of the seven packaged styles, or a style from the book's *config/illustration-styles.yaml*. |
| `--subject <text>` | This gives the subject in place of the figure's `art:` comment. Not listed by `--help`. |
| `--from <image>` | This sends a source image for the model to redraw. The `figure-from-photo` style requires it. |
| `--print` | This prints the prompt and sends nothing. Not listed by `--help`. |
| `--list` | This prints each style with a one-line note and exits. |

Table: Table A.12. press illustrate options

**Example.** The style comes from `--style`, then the figure's `style=` attribute, then `plates.style` in the aesthetic, then the default `wood-engraving`. The session commissions the White Rabbit plate and accepts it.

```text
$ press illustrate white-rabbit
...
$ press art accept build/illustrations/white-rabbit.png \
    --as plate:white-rabbit
...
```

**See also.** Chapter 5, *Figures, plates, and illustrations*, and Chapter 11, *The art department*. `press figures`, `press art accept`, `press cover`.

## press improve {-}

**Synopsis.**

```text
press improve [--apply] [--rounds N]
```

**Description.** Runs the `editorial-passes` workflow from the installed press through the `claude` command. Without `--apply`, it works as counsel: it writes *build/editorial-report.md*, changes nothing, and hashes *book/* and *config/* before and after to prove it. With `--apply`, the workflow rewrites chapters and closes each round with `press check`.

**Options.** Table A.13 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--apply` | This lets the workflow apply its suggestions and gives it the full Bash tool instead of `press` and `python3` alone. |
| `--rounds N` | This sets the largest number of rounds the workflow runs. The workflow's default is 2. Not listed by `--help`. |

Table: Table A.13. press improve options

**Example.** The first run writes the report and changes nothing. Read the report, commit, and then let the workflow apply its suggestions.

```text
$ press improve
...
$ git commit -am "Before the editorial passes"
...
$ press improve --apply --rounds 3
...
```

**See also.** Chapter 15, *The operator's desk and the editorial machines*. `press workflows`, `press research`, `press check`.

## press isbn {-}

**Synopsis.**

```text
press isbn status
press isbn assign print|epub
```

**Description.** Assigns ISBNs offline from the block you bought, which *config/metadata.yaml* records under `registrations.isbn-block` as a prefix and a size. `assign` computes the next unused number and its check digit for one edition and writes it through `press config`. It refuses an edition that already has an ISBN.

**Options.** None.

**Example.** Set the block with two `press config set` commands, one for `registrations.isbn-block.prefix` and one for `registrations.isbn-block.size`. With no block, `status` says so and exits with status 1. With the block, `status` prints the numbers in use and the numbers free. `assign print` writes `registrations.isbn.print`, and `assign epub` writes `registrations.isbn.epub`.

```text
$ press isbn status
no registrations.isbn-block configured; set the prefix and size
  your ISBN agency gave you (e.g. prefix: 978-1-960780, size:
  100)
$ press config set registrations.isbn-block.prefix \
    978-1-960780
...
$ press config set registrations.isbn-block.size 100
...
$ press isbn status
ISBN block 978-1-960780 (size 100): 0 assigned, 100 free
$ press isbn assign print
...
```

**See also.** Chapter 13, *Registrations*. `press onix`, `press pcn`, `press coverwrap`.

## press lookup {-}

**Synopsis.**

```text
press lookup lccn|issn [<number>]
```

**Description.** Asks the Library of Congress about an LCCN, or the ISSN portal about an ISSN, that an agency issued earlier. It reaches the network, as `press cover`, `press illustrate`, `press art commission`, and `press research` do, and it never issues a number. Without a number, it uses `registrations.lccn` or `registrations.issn` from the config. It exits with status 0 only when the outcome is `found`.

**Options.** None.

**Example.** Store the number the Library of Congress sent, then look it up. The outcome is one of `found`, `not-found`, `ambiguous`, `mismatch`, `invalid`, and `unavailable`.

```text
$ press config set registrations.lccn <number>
$ press lookup lccn
...
```

**See also.** Chapter 13, *Registrations*. `press pcn`.

## press markdown {-}

**Synopsis.**

```text
press markdown
```

**Description.** Stitches the Manuscript edition (the stitched Markdown), *dist/alice.md*, from the chapter files and appendix files without pandoc. The file is a header followed by the manuscript as you wrote it. Press removes only the attribute blocks from the headings.

**Options.** None.

**Example.** The edition comes straight from the files in *book/*, in the order press sorts them.

```text
$ press markdown
+ stitched 4 files -> dist/alice.md
```

**See also.** Chapter 7, *Building the editions*. `press verify-formats`.

## press migrate {-}

**Synopsis.**

```text
press migrate [plan] | apply | rollback | status
```

**Description.** Moves the book's pin to the next press major, and changes nothing else. `plan`, the default, prints the change and writes nothing. `apply` writes an exact backup to *.press/migration-backup.json*, then rewrites the pins in *requirements.txt* and *.github/workflows/*.

**Options.** None.

**Example.** `rollback` restores the prior bytes, and `status` prints the current pin. Press refuses a pin it finds outside *requirements.txt* and *.github/workflows/*. At the time of this writing, press 3 is the newest major, so there is nothing to move to yet. The session asks for the status of the Alice book, which follows `v3`.

```text
$ press migrate status
pinned to v3:
  requirements.txt: clintecker/press@v3
  .github/workflows/book.yml:
    clintecker/press/.github/workflows/build.yml@v3
```

**See also.** Chapter 14, *Continuous integration and the release contract*. `press selftest`.

## press new {-}

**Synopsis.**

```text
press new <directory> [--author A] [--publisher P]
          [--place PLACE] [--owner GH]
```

**Description.** Creates a book repository in a new directory. The directory's name becomes the slug and must match `[a-z0-9][a-z0-9-]*`. Press refuses a path that exists. Otherwise it copies the template, stamps the four workflows into *.claude/workflows/*, and fills in the identity. It does not run `git init`.

**Options.** Table A.14 lists the options.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--author A` | This sets the byline. Without it, press reads `git config user.name`. If that is empty, it writes "The Author". Not listed by `--help`. |
| `--publisher P` | This sets the imprint. The default is the author. Not listed by `--help`. |
| `--place PLACE` | This sets the place of the imprint. The default is "Earth". Not listed by `--help`. |
| `--owner GH` | This names the GitHub account that owns the repository, and writes live `repository` and `site-url` lines. Without it, those lines stay commented out, with `OWNER` in place of the account. Not listed by `--help`. |

Table: Table A.14. press new options

**Example.** The first line of output ends with the absolute path of the new directory, which we shorten here.

```text
$ press new alice --author "Lewis Carroll" \
    --owner wonderland-press
scaffolded alice -> /.../alice
next: edit config/metadata.yaml, write book/chapters/, ...
```

**See also.** Chapter 1, *Introduction*, and Chapter 3, *The shape of a book repository*. `press add`, `press config set`.

## press onix {-}

**Synopsis.**

```text
press onix [--forthcoming]
```

**Description.** Writes an ONIX 3.0 metadata record to *dist/alice.onix.xml*. The record always holds a print product, and an EPUB product when an EPUB ISBN exists. It carries no price, because a book repository holds none.

**Options.** Table A.15 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--forthcoming` | This sets the publishing status to forthcoming (code 02) instead of active (code 04). |

Table: Table A.15. press onix options

**Example.** The Alice book has no ISBN yet, so the record holds only the print product.

```text
$ press onix
wrote dist/alice.onix.xml (1 product(s); ISBNs: none yet)
```

**See also.** Chapter 13, *Registrations*. `press isbn`, `press pcn`.

## press pages {-}

**Synopsis.**

```text
press pages
```

**Description.** Builds every artifact the Pages bundle links, assembles the bundle in *dist/pages/*, and then verifies it. The bundle holds the landing page, a *read/* copy of the reader site, and *downloads/*, plus *sitemap.xml* and *robots.txt* when you set `site-url`. The verifier checks that every local reference resolves.

**Options.** None.

**Example.** You can run it alone, without `press all`, to rebuild the bundle.

```text
$ press pages
...
+ assembled pages site -> dist/pages
Verified dist/pages: every local reference resolves ...
```

**See also.** Chapter 7, *Building the editions*, Chapter 8, *Verifying the artifacts*, and Chapter 14, *Continuous integration and the release contract*. `press verify-pages`, `press site`.

## press pcn {-}

**Synopsis.**

```text
press pcn
```

**Description.** Prints the field values for the Library of Congress PrePub Book Link form and writes them to *dist/alice-pcn.txt*. It never contacts the Library of Congress. A value the book lacks prints as `(needed on the form)`. When the print ISBN is missing, its line points you to `press isbn assign print`.

**Options.** None.

**Example.** Example A.7 shows the start of the report on the fresh scaffold. When the Library of Congress sends the LCCN, store it with `press config set registrations.lccn <number>`.

**Example A.7. press pcn**

```text
$ press pcn
Library of Congress PCN -- PrePub Book Link field values
https://www.loc.gov/publish/pcn/  (self-publishers use PCN, not
  CIP)

  Title                          alice
  Subtitle                       A subtitle
...
(also written to dist/alice-pcn.txt)
```

**See also.** Chapter 13, *Registrations*. `press lookup`, `press isbn`.

## press pdf {-}

**Synopsis.**

```text
press pdf
```

**Description.** Builds the Print edition, *dist/alice.pdf*, through pandoc and then latexmk, which runs LuaLaTeX as many times as the lists need. On the way, it generates the front matter and the subject index and checks the table of authorities. The index or the table of authorities can refuse the build. The first run on a fresh machine spends several minutes on a font scan, which looks like a hang and is not one.

**Options.** None.

**Example.** Here the subject index refuses the build, because a curated term matches nothing in the text.

```text
$ press pdf
...
gen_index: curated terms match nothing in the text: Jabberwock
  (fix the patterns or remove the terms; silence is not allowed)
```

**See also.** Chapter 7, *Building the editions*, and Chapter 10, *Front matter, the index, and the table of authorities*. `press verify`, `press render`.

## press print {-}

**Synopsis.**

```text
press print
```

**Description.** Builds the print interior, *dist/alice-interior.pdf*, two-sided for the book's design profile. Every image goes through the print-safe pass, which flattens it and caps its resolution.

**Options.** None.

**Example.** The interior uses the print defaults file, *print.yaml*.

```text
$ press print
+ pandoc --defaults=~/alice/build/defaults/print.yaml ...
...
```

**See also.** Chapter 12, *The print pack*. `press verify-print`, `press coverwrap`, `press publish`.

## press publish {-}

**Synopsis.**

```text
press publish kdp|ingram [--report-only]
```

**Description.** Rebuilds and verifies the four files a retail channel needs: the print interior, the cover wrap, the Circulating edition (EPUB), and the marketing cover image. It then writes a checklist to *dist/publish-kdp.md* or *dist/publish-ingram.md*. The command exits with status 1 if any file fails its verification.

**Options.** Table A.16 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--report-only` | This writes the checklist without the verification, and marks each file "present but NOT verified (report-only)". |

Table: Table A.16. press publish options

**Example.** The checklist has three parts: the files, the identity the channel will ask for, and the tasks only a person can do, such as ordering a physical proof.

```text
$ press publish kdp --report-only
...
$ less dist/publish-kdp.md
```

**See also.** Chapter 12, *The print pack*. `press coverwrap`, `press verify-print`, `press onix`.

## press render {-}

**Synopsis.**

```text
press render
```

**Description.** Builds the Print edition (PDF), then renders every page with `pdftoppm` to a PNG file at 160 dpi in *build/rendered-book/*. Because the target builds the Print edition first, the images always show the current manuscript.

**Options.** None.

**Example.** `press clean` deletes the images with the rest of *build/*.

```text
$ press render
...
$ ls build/rendered-book
page-*.png ...
```

**See also.** Chapter 7, *Building the editions*, and Chapter 9, *The house design*. `press pdf`, `press verify`.

## press research {-}

**Synopsis.**

```text
press research [--max-claims-per-file N]
```

**Description.** Runs the `authorities-research` workflow from the installed press through the `claude` command, with the Web search and Web fetch tools allowed. The workflow extracts the claims of fact from each file, researches each one, audits the findings, and writes *config/authorities.yaml*, the table of authorities. It reports the claims it could not source instead of adding them to the table of authorities.

**Options.** Table A.17 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--max-claims-per-file N` | This caps the claims taken from each file. The default, 0, means every claim. A positive cap takes a sample of the claims, and the workflow's accounting reports the claims it left out. Not listed by `--help`. |

Table: Table A.17. press research options

**Example.** The workflow edits *config/authorities.yaml*, so review the diff before you commit it.

```text
$ press research
...
$ git diff --stat config/authorities.yaml
```

**See also.** Chapter 10, *Front matter, the index, and the table of authorities*, and Chapter 15, *The operator's desk and the editorial machines*. `press improve`, `press pdf`.

## press selftest {-}

**Synopsis.**

```text
press selftest [--write-docs]
```

**Description.** Runs the press's 29 checks on itself, from the ISBN arithmetic to the documents generated from the code. It prints its progress and ends with one success line when all pass. From an installed wheel, it skips the checks that need the press repository's own files.

**Options.** Table A.18 lists the one option.

| Option | Meaning |
|------------------------|----------------------------------------------------------------|
| `--write-docs` | This regenerates *docs/REFERENCE.md*, *docs/INVARIANTS.md*, *docs/PROVIDER-QUALIFICATION.md*, and the packaged provider record from their sources. It is for work in the press repository. Not listed by `--help`. |

Table: Table A.18. press selftest options

**Example.** An author rarely needs this command. It is the press checking itself.

```text
$ press selftest
...
Selftest passed: 29 checks, arithmetic agrees with the canonical
  examples, usage and README name every target
```

**See also.** Chapter 16, *Inside the press*. `press doctor`.

## press site {-}

**Synopsis.**

```text
press site
```

**Description.** Builds the Chapter edition: the reader site in *dist/site/*, one page per chapter with the house reader stylesheet, and its zip, *dist/alice-site.zip*.

**Options.** None.

**Example.** The zip holds the same pages as one download.

```text
$ press site
+ pandoc --defaults=~/alice/build/defaults/chunked.yaml ...
```

**See also.** Chapter 7, *Building the editions*, and Chapter 9, *The house design*. `press pages`, `press html`.

## press skills {-}

**Synopsis.**

```text
press skills
```

**Description.** Lists the packaged skills, one to a line, each with the path of its installed file. At the time of this writing, press has eleven, from `book-aesthetics` to `overused-jargon`.

**Options.** None.

**Example.** The workflows find the skills through this command before they look in a checkout of the press. A tab separates the name from the path, shown here as spaces.

```text
$ press skills
book-aesthetics  .../press/data/skills/book-aesthetics.md
cover-design     .../press/data/skills/cover-design.md
...
```

**See also.** Chapter 15, *The operator's desk and the editorial machines*. `press workflows`.

## press source {-}

**Synopsis.**

```text
press source
```

**Description.** Packages the Source edition (the source zip), *dist/alice-source.zip*. A book outside any Git repository gets an archive of the whole directory. A book that sits untracked inside another repository gets an empty archive (press prints `archived 0 files`) until Git tracks its files.

**Options.** None.

**Example.** The archive leaves out *.git/*, *build/*, *dist/*, and Python's cache directories.

```text
$ press source
~/alice/dist/alice-source.zip
archived 14 files; excluded dirs ['.git', '__pycache__',
  'build', 'dist']
```

**See also.** Chapter 3, *The shape of a book repository*, and Chapter 7, *Building the editions*. `press all`.

## press style {-}

**Synopsis.**

```text
press style
```

**Description.** Runs the style audit alone, the third pass of `press check`. It reads the manuscript and any directories named in `audit-dirs`. In an audit directory, heading and paragraph problems are warnings instead of errors.

**Options.** None.

**Example.** In an audit directory, the audit applies the dash and phrase rules but not the glyph, curly-quote, or banned-pattern rules.

```text
$ press style
Editorial checks passed: 4 Markdown files
```

**See also.** Chapter 6, *Checking the manuscript*. `press check`.

## press txt {-}

**Synopsis.**

```text
press txt
```

**Description.** Builds the Telegraphic edition (plain text at 80 columns), *dist/alice.txt*, with pandoc and the portable defaults.

**Options.** None.

**Example.** Like the other format targets, it does not run the checker first, so run `press check` before you send the file anywhere.

```text
$ press txt
+ pandoc --defaults=~/alice/build/defaults/portable.yaml ...
```

**See also.** Chapter 7, *Building the editions*. `press docx`, `press verify-formats`.

## press verify {-}

**Synopsis.**

```text
press verify
```

**Description.** Rebuilds the Print edition, *dist/alice.pdf*, and verifies it as an object. The verifier checks the page count against `verify-min-pages`, the trim, and the embedded fonts. It also looks for the sentinels and the title, ink on every rendered page, clipping at the edges, and the cover on page 1.

**Options.** None.

**Example.** This capture comes from the press's own three-chapter Alice example, which has 23 pages and two sentinels.

```text
$ press verify
...
Verified alice.pdf: 23 pages, 6 x 9 trim, embedded fonts, 2
  sentinel(s) plus the title as witnesses, every rendered page
  contains ink, no edge clipping, cover on page 1
```

**See also.** Chapter 8, *Verifying the artifacts*. `press verify-formats`, `press pdf`.

## press verify-formats {-}

**Synopsis.**

```text
press verify-formats
```

**Description.** Rebuilds the editions other than the Print edition (PDF), then verifies each of them and the two archives. epubcheck validates the Circulating edition (EPUB). Press then confirms that the editions agree on the chapter witnesses.

**Options.** None.

**Example.** Without epubcheck on a local machine, press reports the missing check as a warning instead of a failure. In the toolchain image, a missing epubcheck fails the run. Example A.8 shows a run on `hatter`, which has no epubcheck.

**Example A.8. press verify-formats without epubcheck**

```text
$ press verify-formats
...
WARNING: epubcheck not installed; EPUB validated structurally
  only. The press toolchain runs the full check in CI. (brew
  install epubcheck)
...
Verified archives: alice-site.zip, alice-source.zip
```

**See also.** Chapter 8, *Verifying the artifacts*, and Appendix D, *The toolchain, platform by platform*. `press verify`, `press all`.

## press verify-pages {-}

**Synopsis.**

```text
press verify-pages
```

**Description.** An alias of `press pages`, not listed by `--help`. It builds, assembles, and verifies the Pages bundle exactly as `press pages` does.

**Options.** None.

**Example.** Both names run the same code and print the same lines.

```text
$ press verify-pages
...
+ assembled pages site -> dist/pages
...
```

**See also.** Chapter 8, *Verifying the artifacts*. `press pages`.

## press verify-print {-}

**Synopsis.**

```text
press verify-print
```

**Description.** Builds and verifies the print interior and, when *assets/cover.jpg* exists, the cover wrap. The interior must be single ink except on a color profile. On any other profile, color on any page makes the verifier refuse the interior with `print profile: colored ink on pages [...]`, followed by advice about the title page.

**Options.** None.

**Example.** The color refusal names the pages at fault, so you can find them in the interior. The Alice book has no cover image yet, so the command verifies the interior alone.

```text
$ press verify-print
...
no assets/cover.jpg; interior verified, wrap not built
```

**See also.** Chapter 12, *The print pack*. `press print`, `press coverwrap`.

## press wordcount {-}

**Synopsis.**

```text
press wordcount
```

**Description.** Counts the words in each chapter file and appendix file and prints a total. It skips fenced and inline code, and it counts the words in HTML comments.

**Options.** None.

**Example.** On a fresh scaffold only the preface exists, with its 42 words of placeholder.

```text
$ press wordcount
    42  book/chapters/00-preface.md
    42  TOTAL
```

**See also.** Chapter 3, *The shape of a book repository*, and Chapter 7, *Building the editions*. `press add`.

## press workflows {-}

**Synopsis.**

```text
press workflows
```

**Description.** Lists the packaged workflows with their arguments, a paste-ready Workflow invocation for each, and whether the book's copy in *.claude/workflows/* matches the installed press. A copy that differs says `DIFFERS from installed press` and names the version.

**Options.** None.

**Example.** Example A.9 shows the entry for one of the four workflows.

**Example A.9. press workflows**

```text
$ press workflows
...
editorial-passes
  args: {root: absolute path to the book repository}. ...
  pinned: .../alice/.claude/workflows/editorial-passes.js
    (matches installed press 3.0.2)
  invoke: Workflow({name: "editorial-passes", args: {root:
    ".../alice"}})
```

**See also.** Chapter 15, *The operator's desk and the editorial machines*. `press improve`, `press skills`.

## Exit codes {-}

Every target exits with status 0 on success and 1 when a check or a verifier fails. A failing outside program passes its own exit status through, so a pandoc or latexmk failure reports the code that program returned. Table A.19 lists the other codes.

| Situation | Exit status |
|---------------------------------------|---------------------------------------------|
| A bare `press`, or a command press does not know | 2, after the usage |
| `press config` | 0 for success, 2 for a usage error, 3 for an unknown or unwritable field, 4 for a refused value or a failed validation, 5 for a read of a field that is not set |
| `press add` | 1 when it refuses to overwrite a file, 2 for a usage error |
| `press doctor` | 0 when the machine is ready, 1 when it is not |
| `press desk` without the `tui` extra or a terminal | 2 |
| The composite action, when it refuses a command | 2 |
| `press lookup` | 0 only when the outcome is `found` |
| `press publish` | 1 when anything is unverified, unless you give `--report-only` |

Table: Table A.19. Exit codes beyond 0 and 1

Test the exit status, not the output, in a script. A chain such as `press check && git commit` stops on a failure. A pipe into `grep` before the `&&` hides the failure behind `grep`'s own status.

## Environment variables {-}

Table A.20 lists the environment variables press reads or sets. The first five rows matter to an author. The rest belong to the toolchain image, to CI, and to work on the press itself.

| Variable | Effect |
|-----------------------|----------------------------------------------------------------|
| `BOOK_ROOT` | This names the book root. The default is the current directory, and press also sets it for the programs a build runs. |
| `PRESS_RELEASE` | This turns on release mode. A build demands the release witnesses (at least two sentinels and a page floor of at least 24), and the commerce gate fails closed. CI sets it on a tag whose name starts with `v`. |
| `OPENAI_API_KEY`, `GEMINI_API_KEY` | These are the image-model keys for the art commands. Press reads them when a command needs them and never stores them. |
| `SOURCE_DATE_EPOCH` | This fixes the build time for reproducible builds. The default is 1784160000. |
| `NO_COLOR`, `FORCE_COLOR` | These turn color in the terminal output off or on. |
| `PRESS_TOOLCHAIN` | The toolchain image sets this, and it makes a missing epubcheck fatal. |
| `BOOK_PUBLISHER` | Press sets this for the plain title page in TeX. |
| `GITHUB_SHA` | Press's build receipts record this in CI. |
| `PRESS_REQUIRE_LUA` | In press development and CI, this forbids skipping the Lua filter tests. |
| `PRESS_LUA_COV_DIR` | In press development, this names the directory for Lua coverage measurement. |
| `PRESS_REQUIRE_BROWSER_CHECK` | In the CI for the press's documentation site, this requires the headless Chrome layout check. |
| `SECURITY_AUDIT_TOKEN` | This is a secret in the press repository's CI, for the check that the security controls still match their record. |

Table: Table A.20. Environment variables
