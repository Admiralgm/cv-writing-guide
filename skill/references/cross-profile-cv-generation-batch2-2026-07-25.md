# Cross-Profile CV Generation — Second Batch (2026-07-25)

## Context

AGENT forwarded a CV generation task to AGENT for 4 AI/Data/Digital Transformation lane vacancies: BCG Platinion (Amsterdam), Accenture Belgium (Brussels), EY (Luxembourg), Unit8 (Zurich). All 4 were commercial/private-sector consulting roles.

## What Worked

1. **Self-contained forwarded prompt**: AGENT's forwarded task included everything — file paths, positioning lanes, critical rules, reply-back instructions. No additional skill loading needed beyond what the prompt specified.

2. **Parallel JSON creation**: All 4 JSON content files written in a single `write_file` batch, then all 4 DOCX files generated in a single `terminal` call chaining 4 `python3 cv_generator.py` invocations. Efficient tool usage.

3. **Fresh tailoring per employer**: Each CV got a unique profile, unique competency ordering, and different experience role emphasis — no copying between CVs. BCG Platinion led with Tetra Pak (enterprise IT consulting), Accenture led with HRAM COO (AI value creation), EY led with Olivia (AI use case discovery), Unit8 led with Olivia (data-driven use cases).

4. **AI-stack inclusion for AI/Data lane**: All 4 CVs included Hermes, MCP, agentic AI, 120M tokens/day, CMUX orchestration material per §C.1 rule (AI-stack material belongs ONLY in AI/Data/Digital Transformation lane).

## Pitfalls Encountered

### 1. cmux send with empty string fails
```bash
# FAILS: "Error: send requires text"
cmux send --workspace UUID ""

# WORKS: use single space
cmux send --workspace UUID " "
```
The 3-stage cmux send pattern (text → newline → Enter key) requires a non-empty string for the middle stage. Use `" "` (single space) instead of `""`.

### 2. CMUX_SOCKET_PATH from cron context
If `CMUX_SOCKET_PATH` is set in the environment (e.g., from a cron job context), cmux commands fail with "Socket not found at ~/.cmux/sockets/cmux.sock". Fix: unset the env var or set it to empty string:
```bash
CMUX_SOCKET_PATH="" /Applications/cmux.app/Contents/Resources/bin/cmux send --workspace UUID "text"
```

### 3. Truncated workspace UUID
Reply-back instructions from AGENT used truncated UUID `0FE55EE2` instead of full `0FE55EE2-18F1-4126-AF57-4F4CBFB20EBA`. cmux requires the full UUID. Fix: always run `cmux tree --all --id-format uuids` and copy the complete UUID.

### 4. Language requirements in JD vs CV
- **EY (Luxembourg)**: requires fluent French. User does not speak French. CV languages line stays `English – Fluent/Business | Serbian – Native | Russian – Fluent/Business`. Do NOT claim French.
- **Unit8 (Zurich)**: requires fluent German. User does not speak German. Same rule — do NOT claim German.
- Both are SOFT_NO_REQUIRED_LANGUAGE_GAP situations in scoring, but for CV generation the rule is simpler: never claim a language not in the CV repository.

## Results

All 4 .docx files generated and verified:
- `User_CV_BCG_Platinion_AI_Tech_Consultant.docx` (40,843 B)
- `User_CV_Accenture_Belgium_Data_AI_Value_Strategy_Consultant.docx` (40,847 B)
- `User_CV_EY_AI_Data_Consulting_Senior.docx` (40,811 B)
- `User_CV_Unit8_Senior_Data_AI_Consultant.docx` (40,869 B)

All at `~/Desktop/LND/CVS/`.

## JSON Content Patterns for AI/Data Lane

### Experience Role Selection (all 4 CVs used the same 4 roles):
1. **Olivia Education** (March 2026 – Present) — AI advisor, LMS integration, agentic AI, always first for AI lane
2. **HRAM Medical Group COO** (Sep 2021 – Nov 2024) — AI-linked CRM, digital transformation, P&L
3. **Globaltel MVNO** (Jan 2016 – Sep 2019) — AWS platform, payment systems, API integration (for BCG/Accenture/Unit8) OR **Algotech** (for EY — workshop facilitation, change management)
4. **Tetra Pak** (Feb 1998 – Jun 2008) — SAP ERP, multi-country IT governance, VMware

### Additional Experience (2 one-liners):
- Algotech (if not in main experience) — Cisco Webex COVID case study
- ZAMTEL or another African telecom — team leadership, infrastructure

### Competency Categories (4 per CV, tailored per employer):
- AI Strategy & Architecture/Use Case Discovery (always first)
- AI Delivery & Implementation / Responsible AI Governance
- Consulting & Stakeholder Management / Business Development
- Executive Operations / Data Platform Strategy