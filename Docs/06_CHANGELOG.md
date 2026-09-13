# 06 — Changelog

> Chronological project history (oldest first). Append new entries at the bottom.
> Record every significant change: milestone completions, approved architecture changes, template revisions, significant local changes.

## Entry format

```text
## [NNN] YYYY-MM-DD — <short title>
- Milestone:
- Affected files:
- Change:
- Reason:
- Impact:
```

---

## [001] 2026-09-11 — Architecture completed; milestone-based build and persistent memory introduced

- **Milestone:** M0 (completed) → M1 (started)
- **Affected files (created):**
  - `Docs/00_PROJECT_STATE.md`
  - `Docs/01_CURRICULUM_DECISIONS.md`
  - `Docs/02_DESIGN_PRINCIPLES.md`
  - `Docs/03_MILESTONES.md`
  - `Docs/06_CHANGELOG.md`
- **Change:**
  1. **Phase 1 architecture completed.** In session 1, Claude produced the full curriculum blueprint:
     - teaching philosophy and level interpretation
     - 5 A1 consolidation units, 10 A2 units, 12 B1 units, with reviews and checkpoints
     - grammar, vocabulary, speaking, reading, listening, writing and pronunciation progressions
     - review and retrieval system, assessment system, file structure, assumptions and risks

     The user approved it as the architectural baseline, **Architecture v1.0**.
  2. **The architecture was converted into a milestone-based construction process** (M0–M8, `03_MILESTONES.md`) following *Design → Build → Validate → Approve → Scale*, with milestone isolation, a mandatory close procedure, and a STOP after each milestone.
  3. **Persistent project memory was introduced** in `Docs/`. The binding content of the blueprint, which until then existed only in chat, was captured in `01_CURRICULUM_DECISIONS.md`: 43 decisions with reasons and consequences, plus Appendices A–J (unit map, dependencies, grammar spiral, thresholds, file architecture, lesson template, workload). A change-control procedure and a change proposal register were added.
  4. **The curriculum will be built incrementally**, not in one massive generation. Pilot before scaling (one A2 unit in M4) is mandatory.
- **Reason:** About 157 high-quality course files cannot be produced reliably in one operation. The project spans many sessions, so it must be recoverable from the filesystem alone. Validating a pilot prevents a flawed template from spreading across the course.
- **Impact:**
  - Any new session can resume from `Docs/`.
  - M1 is in progress: deliverable 1 of 8 done.
  - Remaining M1 deliverables are blocked on OD-05 (course root), OD-06 (`Docs/` vs `00_Curriculum/` roles) and OD-07 (templates location / reserved numbers 04–05).
  - Process refinements proposed but not yet approved: work packages in M5–M7 and a review stop after B1-U01 (OD-09); `CLAUDE.md` and `git init` as recovery aids (OD-10).
  - No course content has been created.

---

## [002] 2026-09-11 — M1 completed: lesson standards, validation framework, recovery file, git

- **Milestone:** M1 (completed)
- **Affected files:**
  - **Created:** `Docs/04_LESSON_STANDARDS.md`, `Docs/05_VALIDATION_LOG.md`, `CLAUDE.md`, `.gitignore`, `GERMAN_LEARNING_PLAN/.gitkeep`
  - **Updated:** `Docs/00_PROJECT_STATE.md`, `Docs/01_CURRICULUM_DECISIONS.md`, `Docs/03_MILESTONES.md`, `Docs/06_CHANGELOG.md`
- **Change:**
  1. **User decisions recorded** (2026-09-11):
     - OD-01: 7 h/week
     - OD-02: exam-compatible, not exam-focused
     - OD-03: general topics, English as comparison language
     - OD-04: Anki, AI role-play and TTS available; tutor optional
     - OD-05: course root `GERMAN_LEARNING_PLAN/`
     - OD-06: `Docs/` authoritative; optional learner-facing `00_Curriculum/`
     - OD-07: `Docs/04` + `Docs/05`
     - OD-08: pilot unit A2-U01 *Erlebnisse*
     - OD-09: work packages in M5–M7 + mandatory review stop after B1-U01
     - OD-10: `CLAUDE.md` + git
     - OD-12: diagnostic completed before M3

     OD-11 (mediation) stays open until before M7.
  2. **`04_LESSON_STANDARDS.md` v1.0 created** (provisional until the M4 pilot):
     - lesson architecture: 19 components, mandatory/optional matrix per file type, length and activity rules, retrieval distribution, speaking levels S1–S4, scaffolding table, recycling rules, grammar and example-selection rules, AI role-play prompt block
     - file standards: Markdown, headings, naming and IDs, YAML metadata with grammar keys, linking, answer keys, word banks, Anki TSV format, register labels, CEFR labels, section icons
     - quality checklist
     - file skeletons
  3. **`05_VALIDATION_LOG.md` created:** entry format, validation types, 13 categories, severity scale, approval states, and V-001 (M1 validation).
  4. **`CLAUDE.md` created:** a concise recovery and workflow pointer into `Docs/`.
  5. **Course root `GERMAN_LEARNING_PLAN/` created**, empty except for `.gitkeep` so git tracks it.
  6. **Git initialised** (branch `main`) with `.gitignore`. It ignores OS and editor files, Obsidian workspace state, learner audio recordings and generated `.apkg` files.
  7. **M1 scope narrowed by the user's definition of M1 completion.** These items were moved out of M1:
     - course README
     - `00_Curriculum/01`–`08` (now optional)
     - stage READMEs
     - `Resources/` files
     - `Learner_Workbook/` files

     They are provisionally reallocated just in time to M2/M3/M4/M6 (OD-13, to be confirmed at M2 start). Proposed work packages were added to M3.
  8. **Local consistency updates to `01`** (no architectural content changed; the version stays v1.0):
     - CD-05, CD-28, CD-36, CD-38: file-timing references updated
     - CD-41: pilot and B1 review stop recorded as decided
     - CD-43: OD-05/06/10 recorded
     - Appendix H: now shows `CLAUDE.md`, `.gitignore`, `Docs/04`–`05`, and marks `00_Curriculum/01`–`08` as optional
- **Reason:** Complete the project infrastructure so future milestones have a stable standard, a validation framework, a fixed destination, automatic recovery and version history.
- **Impact:**
  - M1 is **COMPLETE**. M2 is **NOT STARTED — AWAITING APPROVAL**.
  - Every future course file is built and checked against `04`, and every validation is recorded in `05`.
  - M3 cannot start before the learner has taken the diagnostic.
  - Version history:
    - `024a999` "M1 infrastructure initialized": the complete infrastructure.
    - A follow-up commit records the V-001 results (PASS WITH NOTES), which could only be written after the initial commit existed.

---

## [003] 2026-09-11 — Autonomous mode authorised; AI-attribution trailers removed from git history

- **Milestone:** Between M1 and M2
- **Affected files:**
  - **Updated:** `CLAUDE.md`, `Docs/00_PROJECT_STATE.md`, `Docs/03_MILESTONES.md`, `Docs/05_VALIDATION_LOG.md`
  - **Created:** `tools/check_links.py`
  - **Git history:** both commits rewritten
- **Change:**
  1. **Autonomous execution M2 → M8** authorised by the user (2026-09-11).
     - Per milestone or batch: design → build → validate → correct → record → commit → push → continue, without approval stops.
     - Stop conditions: an architectural contradiction, an unavailable resource, filesystem problems, a fundamental architecture change.
     - Consequences:
       - the "STOP after each milestone" rule is replaced
       - the M4 pilot and B1-U01 review stops become documented Claude validations, with no user approval wait
       - OD-12 is superseded: M3 is built without diagnostic results; A1 adapts via routing and the Schnelltest
       - OD-13 is confirmed
       - OD-11 is delegated to Claude before M7
  2. **Git attribution.** The user forbade `Co-Authored-By` and any other AI-attribution lines in past and future commits.
     - Both commits were rewritten locally with `git filter-branch --msg-filter`:
       - `024a999` → `96621af`
       - `702a566` → `0d9ee6c`
     - Backup refs were deleted, the reflog expired, and the old objects were purged with `gc`.
     - The rule is recorded in `CLAUDE.md`.
  3. **Force push blocked.** The force push (`--force-with-lease`) to update GitHub was blocked by the Claude Code permission system. GitHub still has the old commits. The user must run the push once (command in `00` §15). Until then, work continues locally.
  4. **`tools/check_links.py` added** as a maintained validation tool. It checks links and anchors, and reports links to files planned in Appendix H as PLANNED; `--strict` for M8.
- **Reason:**
  - The user's explicit instructions (autonomy; attribution).
  - Reproducible validation across sessions.
- **Impact:**
  - M2 starts immediately.
  - History is clean locally.
  - Remote synchronisation is pending user action.

---

## [004] 2026-09-11 — M2 Diagnostic System complete

- **Milestone:** M2 (completed) → M3 (started)
- **Affected files:**
  - **Created:**
    - `GERMAN_LEARNING_PLAN/README.md`
    - `GERMAN_LEARNING_PLAN/00_Curriculum/09_Diagnostic_Test.md`
    - `GERMAN_LEARNING_PLAN/Resources/Rubrics.md`
    - `GERMAN_LEARNING_PLAN/Learner_Workbook/Progress_Tracker.md`
  - **Removed:** `GERMAN_LEARNING_PLAN/.gitkeep`
  - **Updated:** `Docs/00`, `03`, `04` (B4, v1.0.1), `05`, `06`
- **Change:**
  1. **Diagnostic.** 10 parts in 2 sittings (about 3 h):
     - self-assessment
     - recognition (27 items)
     - grammar production (73)
     - vocabulary retrieval (40, with a gender score)
     - reading (3 texts, A1–B1)
     - fluency (20 timed cued sentences + 10 quick questions)
     - listening (3 TTS scripts)
     - writing (3 prompts, A1–B1)
     - speaking (6 recorded prompts, which become Story Bank Stage 0)
     - pronunciation (read-aloud + a phone-dictation intelligibility test)

     Routing is per A1 section: P/R/S → 5 categories, a speed rule, a repair order, and 3 overall routes. Also: A2 preview interpretation, vocabulary-domain and gender flags, the retrieval-gap calculation, and a self-assessment vs results comparison.
  2. **Rubrics.**
     - speaking and writing rubrics (5 criteria × 0–4)
     - stage anchors for A1/A2/B1
     - fluency scale
     - pronunciation checklist mapped to the units that train each sound, and dictation bands
     - **error-category codes** (WO, VF, CA, GE, AE, PR, WC, SP, PU, RE, PRN), used everywhere from now on
     - AI rating prompts for writing and speech transcripts
     - checkpoint thresholds
  3. **Progress Tracker.** Diagnostic result tables, grammar spiral (keys from `04` B4 × 4 stages), can-do checklists per stage, unit log, checkpoint table, weekly study log.
  4. **Course README.** Start page, route, weekly rhythm, lesson arc, tools setup, status table.
  5. **A1 section map** fixed in `03` (M3), because the diagnostic routes to these IDs.
- **Reason:** The M2 specification. The section map is fixed now so that M3 stays consistent with the routing.
- **Impact:** The course can now be started: the learner can take the diagnostic. M3 builds the A1 units with exactly these section IDs and the elements the routing categories rely on.

---

## [005] 2026-09-11 — M3 WP1: A1 resources, workbook, A1-U01; CD-05 example corrected

- **Milestone:** M3, WP1
- **Affected files:**
  - **Created (Resources):** `Sentence_Map.md`, `Grammar_Tables.md`, `English_German_Interference.md`, `Pronunciation_Guide.md`, `Redemittel.md`, `Speaking_Toolkit.md`, `Writing_Toolkit.md`, `Listening_Reading_Sources.md`, `Anki/A1.tsv`
  - **Created (Learner_Workbook):** `Story_Bank.md`, `Error_Log.md`, `Chunk_Bank.md`, `Writing_Portfolio.md`
  - **Created (other):** `A1/README.md`, `A1/A1-U01_Ich_und_du.md`, `tools/build_anki.py`
  - **Updated:** `01` (CD-05 example row), `04` (v1.0.2), `09_Diagnostic_Test.md` (Story Bank numbering), Docs 00/03/05/06
- **Change:**
  1. **Shared A1 resources.**
     - The Sentence Map, the course's grammar backbone, is complete from A1 to B1: statements, questions, the bracket, verb-final clauses, position 0, Mittelfeld tendencies, speaking drills.
     - The toolkits (speaking, writing, listening/reading, including TTS instructions and reusable task sheets) are complete.
     - Grammar tables, interference list, pronunciation guide and Redemittel have their A1 content, and grow later.
  2. **Learner Workbook.** The Story Bank has 8 tasks × 3 stages with requirements and a recording log. Error Log (codes from the Rubrics, Top 5), Chunk Bank, Writing Portfolio.
  3. **A1-U01 Ich & du.** The first A1 unit, and the model for the A1 variant:
     - Schnelltest + routing
     - §A–§D, each with Refresh / practice / ⏱️ timed retrieval / ➕ Extra
     - a for-everyone fluency block (60/45/30 introduction, rapid-fire interview, AI role-play, tandem profile)
     - pronunciation, typical mistakes, word bank, self-check, 26 flashcards
  4. **Anki export.** `tools/build_anki.py` generates `Resources/Anki/<stage>.tsv` from the lesson flashcard tables (the single source).
  5. **`01` CD-05 example row corrected** (local correction, the format is unchanged). The original row put *weil* in the Vorfeld. Correct is: the conjunction occupies the Position-2 seat, which is *why* the verb moves to the end. This is the central intuition the Sentence Map teaches, so the example has to show it correctly.
  6. **`04` v1.0.2:** D4 adds 📚 Wortschatz + 🔗 for A1 units; B8 drops the type tag and documents the generator.
- **Reason:** The M3 WP1 plan. Correctness of the core grammar model.
- **Impact:**
  - Learners can now start A1.
  - WP2 (A1-U02, A1-U03) follows the validated A1-U01 pattern.

---

## [006] 2026-09-11 — M3 WP2: A1-U02, A1-U03, structure checker

- **Milestone:** M3, WP2
- **Affected files:**
  - **Created:** `A1/A1-U02_Essen_und_Einkaufen.md`, `A1/A1-U03_Mein_Tag.md`, `tools/check_structure.py`
  - **Updated:** `Resources/Grammar_Tables.md`, `Resources/Anki/A1.tsv` (regenerated), `CLAUDE.md`, Docs 00/03/05/06
- **Change:**
  1. **A1-U02 Essen & Einkaufen.**
     - §A gender clues + 5 plural patterns
     - §B the accusative as "only the masculine changes", with pronouns
     - §C *kein/nicht/doch*
     - §D possessives
     - §E shopping language: *mögen / gern / möchten*; quantities
     - Plus: TTS market dialogue, bakery and dinner-planning role-plays, the fridge 60/45/30 task
  2. **A1-U03 Mein Tag.**
     - §A official vs everyday time, including the *halb* trap
     - §B separable verbs as "the bracket opens"
     - §C time first + frequency
     - Plus: a voicemail (TTS), the main task (info-gap with a unique solution), weekday 60/45/30 = Story Bank Task 2 early recording
  3. **`tools/check_structure.py`** (maintained tool) automates the `04` format rules: one H1, `<details>` balance and blank lines, heading levels, YAML keys, activity numbering and time estimates, A1 section IDs, flashcard tables.
- **Reason:** The M3 WP2 plan; reproducible validation for all later batches and for M8.
- **Impact:** WP3 (A1-U04, A1-U05, A1 Checkpoint) completes A1.

---

## [007] 2026-09-11 — M3 complete: A1 Fundament (A1-U04, A1-U05, A1 Checkpoint)

- **Milestone:** M3 (completed) → M4 (started)
- **Affected files:**
  - **Created:** `A1/A1-U04_Koennen_muessen_duerfen.md`, `A1/A1-U05_In_der_Stadt.md`, `A1/A1_Checkpoint.md`
  - **Updated:** `GERMAN_LEARNING_PLAN/README.md` (status: A1 ready; full resource table), `Resources/Anki/A1.tsv` (124 cards), Docs 00/03/05/06
- **Change:**
  1. **A1-U04 Können, müssen, dürfen.**
     - §A modal meanings, with the *nicht müssen ≠ must not* trap and the no-*zu* rule
     - §B modal bracket (+ separable verbs rejoining)
     - §C imperative with *bitte/mal* (+ infinitive on signs and in recipes)
     - §D a rule-of-thumb table for *nicht*
     - Main task: flat-share rules negotiation; favours; must/want/can 60/45/30
  2. **A1-U05 In der Stadt.**
     - §A *wo?/wohin?* place phrases + directions with a text map
     - §B *war/hatte/es gab* + *vor* = ago
     - §C recognising the Perfekt (participle shapes, a first look at *sein* vs *haben*, 6 usable phrases), the bridge to A2-U01
     - Main tasks: asking the way (repeat-back check), the ticket-machine problem; station listening; Story Bank Task 3 early recording
  3. **A1 Checkpoint.** 6 parts (Reading 12, Language in context 24 mapped to all 19 sections, Writing 2 tasks, Listening 10, Fluency 20, Speaking = Story Bank A1 × 8 + 2 AI-examined situations). Thresholds per Appendix G, a result table, a retake policy, and a remediation map per part.
- **Reason:** The M3 plan; A1 stage complete and validated (V-007).
- **Impact:**
  - The learner can take the diagnostic and do all of A1.
  - M4 (the A2 pilot) begins. It is the first unit in the 5-file A2 format and will test `04` v1.0.2 for real.

---

## [008] 2026-09-12 — M4 complete: A2 pilot (A2-U01 Erlebnisse) validated; `04` v1.1

- **Milestone:** M4 (completed) → M5 (started)
- **Affected files:**
  - **Created:**
    - `A2/README.md`
    - `A2/A2-U01_Erlebnisse/` (5 files)
    - `Resources/Verb_Lists.md`
    - `Resources/Anki/A2.tsv`
    - `tools/check_vocab.py`
  - **Updated:**
    - `Resources/Grammar_Tables.md`, `Redemittel.md`, `English_German_Interference.md`, `Pronunciation_Guide.md` (A2 sections)
    - course `README.md` (status, Verb Lists)
    - `CLAUDE.md` (tools)
    - `Docs/04_LESSON_STANDARDS.md` → **v1.1**
    - Docs 00/03/05/06
- **Change:**
  1. **A2-U01 Erlebnisse**, the first unit in the 5-file A2 format:
     - L1: Perfekt with *haben*, regular and separable participles, sequence words
     - L2: *sein* vs *haben*, irregular participles, trips
     - L3: no-*ge* participles, *schon mal / noch nie*, follow-ups, the natural Perfekt + *war/hatte* mix
     - L4: info-gap main task, Story Bank Task 3 at A2 (2/1.5/1), a blog, an office dialogue, an email, a mixed review with A1, a unit quiz with a redo map
  2. **`04` v1.1 (pilot findings, V-008):**
     - **B2:** explanation subsections are unnumbered H3
     - **A8:** ★ = practised, verified with `tools/check_vocab.py` (≥3 occurrences); recognition count is an upper guideline
     - **D1:** "New words" line in 🔗, and blank-page recall in ✅
     - **D2:** workbook update in L4; link to the next unit
     - **D3:** overview flashcards = words not on lesson cards; plain `## Wortschatz` anchor
  3. **`tools/check_vocab.py`** (maintained tool) makes vocabulary recycling measurable, per unit and in the M8 audit.
- **Reason:** The pilot-before-scaling rule (CD-41). Two findings (heading hierarchy; ★ items not practised) would have repeated across about 100 files if not fixed now.
- **Impact:**
  - M5 builds A2-U02 to U10 under `04` v1.1, using the per-unit checklist in `00` §6.
  - The A1 files remain valid: the v1.1 changes concern explanation subsections and word banks, which the A1 single-file format does not use in the affected way.

---

## [009] 2026-09-12 — M5 WP1: A2-U02, A2-U03, A2-R1

- **Milestone:** M5, WP1
- **Affected files:**
  - **Created:** `A2/A2-U02_Menschen_und_Geschenke/` (5), `A2/A2-U03_Wohnen/` (5), `A2/A2-R1_Wiederholung.md`, `.gitattributes`
  - **Updated:** Resources (Grammar_Tables, Verb_Lists, Redemittel, English_German_Interference, Pronunciation_Guide), `tools/check_vocab.py`, `Anki/A2.tsv`, Docs 00/03/05/06
- **Change:**
  1. **A2-U02 Menschen & Geschenke**, the dative:
     - L1: forms after *mit/bei/von* and "the A1 mystery solved"
     - L2: dative verbs, *gefallen* flip, *Mir ist kalt*
     - L3: two objects, word order, congratulations
     - L4: choosing a present (negotiation), Story Bank Task 8, forum, voicemail, thank-you email, review, quiz
  2. **A2-U03 Wohnen**, two-way prepositions:
     - L1: *Wo?* → dative; position verbs
     - L2: *Wohin?* → accusative; the verb pairs
     - L3: always-dative prepositions, *nach/zu/in*, *seit* + present; flat ads + a viewing call
     - L4: furnish a room from TTS instructions (draw), Story Bank Task 4, Mira's email, writing, review, quiz
  3. **A2-R1 Wiederholung**, the first cumulative review:
     - 3 sittings, 50/30/20 weighting
     - interleaved case and tense rounds, an error hunt
     - a reading + retelling, a vocabulary sprint, a new-neighbour role-play mixing all topics
     - an error-clinic protocol, a voicemail, a reply email, a 15-item quiz with a redo map
  4. **Resources** grew with A2 sections for all three units. `check_vocab.py` now handles phrases starting with a short word. `.gitattributes` normalises line endings.
- **Reason:** The M5 WP1 plan.
- **Impact:** A2.1 is half done: U01–U03 + R1. WP2 (U04–U06, R2, Midpoint) follows, with lesson plans recorded in `00` §6.

---

## [010] 2026-09-12 — M5 WP2 complete: A2-U04, A2-U05, A2-U06, A2-R2, A2 Midpoint

- **Milestone:** M5, WP2 (A2-U04 was committed first, as commit `23f1688`; this entry covers the whole work package)
- **Affected files:**
  - **Created:** `A2/A2-U04_Essen_und_Gewohnheiten/` (5), `A2/A2-U05_Gesundheit/` (5), `A2/A2-U06_Einkaufen_und_Kleidung/` (5), `A2/A2-R2_Wiederholung.md`, `A2/A2_Midpoint_Checkpoint.md`
  - **Updated:** Resources (Grammar_Tables, Verb_Lists, Redemittel, English_German_Interference, Pronunciation_Guide), `Anki/A2.tsv` (337 cards), `GERMAN_LEARNING_PLAN/README.md`, Docs 00/03/05/06
- **Change:**
  1. **A2-U04 Essen & Gewohnheiten:** L1 *weil / denn* for reasons and eating habits · L2 *dass*-clauses, opinions, agreeing and disagreeing, *dass* vs *das* · L3 the restaurant script, *ohne* + accusative, *Könnte ich …?*, tipping · L4 mini-debate, Story Bank Task 7, canteen newsletter, flatmate dialogue, forum post, review, quiz.
  2. **A2-U05 Gesundheit:** L1 body parts, *Mir tut … weh*, dative for body parts · L2 reflexive verbs, the doctor's visit, instructions with *sollen* · L3 *wenn*-clauses, Präteritum of modals, calling in sick, the pharmacy · L4 three-scene main task, Story Bank Task 5, health article, voice message, two emails, review, quiz.
  3. **A2-U06 Einkaufen & Kleidung:** L1 clothes and colours, endings after *der/die/das*, *welch-/dies-*, "the blue one" · L2 endings after *ein/kein/mein*, the signal rule, sizes, trying on, paying · L3 faults, exchange, voucher, refund, shop rules, insisting politely · L4 three-scene main task, 4/3/2 retelling, survey article, service call, complaint email, review, quiz.
  4. **A2-R2 Wiederholung:** 3 sittings, 50/30/20, mixed conjunction and form rounds, an endings clinic, an error clinic, three reading texts, two voice messages, a combined reply, a 20-item quiz with a redo map.
  5. **A2 Midpoint Checkpoint:** diagnostic, not a gate. Reading (9) · language in context (22) · listening (9) · speaking and writing with the rubrics, plus a refresh map from each error type to the unit and resource that fixes it.
  6. **Resources:** verb-final-clause and opinion/restaurant sections for U04; reflexive pronouns and modal Präteritum tables, adjective endings stage 1, reflexive verb list, health and clothes-shopping Redemittel, two interference blocks, two pronunciation sections.
- **Reason:** The M5 WP2 plan in `00` §6.
- **Impact:** A2.1 (U01–U06 + R1, R2, Midpoint) is complete. WP3 (U07–U10, R3, A2 Exit) closes M5.

---

## [011] 2026-09-12 — M5 complete: A2-U07 to U10, A2-R3, A2 Exit Checkpoint

- **Milestone:** M5, WP3 — and with it **M5 (A2 Completion) is finished**
- **Affected files:**
  - **Created:** `A2/A2-U07_Reisen_und_Verkehr/` (5), `A2/A2-U08_Arbeit_und_Termine/` (5), `A2/A2-U09_Feste_und_Plaene/` (5), `A2/A2-U10_Medien_und_Technik/` (5), `A2/A2-R3_Wiederholung.md`, `A2/A2_Exit_Checkpoint.md`
  - **Updated:** Resources (Grammar_Tables, Verb_Lists, Redemittel, English_German_Interference, Pronunciation_Guide), `Anki/A2.tsv` (561 cards), `GERMAN_LEARNING_PLAN/README.md`, Docs 00/03/05/06
- **Change:**
  1. **A2-U07 Reisen & Verkehr:** comparative and superlative (*als* vs *so … wie*, *gern–lieber–am liebsten*) · travel prepositions *Wohin?/Wo?* and the ticket counter · indirect questions with *ob* and question words, delays and refunds · plan-and-survive main task with Story Bank Task 4.
  2. **A2-U08 Arbeit & Termine:** jobs, *seit/ab/vor/für/bis*, *werden* as a full verb · verbs with fixed prepositions and *da-/wo-* words · the business phone call, appointments and the Mittelfeld order · three-scene main task with Story Bank Task 2.
  3. **A2-U09 Feste & Pläne (light):** invitations, accepting and declining, *doch/mal* · the future (present + time word, *werden*) · dates and ordinals, festivals, party small talk · the A2 exam task "Gemeinsam etwas planen" with Story Bank Task 6.
  4. **A2-U10 Medien & Technik:** technical problems and *man/jemand/niemand* · Konjunktiv II for advice, wishes and politeness (no unreal conditionals, CD-15) · *deshalb/trotzdem/sondern* and media habits · support-call main task with Story Bank Task 1.
  5. **A2-R3:** the whole of A2 in three sittings — connector round, forms clinic, three text types, vocabulary sprint, four role-plays, error clinic, four recordings, timed writing, 25-item quiz with a redo map.
  6. **A2 Exit Checkpoint:** the B1 gate per Appendix G — reading (15), language in context (20), listening (12), an **integrated scenario** (email → voicemail → call → message), speaking (monologue, planning dialogue, four reactions), writing (personal + formal), the Story Bank table for all eight tasks, thresholds, a remediation map and a pointer to the Goethe *Modellsatz*.
  7. **Resources:** comparison, places, *da-/wo-*, middle field, future, dates, Konjunktiv II and connector-overview tables; the verbs-with-prepositions list; travel, work/phone, inviting and advice Redemittel; four interference blocks and four pronunciation sections.
- **Reason:** The M5 WP3 plan in `00` §6.
- **Impact:** **A2 is complete**: 10 units, 3 cumulative reviews, a midpoint diagnostic and an exit gate, with 561 A2 flashcards. Next: M6 (B1.1), starting with the B1 README and B1-U01, followed by the special review of German task instructions.

---

## [012] 2026-09-12 — M6 WP1: B1 starts — B1 README, B1-U01 Lebenswege, `04` v1.2

- **Milestone:** M6, WP1 (including the **B1-U01 review stop** required by `03`)
- **Affected files:**
  - **Created:** `B1/README.md`, `B1/B1-U01_Lebenswege/` (5 files), `Resources/Anki/B1.tsv`
  - **Updated:** `Docs/04_LESSON_STANDARDS.md` → **v1.2** (new rule A7.1), Resources (Grammar_Tables, Verb_Lists, Redemittel, English_German_Interference, Pronunciation_Guide), Docs 00/05/06
- **Change:**
  1. **B1 README:** what changes at B1 (instruction language, text length, speaking and writing targets, model answers), the B1.1 unit table, and the "B1 mindset" — say more than one sentence, talk around missing words, accuracy where meaning depends on it, daily input, speak to people.
  2. **B1-U01 Lebenswege:** L1 Präteritum of all verbs and Perfekt-vs-Präteritum · L2 *als / wenn / wann* with childhood memories · L3 Plusquamperfekt and the time conjunctions *nachdem, bevor, während, seit, bis, sobald* · L4 biography presentation, Story Bank Task 3 (4/3/2), a 250-word biography to read, a two-generation interview, a 150–180-word portrait to write, quiz.
  3. **`04` v1.2 — rule A7.1 (the review-stop decision):** a per-element table of the instruction language for B1.1 and B1.2 plus five rules on English support lines (first use only, never hide the task, separate italic line, restatement not translation, and the switch to full German at B1-U07).
  4. **Resources:** B1 Präteritum table and the Plusquamperfekt/time-conjunction table; the Präteritum verb list (33 irregular + 5 mixed); B1 narrating and presenting Redemittel; a narration interference block; a B1 pronunciation section on Präteritum forms and breathing in long sentences.
- **Reason:** The M6 WP1 plan in `00` §6, and the review stop mandated by `03` M6.
- **Impact:** B1 has begun, and the instruction-language question — the biggest open format question for the remaining eleven units — is now settled in the standard rather than decided again in each unit. Next: B1-U02 (relative clauses, adjective endings stage 2, n-declension).

---

## [013] 2026-09-12 — M6 WP1 complete: B1-U02, B1-U03; Git workflow changed to commit-only

- **Milestone:** M6, WP1
- **Affected files:**
  - **Created:** `B1/B1-U02_Menschen_beschreiben/` (5), `B1/B1-U03_Arbeit_und_Beruf/` (5)
  - **Updated:** Resources (Grammar_Tables, Redemittel, English_German_Interference, Pronunciation_Guide), `Anki/B1.tsv` (170 cards), `CLAUDE.md`, Docs 00/05/06
- **Change:**
  1. **B1-U02 Menschen beschreiben:** L1 relative clauses (Nom./Akk.), appearance and character · L2 dative and prepositional relative clauses, n-declension, *sich* = each other · L3 adjective endings stage 2 (dative, article-less) and the paraphrase toolkit · L4 "Wer ist das?" + Taboo, Story Bank Task 8, WG profiles, two views of one colleague, a 150–180-word portrait.
  2. **B1-U03 Arbeit & Beruf:** L1 *zu* + infinitive (and where it is absent) · L2 *um … zu* vs *damit*, *wozu?*, *zum Lernen* · L3 *da*-word + clause and the full job interview (strengths, weaknesses, questions, salary) · L4 complete application (letter + interview), Story Bank Task 1 at B1, two contrasting application letters, a rejection call with feedback.
  3. **Resources:** relative-clause, adjective-endings-stage-2, n-declension, *zu*-infinitive, purpose and *da*-word tables; B1 Redemittel for describing people and for applications; two interference blocks; two pronunciation sections.
  4. **Git workflow (user instruction, 2026-09-12):** Claude now **commits only and never pushes**; the user pushes to GitHub. Recorded in `CLAUDE.md` and `00` §1/§10. Reason: GitHub kept a cached "claude" entry in the repository's Contributors list even after the history had been rewritten to remove all AI-attribution trailers, and the user wants full control over what reaches the public repo.
- **Reason:** The M6 WP1 plan in `00` §6, and the user's Git instruction.
- **Impact:** B1.1 is half built (README, U01, U02, U03 + the instruction-language rule). Next: **B1-R1** (first B1 cumulative review), then B1-U04 (Konjunktiv II, full) and B1-U05 (genitive, paired connectors).

---

## [014] 2026-09-12 — M6 WP2: B1-R1, B1-U04, B1-U05

- **Milestone:** M6, WP2
- **Affected files:**
  - **Created:** `B1/B1-R1_Wiederholung.md`, `B1/B1-U04_Gesundheit_und_Wohlbefinden/` (5), `B1/B1-U05_Reisen_und_Kulturen/` (5)
  - **Updated:** Resources (Grammar_Tables, Redemittel, English_German_Interference, Pronunciation_Guide), `Anki/B1.tsv` (283 cards), Docs 00/05/06
- **Change:**
  1. **B1-R1 Wiederholung:** the first B1 cumulative review — 50 % B1-U01–U03, 30 % A2.2, 20 % older, in three sittings, with a subordinate-clause round across all six connector types, a forms clinic, three text types, a vocabulary sprint, four role-plays, timed writing, an error clinic, four recordings, a 4/3/2 retelling and a 25-item quiz with a repair map.
  2. **B1-U04 Gesundheit & Wohlbefinden:** L1 Konjunktiv II of the present (forms, unreal conditions, wishes, politeness) · L2 Konjunktiv II of the past (*hätte/wäre* + Partizip II, *hätte … sollen/können*, near-misses, mixed time) · L3 the advice ladder, softening particles and reacting to advice, with the stress and wellbeing vocabulary · L4 four "Was würden Sie tun?" scenarios, Story Bank Task 2, an article on the holiday effect, three views on work–life balance, an advice-column reply.
  3. **B1-U05 Reisen & Kulturen:** L1 the genitive (forms, possession, *wegen/trotz/während/statt/innerhalb/außerhalb*, *dessen/deren*, written vs spoken) · L2 paired connectors and *je …, desto …*, plus how to compare cultures without generalising · L3 the formal complaint in five parts, factual register, demands and deadlines, following up by phone · L4 complaint + culture talk, Story Bank Task 5, an Overtourism article, three voices from a tourist town, a forum post.
  4. **Resources:** the full B1 Konjunktiv II table, the genitive and paired-connector tables, Redemittel for hypotheticals/advice and for complaints/culture comparison, two interference blocks and two pronunciation sections.
- **Reason:** The M6 WP2 plan in `00` §6.
- **Impact:** B1.1 is five sixths built. Only **B1-U06 (Passiv)** and the **B1 Midpoint** remain before M6 closes. Validated as V-014.

---

## [015] 2026-09-12 — M6 COMPLETE: B1-U06, B1 Midpoint Checkpoint

- **Milestone:** M6, WP3 and closure
- **Affected files:**
  - **Created:** `B1/B1-U06_Medien_und_Nachrichten/` (5), `B1/B1_Midpoint_Checkpoint.md`
  - **Updated:** `B1/README.md` (every built unit, the review and the Midpoint are now linked from the roadmap), Resources (Grammar_Tables, Redemittel, English_German_Interference, Pronunciation_Guide), `Anki/B1.tsv` (339 cards), Docs 00/03/05/06
- **Change:**
  1. **B1-U06 Medien & Nachrichten:** L1 *Wie wird das gemacht?* (Passiv Präsens/Präteritum, impersonal passive, *von/durch*, passive vs *man*, describing a process) · L2 *Das muss noch gemacht werden* (passive with modals, passive in subordinate clauses, *werden* ↔ *sein*, distributing tasks and responsibility) · L3 *Nachrichten und soziale Medien* (advantages and disadvantages, weighing up, conceding and objecting, checking sources and false reports) · L4 the editorial-plan main task (process + discussion), Story Bank Task 7, the article "Wem gehört die Nachricht?", three reactions, a reader's letter, mixed review and quiz.
  2. **B1 Midpoint Checkpoint:** a diagnostic over B1-U01 to U06 in two sittings — reading (3 texts, 12 items), language in context (24 items), listening (3 recordings, 10 items), speaking (monologue, discussion, integrated complaint situation) and writing (160–200 words), then a profile table and a refresh map with a two-refresh rule.
  3. **Resources:** the full B1 passive section (forms, *werden* conjugation, rules, the three jobs of *werden*, process language), the B1 arguing and weighing-up Redemittel, and an interference and a pronunciation block for the unit.
- **Reason:** The M6 WP3 plan in `00` §6.
- **Impact:** **M6 (B1.1) is complete**: B1-U01 to U06, B1-R1 and the B1 Midpoint. Validated as V-015. Next: M7 (B1.2), with CP-001 (mediation) to be decided before M7 is finalised.

---

## [016] 2026-09-12 — Recap system per level (CP-002, architecture v1.1)

- **Milestone:** between M6 and M7 (user request)
- **Affected files:**
  - **Created:** `A1/A1_Recap/` (4 files), `A2/A2_Recap/` (4), `B1/B1_Recap/` (4)
  - **Updated:** `A1/README.md`, `A2/README.md`, `B1/README.md`, `GERMAN_LEARNING_PLAN/README.md`, `A1/A1_Checkpoint.md`, `A2/A2_Exit_Checkpoint.md`, `B1/B1_Midpoint_Checkpoint.md` (links only), Docs 00/01/05/06
- **Change:**
  1. Each level now has a **recap folder** in its own folder: `00_Overview.md` (navigation, how to revise, what is deliberately not here) plus **exactly three** reference sheets — `01_Wortschatz.md`, `02_Redemittel.md`, `03_Grammatik.md`.
  2. **Wortschatz:** semantic categories with article, plural, forms, Perfekt auxiliary, case and collocation; plus frequent verbs, frequent adjectives, small words, numbers (A1), the A2 participle list and verbs with prepositions, and at B1 abstract nouns, collocations and word families.
  3. **Redemittel:** organised by communicative purpose, with **fixed expressions marked off from productive patterns** (🔒 / 🔁), and a memorisable list at the end of each level (20 / 25 / 30 sentences).
  4. **Grammatik:** every structure of the level with forms, word order, examples, exceptions, contrasts with similar structures, and a typical-error table; each sheet ends in a spoken self-test.
  5. **Scope:** only the levels that exist (A1, A2, B1) were built. B2/C1/C2 do not exist in the repository and were not invented. The B1 recap is marked `in-progress` and covers B1.1, with a **Was noch fehlt** table for U07–U12.
- **Reason:** User request of 2026-09-12 (change proposal **CP-002**, approved the same day): after finishing a level, the learner needs one consolidated place answering *what should I know now?* without rereading every lesson. Three separate sheets rather than one file, so each can be detailed and still findable.
- **Impact:** Architecture **v1.0 → v1.1**; Appendix H updated (≈169 course files). No existing file was moved or restructured; the recaps add no flashcards and no exercises. Validated as V-016.

---

## [017] 2026-09-13 — CP-003: Kurs auf A1 → C2 erweitert (Architektur v2.0)

- **Milestone:** between M6 and M7 (user request); creates the new milestones M9–M11
- **Affected files:**
  - **Created:** `B2/README.md` + `B2/B2_Recap/` (4), `C1/README.md` + `C1/C1_Recap/` (4), `C2/README.md` + `C2/C2_Recap/` (4)
  - **Updated:** `GERMAN_LEARNING_PLAN/README.md` (stage table, recap row, realistic timeline), `B1/README.md` (forward link), Docs 00/01/03/05/06
- **Change:**
  1. **Scope.** The course is no longer "A1 → B1" but **"A1 → C2"**. A1–B1 remains the written core; B2, C1 and C2 are defined stages whose units are built in **M9 (B2, 12 units)**, **M10 (C1, 10 units)** and **M11 (C2, 8 project units)**. M8 stays the audit of the A1–B1 core.
  2. **Stage pages.** Each new stage has a README with its can-do targets, the planned unit inventory, a "what changes compared with the level below" table, and a status block saying the units are not written yet.
  3. **Recaps.** Each new stage has the CP-002 recap shape — `00_Overview` plus exactly three sheets. **B2:** compression, stance, register, Nomen-Verb-Verbindungen, argumentation, Konjunktiv I, participial attributes, passive substitutes, subjective modals. **C1:** connotation, precise near-synonyms, academic and professional language, hedging, cohesion, nominal ↔ verbal style, extended attributes, advanced connectors, focus and ellipsis. **C2:** nuance ladders, idiom by register, metaphor fields, implicature and irony, rhetorical figures, mediation, editing, stylistic syntax, the grammar of vagueness and of authority.
  4. **Honesty.** All twelve new sheets are `status: planned` and state that they are built from the CEFR descriptors and not yet consolidated against units. The C2 stage page states that C2 is prepared, not produced, by a course.
  5. **Planning.** `01` Appendix H gained the new folder tree and a new **Appendix H.1** with the full planned unit inventory for B2, C1 and C2; `03` gained the M9–M11 milestone definitions with scope, work packages and validation criteria.
- **Reason:** User request of 2026-09-13 (change proposal **CP-003**, approved the same day).
- **Impact:** Architecture **v1.1 → v2.0** (scope and stage boundaries changed — a major version by the rule in `01`). Nothing in A1–B1 was moved or rewritten. Full course estimate ≈ 345 files. Validated as V-017.

---

## [018] 2026-09-13 — M9 WP1: B2-U01 gebaut, `04` auf v1.3 (Regel A7.2)

- **Milestone:** M9, WP1 (auf Nutzerwunsch vor M7/M8 begonnen)
- **Affected files:**
  - **Created:** `B2/B2-U01_Identitaet_und_Gesellschaft/` (5), `Resources/Anki/B2.tsv`
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Partizipialattribute, erweitertes Attribut, Gerundivum), `Resources/Redemittel.md` (B2: Abstufen, Einschränken, Zuschreibung vermeiden, Register in drei Höhen), `Resources/English_German_Interference.md` (B2-U01-Block), `Resources/Pronunciation_Guide.md` (lange Nominalphrase, Register), `Learner_Workbook/Story_Bank.md` (**Stufe B2** für alle acht Aufgaben + Spalte im Aufnahme-Log), `B2/README.md`, `tools/build_anki.py` (Stufen B2/C1/C2 ergänzt), Docs 00/03/04/05/06
- **Change:**
  1. **B2-U01 Identität & Gesellschaft:** L1 *Die wachsende Kritik* (Partizip I/II als Attribut, aktiv ↔ passiv, Adjektivendungen, Umformung aus dem Relativsatz) · L2 *Die im Frühjahr beschlossenen Maßnahmen* (erweitertes Attribut, Lesetechnik rückwärts, Gerundivum, Stilentscheidung Attribut ↔ Relativsatz, Amtsdeutsch entschlüsseln) · L3 *Wer gehört dazu?* (abstufen, einschränken, Zuschreibungen erkennen, Register in drei Höhen, das schwierige Gespräch) · L4 *Anwenden* (Podium in beiden Rollen, Story Bank Task 1 auf B2, Kommentar „Die eingebildete Mitte", drei Reaktionen, Leserkommentar 250–300 Wörter, Test).
  2. **`04` v1.3 / Regel A7.2** (aus dem vorgesehenen B2-Review-Stop): ab B2 sind Lektionen **einsprachig Deutsch**, einschließlich der Erklärungen und Fehlertabellen. Englisch bleibt nur in KI-Rollenspielblöcken, in den Prompts der Abruf- und Karteikartentabellen und in zitierten englischen Kalken.
  3. **Story Bank Stufe B2:** alle acht Aufgaben bekommen B2-Anforderungen (einordnen statt nur erzählen, Abstufung, Register, Partizipialattribute); das Aufnahme-Log hat jetzt eine B2-Spalte.
  4. **`tools/build_anki.py`** erzeugt jetzt auch `B2.tsv`, `C1.tsv`, `C2.tsv` (B2 startet mit 61 Karten).
- **Reason:** Nutzerauftrag vom 2026-09-13, die oberen Stufen tatsächlich zu schreiben, beginnend mit B2, in derselben Architektur.
- **Impact:** Die B2-Vorlage ist validiert (V-018) und für U02–U12 freigegeben. M7 (B1.2) und M8 bleiben offen; die Sequenzabweichung ist in `03` vermerkt.

---

## [019] 2026-09-13 — M9 WP2 (Teil 1): B2-U02 Arbeitswelt & Karriere

- **Milestone:** M9, WP2
- **Affected files:**
  - **Created:** `B2/B2-U02_Arbeitswelt_und_Karriere/` (5)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Funktionsverbgefüge und Nominalstil), `Resources/Redemittel.md` (B2: Kritik, Konflikt, Eskalation), `Resources/English_German_Interference.md`, `Resources/Pronunciation_Guide.md`, `Anki/B2.tsv` (120 Karten), `B2/README.md`, Docs 00/05/06
- **Change:**
  1. **B2-U02 Arbeitswelt & Karriere:** L1 *Eine Entscheidung treffen* (Funktionsverbgefüge: zwölf Funktionsverben mit ihrer Logik, feste Artikel und Präpositionen, Protokollstil ↔ Gesprächsstil) · L2 *Nach Prüfung der Unterlagen* (Nominalstil ↔ Verbalstil in beide Richtungen, die Präpositionen des Nominalstils mit Kasus, Nominalisierungsmuster, Stilkritik an der Substantivitis, Bescheid-Übersetzung) · L3 *Das Konfliktgespräch* (Kritik in fünf Schritten, Beobachtung ↔ Bewertung mit Kalender-Probe, sechsstufige Eskalationsleiter, auf Vorwürfe reagieren, deutsche Direktheit einordnen) · L4 *Anwenden* (Konfliktgespräch in beiden Rollen + Bestätigungsmail, Story Bank Task 5 auf B2 als Verhandlung, Fachartikel „Die Zuständigkeitslücke", drei Stimmen aus dem Betrieb, Eskalations-E-Mail 250–300 Wörter, Test).
  2. **Resources:** vollständige B2-Tabelle der Funktionsverbgefüge und der Nominalstil-Präpositionen; Redemittel für Kritik, Reaktion auf Vorwürfe, Einlenken und schriftliche Absprache; Interferenzblock (u. a. *Es tut mir leid* ≠ englisches *sorry*, *Das ist nicht mein Job*); Aussprachblock zu Betonung im Gefüge und Intonation im Konflikt.
- **Reason:** M9 WP2 laut `03`; Fortsetzung des Nutzerauftrags vom 2026-09-13, B2 Einheit für Einheit zu schreiben.
- **Impact:** B2 hat jetzt zwei vollständige Einheiten. Validiert als V-019.

---

## [020] 2026-09-13 — M9 WP2 (Teil 2): B2-U03 Bildung & Lernen

- **Milestone:** M9, WP2
- **Affected files:**
  - **Created:** `B2/B2-U03_Bildung_und_Lernen/` (5)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Konjunktiv I und indirekte Rede), `Resources/Redemittel.md` (B2: Referieren, Zusammenfassen, Zahlen), `Anki/B2.tsv` (177 Karten), `B2/README.md`, Docs 00/05/06
- **Change:**
  1. **B2-U03 Bildung & Lernen:** L1 *Er sagt, er sei* (Konjunktiv-I-Formen, Ersatzregel, drei Zeitstufen, indirekte Fragen und Aufforderungen, *laut / zufolge / angeblich / sollen / wollen*) · L2 *Dem Bericht zufolge* (zwölf Redeeinleitungsverben und ihre Haltung, durchgehend referieren, Abwechslungsmittel, Zitat ↔ Paraphrase ↔ Zusammenfassung, Quellenangabe, eigene Stimme abtrennen) · L3 *Bildungswege* (das deutsche Bildungssystem in acht Begriffen, Bildungswege erzählen, Anteile und Entwicklungen versprachlichen, *um / auf / von … auf*, Beschreibung ↔ Deutung) · L4 *Anwenden* (Referat ohne Wertung + Debatte in beiden Rollen, Story Bank Task 3 auf B2, Artikel „Die Illusion der Durchlässigkeit", drei Reaktionen, Zusammenfassung 250–300 Wörter, Test).
  2. **Resources:** vollständige Konjunktiv-I-Tabelle mit Ersatzregel und Zeitstufen; Redemittel für Redeeinleitungsverben, Quellenangaben, Abwechslung beim Referieren, Abtrennung der eigenen Stimme sowie Zahlen und Grafikbeschreibung.
- **Reason:** M9 WP2 laut `03`.
- **Impact:** B2 hat jetzt drei vollständige Einheiten (U01–U03). Validiert als V-020. Zusätzlich wurde der **Gesamtkurs auf nichtlateinische Zeichen geprüft** — nach einer Korrektur 0 Treffer.

---

## [021] 2026-09-13 — M9 WP2 abgeschlossen: B2-U04 und B2-R1

- **Milestone:** M9, WP2 (abgeschlossen)
- **Affected files:**
  - **Created:** `B2/B2-U04_Medien_und_Oeffentlichkeit/` (5), `B2/B2-R1_Wiederholung.md`
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Passiversatzformen — alle acht Formen), `Resources/Redemittel.md` (B2: Quellenkritik und Hedging), `Anki/B2.tsv` (228 Karten), `B2/README.md`, Docs 00/05/06
- **Change:**
  1. **B2-U04 Medien & Öffentlichkeit:** L1 *Das lässt sich belegen* (*sich lassen*, *-bar / -lich*, *man* und seine Grenzen, Registerwahl) · L2 *Die Frist ist einzuhalten* (*sein + zu*, *haben + zu*, Gerundivum, unpersönliches Passiv, *bekommen*-Passiv, Gesamtübersicht der acht Formen) · L3 *Wem kann man glauben?* (fünf Prüffragen, acht Manipulationstechniken, Hedging, sachlich widersprechen) · L4 *Anwenden* (Faktencheck + Stellungnahme, Story Bank Task 7 auf B2, Essay „Das Misstrauen als Gewohnheit", drei Reaktionen, schriftliche Stellungnahme, Test).
  2. **B2-R1 Wiederholung:** erste kumulative B2-Wiederholung nach Appendix G — drei Sitzungen, 28-Item-Aufwärmen, Formen-Klinik, Umformungs-Runde, vier Textsorten, Wortschatz-Sprint, vier Sprechsituationen, Schreiben unter Zeitdruck, Fehlerklinik mit Fehlertypen, vier Hörminiaturen, 4/3/2-Referat, 20-Item-Test und ein Reparaturplan mit Zwei-Auffrischungen-Regel.
  3. **Resources:** die vollständige Tabelle der acht Passiv- und Ersatzformen mit Registerzuordnung; Redemittel für die fünf Prüffragen, acht Manipulationstechniken, sechs Hedging-Stufen und sachlichen Widerspruch.
- **Reason:** M9 WP2 laut `03`; Nutzerauftrag, B2 fortlaufend ohne Rückfrage zu bauen (2026-09-13).
- **Impact:** **M9 WP2 abgeschlossen.** B2 umfasst jetzt U01–U04 und R1. Validiert als V-021. Als Nächstes WP3: U05–U08, R2, B2 Midpoint.

## [022] 2026-09-13 — M9 WP3 (Teil 1): B2-U05 Wirtschaft & Konsum + Reihenfolge der Milestones

- **Milestone:** M9, WP3 (laufend)
- **Affected files:**
  - **Created:** `B2/B2-U05_Wirtschaft_und_Konsum/` (5 Dateien)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Conditional and concessive clauses), `Resources/Redemittel.md` (B2: Negotiating and talking about money), `Anki/B2.tsv` (281 Karten), `B2/README.md`, Docs 00/03/05/06
- **Change:**
  1. **B2-U05 Wirtschaft & Konsum:** L1 *Sollte es dazu kommen* (*wenn / falls / sofern / soweit*, Bedingung ohne *wenn* mit Verb auf Position 1, *es sei denn*, Nominalbedingungen wie *bei Nichtzahlung*) · L2 *So berechtigt die Kritik auch ist* (konzessive Konjunktionen, Adverbien, Präpositionen, *zwar … aber*, *so + Adjektiv + auch*, echtes vs. rhetorisches Einräumen) · L3 *Der Preis und der Wert* (fünf Verhandlungsphasen, Preis/Kosten/Folgekosten/Wert, Ablehnen in fünf Stärken, *günstig* vs. *billig*) · L4 *Anwenden* (Verhandlung + schriftliche Vereinbarung, Story Bank Task 6 auf B2 mit Zielkonflikt, Artikel „Die Armutsprämie", drei Stimmen als Hörvorlage, Leserbrief, Test).
  2. **Resources:** vollständige Bedingungsübersicht (Formen, Register, vier Typen von real bis irreal-Vergangenheit) und Konzessivübersicht (Bauform → Wortstellung); Redemittel für die fünf Verhandlungsphasen, fünf Ablehnungsstärken und das Sprechen über Geld.
  3. **Reihenfolge festgeschrieben** (Nutzerentscheidung 2026-09-13): **M9 (B2) → M7 (B1.2) → M8 (Audit) → M10 (C1) → M11 (C2)**. In `03` als Tabelle vor M9 eingetragen, in `00` als `Build order` im Statusblock.
- **Reason:** M9 WP3 laut `03`; Nutzerauftrag, B2 fortlaufend zu bauen und danach B1 zu Ende zu führen (2026-09-13).
- **Impact:** B2 umfasst jetzt U01–U05 und R1. Validiert als V-022. Als Nächstes B2-U06 Wissenschaft & Forschung (subjektive Modalverben).

## [023] 2026-09-13 — M9 WP3 (Teil 2): B2-U06 Wissenschaft & Forschung

- **Milestone:** M9, WP3 (laufend)
- **Affected files:**
  - **Created:** `B2/B2-U06_Wissenschaft_und_Forschung/` (5 Dateien)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Subjective modal verbs), `Resources/Redemittel.md` (B2: Research, evidence and degrees of certainty), `Resources/English_German_Interference.md` (B2-U06), `Resources/Pronunciation_Guide.md` (B2-U06), `Anki/B2.tsv` (330 Karten), `B2/README.md`, `B2/B2_Recap/00_Overview.md`, `B2/B2_Recap/03_Grammatik.md`, Docs 00/05/06
- **Change:**
  1. **B2-U06 Wissenschaft & Forschung:** L1 *Sie soll es bewiesen haben* (*sollen* für fremde, *wollen* für Selbstbehauptungen, Infinitiv Perfekt, objektiv ↔ subjektiv, *angeblich / vermeintlich / zufolge / nach eigenen Angaben*) · L2 *Das dürfte kein Zufall sein* (Gewissheitsskala *muss → kann nicht*, Vermutung in der Vergangenheit inkl. *worden sein*, *anscheinend* ↔ *offenbar*, Verbot der doppelten Absicherung) · L3 *Korrelation ist keine Ursache* (Forschungswortschatz, eine Studie referieren, vier Erklärungen für jeden Zusammenhang, fünf Fehlschlüsse, Zahlen ehrlich sagen) · L4 *Anwenden* (Faktencheck mündlich und schriftlich, Story Bank Task 2 auf B2, Artikel „Die Wiederholung, die keiner macht“, drei Stimmen zur Reproduzierbarkeit, Zusammenfassung für Eilige, Test).
  2. **Resources:** die beiden Achsen der subjektiven Modalverben als Gesamttabelle; Redemittel zum Referieren, Einordnen und zu den fünf Fehlschlüssen; zwölf Interferenzfallen (u. a. *eventually*, *evidence*, *significant*, *dürfte nicht*); Aussprachehinweise zum unbetonten Infinitiv Perfekt und zu Fachwörtern auf *-tion*.
  3. **B2-Recap konsolidiert:** § 4 (Subjektive Modalverben) ist jetzt die geprüfte Fassung aus U06 statt der CEFR-Referenz; die Statuszeile nennt **U01–U06** und benennt ausdrücklich, was weiterhin unkonsolidiert ist.
- **Reason:** M9 WP3 laut `03`; Nutzerauftrag, B2 fortlaufend zu bauen (2026-09-13).
- **Impact:** B2 umfasst jetzt U01–U06 und R1. Validiert als V-023. Als Nächstes B2-U07 Recht & Regeln (Genitivpräpositionen, Passiv im Nebensatz).

## [024] 2026-09-13 — M9 WP3 (Teil 3): B2-U07 Recht & Regeln

- **Milestone:** M9, WP3 (laufend)
- **Affected files:**
  - **Created:** `B2/B2-U07_Recht_und_Regeln/` (5 Dateien)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Genitive prepositions and verb clusters), `Resources/Redemittel.md` (B2: Rules, rights and formal complaints), `Resources/English_German_Interference.md` (B2-U07), `Resources/Pronunciation_Guide.md` (B2-U07), `Anki/B2.tsv` (377 Karten), `B2/README.md`, `B2/B2_Recap/00_Overview.md`, `B2/B2_Recap/03_Grammatik.md`, Docs 00/05/06
- **Change:**
  1. **B2-U07 Recht & Regeln:** L1 *Aufgrund der Sachlage* (Genitivpräpositionen nach Bedeutungsfeldern, Dativ-Ausnahmen, nachgestellte Präpositionen, unsichtbarer Genitiv im artikellosen Plural, Register) · L2 *Was zu beachten ist* (Verbreihenfolge am Nebensatzende bis zu vier Verben, Ersatzinfinitiv, Skala der Strenge, Rechte/Pflichten/Haftung, Regeltexte in drei Fragen zerlegen) · L3 *Recht haben und Recht bekommen* (vier Eskalationsstufen, Aufbau eines förmlichen Schreibens, höflich und trotzdem hart, Amtsdeutsch entschlüsseln, Vertrag/Kündigung/Widerruf/Mahnung/Bescheid) · L4 *Anwenden* (Widerspruch schriftlich und am Telefon in beiden Rollen, Story Bank Task 4 auf B2, Artikel „Die unbeantragten Ansprüche“, drei Stimmen zum Verfahren, vollständiger Widerspruch, Test).
  2. **Resources:** Genitivpräpositionen als Gesamttabelle nach Bedeutungsfeldern samt Kasus- und Registerregeln; die Verbketten am Nebensatzende inklusive Ersatzinfinitiv; Redemittel für Strenge-Skala, Eskalationsstufen, Schreibenaufbau und Amtsdeutsch → Klartext; dreizehn Interferenzfallen; Aussprache von Nominalgruppen, Verbketten, Daten und Nummern.
  3. **B2-Recap konsolidiert:** § 7 enthält jetzt die geprüfte Präpositionstabelle aus U07 und die Verbketten; die Statuszeile nennt U01–U07.
  4. **Ethische Absicherung:** Die Einheit sagt an drei Stellen ausdrücklich, dass sie **Sprache** übt und **keinen Rechtsrat** gibt, und verweist auf Vertrag und Beratungsstelle.
- **Reason:** M9 WP3 laut `03`; Nutzerauftrag, B2 fortlaufend zu bauen (2026-09-13).
- **Impact:** B2 umfasst jetzt U01–U07 und R1. Validiert als V-024. Als Nächstes B2-U08 Gesundheit & Psyche (Futur I/II als Vermutung), dann B2-R2 und das B2 Midpoint.

## [025] 2026-09-13 — M9 WP3 (Teil 4): B2-U08 Gesundheit & Psyche

- **Milestone:** M9, WP3 (laufend)
- **Affected files:**
  - **Created:** `B2/B2-U08_Gesundheit_und_Psyche/` (5 Dateien)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Futur as assumption), `Resources/Redemittel.md` (B2: Health, feeling and supportive conversation), `Resources/English_German_Interference.md` (B2-U08), `Resources/Pronunciation_Guide.md` (B2-U08), `Anki/B2.tsv` (427 Karten), `B2/README.md`, `B2/B2_Recap/00_Overview.md`, `B2/B2_Recap/03_Grammatik.md`, Docs 00/05/06
- **Change:**
  1. **B2-U08 Gesundheit & Psyche:** L1 *Er wird es vergessen haben* (Futur I als Vermutung über die Gegenwart, Futur II über die Vergangenheit und für die abgeschlossene Zukunft, Hilfsverbwahl, Signalwörter, Futur ↔ Modalverb als Registerfrage) · L2 *Mir geht es nicht gut* (Dativkonstruktionen, Schmerzverben, seelische Zustände in drei Stufen, Alltagswort ≠ Diagnose, fünf Antwortstufen auf „Wie geht's?“) · L3 *Zuhören, ohne zu reparieren* (vier Gesprächsschritte, was selten hilft, konkrete Angebote mit Datum, Grenzen setzen, um Unterstützung bitten, und die Sätze für den Moment, in dem ein Gespräch nicht reicht) · L4 *Anwenden* (Gespräch und Nachricht in beiden Rollen, Story Bank Task 8 auf B2 mit Beleg statt Etikett, Artikel „Die Erschöpfung, die keine Diagnose ist“, drei Stimmen zur Belastung, die Nachricht, die hilft, Test).
  2. **Resources:** Futur als Vermutung mit Gebrauchstabelle und Registervergleich zu den subjektiven Modalverben; Redemittel für Befinden, Beschwerden, die vier Gesprächsschritte, Grenzen und Bitten; dreizehn Interferenzfallen; Aussprache von unbetontem *wird*, *mir* ↔ *mich* und der Gesprächspause.
  3. **B2-Recap konsolidiert:** § 5 ist jetzt die geprüfte Fassung aus U08; die Statuszeile nennt U01–U08.
  4. **Ethische Absicherung:** vier Hinweise „kein medizinischer Rat, keine Therapie-Ausbildung“ mit Verweis auf Ärztin, Beratungsstelle und Notdienst (ohne erfundene Nummern); beide Rollenspiel-Prompts schließen akute Krisen und Diagnosen ausdrücklich aus.
- **Reason:** M9 WP3 laut `03`; Nutzerauftrag, B2 fortlaufend zu bauen (2026-09-13).
- **Impact:** B2 umfasst jetzt U01–U08 und R1. Validiert als V-025. Es fehlen zum Abschluss von WP3 noch **B2-R2** und das **B2 Midpoint Checkpoint**.

## [026] 2026-09-13 — M9 WP3 abgeschlossen: B2-R2 und B2 Midpoint Checkpoint

- **Milestone:** M9, WP3 (**abgeschlossen**)
- **Affected files:**
  - **Created:** `B2/B2-R2_Wiederholung.md`, `B2/B2_Midpoint_Checkpoint.md`
  - **Updated:** `B2/README.md`, Docs 00/05/06
- **Change:**
  1. **B2-R2 Wiederholung:** zweite kumulative B2-Wiederholung nach Appendix G — drei Sitzungen, 28-Item-Aufwärmen, Formen-Klinik mit 24 Items in vier Gruppen, Umformungs-Runde über drei Register, zwei Dreiminuten-Themen, vier Textsorten, Wortschatz-Sprint über vier Felder, vier Situationen mit Registerwechsel als Härtetest, Schreiben unter Zeitdruck, Fehlerklinik mit 16 typisierten Fehlern, vier Höraufnahmen, 4/3/2-Referat, 20-Item-Test und die Zwei-Auffrischungen-Regel.
  2. **B2 Midpoint Checkpoint:** Diagnose nach der ersten Hälfte von B2 in zwei Sitzungen — Lesen (Bescheid, populärwissenschaftlicher Absatz, zwei Nachrichten), Sprache im Kontext (24 Punkte), Hören (drei Aufnahmen), Sprechen (Monolog, Faktencheck, integrierte Situation mit Sie/du-Wechsel), Schreiben (Widerspruch, 220–260 Wörter) mit Bewertungsraster, Profiltabelle, Richtwerten und einer Auffrischungskarte, die **genau zwei** Bereiche zulässt und für acht Fehlerbilder direkt auf die zuständige Aktivität verlinkt.
  3. **B2/README.md:** Statuszeile, Wiederholungs- und Checkpoint-Zeilen sowie der Arbeitsweg auf den neuen Stand gebracht.
- **Reason:** Abschluss von M9 WP3 laut `03`.
- **Impact:** **M9 WP3 abgeschlossen.** Die erste Hälfte von B2 ist vollständig: U01–U08, R1, R2 und das Midpoint. Validiert als V-026. Als Nächstes WP4: **B2-U09 Kunst & Kultur**, U10–U12, B2-R3 und das B2 Exit.

## [027] 2026-09-13 — M9 WP4 (Teil 1): B2-U09 Kunst & Kultur

- **Milestone:** M9, WP4 (laufend)
- **Affected files:**
  - **Created:** `B2/B2-U09_Kunst_und_Kultur/` (5 Dateien)
  - **Updated:** `Resources/Grammar_Tables.md` (B2: Comparison, real and irreal), `Resources/Redemittel.md` (B2: Talking about works and criticism), `Resources/English_German_Interference.md` (B2-U09), `Resources/Pronunciation_Guide.md` (B2-U09), `Anki/B2.tsv` (471 Karten), `B2/README.md`, `B2/B2_Recap/00_Overview.md`, `B2/B2_Recap/03_Grammatik.md`, Docs 00/05/06
- **Change:**
  1. **B2-U09 Kunst & Kultur:** L1 *Als ob nichts gewesen wäre* (irrealer Vergleich mit *als ob / als wenn / als*, beide Wortstellungen, drei Zeitstufen, einleitende Verben inkl. der unpersönlichen, *so tun, als ob* als unterstellte Absicht, *wie* ↔ *als* ↔ *als ob*) · L2 *Je genauer, desto besser* (Vergleichspartikeln, *je … desto/umso* mit ihrer Wortstellung, Unterschiede abstufen von *bei weitem* bis *kaum*, exakte Differenz mit *um*, *immer* + Komparativ, schriftsprachliche Vergleichsausdrücke) · L3 *Worüber man bei einem Film spricht* (Werk beschreiben, Wirkung benennen, die vier Fragen einer Kritik, Geschmack ↔ Urteil, empfehlen und abraten ohne zu verraten) · L4 *Anwenden* (dieselbe Rezension als Entscheidungshilfe und als Kennergespräch, 4/3/2-Rezension, Artikel „Vier Sterne und kein Grund“, drei Stimmen über Kritik, geschriebene Rezension, Test).
  2. **Resources:** realer und irrealer Vergleich als Gesamttabelle inkl. *je … desto* und Abstufungsskala; Redemittel für Beschreiben, Wirkung, die vier Kritikfragen, Geschmack ↔ Urteil und Empfehlungen; dreizehn Interferenzfallen; Aussprache von Konjunktiv-Umlauten, Komparativen und Kulturfremdwörtern.
  3. **B2-Recap konsolidiert:** § 6 enthält die geprüfte Fassung des irrealen Vergleichs und einen neuen Unterabschnitt zum realen Vergleich; Statuszeile U01–U09.
  4. **Story-Bank-Entscheidung:** Die acht Aufgaben sind auf B2 durchlaufen; ab U09 tritt die **Rezension** als 4/3/2-Format an ihre Stelle (`StageB2_Rezension`), begründet im Overview und in L4.
- **Reason:** M9 WP4 laut `03`; Nutzerauftrag, B2 fortlaufend zu bauen (2026-09-13).
- **Impact:** B2 umfasst jetzt U01–U09, R1, R2 und das Midpoint. Validiert als V-027. Als Nächstes **B2-U10 Migration & Zusammenleben** (*indem, sofern, ohne dass, anstatt dass*).

