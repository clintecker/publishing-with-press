## 10. The print pack

### 10.1 Four orthogonal choices

| Choice | Key | Default | Controls |
|---|---|---|---|
| Trim & interior | `print.profile` | `house-6x9` | page size and interior geometry |
| Binding | `print.binding` | `perfect-bound` | the cover's topology (spine, flaps) |
| Cover material | `print.material` | `paperback` | the cover treatment (cloth vs printed) |
| Provider | `print.provider` | `house` | the spine, bleed, and wrap **numbers** |

Source: `docs/PRINT-FORMATS.md`.

```sh
press config set print.profile novella-5x8 && \
press config set print.provider lulu && \
press config set print.binding casewrap && \
press config set print.material casewrap
```

- **Bindings.**
  - `perfect-bound`: back · spine · front.
  - `saddle-stitch` and `coil`: no spine.
  - `casewrap`: a hardcover printed on the board, with board turn-in and hinge.
  - `dust-jacket`: a jacket with flaps.
- **Materials.**
  - `paperback` and `casewrap` are printed.
  - `linen`: the printed field is suppressed and only the jacket is printed. "Press never bakes a simulated cloth texture into a real linen cover."
- **Refusals.** `press check` refuses an unsupported trim, binding, or ink combination before any render. The message comes from `ProviderSpec.check_selection`.

### 10.2 Design profiles

The table is in §7.2, with full numbers in the profile files under `src/press/data/profiles/`. Which providers cut each trim (`docs/PRINT-FORMATS.md`):

| Profile | Trim | For | Cut by |
| --- | --- | --- | --- |
| `house-6x9` | 6×9 | the sealed house default | lulu, kdp, ingramspark |
| `house-6x9-color` | 6×9 | a colour interior on the house geometry | kdp |
| `novella-5x8` | 5×8 | a short novel / novella | lulu, kdp, ingramspark |
| `digest-5.5x8.5` | 5.5×8.5 | trade-paperback genre fiction | lulu, kdp, ingramspark |
| `mass-market-4.25x6.87` | 4.25×6.87 | rack-sized genre paperback | lulu |
| `large-print-7x10` | 7×10 | large-print / accessibility | lulu, kdp, ingramspark |

**Profile mechanics** (`src/press/profiles.py`):

- `ink` is `single` or `color`.
- An unknown id fails with `unknown print profile '<id>'; available: ...`.
- `digest()` is the first 16 hex characters of a sha256 over id, design-major, trim, interior, and web, plus ink when it is not single.

**Seals** live in `src/press/data/profile-seals.yaml`. All six are at `design-major: 1`, `qualified-on: '2026-07-25'`. The house-6x9 digest is `c524978840a0af4e`.

**Colour.** `house-6x9-color` is "the 6×9 house geometry, byte-for-byte, with one difference: the interior prints in colour".

- It lifts the print verifier's single-ink rule.
- It keeps plates in colour instead of greying them at intake.
- It must be paired with a provider that documents a colour caliper, which today means **KDP** only.
- `print.color-grade` takes `standard-color` (default) or `premium-color`.

### 10.3 Profile lifecycle (contributors, not authors)

`docs/PROFILE-LIFECYCLE.md` and the `profile-lifecycle` skill:

```text
usage: python3 -m press.profile_lifecycle validate
       python3 -m press.profile_lifecycle scaffold <id> --trim WxH [--ink single|color] [--from <base>]
       python3 -m press.profile_lifecycle seal <id> [--note "why"]
       python3 -m press.profile_lifecycle list
```

1. **Scaffold** from proven geometry. The default base is `house-6x9`. Scaffolding never clobbers an existing profile.
2. **Prove** with the golden-copy geometry test. It renders every shipped profile at its declared trim: `tests/test_visual_regression.py::test_profile_renders_at_its_declared_trim`.
3. **Seal.** The digest is read from the profile itself, so "you can never seal a geometry the profile does not actually have".
4. **Commit** the profile YAML and the seal ledger together.

From then on, `check_profile_seals` in selftest turns red on drift.

### 10.4 Provider specs and spine math (`src/press/provider_specs.py`, `src/press/data/provider-specs/*.yaml`)

**Spine shapes:**

- `constant`: `pages * caliper[stock] + allowance` (KDP, and house).
- `divisor`: `pages / divisor + allowance` (Lulu paperback; stock-independent).
- `ppi-table`: `pages / ppi[stock]` (IngramSpark).
- `lookup`: a stepped table keyed by page-count band (Lulu hardcover).

| Provider | Spine | Bleed / safety | Bindings | Trims | Page bounds |
|---|---|---|---|---|---|
| `house` (default) | constant; white 0.002252, cream 0.0025 in/page; allowance 0.0 ("v1 value; real specs use 0.06") | 0.125 | perfect-bound, saddle-stitch, coil; no catalog (refuses nothing) | none | none |
| `kdp` (verified 2026-07-21) | constant; white 0.002252, cream 0.0025, standard-color 0.002252, premium-color 0.002347; allowance 0.06 | 0.125 / 0.25 | perfect-bound; casewrap (margin 0.5906 "15mm wrap", hinge 0.3937 "10mm hinge"); **no** dust jacket, linen, saddle, or coil | 5×8 (PB only), 5.5×8.5, 6×9, 6.14×9.21, 7×10, 8.25×11 | PB 24–828, casewrap 75–550 |
| `lulu` | paperback `pages/444 + 0.06`; hardcover lookup of 26 bands (24–84 pages → 0.25in; 85–140 → 0.5; +0.0625 per band; to 779–800 → 2.0625) | 0.125 / 0.5 | perfect-bound, saddle-stitch, coil, casewrap (margin 0.75, hinge 0.25), dust-jacket (flap 3.25, strip 0.25; UNCONFIRMED) | 13 trims, Pocketbook 4.25×6.875 to US Letter 8.5×11 | PB 32–800, saddle 4–88, coil 2–470, hardcover 24–800 |
| `ingramspark` | ppi-table; cream 444, white 512, white-70 377, groundwood 400 | 0.125 / 0.25 | perfect-bound, casewrap (margin 0.625, hinge 0.5; "OFFICIAL" formula), dust-jacket | 9 trims | 18–1200 PB, 18–1050 hardcover |

**Computed spine widths** (inches; cream unless noted):

| pages | house | KDP | KDP white | Lulu PB | Ingram cream | Ingram white | Lulu hardcover |
|---|---|---|---|---|---|---|---|
| 100 | 0.25 | 0.31 | 0.2852 | 0.2852 | 0.2252 | 0.1953 | 0.5 |
| 200 | 0.5 | 0.56 | 0.5104 | 0.5105 | 0.4505 | 0.3906 | 0.75 |
| 400 | 1.0 | 1.06 | 0.9608 | 0.9609 | 0.9009 | 0.7812 | 1.1875 |

**Where the provider data comes from.** It is one reviewed ledger, `quality/providers.yaml`; the copy shipped in the wheel is generated from it (§10.8). "Ingram is the one vendor whose casewrap and jacket TOTAL formulas are officially published."

### 10.5 The cover wrap (`src/press/gen_coverwrap.py`)

**Build.** `press coverwrap` builds `print` first. The page count is read from the interior with pypdf.

**Requirements:**

- `assets/cover.jpg` ("coverwrap needs assets/cover.jpg");
- metadata title, author, publisher, publisher-place.

**Layout**, left to right: `[margin][inner][back][spine][front][inner][margin]`.

```text
panel_w = trim_w + width_delta
wrap_w = 2 * margin + 2 * inner + 2 * panel_w + spine
wrap_h = 2 * margin + trim_h + height_delta
back_x = margin + inner
front_x = back_x + panel_w + spine
```

- `BLEED_IN = 0.125`, "universal across print vendors".
- `inner = hinge + flap + strip`.

**Example wraps** (6×9, 200 pages, cream):

| provider / binding | spine | wrap |
|---|---|---|
| house perfect-bound | 0.5 | 12.75 × 9.25 |
| KDP perfect-bound | 0.56 | 12.81 × 9.25 |
| Lulu perfect-bound | 0.5105 | 12.7605 × 9.25 |
| Lulu casewrap | 0.75 | 15.0 × 10.75 |
| Lulu dust-jacket | 0.75 | 20.0 × 9.25 |
| Ingram casewrap | 0.4505 | 14.3305 × 10.5 |
| house saddle-stitch | 0 | 12.25 × 9.25 |

**Barcode.**

- An EAN-13 sits lower right of the back panel, 0.5in in from the spine fold and 0.5in up, anchored `south east`, on a white card.
- Module width is 0.0130in, "100% EAN magnification is 0.33mm", so 95 modules come to about 1.235in. Bars are 0.9in tall.
- The TikZ node uses `inner sep=0`. This is the v2.3.1 fix (#210): the old default padding pushed the first guard bar into the left quiet zone.
- With no ISBN: a 2in × 1.2in white box reading `[ISBN pending]`, "an honest placeholder".

**Spine text.** Drawn only when the spine is at least 0.25in. The providers' declared spine-text minimums (KDP 79 pages, Lulu 81, Ingram 48) are not used.

**Cloth field.** `black!85!red!25!white`, RGB (201,191,191). It is dropped for linen.

**Logo.** 1.1in wide.

**Image caps.** Cover art is capped at `590 × wrap_h` px and the logo at 649 px, flattened by `print_safe.prepare_cover` into `build/coverwrap-assets/`.

**Compile and check.** Built with `latexmk -lualatex -interaction=nonstopmode coverwrap.tex` in `build/coverwrap`, then the mediabox is checked within 0.01in.

### 10.6 Barcode arithmetic and the wrap verifier

**EAN-13** (`src/press/barcode.py`).

- The check digit weights alternate 1 and 3: `(10 - total % 10) % 10`.
- The pattern is `"101" + left + "01010" + right + "101"`, with L/G parity chosen by the first digit.
- A bad check digit is refused, because "a mistyped ISBN on a cover is unrecoverable".
- The selftest canonical example is ISBN `978-0-306-40615-7`.

**`verify_coverwrap`** checks, in order:

1. one page;
2. size equals `layout(pages)` within ±0.01in;
3. fonts embedded;
4. no `/SMask` image: "coverwrap embeds N image(s) with transparency (a soft mask); a print preflight flags it...";
5. no image over 600 PPI, via `pdfimages`, otherwise a note;
6. the title survives as text;
7. a 150dpi `pdftoppm` render that is not blank;
8. a front panel with stddev of at least 8, otherwise "the cover art did not survive";
9. a barcode white card (some pixel >245) and marks (some pixel <70);
10. with an ISBN, at least 25 transitions and clean quiet zones.

Success line:

```text
Verified <wrap>: one page, W x H in (N-page spine), embedded fonts, no transparency, images under 600 PPI, front art present, title survives, barcode: EAN-13 readable with quiet zones | honest placeholder present
```

### 10.7 Print-safe images (`src/press/print_safe.py`)

The print build flattens every image onto white and caps its resolution, so a vendor preflight sees no transparency and no over-resolution.

- **Caps:** logo long edge 1000px; figures 1900px (about 300 PPI at 6.3in).
- **Conversion:** grayscale is kept; JPEG is written at q88, PNG otherwise.
- **Output:** `build/print-assets/`.
- **Image paths:** `print-safe-images.lua` points interior images there.

History (`docs/LULU.md`): Lulu once flagged *transparency* (the logomark is ink on transparency) and *images over 600 PPI*, because a 1024px logo at 1.7in is about 602 PPI. "a current `press verify-print` interior triggers **neither** warning". A custom `tex/title-page-print.tex` should point its logo at `build/print-assets/`.

### 10.8 Providers, qualification, and ordering

**The ledger.** `quality/providers.yaml` is canonical. `src/press/data/providers.yaml` is a generated projection: a banner followed by the canonical bytes, compared byte-for-byte, regenerated by `python3 -m press selftest --write-docs`. "Never edit it by hand" (`docs/PROVIDER-DATA.md`).

**Vocabulary** (`qualification.py`).

- **Dispositions:** primary, secondary, hosted-candidate, candidate, not-fit.
- **Capability values:** supported, unsupported, by_approval, unknown.
- **The 11 capabilities:** api, sandbox, one_copy_pod, file_validation, pricing_api, order_creation, shipping, cancellation, webhooks, worldwide, seller_of_record.

**The researched providers:**

| Provider | Disposition |
|---|---|
| lulu | primary |
| bookvault | secondary |
| peecho | hosted-candidate (the only one with seller_of_record supported) |
| mixam | candidate |
| cloudprinter | candidate |
| prodigi | candidate |
| onpress | not-fit |
| print-bind-ship | not-fit |
| 48-hour-books | not-fit (10-copy minimum) |

"A provider here is *researched*, not *qualified*" (`docs/PROVIDER-QUALIFICATION.md`).

**The 11-point physical checklist**, verbatim:

| | |
|---|---|
| **content** | the interior text matches the release-approved manuscript |
| **pagination** | page count and page order match the manifest |
| **trim** | the cut size matches the declared trim within tolerance |
| **bleed** | full-bleed art reaches the trimmed edge without white slivers |
| **spine** | spine text is centred and square for the page count |
| **barcode** | the EAN-13 scans and matches the declared ISBN |
| **color** | single-ink interior and cover reproduce as specified |
| **paper** | stock weight and shade match the declared paper |
| **binding** | the binding is square, tight, and opens flat enough to read |
| **packaging** | the copy arrives undamaged and appropriately protected |
| **tracking** | the tracking link resolves and matches the destination |

**`config/qualification.yaml`:**

```yaml
schema_version: 1
inspections:
  - provider: lulu
    product_id: "PB-BW-6x9"
    region: US
    edition_id: "<the edition_id the copy was ordered against>"
    inspector: "Your Name"
    results: {content: pass, pagination: pass, trim: pass, bleed: pass, spine: pass,
              barcode: pass, color: pass, paper: pass, binding: pass, packaging: pass, tracking: pass}
```

- Every point must pass. "A single failure does not qualify."
- An inspection is scoped to an exact `edition_id`.

**Edition identity** (`src/press/edition.py`).

- The `edition_id` is a sha256 over the production facts only: interior and cover bytes, print spec, ISBN, and toolchain digest.
- Excluded: source commit, tree state, input digests, receipts, and qualifications.
- Changing the manuscript, cover, or print spec mints a new identity, which makes the old inspection stale.
- Forbidden keys anywhere in the manifest: price, amount, cost, currency, card, cvv, secret, password, token, apikey, credential, email, address, recipient, customer, phone.
- CLI: `python3 -m press.edition verify <manifest.json> [<book-root>]`.

**Direct print ordering** (`src/press/commerce.py`, `docs/PRINT-ORDERING.md`). This is off by default.

```yaml
commerce:
  print-ordering:
    enabled: true
    edition: paperback
    storefront-url: "https://www.lulu.com/shop/..."
    seller-of-record: "Lulu"
    support-url: "https://example.test/support"   # optional; omit to generate
    policies:
      privacy: "We keep no reader data; the provider handles your order."
```

- **The CTA.** The landing page shows an accessible, script-free `<aside class="print-order">` headed "Order a print copy". It discloses the seller before the reader leaves and uses `rel="noopener noreferrer"`.
- **Generated policy pages.** If you omit a policy URL, the press generates `support.html`, `privacy.html` or `refunds.html` disclosing the seller. "press never invents legal terms."
- **`press check` refuses:**
  - a non-HTTPS URL;
  - an unnamed seller ("a hosted checkout does not imply who the legal seller is");
  - an unknown key;
  - any secret-shaped value (e.g. `sk_live`, `bearer <16+>`, `?token=`).
- **Release gate.** At the end of `press all` the gate builds `print` and `coverwrap` and computes the manifest. It then requires a passed inspection for this `edition_id`; without one it fails with "order and inspect a copy and record it in config/qualification.yaml before advertising ordering". It is advisory unless `PRESS_RELEASE=1`.
- **What press does not do:** "process or store payment, calculate tax, hold provider credentials, receive a reader's name or address, or operate a store."

**Deferred work.** The custom merchant-of-record machinery (broker, Stripe checkout, webhooks, outbox, reconciliation) is in the Icebox; the plan is `docs/DIRECT-ORDERING-PLAN.md`. Nonetheless, `src/press/providers/` exists. It holds:

- a provider-neutral contract: QUOTE, FILE_VALIDATION, SUBMIT, LOOKUP, CANCELLATION, WEBHOOKS;
- statuses created → delivered, plus rejected, canceled, error, unknown;
- money in integer minor units;
- a smart fake;
- a **Lulu Print API adapter**. Base URLs are `https://api.lulu.com` and sandbox `https://api.sandbox.lulu.com` (the default). It uses OAuth2 client credentials and verifies webhooks with `Lulu-HMAC-SHA256`. Its SKU builder turns 6×9 into `0600X0900.BW.STD.PB.060UW444.MXX`.

  It is reachable only from tests; no CLI command uses it.

### 10.9 Printing at Lulu (`docs/LULU.md`)

1. Run `press verify-print`. It writes `dist/<slug>-interior.pdf` and, if `assets/cover.jpg` exists, `dist/<slug>-coverwrap.pdf` with 0.125in bleed.
2. At Lulu, choose **Print Your Book**, then the product **Paperback, Perfect Bound**. For hardcover, set `print.provider lulu` and `print.binding casewrap|dust-jacket` first.
3. Match the settings:

   | Lulu setting | Set it to |
   | --- | --- |
   | Page size / trim | your `print.profile` trim |
   | Binding | match `print.binding` |
   | Interior color | Black & white |
   | Paper | match `print.paper` |
   | Cover finish | Glossy or Matte (your choice) |

4. Upload the interior, then the one-piece cover PDF.
5. Leave Lulu's own barcode off when `registrations.isbn.print` is set.
6. You may see the note "a white bleed margin was added". It is expected and harmless.
7. Order **one** golden copy, inspect it against the 11 points, and record the result in `config/qualification.yaml`.

Troubleshooting (verbatim):

```text
| Cover is the wrong size | Lulu product ≠ your `print.binding` | Match the binding (or set `print.binding`), rebuild |
| Spine text is off-center | Lulu paper ≠ your `print.paper` | Match the paper, rebuild |
| Transparency detected | An old upload (print-safe now flattens) | Rebuild with `press verify-print`, re-upload |
| Images over 600 PPI | An old upload (print-safe now caps PPI) | Rebuild with `press verify-print`, re-upload |
| No cover was built | No `assets/cover.jpg` | Add cover art, then `press coverwrap` |
| Fonts not embedded | Not from a press build | Rebuild with `press verify-print` |
```

Caveat: with `print.provider: lulu` the paperback spine is paper-independent, and the default provider is `house`, not lulu. See §20.

### 10.10 `press publish kdp|ingram [--report-only]` (`src/press/publish.py`)

**What it verifies.** It rebuilds and verifies four artifacts:

- "Print interior PDF (mirrored margins, black ink)";
- "Cover wrap PDF (trim + bleed, spine computed)";
- "EPUB (KDP eBook / Ingram ebook program)";
- "Marketing cover image (front board only)".

**What it writes.** The checklist goes to `dist/publish-<channel>.md`, in three sections:

- "Files the channel needs";
- "Identity the channel will ask for": print ISBN, title, subtitle, author, description, keywords;
- "Only a person can do these".

**The human-only items:**

- **KDP:** "KDP account with tax interview completed"; "Category selections (2 allowed; note 10 keyword slots)"; "Pricing per marketplace and royalty option (60% print)"; "Order a physical proof before approving publication".
- **Ingram:** "IngramSpark account and title setup fee"; "BISAC subject codes (3 allowed)"; "Wholesale discount and returns policy decisions"; "Order a physical proof before enabling distribution".

**Exit status.** It exits 1 if anything is unverified. `--report-only` marks each file "present but NOT verified (report-only)" instead.

---


### 6.7 Coverwrap verification

The wrap must be one page, and its size must equal the generator's own computed layout within 0.01in. The other checks:

- embedded fonts;
- no soft-mask transparency;
- images no more than 600 PPI;
- the title survives as text;
- not blank;
- a front panel stddev of at least 8;
- a barcode card;
- with an ISBN: at least 25 transitions on the scanline (EAN-13 has 59) and clean quiet zones.

Details are in §10.6.

---


---

# Shared context (every chapter)

### 1.4 Philosophy

**The four laws** (`docs/ARCHITECTURE.md`):

> 1. **Facts are stated once.** A book's identity lives in its config; the house design lives in press data; the artifact graph lives in the registry. If you find the same fact in two places, one of them is a bug already filed or a bug you should file.
> 2. **Generators over checkers over conventions.** Prefer machinery that produces the right thing to machinery that detects the wrong thing, and either to a sentence in a document asking people to behave.
> 3. **Artifacts are verified as objects.** A green build means the actual PDF was rendered and inspected, the actual EPUB was validated by the tool retail channels run, the actual site was crawled. Verifying without rebuilding is forbidden by construction.
> 4. **Scars become law.** Every production failure earns a mechanical guard and an entry in CLAUDE.md's scars list. Do not relearn them.

**Product laws** (`ROADMAP.md`):

- Facts are stated once and projected mechanically.
- Generators establish structure; verifiers prove artifacts as objects "rather than trusting command exit status".
- "A scar becomes an executable invariant, a named proof, or an explicit public contract—not merely a warning in prose."
- Valid output stays compatible within a major.
- Book repositories contain book facts only.
- "Trust accumulates from deterministic functions through compositions, real tools, complete workflows, consumer repositories, and release identity. A higher layer cannot erase missing proof below it."

**No book in the press.** From `CLAUDE.md`:

> There is no book in here. Every book-specific fact (title, slug, sentinels, banned vocabulary, front matter, art) lives in the book repository that consumes this package.

Also: "if a book needs machinery, the machinery belongs here". This is enforced. The integration gate requires that "no original-book identity may appear in a clean scaffold's public artifacts", and selftest `scaffold_neutrality` checks that a scaffolded book contains no "Clint Ecker" or "LGTM".

**Provenance vs verification** (`docs/ARCHITECTURE.md`):

> generation makes a fact true, verification proves it stayed true all the way into the object a reader receives.

**The pinned contract.** Books pin a tag. `vN` floats; three-part tags are immutable "and immutability is enforced, not promised". "Design is part of the contract: within a major, fixes may correct broken output but must not change typography or layout of a valid book; design and template changes require a new major." See §12.

**Non-goals** (`docs/NON-GOALS.md`). "Press is a prose engine." It is not:

- a page-layout or design application (it does not replace InDesign, Affinity, Scribus, or Quark);
- a fixed-layout picture-book, comic, or magazine designer;
- an interactive or rich-media ebook builder.

The heuristic: "a new profile of the prose engine -- another trim, a colour interior, large print -- is core press work; a new *engine* is not." The planned answer for designed interiors is the *finisher*, a supplied-interior source mode (`interior: path/to/interior.pdf`). It is planned work on the Book breadth milestone, not shipped.

**What the author owns and what the press owns** (`docs/QUICKSTART.md`):

- "Yours to decide": title, author, words, and the visual identity.
- "The press owns": build order, verification pipeline, file names, and formats.

---


## 19. War stories, scars, and design rationales (sidebar candidates)

Each entry names its source. Lines are 1-based.

1. **The infinite empty pages.** "A figure taller than the text block makes LuaLaTeX ship empty pages forever, silently, at 100% CPU." The fix caps every image at 6.3in (now per profile), and "never stack a third `titlepage`". Sources: `CLAUDE.md:178-182`; `src/press/data/tex/book-header.tex:148-186`.
2. **The missing Libertine face.** "Ubuntu has no `fonts-libertinus` package, and `--no-install-recommends` drops the Libertine keyboard face; the Dockerfile states `fonts-linuxlibertine` explicitly." Source: `CLAUDE.md:183-185`.
3. **The epubcheck that exists but cannot run.** Ubuntu's launcher needs binfmt_misc, which containers do not register. "the command exists, `which` finds it, and it dies with 'Exec format error' only at execution." The fix is a `java -jar` wrapper, and a present-but-unrunnable tool is reported as a toolchain fault. Sources: `CLAUDE.md:186-190`; `Dockerfile:41-46`; `src/press/verify_formats.py:399-440`. The Real-ESRGAN comment in the Dockerfile calls the same trap "the epubcheck/binfmt scar".
4. **The lists that would not converge.** Plain lualatex under pandoc does not run enough passes, so the build goes through latexmk. Also, `toc-depth: 1` silently empties the List of Plates; the header raises tocdepth inside the lof file. Sources: `CLAUDE.md:191-194`; `book-header.tex:104-139`.
5. **Links that overshoot.** hyperref anchors floats at the caption, so list-of-plates links overshoot the image. The fix moved from the `hypcap` package to `caption`'s `hypcap=true`. "When touching PDF links, verify destinations with pypdf". The verifier now does so. Sources: `CLAUDE.md:195-197`; `src/press/verify_pdf.py:44-104`.
6. **The chunked writer copies media itself.** Site assembly must tolerate directories that already exist (`dirs_exist_ok=True`). Sources: `CLAUDE.md:198-199`; `src/press/build.py:319-341`.
7. **JPEG plates, then PNG masters.** "Truecolor PNG barely compresses engraving grain, which is why plates were once baked JPEGs". `press art enhance` quantizes to a few grays, and intake keeps alpha PNG masters. "Do not reintroduce a baked-white JPEG master." Sources: `CLAUDE.md:200-204`; CHANGELOG 3.0.0 (#226).
8. **Blessing stale artifacts.** "Verifying `dist/` without rebuilding blesses stale artifacts; the CLI's dependency edges exist so that cannot happen." This is enforced by `INV-graph-no-stale` (critical). Source: `CLAUDE.md:205-206`.
9. **The renderer fallback.** The verifier renders with `pdftoppm` when the authoring sandbox's renderer is absent. "Keep that fallback working." Sources: `CLAUDE.md:207-208`; `verify_pdf.py:21,336-355`.
10. **The hang that isn't.** The first LuaLaTeX run spends several minutes on a font scan. Sources: `CLAUDE.md:209-210`; also stated in QUICKSTART and INSTALL.
11. **A red check that shipped green.** "Never pipe a check command into grep before `&&` in a commit chain; the pipeline exit code is grep's, and a red check once shipped as green." Source: `CLAUDE.md:211-212`.
12. **The KOMA spelling trap.** In print, `open=any` must be spelled the KOMA way. "the standard-class spelling openany is silently ignored under twoside". `open=right` "would ship genuinely blank versos". Source: `src/press/data/defaults/print.yaml:3-7`.
13. **epubcheck versus pandoc's empty date.** pandoc emits an empty `dc:date`, which epubcheck rejects (RSC-005). The press therefore writes a year extracted from the prose date into `build/epub-metadata.xml`. Source: `src/press/build.py:594-623`.
14. **`CI=false` is truthy.** Toolchain strictness is keyed on `PRESS_TOOLCHAIN`, set in the image, "not the ambient CI variable". Source: `src/press/verify_formats.py:408-411`.
15. **The barcode that crowded its quiet zone.** A TikZ node's default padding shifted the EAN-13, so `verify-print` refused a correct wrap. The fix is `inner sep=0` on the node. Sources: CHANGELOG 2.3.1 (#210); `src/press/gen_coverwrap.py:393-400`.
16. **The five-percent box.** gpt-image lays its "white" ground near `#f1f2f3`. A naive inversion leaves "a five-percent box that is glaring on cream paper", so the luminance key starts at 225. Source: `src/press/art.py:67-73`.
17. **Literal, silly plates.** Commissions used to draw from captions, which produced "literal, silly plates". Now a figure with no `art:` description is refused: "A caption is a label, not art direction (#225)". Sources: `docs/ILLUSTRATIONS.md`; `src/press/illustrate.py:118-141`.
18. **The cover that invented its own subject.** Before v2.3.1, a book that named its subject only in `description` got "the book's subject" literally, and the model invented generic motifs. A fallback chain now applies. Sources: CHANGELOG 2.3.1; `src/press/cover.py:71-84`.
19. **Release automation that rewrote mypy.** An unanchored version regex in the release script "once rewrote [tool.mypy]'s python_version". It is now anchored, with `count=1`. Source: `scripts/release.sh:91-93`.
20. **11.5% coverage, broken covers.** "a title-page generator shipped a dropped and a clipped cover at 11.5% coverage: the lines ran, the artifact was never inspected." Hence "A producer is only proven by a verifier that rejects a broken artifact." This is also why the PDF verifier checks the cover on page 1. Source: `CONTRIBUTING.md:85-90`.
21. **The vacuous test.** A title-tie test passed with no filter, because pandoc ties `Mr.` itself. It was found by the 3.0.2 Lua coverage backfill, and the Lua tests had been silently skipping in CI until `PRESS_REQUIRE_LUA=1`. Source: `CHANGELOG.md:30-40`.
22. **A stray asterisk and "Fig-ure".** The float package's `\caption*` printed a stray asterisk above placed figures. A narrow wrap could hyphenate "Figure". The fixes were the caption package as the single caption authority and an `\mbox` around the label. Source: `CHANGELOG.md:140-150`.
23. **The 602-PPI logo.** Lulu flagged a 1024px logo printed at 1.7in as over 600 PPI, and flagged the logo's transparency. The print-safe pass now flattens every image and caps its resolution. Sources: `docs/LULU.md`; `src/press/print_safe.py`.
24. **An honest refusal beats a guessed thickness.** A colour interior is refused at Lulu and IngramSpark because no colour caliper is sourced: "the press will not guess a thickness". Sources: `docs/PRINT-FORMATS.md`; `src/press/provider_specs.py:87-101`.
25. **A migration that promised too much.** `press migrate` told v2→v3 users their geometry would be byte-for-byte unchanged. That was true only for v1→v2. Fixed in 3.0.1 (#262). Sources: `CHANGELOG.md:42-56`; `src/press/migrate.py:161-185`.
26. **The macOS runner retired mid-release.** GitHub retired `macos-14` ("configuration not supported", cancelled within a second), so the job moved to `macos-15`. Sources: CHANGELOG 3.0.0; `docs/COMPATIBILITY.md`.
27. **Forty-one Pillow advisories.** Five were critical. The hash lock made this a one-package bump: `scripts/lock-deps.sh --upgrade-package pillow`. Source: CHANGELOG 3.0.2.
28. **The subprocess gate's blind spot.** The adapters boundary gate missed `from subprocess import Popen`, and the desk launcher did exactly that. The gate now resolves aliases, and the launcher moved into `press.adapters`. Source: CHANGELOG 2.3.1.
29. **Sentinels on a drop cap.** The drop cap splits and small-caps a chapter's first word, so a sentinel placed there fails exact PDF matching. Choose mid-chapter phrases. Sources: the maintainer's notes; `src/press/data/lua/chapter-dropcap.lua`.
30. **The ghost of a gradient.** The luminance key reads every dark pixel as ink, so a gradient ground "survives as a smudge". Since 3.0.0, intake judges the border and refuses, naming the fix. Sources: CHANGELOG 3.0.0; `src/press/art.py:94-133`.

Design rationales that work as sidebars:

- **Why pip-from-git is not used in CI.** A private book needs no cross-repo token, and the installed press is pinned to the exact action ref (`CLAUDE.md:20-25`).
- **Why the index uses chapter labels rather than page numbers.** "both stay put across editions, which page numbers do not" (`src/press/gen_index.py:71-73`).
- **Why there is no plugin loader.** "Behavior cannot come from the accident of which package imported first" (`docs/ARCHITECTURE.md`).
- **Why the jargon checker exists twice.** The skill must work without the press installed, and a byte-parity contract keeps the two copies identical (`docs/WORKFLOWS.md`).
- **Why the hard-coded "diseases".** "'apply the skills' alone produces locally-obedient, globally-patterned prose" (`CLAUDE.md`).
- **Why the toolchain image is pinned by digest.** The `sha-` tag is mutable; a digest pins bytes (`CLAUDE.md` "The contract").
- **Why `main` takes direct pushes.** Trust is enforced at the release boundary, the tag (`SECURITY.md`, #153).

---


## 20. Open questions and contradictions (writers: avoid or hedge these)

### A. Docs contradict code. Follow the code.

1. **"In v1 the page trim is 6 x 9"** (`docs/QUICKSTART.md`, "What you are building"). This is stale. v2 and later have six profiles. The README still says "verified 6 x 9 PDF". That is the default, not the only option.
2. **The toolchain pin.** ARCHITECTURE.md ("Design versioning") and COMPATIBILITY.md say three-part tags pin "an existing immutable `sha-` tag". CLAUDE.md and `release-contract.yml` say a `sha-` tag alone is mutable and refused; an `@sha256:` digest is required. Use the digest wording.
3. **The invariant ledger's location.** ARCHITECTURE.md says `quality/invariants.yaml`. The real file is `.celebrimbor/invariants.yaml`. EXTENSION-CONTRACT.md likewise says `quality/surfaces.yaml`; the real file is `.celebrimbor/surfaces.yaml`.
4. **hypcap.** CLAUDE.md says the `hypcap` package is "loaded in the hyperref after-hook". Code: the package was removed, and `caption`'s `hypcap=true` does the job (`book-header.tex:134-139`).
5. **The 6.3in cap.** CLAUDE.md states it as universal. It is the house profile's value; other profiles use 4.8–7.2in. The cover-design and plates skills say 7.1in. Use "per profile; 6.3in on the house 6×9".
6. **"Page-accurate subject index" / "will not print a wrong page number"** (`docs/BOOK-PARTS.md`). The index lists chapter numbers and appendix letters, not pages.
7. **Index placement.** BOOK-PARTS shows the index last in the back matter. It takes the *first* free letter from `a`, while `press add appendix` assigns `z-`, `y-`… So the index usually sorts *before* authored appendices.
8. **Appendix lettering.** The scaffolded book `CLAUDE.md` says appendices order "by letter prefix (`a-`, `b-`, ...)". `press add appendix` counts down from `z-`. Both orderings are valid filenames; describe `press add`'s behavior.
9. **`verify-min-pages` default.** CONFIGURATION.md says "default 40", which is the model default. The scaffold template writes `1`.
10. **`tests/known-bad` "on every build"** (CLAUDE.md). The fixtures run in `press check` and `press all`, not in a bare `press pdf`.
11. **ILLUSTRATIONS.md widths.**
    - It says full-bleed and frontispiece "ignore width". The validator *refuses* a measure on a non-in-flow place.
    - It says a `plate` sits at its width, yet also that a measure on a plate is refused.
    - `place=margin` is an outer wrap inside the column, not a true margin figure.
    - "full-bleed" does not bleed: it is a cleared leaf inside the margins.
12. **"Seller of record: Lulu"** (PRINT-ORDERING, QUICKSTART). The provider ledger records Lulu `seller_of_record: unsupported` ("the publisher is the seller in the custom route"). Only Peecho is marked supported. Do not assert that Lulu is legally the seller of record. Say press's *model* is provider-as-seller and the publisher must confirm.
13. **LULU.md spine claims.** "Set the paper first so the spine math is right." With `print.provider: lulu`, the paperback spine is `pages/444 + 0.06`, independent of paper. The default provider is `house` (KDP-like calipers, 0 allowance), not Lulu. A Lulu-bound book should set `print.provider lulu`; the doc never says so for paperbacks.
14. **COMPATIBILITY.md** says "Each release records the toolchain image digest ... in its notes". Notes come from the CHANGELOG; the digest lives in the release receipt artifact.
15. **COVER-STYLES.md.**
    - `text: composited` "have the press set type": nothing implements compositing.
    - "Every style prints in your book's `accent`": the code reads `web-palette.accent`, which the house palette does not define, so the hard-coded `#7a2325` is used.
    - The doc says each card is a different book and later "the same book in each".
16. **Cover sizes.** `press cover` asks gpt-image-2 for 1024×1536. `press art commission` asks for 2304×3456. Intake checks only the aspect ratio (±3%), never resolution or DPI.
17. **Cover aspect check vs profile.** `art accept --as cover` reads `metadata.trim` (default 6×9), not the profile. A 5×8 book's cover is checked against 1.5, not 1.6.
18. **Plate greying.** "Intake greys it to the single interior ink." This happens only when `plates.medium` contains both the words "single" and "ink" (the house text does) and the profile is not colour.
19. **DESK.md.**
    - The evidence states `*` and `!` cannot appear in the live desk, because no evidence is passed and present artifacts show `o`.
    - The keymap omits `c` (cancel).
    - CLAUDE.md says every config field is settable from the wizard; only title, subtitle, author and description are.
20. **WORKFLOWS.md and CLAUDE.md skill lists** omit `book-aesthetics` and `profile-lifecycle`. `press skills` lists 11.
21. **Extension contract major 3 and `config/extensions.yaml`** are documented but not implemented. `SUPPORTED_CONTRACT_MAJORS = (2,)` even in v3.
22. **`press add` summary.** The catalog says "Add a chapter, appendix, or front-matter part". There is no front-matter part type: `--front` means a `00-` chapter or an `a-` appendix.
23. **Help grammar omissions.** `art enhance`, `cover --print`, `illustrate --subject/--print`, `improve --rounds`, `research --max-claims-per-file`, `aesthetic --overwrite`, `new --author/--publisher/--place/--owner`, `config --json/--dry-run/--file`, and `selftest --write-docs` all exist in code but not in `--help`.
24. **`verify-pages`** appears in README's "Checking" list and REFERENCE.md but not in `press --help`. It is an alias of `pages`.
25. **The metadata template comment** says "Enable it once the edition is qualified (press qualify)". There is no `press qualify` command. The qualification is recorded by hand in `config/qualification.yaml`.
26. **README's quick start** says `press new my-book; cd my-book && git init && make all`. That is accurate: `press new` does not `git init`, and the source zip needs git-tracked files, so `git init` plus an add/commit matters before `press source` and `press all`. This is inferred from the policy's "tracked files only" and should be verified before writers claim it.
27. **`docs/GALLERY.md`** says nine example cards lead with covers, but also says "the cards above are typographic rather than photographic". `build_examples.py` comments say "eight" examples; there are nine.

### B. Code behaviors that look like bugs. Do not document them as features.

1. **Print interior side margins.** `print-header.tex` re-sets `inner=0.88in,outer=0.58in` after the profile geometry. Every print interior may therefore get the house 6×9 side margins, regardless of profile. This comes from reading include order and was not verified by a build.
2. **Possibly missing print images.** `print-safe-images.lua` redirects *all* `assets/…` images to `build/print-assets/`. `print_safe` copies only the logo, top-level `assets/*.jpg` and `assets/woodcuts/*`. A figure at `assets/fig/x.jpg` (the docs' own example path) could be missing from the print interior. Unverified.
3. **Hard-coded 6×9 text.** The landing page's PDF row, the `publish` checklist trim, and the coverwrap back-text width all read the legacy `metadata.trim`, defaulting to 6×9, not the profile. Non-6×9 books show "6 by 9", and their back-cover text box may overrun into the spine.
4. **Unused provider minimums.** Spine-text minimums (KDP 79, Lulu 81, Ingram 48 pages) and provider `safety` values are declared but unused. Spine text is drawn whenever the spine is at least 0.25in. No even-page or saddle-stitch divisible-by-4 rule is enforced.
5. **`print.page-thickness`** is ignored for Lulu hardcovers. The IngramSpark dust-jacket spine uses the paperback PPI formula.
6. **Page-count bounds** are checked only inside cover-wrap generation, so a coverless book's page count is never bounded.
7. **`raised-cap`** renders identically to `drop-cap`.
8. **`lang="en"` is fixed** on the landing page, policy pages and JSON-LD `inLanguage`, ignoring metadata `lang`. The reader uses `$lang$`.
9. **The Markdown edition** is raw stitched source. `::: verse` divs, figure attributes and `<!-- art: -->` comments ship as written.
10. **The txt and docx editions** have no drop cap and no scene-break ornament.
11. **`press verify-formats`** includes an existing, possibly stale, `dist/<slug>.pdf` in the cross-edition agreement check without rebuilding it.
12. **`press verify-print`** builds the print interior twice when a cover exists.
13. **`press all`** builds neither `print` nor `coverwrap`, but the commerce release gate (ordering-enabled books only) does.
14. **The doctor and `pdfimages`.** Doctor does not check `pdfimages`, and its absence silently softens two checks to notes. A broken *optional* tool fails doctor.
15. **Gemini spends by default.** `press art commission` sends to both OpenAI and Gemini with no confirmation. Without `GEMINI_API_KEY` it exits after already paying for the OpenAI images.
16. **Plate shape keywords.** A plate prompt lacking the exact words "landscape composition" or "portrait composition" is generated square.
17. **`events.py`** (the child-event protocol) and the Lulu Print API adapter are not wired to any runtime path.
18. **Inconsistent check selection.** `release.sh` picks the `consumer` check with `first`; the release contract uses `sort_by(.started_at) | last`.
19. **The Dockerfile** installs PyYAML (unused) and unpinned Pillow. The action reinstalls from the hash lock anyway.
20. **ISBN minting** starts at publication number 0. ONIX always emits `NotificationType 03`, even with `--forthcoming`.
21. **`migrate plan`** on a v3 book proposes v4, which does not exist.

### C. Not documented anywhere. Do not invent.

- **pipx.** Not documented or proven.
- **Tool versions.** Pandoc and TeX Live versions are not pinned by number; they are "whatever Ubuntu 24.04 shipped".
- **Build timings.** Only the first-run font scan is described.
- **Windows.** Not tested.
- **Book-level `\part` divisions.** Unsupported.
- **Cross-references to chapters or sections.** None exist; only figures.
- **A generated glossary or "also by".** Planned, not built.
- **The finisher (supplied-interior PDF).** Planned on the Book breadth milestone, not shipped.
- **The custom merchant-of-record commerce stack.** Icebox.
- **Non-Latin and right-to-left scripts.** Icebox, "a major per script family".