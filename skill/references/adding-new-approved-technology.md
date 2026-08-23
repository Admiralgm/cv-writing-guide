# Adding a New Approved Technology to the CV Repository

## Context

On 2026-07-28, User asked to add Docker (macOS) and Python to the CV Repository Database as genuine competencies. Both terms were previously on the anti-fabrication FORBIDDEN list (and in the integrity check script's DENYLIST) because they had been lifted from job descriptions by a mixture-of-agents pipeline on 2026-07-25. The user's request was legitimate — he actively uses Docker for sandboxed AI projects and develops Python scripts daily as part of Hermes AI skill creation.

## The Four-Location Cascade Update

When a user acquires a new technology competency that was previously FORBIDDEN, four independent locations must be updated atomically. Missing any one leaves the system in an inconsistent state where the next CV generation session will flag the now-legitimate technology as a fabrication.

### Location 1 — CV Repository Database (`~/CV_REPOSITORY_DATABASE.md`)

Add the new technology to **six places** in the database:

1. **Header version number** — bump the `Repository version:` line
2. **Changelog** — new version row at the top of the changelog table describing the addition
3. **§4.5** (Advanced AI Stack) — new bullet(s) with factual description of how the technology is used
4. **§6** (ATS Keyword Bank) — new line in Bank 2 (AI Centre of Excellence) with the keyword
5. **§7** (Skills Inventory) — new entry under the appropriate category (usually "Artificial Intelligence & Automation")
6. **Footer version number** — bump the version in the end-of-file italic line

Always backup first: `cp CV_REPOSITORY_DATABASE.md CV_REPOSITORY_DATABASE.md.bak.$(date +%Y%m%d_%H%M%S)`

### Location 2 — cv-writing SKILL.md

Three edits in the anti-fabrication section:

1. **Approved terms list** — add the technology with a parenthetical description
2. **Forbidden terms list** — remove the technology from the comma-separated string
3. **Inline DENYLIST** (inside the `HOW TO VERIFY` Python code block) — remove the technology from the DENYLIST array, add a NOTE comment documenting the removal date

### Location 3 — cv-repository-management SKILL.md

Three edits in the anti-fabrication protocol section:

1. **APPROVED list** — add the technology under the appropriate category heading (AI tools, Automation, Infrastructure, Languages, etc.)
2. **FORBIDDEN list** — remove the technology from the comma-separated forbidden terms string
3. **Inline DENYLIST** (inside the `HOW TO VERIFY` Python code block) — remove the technology from the DENYLIST array

### Location 4 — cv_content_integrity_check.py script

File location: `skills/productivity/cv-writing/scripts/cv_content_integrity_check.py`

Remove the technology from the `DENYLIST` array. This is the automated script that runs on every .docx before delivery — if the term stays here, every CV containing the now-legitimate technology will be flagged as a fabrication.

## Cross-Profile Sync

The skill files exist as **identical copies** (not symlinks) across profiles:
- `skills/productivity/cv-writing/` (shared)
- `skills/productivity/cv-writing/` (profile copy)

Similarly for cv-repository-management:
- `skills/productivity/cv-repository-management/` (shared)
- `skills/productivity/cv-repository-management/` (profile copy)

When patching with `cross_profile=True`, the shared copy is updated. After patching, verify with `diff` and sync with `cp` if the profile copies are separate files.

## Verification

After all edits:

1. `grep -n "NewTech" CV_REPOSITORY_DATABASE.md` — confirm the new technology appears in the expected sections (header, changelog, §4.5, §6, §7, footer)
2. Check the DENYLIST in the integrity check script — confirm the technology is NOT present
3. Check the forbidden terms list in both SKILL.md files — confirm the technology is NOT present
4. Check the approved terms list in both SKILL.md files — confirm the technology IS present
5. `diff` the shared vs profile copies of both skill files — confirm identical

## Pitfalls

- **Forgetting the inline DENYLIST in SKILL.md**: There are TWO denylists per skill — the one in the Python script file AND the one inside the SKILL.md's `HOW TO VERIFY` code block. Both must be updated. That's 4 denylists total across 2 skills + 1 script.
- **Forgetting the FORBIDDEN list string**: The FORBIDDEN list is a separate comma-separated paragraph in SKILL.md, not the same as the DENYLIST array. It must also be updated in both skills.
- **Cross-profile write guard**: Patching skill files under `skills/` from a AGENT session triggers the cross-profile soft guard. Use `cross_profile=True` after confirming this is the user's intent.
- **Backup before database edits**: Always `cp` the database file before any edit.
- **User-owned skills**: The `cv-repository-management` skill is user-owned (not curator-managed). The background curator cannot patch it. If it needs updating, recommend `hermes curator adopt cv-repository-management` to the user, or patch it during a foreground session with explicit user direction (cross_profile=True).