# Registrations

::: {.in-this-chapter}
> **In this chapter:**
>
> - The governing rule
> - ISBNs
> - ISSN and LCCN
> - The retail flag
> - Preassigned control numbers
> - ONIX
> - Looking numbers up
> - Where each number goes
> - Order of operations
:::

A book for sale carries numbers that other people issue. Each edition needs an ISBN. Many books also carry an LCCN from the Library of Congress, and a serial carries an ISSN. The press cannot buy any of these numbers, and it does not try. It checks the numbers you give it, writes them into every artifact that needs them, and assembles the fields that each agency's form asks for. The Alice book has no registrations yet, so user `alice` works through each flow on `hatter` with the press's own examples and the placeholder `pending`.

## The governing rule

A *registration* is a number that an outside agency assigns to your book and that the book must then carry. The registrations skill, which comes with the press, states the rule for all of them in one sentence: "The press never issues a number over the network." The skill then separates three activities, which Table 13.1 lists.

| Activity | Who acts | Meaning |
|------------------|------------------|----------------------------------------------------|
| Issuance | You | You buy a number from an agency. No press target does this. |
| Metadata submission | The press, then you | The press assembles the fields that an agency asks for. You send them through the agency's own form. |
| Read-only lookup | The press, on request | The press asks a public catalog about a number that you already hold. It runs only when you ask for it. |

Table: Table 13.1. The three registration activities

Every number lives in *config/metadata.yaml*, under the key `registrations`. The numbers are ordinary fields, so `press config` reads, writes, and validates them like the title or the slug. Chapter 3, *The shape of a book repository*, describes that command.

A number that is still on order can stand as the word `pending`. The skill calls it "the one honest placeholder". The press renders it as `[pending]`. Example 13.1 shows the Alice book with both of its ISBNs still on order.

**Example 13.1. Two ISBNs on order**

```text
registrations:
  isbn:
    print: pending
    epub: pending
```

You can build, check, and verify the Alice book with Example 13.1 in place. The section "The retail flag" later in this chapter explains how to keep a pending number out of a book for sale.

## ISBNs

An ISBN identifies one edition of one book, so the printed book and the Circulating edition (the EPUB) each need their own. The press documentation states where the numbers come from: "there is no API that issues ISBNs; you buy a prefix, then assign from it offline". The agency sells you a block of numbers that share a prefix. After that, you assign each number in the block yourself, one to each edition.

::: {.warning}
> **Warning:** Do not take the free ISBN that KDP offers. The registrations skill tells you to buy your own block instead, and it names the Bowker 10-pack.
:::

### The ISBN block

You describe your block to the press under `registrations.isbn-block`, with the prefix and the size that the agency gave you. Example 13.2 shows the press's example block. It is not a block that the Alice book owns, so `alice` types the numbers from her own agency's receipt in its place.

**Example 13.2. An ISBN block in config/metadata.yaml**

```text
registrations:
  isbn-block:
    prefix: "978-1-960780"
    size: 100
```

The press holds the block to three rules. The prefix starts with 978 or 979. The documentation lists sizes of 10, 100, and 1,000, and the code accepts sizes from 10 through 1,000,000. The prefix must have exactly `12 - log10(size)` digits, hyphens aside.

The example prefix holds ten digits, and a block of 100 needs `12 - 2` of them. The rule leaves two digits for the publication number, which is room for a hundred titles. Prefix and publication number make twelve digits, and the thirteenth is the check digit.

The checker refuses a malformed block. The press does not validate an incomplete block, one with the prefix or the size missing. The press cannot judge a prefix until it knows the size that goes with it.

::: {.tip}
> **Tip:** Set the prefix and the size in the same sitting. A block with only one of the two passes the checker without inspection. The checker then says nothing about a wrong prefix.
:::

### Status and assignment

The target `press isbn status` reports on the block. In a fresh scaffold of the Alice book, with no block yet, it says so and tells you what to set. Example 13.3 shows that run, with the output broken into three lines to fit the page.

**Example 13.3. The status of a fresh scaffold with no ISBN block**

```text
$ press isbn status
no registrations.isbn-block configured; set the prefix and
size your ISBN agency gave you (e.g. prefix: 978-1-960780,
size: 100)
```

With a block in place, the same target prints one line in the form `ISBN block {prefix} (size N): X assigned, Y free`. Run it before every assignment, so that you know how much of the block you have left.

The target `press isbn assign` takes the edition, `print` or `epub`. It mints the lowest unused publication number and computes the check digit, the EAN-13 digit that Chapter 12, *The print pack*, works through by hand. Then it joins the parts with hyphens, as `{prefix}-{publication}-{check}`. The target writes the result through the validated path of `press config`, the same check that any `press config set` passes. A print number goes to the key `registrations.isbn.print`, and the EPUB number goes to the key `registrations.isbn.epub` beside it.

Two cases stop the assignment. If the edition already holds a number other than `pending`, the press refuses and tells you to "unset it first to reassign". If the block has no free numbers left, the press refuses with "Buy another prefix from your agency".

::: {.warning}
> **Warning:** Do not unset an ISBN that appears on a printed copy or in a retailer's catalog. The press lets you reassign after an unset, but it cannot recall the copies that carry the old number.
:::

## ISSN and LCCN

An ISSN identifies a serial, such as a journal or a numbered series. A book that has one stores it in `registrations.issn`, with a command such as `press config set registrations.issn <number>`. The press tests an ISSN with a mod-11 check, and Example 13.4 works the number that the press's selftest uses as its valid case, 0378-5955.

**Example 13.4. The mod-11 check for ISSN 0378-5955**

```text
digit    0   3   7   8   5   9   5
weight   8   7   6   5   4   3   2
product  0  21  42  40  20  27  10   sum 160

160 mod 11 = 6
check = 11 - 6 = 5          ISSN 0378-5955
```

The selftest's two invalid cases are 0378-5954, whose check digit should be 5, and 123X-5678.

An LCCN, the Library of Congress Control Number, has no check digit at all. The press can check only its shape. Before it does, the press normalizes the number in three ways. It removes blanks. It drops a slash and anything after the slash. When the number has a hyphen, it fills the serial part after the hyphen with leading zeros to six digits.

Table 13.2 gathers the checks for all four numbers.

| Number | Check | Meaning |
|------------|------------------------|--------------------------------------------------|
| ISBN-13 | EAN-13 check digit | The thirteenth digit must match the weighted sum of the first twelve. Chapter 12 gives the formula. |
| ISBN-10 | Mod-11 check | The press can compute the older ten-digit form. It returns none for a 979 prefix. |
| ISSN | Mod-11 check, weights 8 to 2 | The eighth character must match the sum. A check value of 10 appears as `X`. |
| LCCN | Shape only | After normalization, the number must match `[a-z]{0,3}\d{8,12}`: up to three lowercase letters, then eight to twelve digits. |

Table: Table 13.2. How the press checks each number

A self-publisher gets an LCCN through the Preassigned Control Number (PCN) program. The Library of Congress runs it through a service called PrePub Book Link. The Library's other program, Cataloging in Publication (CIP), is not open to a self-publisher, as the press's PCN listing reminds you. The section "Preassigned control numbers" later in this chapter shows how the press prepares the PCN form.

## The retail flag

A pending number is useful while the book is in production and wrong in a book for sale. The key `registrations.retail` tells the press which of the two you build. When it is `false`, the default, a missing or pending number produces only advice.

When it is `true`, the book must carry two real ISBNs, one for `print` and one for `epub`. A missing ISBN appears in the refusal as `isbn print missing` or `isbn epub missing`, and a pending one appears as pending. A book need not declare an LCCN or an ISSN. If it declares either one, the number must be real, because a `pending` LCCN or ISSN also appears in the refusal. The refusal reads as follows, broken here to fit the page:

```text
retail edition declared while registrations are absent or
pending: <list>
```

The `<list>` holds the entries at fault. If `alice` sets the flag while Example 13.1 is still in place, `press check` refuses the book with both of them.

::: {.sidebar}
> **Why pending is a word**
>
> A book in production often waits on a number. The ISBN agency already has your money, or the PCN form is still with the Library. There are two ways to keep building in the meantime. You can type a number you expect to receive, or you can type the word `pending`. The press gives the second a name and a rule.
>
> A guessed number looks like a real one on every page that it reaches. Nothing in the artifact tells a reader or a distributor that it is wrong. The word `pending` prints as `[pending]`, which nobody mistakes for an ISBN. The cover wrap follows the same reasoning, with a box that reads `[ISBN pending]` where the bars will go. The retail flag then closes the gap at the other end. Once you declare a retail edition, a pending number makes the checker refuse the book.
:::

Set the flag when you prepare the release. Then run the checker, and rebuild every edition so that the numbers reach the artifacts:

```text
$ press config set registrations.retail true
$ press check
$ press all
```

## Preassigned control numbers

The target `press pcn` assembles the field values for the PrePub Book Link form. It reads them from the book's metadata and prints them as a list. It never contacts the Library of Congress. You copy the values into the form yourself, so the submission stays in your hands.

Example 13.5 shows the target in a fresh scaffold made with `press new alice --author "Lewis Carroll"`, before the changes of Chapters 3 and 10, and before you set any registration. The values come from the book's metadata, and the labels and the layout are the press's. The author and the publisher are both Lewis Carroll, because the scaffold uses the author as the publisher by default. Example 13.5 breaks two long lines to fit the page and omits the closing advice, which the next paragraph quotes.

**Example 13.5. The PCN field values for a fresh Alice scaffold**

```text
$ press pcn
Library of Congress PCN -- PrePub Book Link field values
https://www.loc.gov/publish/pcn/
    (self-publishers use PCN, not CIP)

  Title                          alice
  Subtitle                       A subtitle
  Author(s)                      Lewis Carroll
  Publisher name                 Lewis Carroll
  Place of publication           Earth
  Projected year of publication  2026
  Print ISBN
    (assign one first: press isbn assign print)
  Language                       en-US
  Medium                         print (monograph)

...
(also written to dist/alice-pcn.txt)
```

The two omitted lines matter. The first tells you what to do after you submit: "No LCCN recorded yet. Submit the fields above through PrePub Book Link; when the LCCN comes back, store it with `press config set registrations.lccn <number>`." The second states the obligations: "a self-publisher is eligible for a PCN (not CIP), and a copy of the published book must be deposited with the Library of Congress within three months of publication."

A field with no value in the metadata prints as `(needed on the form)`. You see the gap in the listing before the Library sees it on the form. The fresh scaffold shows a different gap. Its title is the slug, its subtitle reads "A subtitle", and its place of publication is "Earth", the scaffold's default.[^13-earth] All three are placeholders. Chapters 3 and 10 replace them in the Alice book with its full title, its double subtitle, the publisher Wonderland Press, and the place Oxford. The target also writes the listing to *dist/alice-pcn.txt*, so you can keep it with your records.

::: {.tip}
> **Tip:** Run `press isbn assign print` before `press pcn`. The form asks for the print ISBN, and the listing shows a reminder in its place until the number exists.
:::

::: {.warning}
> **Warning:** Put the deposit date in your calendar on the day of publication. The press records the obligation in the PCN listing, but it does not track the three months for you.
:::

## ONIX

Distributors and retailers take book metadata in ONIX, the trade's XML format for product records. For the Alice book, the target `press onix` writes an ONIX 3.0 record to *dist/alice.onix.xml*. With the option `--forthcoming`, the record describes a forthcoming book, announced and not yet on sale. Table 13.3 lists the main elements that the press writes and where their values come from.

| Element | Value | Meaning |
|--------------------------------|------------------|----------------------------------------------|
| `ONIXMessage` | `release="3.0"` | The message uses the ONIX 3.0 reference namespace, *http://ns.editeur.org/onix/3.0/reference*. |
| `Sender/SenderName` | the publisher | The press writes the book's publisher, or the word "press" when the book names none. |
| `SentDateTime` | `YYYYMMDDTHHMM` | The element holds a date and time, to the minute. |
| `RecordReference` | `{base}/{slug}-{label}` | The base is the book's `site-url`. Without one, the press uses the `repository`, and without that, `press:` and the slug. |
| `ProductIdentifier` | `ProductIDType 15` | The element holds the product's ISBN-13. |
| `ProductComposition` | `00` | The press writes the same value for every product. |
| `ProductForm` | `BB`, `BC`, `EA` | `BB` is a hardback, for a casewrap or dust-jacket binding. `BC` is a paperback, for any other binding. `EA` is the Circulating edition (EPUB). |
| `TitleType` | `01` | The element marks the book's title. |
| `Contributor` | `ContributorRole A01` | The element names the author, with the ONIX role code for an author. |
| `Language` | `LanguageRole 01` | The element holds the ISO 639-2/B code that the press maps from the book's `lang`. The press maps 13 languages and omits the element for any other. |
| `Publisher` | `PublishingRole 01` | The element names the publisher, with `CityOfPublication` beside it. |
| `PublishingStatus` | `04`, `02` | The status is `04`, active, unless you give `--forthcoming`, which writes `02`. |
| `PublishingDate` | role 01, `dateformat="05"` | The element holds the year of publication only. |

Table: Table 13.3. The main ONIX elements that press onix writes

The Alice book has a `site-url`, so its record references begin with *https://wonderland-press.github.io/alice/*. Its default binding is perfect-bound, so its print product is a `BC`.

The registrations decide which products appear. The print product is always in the record, even before it has an ISBN. The EPUB product appears only when the book holds an EPUB ISBN. A book with no EPUB ISBN sends a distributor a print product only, which is an accurate account of the book.

One element is missing on purpose. The record carries no price, because "a book repository holds no price, by design".

## Looking numbers up

The target `press lookup` asks a public catalog about an LCCN or an ISSN. Its synopsis takes the kind of number and an optional number:

```text
press lookup lccn|issn [<number>]
```

The documentation describes it as "the one command that reaches the network; ordinary builds never do. It is never an issuance path." With a number on the command line, the target looks up that number. Without one, it looks up the number in `registrations.lccn` or `registrations.issn`. An LCCN goes to *https://lccn.loc.gov/{lccn}/mods*, which returns a MODS XML record. An ISSN goes to *https://portal.issn.org/resource/ISSN/{issn}*, which returns JSON-LD.

The lookup talks to servers that the press does not control, so it holds every request to fixed limits. Table 13.4 lists them.

| Limit | Value | Meaning |
|--------------------|---------------|----------------------------------------------------|
| Timeout | 10 seconds | The press abandons a request that takes longer. |
| Retries | 2 | The press retries only after a timeout, a connection error, or a 5xx status. |
| Redirects | 3 at most | A longer chain of redirects ends the request. |
| Response size | 512 KiB | The press reads no more than this from any response. |
| XML declarations | refused | The press refuses XML that holds `<!DOCTYPE` or `<!ENTITY`, and it does not parse it. A catalog record needs neither. |
| Media types | allow-listed | The press accepts only the response types it expects. |

Table: Table 13.4. The limits on press lookup

The press identifies itself to the catalogs with a fixed User-Agent string.[^13-agent]

A lookup ends in one of six outcomes: `found`, `not-found`, `ambiguous`, `mismatch`, `invalid`, or `unavailable`. Only `found` exits 0, so a script can test the exit status and stop on anything else. The Alice book has no LCCN and no ISSN, so `alice` has nothing to look up yet. Once she holds an LCCN, she can run `press lookup lccn` with it.

::: {.tip}
> **Tip:** Give a number on the command line to look it up before you store it. If the catalog holds a record for that number, the lookup ends `found`.
:::

## Where each number goes

The first law of the press reads "Facts are stated once." A registration is a fact of exactly that kind, and the book records it in one place, the `registrations` block. The press then carries each number into every artifact that needs it. @fig:where-numbers-land shows the routes.

![Where each registration number goes](assets/woodcuts/13-01-where-numbers-land.png){#fig:where-numbers-land .diagram width=full-measure fig-alt="A diagram with the registrations block of metadata.yaml on the left and five destinations on the right: the copyright page, the EPUB metadata, the wrap barcode, the ONIX file, and the PCN listing. Each arrow is labeled with the field it carries."}

<!-- art: ARCHETYPE data-flow, drawn left to right. Left: one dog-eared file icon, "config/metadata.yaml", with a boxed excerpt below it headed "registrations:" listing in small monospace, top to bottom, "isbn.print", "isbn.epub", "lccn", "issn". Right: five boxes in a vertical stack, top to bottom: "copyright page" (a small page outline), "EPUB metadata" (file icon "content.opf"), "wrap barcode" (small EAN-13 bars), "ONIX file" (file icon "dist/alice.onix.xml"), "PCN listing" (file icon "dist/alice-pcn.txt"). Arrows, labels in small monospace: to copyright page "isbn.print, isbn.epub, lccn". To EPUB metadata "isbn.epub as urn:isbn:". To wrap barcode "isbn.print as EAN-13". To ONIX file "isbn.print, isbn.epub as ProductIDType 15". To PCN listing "isbn.print". Give "registrations:" a 20% gray fill. The reader should see first that one block feeds all five. -->

The print ISBN goes to the most places. It prints on the copyright page (the press calls it the colophon) and drives the EAN-13 barcode on the cover wrap. It also identifies the print product in the ONIX record and fills the Print ISBN field of the PCN listing.

The EPUB ISBN becomes the identifier of the Circulating edition. The press writes it as `urn:isbn:` and the number. It also adds the EPUB product to the ONIX record. The EPUB verifier reads the package file and confirms the identifier, as Chapter 8, *Verifying the artifacts*, describes.

The copyright page carries one line for each ISBN the book declares and one for the LCCN. The ISSN does not print there. Chapter 10, *Front matter, the index, and the table of authorities*, shows those lines. A pending number prints there as `[pending]`. The barcode carries only the print ISBN, and the EPUB identifier carries only the EPUB ISBN. Every route starts at the same block, so the copyright page cannot show a print ISBN that differs from the barcode's, or an EPUB ISBN that differs from the EPUB identifier.

## Order of operations

To register the Alice book, `alice` takes the steps in the order that the registrations skill gives:

1. Buy an ISBN block from your agency.
2. Record its prefix and size under `registrations.isbn-block`.
3. Assign the two ISBNs:

   ```text
   $ press isbn assign print
   $ press isbn assign epub
   ```

4. Assemble the PCN fields:

   ```text
   $ press pcn
   ```

5. Submit the fields through PrePub Book Link.
6. When the LCCN comes back, store it:

   ```text
   $ press config set registrations.lccn <number>
   ```

7. Write the ONIX record for your distributors:

   ```text
   $ press onix
   ```

8. Declare the retail edition, check the book, and rebuild it:

   ```text
   $ press config set registrations.retail true
   $ press check
   $ press all
   ```

The ISBN comes before the PCN form because the form asks for it. The retail flag comes last. Once it is set, the checker refuses the book while either ISBN is absent or pending, or while a declared LCCN or ISSN is still pending. The skill's order names no step for an ISSN.

A publisher with CIP data from the Library prints it as a block on the copyright page. The press does not generate that block. If your book has one, it goes in a hand-authored *tex/title-page.tex*, which replaces the generated front matter as Chapter 10 describes.

[^13-earth]: The scaffold's default for the place is accurate, as far as it goes.

[^13-agent]: The string is `press-registrations-lookup (+https://github.com/clintecker/press)`.
