# Preface {.unnumbered}

A book now has to exist in several forms at once. A printer wants a PDF and a cover wrap with a computed spine, and a retail channel wants an EPUB that passes epubcheck. Readers want a Web site, a plain-text file, or a Word document. Most authors build each of these by hand, and they build them again after every correction. This book is about press, a program that builds all of them from one directory of Markdown and then inspects each finished file as an object.

The press began as the production machinery of one book, *Mostly Done.* Its maintainer pulled the machinery out of that book so that, in the package's own words, "the next book starts with the scars already paid for." A *scar*, in the press's vocabulary, is a production failure turned into a guard. A figure taller than the text block once sent LuaLaTeX into an endless run of empty pages. That failure, and each one like it, became a rule that the press now enforces. A second book, *Make Ready*, later went through the press from manuscript to registered ISBNs. Neither book lives in the press repository, which holds only the machinery.

The first commit to the press carries the date 2026-07-17. Version 2.0.0 followed four days later, and version 3.0.0, a design release, arrived on 2026-11-10. This book describes press 3.0.2, dated 2026-11-11, which is the current release at the time of this writing. Every statement about the press comes from its source and its documentation at that release. Where the documentation and the code disagree, we follow the code. Where neither says anything, neither do we.

This book is itself a press book. The press built every *edition* of it, one for each published form, from the Markdown in this book's repository. It verified each edition with the checks the chapters describe. If a page in your hands looks wrong, the fault is in the manuscript or in the press, and either way we want to hear about it.

## Who should read this book {-}

This book is for anyone who has a manuscript in Markdown and wants a finished book in print, as an EPUB, and on the Web. Perhaps you wrote something long in a text editor and kept it in Git. If you then lost a weekend persuading it into a PDF that a printer would accept, you are the reader we had in mind. Small-press operators who publish several books under one imprint will find that the same machinery serves every title they keep.

We assume that you can work at a Unix shell prompt, edit a text file, and use Git to clone, commit, and push. You do not need to know TeX, and you do not need to know pandoc. The press runs both for you, and the chapters explain what each one does when the explanation helps you read a refusal. Nor do you need to write Python, although Chapter 16 will make more sense if you can read it.

A second reader is the developer asked to keep a group's book builds running. We wrote Chapters 14 through 16 for that person. They cover continuous integration, the release contract that proves each press tag, the desk and the editorial machines, and the inside of the package.

The book does not teach Markdown from the beginning, and it does not compare the press with other publishing tools at any length. It explains one program, the reasons behind its rules, and what to do when it refuses your build.

## Organization of this book {-}

The chapters follow the order in which you make a book. Chapters 2 through 8 take a book from installation to verified artifacts, and you should read them in order the first time. Chapters 9 through 13 cover the work that follows a sound manuscript, and you can read them as your book needs them. Chapters 14 through 16 are for the person who runs the press. The appendixes are for reference.

**Chapter 1, *Introduction***\
Explains what press is, where it came from, and its four laws, then tours a build from `press new` to the finished editions and lists them.

**Chapter 2, *Installing press***\
Installs the Python package and the toolchain, runs `press doctor`, and shows how to build inside the toolchain image.

**Chapter 3, *The shape of a book repository***\
Scaffolds a book with `press new`, describes each file and the metadata fields, and shows how chapters and appendixes sort.

**Chapter 4, *Writing the manuscript***\
Describes the dialect the press reads, the characters you may type, and the forms a chapter can hold, from footnotes to set pieces.

**Chapter 5, *Figures, plates, and illustrations***\
Separates figures from plates, then covers the image line, the two lists, placement and measure, the height cap, and print-safe images.

**Chapter 6, *Checking the manuscript***\
Takes `press check` apart pass by pass, then covers house rules, sentinels, the page floor, and the exit status.

**Chapter 7, *Building the editions***\
Shows what each target runs, what the press tells pandoc, how the filter chain works, and what `press all` does in order.

**Chapter 8, *Verifying the artifacts***\
Explains how each verifier inspects a finished artifact, how witnesses tie the editions together, and how to read a failure.

**Chapter 9, *The house design***\
Gives the house page in numbers, the six design profiles, and the reader site, and explains why a design change needs a new major version.

**Chapter 10, *Front matter, the index, and the table of authorities***\
Covers the front-matter file key by key, the title and copyright pages, the subject index, the table of authorities, and the sources companion.

**Chapter 11, *The art department***\
Describes how the press commissions covers and plates, what intake does to a delivered image, and which commands spend money.

**Chapter 12, *The print pack***\
Builds the print interior and the cover wrap, works through providers and spine math, covers the publish checklists, and ends with ordering a copy.

**Chapter 13, *Registrations***\
Explains ISBNs, the ISSN and LCCN, ONIX, and the retail flag, and shows where each number goes: the copyright page, the EPUB metadata, the wrap barcode, the ONIX file, and the PCN listing.

**Chapter 14, *Continuous integration and the release contract***\
Describes a book's CI, the reusable workflow, the composite action, the toolchain image pinned by digest, and the receipts. Covers floating and immutable tags, the release contract, release builds, the Pages deploy, and moving between majors with `press migrate`.

**Chapter 15, *The operator's desk and the editorial machines***\
Shows the desk, the operator commands (`press improve`, `press research`, `press aesthetic`), and the four workflows and their skills. Explains why the editorial passes name the faults of machine prose outright.

**Chapter 16, *Inside the press***\
Maps the package, follows the data from manuscript to edition, and covers invariants, `press selftest`, and what a contributed scar must earn.

**Appendix A, *Command reference***\
Lists every command and option in manual-page form, with the exit codes and environment variables.

**Appendix B, *Configuration reference***\
Lists every key of every configuration file, with its type, its default, and the chapter that explains it.

**Appendix C, *Messages and refusals***\
Gives the messages the press prints when it refuses a build, each with its cause and remedy. Look a message up here before you read the code.

**Appendix D, *The toolchain, platform by platform***\
Describes what the toolchain needs on Debian and Ubuntu, on macOS, and inside the toolchain image, and which platforms the press does not test.

**Appendix E, *Glossary***\
Defines the terms the book uses, with the chapter that treats each one.

**Appendix F, *Index of subjects***\
Lists the subjects of the book with the chapters, appendixes, and Preface where they appear. The press generates it from *config/index-terms.yaml* on every build.

A Colophon at the very end describes the animal on the cover and how we made the book.

## Conventions used in this book {-}

This book uses the following typographical conventions:

*Italic*
:   Marks filenames, directory names, URLs, and the titles of books, and new terms where the text defines them.

`Constant width`
:   Marks commands, options, configuration keys, values, environment variables, and the contents of files, and, in examples, the output of commands.

*`Constant width italic`*
:   Marks, in running text, a value you supply yourself, such as *`file`* in `press art accept` *`file`*. In a syntax line, a word in angle brackets, such as `<name>`, plays the same part.

`$`
:   The shell prompt for an ordinary user. A `#` prompt means that the command must run as root. The few commands in this book that need root run through `sudo` at an ordinary `$` prompt. Inside a file, such as a YAML file or a Makefile, a leading `#` begins a comment and is not a prompt.

`[ ]`, `|`, and `...`
:   In syntax lines, square brackets enclose an optional item, a vertical bar separates alternatives of which you choose one, and three periods mark an item you may repeat. In an example, a line that holds only `...` marks output that the example leaves out. A message shown on more than one line in this book is one line in the terminal.

Tip
:   A short paragraph set off from the text that opens with the word Tip gives a suggestion or a shortcut.

Warning
:   A short paragraph set off from the text and opened by the word Warning marks a step that can cost you work. The same step can send a broken artifact to a printer. A warning always comes before the step it protects.

Sidebar
:   A longer boxed passage under a bold title tells a piece of history, a production failure, or the reasoning behind a rule. You can skip a sidebar and lose nothing you need to build a book.

Figure 2.1
:   Figures, tables, and examples carry numbers by chapter, or by letter in an appendix (Table B.1). Figure 2.1 is the first figure in Chapter 2, and Table 2.1 and Example 2.1 are the first table and example there. The press numbers the figures and builds the List of Figures from them. We number the tables and examples by hand in the same form so that the three agree. Plates, the engravings in some chapters, carry no number and appear in the List of Plates.

Print edition
:   The press names the eight editions it produces, and this book uses its names. Four of them are the Print edition (PDF), the Circulating edition (EPUB), the Single-leaf edition (one self-contained HTML file), and the Chapter edition (the reader site and its zip). The other four are the Manuscript edition (the stitched Markdown), the Telegraphic edition (plain text), the Office edition (DOCX), and the Source edition (the source zip).

Two more conventions concern cross-references and versions. The press numbers figures and resolves references to them itself, but it has no cross-references to chapters or sections. We typed every reference to a chapter, a section, a table, or an example by hand. By the press's own second law, such references are a convention, the weakest kind of guard, and you should trust them accordingly. A version number in the text comes with the phrase "at the time of this writing", because the press will move on after the book goes to print.

Every example follows one cast. The sample book is *Alice's Adventures in Wonderland*, slug `alice`, kept by the user `alice` on the workstation `hatter`. Its CI runs on the host `printshop`, and its repository belongs to the owner `wonderland-press`. We call it the *Alice book*. The press repository carries *the press's own three-chapter Alice example*, the opening chapters of the same novel, and every real capture in this book comes from it. Wherever the text shows output from the three-chapter example, it says so.

## Using code examples {-}

This book is here to help you get your books built. In general, you may quote the text of this book and reuse its examples in your own books and build scripts without permission. Reproducing a substantial part of the book requires the publisher's consent.

We appreciate, but do not require, attribution. An attribution usually includes the title, the author, and the copyright line, for example: "*Publishing with Press*, by Clint Ecker. Copyright 2026 Clint Ecker."

The press itself has a license of its own, MIT, for "code and bundled content alike". Its README says: "A book you make with the press is yours entirely." Nothing in this book changes those terms.

We wrote the examples against press 3.0.2, the current release at the time of this writing. Commands, options, and messages can change between releases. If an example fails on a later release, check `press --help` and Appendix A, *Command reference*, against the version you run, and then tell us.

## How to contact us {-}

We checked the information in this book against the fact base, which came from the press's source and its documentation, and the press checked the book against its own rules. You may still find that a feature changed after the book went to print, or that we made a mistake. Please tell us about any error you find, and about anything you would like to see in the next printing.

The book's repository has an issue tracker, and that is the place for errata, questions about the text, and suggestions:

*https://github.com/clintecker/publishing-with-press/issues*

The press keeps its own documentation on the Web, built from the press repository by its own CI. Look there when a command behaves differently from the way this book describes it:

*https://clintecker.github.io/press/*

The book's *Pages site*, which the press built from this manuscript and GitHub Pages serves, carries every edition of the book:

*https://clintecker.github.io/publishing-with-press*

A fault in the press itself, as distinct from a fault in this book's account of it, belongs in the press's own repository, `clintecker/press` on GitHub. When you report one, include the output of `press doctor` and the message the press printed, exactly as it printed it.

## Acknowledgments {-}

A book about a program that builds books depends on the program, and on the person who keeps it. Clint Ecker maintains the press and directed the work on this book.

The machines did much of the rest. Language models drafted the text from a fact base, and the fact base came from the press source and its documentation. A squad of editorial agents then checked every chapter against that fact base and the house rules. The build machines ran `press all` more times than anyone thought to count, and the press refused the book each time it broke a rule.

Lewis Carroll supplied the sample text. His book is long out of copyright. We thank him for a manuscript that never once missed a deadline.

Finally, we thank in advance the reader who files the first erratum. We checked every chapter, and we expect that you will find something anyway.

![The shop at morning: a small press at the start of a build](assets/woodcuts/the-shop-at-morning.png){place=frontispiece}

<!-- art: a small nineteenth-century print shop at the start of the working day, seen from the doorway at eye level with correct one-point perspective and a level floor: a row of type cases on the left, a compact brass hand press with a lever and a platen in the centre, a long proofing table on the right under a tall window, morning light in parallel hatched rays, one apprentice in an apron carrying a chase of locked type toward the press, a second figure at the far table reading a sheet, shelves of bound volumes along the back wall; landscape composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->
