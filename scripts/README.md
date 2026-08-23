# cv_generator.py — JSON Content Schema

## Usage

```bash
python3 scripts/cv_generator.py cv_content_Company_Role.json
```

Produces `User_CV_Company_Role.docx` in the same directory.

## JSON Schema

```json
{
    "headline": "TECHNICAL PROGRAM MANAGER — AI/ML",
    "profile": "150-word professional profile paragraph...",
    "competencies": [
        "Category: item1 • item2 • item3 • item4",
        "Category2: item1 • item2 • item3"
    ],
    "experience": [
        {
            "title": "ROLE TITLE",
            "org": "Organization",
            "location": "City, Country",
            "dates": "Month YYYY – Present",
            "bullets": [
                "Compound bullet: fact 1, fact 2, and fact 3.",
                "Key Achievement: one crisp sentence."
            ]
        }
    ],
    "additional_experience": [
        "Role | Company | Location | Dates — one compound sentence."
    ],
    "education": [
        "• Degree, Institution, Years"
    ],
    "languages": "English – Fluent/Business | Serbian – Native | Russian – Fluent/Business",
    "company": "CompanyName",
    "role": "Role_Title_With_Underscores"
}
```

## Rules

- `headline`: 4-9 words, uppercase, tailored per vacancy
- `profile`: ~150 words (140-160 range), no first-person pronouns
- `competencies`: 10-14 phrases, ordered by employer priority
- `experience`: 3-5 roles, reverse chronological, max 3 bullets each (last = Key Achievement)
- `additional_experience`: optional, max 3 one-liners
- `company` and `role`: used for filename generation (underscores, no spaces)
- Name is always User MARKOVIĆ (with diacritic) — hardcoded in the script
- Contact block is hardcoded: phone, email, LinkedIn, city, citizenship
- Footer is hardcoded: "User Marković" 9pt centered

## §0.4 Formatting Implemented

- A4 portrait (8.2677" x 11.6929")
- Margins: 0.45" top/bottom, 0.6201" left/right
- Arial throughout
- Name: 20pt bold #365F91, centered, 1pt #4F81BD bottom rule, 0.25pt expanded spacing
- Headline: 12pt bold italic, centered, 0.75pt expanded spacing
- Contact: 9pt black, centered, two lines with manual line break
- Section headings: 12pt bold #1F497D, bottom border, keep-with-next
- Role title: 10pt bold black
- Date: 10pt regular black
- Bullets: • U+2022, 10pt, 0.18" left indent, 0.12" hanging
- Footer: "User Marković" 9pt centered, every page
