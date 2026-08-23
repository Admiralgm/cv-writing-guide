#!/usr/bin/env python3
"""
CV Generator v2 for User Marković — Reference-CV Format Match
Matches User_Tailored_Delivery_Lead_CV.docx format exactly:
- US Letter (8.5" x 11")
- 0.45" T/B, 0.6201" L/R margins
- 20pt bold #365F91 name with #4F81BD bottom rule
- 12pt bold headline (NOT italic — reference CV doesn't use italic)
- 9pt two-line contact block with manual line break
- 12pt bold #1F497D section headings (no bottom border in reference)
- 10pt body throughout
- NO bullet characters — plain paragraphs for impact statements
- "SELECTED DELIVERY IMPACT" section between competencies and experience
- ALL 12 experience roles included (3+ pages)
- Languages in contact block, not separate section
- Footer: "User Marković" 9pt centered

Usage:
    python3 cv_generator_v2.py <json_file>

JSON Schema:
{
    "headline": "ROLE TITLE | KEYWORDS | KEYWORDS",
    "profile": "150-word paragraph (no first person, no AI-slop)",
    "competencies": "Cat1: item1, item2 | Cat2: item1, item2 | ...",
    "delivery_impact": ["2-3 compound impact statements (paragraphs, no bullets)"],
    "experience": [
        {"title": "Role Title", "org": "Org", "location": "City, Country",
         "dates": "Month YYYY – Month YYYY",
         "bullets": ["paragraph...", "paragraph...", "Key Achievement: ..."]}
    ],
    "education": ["• Degree, Institution, Years"],
    "company": "CompanyName",
    "role": "Role_Title_Underscores"
}

Output: User_CV_<Company>_<Role>.docx in the same directory.
"""

import json
import sys
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Format constants from reference CV
COLOR_NAME = RGBColor(0x36, 0x5F, 0x91)
COLOR_NAME_RULE = RGBColor(0x4F, 0x81, 0xBD)
COLOR_HEADING = RGBColor(0x1F, 0x49, 0x7D)
COLOR_BODY = RGBColor(0x00, 0x00, 0x00)
FONT_FAMILY = "Arial"

# Default: US Letter (reference CV uses US Letter)
# Pass env A4=1 for A4 output (8.27" x 11.69")
USE_A4 = os.environ.get("A4", "").strip() in ("1", "true", "yes")
if USE_A4:
    PAGE_WIDTH = Inches(8.27)
    PAGE_HEIGHT = Inches(11.69)
else:
    PAGE_WIDTH = Inches(8.5)
    PAGE_HEIGHT = Inches(11.0)
MARGIN_TB = Inches(0.45)
MARGIN_LR = Inches(0.6201)


def add_bottom_border(paragraph, color_hex="4F81BD", size="8", space="4"):
    """Add a bottom paragraph border (for the name rule)."""
    pPr = paragraph._element.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), size)
    bottom.set(qn('w:space'), space)
    bottom.set(qn('w:color'), color_hex)
    pbdr.append(bottom)
    pPr.append(pbdr)


def set_character_spacing(paragraph, points):
    """Set expanded character spacing on a paragraph."""
    pPr = paragraph._element.get_or_add_pPr()
    rPr = pPr.find(qn('w:rPr'))
    if rPr is None:
        rPr = OxmlElement('w:rPr')
        pPr.append(rPr)
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:val'), str(int(points * 20)))
    rPr.append(spacing)


def set_keep_with_next(paragraph):
    """Prevent orphan headings."""
    pPr = paragraph._element.get_or_add_pPr()
    pPr.append(OxmlElement('w:keepNext'))
    pPr.append(OxmlElement('w:keepLines'))


def add_manual_line_break(paragraph):
    """Add a manual line break (Shift+Enter) within a paragraph."""
    run = paragraph.add_run()
    br = OxmlElement('w:br')
    run._element.append(br)


def add_section_heading(doc, text):
    """Add a 12pt bold #1F497D section heading (no bottom border, matching reference)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    set_keep_with_next(p)
    run = p.add_run(text.upper())
    run.font.name = FONT_FAMILY
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = COLOR_HEADING


def add_body_paragraph(doc, text, bold=False):
    """Add a 10pt body paragraph (no bullet character, matching reference CV)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(text)
    run.font.name = FONT_FAMILY
    run.font.size = Pt(10)
    run.font.bold = bold
    run.font.color.rgb = COLOR_BODY
    return p


def add_role_heading(doc, text):
    """Add a 10pt bold role heading (matching reference CV — bold but NOT blue)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    set_keep_with_next(p)
    run = p.add_run(text)
    run.font.name = FONT_FAMILY
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = COLOR_BODY
    return p


def build_cv(content, output_path):
    doc = Document()

    # Page setup — US Letter (matching reference CV)
    section = doc.sections[0]
    section.page_width = PAGE_WIDTH
    section.page_height = PAGE_HEIGHT
    section.top_margin = MARGIN_TB
    section.bottom_margin = MARGIN_TB
    section.left_margin = MARGIN_LR
    section.right_margin = MARGIN_LR

    # Normal style
    normal = doc.styles['Normal']
    normal.font.name = FONT_FAMILY
    normal.font.size = Pt(10)
    normal.font.color.rgb = COLOR_BODY
    normal.paragraph_format.space_after = Pt(2)
    normal.paragraph_format.line_spacing = 1.0

    # === THREE-LINE IDENTITY BLOCK ===

    # 1. Name — 20pt bold #365F91, centered, bottom rule
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run("User MARKOVI\u0106")
    run.font.name = FONT_FAMILY
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAME
    set_character_spacing(p, 0.25)
    add_bottom_border(p, "4F81BD", "8", "4")

    # 2. Headline — 12pt bold (NOT italic per reference CV), centered
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(content['headline'].upper())
    run.font.name = FONT_FAMILY
    run.font.size = Pt(12)
    run.font.bold = True
    set_character_spacing(p, 0.75)

    # 3. Contact — 9pt, centered, two lines with manual line break
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    r1 = p.add_run("Phone +381 64 110 8335 | email : XXXXXX  | linkedin.com/in/XXXXXX")
    r1.font.name = FONT_FAMILY; r1.font.size = Pt(9); r1.font.color.rgb = COLOR_BODY
    add_manual_line_break(p)
    r2 = p.add_run("Belgrade, Serbia | EU citizen (Czech Republic)")
    r2.font.name = FONT_FAMILY; r2.font.size = Pt(9); r2.font.color.rgb = COLOR_BODY

    # === PROFESSIONAL PROFILE ===
    add_section_heading(doc, content.get('profile_heading', 'PROFESSIONAL PROFILE'))
    add_body_paragraph(doc, content['profile'])

    # === CORE COMPETENCIES ===
    add_section_heading(doc, "CORE COMPETENCIES")
    # Competencies as a single paragraph with pipe separators (matching reference)
    if isinstance(content.get('competencies'), str):
        add_body_paragraph(doc, content['competencies'])
    elif isinstance(content.get('competencies'), list):
        add_body_paragraph(doc, " | ".join(content['competencies']))

    # === SELECTED DELIVERY IMPACT (optional, between competencies and experience) ===
    if content.get('delivery_impact'):
        add_section_heading(doc, content.get('delivery_impact_heading', 'SELECTED DELIVERY IMPACT'))
        for impact in content['delivery_impact']:
            add_body_paragraph(doc, impact)

    # === PROFESSIONAL EXPERIENCE ===
    add_section_heading(doc, "PROFESSIONAL EXPERIENCE")
    for exp in content['experience']:
        # Role title — bold
        role_text = exp['title']
        if exp.get('org'):
            role_text += " | " + exp['org']
        if exp.get('location'):
            role_text += " | " + exp['location']
        if exp.get('dates'):
            role_text += " | " + exp['dates']
        add_role_heading(doc, role_text)

        # Bullets as plain paragraphs (NO bullet character — matching reference CV)
        for bullet in exp['bullets']:
            add_body_paragraph(doc, bullet)

    # === ADDITIONAL RELEVANT EXPERIENCE (optional) ===
    if content.get('additional_experience'):
        add_section_heading(doc, "ADDITIONAL RELEVANT EXPERIENCE")
        for line in content['additional_experience']:
            add_body_paragraph(doc, line)

    # === EDUCATION ===
    add_section_heading(doc, "EDUCATION")
    for edu in content['education']:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(edu)
        run.font.name = FONT_FAMILY
        run.font.size = Pt(10)
        run.font.bold = True  # Reference CV has bold education entries
        run.font.color.rgb = COLOR_BODY

    # === LANGUAGES (in contact block per reference — only add separate section if requested) ===
    if content.get('languages_section'):
        add_section_heading(doc, "LANGUAGES")
        add_body_paragraph(doc, content['languages_section'])

    # === Footer ===
    footer = section.footer
    footer.is_linked_to_previous = False
    pf = footer.paragraphs[0]
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf.paragraph_format.line_spacing = 1.0
    run = pf.add_run("User Markovi\u0107")
    run.font.name = FONT_FAMILY
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_BODY

    doc.save(output_path)
    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cv_generator_v2.py <json_file>")
        sys.exit(1)
    json_path = sys.argv[1]
    with open(json_path, 'r', encoding='utf-8') as f:
        content = json.load(f)
    company = content.get('company', 'Unknown')
    role = content.get('role', 'Role')
    output_dir = os.path.dirname(os.path.abspath(json_path))
    output_path = os.path.join(output_dir, f"User_CV_{company}_{role}.docx")
    build_cv(content, output_path)
    print(f"OK: {output_path}")


if __name__ == "__main__":
    main()
