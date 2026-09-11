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
