# Batch Humanization + A4 Conversion — 2026-07-25

## Context

After the mixture-of-agents CV generation (13 CVs × 3 agents = 39 .docx files),
the user requested humanization of all 13 final CVs and conversion from US Letter
to A4 page size.

## Baseline Analysis (Before Humanization)

Ran `humanizer_analyze.py` on extracted .docx text:

```
Words: 1703  |  Sentences: 51  |  Avg sentence length: 33.4 words

Burstiness CV: 0.446 [WARN] MODERATE
Perplexity Proxy: 72.9/100 [OK] HUMAN-LIKE
Discourse Markers: 0.6/1000 [OK] HUMAN-LIKE
AI Vocabulary: 4.1/1000 [WARN] MODERATE (key×5, comprehensive×2)
Em Dashes: 9 (5.3/1000) [FAIL] overused
Rule of Three: 7 instances (13.7%)

OVERALL: LIKELY HUMAN-WRITTEN  Score: 1.5/2.0
```

## Humanization Script

Built `/tmp/humanize_cvs.py` — applies all 7 humanizer methods + 29 AI pattern
removal to body text only (skips headings, role titles, date lines, contact line,
name header). Also converts page size to A4 in the same pass.

### Key functions:

```python
def is_heading(para):
    """Section heading: bold, 12pt, colored."""
    if not para.runs: return False
    run = para.runs[0]
    return (run.font.bold and run.font.size and
            run.font.size.pt == 12 and run.font.color and run.font.color.rgb)

def is_role_title(para):
    """Role title: bold, 10pt, contains |."""
    if not para.runs: return False
    run = para.runs[0]
    return (run.font.bold and run.font.size and
            run.font.size.pt == 10 and '|' in para.text)

def is_date_line(para):
    """Date line: italic, gray (595959 or 505050)."""
    if not para.runs: return False
    run = para.runs[0]
    if run.font.italic and run.font.color and run.font.color.rgb:
        return '595959' in str(run.font.color.rgb) or '505050' in str(run.font.color.rgb)
    return False

def should_humanize(para):
    """Only humanize body text — skip all structural elements."""
    if is_heading(para) or is_role_title(para) or is_date_line(para): return False
    if is_name_header(para) or is_tagline(para) or is_contact_line(para): return False
    if not para.text.strip(): return False
    return True
```

### Humanization transformations applied:

1. **Em dash removal**: ` — ` → `, ` (all em dashes in body text)
2. **AI vocabulary removal**: furthermore, moreover, additionally, notably,
   consequently, comprehensive, key (as adjective), serves as, stands as,
   boasts, features, delve, tapestry, pivotal, showcase, underscore, etc.
3. **Filler phrase removal**: "in order to" → "to", "due to the fact that" → "because"
4. **Significance inflation removal**: "sets the stage for" → "enables",
   "contributing to" → "supporting"
5. **-ing ending fixes**: ", highlighting " → ", which highlights "
6. **Burstiness engineering**: break sentences over 35 words at comma boundaries
7. **"key" overuse**: "key role/driver/factor" → "central role/driver/factor" (max 3 per CV)

### A4 conversion:

```python
def convert_to_a4(doc):
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
```

## Post-Humanization Fix: Education Em Dashes

After the main humanization pass, 26 em dashes remained in education sections
across all 13 CVs (2 per CV: Magister and Master degree lines). These are
structured degree names: `Magister of Electrical Engineering — Telecommunications`

The humanizer correctly skipped headings but processed education paragraphs.
Fix: separate pass replacing ` — ` with `, ` in ALL paragraphs:

```python
for p in doc.paragraphs:
    if '—' in p.text:
        new_text = p.text.replace(' — ', ', ').replace('—', '-')
        if new_text != p.text and p.runs:
            p.runs[0].text = new_text
            for r in p.runs[1:]: r.text = ''
```

All 3 agents (H0, H2, H3) had the same issue — 26 em dashes each. Fixed
post-merge with the same pass.

## After Humanization (Final)

```
Words: 1703  |  Sentences: 46  |  Avg sentence length: 37.0 words

Burstiness CV: 0.464 [OK] HUMAN-LIKE
Perplexity Proxy: 72.9/100 [OK] HUMAN-LIKE
Discourse Markers: 0.6/1000 [OK] HUMAN-LIKE
AI Vocabulary: 0.0/1000 [OK] HUMAN-LIKE
Em Dashes: 0 [OK]
Rule of Three: 7 instances (15.2%)

OVERALL: LIKELY HUMAN-WRITTEN  Score: 2.0/2.0
```

## Mixture-of-Agents Humanization Merge

All 3 agents humanized all 13 CVs independently. Scoring formula:

```
quality_score = min(40, burstiness/0.5*40)
              + min(30, (1-ai_vocab/5)*30)
              + min(15, (5-em_dashes)*3)
              + min(15, overall_score/2.0*15)
```

Results:
- H0 won 12/13 (perfect AI vocab removal: 0/1000 across all CVs)
- H2 won 1/13 (ARRISE — higher burstiness 0.514 vs H0's 0.473)
- H3 won 0/13 (lower burstiness across the board)

H0's advantage: the regex-based humanization script was more aggressive at
removing AI vocabulary words, achieving 0/1000 density. H2 and H3 left
residual "key" and "landscape" occurrences (0.6-1.3/1000).

## Final Verification (All 13 CVs)

| Check | Result |
|-------|--------|
| A4 (8.27×11.69") | ✅ All 13 |
| All 12 experience roles | ✅ All 13 |
| 0 first-person pronouns | ✅ All 13 |
| 0 em dashes | ✅ All 13 |
| 0 AI vocabulary | ✅ All 13 |
| 0 AI-slop phrases | ✅ All 13 |
| 0 bullet chars in body | ✅ All 13 |
| Humanizer score 2.0/2.0 | ✅ All 13 |

## Output

Final humanized CVs: `~/Desktop/LND/CVS/FINAL_HUM/`
- 13 .docx files, ~42KB each
- A4 page size, Arial font, all formatting preserved
- Humanizer analysis: 2.0/2.0 (LIKELY HUMAN-WRITTEN) across all metrics

## Lessons for Future Sessions

1. **Always set A4 in the generator script** — don't rely on a post-conversion pass
2. **Education em dashes are the #1 humanization miss** — add a dedicated
   post-humanization pass for ALL paragraphs, not just body text
3. **Regex-based humanization beats LLM-based for AI vocab removal** — H0's
   deterministic script achieved 0/1000 while H2/H3's LLM approaches left residual
   vocabulary
4. **Run humanizer_analyze.py before AND after** — the before/after comparison
   is the verification artifact that proves the humanization worked
5. **A4 conversion is trivial** — 2 lines of python-docx code, but easy to forget
   if the generator script doesn't include it
