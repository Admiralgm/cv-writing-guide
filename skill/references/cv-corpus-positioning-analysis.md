# Corpus-Level CV Positioning Analysis (workflow)

Use when the user asks "who am I / what is my value" across their CV library,
or when a new batch of tailored CVs warrants re-deriving the positioning
landscape. Validated 2026-08-10 on `OLD CV/` (500 files → 286 unique CVs).

## Why it works

User's tailored CVs are the best single signal of his marketable identity:
each one is a self-positioning for a specific employer. Aggregating all of
them reveals the constant core (what he always claims), the archetype range
(how he varies the lens), and the chameleon risk (when the spread reads as
unfocused).

## Steps

### 1. Extract all text (bulk)
```bash
mkdir -p /tmp/cv_extract
cd "~/Desktop/CV/OLD CV"
# docx → txt via macOS native textutil (fast, no deps)
for f in *.docx; do textutil -convert txt -output "/tmp/cv_extract/${f%.docx}.txt" "$f" 2>/dev/null; done
# pdf → txt only for files without a docx twin (avoid duplicates)
for f in *.pdf; do base="${f%.pdf}"; [ -f "/tmp/cv_extract/${base}.txt" ] || pdftotext -layout "$f" "/tmp/cv_extract/${base}.pdf.txt" 2>/dev/null; done
```
- 264 docx converted in seconds; ~40 pdf-only added. Both tools are on macOS by default.
- `.doc` (old binary): textutil also handles it; `.pages`: ZIP, skip.

### 2. Classify: headline + profile extraction
- Filename encodes the target employer/role — use it as a first signal.
- Headline = line 1-2 after the name (the positioning line).
- Profile = text after PROFESSIONAL PROFILE / SUMMARY / EXECUTIVE PROFILE
  header, or first paragraph ≥100 chars.
- Multi-tag each CV by regex on (filename + headline + profile): AI/Agentic,
  COO/Ops, Delivery/PMO, Telecom, UN, Consulting, Product, GM, etc.
- Skip JDs, ToRs, proposals, cover letters, forms (name-filter: `JD `, `ToR`,
  `TMC`, `proposal`, `cover letter`).
- Expect ~20 archetype tags on 286 CVs; multi-tagging is intentional — one CV
  legitimately claims 3-6 roles.

### 3. Theme-mine the profile texts
- Frequency-count across concatenated profiles: "25+/26+ years" (221/286),
  "hands-on" (63×), P&L, AI/automation, telecom, UN, Africa, EU citizenship.
- Extract money/scale metrics via regex (€ amounts, 100k/500k counts).
- These become the "constant core" and "recurring proof points" sections.

### 4. Synthesize
Structure the output as: one-line identity → constant core → archetype table →
recurring proof points → market value (scarcity argument) → honest warning.
The chameleon-risk section is essential — User values blunt truth over
flattery, and the corpus spread (CTO/COO/AI Dir/TPM/consultant/GM) is the
single most important strategic finding.

## Pitfalls

- **Terminal parser limits**: long `for` loops with multiple statements get
  blocked by the command parser. Split extraction into separate docx/pdf
  commands; keep each under ~1KB.
- **Duplicate pairs**: most CVs exist as .docx + .pdf twins — extract docx
  first, then only pdfs lacking a txt twin, or you double-count.
- **Old-format CVs** (2012-era, numbered 555-903): poor headings ("Profile &
  Objective"), short profiles — the classifier's "Other" bucket catches them;
  inspect a sample manually rather than trusting counts.
- **Name filter noise**: `CV_REPOSITORY_DATABASE.md*` backups, `~$` temp
  files, `.DS_Store` — exclude before counting.
- Output artifacts are session-scoped (/tmp/cv_extract, /tmp/cv_analysis.json);
  the durable product is the synthesis document (see
  `references/market-positioning-2026-08.md`).
