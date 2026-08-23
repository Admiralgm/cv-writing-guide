# CV Humanization Post-Processing Workflow

> Developed 2026-07-25 during the 13-CV mixture-of-agents batch.
> Applied to all 13 FINAL/ CVs, output to H2_HUM/.

## When to Use

After generating CV .docx files (via cv_generator_v2.py or any other method), run this humanization pass before delivery. The generator produces clean, structured output that reads as AI-generated — this pass makes it read as human-written.

## Workflow

### Step 1: Convert page size (if needed)

The reference CV uses US Letter (8.5" x 11"). If the target employer expects A4 (8.27" x 11.69"), set the env var:

```bash
A4=1 python3 cv_generator_v2.py <json_file>
```

Or post-process with python-docx:
```python
section = doc.sections[0]
section.page_width = Inches(8.27)
section.page_height = Inches(11.69)
```

### Step 2: Apply 7 humanizer methods to body text

Target body text only — NOT headings, NOT the contact line, NOT role title/date lines, NOT education entries.

**Method 1 — Burstiness:** Vary sentence lengths dramatically. Insert short 3-8 word sentences after every 3-4 regular ones. Break sentences over 35 words into two. Target burstiness CV > 0.45.

**Method 2 — Discourse Markers:** Remove all formal transition words (furthermore, moreover, additionally, notably, consequently, therefore, thus, as a result, in conclusion).

**Method 3 — Specificity:** Replace generic claims with specific numbers from the CV repository. Every claim should have a number, a name, or a date.

**Method 4 — Hedging:** Add genuine uncertainty where appropriate. "This suggests" not "This proves". "It appears that" not "It is clear that".

**Method 5 — Narrative:** Add professional observations where natural. "In practice, this meant rethinking how teams worked, not just what tools they used."

**Method 6 — Structural:** Vary paragraph lengths. One section can be 2 sentences, another 8. Break symmetry.

**Method 7 — AI Pattern Removal:** Remove all 29 AI patterns from the humanizer skill (AI vocabulary, filler phrases, signposting, chatbot artifacts, rule-of-three, em dashes).

### Step 3: Specific fixes

- **Em dashes (—):** ZERO allowed in body text. Replace with commas, periods, or parentheses. (En dashes in date ranges like "Mar 2026 – Present" are fine — they're in role headings, not body text.)
- **"Key" as adjective:** Max 1 per entire CV. Remove all others.
- **"Comprehensive":** Remove entirely.
- **"Furthermore/moreover/additionally/notably":** Remove entirely.
- **Rule-of-three patterns:** Break "X, Y, and Z" lists to "X and Y" or restructure.

### Step 4: Verify with humanizer_analyze.py

```bash
python3 skills/creative/humanizer/scripts/humanizer_analyze.py --file <extracted_text.txt>
```

Target metrics:
| Metric | Target |
|--------|--------|
| Burstiness CV | > 0.45 (HUMAN-LIKE) |
| Perplexity Proxy | > 60 (HUMAN-LIKE) |
| Discourse Markers | < 2/1000 words |
| AI Vocabulary | < 3/1000 words |
| Em Dashes | 0/1000 words |
| Overall | LIKELY HUMAN-WRITTEN |

### Step 5: Re-extract text and re-analyze after fixes

After the fix pass, re-extract .txt from .docx and re-run analysis to confirm improvements.

## Pitfalls

- **Do NOT modify headings, contact line, name, role titles, or date lines.** These are structural elements, not body text.
- **Do NOT add first-person pronouns (I/me/my) to CV body text.** CVs use action-led phrasing. (Cover letters can use first person.)
- **Do NOT add "I think" or "in my opinion"** — these are CVs, not opinion pieces.
- **Keep all facts/numbers/company names EXACTLY the same.** Humanization changes wording, not data.
- **Maintain the same paragraph structure.** Don't merge or split paragraphs — just edit the text within them.
- **The humanizer_analyze.py may flag en dashes in date ranges** (e.g., "Mar 2026 – Present") as em dashes. These are in role headings which are excluded from modification. The count is a false positive — verify by inspecting the actual text.

## Reference

- Humanizer skill: `creative/humanizer/SKILL.md` — full 29-pattern list and 7 methods
- Analysis script: `skills/creative/humanizer/scripts/humanizer_analyze.py`
- This session's implementation: `H2_HUM/humanize_all.py` and `H2_HUM/fix_key_emdash.py`
