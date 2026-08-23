# CV Fabrication Audit — 2026-07-25

## Incident

On 2026-07-25, a mixture-of-agents (MOA) CV generation pipeline produced 13 tailored CVs across AGENT, AGENT, and AGENT. An external reviewer (Claude) found that the CVs contained fabricated technical competencies lifted directly from job descriptions — terms like Azure AI, OAuth2, Python, Kubernetes, RAG, neural networks, MLOps, Scrum, microservices — none of which exist in User's CV Repository Database.

## Root Cause

The agents (especially AGENT/GLM-5.2, the smartest) mirrored JD vocabulary too aggressively. When a JD mentioned "Azure AI Foundry, RAG architectures, fine-tuning pipelines, OAuth2/OpenID Connect," the agents copied these into the Core Competencies section as if they were User's skills. This is a §0.3/§0.9 violation ("nothing invented or inflated," "never manufacture a match").

## Audit Method

### 1. Word-Boundary Regex (not substring)

Use `re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE)` — NOT `term in text.lower()`. Substring matching produces false positives:
- "RAG" matches inside "average" (ave-**rag**-e)
- "Rust" matches inside "trust" (tru-**st**)
- "agile" might match inside other words

### 2. Denylist (70+ terms)

Terms that must NEVER appear in a CV unless they're in the CV Repository:

**Cloud/Platforms:** Azure, Azure AI, GCP, Google Cloud, Foundry, AI Search, AI Studio, Copilot, Power BI, Power Platform, SharePoint, Dynamics

**Languages:** Python, Java, JavaScript, TypeScript, C#, C++, Go, Rust, Scala, R

**Infrastructure:** Kubernetes, Docker, Terraform, Ansible, Helm, Istio, Nginx

**AI/ML:** TensorFlow, PyTorch, scikit-learn, Keras, Hugging Face, LangChain, LlamaIndex, Pinecone, Weaviate, Chroma, RAG, retrieval-augmented generation, fine-tuning, neural network, deep learning, machine learning, NLP, computer vision, MLOps, DevOps, DevSecOps, prompt engineering

**Databases:** PostgreSQL, MongoDB, Cassandra, Redis, Elasticsearch, Neo4j, vector database, vector store

**Web frameworks:** React, Angular, Vue, Node.js, Flask, Django, FastAPI, Spring Boot, ASP.NET

**Data engineering:** Spark, Kafka, RabbitMQ, Airflow, Databricks, Snowflake, MLflow, Kubeflow

**Methodologies:** Scrum, waterfall, agile (as a claimed skill), microservices, containerization

**Data concepts:** data quality, data science, data maturity, model governance, analytics centre, data governance, data lineage

**Security:** OAuth, OAuth2, OpenID, SAML, JWT, Kerberos

**Other:** blockchain, Scrapling (wrong tool name — repo says Scrapple)

### 3. Approved Terms (in the repository — safe to use)

**AI tools:** Hermes AI, OpenClaw, CMUX, Ollama, OpenRouter, MLX, MCP (Model Context Protocol)
**Automation:** SearXNG, Camoufox, Scrapple (NOT Scrapling), Playwright, Chrome CDP (Chrome DevTools Protocol), Tesseract OCR, OCRMAC, RapidAPI-OCR
**AI patterns:** RAG (Retrieval-Augmented Generation), LLM-WIKI, OKF (Open Knowledge Format), agentic memory, sessions memory, Agent Harness
**Hardware:** NVIDIA DGX-B200, Moonshot Kimi K2.6 NVFP4
**Cloud:** AWS (NOT Azure, NOT GCP)
**Enterprise:** SAP ERP, VMware (virtualized — NOT "virtualization"), Cisco Webex
**LMS:** Moodle, Canvas, SCORM, xAPI
**Telecom:** VSAT, SDH, DSL, FTTX/GPON, 3G/4G/5G, Wi-Fi, LTE
**Other:** API/web services bridges, OCR pipelines, LLM, AI agents, agentic workflows

### 4. What to Do When a JD Requires a Skill User Doesn't Have

1. DO NOT fabricate the skill
2. DO NOT mirror JD vocabulary for tools/platforms User hasn't used
3. Lean on adjacent genuine experience (API integration, team leadership, platform delivery)
4. Acknowledge the gap honestly if needed
5. Source competencies ONLY from CV Repository §2 Option C + §3.1-§3.12

## Fixes Applied on 2026-07-25

| CV | Fabricated Terms | Fixed To |
|----|-----------------|----------|
| Comtrade | Azure AI, Foundry, AI Search, OAuth2, OpenID, RAG, vector database, fine-tuning | Hermes AI, CMUX, MCP, Scrapple, SearXNG, Camoufox, Tesseract, OCRMAC, RapidAPI-OCR |
| BCG | Azure, microservices, Agile Methods, containerization | AWS, Hermes AI, CMUX, enterprise architecture, Delivery Methods |
| EY | Azure AI, AI Search, AI Studio | Hermes AI, CMUX, Ollama, OpenRouter, MCP servers |
| TecAlliance | Python, Azure, data quality | API integration, AWS, Hermes AI, CMUX, operational efficiency |
| Zühlke | Azure, Kubernetes, OAuth2, OpenID, RAG | AWS, API integration, Scrapple, agentic workflows |
| Everseen | neural network, Scrum, waterfall, Agile | agentic AI workflows, cross-functional delivery, Delivery Frameworks |
| Neurons Lab | prompt engineering | AI tool deployment |
| Tenstorrent | Agile | Delivery Frameworks |
| Unit8 | machine learning, MLOps, data science, data maturity, model governance, analytics centre, data governance | AI adoption, AI operations, AI tooling, AI maturity, operational excellence |
| All CVs (4) | Scrapling (wrong name) | Scrapple (correct name) |
| All CVs (6) | virtualization | virtualized |

## Verification Script

`scripts/cv_content_integrity_check.py` — run on any directory of .docx files:
```bash
python3 scripts/cv_content_integrity_check.py /path/to/cv_directory
```

Exit 0 = all pass, exit 1 = fabrications found.

## Key Lessons

1. The smartest agent (AGENT/GLM-5.2) was the WORST fabricator — don't assume model quality prevents fabrication
2. JD vocabulary mirroring is fine for CONCEPTS but NOT for TOOLS/PLATFORMS/LANGUAGES
3. Internal structural checks (page size, roles, formatting) don't catch content fabrication — you need a content integrity check
4. External review (Claude) caught what 3 agents + humanizer analyzer missed
5. Word-boundary regex is essential — substring matching produces false positives that waste time
6. The humanizer can introduce new errors (Key Achievement → central Achievement) — always re-audit after humanization
