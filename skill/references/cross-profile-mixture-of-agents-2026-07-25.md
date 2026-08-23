# Cross-Profile Mixture-of-Agents CV Generation (2026-07-25)

## Context

User requested 13 tailored machine-readable .docx CVs for 13 LinkedIn job vacancies. Previous attempt (same day, earlier session) split jobs across agents — 5/4/4 — and produced garbage ("delete all CVs since they SUCK"). User corrected the approach: "DO NOT SPLIT THE JOB. WORK AS MIXTURE OF AGENTS, ALL AGENTS DO THE SAME, YOU THEN Summarize."

## What Changed

### Previous approach (FAILED): Work splitting
- Each agent got 4-5 different vacancies to produce
- Lesser models (deepseek-v4-flash) produced formulaic AI-slop profiles
- No cross-model comparison or quality selection
- User deleted all 13 files

### New approach (SUCCEEDED): Mixture of agents
- ALL 3 agents (AGENT, AGENT, AGENT) produce ALL 13 CVs independently
- Orchestrator (AGENT) builds shared infrastructure, dispatches, generates own CVs, then merges
- Each agent writes to its own directory (H0/, H2/, H3/) to avoid collisions
- Orchestrator scores each CV and picks the best version per vacancy
- Winners copied to FINAL/ directory

## Architecture

### Shared Infrastructure (created by AGENT):
1. `cv_generator_v2.py` — Python script matching reference CV format exactly (US Letter, no bullet chars in body, ALL 12 roles, "SELECTED DELIVERY IMPACT" section, 3+ pages). Feed it JSON, it produces .docx.
2. `TAILORING_INSTRUCTIONS_V2.md` — Per-vacancy guidance: headline, profile focus, competencies, delivery impact emphasis, experience emphasis, AI-stack inclusion/exclusion rules.

### Dispatch Protocol:
1. Create output directories: H0/, H2/, H3/ — copy generator to each
2. `cmux tree --all --id-format uuids` to discover workspace UUIDs
3. Verify target agents at `─ ready │` with `cmux capture-pane`
4. 3-stage cmux send: text → space → Enter key (NOT empty string — it fails)
5. Prompt is self-contained: all 13 JD file paths, tailoring instructions path, CV Repository path, generator path, JSON schema, all 12 experience roles with dates/orgs, critical rules, reply-back instructions with FULL UUID
6. Send STOP to any active agents before re-dispatching (if correcting mid-task)

### Merging Protocol:
1. After all agents complete, verify each .docx opens with python-docx
2. Score each CV version on 4 axes:
   - Profile depth (40pts, target 150 words)
   - Competencies richness (20pts, target 80 words)
   - Delivery impact statements (15pts, target 3)
   - Experience depth (25pts, target 75 paragraphs)
3. Pick highest-scoring version per vacancy
4. Copy winners to FINAL/ directory
5. Verify: 0 first-person pronouns, 0 AI-slop, 0 body bullet chars, all 12 roles, US Letter format

## Results

### Merge Scores (13 vacancies):

| Vacancy | H0 Score | H2 Score | H3 Score | Winner |
|---------|----------|----------|----------|--------|
| Everseen | 88.3 | 77.5 | 88.6 | H3 |
| Comtrade | 88.0 | 76.7 | 89.1 | H3 |
| ARRISE | 84.6 | 71.2 | 92.1 | H3 |
| Tenstorrent | 86.8 | 74.2 | 90.2 | H3 |
| TecAlliance | 88.7 | 78.6 | 93.9 | H3 |
| Zühlke | **93.1** | 80.5 | 91.0 | **H0** |
| Rohlik | 87.8 | 72.3 | 93.2 | H3 |
| KPMG | 86.8 | 73.5 | 92.5 | H3 |
| BCG | 87.0 | 77.3 | 92.7 | H3 |
| Neurons | 86.7 | 75.2 | 92.9 | H3 |
| Accenture | 87.8 | 75.9 | 91.7 | H3 |
| EY | 86.6 | 74.6 | 94.2 | H3 |
| Unit8 | 90.4 | 74.8 | 94.5 | H3 |

**AGENT won 12/13.** User correctly predicted "he is smarter."
**AGENT won 1/13** (Zühlke — richest competencies + experience depth).

### Quality Verification (ALL 13 FINAL CVs):
- ✅ All 12 experience roles in every CV (not shortened)
- ✅ 0 first-person pronouns in body text
- ✅ 0 AI-slop phrases
- ✅ 0 bullet characters in body text (education uses • — matches reference)
- ✅ US Letter format (8.5×11")
- ✅ All 5 section headings (Profile, Competencies, Delivery Impact, Experience, Education)
- ✅ AI-stack correctly included in AI/Data lane CVs, excluded from ARRISE/Rohlik
- ✅ No French claimed (EY), no German claimed (Unit8)

## Key Lessons

1. **Mixture-of-agents beats work-splitting for quality tasks.** When the user says "ALL AGENTS DO THE SAME," they mean it. Each agent produces all CVs; the orchestrator picks the best per vacancy. This leverages model diversity — H3's profiles were richer (139-150 words), H0's competencies were richer (79-92 words).

2. **The user knows which model is better.** "YOU SHOULD ASK AGENT to do it, he is smarter" — H3 won 12/13. Trust the user's model assessment.

3. **Reference CV format matters.** The previous batch used `cv_generator.py` (A4, bullet chars, 3-5 roles). This batch used `cv_generator_v2.py` (US Letter, no bullets, all 12 roles, "SELECTED DELIVERY IMPACT" section). The format upgrade was driven by reading the actual reference DOCX file.

4. **STOP before re-dispatching.** When the user corrects mid-task ("DO NOT SPLIT THE JOB"), send STOP to all agents immediately, wait for `─ ready │`, then re-dispatch with the corrected approach.

5. **Scoring formula works.** The 4-axis scoring (profile 40, competencies 20, impact 15, experience 25) produced clear winners with meaningful differentiation. H3 consistently scored 90+ due to 140-150 word profiles.

## Artifacts

- Generator: `scripts/cv_generator_v2.py` (in cv-writing skill)
- Output: `~/Desktop/LND/CVS/FINAL/` — 13 .docx files
- Per-agent dirs: `~/Desktop/LND/CVS/H0/`, `H2/`, `H3/`
- Tailoring guide: `~/Desktop/LND/CVS/TAILORING_INSTRUCTIONS_V2.md`
- Merge winners: `~/Desktop/LND/CVS/merge_winners.json`
