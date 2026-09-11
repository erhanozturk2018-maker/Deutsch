# 00 — Project State

> **Read this file first** (after `CLAUDE.md`). It is the persistent memory of the project. A new session must be able to continue the work from `Docs/` alone, without any chat history.
>
> **Last updated:** 2026-09-11. Session 4: M3 WP2 complete; WP3 in progress. **Update at every milestone or batch boundary.**

---

## 1. Status

```text
Project:            German A1 → B1 Curriculum
Architecture:       Approved — Baseline v1.0 (2026-09-11)
Mode:               AUTONOMOUS M2 → M8 (user authorisation 2026-09-11)
Current Phase:      Curriculum Construction
Current Milestone:  M3 — A1 Consolidation
Status:             IN PROGRESS
Current batch:      M3 WP3 — A1-U04, A1-U05, A1 Checkpoint + A1 stage validation
Next task:          A1-U04 ✅ written (structure check passed, not yet stage-validated). NEXT: write GERMAN_LEARNING_PLAN/A1/A1-U05_In_der_Stadt.md, then A1_Checkpoint.md, then the M3 stage validation
Last completed:     M2 — Diagnostic System (2026-09-11, V-003)
Push status:        OK — remote history corrected 2026-09-11 (see §15)
```

---

## 2. How to resume (new session)

1. Read `CLAUDE.md`, then this file, then the relevant parts of:
   - [02_DESIGN_PRINCIPLES.md](02_DESIGN_PRINCIPLES.md)
   - [01_CURRICULUM_DECISIONS.md](01_CURRICULUM_DECISIONS.md)
   - [03_MILESTONES.md](03_MILESTONES.md)
   - [04_LESSON_STANDARDS.md](04_LESSON_STANDARDS.md)
   - [05_VALIDATION_LOG.md](05_VALIDATION_LOG.md)
   - [06_CHANGELOG.md](06_CHANGELOG.md)
2. Find the current milestone, batch and **next task** in §1 and §6.
3. Never rebuild what is marked COMPLETE. Resume at the recorded next task.
4. Architecture changes go through change control (end of `01`). Never change it silently.

---

## 3. What this project is

A complete, CEFR-aligned German course from the learner's current level (A1 known, A2 partial) to the **end of B1**. It is written as Markdown in `C:\Users\erhan\Desktop\Deutch\GERMAN_LEARNING_PLAN\`.

The goal is **functional B1 communication**, not grammar coverage. The course prioritises production, active retrieval, spontaneous speaking and spiral recycling.

It is designed by Claude acting as German teacher and curriculum designer, and built incrementally in milestones M0–M8. Git repository with remote `origin` (`https://github.com/erhanozturk2018-maker/Deutsch`, branch `main`).

---

## 4. Workflow rules (binding)

- **Autonomous mode** (user authorisation, 2026-09-11). For each milestone or batch:
  1. Design
  2. Build
  3. Validate
  4. Correct
  5. Record (00, 03, 05, 06)
  6. Commit
  7. Push
  8. **Continue** with the next milestone, with no approval stop

  Stop only if:
  - a genuine architectural contradiction makes continuing unsafe
  - a required resource is unavailable and cannot be substituted
  - the filesystem becomes inaccessible
  - a decision would fundamentally change the approved architecture

  For non-blocking uncertainties: make the most defensible choice, record it, continue.
- **Pilot before scaling** still applies. The M4 pilot (A2-U01) and the B1-U01 special review are validated by Claude (a real, documented validation), and `04` is adjusted if needed. The user no longer needs to approve them before scaling.
- **Never skip validation.** Record only validations that actually happened. **Never invent learner results.**
- **No silent architectural changes.** Problem → reason → proposal → register entry (`01`) → decision → changelog. Decisions that would *fundamentally* change the architecture require stopping and asking the user.
- **Git:**
  - Meaningful commits at milestone and batch boundaries.
  - **No `Co-Authored-By` or other AI-attribution lines, ever.**
  - No force-push unless the user asks.
  - No temporary scripts or junk in the repository.
- **Context limits:** save state (00, 03, 06), commit, record the exact next task, then stop. The next session resumes.

---

## 5. Milestones

| ID | Milestone | Status |
|---|---|---|
| M0 | Curriculum Architecture | ✅ COMPLETE (2026-09-11) |
| M1 | Project Infrastructure | ✅ COMPLETE (2026-09-11), V-001 |
| M2 | Diagnostic System | ✅ COMPLETE (2026-09-11), V-003 |
| M3 | A1 Consolidation | 🔄 IN PROGRESS (WP1 ✅, WP2 ✅, WP3 in progress) |
| M4 | A2 Pilot (A2-U01 *Erlebnisse*) | ⬜ NOT STARTED |
| M5 | A2 Completion | ⬜ NOT STARTED |
| M6 | B1.1 | ⬜ NOT STARTED |
| M7 | B1.2 | ⬜ NOT STARTED |
| M8 | Final Curriculum Audit | ⬜ NOT STARTED |

---

## 6. Current work — M3 A1 Consolidation

**Section map:** fixed in `03` (M3). The diagnostic routes to these exact IDs.

**WP1 ✅ (2026-09-11, V-005):** 8 Resources files + `Anki/A1.tsv`, 4 Workbook files, `A1/README.md`, `A1-U01`, `tools/build_anki.py`.

**WP2 ✅ (2026-09-11, V-006):** `A1-U02`, `A1-U03`, `tools/check_structure.py`.

**WP3** (in progress):
1. `A1/A1-U04_Koennen_muessen_duerfen.md`: §A modal forms and meaning · §B modals in the bracket (+ modal + separable verb) · §C imperative (+ *mal, bitte*) · §D position of *nicht*
2. `A1/A1-U05_In_der_Stadt.md`: §A places & directions as chunks · §B *war/hatte* · §C recognising the Perfekt (bridge to A2-U01)
3. `A1/A1_Checkpoint.md`: 4 skills + fluency + Story Bank A1 recordings (all 8 tasks); thresholds ≥75%, speaking ≥2.5, fluency Developing+; remediation map to A1 sections
4. Update the course `README.md` status table (A1 ✅)
5. Run `tools/check_structure.py`, `tools/build_anki.py`, `tools/check_links.py`
6. **A1 stage validation** (M3 closing validation), record, commit, push → M4

**Pattern to follow:** `A1-U01` (skeleton D4 in `04`):
- YAML
- header
- 🎯
- ⚡ Schnelltest: 3 items per section, keys in `<details>`
- route table
- per section: Refresh / 💬 / practice / ⏱️ timed / ➕ Extra
- "For everyone": fluency + role-play with an AI prompt block + optional writing + a Story Bank link
- 👄, ⚠️ table with codes, 📚 Wortschatz, 🔗, ✅, 🃏 (`| You see (prompt) | You say (Deutsch) |`), footer navigation

**WP3:** A1-U04, A1-U05, `A1/A1_Checkpoint.md` + stage validation

## 7. Next planned work

After M3:
- **M4:** A2 pilot, A2-U01 *Erlebnisse*, with a real pilot validation
- **M5:** A2 completion in 3 batches
- **M6:** B1.1, with a special review after B1-U01
- **M7:** B1.2, after deciding OD-11 (mediation)
- **M8:** final audit

## 8. Approved curriculum version

- **Architecture v1.0.** Authoritative record: `01_CURRICULUM_DECISIONS.md` (CD-01–CD-43, Appendices A–J).
- **Lesson standard:** `04_LESSON_STANDARDS.md` v1.0, provisional until the M4 pilot and the B1-U01 review.
- **Pending change proposal:** CP-001 (mediation), to be decided by Claude before M7 is finalised (OD-11).

---

## 9. Learner profile

**Stated by the user:**
- Knows German basics at about A1; partially familiar with A2.
- Does **not** want to restart from zero.
- Speaks English well.
- Main difficulty: **German is recognisable when reading or listening, but retrieval during spontaneous speaking is weak.**
- Wants natural communication, structured progression, engaging variety, English explanations, Markdown.
- Target: end of B1.

**Working assumptions:**
- 7 h/week
- exam-compatible, not exam-focused
- general-life topics; English as comparison language
- Anki, AI role-play (voice) and TTS available; tutor optional

**Working hypothesis (unverified):** receptive about A2-, productive about A1+ (recognition–production gap).

**Diagnostic results:** not taken yet. The learner takes the diagnostic before *working through* A1 (course usage order). Results are never invented by Claude.

---

## 10. Important constraints

- Markdown per `04_LESSON_STANDARDS.md`; English explanations; German task instructions from B1 (CD-10).
- No audio or image files. Listening uses TTS-ready scripts (CD-30). External resources are optional extras; no lesson may depend on them.
- Original texts only; no reproduction of exam or third-party material.
- Windows 11; workspace `C:\Users\erhan\Desktop\Deutch`.
- About 157 course files, built in milestones and batches.

---

## 11. Known issues

| ID | Issue | Mitigation | Revisit |
|---|---|---|---|
| KI-01 | No audio production | TTS-ready scripts + TTS instructions | M4 |
| KI-02 | No live speaking partner | Self-recording checklist, AI role-play prompts | M3 |
| KI-03 | Self-assessment bias | Production-based, timed diagnostic; recognition vs production compared | M2 |
| KI-04 | About 157 files: drift risk | Batches, pilot, `04` Part C, validation log | Every milestone |
| KI-05 | Naturalness of examples | `04` A10 | Every milestone, M8 |
| KI-06 | B1.1 grammar density | Load rhythm | M6 |
| KI-07 | Adjective endings and gender errors persist | CD-17 targets | – |
| KI-08 | Motivation over about 12 months | Story Bank, light units | – |
| KI-09 | External content can change | Not required anywhere | – |
| KI-10 | Mediation gap | OD-11 | Before M7 |
| KI-11 | `04` numeric targets are estimates | Pilot + B1-U01 review | M4, M6 |
| KI-13 | Listening transcripts are visible when copied into TTS | "Copy without reading" instructions; AI read-aloud option | M4 |
| KI-14 | ~~GitHub still held the old commits with AI-attribution trailers~~ **Resolved 2026-09-11** (force push with the user's explicit permission) | – | – |

---

## 12. Decisions

**Open:**
- **OD-11:** CP-001 mediation. Claude decides before M7 is finalised, records the reasoning.

**Resolved 2026-09-11** (details in `06` [002] and [003]):
- OD-01 to OD-10 as recorded in `06` [002].
- **OD-12 (superseded by the user's autonomy authorisation):** M3 is *built* without waiting for diagnostic results. The A1 units adapt to the learner through the diagnostic routing system and the per-unit Schnelltest. The learner still takes the diagnostic before *starting* A1.
- **OD-13 (confirmed by the user's M2/M3 instructions):** just-in-time allocation.
  - M2: Rubrics, Progress Tracker, course README.
  - M3: A1 README, A1 resources, remaining Workbook files.
  - M4: A2 README, Verb_Lists, `A2.tsv`.
  - M6: B1 README, `B1.tsv`.
- **Tools decision (Claude, 2026-09-11):** `tools/check_links.py` and later `tools/build_anki.py` are committed as small maintained helper scripts. They make validation and Anki export reproducible for future sessions. They are maintained tools, not temporary scripts.

---

## 13. Files that currently exist

```
Deutch/
├── .gitignore  CLAUDE.md
├── Docs/  00–06
├── tools/  check_links.py  build_anki.py  check_structure.py
└── GERMAN_LEARNING_PLAN/
    ├── README.md
    ├── 00_Curriculum/09_Diagnostic_Test.md
    ├── A1/  README.md  A1-U01_Ich_und_du.md  A1-U02_Essen_und_Einkaufen.md  A1-U03_Mein_Tag.md
    ├── Resources/  Rubrics.md  Sentence_Map.md  Grammar_Tables.md  English_German_Interference.md
    │               Pronunciation_Guide.md  Redemittel.md  Speaking_Toolkit.md  Writing_Toolkit.md
    │               Listening_Reading_Sources.md  Anki/A1.tsv
    └── Learner_Workbook/  Progress_Tracker.md  Story_Bank.md  Error_Log.md  Chunk_Bank.md  Writing_Portfolio.md
```

## 14. Planned files

See `03_MILESTONES.md` (deliverables per milestone) and `01` Appendix H (full tree).

---

## 15. Git and push status

- **2026-09-11:** At the user's request, the `Co-Authored-By` trailers were removed from the first two commits by rewriting history locally.

  | Old hash | New hash | Commit |
  |---|---|---|
  | `024a999` | `96621af` | M1 infrastructure initialized |
  | `702a566` | `0d9ee6c` | Record M1 validation results |
- The first force-push attempt was blocked by the permission system. After the user's explicit permission in chat, it was repeated: `git push --force-with-lease=main:702a566… origin main` → `+ 702a566...6265ff2 main -> main (forced update)`.
- **Verified:** `origin/main` equals local `main`, and 0 trailers remain in the remote history. GitHub's "Contributors" sidebar may show the old entry until GitHub refreshes its cache.
- **From now on:** normal fast-forward pushes after every milestone or batch commit. No force-push unless the user asks.
