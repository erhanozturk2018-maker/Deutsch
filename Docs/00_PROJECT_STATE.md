# 00 — Project State

> **Read this file first.** It is the persistent memory of the project. A new session must be able to continue the work from `Docs/` alone, without any chat history.
>
> **Last updated:** 2026-09-11. Session 3: M1 completed. **Update this file whenever the project state changes.**

---

## 1. Status

```text
Project:            German A1 → B1 Curriculum
Architecture:       Approved — Baseline v1.0 (2026-09-11)
Current Phase:      Curriculum Construction
Current Milestone:  M1 — Project Infrastructure
Status:             COMPLETE (2026-09-11; validation V-001)
Next Milestone:     M2 — Diagnostic System
Next Status:        NOT STARTED / AWAITING APPROVAL
Next action:        Wait for explicit user approval to start M2. Confirm OD-13 (allocation of deferred M1 items) at M2 start.
Blocked by:         Nothing, except the user's go-ahead for M2
```

---

## 2. How to resume (new session)

1. Read this file, then the relevant parts of:
   - [02_DESIGN_PRINCIPLES.md](02_DESIGN_PRINCIPLES.md): the constitution
   - [01_CURRICULUM_DECISIONS.md](01_CURRICULUM_DECISIONS.md): architecture + change control
   - [03_MILESTONES.md](03_MILESTONES.md): what each milestone builds and how it is validated
   - [04_LESSON_STANDARDS.md](04_LESSON_STANDARDS.md): how every course file is built
   - [05_VALIDATION_LOG.md](05_VALIDATION_LOG.md): what has been validated and approved
   - [06_CHANGELOG.md](06_CHANGELOG.md): history

   The workspace-level `CLAUDE.md` summarises this procedure.
2. Find the current milestone and its open deliverables in `03_MILESTONES.md`.
3. Check §12 (unresolved decisions). **Never assume an answer. Ask the user.**
4. Work **only** on the current milestone.
5. Anything that would change the architecture (the CD decisions or Appendices A–J in `01`) goes through **change control** (end of `01`). Never change it silently.
6. After each work package, update this file and commit. At milestone end, follow the close procedure (§4), then **STOP**.

---

## 3. What this project is

A complete, CEFR-aligned German course from the learner's current level (A1 known, A2 partial) to the **end of B1**. It is written as Markdown in `C:\Users\erhan\Desktop\Deutch\GERMAN_LEARNING_PLAN\`.

The goal is **functional B1 communication**, not grammar coverage. The course prioritises production, active retrieval, spontaneous speaking and spiral recycling.

It is designed by Claude acting as German teacher and curriculum designer, and built incrementally over many sessions in milestones M0–M8. The project is under git version control.

---

## 4. Workflow rules (binding)

- **Design → Build → Validate → Approve → Scale.** Never generate the whole curriculum in one operation.
- **Milestone isolation.** Only the current milestone. Never start the next milestone without explicit user approval.
- **Closing a milestone:**
  1. Update this file.
  2. Update `03_MILESTONES.md`.
  3. Update `06_CHANGELOG.md`.
  4. Validate and log in `05_VALIDATION_LOG.md`.
  5. Summarise what was created.
  6. List unresolved issues.
  7. Commit.
  8. **STOP.**
- **Work packages** in M5–M7 (and proposed for M3), with a state save and commit after each.
- **Pilot before scaling.** A2-U01 (M4) must be approved before other A2/B1 units are built. Mandatory second validation at the review stop after B1-U01 (M6 WP1).
- **Diagnostic before A1.** The learner takes the M2 diagnostic, and the results are recorded, before M3 starts.
- **No silent architectural changes.** Problem → explanation → proposal → register entry (`01`, change control) → user approval → apply → changelog.
- **Local corrections** (wording, examples, exercise choice, fixes within a unit) may be made normally. Log significant ones.
- **Validation log** records only validations that actually happened.

---

## 5. Milestones

| ID | Milestone | Status |
|---|---|---|
| M0 | Curriculum Architecture | ✅ COMPLETE (2026-09-11) |
| M1 | Project Infrastructure | ✅ COMPLETE (2026-09-11), V-001 |
| M2 | Diagnostic System | ⏸️ NOT STARTED — AWAITING APPROVAL |
| M3 | A1 Consolidation | ⬜ NOT STARTED (needs diagnostic results) |
| M4 | A2 Pilot (A2-U01 *Erlebnisse*) | ⬜ NOT STARTED |
| M5 | A2 Completion | ⬜ NOT STARTED |
| M6 | B1.1 | ⬜ NOT STARTED |
| M7 | B1.2 | ⬜ NOT STARTED |
| M8 | Final Curriculum Audit | ⬜ NOT STARTED |

**Completed milestones:**
- **M0.** Phase 1 blueprint, approved as Baseline v1.0 on 2026-09-11. Its binding content is in `01`.
- **M1.** The `Docs/` system:
  - authoritative decision record
  - design principles
  - milestone system
  - lesson standards
  - validation framework
  - changelog
  - course root `GERMAN_LEARNING_PLAN/`
  - `CLAUDE.md` recovery instructions
  - git repository with `.gitignore` and initial commit

---

## 6. Current work

None in progress. M1 is closed. Waiting for the user's approval to start M2.

## 7. Next planned work

1. The user approves the start of M2 and confirms OD-13 (allocation of the items moved out of M1).
2. **M2:** diagnostic test + routing. Provisionally also `Resources/Rubrics.md`, `Learner_Workbook/Progress_Tracker.md` and a minimal `GERMAN_LEARNING_PLAN/README.md` (OD-13).
3. Validate M2, close, **STOP**.
4. The learner takes the diagnostic; results are recorded here (§9) and in the Progress Tracker.
5. Only then: M3 (A1 Consolidation), after approval.

---

## 8. Approved curriculum version

- **Architecture v1.0**, the Phase 1 blueprint approved on 2026-09-11.
- **Authoritative record:** `01_CURRICULUM_DECISIONS.md`: decisions CD-01 to CD-43 plus Appendices A–J.
- **Lesson standard:** `04_LESSON_STANDARDS.md` v1.0, provisional until the M4 pilot and the B1-U01 review stop.
- The original blueprint text exists only in the session 1 chat and is **not** needed. If a detail is not in `01`, it is not binding.
- Pending change proposals: CP-001 (mediation strand, candidate; decide before M7).
- 2026-09-11: status and timing references in `01` were updated to reflect the approved decisions (OD-05/06/08/09/10). No architectural content changed; the version stays v1.0.

---

## 9. Learner profile

**Stated by the user:**
- Knows German basics at about A1; partially familiar with A2.
- Does **not** want to restart from zero unless the diagnostic shows a missing prerequisite.
- Speaks English well. English interference is expected.
- Recognises words when reading or listening but wants much stronger **active retrieval** and **spontaneous production**.
- Wants to communicate naturally, not just pass grammar tests.
- Prefers structured, logical progression. Wants engaging, non-repetitive learning.
- Wants explanations in English. Comfortable learning from Markdown.
- Target: **end of B1**.

**Approved working assumptions (2026-09-11):**

| Topic | Assumption | Decision |
|---|---|---|
| Study time | **7 hours/week** (initial assumption) | OD-01 |
| Exam | **Exam-compatible, not exam-focused** | OD-02 |
| Topics and comparison language | **General-life topics; English as the comparison language** for now | OD-03 |
| Tools | **Anki, AI role-play (voice) and text-to-speech are available**; a human tutor is optional | OD-04 |

**Working hypothesis (unverified until the M2 diagnostic):**
- Receptive level about A2-, productive about A1+ (recognition–production gap).
- Likely weak spots:
  - dative system
  - adjective endings
  - gender
  - verb-final order under pressure
  - *haben/sein* in Perfekt
  - separable verbs in speech
  - small active vocabulary
  - slow retrieval
  - natural-speed listening

**Diagnostic results:** not yet taken. Required before M3 (OD-12).

---

## 10. Important constraints

- **Format:** Markdown only, following `04_LESSON_STANDARDS.md` (GFM; only `<details>`/`<summary>`/`<br>` as HTML; YAML front matter; ASCII filenames). English explanations; instruction language moves to German in B1 (CD-10).
- **No audio production.** Listening uses TTS and external sources with reusable task sheets (CD-30). No audio or image files in the repository.
- **No built-in human feedback.** Feedback comes from self-recording, AI prompts, and an optional tutor.
- **Copyright:** original texts and tasks only. Never reproduce official exam material or third-party texts. Cite external sources by name.
- **Environment:** Windows 11. Workspace `C:\Users\erhan\Desktop\Deutch`. Git repository initialised 2026-09-11 (branch `main`). Learner audio recordings are git-ignored.
- **Scale:** about 157 course files, built across many sessions in milestones and work packages.
- **Workload target:** about 230 h guided + about 105 h exposure at 7 h/week (CD-40). Lesson files 60–90 minutes each.

---

## 11. Known issues

| ID | Issue | Mitigation | Revisit |
|---|---|---|---|
| KI-01 | No audio can be produced, so listening is the weakest part | TTS-first routine, external sources, reusable task sheets | M4 pilot |
| KI-02 | No live speaking partner, so errors can become fixed habits | Self-recording checklist, AI role-play with delayed correction (`04` A12); recommend a tandem partner or tutor | M3 (`Speaking_Toolkit`) |
| KI-03 | Self-assessment bias | Production-based, timed diagnostic and checkpoints | M2 |
| KI-04 | About 157 files: risk of drift in quality and consistency | Milestones, work packages, pilot, `04` Part C checklist, validation log | Every milestone |
| KI-05 | Naturalness of German examples needs constant vigilance | `04` A10 criteria, register tags, ✅/⚠️/❌ markers | Every milestone, M8 |
| KI-06 | B1.1 is grammar-dense | Lighter units and reviews between; accepted in v1.0 | M6 |
| KI-07 | Adjective endings and gender will keep producing errors through B1 | Communicative accuracy targets (CD-17) | – |
| KI-08 | Motivation over about 12 months | Story Bank, light units, 15-minute minimum day | – |
| KI-09 | External links and content can change | Cite by name; generic task sheets | M3, M8 |
| KI-10 | Mediation only lightly covered | CP-001 candidate | Before M7 |
| KI-11 | Several `04` numeric targets are first estimates: English-cue shares at B1 (≤50% / ≤25%), recycling minimums (5/8 items per lesson, 15/20 per unit), 60% production share | Confirm or adjust in the M4 pilot and the B1-U01 review stop | M4, M6 |
| KI-12 | Items moved out of M1 need a confirmed home | Provisional just-in-time allocation in `03` (OD-13) | M2 start |

---

## 12. Unresolved decisions

| ID | Question | Recommendation / default | Blocks |
|---|---|---|---|
| OD-13 | Allocation of the items moved out of M1 (course README, stage READMEs, `Resources/`, `Learner_Workbook/`) | Just in time, as marked *(OD-13)* in `03`: M2 → `Rubrics.md`, `Progress_Tracker.md`, minimal course README. M3 → `A1/README.md`, A1-needed resources, remaining Workbook files (with proposed M3 work packages). M4 → `A2/README.md`, `Verb_Lists.md`, `A2.tsv`. M6 → `B1/README.md`, `B1.tsv` | Confirm at M2 start |
| OD-11 | CP-001 mediation strand | Decide before M7 | M7 |

**Resolved on 2026-09-11** (user approval; see `06_CHANGELOG.md` [002]):
- **OD-01:** 7 h/week.
- **OD-02:** exam-compatible, not exam-focused.
- **OD-03:** general topics; English as comparison language.
- **OD-04:** Anki, AI role-play and TTS available; tutor optional.
- **OD-05:** course in `Deutch/GERMAN_LEARNING_PLAN/`.
- **OD-06:** `Docs/` authoritative; optional learner-facing `00_Curriculum/`.
- **OD-07:** `Docs/04_LESSON_STANDARDS.md` + `Docs/05_VALIDATION_LOG.md`.
- **OD-08:** pilot unit A2-U01 *Erlebnisse*.
- **OD-09:** work packages in M5–M7 + mandatory review stop after B1-U01.
- **OD-10:** `CLAUDE.md` + git.
- **OD-12:** diagnostic must be completed before M3.

---

## 13. Files that currently exist

```
Deutch/
├── .git/                           ← repository (branch main)
├── .gitignore
├── CLAUDE.md                       ← recovery/workflow pointer for new sessions
├── Docs/
│   ├── 00_PROJECT_STATE.md         ← this file
│   ├── 01_CURRICULUM_DECISIONS.md  ← decisions CD-01–CD-43, Appendices A–J, change control
│   ├── 02_DESIGN_PRINCIPLES.md     ← 19 principles + file-level check
│   ├── 03_MILESTONES.md            ← M0–M8: scope, deliverables, validation, work packages
│   ├── 04_LESSON_STANDARDS.md      ← lesson architecture, file standards, quality checklist, skeletons
│   ├── 05_VALIDATION_LOG.md        ← validation framework + V-001
│   └── 06_CHANGELOG.md             ← project history
└── GERMAN_LEARNING_PLAN/
    └── .gitkeep                    ← course root placeholder (no course content yet)
```

## 14. Planned files (not yet created)

Allocation marked *(OD-13)* is provisional until confirmed.

| Milestone | Files |
|---|---|
| M2 | `GERMAN_LEARNING_PLAN/00_Curriculum/09_Diagnostic_Test.md` · *(OD-13)* `Resources/Rubrics.md`, `Learner_Workbook/Progress_Tracker.md`, `GERMAN_LEARNING_PLAN/README.md` |
| M3 | `A1/A1-U01_Ich_und_du.md` … `A1-U05_In_der_Stadt.md`, `A1/A1_Checkpoint.md` · *(OD-13)* `A1/README.md`; `Resources/` Sentence_Map, Speaking_Toolkit, Writing_Toolkit, Listening_Reading_Sources, Pronunciation_Guide, English_German_Interference, Grammar_Tables, Redemittel, `Anki/A1.tsv`; `Learner_Workbook/` Error_Log, Chunk_Bank, Story_Bank, Writing_Portfolio |
| M4 | `A2/A2-U01_Erlebnisse/` (5 files) · *(OD-13)* `A2/README.md`, `Resources/Verb_Lists.md`, `Resources/Anki/A2.tsv` |
| M5 | `A2/A2-U02` … `A2-U10` (9 × 5 files), `A2-R1/R2/R3_Wiederholung.md`, `A2_Midpoint_Checkpoint.md`, `A2_Exit_Checkpoint.md` |
| M6 | `B1-U01` … `B1-U06` (6 × 5 files), `B1-R1_Wiederholung.md`, `B1_Midpoint_Checkpoint.md` · *(OD-13)* `B1/README.md`, `Resources/Anki/B1.tsv` |
| M7 | `B1-U07` … `B1-U12` (6 × 5 files), `B1-R2/R3_Wiederholung.md`, `B1_Exit_Checkpoint.md` |
| M8 | Audit entry in `05`; decision on optional `00_Curriculum/01`–`08` |

The full tree with exact names is in `01_CURRICULUM_DECISIONS.md`, Appendix H.
