#!/usr/bin/env python3
"""
Cover Letter Generator — A4, Arial, matching CV §0.4 formatting lock.

Produces professional .docx cover letters from JSON input.

Usage:
    python3 cover_letter_generator.py <json_file> <output_docx>

JSON schema:
{
  "company": "Company Name",
  "role": "Role Title",
  "salutation": "Dear Hiring Manager,",
  "paragraphs": [
    "Paragraph 1 (50-80 words): Lead with verified value proposition",
    "Paragraph 2 (80-100 words): Map requirements to specific evidence",
    "Paragraph 3 (80-100 words): Continue mapping. AI stack for AI-lane roles",
    "Paragraph 4 (40-60 words): State fit confidently, invite discussion"
  ]
}

Output: A4 portrait, Arial font throughout.
  - 20pt blue (#365F91) name header with bottom border rule
  - 9pt contact line below header
  - 10pt right-aligned date
  - 10pt salutation
  - 10pt body paragraphs (4 paragraphs, 250-350 words total)
  - 10pt closing ("Sincerely, User")

Based on the §0.4 formatting lock from CV Repository Database v26.
"""

import json
import sys
import os
from datetime import date
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def add_bottom_border(paragraph):
    """Add a bottom border line to a paragraph (like the CV name header rule)."""
    p = paragraph._p
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '365F91')
    pBdr.append(bottom)
    pPr.append(pBdr)


def generate_cover_letter(json_path, output_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    doc = Document()

    # Page setup — A4
    section = doc.sections[0]
    section.page_width = Emu(7562215)   # 8.27"
    section.page_height = Emu(10689590) # 11.69"
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

    # Set default font to Arial throughout
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(10)

    # Name header — 20pt blue, bold
    name_para = doc.add_paragraph()
    name_para.paragraph_format.space_after = Pt(2)
    name_run = name_para.add_run('User')
    name_run.font.name = 'Arial'
    name_run.font.size = Pt(20)
    name_run.font.bold = True
    name_run.font.color.rgb = RGBColor(0x36, 0x5F, 0x91)
    add_bottom_border(name_para)

    # Contact line — 9pt
    contact_para = doc.add_paragraph()
    contact_para.paragraph_format.space_after = Pt(6)
    contact_run = contact_para.add_run(
        'Belgrade, Serbia  |  +381 64 110 8335  |  your-handle@gmail.com  |  '
        'linkedin.com/in/User-markovic3229  |  Dual National — Czech Republic (EU) & Serbia'
    )
    contact_run.font.name = 'Arial'
    contact_run.font.size = Pt(9)

    # Date — right-aligned, 10pt
    date_para = doc.add_paragraph()
    date_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    date_para.paragraph_format.space_after = Pt(6)
    date_para.paragraph_format.space_before = Pt(6)
    today = date.today().strftime('%d %B %Y')
    date_run = date_para.add_run(today)
    date_run.font.name = 'Arial'
    date_run.font.size = Pt(10)

    # Company address (optional)
    if data.get('company'):
        company_para = doc.add_paragraph()
        company_para.paragraph_format.space_after = Pt(6)
        company_run = company_para.add_run(data['company'])
        company_run.font.name = 'Arial'
        company_run.font.size = Pt(10)

    # Salutation — 10pt
    salutation = data.get('salutation', 'Dear Hiring Manager,')
    sal_para = doc.add_paragraph()
    sal_para.paragraph_format.space_after = Pt(6)
    sal_run = sal_para.add_run(salutation)
    sal_run.font.name = 'Arial'
    sal_run.font.size = Pt(10)

    # Body paragraphs — 10pt
    for para_text in data.get('paragraphs', []):
        body_para = doc.add_paragraph()
        body_para.paragraph_format.space_after = Pt(6)
        body_para.paragraph_format.line_spacing = 1.15
        body_run = body_para.add_run(para_text)
        body_run.font.name = 'Arial'
        body_run.font.size = Pt(10)

    # Closing — 10pt
    closing_para = doc.add_paragraph()
    closing_para.paragraph_format.space_before = Pt(6)
    closing_run = closing_para.add_run('Sincerely,\nUser')
    closing_run.font.name = 'Arial'
    closing_run.font.size = Pt(10)

    doc.save(output_path)
    print(f'Generated: {output_path}')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 cover_letter_generator.py <json_file> <output_docx>')
        sys.exit(1)
    generate_cover_letter(sys.argv[1], sys.argv[2])
