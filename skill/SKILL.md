---
name: cv-writing-guide
description: "Use when writing or reviewing any CV, resume, or cover letter. Research-backed best practices for ATS optimization, executive CVs, structure, bullet writing, and keyword strategy — applicable to any candidate, not just User."
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [career, cv, resume, cover-letter, ats, job-application, writing-guide]
    related_skills: [cv-writing, cv-formatting, cv-generation, humanizer]
---

# CV Writing Guide — Research-Backed Best Practices

## Overview

A general-purpose CV/resume writing skill built from 12 authoritative sources researched via SearXNG in July 2026: Resumly, Apollo Technical, StandOut CV, ResumeWorded, TopResume, Arielle Executive, Briefcase Coach, Sandia National Laboratories, Syracuse University College of Law, PPAAC, and the original Harvard Career Services reference. Covers ATS optimization, executive CV structure, bullet writing (including the STAR method), keyword strategy, cover letters, and 2025–2026 trends.

**Scope:** This skill covers the universal principles. For User-specific CV generation, use `cv-writing` (format/content rules) + `cv-formatting` (DOCX spec) + `cv-generation` (database workflow) instead.

## When to Use

- Writing a CV or resume for anyone (not just User)
- Reviewing or optimizing an existing CV for ATS compatibility
- Writing a cover letter
- Advising on CV structure, length, or content choices
- Preparing a CV for executive/senior-level roles

**Don't use for:** User's CVs — use `cv-writing` + `cv-formatting` + `cv-generation` instead.

> **Update (v1.1.0):** This skill is now integrated with the User CV ecosystem. For **commercial/private-sector** applications, load this skill alongside `cv-writing` and `cv-generation` — it provides the research foundation (STAR method, ATS optimization, action verbs, cover letter rules) while `cv-writing` provides User's specific format and tone. The CV repository database (§0.10 and §C.7) now references these practices directly. For **UN sector** applications, the UN-specific format spec takes precedence; this skill's general practices still apply where they don't conflict.

---

## 1. ATS OPTIMIZATION (The Gatekeeper)

~75% of resumes are rejected by ATS before a human ever sees them (Jobscan data, 2025; confirmed by Resumly and Apollo Technical, 2026). Employers spend an average of just 8.8 seconds scanning a resume before deciding a candidate's fate (Resumly, 2026). ATS now uses NLP and AI algorithms to understand context, not just keyword matching.

### Format Rules

| Rule | Why |
|------|-----|
| Single-column layout | ATS reads left-to-right, top-to-bottom; columns break reading order |
| Standard section headers | "Experience", "Education", "Skills" — not "Journey" or "What I Do" |
| No tables, text boxes, or images | ATS cannot parse content inside these elements |
| No headers/footers for critical content | Many ATS skip footer content entirely |
| One or two legible fonts | Calibri, Arial, Helvetica, Cambria, Georgia — 10–12pt body text (Apollo Technical, StandOut CV) |
| Save as PDF unless .docx requested | Most modern ATS parse PDF natively; .docx for government/EU portals |
| Reverse-chronological order | Most recent first; ATS and recruiters expect this |

### Keyword Strategy

1. Study 5–10 target job descriptions
2. List repeated skills, tools, and domain terms
3. Map those terms to your experience truthfully — never list skills you don't have
4. Place 15–25 high-value keywords across Professional Summary, Skills, and bullet points
5. Use exact phrases from the posting (e.g., "Kubernetes", "HIPAA compliance")
6. Mirror common synonyms ("OKR / goals", "ETL / data pipelines") to cover variation in JD language

### ATS Compatibility Checklist

- [ ] Single-column layout (no multi-column)
- [ ] Standard section headers
- [ ] No tables for content layout
- [ ] No text boxes or images with text
- [ ] No critical content in headers/footers
- [ ] Text-based PDF (not scanned/image) — verify with `pdftotext` or PyMuPDF
- [ ] PDF metadata populated (title, author fields)
- [ ] Linear reading order (no RTL columns)
- [ ] File unlocked, not password-protected
- [ ] Keywords from JD present in Summary + Skills + bullets

---

## 2. RESUME/CV STRUCTURE

### Standard Structure (entry to mid-level)

```
HEADER
  Name (largest font, 16-18pt)
  Contact: City, Country | Phone | Email | LinkedIn
  (Optional: Portfolio, GitHub, citizenship/eligibility)

PROFESSIONAL SUMMARY
  2-3 sentences: identity, years, core value proposition
  3-4 bullet highlights with bold category labels

CORE COMPETENCIES / SKILLS
  Inline bullet list or categorized list
  Group by domain (e.g., "AI Strategy: item1, item2, item3")

PROFESSIONAL EXPERIENCE
  Role Title | Organization | Location | Dates
  2-3 compound bullets (3 max)
  Last bullet: Key Achievement

EDUCATION
  Degree | Institution | Year

LANGUAGES (if relevant)
  Inline: English – Fluent | Serbian – Native
```

### Executive Structure (director, VP, C-suite)

Executive resumes follow different rules from standard templates (ResumeWorded, Page Executive):

- **2–3 pages acceptable** — depth of experience justifies length
- **Lead with a powerful executive summary** — 3-4 sentences positioning strategic value, not just skills
- **Core competencies as keyword grid** — ATS-friendly but also signals breadth to recruiters
- **Achievements before responsibilities** — recruiters scan for impact, not job descriptions
- **Truncate roles older than 10-15 years** — list title/company/dates only, no bullets
- **Board experience, P&L scope, team size** — include as quantified metrics in summary or role headers
- **Strategic keywords for 2026**: AI fluency, digital transformation, change management, data-driven decision-making (Page Executive)
- **Include scope metrics**: budget managed, team size, geographic scope, revenue impact

### Section Order Flexibility

- Private sector: Experience → Education (experience leads)
- UN/academic/medical: Education → Experience (credentials lead)
- Career changers: Skills/Competencies → Experience (transferable skills lead)

---

## 3. BULLET WRITING — THE CORE CRAFT

### The Formula

Every bullet should answer: **What did you do? How did you do it? What was the result?**

Pattern: `Action verb + task + method/tool + quantified result`

### The STAR Method (Resumly, 2026)

The best way to frame your achievements is by using the STAR method, a narrative technique that provides context and highlights results. Every bullet point in your experience section should be a mini-story of your success.

- **S — Situation**: Briefly describe the context or challenge you faced
- **T — Task**: Explain your specific responsibility or goal in that situation
- **A — Action**: Detail the specific actions you took to address the task
- **R — Result**: Quantify the outcome using numbers, percentages, or other concrete metrics

**Before:** "Planned the annual company conference."

**After (STAR):** "Orchestrated the 2024 annual sales conference for 500+ attendees, negotiating with 20+ vendors and managing a $150,000 budget to deliver the event 15% under budget while increasing attendee satisfaction scores by 25% year-over-year."

### Examples — Weak vs Strong

**WEAK (task description):**
- Responsible for managing the IT infrastructure across multiple offices
- Handled vendor relationships and contract negotiations
- Led the migration to cloud-based systems

**STRONG (impact-driven):**
- Reduced infrastructure costs 35% ($1.2M annual savings) by consolidating 11 data centers into 3 regional hubs with automated failover
- Negotiated $4.2M in vendor contracts, achieving 18% below market rate through competitive bidding across 14 suppliers
- Migrated 200+ services to AWS in 6 months with zero downtime, cutting deployment time from hours to minutes via CI/CD pipelines

### Bullet Rules

1. **Quantify everything possible** — numbers, percentages, dollar amounts, time saved, team size, user count
2. **Start with action verbs** — Spearheaded, Architected, Negotiated, Transformed, Streamlined, Deployed
3. **One bullet = one achievement** — don't pack unrelated accomplishments into one bullet (exception: compound bullets for executive density, see `cv-writing` skill)
4. **Maximum 2 lines per bullet** — dense but scannable
5. **No responsibility lists** — "Responsible for X" is a job description, not an achievement
6. **Prefer "by" construction** — "Achieved X by doing Y" shows causation

### Action Verb Bank

| Category | Verbs |
|----------|-------|
| Leadership | Spearheaded, Directed, Orchestrated, Championed, Steered, Governed |
| Building | Architected, Designed, Built, Engineered, Deployed, Implemented |
| Improving | Streamlined, Optimized, Accelerated, Modernized, Overhauled, Transformed |
| Financial | Negotiated, Reduced, Saved, Generated, Delivered, Drove |
| Analytical | Analyzed, Evaluated, Assessed, Diagnosed, Audited, Benchmarked |
| People | Mentored, Trained, Led, Managed, Recruited, Upskilled |

---

## 4. PROFESSIONAL SUMMARY

The summary is the first thing read — by both ATS and human. It must be dense, specific, and tailored.

### Structure (3-4 sentences)

1. **Identity + years** — who you are, how many years, your domain
2. **Core capability** — what you do better than most
3. **Proof point** — one concrete achievement that validates the claim
4. **Differentiator** — what makes you unique (bridge between strategy and execution, dual expertise, geographic scope)

### Weak vs Strong

**WEAK:** "Experienced professional with a proven track record of delivering results in fast-paced environments. Skilled in leadership, communication, and strategic planning."

**STRONG:** "Technology executive with 18+ years bridging AI strategy and IT operations across 11 countries. Reduced Cisco infrastructure costs 70% through a vendor renegotiation that became an official Cisco case study. Dual EU/Serbian citizen with fluency in English, Russian, and Serbian."

---

## 5. TAILORING TO JOB DESCRIPTIONS

### The Mirror Technique

1. **Read the JD 3 times** — first for content, second for keywords, third for tone
2. **Extract the vocabulary** — exact phrases they use (not synonyms you prefer)
3. **Mirror in your CV**:
   - If JD says "stakeholder alignment" → use "stakeholder alignment" (not "getting buy-in")
   - If JD names vendors (LSEG, Stripe, SAP) → name them in Competencies if you have them
   - If JD emphasizes "cross-functional" → use that exact word in your bullets
4. **Reorder experience** — keep reverse-chronological order (most recent first); all sources confirm this is what ATS and recruiters expect. Do NOT move a more relevant but older role above a more recent one — it confuses ATS parsers and raises red flags for recruiters
5. **Adjust summary** — rewrite the opening 2 sentences to position yourself for THIS role

### Keyword Density

- Too few keywords → ATS rejects
- Too many → looks stuffed, human rejects
- Sweet spot: 15-25 high-value terms naturally integrated into Summary + Skills + bullets
- Place keywords in context, not in isolation — "Kubernetes" in a bullet beats "Kubernetes" in a keyword list

---

## 6. COVER LETTERS

### Structure (1 page, 3-4 paragraphs)

**Paragraph 1 — Hook (2-3 sentences)**
- Name the role and company explicitly
- State why you're interested in THIS company (not "I am writing to apply")
- One sentence positioning yourself for the role

**Paragraphs 2-3 — Proof (3-4 sentences each)**
- Map 3-4 specific experiences to JD requirements
- Use the same "action + method + result" formula as CV bullets
- Reference specific projects, metrics, and outcomes
- Don't repeat the CV verbatim — add narrative context

**Paragraph 4 — Close (2-3 sentences)**
- Reiterate fit in one sentence
- State availability for interview
- Professional sign-off

### Cover Letter Rules

- 1 page maximum — never longer
- **Write in the body of your email, not as a separate attachment** (StandOut CV) — if you attach it separately, you slow down the recruiter and risk being ignored. The only exception is when a portal explicitly requires a separate document
- Address to a named person if possible (check LinkedIn for hiring manager)
- Match the CV's tone and vocabulary
- Don't apologize for gaps or weaknesses — focus on strengths
- Don't list every job — pick 3-4 strongest proof points
- **Avoid first-person pronouns** ("I", "me", "my") where possible — use action-led phrasing instead (Apollo Technical, Syracuse Law)

---

## 7. COMMON MISTAKES (From Harvard + Multi-Source)

| # | Mistake | Fix |
|---|---------|-----|
| 1 | Spelling and grammar errors | Proofread 3 times, use a tool, read aloud — 80% of recruiters may reject for typos alone (Resumly) |
| 2 | Missing email or phone | Always include both in header |
| 3 | Generic objective statement | Replace with tailored professional summary |
| 4 | Task descriptions instead of achievements | Rewrite every bullet with quantified impact using STAR method |
| 5 | Too long (entry-level) or too short (executive) | 1 page for <5 yrs, 2 for mid, 2-3 for executive |
| 6 | Creative section headers | Use standard: Experience, Education, Skills |
| 7 | Inconsistent formatting | One font, consistent spacing, uniform bullet style |
| 8 | No keywords from JD | Tailor with 15-25 JD keywords |
| 9 | Tables/columns for layout | Single-column only for ATS |
| 10 | Photo, DOB, marital status (non-UN) | Omit unless specifically requested |
| 11 | First-person pronouns ("I", "me", "my") | Use action-led phrasing — "Directed" not "I directed" (Apollo Technical, Syracuse Law) |
| 12 | Industry jargon without explanation | Keep language clear and accessible; define acronyms (PPAAC) |
| 13 | "References available upon request" | Omit entirely — recruiters know references are available; this wastes space (Syracuse Law) |
| 14 | Relying solely on AI to write resume | Hiring managers detect generic AI content; use AI as a tool, not a replacement for authentic voice (PPAAC) |

---

## 8. FILE FORMAT GUIDANCE

| Situation | Format | Why |
|-----------|--------|-----|
| Default (modern ATS: Greenhouse, Lever, Workday, Taleo) | PDF | Preserves layout, text-based PDFs parse natively |
| Government/EU institution portals | .docx | Some portals explicitly request Word |
| Portal paste option | Plain text | Bypasses ATS parsing entirely |
| Never | Locked/encrypted PDF, scanned image PDF, password-protected .docx | ATS cannot parse |

### PDF Verification

Before submitting, verify the PDF has extractable text:
```bash
# Method 1: pdftotext
pdftotext cv.pdf - | head -20
# If you see text → good. If empty → it's an image PDF.

# Method 2: PyMuPDF
python3 -c "import fitz; doc=fitz.open('cv.pdf'); print(doc[0].get_text()[:200])"
```

Also check PDF metadata is populated (title, author) — blank metadata is a weak signal to ATS.

---

## 9. 2025–2026 TRENDS (From Research)

| Trend | Source | Implication |
|-------|--------|-------------|
| ATS uses NLP/AI for context, not just keywords | Resumly, BuildFast AI | Keywords must be in context, not stuffed |
| AI fluency is a top executive skill | Page Executive, PPAAC | Include AI/automation/digital transformation in executive CVs |
| 75% rejection rate by ATS | Resumly, Apollo Technical (Jobscan) | ATS optimization is mandatory, not optional |
| 8.8-second average scan time | Resumly | Resume must make impact in under 9 seconds — top third is prime real estate |
| Executive CVs need major overhaul, not update | ResumeWorded, Arielle Executive, Briefcase Coach | Don't append to old CV — rebuild for target level; avoid "kitchen sink" resume |
| Remote/hybrid work expands applicant pools | All sources | Geographic flexibility is a differentiator — state it |
| .docx vs PDF gap narrowing | ResumePilot, Resumly | Both parse well on modern ATS; PDF preferred for layout fidelity |
| Federal resumes now 2-page max (US) | Resumly | US federal government agencies accepting resumes up to 2 pages only starting late 2025 |
| "Kitchen sink" resume is the #1 executive mistake | Briefcase Coach | Don't just pile new experience on old template — rebuild and tailor for target role |
| Halo Effect in resume design | Arielle Executive | Clean, minimalist resume = perceived as competent; cluttered = perceived as less competent |

---

## 10. VERIFICATION CHECKLIST

Before delivering any CV:

- [ ] ATS format: single-column, standard headers, no tables/text boxes/images
- [ ] Keywords: 15-25 from JD, placed in Summary + Skills + bullets
- [ ] Bullets: action verb + task + method + quantified result (STAR method)
- [ ] Summary: identity + years + capability + proof + differentiator
- [ ] Length: 1 page (<5 yrs), 2 (mid-level), 2-3 (executive)
- [ ] No "responsible for" or task-description bullets
- [ ] No creative section headers
- [ ] No photo/DOB/marital status (unless UN/region-specific requirement)
- [ ] No first-person pronouns ("I", "me", "my") — use action-led phrasing
- [ ] No industry jargon without explanation — keep language accessible
- [ ] No "references available upon request" — omit entirely
- [ ] File: text-based PDF or .docx (per portal requirement)
- [ ] PDF has extractable text (verified with pdftotext/PyMuPDF)
- [ ] PDF metadata populated (title, author)
- [ ] Spelling/grammar: proofread 3 times
- [ ] Tailored to specific JD (not a generic CV)
- [ ] Action verbs varied (not "Managed" for every bullet)
- [ ] Cover letter: written in email body (not separate attachment), unless portal requires otherwise
- [ ] Cover letter: addresses recipient by name

---

## Research Sources

This skill synthesizes research from July 2026 via SearXNG, verified by direct URL fetch:

1. **Resumly** — How to Make Your Resume Stand Out in 2026 (resumly.ai/blog/how-to-make-your-resume-stand-out-in-2025) — Updated June 19, 2026. Covers ATS optimization, STAR method, action verbs, 8.8-second scan time, global conventions
2. **Apollo Technical** — The 8 Resume Best Practices You Want To Know (apollotechnical.com/resume-best-practices) — Updated Feb 2, 2026. Format, fonts, quantification, mistakes to avoid
3. **StandOut CV** — How to write a CV (standout-cv.com/cv-advice/how-to-write-a-cv) — Updated May 7, 2026. Structure, formatting, profile writing, cover letters
4. **ResumeWorded** — How To Write an Executive Resume: The Definitive 2026 Guide (resumeworded.com/blog/executive-resume/) — Executive templates, summaries, truncation rules
5. **TopResume** — 10 Impactful Updates for Your Executive-Level Resume (topresume.com/career-advice/10-powerful-changes-for-your-senior-level-resume) — Executive-specific updates, credentials, quantification
6. **Arielle Executive** — How To Write An Executive Resume (That Actually Works In 2026) (arielleexecutive.com/executive-level-resume/) — Updated Feb 23, 2026. 7-section structure, Halo Effect, commercial positioning
7. **Briefcase Coach** — Writing an Executive Resume: An Expert Guide (briefcasecoach.com/writing-an-executive-resume/) — Value proposition, "kitchen sink" mistake, KPIs, RAS formula
8. **Sandia National Laboratories** — Resume Writing Best Practices (sandia.gov PDF, SAND2023-01563A, updated March 2024) — Manual review process, keyword alignment, section recommendations
9. **Syracuse University College of Law** — Resume Guide (law.syracuse.edu PDF) — Legal resume framework, what to exclude, formatting basics
10. **PPAAC** — Essential Resume Do's and Don'ts for 2025 Updates (ppaac.com/essential-resume-dos-and-donts-for-2025-updates/) — AI skills, jargon avoidance, ATS keywords
11. **Harvard College** — Guide to Creating a Strong Resume (careerservices.fas.harvard.edu) — Original reference; page restructured under Mignone Center for Career Success, core principles retained
12. **Jobscan** — ATS rejection rate data (jobscan.co) — 75% ATS rejection statistic, widely cited across sources

---

## Related

- `cv-writing` — User canonical CV format (content rules, structure, humanization)
- `cv-formatting` — User DOCX specification (fonts, sizes, margins, python-docx template)
- `cv-generation` — Generate CVs from master CV database (workflow for User's applications)
- `humanizer` — Mandatory humanization of all prose output
