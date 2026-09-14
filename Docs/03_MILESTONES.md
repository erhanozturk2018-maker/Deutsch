# 03 — Milestones

> **Purpose:** Breaks the curriculum build into milestones that can be built, checked and approved separately.
> Workflow: **Design → Build → Validate → Approve → Scale.** Never "design → generate everything".
>
> **Last updated:** 2026-09-11 (M1 closed)

## Overview

| ID | Milestone | Status | Depends on |
|---|---|---|---|
| M0 | Curriculum Architecture | ✅ COMPLETE | – |
| M1 | Project Infrastructure | ✅ COMPLETE (2026-09-11) | M0 |
| M2 | Diagnostic System | ✅ COMPLETE (2026-09-11), V-003 | M1 |
| M3 | A1 Consolidation | ✅ COMPLETE (2026-09-11), V-007 | M2 (diagnostic *built*; results not required, see OD-12) |
| M4 | A2 Pilot (A2-U01 *Erlebnisse*) | ✅ COMPLETE (2026-09-12), V-008 | M3 |
| M5 | A2 Completion | ✅ COMPLETE (2026-09-12), V-009/V-010/V-011 | M4 **validated** |
| M6 | B1.1 | ✅ COMPLETE (2026-09-12), V-012/V-013/V-014/V-015 | M5 |
| M7 | B1.2 | ▶ IN PROGRESS (WP2) | M6 · CP-001 decided 2026-09-14 |
| M8 | Final Audit of the A1–B1 core | ⬜ NOT STARTED | M7 |
| M9 | B2 (12 units) | ▶ IN PROGRESS (WP1) | CP-003 — **vorgezogen auf Wunsch des Nutzers, 2026-09-13** |
| M10 | C1 (10 units) | ⬜ NOT STARTED | M9 |
| M11 | C2 (8 project units) | ⬜ NOT STARTED | M10 |

**Status values:**
- `NOT STARTED`
- `AWAITING APPROVAL`: waiting for the user's go-ahead to start, or for acceptance of a pilot or review stop
- `IN PROGRESS`
- `COMPLETE`: built, validated (logged in `05_VALIDATION_LOG.md`) and closed
- `BLOCKED`: waiting on an open decision

## Rules that apply to every milestone

> **Autonomous mode (user authorisation, 2026-09-11):** milestones M2 → M8 run back to back with no user approval stops. See `CLAUDE.md` and `00` §4 for the stop conditions.

1. **Isolation.** Work on one milestone (and batch) at a time, in order.
2. **Closing a milestone or batch:**
   1. Validate and record the result in `05_VALIDATION_LOG.md`.
   2. Correct defects.
   3. Update `00_PROJECT_STATE.md`.
   4. Update this file.
   5. Update `06_CHANGELOG.md`.
   6. Commit (no AI-attribution lines).
   7. Push if possible.
   8. **Continue** with the next milestone or batch.
3. **Work packages (WP)**, approved 2026-09-11 (OD-09). Large milestones are built in batches. After each WP: validate, update `00_PROJECT_STATE.md`, commit.
4. **Review stops** are marked 🛑. In autonomous mode they are **documented Claude validations** (recorded in `05`, with `04` adjusted if needed). Work does not wait for the user.
5. **Pilot before scaling.** No unit template is copied at scale before it has been validated (CD-41).
6. **No silent architecture changes.** Findings that affect the architecture go through change control (`01`, end of file).
7. **Every course file** must pass the quality checklist in `04_LESSON_STANDARDS.md` (Part C) and the file-level check in `02_DESIGN_PRINCIPLES.md`.
8. **Shared resources are created just in time**, in the milestone that first needs them, and extended by later milestones. The provisional allocation of the items moved out of M1 is marked *(OD-13)*; confirm it before M2 starts.

---

## M0 — Curriculum Architecture

- **Objective:** Design a pedagogically coherent A1→B1 curriculum for this specific learner.
- **Scope:** Teaching philosophy, level interpretation, stages, units, progressions, review, assessment, file structure, risks.
- **Deliverables:** The Phase 1 blueprint (produced in conversation, session 1). Its binding content is captured in `01_CURRICULUM_DECISIONS.md` (decisions + Appendices A–J).
- **Dependencies:** None.
- **Validation criteria:** The internal audit against the user's 17 quality points was done during Phase 1. Revisions from that audit:
  - Konjunktiv II chunks moved earlier.
  - Story Bank added.
  - TTS listening routine added.
  - B1.2 lightened (U08 light, U12 integration only).
  - A1 gate requires fluency, not only accuracy.
  - Cumulative review weighting added.

  Remaining known gap: mediation (CP-001).
- **Completion status:** ✅ **COMPLETE**. Approved by the user on 2026-09-11 as Architecture Baseline v1.0.
- **Next milestone:** M1.

---

## M1 — Project Infrastructure

- **Objective:** Build the lasting structure that every later milestone depends on: project memory, decision record, principles, milestone system, lesson standards, validation framework, course root, recovery instructions, version history. **No course content.**
- **Scope (approved by the user on 2026-09-11):**
  - `Docs/` system
  - course root
  - `CLAUDE.md`
  - git
- **Moved out of M1** (by the user's definition of M1 completion, 2026-09-11). They are reallocated just in time; see the *(OD-13)* marks in M2–M6:
  - `GERMAN_LEARNING_PLAN/README.md`
  - `00_Curriculum/01`–`08` (now optional per OD-06)
  - stage READMEs
  - `Resources/` files
  - `Learner_Workbook/` files
- **Deliverables:**
  1. ✅ `Docs/00_PROJECT_STATE.md`: persistent project memory
  2. ✅ `Docs/01_CURRICULUM_DECISIONS.md`: authoritative decision record + architecture appendices + change control
  3. ✅ `Docs/02_DESIGN_PRINCIPLES.md`: design constitution
  4. ✅ `Docs/03_MILESTONES.md`: milestone system (this file)
  5. ✅ `Docs/04_LESSON_STANDARDS.md`: lesson architecture, file standards, quality checklist, file skeletons
  6. ✅ `Docs/05_VALIDATION_LOG.md`: validation framework + V-001
  7. ✅ `Docs/06_CHANGELOG.md`: project history
  8. ✅ `GERMAN_LEARNING_PLAN/`: course root (holds only `.gitkeep`, so git tracks the empty folder)
  9. ✅ `CLAUDE.md`: concise recovery and workflow instructions
  10. ✅ Git repository + `.gitignore` + initial commit `M1 infrastructure initialized`
- **Dependencies:** M0.
- **Validation criteria:**
  - The expected structure exists.
  - Internal links resolve.
  - No contradictory architecture across Docs.
  - The authoritative source is clearly identified.
  - A new session can recover from the filesystem.
  - The repository is initialised with an initial commit and nothing unnecessary is committed.
  - No lesson, diagnostic or A1/A2/B1 content was created.
- **Validation record:** V-001 in `05_VALIDATION_LOG.md`.
- **Completion status:** ✅ **COMPLETE** (2026-09-11).
- **Next milestone:** M2, not started, awaiting the user's approval to begin.

---

## M2 — Diagnostic System

- **Objective:** Find out where the learner really is, measuring accuracy **and** speed, and route them through the curriculum (CD-03).
- **Scope:** The entry diagnostic and routing system. It must determine:
  - which A1 material can be skipped
  - which A1 material needs consolidation
  - whether the learner is ready for A2
  - major grammar weaknesses
  - vocabulary retrieval weaknesses
  - the speaking and fluency baseline
- **Deliverables:**
  1. `GERMAN_LEARNING_PLAN/00_Curriculum/09_Diagnostic_Test.md`, containing:
     - can-do self-assessment (A1/A2/B1 descriptors)
     - about 40 grammar production items, each tagged with the unit or `§` section it routes to (covering all A1 units and the key A2 topics: Perfekt, dative, two-way prepositions, *weil/dass*, adjective endings, comparison, Konjunktiv II chunks, verbs + prepositions)
     - about 40 vocabulary retrieval items by topic
     - a timed fluency check with thresholds in seconds
     - short reading texts (A1/A2)
     - 3 writing prompts of rising level
     - 6 recorded speaking prompts
     - an optional listening part (TTS)
     - scoring instructions
     - a **routing table**
     - answer key in `<details>`
  2. *(OD-13)* `Resources/Rubrics.md`: the single rubric (CD-36), needed to score the diagnostic's writing and speaking
  3. *(OD-13)* `Learner_Workbook/Progress_Tracker.md`: every Appendix D structure × 4 stages (grammar keys from `04` B4), can-do ticks, checkpoint scores, **diagnostic results section**
  4. *(OD-13)* `GERMAN_LEARNING_PLAN/README.md`: a minimal start page (what the course is, "start with the diagnostic", navigation), extended in later milestones
- **Dependencies:** M1 (standards, validation framework); user go-ahead.
- **Validation criteria:**
  - A coverage matrix shows every A1 unit and every listed A2 topic has at least 2 items.
  - Every item routes to exactly one unit or section.
  - Routing rules are unambiguous (≥85% + fast / 60–84% / <60%).
  - At least 80% of items require production.
  - Total time 2–3 hours, splittable into 2 sittings.
  - The answer key has been checked item by item.
  - Fluency thresholds are defined in seconds.
  - Links resolve; `04` Part C applies where relevant.
- **Usage order (OD-12, superseded as a *build* dependency on 2026-09-11):**
  - The learner takes the diagnostic before *working through* A1.
  - M3 is *built* without results. The A1 units adapt through the diagnostic routing table and each unit's Schnelltest.
  - Claude never takes the diagnostic and never invents results.
- **Built (2026-09-11):**
  - `00_Curriculum/09_Diagnostic_Test.md`: 10 parts in 2 sittings, answer keys, routing into 5 categories (⚪ Skip · 🟢 Brief review · 🟡 Consolidate · 🟠 Intensive · 🔴 Repair) with a speed rule, a repair-order table, and 3 overall routes (Fast track / Standard / Foundations)
  - `Resources/Rubrics.md`
  - `Learner_Workbook/Progress_Tracker.md`
  - `GERMAN_LEARNING_PLAN/README.md`
  - `tools/check_links.py`
- **Completion status:** ✅ COMPLETE (2026-09-11), validation V-003
- **Next milestone:** M3.

---

## M3 — A1 Consolidation ("Fundament")

- **Objective:** Turn existing A1 knowledge into **faster, more reliable production**. This is **not** a beginner course.
- **Scope:** 5 single-file A1 units plus the A1 Gate, following Appendix B of `01` and skeleton D4 of `04`. Emphasis is adjusted according to the diagnostic results.
- **Deliverables:**
  - `A1/A1-U01_Ich_und_du.md`, `A1-U02_Essen_und_Einkaufen.md`, `A1-U03_Mein_Tag.md`, `A1-U04_Koennen_muessen_duerfen.md`, `A1-U05_In_der_Stadt.md`, `A1/A1_Checkpoint.md`
  - *(OD-13)* `A1/README.md`
  - *(OD-13)* Shared resources first needed by A1:
    - `Resources/Sentence_Map.md` (full)
    - `Speaking_Toolkit.md` (full)
    - `Writing_Toolkit.md` (full, including the writing-feedback prompt)
    - `Listening_Reading_Sources.md` (full)
    - `Pronunciation_Guide.md`, `English_German_Interference.md`, `Grammar_Tables.md`, `Redemittel.md` (foundations + A1 content)
    - `Anki/A1.tsv`
  - *(OD-13)* `Learner_Workbook/Error_Log.md`, `Chunk_Bank.md`, `Story_Bank.md` (8 tasks × 3 stages), `Writing_Portfolio.md`
- **A1 section map (fixed in M2; the diagnostic routes to these IDs, so M3 must use them exactly):**

  | Unit | Sections |
  |---|---|
  | A1-U01 | §A present tense (regular, e→i / a→ä, *sein, haben*) · §B verb in position 2 (Sentence Map) · §C questions + follow-ups · §D numbers & personal data |
  | A1-U02 | §A gender & plural (gender clues) · §B nominative & accusative (+ *mich/dich/ihn*…, *es gibt*) · §C *kein/nicht* · §D possessives · §E shopping language (*möchte, hätte gern*, quantities, prices) |
  | A1-U03 | §A time (clock, *um/am/im*, *von … bis*) · §B separable verbs · §C time first: inversion + frequency adverbs |
  | A1-U04 | §A modal verbs: forms and meaning · §B modal verbs in the bracket · §C imperative (+ *mal, bitte*) · §D position of *nicht* |
  | A1-U05 | §A places & directions as chunks (*zum/zur, im, nach/zu Hause, mit dem Bus*; directions) · §B *war/hatte* · §C recognising the Perfekt (bridge to A2-U01) |

  Each section must contain the elements its routing category relies on:
  - a short **refresh explanation** (for 🟢)
  - a **timed retrieval activity** (for 🟢, and the ⚪ fluency check)
  - full practice (for 🟡)
  - an **"Extra" round** (for 🟠 and 🔴)
- **Work packages (proposed with OD-13):**
  - **WP1 ✅ (2026-09-11, V-005):** shared resources + `A1/README.md` + A1-U01. The optional review stop was done as a Claude validation in autonomous mode.
  - **WP2 ✅ (2026-09-11, V-006):** U02, U03
  - **WP3 ✅ (2026-09-11, V-007):** U04, U05, A1 Checkpoint + stage validation
- **Completion status:** ✅ **COMPLETE** (2026-09-11). Stage validation V-007.
- **Dependencies:** M2 (built). Diagnostic *results* are not needed to build M3 (OD-12 superseded); the units adapt through routing.
- **Validation criteria:**
  - Every unit opens with a 10-minute Schnelltest whose results route to labelled `§` sections.
  - Content matches Appendix B.
  - Every unit contains timed retrieval and a fluency task.
  - The full route through any unit takes 5 hours or less.
  - No content assumes zero knowledge.
  - Chunks that will be systematised later are marked with forward links.
  - Checkpoint thresholds match Appendix G (≥75%, speaking ≥2.5/4, fluency).
  - `Sentence_Map.md` uses the CD-05 table format exactly.
  - Links resolve; `04` Part C passed.
- **Completion status:** ⬜ NOT STARTED
- **Next milestone:** M4.

---

## M4 — A2 Pilot

- **Objective:** Build **one** complete A2 unit with the final lesson architecture, to **validate the design before scaling**.
- **Scope:** **A2-U01 *Erlebnisse*** (approved 2026-09-11, OD-08). Perfekt; heavy load; the first A2 unit; links to Story Bank task 3.
- **Deliverables:**
  - `A2/A2-U01_Erlebnisse/`: `00_Overview_und_Wortschatz.md`, `L1_*`, `L2_*`, `L3_*`, `L4_Anwenden.md`
  - *(OD-13)* `A2/README.md`, `Resources/Verb_Lists.md`, `Resources/Anki/A2.tsv`
  - A2 additions to the other resources
  - A pilot evaluation entry in `05_VALIDATION_LOG.md`
- **The pilot must test:**
  - grammar explanation (10-point standard)
  - vocabulary density (~45 ★ + ~40 recognition)
  - retrieval practice
  - speaking tasks
  - reading/listening (TTS routine)
  - writing
  - review (3-2-1 warm-ups reaching back into A1)
  - lesson length
  - Markdown organisation
- **Dependencies:** M3.
- **Validation criteria:**
  - Every lesson has an estimated time of 60–90 minutes. Ideally a **learner trial** of at least L1 and L4 reports real time and difficulty.
  - At least 60% production items.
  - At least 6 activity types across the unit.
  - Every `04` A3 component present, or deliberately left out with a reason.
  - The main task matches Appendix B.
  - `04` Part C passed.
  - **Explicit user approval of the template** 🛑
- **Result (2026-09-12):** Pilot validated (V-008). Findings applied as `04` v1.1: explanation subheadings; ★ = practised, checked with `tools/check_vocab.py`; recognition guideline; D2/D3 clarifications. **Completion status: ✅ COMPLETE.**
- **Exit rule:** If the pilot reveals problems:
  1. Revise `04_LESSON_STANDARDS.md` (v1.x, logged) or propose an architecture change (change control).
  2. Re-validate.
  3. Only then start M5.
- **Completion status:** ⬜ NOT STARTED
- **Next milestone:** M5.

---

## M5 — A2 Completion

- **Objective:** Build the rest of A2 using the approved pilot template.
- **Scope:**
  - A2-U02 to U10
  - A2-R1, R2, R3
  - A2 Midpoint and A2 Exit
  - A2 flashcards complete
  - A2 resource content
  - Story Bank A2 stage
  - Pilot feedback applied to A2-U01 if needed
- **Work packages (approved, OD-09):**
  - **WP1 ✅ (2026-09-12, V-009):** U02, U03, R1
  - **WP2 ✅ (2026-09-12, V-010):** U04, U05, U06, R2, Midpoint
  - **WP3 ✅ (2026-09-12, V-011):** U07, U08, U09, U10, R3, A2 Exit
- **Dependencies:** M4 **approved**.
- **Validation criteria:**
  - Unit map fidelity (Appendix B).
  - Recycling check: every unit's tasks require at least 3 structures from earlier units (Appendix D) and meet `04` A8.
  - Vocabulary counts within Appendix E.
  - At least 6 activity types per unit, and no identical main-task type in consecutive units.
  - U09 light.
  - Reviews weighted 50/30/20 and reaching into A1.
  - The Exit implements Appendix G, including an integrated scenario.
  - Links resolve; `04` Part C passed.
- **Completion status:** ✅ COMPLETE (2026-09-12, V-009 WP1 · V-010 WP2 · V-011 WP3)
- **Next milestone:** M6.

---

## M6 — B1.1

- **Objective:** Build B1.1 (*Erzählen & Beschreiben*).
- **Scope:**
  - B1-U01 to U06
  - B1-R1
  - B1 Midpoint
  - *(OD-13)* `B1/README.md` and `Resources/Anki/B1.tsv`
  - B1 resource content
- **Work packages (approved, OD-09):**
  - **WP1:** B1-U01 only → 🛑 **mandatory review stop**. B1 introduces German task instructions (CD-10) and longer texts, so the B1 variant of the template gets a second validation pass. Findings may revise `04` (v1.x) before WP2.
  - **WP2:** U02, U03, R1
  - **WP3:** U04, U05, U06, Midpoint
- **Dependencies:** M5.
- **Validation criteria:**
  - As in M5, plus: instruction language follows CD-10 and `04` A7.
  - Reading texts reach B1 length and complexity.
  - Relative clauses are used for talking-around-words tasks from U02 on.
  - The Midpoint includes a review.
- **Completion status:** ✅ **COMPLETE (2026-09-12)** — WP1 (B1 README, U01, review stop → `04` v1.2/A7.1, U02, U03; V-012/V-013), WP2 (B1-R1, U04, U05; V-014), WP3 (U06, B1 Midpoint; V-015). All four tools pass: 113 files / 0 problems, 1611 links / 0 broken, `B1.tsv` 339 cards.
- **Next milestone:** M7.

---

## M7 — B1.2

- **Objective:** Build B1.2 (*Argumentieren & Handeln*) and the final assessment.
- **Scope:** B1-U07 to U12, B1-R2, R3, B1 Exit, B1 flashcards complete, final resources, Story Bank B1 stage.
- **Work packages (approved, OD-09):**
  - **WP1:** U07, U08, U09, R2
  - **WP2:** U10, U11, U12, R3, Exit
- **Dependencies:** M6. **CP-001 (mediation, OD-11) — decided 2026-09-14** in a scoped form (recognised task type, not a new lesson component; one mediation task each in B1-U10, U11, U12 and the B1 Exit). See `01`, change proposal register and the section „Mediation (CP-001, scoped)“. Exam-compatible, not exam-focused (OD-02).
- **Validation criteria:**
  - As in M5/M6, plus: task instructions fully in German.
  - U08 light; U12 has no new grammar.
  - The Exit includes integrated scenarios and a pointer to the official Goethe *Modellsatz*.
  - Every B1 can-do target (Appendix A) is assessed.
- **Completion status:** ▶ IN PROGRESS (WP2). **WP1 ✅ abgeschlossen** (2026-09-13/14): B1-U07 (V-032), B1-U08 (V-033), B1-U09 (V-034), B1-R2 (V-035). WP2 offen: U10–U12, B1-R3, B1 Exit. Begonnen nach dem Abschluss von M9, gemäß der Reihenfolge oben.
- **Next milestone:** M8.

---

## M8 — Final Curriculum Audit

- **Objective:** Audit the complete A1→B1 curriculum and fix what is found.
- **Scope:** All course files and `Docs/`. Audit points:
  - consistency
  - grammar dependencies
  - vocabulary recycling
  - CEFR progression
  - speaking progression
  - difficulty progression
  - duplicate content
  - missing prerequisites
  - broken Markdown links
  - unrealistic workload
  - activity variety
  - quality of examples
  - assessment coverage
- **Deliverables:**
  - An audit entry in `05_VALIDATION_LOG.md` (plus a separate report file only if the audit is too large for the log)
  - Local fixes applied
  - Architecture-level findings raised via change control
  - Decision on the optional `00_Curriculum/01`–`08` learner-facing files (OD-06)
  - Final state update
- **Dependencies:** M7.
- **Validation criteria:**
  - Every audit point has a documented result.
  - Zero unresolved links.
  - Every Appendix D structure reaches a "spontaneous use demanded" location.
  - Every unit's vocabulary is recycled at least once later.
  - Total workload is consistent with Appendix J, or the deviation is documented.
- **Completion status:** ⬜ NOT STARTED
- **Next milestone:** M9 (CP-003).

---

> ### Reihenfolge der verbleibenden Milestones (Nutzerentscheidung, 2026-09-13)
>
> Auf ausdrücklichen Wunsch des Nutzers gilt ab jetzt diese Reihenfolge:
>
> | Rang | Milestone | Inhalt |
> |---|---|---|
> | 1 | **M9** | B2 vollständig (U01–U12, R1–R3, Midpoint, Exit) |
> | 2 | **M7** | B1.2 fertigstellen (B1-U07–U12, B1-R2, B1-R3, B1 Exit) |
> | 3 | **M8** | Audit des A1–B1-Kerns (`check_links --strict`) |
> | 4 | **M10** | C1 |
> | 5 | **M11** | C2 |
>
> Begründung des Nutzers: B2 zuerst zu Ende bringen, dann die Lücke in B1 schließen, danach die oberen Stufen. Die Sequenzabweichung gegenüber der ursprünglichen Planung (M7 vor M9) ist damit bestätigt und nicht mehr provisorisch.

## M9 — B2

- **Objective:** Build the B2 stage (*Arguing Precisely, Understanding Everything*).
- **Scope:**
  - B2-U01 to U12 in the five-file form (`00_Overview_und_Wortschatz`, `L1`–`L3`, `L4_Anwenden`)
  - B2-R1, B2-R2, B2-R3; B2 Midpoint Checkpoint; B2 Exit Checkpoint
  - `Resources/Anki/B2.tsv`; B2 sections in Grammar_Tables, Verb_Lists, Redemittel, Pronunciation_Guide, English_German_Interference
  - **Consolidation of `B2/B2_Recap/`**: each unit's vocabulary, phrases and grammar folded into the three sheets in the same batch; `status:` moves `planned → in-progress → validated`
- **Work packages:** **WP1 = U01 ✅** (2026-09-13, V-018) + Review-Stop → `04` v1.3 / Regel A7.2 · **WP2 = U02–U04 + R1 ✅** (2026-09-13, V-019 bis V-021) · **WP3 = U05–U08 + R2 + Midpoint ✅** (2026-09-13, V-022 bis V-026) · **WP4 = U09–U12 + R3 + Exit ✅** (2026-09-13, V-027 bis V-031)
- **Dependencies:** CP-003 (approved 2026-09-13). **Sequenzabweichung:** M9 wurde auf ausdrücklichen Wunsch des Nutzers **vor** M7 (B1.2) und M8 begonnen. M7 und M8 bleiben offen und unverändert im Plan.
- **Validation criteria:**
  - Instruction language **fully German** at B2 level (extends `04` A7.1).
  - Reading texts 500–900 words with a recognisable stance; listening 400–600 words.
  - Every structure in the B2 recap grammar sheet is taught in a unit and demanded spontaneously at least once.
  - Speaking targets 4–5-minute turns; Story Bank recorded at B2.
  - Register (⬇ / neutral / ⬆) is taught explicitly and tested.
- **Completion status:** ✅ **COMPLETE** (2026-09-13, V-031). B2 umfasst zwölf Einheiten, drei Wiederholungen, das Midpoint und das Exit Checkpoint; der B2-Recap ist aus dem Kurs konsolidiert.
- **Next milestone:** **M7 (B1.2)** gemäß der Reihenfolge oben; danach M8, M10, M11.

---

## M10 — C1

- **Objective:** Build the C1 stage (*Effective Operational Command*).
- **Scope:** C1-U01 to U10 (larger units), C1-R1, C1-R2, C1 Midpoint, C1 Exit, `Resources/Anki/C1.tsv`, C1 resource sections, and consolidation of `C1/C1_Recap/`.
- **Work packages:** WP1 = U01 + review stop · WP2 = U02–U05 + R1 + Midpoint · WP3 = U06–U10 + R2 + Exit
- **Dependencies:** M9.
- **Validation criteria:**
  - Texts 1 000–2 000 words, including one literary and one academic genre per review cycle.
  - Writing tasks are **named genres** (Abstract, Bericht, Rezension, Stellungnahme, Protokoll), each with a model and a rubric.
  - Mediation appears in at least three units (settles CP-001 for the upper stages).
  - Every unit demands one register switch and one piece of implicit-meaning work.
- **Completion status:** ⬜ NOT STARTED
- **Next milestone:** M11.

---

## M11 — C2

- **Objective:** Build the C2 stage (*Mastery*) as **projects and feedback loops**, not as content delivery.
- **Scope:** C2-U01 to U08, C2-R1, the C2 Final Assessment (portfolio + oral defence), `Resources/Anki/C2.tsv` (nuance pairs rather than words), C2 resource sections, and consolidation of `C2/C2_Recap/`.
- **Work packages:** WP1 = U01 + U02 + review stop · WP2 = U03–U05 · WP3 = U06–U08 + R1 + Final
- **Dependencies:** M10.
- **Validation criteria:**
  - Each unit is a **project with an audience**, not a lesson sequence.
  - Every unit contains an editing task on someone else's German and a mediation task.
  - Assessment is a portfolio with an oral defence; no gap-fill test at this level.
  - The stage page's honesty clause (a course prepares C2, it does not produce it) is preserved.
- **Completion status:** ⬜ NOT STARTED
- **Next milestone:** None. The project is then complete; maintenance follows based on learner feedback.

