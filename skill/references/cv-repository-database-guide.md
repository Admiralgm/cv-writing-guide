# CV Repository Database v26 — Guide for CV Generation

## Location
`~/CV_REPOSITORY_DATABASE.md` (999 lines, ~110KB)

## Structure (v26, July 2026)

### Part I — Career Facts & Evidence (§1–§12) — Read this first

- **§1 Header & Contact**: Name, address, phone, email, LinkedIn, nationality (dual: Serbia + Czech Republic EU), DOB, languages. PII warning: portal/form fields only — never copy verbatim into free-format CVs.
- **§2 Professional Summaries**: 5 options (A: Ops/Leadership, B: FinTech, C: AI/Transformation, D: UN/INGO, E: Undersea Fibre). Write custom profiles per vacancy — never paste these unchanged.
- **§3 Professional Experience**: 12 entries (§3.1–§3.12) from Olivia Education (Mar 2026–Present) through Tetra Pak (1998–2008). Each with detailed bullets, tags, dates, team sizes, revenue figures.
- **§4 Entrepreneurial & Distinctive Projects**: ALFA NET, Project Wakanda, Undersea Fibre, Football Referee, AI Stack.
- **§5 Education, Certifications & Publications**: MPhil + MSc Electrical Engineering (University of Belgrade ETF), UN/UNICEF certs, ITU connectivity cert, LinkedIn AI articles.
- **§6 ATS Keyword Banks**: 3 banks (COO/FinTech, AI/Digital Transformation, Connectivity/Infrastructure).
- **§7 Skills Inventory**: Executive Leadership, Digital Connectivity, AI & Automation, FinTech, Telecom, International Development.
- **§8 Cover Letter Building Blocks**: AI Stack paragraph, Undersea Fibre paragraph, Connectivity paragraph.
- **§9 Location & Logistics**: Belgrade-based, Czech EU citizen, 10 years Africa experience.
- **§10 Application History**: (Populate during job search)
- **§11 Competency-to-Evidence Quick-Reference Matrix**: 15 requirement clusters mapped to specific roles/sections and proof points. Use this for fast tailoring without re-scanning §3–§4.
- **§12 Objection-Handling / Narrative Bridges**: Pre-written answers for consultancy pattern, sector-hopping, AI-stack positioning, title ceiling, age/DOB omission.

### Part II — Generation Instructions (§0 + deltas) — Applied after reading facts

- **§0 Universal Core Rules**: Applies to every CV.
  - §0.1 Step Zero: Select Application Track (UN vs Commercial)
  - §0.2 Precedence Order: Vacancy instructions > Mandatory forms > §0.4 Formatting Lock > Delta section > Core > Facts
  - §0.3 Factual Integrity: Never invent facts. Use precise verbs (led, owned, managed vs advised, supported).
  - §0.4 Reference-CV Formatting Lock: A4 portrait, exact margins (0.45"/0.6201"), Arial, 20pt blue name (#365F91) with 1pt #4F81BD bottom rule, 12pt bold-italic headline, 9pt two-line contact block, 12pt blue section headings (#1F497D), 10pt body, 9pt centered footer. SOLE VISUAL AUTHORITY.
  - §0.5 Content Construction Formula: Candidature thesis, ~150-word profile, competency selection, compressed STAR/CAR bullets, education, certifications, languages, references.
  - §0.6 Dates & Chronology: One consistent format, no double-counting.
  - §0.7 Privacy & PII: Data minimization default — no DOB, address, marital status, photo, salary.
  - §0.8 ATS Rules: Conventional headers, spell out acronyms, no tables, .docx master.
  - §0.9 Quality Gate: Check track, formatting, facts, bullets, privacy, ATS, file opens.
  - §0.10 Writing Best Practices: 8.8-second scan time, no first-person, no jargon, no "references available upon request", vary action verbs, proofread 3x.
  - §0.11 Vacancy-to-Evidence Workflow: Extract requirements → rate STRONG/PARTIAL/GAP → map to evidence → place in CV.
  - §0.12 Canonical Figures: Single source of truth for recurring numbers (team sizes: 14/86/127/180, VSAT: $10K→$900, IRU: 4×STM-1, M&A: $500M+, BUSPLUS: 500K tx/day, HRAM: €3.5M/€1.4M).

- **§0-DELTA-UN**: UN-sector mode (free-format CV, official form, or portal). 4-5 pages, British English, education before experience, references required, declaration statement.
- **§0-DELTA-COMMERCIAL**: Commercial/private-sector mode. 2-3 pages, positioning lanes (C-suite, Director, Programme, Technical, AI, Telecom, Sales, FinTech, NGO), AI-stack exclusion rule for non-AI lanes.

## Key v26 Changes from Previous Versions

- v25: Established §0.4 as mandatory formatting lock (was US Letter, now A4 per v26)
- v26: Changed page from US Letter to A4 portrait, contact block from 10pt to 9pt
- v17-v18: Fixed ZAMTEL team size discrepancy (120→180)
- v19: Added research-backed best practices (STAR, 8.8-second scan, Halo Effect)
- v20: Added §0.12 Canonical Figures, §12 Objection-Handling, PII warning banner
- v22: Profile target changed to ~150 words (140-160 range)

## How to Use for CV Generation

1. Read §1–§12 for career facts (source of truth)
2. Classify the vacancy (UN vs Commercial → select delta)
3. Use §11 matrix to map requirements to evidence quickly
4. Use §0.12 for exact recurring figures
5. Apply §0.4 formatting lock (use `scripts/cv_generator.py`)
6. Apply §0.5 content formula (150-word profile, competencies, compound bullets)
7. Run §0.9 quality gate before delivery
