# Cross-Profile Batch CV Generation — QUALITY FAILURE (2026-07-25)

## What Happened

User requested 13 tailored machine-readable .docx CVs generated in parallel across AGENT/2/3. The orchestrator (AGENT) built a shared `cv_generator.py` and `TAILORING_INSTRUCTIONS.md`, dispatched 4 JDs each to AGENT (deepseek-v4-flash) and AGENT (glm-5.2), and generated 5 CVs locally.

All 13 .docx files were produced — structurally correct (A4, Arial, correct fonts/sizes, correct page dimensions, 35-41 paragraphs each, 40-41KB). Every file opened with python-docx verification.

**User deleted all 13 files: "delete all CVs ... since they SUCK !!!"**

## Root Causes

1. **Formulaic, un-tailored profiles**: The lesser models (deepseek-v4-flash, glm-5.2) produced generic professional profiles that read as AI slop. The profiles technically matched the JD keywords but lacked the sharp, opinionated, human voice that User's CVs require (see cv-writing skill §8 HUMANIZE ALL OUTPUT).

2. **JSON intermediate format loses nuance**: The pipeline was: read JD → read CV Repository → create JSON content file → run cv_generator.py → .docx. The JSON schema (headline, profile, competencies array, experience array with bullets) forced content into rigid structures. Compound bullets became separate list items. Achievement bullets lost their punch. The format was correct but the prose was dead.

3. **No humanization step**: The `humanizer` skill is MANDATORY per cv-writing skill §8. It was not applied to any of the 13 CVs. The output was raw LLM-generated prose in .docx format — structurally perfect, qualitatively garbage.

4. **Surface-level tailoring only**: Each CV had a different headline and slightly different profile paragraph, but the same experience entries, the same competency categories, and the same bullet text appeared across multiple CVs with only minor word swaps. A human reader (User) immediately spotted the pattern.

5. **Wrong workspace UUID**: The orchestrator dispatched to UUID `C85DF3C8` (from MEMORY.md and the cross-profile-coordination skill's "Known Target Map") instead of the real AGENT at `7F557C38`. A different glm-5.2 instance received the prompt. The real AGENT sat idle. When re-dispatched to the correct UUID, AGENT found the files already present (created by the wrong instance) and reported done without regenerating.

## Lessons

1. **CV generation is a QUALITY task, not a THROUGHPUT task.** Do NOT parallelize across lesser models. Each CV needs the strongest model's language capabilities, humanization, and individual review.

2. **The humanizer step is not optional.** Per cv-writing §8, ALL user-facing prose must be humanized. The cross-profile pipeline skipped this entirely.

3. **JSON intermediate format is a lossy transformation.** Going from CV Repository → JSON → .docx loses the compound bullet structure, the voice, and the tailoring nuance. Better approach: generate CVs as markdown/text first, review, then convert to .docx.

4. **Always run `cmux tree --all --id-format uuids` before dispatching.** NEVER trust UUIDs from memory, from skills, or from previous sessions. The cross-profile-coordination skill's "Known Target Map" had the WRONG UUID for AGENT.

5. **Verify the target agent is the RIGHT agent.** When the user says "AGENT is at workspace_id=7F557C38", use that UUID. Do not argue. Do not check your memory. Use what the user tells you.

## What to Do Instead

For batch CV generation:
1. Generate each CV one at a time on AGENT (strongest model)
2. Read the JD, read the CV Repository, write the tailored CV as markdown
3. Apply the humanizer skill to the prose
4. Convert to .docx using cv_generator.py (or write directly as .docx)
5. Review each CV individually before delivering
6. Only use cross-profile dispatch for research/data gathering, not for prose generation

## Artifacts

- `cv_generator.py` — still valid as a .docx formatting tool, just don't feed it unhumanized JSON
- `TAILORING_INSTRUCTIONS.md` — still valid as a guide, but needs a humanization step added
- 13 JSON content files — deleted along with the .docx files, but the generator script remains at `~/Desktop/LND/CVS/cv_generator.py`
