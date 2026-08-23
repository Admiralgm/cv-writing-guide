# CV Batch Update Technique — Propagating New Repo Terms to Existing .docx CVs

## When to Use

When new terms are legitimately added to `CV_REPOSITORY_DATABASE.md` (user-directed) and existing CVs need to be updated to include them. This is NOT for fixing fabrications — it's for propagating genuine new competencies.

## The Core Problem: Run-Collapse Formatting Destruction

python-docx paragraphs contain **runs** — individually formatted text segments. A paragraph like a competencies line may have one run (all same formatting) or multiple runs (mixed bold/non-bold). 

**WRONG approach** (`replace_in_paragraph`):
```python
# This DESTROYS formatting by collapsing all runs into one
full_text = para.text
new_text = full_text.replace(old, new)
para.runs[0].text = new_text  # all text in first run
for r in para.runs[1:]:       # clear all other runs
    r.text = ''
```
This preserves the first run's font/size/bold but loses any mixed formatting within the paragraph.

**RIGHT approach** (`replace_in_runs`):
```python
def replace_in_runs(para, old_str, new_str):
    # Try replacing within a single run first — preserves all formatting
    for run in para.runs:
        if old_str in run.text:
            run.text = run.text.replace(old_str, new_str)
            return True
    # Fallback: old_str spans multiple runs — collapse as last resort
    if old_str not in para.text:
        return False
    if para.runs:
        full = ''.join(r.text for r in para.runs)
        new_full = full.replace(old_str, new_str)
        para.runs[0].text = new_full
        for r in para.runs[1:]:
            r.text = ''
        return True
    return False
```

## The Duplicate Paragraph Problem

Most CVs have **two near-identical competency paragraphs**:
- **Para 5** (bold, 12pt) — heading/ATS-optimized variant, uses `&` (e.g., "Governance & Security")
- **Para 6** (regular, 10pt) — body-text variant, uses `and` (e.g., "Governance and Security")

If you apply text replacement to BOTH, every new term appears twice in the CV — a duplicate.

**Fix:** Only target para 5 (the bold heading). Para 6 mirrors it with `and` instead of `&` and doesn't need separate updates.

## Zühlke-Specific Structure

Zühlke has a different CV structure from the other 10 AI-lane CVs:
- **Para 5/6**: Competencies (same dual-paragraph pattern)
- **Para 8**: "Built and operates a multi-profile Hermes AI stack..." (Selected Delivery Impact — SUMMARY, do NOT add new tools here)
- **Para 15**: "Built and operationalised custom AI agent frameworks..." (Experience — add Agent Harness here)
- **Para 16**: "Operates a high-throughput personal AI stack..." (Experience — add new terms here)

**Rule:** Only add new terms to the experience section (paras 15-16), NOT the delivery impact summary (para 8). The delivery impact is a high-level summary and doesn't need every tool listed.

## Standard Insertion Points (10 CVs)

For the 10 standard AI-lane CVs (all except Zühlke):

| Paragraph | What's there | What to add |
|-----------|-------------|-------------|
| Para 14 | "Built and operationalised... MCP) server architectures for automated content generation..." | Add `Agent Harness` after `MCP` |
| Para 15 | "Operates a high-throughput... Camoufox browser automation. Key Achievement:" | Add `Playwright, Chrome CDP, RAG, LLM-WIKI, OKF, agentic memory, sessions memory` before `Key Achievement:` |
| Para 5 | Competencies (bold) | For CVs with explicit AI tool clusters only: append new terms to one cluster |

## CVs with Explicit AI Tool Competencies

Only these 5 CVs list specific AI tools in their competencies section:
- **Comtrade** — "AI Operations" cluster
- **Zühlke** — "AI Operations" cluster
- **BCG Platinion** — "Cloud Computing & AI" cluster
- **EY** — "Hands-on AI Tooling" cluster
- **TecAlliance** — "Solution Architecture" cluster

The other 6 CVs (Accenture, Everseen, KPMG, Neurons Lab, Tenstorrent, Unit8) use conceptual competencies (e.g., "AI Strategy & Value Creation") and don't list specific tools — do NOT add tool names to their competencies.

## Backup-Then-Update Workflow

1. **Back up all CVs** to a `_BAK` directory before any modification
2. **Run the update script** with `replace_in_runs()` (not `replace_in_paragraph()`)
3. **Verify formatting preserved** — compare run count, font, size, bold between backup and current for every paragraph
4. **Check for duplicates** — each new term should appear 1-2x per CV, never 3x
5. **Run integrity check** — `python3 scripts/cv_content_integrity_check.py <dir>`
6. **Run humanizer checks** — 0 em dashes, 0 AI-slop, 0 corrupted labels, 0 first-person pronouns

## Verification Script

```python
# Check: formatting preserved + no duplicates + all terms present
from docx import Document
import re

new_terms = ['Playwright', 'Chrome CDP', 'RAG', 'LLM-WIKI', 'OKF', 
             'agentic memory', 'sessions memory', 'Agent Harness']

for fname in ai_lane_cvs:
    doc = Document(fname)
    full = ' '.join([p.text for p in doc.paragraphs])
    for term in new_terms:
        count = len(re.findall(r'\b' + re.escape(term) + r'\b', full, re.IGNORECASE))
        if count == 0: print(f'MISSING: {term}')
        elif count > 2: print(f'DUPLICATE: {term} ({count}x)')
```
