# 00 — Project State

> **Read this file first** (after `CLAUDE.md`). It is the persistent memory of the project. A new session must be able to continue the work from `Docs/` alone, without any chat history.
>
> **Last updated:** 2026-09-12. Session 6: M6 (B1.1) complete (V-015). **Update at every milestone or batch boundary.**

---

## 1. Status

```text
Project:            German A1 → C2 Curriculum (A1–B1 im Bau; B2/C1/C2 angelegt, CP-003)
Architecture:       Approved — v2.0 (2026-09-13: CP-003, scope extended to A1 → C2)
Lesson standard:    04_LESSON_STANDARDS v1.3 (A1/A2 pilot-validated; B1 A7.1 aus V-012; B2+ A7.2 einsprachig Deutsch, V-018)
Mode:               AUTONOMOUS M2 → M8 (user authorisation 2026-09-11); M9–M11 added by CP-003
Current Phase:      Curriculum Construction
Current Milestone:  M6 — B1.1 ✅ COMPLETE (2026-09-12, V-015)
Status:             BETWEEN MILESTONES
Current batch:      M9 WP2 (B2-U02 fertig, V-019). Sequenz auf Nutzerwunsch: B2 vor M7/M8.
Next task:          M9 WP2 weiter: **B2-U03 Bildung & Lernen** (Konjunktiv I und indirekte Rede; Hauptaufgabe: einen Artikel referieren + Bildungsdebatte), danach **B2-U04 Medien & Öffentlichkeit** (Passiversatzformen) und **B2-R1** (Wiederholung U01–U04). Offen und unverändert: M7 (B1.2), M8 (Audit A1-B1), M10 (C1), M11 (C2). Jede Einheit: 5 Dateien, Resources ergänzen, check_vocab/structure/links/anki, Validierung, Commit
Last completed:     M9 WP2 Teil 1 — B2-U02 Arbeitswelt & Karriere (2026-09-13, V-019)
Push status:        MANUAL - the user pushes (instruction 2026-09-12). Claude commits only.
                    Last commit pushed by the user: 9b40326 (Recap-System, 2026-09-13 geprueft)
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
| M3 | A1 Consolidation | ✅ COMPLETE (2026-09-11), V-005 / V-006 / V-007 |
| M4 | A2 Pilot (A2-U01 *Erlebnisse*) | ✅ COMPLETE (2026-09-12), V-008 |
| M5 | A2 Completion | 🔄 IN PROGRESS (WP1 ✅, WP2 in progress) |
| M6 | B1.1 | ⬜ NOT STARTED |
| M7 | B1.2 | ⬜ NOT STARTED |
| M8 | Final Curriculum Audit | ⬜ NOT STARTED |

---

## 6. Last completed milestone — M6 B1.1 ✅

**Model to follow:** the validated A2 units under `04` v1.1, with the B1 changes below. **A2 is complete and must not be rebuilt.**

**What changes at B1** (from `01` CD-10, CD-18, CD-23, Appendix B, and `04` A7):
- **More German in the instructions.** Task lines, success criteria and activity titles move step by step into German; explanations stay in English. The exact rule is reviewed after B1-U01 (see below).
- **Longer texts:** reading 200–400 words, with real structure (article, report, interview, forum thread).
- **Relative clauses** from B1-U02 on are used for "talk around the word you don't know" tasks.
- Speaking targets S3–S4: 2-minute turns, 4/3/2 retellings, opinion with counter-argument.

**Per-unit checklist** (unchanged from A2, plus the B1 points):
- 5 files: `00_Overview_und_Wortschatz` (plain `## Wortschatz`, "Recycled from" ≥15 items from ≥3 earlier units incl. A1) · `L1`–`L3` (~80–90 min, 7–8 numbered activities) · `L4_Anwenden` (main task from Appendix B, timed retell, 📖, 🎧, 📝, mixed review, 10-item quiz with redo map, workbook update)
- Reading in ≥2 and listening in ≥2 of L1–L4; writing in ≥2 (L4 always)
- Run `tools/check_structure.py`, `tools/check_vocab.py <unit>`, `tools/build_anki.py`, `tools/check_links.py`
- Add each unit's B1 content to Resources; create `Resources/Anki/B1.tsv` with the first B1 unit

**WP1:** `B1/README.md` ✅ · **B1-U01 Lebenswege** ✅ (V-012) · **review stop ✅** → `04` **v1.2**, rule **A7.1** fixes the instruction language for B1.1 and B1.2. Remaining in WP1: **B1-U02 Menschen beschreiben** (relative clauses nom/acc/dat and with prepositions; adjective endings stage 2; n-declension; *sich* = each other; main tasks: "Wer ist das?" and Taboo-style describing; Story Bank Task 8 at B1) and **B1-U03 Arbeit & Beruf** (*zu* + infinitive; *um … zu* vs *damit*; *da-* word + clause; job-interview simulation and application email).

**WP2 ✅ COMPLETE (V-014):** **B1-R1** (cumulative review: B1-U01 to U03 at 50 %, A2.2 at 30 %, older A2/A1 at 20 %; three sittings; error clinic; four role-plays) · **B1-U04 Gesundheit & Wohlbefinden** (Konjunktiv II in full: unreal *wenn*-clauses, wishes, polite forms; "What would you do?" scenarios and an advice-column reply) · **B1-U05 Reisen & Kulturen** (genitive + *wegen, trotz, während, statt*; paired connectors *entweder…oder, weder…noch, sowohl…als auch, nicht nur…sondern auch*; formal complaint email and culture-comparison talk)

**WP3 ✅ COMPLETE (V-015):** **B1-U06 Medien & Nachrichten** (Passiv: Präsens, Präteritum, mit Modalverben; *man* as the active alternative; news and social media; main tasks: describing a process and a pros/cons discussion; Story Bank Task 7 at B1) · **B1 Midpoint Checkpoint** (four skills + integrated scenario, diagnostic only, redirects to weak units), then the M6 closing validation

**Story Bank at B1:** all eight tasks are recorded again at B1 level across M6/M7; the B1 Exit requires the full set.

## 7. Next planned work

- **M7:** B1.2 (B1-U07 to U12, B1-R2, B1-R3, B1 Exit). Decide OD-11 (mediation) before it is finalised.
- **M8:** audit of the **A1–B1 core** (including `check_links --strict`), report, state "A1 → B1 COMPLETE"
- **M9 (B2), M10 (C1), M11 (C2)** — defined in `03` by CP-003. Stage pages and recaps already exist; the units do not.
- **Recaps (standing task, CP-002):** every new B1 unit is added to `B1/B1_Recap/01_Wortschatz.md`, `02_Redemittel.md` and `03_Grammatik.md` in the same batch, and the „Was noch fehlt“ table in `00_Overview.md` is updated. When B1.2 is complete, `status:` changes from `in-progress` to `validated`.

## 8. Approved curriculum version

- **Architecture v1.0.** Authoritative record: `01_CURRICULUM_DECISIONS.md` (CD-01–CD-43, Appendices A–J).
- **Lesson standard:** `04_LESSON_STANDARDS.md` **v1.1**, validated for A1/A2 by the M4 pilot. The B1 variant is checked at the B1-U01 special review.
- **Pending change proposal:** CP-001 (mediation), to be decided by Claude before M7 is finalised (OD-11).
- **Applied change proposal:** CP-002 (per-level recap folders), approved by the user on 2026-09-12 → architecture v1.1.
- **Applied change proposal:** CP-003 (scope A1 → C2, stages B2/C1/C2 with milestones M9–M11), approved by the user on 2026-09-13 → architecture **v2.0**.

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

- **Git: commit only, never push (user instruction, 2026-09-12).** Claude commits at every batch boundary with a clean message (no AI-attribution lines, no `Co-Authored-By`); the user pushes to GitHub manually. Reason: the user wants full control over what reaches the public repository and over who appears as a contributor there.

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

**Decided in autonomous mode (Claude, 2026-09-12) — Story Bank allocation for the rest of A2:**
- U01 → Task 3 · U02 → Task 8 · U03 → Task 4 · U04 → Task 7 · U05 → Task 5 (all recorded at A2 level).
- **U06 → no Story Bank task** (a 4/3/2 retelling on "my style" instead): U06's theme fits none of the remaining tasks, and repeating a task this soon adds nothing.
- **U07 → Task 4 re-recorded with comparisons · U08 → Task 2 · U09 → Task 6 · U10 → Task 1.** The A2 Exit records all eight.
- Reason: the eight tasks must all exist at A2 level by the Exit (Appendix G), and each remaining task fits one unit's theme.

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
├── tools/  check_links.py  check_structure.py  check_vocab.py  build_anki.py
└── GERMAN_LEARNING_PLAN/
    ├── README.md
    ├── 00_Curriculum/09_Diagnostic_Test.md
    ├── A1/  README + U01–U05 + A1_Checkpoint.md
    ├── A2/  README.md  U01–U10 (each a folder: 00_Overview_und_Wortschatz + L1–L4)
    │         A2-R1_Wiederholung.md  A2-R2_Wiederholung.md  A2-R3_Wiederholung.md
    │         A2_Midpoint_Checkpoint.md  A2_Exit_Checkpoint.md            ← A2 COMPLETE
    ├── Resources/  Rubrics  Sentence_Map  Grammar_Tables  Verb_Lists  English_German_Interference  Pronunciation_Guide
    │               Redemittel  Speaking_Toolkit  Writing_Toolkit  Listening_Reading_Sources  Anki/A1.tsv  Anki/A2.tsv
    └── Learner_Workbook/  Progress_Tracker  Story_Bank  Error_Log  Chunk_Bank  Writing_Portfolio
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
