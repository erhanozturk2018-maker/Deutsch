# 05 — Validation Log

> **Purpose:** The authoritative record of every validation performed on the project: what was checked, against which criteria, what was found, and whether it was approved.
>
> **Rule:** Record only validations that actually happened. Never pre-fill results. Append new entries at the bottom and add them to the index. Entries are not rewritten afterwards; later corrections go in a new entry that references the old one.
>
> Criteria come from [03_MILESTONES.md](03_MILESTONES.md) (per milestone) and from the quality checklist in [04_LESSON_STANDARDS.md](04_LESSON_STANDARDS.md) (Part C, per file).

## Entry index

| ID | Date | Milestone | Artifact(s) | Type | Result | Approval |
|---|---|---|---|---|---|---|
| V-001 | 2026-09-11 | M1 | M1 infrastructure (`Docs/`, `CLAUDE.md`, `.gitignore`, course root, git) | Self-validation + automated checks | PASS WITH NOTES | Approved (user, 2026-09-11) |
| V-002 | 2026-09-11 | between M1/M2 | Git history correction (removal of AI-attribution trailers) | Automated check | PASS (local) / remote pending | – |
| V-003 | 2026-09-11 | M2 | Diagnostic, Rubrics, Progress Tracker, course README | Self-validation + automated checks | PASS WITH NOTES (2 defects fixed) | – (autonomous mode) |
| V-004 | 2026-09-11 | M3 (during WP1) | Remote history correction (follow-up to V-002) | Automated check | PASS | – |
| V-005 | 2026-09-11 | M3 WP1 | A1 resources, Learner Workbook, A1 README, A1-U01, build_anki | Self-validation + automated checks | PASS WITH NOTES (3 minor fixes) | – |
| V-006 | 2026-09-11 | M3 WP2 | A1-U02, A1-U03, tools/check_structure.py | Self-validation + automated checks | PASS WITH NOTES (6 fixes) | – |
| V-007 | 2026-09-11 | M3 (closing) | Whole A1 stage: A1-U01–U05, A1 Checkpoint, A1 resources, README | Self-validation + automated checks | PASS WITH NOTES | – |
| V-008 | 2026-09-12 | M4 (pilot) | A2-U01 Erlebnisse (5 files), A2 README, A2 resources, check_vocab.py | Pilot validation: self-validation + automated checks | PASS WITH NOTES → 04 v1.1 | – (autonomous mode) |
| V-009 | 2026-09-12 | M5 WP1 | A2-U02, A2-U03, A2-R1, resource sections | Self-validation + automated checks | PASS WITH NOTES | – |

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

---

## V-002 — Git history correction (AI-attribution trailers)

- **Date:** 2026-09-11
- **Milestone:** Between M1 and M2
- **Artifact(s):** The git history of `main`
- **Validator:** Claude
- **Validation type:** Automated check
- **Categories:** `VCS`
- **Criteria:**
  1. No commit message reachable from any ref contains `Co-Authored-By` or another AI-attribution line.
  2. The pre-correction commits are no longer present locally.
  3. Commit content (trees) is unchanged; only the messages changed.
- **Method:**
  - `git log --all --format=%B | grep -ci co-authored-by` returned `0`.
  - `git cat-file -t 702a566` / `024a999` both returned *not a valid object* after `update-ref -d refs/original/*`, `reflog expire --expire=now --all` and `gc --prune=now`.
  - `filter-branch --msg-filter` only changes messages. The rewritten commits `96621af` and `0d9ee6c` keep the same authors and files (`git log --stat` identical to V-001's file list).
- **Findings:**
  1. `VCS`, PASS. Criteria 1–3 are met locally.
  2. `VCS`, **Major (open).** The force push that would update GitHub was blocked by the Claude Code permission system. `origin/main` still points to the old `702a566`, whose message contains the trailer. Local `main` has diverged (ahead 2, behind 2), so normal pushes are rejected.
- **Required changes:** The user runs `git push --force-with-lease=main:702a5669f03f751f3c09a5ed8ddda464102ef03d origin main` once (see `00` §15).
- **Resolution:** Pending user action. Claude re-checks with `git fetch` at every boundary and pushes only when a fast-forward push is possible.
- **Result:** PASS locally. The remote is not yet corrected.
- **Approval status:** –

---

## V-003 — M2 Diagnostic System

- **Date:** 2026-09-11
- **Milestone:** M2 — Diagnostic System (closing validation)
- **Artifact(s):**
  - `GERMAN_LEARNING_PLAN/00_Curriculum/09_Diagnostic_Test.md`
  - `GERMAN_LEARNING_PLAN/Resources/Rubrics.md`
  - `GERMAN_LEARNING_PLAN/Learner_Workbook/Progress_Tracker.md`
  - `GERMAN_LEARNING_PLAN/README.md`
  - `tools/check_links.py`
- **Validator:** Claude
- **Validation type:** Self-validation + automated checks
- **Categories:** `STR`, `LNG`, `PED`, `CEF`, `DEP`, `LNK`, `USE`, `SCP`
- **Criteria:** The M2 criteria in `03_MILESTONES.md`, plus the user's M2 specification:
  - distinguish recognition, controlled production, guided retrieval and spontaneous production
  - measure grammar, vocabulary, lexical retrieval, speaking, listening, reading, writing and pronunciation/intelligibility
  - route each area to skip / brief review / consolidate / intensive / prerequisite repair
  - include administration instructions, rubrics and a progress tracker
- **Method:**
  - **Automated** (`python tools/check_links.py` plus inline Python):
    - link and anchor resolution
    - one H1 per file
    - `<details>` open/close balance
    - item-number continuity per part
  - **Manual:**
    - a read-through of every item and answer key
    - an option-position check of the recognition key
    - a word count of the dictation text
    - arithmetic of all maximum scores and domain groupings
    - a walkthrough of the routing rules against boundary cases (P = 6/R ✓/fast; P = 6/R ✗; P = 2/R ✓; P = 2/R ✗; P = 5/slow)
- **Findings:**
  1. `LNK`, PASS. 86 links: 76 ok, 10 planned (to A1 files, `Story_Bank.md` and `Error_Log.md`, all in Appendix H and scheduled for M3), 0 broken.
  2. `STR`, **Minor (fixed).** The diagnostic had 4 H1 headings (for the sittings and scoring), against `04` B2. Resolution: changed to H2/H3. Recheck: one H1 per file.
  3. `PED`, **Major (fixed).** The routing table said "apply the first rule that fits", but listed 🟢 Brief review *before* ⚪ Skip. Brief review (P = 5–6) would have caught every Skip case, so Skip could never be reached. Resolution: reordered to Repair → Intensive → Consolidate → Skip → Brief review, and reworded the Brief review rule. Boundary cases rechecked: P = 6/R ✓/fast → Skip; P = 6 slow → Skip moves down to Brief review.
  4. `STR`, PASS. Item continuity: Part 2 27 items, Part 3 73, Part 4 40, Part 5 13, Part 6 30, Part 7 12, Part 9 6. No gaps. 10 answer boxes, all closed.
  5. `DEP`/`STR`, PASS. Coverage: all 19 A1 sections have 3 production items + 1 recognition item. 15 of 19 also have timed fluency items; §D numbers, U02-§A gender (covered by the gender score instead) and U05-§C recognition have none, by design. All 8 listed A2 topics have 2 production items + 1 recognition item.
  6. `PED`, PASS. The four levels of knowing are each measured by named parts. The recognition–production gap is computed explicitly (R% − P%; C% − V%).
  7. `PED`, **Note.** The M2 criterion "≥ 80% of items require production" is met for grammar and vocabulary: production items 3.1–3.54, 3.58–3.73, Part 4 and Part 6 = 140 of 170 grammar/vocabulary items (82%). Across *all* items including the receptive reading/listening skill tests, the share is about 73%. Reading and listening comprehension are receptive by definition, and the user's specification requires measuring recognition, so this is accepted as intended.
  8. `LNG`, PASS. All German items, texts, transcripts and keys were reread. Answer-key alternatives are given where natural variants exist (e.g. *Ich muss heute zum Arzt*; *Wo kommst du her?* [spoken]). Unnatural but "correct" forms get 1 point with an explanation (e.g. *tausendneunhundert…* for a year; *Ich will …* at the bakery gets 0).
  9. `CEF`, PASS. Texts rise from A1 (notice, announcement) through A2 (email, voicemail, dialogue) to B1 (forum post). Writing and speaking tasks are rated at the level each task allows.
  10. `WRK`, PASS. Estimated time: Sitting 1 ≈ 90 min, Sitting 2 ≈ 85 min, scoring ≈ 30 min.
  11. `USE`, PASS. The file includes: administration instructions, materials list, rules (including marking guesses), TTS instructions with 3 options and a fallback, a scoring walkthrough in 7 steps, and where to record everything in the tracker.
  12. `SCP`, PASS. No learner results were invented. No lesson content was created.
  13. `STR`, **Note.** `04` B4 was extended with the metadata type `diagnostic` and a rule that non-lesson files carry no YAML (v1.0.1). This is a local clarification.
- **Required changes:** None remaining.
- **Resolution:** Findings 2 and 3 fixed before commit.
- **Result:** **PASS WITH NOTES**
- **Approval status:** – (autonomous mode; the user may review at any time)

---

## V-004 — Remote history correction (follow-up to V-002)

- **Date:** 2026-09-11
- **Milestone:** During M3 WP1
- **Artifact(s):** `origin/main` on GitHub
- **Validator:** Claude
- **Validation type:** Automated check
- **Categories:** `VCS`
- **Criteria:** The open finding 2 of V-002. The remote must hold the corrected history, with no AI-attribution trailers in any commit.
- **Method:**
  - With the user's explicit permission: `git push --force-with-lease=main:702a5669f03f751f3c09a5ed8ddda464102ef03d origin main` → `+ 702a566...6265ff2 main -> main (forced update)`
  - Then `git fetch`
  - `git status --short --branch` → `## main...origin/main` (in sync)
  - `git log origin/main --format=%B | grep -ci co-authored-by` → `0`
- **Findings:**
  1. `VCS`, PASS. The remote history is `96621af`, `0d9ee6c`, `cdfa26e`, `6265ff2`, all authored by Erhan, with no trailers.
- **Required changes:** None.
- **Resolution:** Resolves V-002 finding 2.
- **Result:** **PASS**
- **Approval status:** –

---

## V-005 — M3 WP1: A1 shared resources, workbook, A1 README, A1-U01

- **Date:** 2026-09-11
- **Milestone:** M3, WP1
- **Artifact(s):**
  - **Resources:** `Sentence_Map.md`, `Grammar_Tables.md`, `English_German_Interference.md`, `Pronunciation_Guide.md`, `Redemittel.md`, `Speaking_Toolkit.md`, `Writing_Toolkit.md`, `Listening_Reading_Sources.md`, `Anki/A1.tsv` (generated)
  - **Learner_Workbook:** `Story_Bank.md`, `Error_Log.md`, `Chunk_Bank.md`, `Writing_Portfolio.md`
  - `A1/README.md`
  - `A1/A1-U01_Ich_und_du.md`
  - `tools/build_anki.py`
- **Validator:** Claude
- **Validation type:** Self-validation + automated checks
- **Categories:** `STR`, `LNG`, `PED`, `CEF`, `DEP`, `VOC`, `SPK`, `WRK`, `LNK`, `USE`
- **Criteria:**
  - `03` M3 criteria applicable to WP1: section map fidelity, Schnelltest routing, timed retrieval, a fluency task, full route ≤5 h, no zero-knowledge content, forward-marked chunks, CD-05 table format in the Sentence Map
  - `04` Part C checklist for A1-U01
  - skeleton D4
- **Method:**
  - `python tools/check_links.py` → 207 links: 181 ok, 26 planned, 0 broken
  - `python tools/build_anki.py` → A1: 26 cards; TSV header and UTF-8 checked with `cat -A`
  - manual reread of all German in A1-U01 and the resources
  - item-by-item answer-key check
  - time-estimate summation
  - a section-by-section comparison against the M3 section map and D4
- **Findings:**
  1. `STR`/`DEP`, PASS. A1-U01 has exactly the sections §A–§D of the fixed map, with IDs `A1-U01-§A`…`§D`. Each section has: Refresh, examples, practice, a ⏱️ timed retrieval activity, and a ➕ Extra round, i.e. every element the routing categories rely on. The Schnelltest has 3 items per section; its routing table is consistent with the diagnostic categories (the more cautious result wins; 🔴 always full + Extra).
  2. `SPK`, PASS. The speaking levels progress:
     - S1: Activities 3 and 8, drills
     - S2: Activity 13
     - S3: Activity 21, AI role-play with a goal and a complication
     - S4: Activity 19, a timed 60/45/30 retelling, and Activity 20, rapid-fire spontaneous answers

     There is one timed and one unscripted activity for everyone, and a Story Bank Task 1 link.
  3. `PED`, PASS.
     - 7 timed or recorded production activities
     - Production items make up far more than 60% of the practice
     - Activity types: map sorting, transformation, error correction, question generation, reading, TTS listening/form filling, dictation, role-play, a writing profile
     - A1 content is framed as a refresh; nothing assumes zero knowledge
  4. `LNG`, PASS. All German reread. Register notes are included (*Was ist dein Name?* ⚠️ uncommon; *Wo kommst du her?* [spoken]; *zwo* [spoken]). Chunks used before their system is taught (*aus der Türkei*, *bei einer Bank*, *zu Hause*, *mit dem Rad*) are marked as fixed phrases or glossed.
  5. `WRK`, PASS. The full route is about 235 min (Schnelltest 10 + §A 40 + §B 45 + §C 50 + §D 40 + everyone 50), inside the ~4 h estimate. The all-⚪ route is about 60 min.
  6. `USE`, **Minor (fixed).** The A1 README's "fast route ~1 h" was ambiguous: a route with 🟢 sections takes about 1 h 40 min. Relabelled "Fast route (all sections ⚪)".
  7. `LNG`/`STR`, **Minor (fixed).** `01` CD-05 had an incorrect example row (*weil* in the Vorfeld). Corrected: the conjunction takes the Position-2 seat. The table format is unchanged, so this is a local correction (see `06` [005]).
  8. `STR`, **Minor (fixed).** The diagnostic called its speaking prompts "the first six" Story Bank tasks; they are tasks 1, 2, 3, 4, 6 and 7. Wording and file-naming instruction corrected, and a Story Bank number column added.
  9. `STR`, **Note.** `04` v1.0.2 (local):
     - D4 gains the 📚 Wortschatz and 🔗 sections for A1 units, which have no overview file
     - B8 drops the type tag and documents `tools/build_anki.py` as the only way to produce `.tsv` files
  10. `VOC`, PASS. The A1-U01 word bank marks ★ items and uses B7 notation. The 26 flashcards are all production-direction.
  11. `LNK`, PASS. 26 planned links, all to files listed in Appendix H: the remaining A1 units, A1_Checkpoint, and the A2/B1 overview files.
- **Required changes:** None remaining.
- **Resolution:** Findings 6–8 fixed before commit.
- **Result:** **PASS WITH NOTES**
- **Approval status:** – (autonomous mode)

---

## V-006 — M3 WP2: A1-U02 Essen & Einkaufen, A1-U03 Mein Tag

- **Date:** 2026-09-11
- **Milestone:** M3, WP2
- **Artifact(s):** `A1/A1-U02_Essen_und_Einkaufen.md`, `A1/A1-U03_Mein_Tag.md`, `tools/check_structure.py`; `Resources/Grammar_Tables.md` (fix); `Resources/Anki/A1.tsv` (regenerated, 77 cards)
- **Validator:** Claude
- **Validation type:** Self-validation + automated checks
- **Categories:** `STR`, `LNG`, `PED`, `DEP`, `VOC`, `SPK`, `WRK`, `LNK`
- **Criteria:** The `03` M3 criteria (section map, Schnelltest routing, timed retrieval, fluency task, ≤5 h, chunks marked); the `04` Part C checklist.
- **Method:**
  - `python tools/check_structure.py` → 20 files, 0 problems (after fixing a false-positive regex in the new tool itself)
  - `python tools/check_links.py` → 238 links, 212 ok, 26 planned, 0 broken
  - `python tools/build_anki.py` → 77 A1 cards
  - manual reread of all German, answer-key check, timing sums
  - uniqueness check of the info-gap solution in A1-U03 Activity 16
- **Findings:**
  1. `STR`/`DEP`, PASS.
     - U02 has §A–§E; U03 has §A–§C, matching the section map.
     - Every section has Refresh / examples / practice / ⏱️ / ➕.
     - U02 routing adds the diagnostic gender-score rule and the §A → §D dependency order; U03 points to a repair of A1-U01 §B first.
  2. `SPK`, PASS.
     - U02: fridge 60/45/30 (S4), bakery role-play with a complication (S3), dinner-planning negotiation (S3/S4).
     - U03: info-gap "find a time with Sam" (S3, the main task from Appendix B), weekday 60/45/30 (S4 = Story Bank Task 2 early recording).
  3. `PED`, PASS. The A1-U03 info gap has exactly one solution (Thursday from 19:00). The AI prompt keeps Sam's week hidden, so the learner has to ask for the information.
  4. `LNG`, **Minor (fixed), 6 items:**
     - U02 Aussprache list contained a stray "*frisch?* (no ch!)"
     - U02 pronunciation sentence was nonsensical ("halb acht Kuchen")
     - U02 Activity 14 #7 required a dative ending (*mit ihrem Hund*) not yet taught; replaced with an accusative item (*suchen ihren Hund*)
     - U02 gender table gave *Bäckerei* as an example under "-ie"; fixed to "-ei / -ie / -ik", and the same gap fixed in `Grammar_Tables.md`
     - U03 role-play opener *"Du wolltest dich treffen"* was unnatural without *mit mir*; replaced
     - U03 pronunciation sentence contradicted itself (*Am Freitag … heute*); replaced
  5. `DEP`, PASS. Chunks used ahead of their system are flagged with forward links: dative (*in meinem Kühlschrank, auf dem Markt, bei meinen Eltern*) → A2-U02; *ein neues Handy* → A2-U06; Perfekt *gekauft* → A2-U01; *den Kunden* (n-declension) → B1-U02.
  6. `WRK`, PASS. U02 full route ≈ 290 min (the longest unit, flagged in the file: "plan 3–4 sittings"); U03 ≈ 245 min. Both are within the ≤ 5 h criterion.
  7. `VOC`, PASS. Both word banks are in B7 notation with ★ items; separable verbs are marked with `\|`. Flashcards: U02 27, U03 24, all production-direction.
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before commit.
- **Result:** **PASS WITH NOTES**
- **Approval status:** – (autonomous mode)

---

## V-007 — M3 closing validation: the whole A1 stage

- **Date:** 2026-09-11
- **Milestone:** M3 (closing); covers WP3 (A1-U04, A1-U05, A1 Checkpoint) and the stage as a whole
- **Artifact(s):**
  - `A1/A1-U01` … `A1-U05`, `A1/A1_Checkpoint.md`, `A1/README.md`
  - the A1 resources
  - course `README.md` (status + resource table)
  - `Resources/Anki/A1.tsv` (124 cards)
- **Validator:** Claude
- **Validation type:** Self-validation + automated checks
- **Categories:** `STR`, `LNG`, `PED`, `CEF`, `DEP`, `VOC`, `SPK`, `WRK`, `LNK`, `USE`, `SCP`
- **Criteria:** The complete M3 criteria in `03` (section map, Schnelltest routing, timed retrieval + fluency task per unit, full route ≤5 h, no zero-knowledge content, forward-marked chunks, checkpoint thresholds = Appendix G, CD-05 map format, links resolve, `04` Part C).
- **Method:**
  - `tools/check_structure.py` → 23 files, 0 problems
  - `tools/check_links.py` → 290 links: 268 ok, 22 planned (all to A2/B1 files in Appendix H), 0 broken
  - `tools/build_anki.py` → 124 cards
  - manual reread of U04, U05 and the checkpoint (German, keys, map geometry in U05 Activity 2)
  - stage-level cross-checks: coverage, recycling, speaking progression, pronunciation coverage, workload
- **Findings:**
  1. `STR`/`DEP`, PASS. All 19 section IDs of the map exist, in the right units. The A1 Checkpoint Part 2 tests **every one of the 19 sections** at least once, and its key maps each item to its section for the remediation map.
  2. `PED`, PASS. Every unit has: Schnelltest + routing, per-section ⏱️ timed retrieval and ➕ Extra, a for-everyone block with at least one timed S4 activity and at least one S3 role-play with an AI prompt block, pronunciation, a mistakes table with error codes, a word bank, self-check, and flashcards.
  3. `SPK`, PASS. Speaking builds across the stage:
     - fast-answer and start-with drills (S1–S2)
     - role-plays with a goal and a complication: café, bakery, dinner planning, Sam info gap, flat-share negotiation, favours, directions, ticket machine (S3)
     - 60/45/30 retellings in every unit, plus rapid-fire answers (S4)

     Story Bank Tasks 1, 2, 3 are recorded early in U01, U03, U05; all 8 are recorded in the Checkpoint.
  4. `CEF`, PASS. Skill texts stay at A1: notices, messages, ads, announcements, short dialogues. A2 structures appear only as recognition or fixed phrases (dative place phrases, the Perfekt bridge in U05 §C, *trotzdem / wenn* in one transcript each), and each is marked or glossed.
  5. `VOC`, PASS.
     - All five units have word banks in B7 format.
     - Everyday vocabulary recycles across units (food → U02, U04 fridge/WG, the Checkpoint; transport/times → U03, U05, the Checkpoint; modals → U04, U05 role-plays).
     - 124 production-direction cards.
  6. `LNG`, PASS. All German reread.
     - U04: *müssen/dürfen* negation contrast used consistently; the *braten → Brat!* imperative note is correct.
     - U05: map directions checked, including the "from the station, the cinema is on your LEFT" reversal in answer b6.
     - Checkpoint: keys verified item by item.
     - One link typo in the Checkpoint (`_and_` for `_und_`) was fixed before commit.
  7. `WRK`, PASS. Full routes:
     - U01 ≈ 240 min, U02 ≈ 290 min, U03 ≈ 245 min, U04 ≈ 250 min, U05 ≈ 215 min
     - Checkpoint ≈ 150 min + scoring
     - A1 full route ≈ 23 h; the all-⚪ route ≈ 5 × 1 h + Checkpoint

     Both are within Appendix J (8–25 h).
  8. `PED`/`CEF`, **Note (interpretation recorded).** Appendix G says "≥75% in the written and listening parts" for the A1 gate. This is implemented as: Reading ≥9/12, Language in context ≥18/24, Listening ≥8/10 (≥75%), while **Writing** is rated with the rubric (avg ≥2.5, the same bar as speaking), because productive skills are rubric-rated everywhere in the course (CD-36). The retake policy uses an AI-generated parallel version of Part 2 to avoid rote memory of items.
  9. `WRK`, **Note (open, as expected).** All time estimates are Claude's estimates. No learner trial has happened yet (none is invented). They will be revisited when the learner reports real times (KI-11).
  10. `SCP`, PASS. No learner results invented; no A2/B1 lesson content created; A2/B1 are referenced only as planned links.
- **Required changes:** None remaining.
- **Resolution:** Finding 6's link typo was fixed before commit.
- **Result:** **PASS WITH NOTES**. M3 is complete.
- **Approval status:** – (autonomous mode)

---

## V-008 — M4 pilot validation: A2-U01 *Erlebnisse*

- **Date:** 2026-09-12
- **Milestone:** M4 — A2 Pilot (closing validation)
- **Artifact(s):**
  - `A2/A2-U01_Erlebnisse/` (00_Overview_und_Wortschatz, L1_Mein_Wochenende, L2_Unterwegs, L3_Schon_mal_erlebt, L4_Anwenden)
  - `A2/README.md`
  - `Resources/Verb_Lists.md` (new)
  - A2 sections added to Grammar_Tables, Redemittel, English_German_Interference, Pronunciation_Guide
  - `Resources/Anki/A2.tsv` (64 cards)
  - `tools/check_vocab.py` (new)
- **Validator:** Claude
- **Validation type:** Pilot validation. Self-validation plus automated checks. **No learner trial** yet (none invented).
- **Categories:** `STR`, `LNG`, `PED`, `CEF`, `DEP`, `VOC`, `SPK`, `WRK`, `LNK`, `USE`
- **Criteria:**
  - the M4 pilot criteria in `03`: time 60–90 min per lesson; ≥60% production; ≥6 activity types; every A3 component present or deliberately omitted; main task = Appendix B; `04` Part C
  - the user's pilot questions: realistic length? manageable vocabulary density? understandable explanations? does the sequence work? enough speaking? Markdown organisation? does the standard need adjustment?
- **Method:**
  - `check_structure.py`: first run flagged 3 files, then 0 problems
  - `check_links.py`: 399 links, 0 broken
  - `build_anki.py`: 64 A2 cards
  - `check_vocab.py` (new): first run flagged 6 real + 4 false items; after fixes, 1 borderline item
  - a component-by-component comparison of each lesson with A3, D1–D3
  - summing the time estimates
  - counting activity types and speaking levels
  - reading all German texts, dialogues, keys and samples
- **Findings:**
  1. `WRK`, PASS (estimate). L1 ≈ 80, L2 ≈ 80, L3 ≈ 85, L4 ≈ 85 min, all within 60–90. Each lesson has 7–8 numbered activities (A4: 7–10 for 75–90 min). Unit total ≈ 5.5 h; with flashcards and free listening ≈ 7 h, i.e. one week at 7 h/week, consistent with Appendix J. **Real times are unverified** until a learner trial (KI-11).
  2. `PED`, PASS.
     - **Production share:** well over 60% in every lesson. Only the Entdecken noticing questions and the reading/listening questions are recognition.
     - **Activity types used across the unit (13):** pattern-noticing · transformation · dialogue-completion · story-reconstruction · timed-speaking · role-play · info-gap · retelling 2/1.5/1 · game (two truths and a lie) · reading-comprehension · listening-specific · prediction · writing (forum, email) · mixed review · quiz
     - **Input first:** every new-content lesson opens with discovery (voice message, blog, party dialogue) before the explanation.
  3. `SPK`, PASS.
     - L1: S1 timed drill → S3 role-play (Monday coffee) → S4 60 s
     - L2: S1 trios → S3 trip interview → S4 60 s
     - L3: S3/S4 game + a 60 s story
     - L4: S3 info gap + S4 2/1.5/1 retell (Story Bank Task 3, A2 early version)

     There are ≥2 AI prompt blocks per lesson set, and all use delayed correction. Speaking share of time ≥20% in each lesson.
  4. `STR`, **Major (fixed) → standard change.** Explanations used `####` headings directly under `##`. This violated B2 ("never skip a level"), while `###` is reserved for numbered activities. Fixed by making explanation subsections **unnumbered H3**. `04` B2 was updated (v1.1) so every later unit follows it.
  5. `VOC`, **Major (fixed) → standard change.** `check_vocab.py` showed that 6 ★ items (*Urlaub, spazieren gehen, Ausflug, reden, wandern, langweilig/anstrengend*) appeared fewer than 3 times in the lessons: listed, not practised. Fixed by adding items to L1 #6, L2 #6, L2 #8 checklist, L3 #5, and the L1 #8 checklist. Recheck: 41 ★ items, 1 borderline (*losfahren/losgehen*, 2 + 1 hits across the two forms = 3 exposures, accepted). `04` A8 gained the rule "★ = practised, verified with `check_vocab.py`".
  6. `VOC`, **Note → guideline clarified.** The recognition list has about 15 items plus the participle list, not the ~40 in Appendix E. Judgement: for a unit carrying about 50 participles, ~40 more recognition words would be overload. `04` A8 now treats Appendix E's recognition figure as an upper guideline. This is a local clarification; Appendix E itself is unchanged.
  7. `LNG`, **Minor (fixed), 7 items found in rereading:**
     - L2: *fahren* + object example used a genitive (*meines Vaters*, B1) → replaced
     - L3: *-ieren* stress wrongly given as *teleFOnieren* (in 2 places) → *telefoNIEren*
     - L3: an awkward retrieval item #10 → reworded
     - L4 reading: asked for 5 *sein*-participles but the text had 4 → a sentence added
     - L4 email sample: contained *fallen lassen* (too complex) → *ist fast ins Wasser gefallen*
     - L1: a sloppy "New words" line → cleaned
     - Pronunciation guide: odd example *vereisen* → *verändern*
  8. `CEF`/`DEP`, PASS.
     - Texts are A2 (voice message, blog post, party dialogue, blog, office dialogue).
     - Structures beyond the unit are glossed as phrases, with a forward reference: *dir* (A2-U02), *wollte* (A2-U05), *dass* (A2-U04), *an den See* (A2-U03).
     - Nothing requires unintroduced grammar in production.
  9. `USE`, PASS.
     - The Markdown organisation works: overview → L1–L4, footer navigation, word-bank anchor, answer keys after each activity.
     - Explanations follow the 10-point standard in content and are readable in about 10 minutes.
     - One improvement for later units: a plain `## Wortschatz` heading for the anchor (applied).
  10. `STR`, **Note → D2/D3 clarified.** L4 includes workbook-update instructions, and overview flashcards are limited to words not on lesson cards. Both are written into `04` D2/D3 (v1.1).
  11. `REC`, PASS. `00` §6 now contains the per-unit checklist derived from the pilot and the WP1 lesson plans, so a new session can build the next units consistently.
- **Answers to the user's pilot questions:**
  - **Length:** realistic on paper (80–85 min); needs a learner trial.
  - **Vocabulary density:** manageable after moving the practice gaps in (finding 5).
  - **Explanations:** understandable, with the "why you need this" hook plus tables.
  - **Sequence:** works (discover → explain → drill → timed → task → speak).
  - **Speaking load:** sufficient (≥20% of time, S4 in every lesson).
  - **Markdown:** works.
  - **Standard adjusted?** Yes: `04` v1.1 (findings 4, 5, 6, 10).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed; `04` v1.1 recorded in `06` [008].
- **Result:** **PASS WITH NOTES**. The pilot is validated, and scaling (M5) may proceed under v1.1.
- **Approval status:** – (autonomous mode; the pilot user-approval step was replaced by this documented validation, per the user's 2026-09-11 authorisation)

---

## V-009 — M5 WP1: A2-U02, A2-U03, A2-R1

- **Date:** 2026-09-12
- **Milestone:** M5, WP1
- **Artifact(s):**
  - `A2/A2-U02_Menschen_und_Geschenke/` (5 files)
  - `A2/A2-U03_Wohnen/` (5 files)
  - `A2/A2-R1_Wiederholung.md`
  - Resources: Grammar_Tables (dative, prepositions), Verb_Lists (dative verbs, position verbs, *umziehen*), Redemittel (likes/presents, home), Interference (2 A2 blocks), Pronunciation (question melody, endings, *-ig*, clusters)
  - `tools/check_vocab.py` (short-word phrase fix)
  - `.gitattributes`
  - `Anki/A2.tsv` (172 cards)
- **Validator:** Claude
- **Validation type:** Self-validation + automated checks
- **Categories:** `STR`, `LNG`, `PED`, `CEF`, `DEP`, `VOC`, `SPK`, `WRK`, `LNK`, `USE`
- **Criteria:** The M5 criteria in `03` (unit map fidelity, recycling ≥3 earlier structures per unit + `04` A8, vocabulary within Appendix E, ≥6 activity types per unit, no identical main-task type in consecutive units, reviews 50/30/20 reaching A1, links); the `04` v1.1 Part C checklist; the per-unit checklist in `00` §6.
- **Method:**
  - `check_structure.py` → 41 files, 0 problems
  - `check_vocab.py` → U02: 32 ★, 0 below 3 (after a tool fix for *Es tut mir leid*); U03: 25 ★ rows, 0 below 3
  - `check_links.py` → 550 links, 0 broken, 22 planned
  - `build_anki.py` → 172 A2 cards
  - manual reread of all German; answer keys item by item; timing sums; main-task comparison with Appendix B; review weighting count
- **Findings:**
  1. `STR`/`DEP`, PASS. U02 matches Appendix B (dative system: articles, pronouns, dative verbs, two objects; main task: a present chosen together). U03 matches (two-way prepositions, *stellen/stehen, legen/liegen, hängen*, dative prepositions; main tasks: furnish a room from spoken instructions + a flat-viewing call).
  2. `PED`, PASS.
     - The A1 fixed phrases (*zum, mit dem, im/ins*) are explicitly explained in context: U02 L1 "the A1 mystery, solved", U03 L2 "part 2". This is a strong spiral moment (CD-06).
     - Main-task types differ from U01: negotiation/decision (U02) and info-transfer drawing + phone call (U03), vs U01's info gap.
     - Each unit uses ≥8 activity types.
  3. `SPK`, PASS. Every lesson has ⏱️ drills (S1–S2), an AI role-play with a complication (S3) and a 60 s monologue (S4). The L4s have 2/1.5/1 retellings: Story Bank Task 8 (U02), Task 4 (U03), plus Task 1 in U03 L3.
  4. `VOC`/`DEP`, PASS. "Recycled from" tables cover 5 (U02) and 7 (U03) earlier units, including A1. The R1 weighting was counted: warm-up 8/4/3 items = 53/27/20%. Case round and quiz mix the recent block with A1.
  5. `LNG`, **Minor (fixed), 10 items:**
     - U02 L1: *Onkel* in an *-er* pronunciation list
     - U02 L2: *zu der Wand* → *zur Wand*; a sample answer rewritten to avoid unintroduced adjective endings
     - U02 L4: *für uns* wrongly listed as dative
     - U03 L1: a *denn* in the sample (U04 grammar); an ambiguous/unnatural plan sentence (2 revisions)
     - U03 L2: a trick item printed wrong German; replaced by a clean gap
     - U03 L4: a messy reading key; a misaligned plan solution
     - R1: gloss for *super, dass …*
  6. `CEF`, PASS. Texts are A2 (photo talk, shop dialogue, group chat, forum, voicemail, flat ads, phone call, emails, a story). Structures beyond the unit are glossed or treated as phrases, with forward references: *wir könnten* → U10; *am besten* → U07; *sich freuen* → U05; *dass* → U04; n-declension → B1-U02.
  7. `WRK`, PASS (estimate). Lessons 80–85 min; R1 ≈ 150 min in 3 sittings. No learner trial yet (KI-11).
  8. `VCS`, **Note.** `.gitattributes` (`* text=auto eol=lf`) added, which ends the constant CRLF warnings (V-001 note 8).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before the batch commit.
- **Result:** **PASS WITH NOTES**
- **Approval status:** – (autonomous mode)
