#!/usr/bin/env python3
"""
CV Content Integrity Check — Anti-Fabrication Audit

Checks every .docx in a directory for fabricated technical terms that don't
exist in the CV Repository Database. Uses word-boundary regex (not substring)
to prevent false positives.

Usage:
    python3 cv_content_integrity_check.py /path/to/cv_directory

Exit 0 = all CVs clean
Exit 1 = fabrications found

Based on the 2026-07-25 fabrication incident where MOA-generated CVs contained
JD-lifted terms (Azure AI, OAuth2, Python, Kubernetes, RAG, etc.) presented as
User's competencies.
"""

import sys
import os
import re
from docx import Document

REPO_PATH = '~/CV_REPOSITORY_DATABASE.md'

# Terms that must NEVER appear unless they exist in the repository
DENYLIST = [
    # Cloud/Platforms
    'Azure', 'Azure AI', 'GCP', 'Google Cloud', 'Foundry', 'AI Search', 'AI Studio',
    'Copilot', 'Power BI', 'Power Platform', 'SharePoint', 'Dynamics',
    # Languages
    'Java', 'JavaScript', 'TypeScript', 'C#', 'C++', 'Go', 'Rust', 'Scala',
    # Infrastructure
    'Kubernetes', 'Terraform', 'Ansible', 'Nginx',
    # AI/ML
    'TensorFlow', 'PyTorch', 'scikit-learn', 'Keras', 'Hugging Face',
    'LangChain', 'LlamaIndex', 'Pinecone', 'Weaviate', 'Chroma',
    'retrieval-augmented', 'fine-tuning', 'fine-tune',
    'neural network', 'deep learning', 'machine learning',
    'MLOps', 'DevOps', 'DevSecOps', 'prompt engineering',
    # Databases
    'PostgreSQL', 'MongoDB', 'Cassandra', 'Redis', 'Elasticsearch', 'Neo4j',
    'vector database', 'vector store',
    # Web frameworks
    'React', 'Angular', 'Vue', 'Node.js', 'Flask', 'Django', 'FastAPI',
    # Data engineering
    'Spark', 'Kafka', 'RabbitMQ', 'Airflow', 'Databricks', 'Snowflake',
    'MLflow', 'Kubeflow',
    # Methodologies
    'Scrum', 'waterfall', 'microservices', 'containerization',
    # Data concepts
    'data quality', 'data science', 'data maturity', 'model governance',
    'analytics centre', 'data governance', 'data lineage',
    # Security
    'OAuth', 'OAuth2', 'OpenID', 'SAML', 'JWT',
    # Other
    'blockchain', 'Scrapling',  # wrong tool name — repo says Scrapple
]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cv_content_integrity_check.py <directory_with_docx_files>")
        sys.exit(1)

    cv_dir = sys.argv[1]

    if not os.path.isdir(cv_dir):
        print(f"ERROR: Directory not found: {cv_dir}")
        sys.exit(1)

    # Load repository as source of truth
    if not os.path.exists(REPO_PATH):
        print(f"ERROR: CV Repository not found at {REPO_PATH}")
        sys.exit(1)

    with open(REPO_PATH, 'r') as f:
        repo_text = f.read()

    # Check each CV
    all_clean = True
    cv_files = [f for f in sorted(os.listdir(cv_dir)) if f.endswith('.docx')]

    if not cv_files:
        print(f"No .docx files found in {cv_dir}")
        sys.exit(0)

    print(f"Checking {len(cv_files)} CV files in {cv_dir}")
    print(f"Repository: {REPO_PATH}")
    print(f"Denylist: {len(DENYLIST)} terms")
    print("=" * 70)

    for cv_file in cv_files:
        cv_path = os.path.join(cv_dir, cv_file)
        try:
            doc = Document(cv_path)
        except Exception as e:
            print(f"ERROR reading {cv_file}: {e}")
            all_clean = False
            continue

        full_text = ' '.join([p.text for p in doc.paragraphs])

        fabrications = []
        for term in DENYLIST:
            # Word-boundary regex — prevents false positives
            cv_match = re.search(r'\b' + re.escape(term) + r'\b', full_text, re.IGNORECASE)
            repo_match = re.search(r'\b' + re.escape(term) + r'\b', repo_text, re.IGNORECASE)
            if cv_match and not repo_match:
                fabrications.append(term)

        if fabrications:
            all_clean = False
            print(f"FAIL: {cv_file}")
            for fab in fabrications:
                # Find where it appears
                for i, p in enumerate(doc.paragraphs):
                    if re.search(r'\b' + re.escape(fab) + r'\b', p.text, re.IGNORECASE):
                        match = re.search(r'\b' + re.escape(fab) + r'\b', p.text, re.IGNORECASE)
                        idx = match.start()
                        context = p.text[max(0, idx-30):idx + len(fab) + 30]
                        print(f"  [{fab}] para {i}: ...{context}...")
                        break
            print()
        else:
            print(f"PASS: {cv_file}")

    print("=" * 70)
    if all_clean:
        print(f"ALL {len(cv_files)} CVs CLEAN — no fabrications found")
        sys.exit(0)
    else:
        failed = sum(1 for f in cv_files if any(
            re.search(r'\b' + re.escape(term) + r'\b',
                      ' '.join([p.text for p in Document(os.path.join(cv_dir, f)).paragraphs]),
                      re.IGNORECASE) and
            not re.search(r'\b' + re.escape(term) + r'\b', repo_text, re.IGNORECASE)
            for term in DENYLIST
        ))
        print(f"{failed}/{len(cv_files)} CVs HAVE FABRICATIONS — fix before delivery")
        sys.exit(1)


if __name__ == '__main__':
    main()
