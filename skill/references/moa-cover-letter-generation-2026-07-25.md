# MOA Cover Letter Generation — Worked Example (2026-07-25)

## Context

Mixture of Agents (MOA) task: all 3 Hermes agents (AGENT, AGENT, AGENT) independently generate the same 13 cover letters as .docx files. After all 3 complete, the orchestrator MERGES the best paragraphs from all 3 agents into 13 synthesized cover letters that are better than any individual version. **DO NOT simply pick one winner per vacancy** — the user explicitly corrected this approach on 2026-07-25: "I dont want you to select the WINNING file, I want you to merge the best parts and create an EXCELLENT COVER LETTERS." Read each paragraph from all 3 agents, identify the strongest version of each paragraph, and synthesize them into one merged cover letter per vacancy.

## Workflow

### Step 1: Read sources
```
read_file(TAILORING_INSTRUCTIONS.md)
read_file(cover_letter_generator.py)
read_file(CV_REPOSITORY_DATABASE.md)  # all 1011 lines
read_file(each LI_*.md)               # all 13 JDs
```

### Step 2: Write JSON files
Each cover letter is a JSON file with schema:
```json
{
  "company": "Company Name",
  "role": "Role Title",
  "salutation": "Dear Hiring Manager,",
  "paragraphs": [
    "Paragraph 1 (50-80 words): Lead with verified value proposition, not 'I am writing to apply'",
    "Paragraph 2 (80-100 words): Map 2-3 requirements to specific evidence, compressed STAR/CAR",
    "Paragraph 3 (80-100 words): Continue mapping. AI stack for AI-lane roles; ops/leadership for non-AI",
    "Paragraph 4 (40-60 words): State fit confidently, invite discussion. No 'I look forward to hearing from you'"
  ]
}
```

### Step 3: Generate .docx
```bash
python3 ~/Desktop/LND/CVS/FINAL_HUM/COVER_LETTERS/cover_letter_generator.py <json_path> <output_docx>
```

### Step 4: Run integrity check
```bash
python3 skills/productivity/cv-writing/scripts/cv_content_integrity_check.py /path/to/output/dir/
```
Exit 0 = all pass. Exit 1 = failures. Fix flagged JSON files and regenerate.

### Step 5: Notify orchestrator
```bash
cmux send --workspace <FULL_UUID> "COVER LETTERS DONE"
cmux send-key --workspace <FULL_UUID> Enter
```

## Critical Rules

### Content rules (from TAILORING_INSTRUCTIONS.md §C.5)
- **Paragraph 1**: Open with a strong value proposition. DO NOT write "I am writing to apply for..."
- **Paragraph 4**: DO NOT write "I look forward to hearing from you" or any AI cliché
- **250-350 words total** across 4 paragraphs
- No em dashes (—) — use commas or periods
- No AI-slop vocabulary: "furthermore," "notably," "it is important to note," "in order to," "due to the fact that"
- Vary sentence length dramatically (3-1-5 pattern)
- Write like a person who did the work, not a model summarizing it
- First person is OK in cover letters, but vary sentence openings

### AI-stack exclusion rule (§C.1)
- **ARRISE and Rohlik**: EXCLUDE AI stack content entirely. Focus on operations, leadership, digital transformation, telecom, P&L.
- **All other 11**: Include AI stack content (Hermes AI, CMUX, Ollama, DGX-B200, etc.)

### Anti-fabrication rules (§9)
- Every technical term MUST exist in CV_REPOSITORY_DATABASE.md
- Forbidden: Azure, Python, Kubernetes, Docker, OAuth, TensorFlow, PyTorch, neural network, machine learning, MLOps, DevOps, Scrum, microservices, fine-tuning, data science, prompt engineering, Scrapling (use Scrapple), Copilot, Power BI
- Approved: Hermes AI, OpenClaw, CMUX, Ollama, OpenRouter, MLX, MCP, SearXNG, Camoufox, Scrapple, Playwright, Chrome CDP, RAG, LLM-WIKI, OKF, agentic memory, sessions memory, Agent Harness, FreeAIOCR, NVIDIA DGX-B200, Moonshot Kimi K2.6 NVFP4, AWS, SAP ERP, VMware, Cisco Webex, Moodle, Canvas, SCORM, xAPI, VSAT, SDH, DSL, FTTX/GPON, 3G/4G/5G, Wi-Fi, LTE, API/web services bridges, OCR pipelines, LLM, AI agents, agentic workflows
- Do NOT mirror JD vocabulary for tools/platforms User has never used
- If a JD requires a skill User doesn't have, lean on adjacent genuine experience

### Name
- Always "User" (uppercase in header, normal case in body)

## Pitfalls

### 1. cmux send with empty string fails
```bash
# WRONG — "send requires text" error
cmux send --workspace UUID "" && cmux send-key --workspace UUID Enter

# RIGHT — send message, then send-key Enter
cmux send --workspace UUID "COVER LETTERS DONE"
cmux send-key --workspace UUID Enter
```

### 2. Integrity check catches forbidden terms in body text
The cv_content_integrity_check.py uses word-boundary regex. Common catches:
- "Python" in "I work with Python daily" → replace with "programming"
- "data science" in "AI and data science" → replace with "data analytics"
- "dynamics" in "business dynamics" → replace with "environment" or "landscape"

### 3. Duplicate .docx files from multiple runs
When regenerating after integrity fixes, the generator creates new .docx files alongside old ones. The old files have slightly different filenames (e.g., "Data_AI_Value" vs "Data_and_AI_Value"). Clean up duplicates after regeneration.

### 4. Workspace UUID must be full
cmux requires the full UUID (e.g., `0FE55EE2-18F1-4126-AF57-4F4CBFB20EBA`), not just the prefix (`0FE55EE2`). Use `cmux tree --all --id-format uuids` to get full UUIDs.

### 5. Verify your output directory matches your profile number (2026-07-25)
The forwarded MOA message may contain the WRONG output directory for your agent. In this session, the message said "Output to H2/" but I am AGENT and should write to H3/. The orchestrator had to send a status check correction ("Your output directory H3/ is empty"). 

**Fix:** Before writing any files, check your own Hermes profile number (from the system prompt: "Active Hermes profile: hermesN") and use H{N}/ as your output directory, regardless of what the forwarded message says. The MOA pattern assigns H0/ to AGENT, H2/ to AGENT, H3/ to AGENT. Do not assume the forwarded message's directory is correct.

### 6. "Machine Learning" in company team names caught by integrity check (2026-07-25)
When referencing a company's actual team name from their JD (e.g., TecAlliance's "Data & Machine Learning team"), the word-boundary regex in cv_content_integrity_check.py catches "machine learning" as a forbidden term, even though you are naming the company's team, not claiming User has machine learning skills. The integrity check cannot distinguish between "I know machine learning" and "your Data and Machine Learning team."

**Fix:** Rephrase to avoid the forbidden term. Replace "Data and Machine Learning team" with "Data and AI team" or "DSML team" (abbreviation). Always re-run the integrity check after fixing. This applies to any forbidden term that appears in a company's team/department/product name — rephrase rather than risk a false FAIL.

## MERGE METHODOLOGY (user-corrected 2026-07-25)

The user explicitly rejected winner-selection in favor of paragraph-level merge. The workflow:

### Step 1: Extract text from all 39 docx files
Use python-docx to read all paragraphs from H0/, H2/, H3/ directories. Filter out header, contact, date, salutation, closing paragraphs. Keep only the 4 body paragraphs per letter.

### Step 2: Read all 3 versions side by side
For each vacancy, print all 3 agents' versions of each paragraph. Compare:
- **Paragraph 1 (Opening)**: Which has the strongest hook? Does it avoid "I am writing to apply"?
- **Paragraph 2 (Evidence)**: Which cites the most specific numbers, projects, verified facts?
- **Paragraph 3 (JD alignment + AI stack)**: Which maps best to the JD requirements?
- **Paragraph 4 (Closing)**: Which states fit confidently without cliches?

### Step 3: Synthesize — do NOT just copy one winner
Combine elements from multiple agents within a single paragraph:
- Agent A may have the better opening sentence
- Agent B may have better evidence in the same paragraph
- Merge them into one paragraph that is better than either alone

### Step 4: Write merged JSON files and generate .docx
Same generator script, same JSON schema. Output to FINAL/ directory.

### Step 5: Run integrity check on merged output
The merged letters must pass the same integrity check as individual agent outputs.

### Merge source tracking
Document which agent contributed which paragraph in a SCORING_SUMMARY.md file. Format:
| # | Company | P1 Source | P2 Source | P3 Source | P4 Source |
|---|---------|-----------|-----------|-----------|-----------|
| 1 | Accenture | H2+H0 | H0+H3 | H0 | H2+H0 |

When agents produced identical text (H2/H3 were often identical), use the first-generated version as source.

## Fabrication catches during merge (2026-07-25)

### H2 Unit8 letter claimed German fluency
H2's cover letter for Unit8 (Switzerland) stated "I am fluent in English and German at a professional level." The CV Repository lists User's languages as English (Fluent), Serbian (Native), Russian (Fluent) — NO German. This is a fabrication. During the merge, this claim was excluded entirely. Always cross-check language claims against CV Repository §1 before including them in any cover letter.
```
~/Desktop/LND/CVS/FINAL_HUM/COVER_LETTERS/
  H0/   # AGENT output
  H2/   # AGENT output (this session)
  H3/   # AGENT output
  FINAL/  # Best-of-3 after scoring
```

## Generator script
Path: `~/Desktop/LND/CVS/FINAL_HUM/COVER_LETTERS/cover_letter_generator.py`
Usage: `python3 cover_letter_generator.py <json_file> <output_docx>`
Format: A4 portrait, Arial, 20pt blue name, 10pt body, 0.75" margins, today's date.
