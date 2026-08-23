# Cross-Profile CV Generation Pattern (2026-07-25)

## Context

User requested tailored machine-readable .docx CVs for 13 qualified job vacancies, generated in parallel across AGENT (orchestrator), AGENT (deepseek-v4-flash), and AGENT (glm-5.2).

## Architecture

### Shared Infrastructure (created by AGENT):
1. `cv_generator.py` — Python script implementing §0.4 formatting lock (A4, Arial, 20pt blue name, 12pt blue headings, bullets, footer). Feed it JSON, it produces .docx.
2. `TAILORING_INSTRUCTIONS.md` — Step-by-step guide for each agent: read JD, read CV Repository, tailor content (150-word profile, 10-14 competencies, 3-5 experience roles), write JSON, run generator.

### Work Distribution:
- **AGENT** (5 CVs): Everseen, Comtrade, Neurons Lab, ARRISE, TecAlliance
- **AGENT** (4 CVs): Tenstorrent, Zühlke, Rohlik, KPMG Malta
- **AGENT** (4 CVs): BCG Platinion, Accenture Belgium, EY, Unit8

### Dispatch Protocol:
1. `cmux tree --all --id-format uuids` to discover workspace UUIDs
2. `cmux list-windows --id-format both` to cross-reference
3. Verify target agents at `─ ready │` with `cmux capture-pane`
4. 3-stage cmux send: text → newline → Enter key
5. Include in prompt: JD file paths, positioning lane per vacancy, critical rules, reply-back instructions with FULL UUID

### JSON Content Schema:
```json
{
    "headline": "TECHNICAL PROGRAM MANAGER — AI/ML",
    "profile": "150-word professional profile...",
    "competencies": ["Category: item1 • item2 • item3", ...],
    "experience": [
        {
            "title": "ROLE TITLE",
            "org": "Organization",
            "location": "City, Country",
            "dates": "Month YYYY – Present",
            "bullets": ["Compound bullet...", "Key Achievement: ..."]
        }
    ],
    "additional_experience": ["One-liner per role..."],
    "education": ["• Degree, Institution, Years"],
    "languages": "English – Fluent/Business | Serbian – Native | Russian – Fluent/Business",
    "company": "CompanyName",
    "role": "Role_Title_Underscores"
}
```

## Pitfalls Encountered

1. **Truncated UUID in reply-back**: AGENT sent reply-back instructions with `0FE55EE2` instead of full `0FE55EE2-18F1-4126-AF57-4F4CBFB20EBA`. AGENT got `Error: Invalid workspace handle` and was stuck trying to reply. User saw it as "sitting idle." Fix: ALWAYS use full UUID from `cmux tree --all --id-format uuids`.

2. **User perception of idle agents**: Both AGENT and AGENT were actively processing (reading CV Repository, tailoring content, writing JSON) but appeared idle because the TUI showed thinking states (`brainstorming…`, `reflecting…`, `musing…`) not progress bars. User sent multiple angry messages thinking agents were stuck. Lesson: when dispatching to other agents, set expectations with the user that thinking states are normal and take 1-3 minutes.

3. **AGENT faster than AGENT**: Deepseek V4 Flash completed 4 CVs in ~2 minutes. GLM-5.2 took ~3 minutes including the stuck reply-back attempt. For batch generation tasks, deepseek is the faster workhorse.

## Results

All 13 .docx files generated and verified:
- Every file opens with python-docx
- All have User MARKOVIĆ (with diacritic) as first paragraph
- All have A4 page dimensions (7559675 x 10692130 EMU)
- File sizes: 40-41 KB each
- Paragraph counts: 35-41 per CV
