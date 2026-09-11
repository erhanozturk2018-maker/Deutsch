# 05 — Validation Log

> **Purpose:** The authoritative record of every validation performed on the project: what was checked, against which criteria, what was found, and whether it was approved.
>
> **Rule:** Record only validations that actually happened. Never pre-fill results. Append new entries at the bottom and add them to the index. Entries are not rewritten afterwards; later corrections go in a new entry that references the old one.
>
> Criteria come from [03_MILESTONES.md](03_MILESTONES.md) (per milestone) and from the quality checklist in [04_LESSON_STANDARDS.md](04_LESSON_STANDARDS.md) (Part C, per file).

## Entry index

| ID | Date | Milestone | Artifact(s) | Type | Result | Approval |
|---|---|---|---|---|---|---|
| V-001 | 2026-09-11 | M1 | M1 infrastructure (`Docs/`, `CLAUDE.md`, `.gitignore`, course root, git) | Self-validation + automated checks | PASS WITH NOTES | Pending user approval |

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
- **Method:**
  - **Filesystem:** `find . -path ./.git -prune -o -print` on the workspace, compared with the M1 deliverable list.
  - **Links:** a Python link and anchor checker (a temporary script in the session scratchpad, not in the repository). It resolves every relative link and GitHub-style heading anchor in all `.md` files, skipping code blocks.
  - **Consistency:** `grep` over `Docs/*.md` and `CLAUDE.md` for:
    - stale "pending" references to decisions that are now resolved
    - M1 still marked in progress
    - M2 marked as started
    - leftover "M1 deliverable" references in `01`
  - **Authority:** `grep` for authority statements.
  - **Recovery:** a read-through of the path `CLAUDE.md` → `00` §1–2 → `03`, checking whether current milestone, next action, rules and open decisions can be found without chat history.
  - **Scope:** listed every file under `GERMAN_LEARNING_PLAN/`.
  - **Git:** `git init -b main`, `git status --short` of the staged set before committing, `git log --stat`, `git status --short --branch` after committing, and an ignored-files check.
- **Findings:**
  1. `STR`, PASS. All M1 deliverables exist: `Docs/00`–`06` (7 files), `CLAUDE.md`, `.gitignore`, `GERMAN_LEARNING_PLAN/` (containing only `.gitkeep`), `.git/`.
  2. `LNK`, PASS. **41 links checked, 0 broken**, including 28 anchors inside `01` and `04`.
  3. `REC` (consistency), PASS. No stale "pending" references to OD-05/06/07/08/09/10/12. M2 is not marked as started. The only "M1 … in progress" text is changelog entry [001], which was correct when it was written (a historical entry, not a contradiction).
  4. `REC` (authority), PASS. `Docs/` is named as the source of truth in `CLAUDE.md`. `01` is named as the authoritative architecture record in its header, in CD-43 and in Appendix H.
  5. `REC` (recovery), PASS. From `CLAUDE.md` and `00` §1 alone, a new session can find: the project, current and next milestone, next action, binding workflow rules (`00` §4), open decisions (`00` §12), existing and planned files (`00` §13–14), and architecture (`01`).
  6. `SCP`, PASS. `GERMAN_LEARNING_PLAN/` contains only `.gitkeep`. No lesson, unit, diagnostic, checkpoint, resource or workbook file exists.
  7. `VCS`, PASS:
     - Repository initialised on branch `main`.
     - Commit `024a999` "M1 infrastructure initialized", author Erhan, contains exactly the 10 intended files (2,453 lines).
     - Working tree clean after the commit.
     - No ignored or unnecessary files present or committed.
     - This validation record was written after that commit and is committed separately. There are no fake historical commits.
  8. `VCS`, **Note.** Git prints "LF will be replaced by CRLF" warnings because of the global `core.autocrlf` setting. This is harmless: file content is unaffected. An optional `.gitattributes` could silence it later.
  9. `STR`, **Note.** The user narrowed M1's scope when defining its completion (2026-09-11). Course README, stage READMEs, `Resources/` and `Learner_Workbook/` were moved out of M1 and provisionally reallocated just in time to later milestones (OD-13). This is recorded in `00`, `03` and `06`; nothing was dropped silently.
  10. `PED`, **Note.** Several numeric targets in `04` are first estimates (KI-11). They must be confirmed by the M4 pilot and the B1-U01 review stop.
  11. `STR`, **Note.** `04` A2 lists 19 components, while Appendix I of `01` lists 18 sections. `04` splits Reading and Listening and makes the Answer key explicit. This refines the approved template; it does not change the architecture.
  12. `REC`, **Note.** `02` (file-level check) and `04` Part C (quality checklist) overlap on purpose: `02` is the short constitutional check, `04` the full acceptance checklist. `03` requires both. They can be merged later if the overlap causes friction.
- **Required changes:** None.
- **Resolution:** Not applicable (no defects found).
- **Result:** **PASS WITH NOTES**
- **Approval status:** Pending user approval
