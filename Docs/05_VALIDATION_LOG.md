# 05 — Validation Log

> **Purpose:** The authoritative record of every validation performed on the project: what was checked, against which criteria, what was found, and whether it was approved.
>
> **Rule:** Record only validations that actually happened. Never pre-fill results. Append new entries at the bottom and add them to the index. Entries are not rewritten afterwards; later corrections go in a new entry that references the old one.
>
> Criteria come from [03_MILESTONES.md](03_MILESTONES.md) (per milestone) and from the quality checklist in [04_LESSON_STANDARDS.md](04_LESSON_STANDARDS.md) (Part C, per file).

## Entry index

| ID | Date | Milestone | Artifact(s) | Type | Result | Approval |
|---|---|---|---|---|---|---|
| V-001 | 2026-09-11 | M1 | M1 infrastructure (`Docs/`, `CLAUDE.md`, `.gitignore`, course root, git) | Self-validation + automated checks | See entry | Pending user approval |

---

## Validation types

| Type | Meaning |
|---|---|
| **Self-validation** | Claude checks the artifact against the criteria and records what it checked and how |
| **Automated check** | A script or command (link checker, file listing, `git` inspection). The command and its output summary are recorded |
| **User review** | The user reviews and gives feedback or approval |
| **Learner trial** | The learner actually works through the material and reports time, difficulty and problems. This is the strongest evidence for workload and usability |

## Validation categories

| Code | Category | Typical checks |
|---|---|---|
| `STR` | Structural | Files and folders exist as planned (Appendix H of `01`); required components present (`04` A3) |
| `LNG` | Linguistic | Grammar, spelling, translations, answer keys correct |
| `PED` | Pedagogical | Design principles (`02`) met; communicative progression; grammar serves tasks |
| `CEF` | CEFR / progression | Level-appropriate; can-do objectives; difficulty increases sensibly |
| `DEP` | Prerequisite / dependency | Nothing requires later material (Appendices C–D of `01`); metadata accurate |
| `VOC` | Vocabulary | Sizes (Appendix E); recycling rules (`04` A8); collocations and chunks |
| `SPK` | Speaking | S-level progression (`04` A6); timed and unscripted activities present |
| `WRK` | Workload | Time estimates vs targets; actual times from learner trials |
| `LNK` | Markdown / link integrity | Links resolve (or are *planned* targets); rendering; heading hierarchy; naming |
| `USE` | Learner usability | Clear instructions; navigation; the learner can work without help |
| `SCP` | Scope compliance | Only the current milestone's work was done; no unapproved architecture changes |
| `REC` | Recovery / documentation | A new session can resume from `Docs/` + `CLAUDE.md`; state files current and consistent |
| `VCS` | Version control | Repository state, commits, nothing unnecessary tracked |

## Severity scale

| Severity | Meaning | Consequence |
|---|---|---|
| **Critical** | Breaks the learning path or the architecture (e.g. wrong prerequisite order, missing answer keys, broken navigation, a silent architecture change) | Must be fixed before approval |
| **Major** | Clearly lowers quality (e.g. an unnatural example set, too little retrieval, workload well off target) | Must be fixed, or explicitly accepted by the user |
| **Minor** | Small defect (e.g. a typo, a single weak example, a formatting slip) | Fix during the next pass; does not block |
| **Note** | An observation or suggestion with no defect | No action required |

## Approval status values

`Pending user approval` · `Approved` · `Approved with changes` · `Rejected` · `Superseded by V-xxx`

## Entry format

```text
## V-NNN — <short title>
- Date:
- Milestone:            (and work package, if any)
- Artifact(s):
- Validator:            (Claude / user / learner)
- Validation type:      (self-validation / automated check / user review / learner trial)
- Categories:           (codes from the table above)
- Criteria:             (list, or a reference to 03_MILESTONES / 04 Part C)
- Method:               (how each criterion was checked, including commands)
- Findings:             (numbered; each with category + severity)
- Required changes:
- Resolution:           (what was changed, where, when)
- Result:               PASS / PASS WITH NOTES / FAIL
- Approval status:
```

---

## V-001 — M1 infrastructure validation

- **Date:** 2026-09-11
- **Milestone:** M1 — Project Infrastructure (closing validation)
- **Artifact(s):**
  - `Docs/00_PROJECT_STATE.md`, `01_CURRICULUM_DECISIONS.md`, `02_DESIGN_PRINCIPLES.md`, `03_MILESTONES.md`, `04_LESSON_STANDARDS.md`, `05_VALIDATION_LOG.md`, `06_CHANGELOG.md`
  - `CLAUDE.md`, `.gitignore`, `GERMAN_LEARNING_PLAN/` (course root), git repository
- **Validator:** Claude
- **Validation type:** Self-validation + automated checks
- **Categories:** `STR`, `LNK`, `REC`, `SCP`, `VCS`
- **Criteria:** The M1 validation criteria in `03_MILESTONES.md`:
  1. The expected structure exists.
  2. Internal links resolve.
  3. No contradictory architecture exists across Docs.
  4. The authoritative source is clearly identified.
  5. A new session can recover the project from the filesystem.
  6. The repository is initialised with an initial commit, and nothing unnecessary is committed.
  7. No lesson, diagnostic, or A1/A2/B1 content was created.
- **Status:** IN PROGRESS. Results are recorded below once the checks have run.
