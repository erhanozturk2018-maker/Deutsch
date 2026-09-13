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

---

## V-010 — M5 WP2: A2-U04, A2-U05, A2-U06, A2-R2, A2 Midpoint

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/A2/A2-U04_Essen_und_Gewohnheiten/` (5 files), `A2-U05_Gesundheit/` (5), `A2-U06_Einkaufen_und_Kleidung/` (5), `A2-R2_Wiederholung.md`, `A2_Midpoint_Checkpoint.md`, and the Resources sections added for these units.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The M5 criteria in `03`; the `04` v1.1 Part C checklist; the per-unit checklist in `00` §6.
- **Method:**
  - `check_structure.py` → 58 files, 0 problems
  - `check_vocab.py` → U04: 0 below 3 · U05: 38 ★ rows, 0 below 3 (after adding practice for *krankschreiben*) · U06: 36 ★ rows, 0 below 3 (after adding practice for *zurückgeben*, *Mütze/Schal/Brille*, *Tüte*)
  - `check_links.py` → 811 links, 0 broken, 17 planned
  - `build_anki.py` → A2.tsv 337 cards (U04–U06 tagged)
  - manual reread of all German; answer keys item by item; activity numbering and timing sums; review weighting count; main-task comparison with Appendix B
- **Findings:**
  1. `STR`/`DEP`, PASS. U05 matches Appendix B (reflexive verbs incl. dative for body parts, *wenn*, Präteritum of modals, *sollen*; doctor's visit and calling in sick). U06 matches (adjective endings stage 1 per CD-17, *welch-/dies-*; complaint and return). U04 was validated in the same batch's first part.
  2. `PED`, PASS. Main-task types differ from the neighbours: U04 debate + restaurant, U05 a three-scene illness sequence, U06 a three-scene purchase-and-return sequence. Each unit uses ≥8 activity types. The adjective-ending load is split over two lessons with the signal rule as the single explanation, and CD-17's communicative accuracy target is stated to the learner in U06 L1 and the overview.
  3. `SPK`, PASS. Every lesson has ⏱️ drills, an AI role-play with a complication and a 60 s monologue. U05 L4 records Story Bank Task 5 (A2); U06 L4 uses a 4/3/2 retelling instead of a Story Bank task, since Tasks 1, 2 and 6 are reserved for U07–U09 (decision recorded in `00` §12).
  4. `VOC`/`DEP`, PASS. "Recycled from" tables: U05 seven earlier units (incl. three A1), U06 seven (incl. two A1 and the A1 case table). R2 weighting counted: warm-up 8/4/3 = 53/27/20 %.
  5. `LNG`, **Minor (fixed), 6 items:**
     - U05 L1: a garbled *ch/sch* pronunciation list rewritten
     - U05 L3: activity numbering started at 4 (renumbered 3–7); the *seit* trick item's instruction now warns that one sentence is about now
     - U06 L2: *nichts zu Kurzes* replaced; a dative adjective phrase in a sample answer removed
     - U06 L3: a dative adjective phrase in an answer key replaced; *in einer anderen Größe/Farbe* marked as a fixed phrase in L2 and L3
     - R2: a genitive (*wegen eines technischen Problems*) replaced by *aus technischen Gründen*
     - Midpoint: a wrong anchor to the Progress Tracker fixed
  6. `CEF`, PASS. Texts stay A2 (chat messages, surgery and shop dialogues, magazine article, notices, small ads, voicemails, reviews, emails). Structures beyond the unit are glossed with a forward reference: *als* → B1-U01, comparison → A2-U07, dative adjective endings → B1-U02, *sich freuen auf* → A2-U08.
  7. `WRK`, PASS (estimate). Lessons 80–85 min; R2 ≈ 150 min in 3 sittings; Midpoint ≈ 110 min in 2 sittings. No learner trial yet (KI-11).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before the batch commit.
- **Result:** **PASS WITH NOTES**
- **Approval status:** – (autonomous mode)

---

## V-011 — M5 WP3 and M5 closure: A2-U07 to U10, A2-R3, A2 Exit Checkpoint

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/A2/A2-U07_Reisen_und_Verkehr/` (5 files), `A2-U08_Arbeit_und_Termine/` (5), `A2-U09_Feste_und_Plaene/` (5), `A2-U10_Medien_und_Technik/` (5), `A2-R3_Wiederholung.md`, `A2_Exit_Checkpoint.md`, and the Resources sections for these units.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The M5 criteria in `03` (unit map fidelity, recycling, vocabulary, ≥6 activity types, no identical main-task type in consecutive units, U09 light, reviews 50/30/20 reaching A1, the Exit implementing Appendix G); the `04` v1.1 Part C checklist; the per-unit checklist in `00` §6.
- **Method:**
  - `check_structure.py` → 80 files, 0 problems
  - `check_vocab.py` → U07: 33 ★, 0 below 3 · U08: 32 ★, 0 below 3 · U09: 29 ★, 0 below 3 · U10: 27 ★, 0 below 3 (each after adding practice for the items the tool flagged)
  - `check_links.py` → 1149 links, 0 broken, 3 planned (all B1 targets)
  - `build_anki.py` → A2.tsv 561 cards, tagged by unit
  - manual reread of all German; answer keys item by item; activity numbering and timings; review weighting count; Exit thresholds compared with Appendix G
- **Findings:**
  1. `STR`/`DEP`, PASS. U07 matches Appendix B (comparison, *an/auf/in/nach* with places, indirect questions, *hätte/würde gern*; trip planning + missed connection). U08 matches (verbs + prepositions, *wo-/da-* words, *seit/ab/vor/für/bis*, *werden* as a full verb, middle field; reschedule by phone + working day). U09 matches and is genuinely **light** (no new major grammar beyond the future, *doch*, dates; 70–75-minute lessons; `est_minutes` 285 vs 325). U10 matches (Konjunktiv II advice/wishes only — no unreal conditionals, per CD-15 — *deshalb/trotzdem/sondern*, *man/jemand/niemand*).
  2. `PED`, PASS. Main-task types stay distinct across the block: comparison-and-decide (U07), three-scene working day (U08), joint planning, exam-style (U09), support call (U10). Each unit uses ≥8 activity types. A2-R3 has an error clinic, a vocabulary sprint and four interleaved role-plays.
  3. `SPK`, PASS. Every lesson has ⏱️ drills, an AI role-play with a complication and a 60 s monologue. Story Bank A2: U07 → Task 4 (with comparisons), U08 → Task 2, U09 → Task 6, U10 → Task 1; the Exit requires all eight and asks for the four early ones to be re-recorded. This closes the allocation decision recorded in `00` §12.
  4. `VOC`/`DEP`, PASS. "Recycled from" tables: U07 seven units, U08 seven, U09 eight, U10 eight, each including A1. A2-R3 weighting counted: warm-up 12/5/3 = 60/25/15 % — within tolerance of 50/30/20 given that the recent block is four units rather than three; the quiz is 25 items weighted 7/6/6/6 across U07–U10 with A1/A2.1 items inside the reading and error clinic.
  5. `ASS`, PASS. The A2 Exit implements Appendix G: four skills in an exam-like structure with original tasks, an **integrated scenario** (email → voicemail → phone call → written message), Story Bank recordings, thresholds ≥70 % per receptive part and task completion ≥3/4 for speaking and writing, a remediation map, and a pointer to the official Goethe *Modellsatz* as external validation (no official material reproduced).
  6. `LNG`, **Minor (fixed), 8 items:**
     - U07 L2/L3: *in einer anderen Größe/Farbe* marked as a fixed phrase (dative endings are B1-U02); *gelten* given a proper explanation and card
     - U08 L1: a garbled pronunciation list rewritten as two clean rules (compounds vs loanwords)
     - U08 L3: two *zu*-infinitives removed from answer keys (B1 grammar)
     - U09 L1: a broken sample sentence and a wrong relative link fixed
     - U09 L2: three explanation subheadings were numbered like activities; renumbered as plain H3
     - U10 L1: a Konjunktiv II sentence removed from the L1 sample (it belongs to L2)
     - U10 L3: a malformed Sentence-Map row and a *zu*-infinitive in a sample answer fixed
     - U10 L4: the *zu*-infinitive in the reading text glossed with a forward reference to B1-U03
  7. `CEF`, PASS. Texts stay A2 (chat, ticket counter, announcements, forum, job ad, voicemails, notices, small ads, advice column, hotline). Forward references are glossed: *als* → B1-U01, dative adjective endings → B1-U02, *zu*-infinitive → B1-U03, unreal conditionals → B1-U04.
  8. `WRK`, PASS (estimate). U07, U08, U10 lessons 80–85 min; U09 70–75 min (light); A2-R3 ≈150 min in 3 sittings; A2 Exit ≈210 min in 2 sittings. No learner trial yet (KI-11).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before the batch commits.
- **Result:** **PASS WITH NOTES** — M5 (A2 Completion) is closed.
- **Approval status:** – (autonomous mode)

---

## V-012 — M6 WP1: B1 README, B1-U01 Lebenswege, and the B1 instruction-language review stop

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/B1/README.md`, `B1/B1-U01_Lebenswege/` (5 files), the B1 sections added to Resources, `Resources/Anki/B1.tsv`, and — as the **special review stop** required by `03` M6 — the instruction-language rule now in `04` A7.1 (v1.2).
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The M6 criteria in `03` (instruction language per CD-10 and `04` A7; B1-length reading texts; the unit map in Appendix B); the `04` Part C checklist; the per-unit checklist in `00` §6.
- **Method:**
  - `check_structure.py` → 86 files, 0 problems
  - `check_vocab.py` → B1-U01: 30 ★ rows, 0 below 3 (after adding practice for *aufwachsen* and *umziehen*)
  - `check_links.py` → 1228 links, 0 broken, 3 planned
  - `build_anki.py` → `B1.tsv` created, 56 cards tagged `B1-U01`
  - manual reread of all German; answer keys item by item; comparison of every instruction against CD-10 and `04` A7
- **Findings:**
  1. `STR`/`DEP`, PASS. B1-U01 matches Appendix B: Präteritum of all verbs (written vs spoken), *als* vs *wenn* (CD-16 kept it for B1), Plusquamperfekt with *nachdem/bevor*, plus *während, seit, bis, sobald*; main task: biography presentation, and the 4/3/2 retelling as Story Bank Task 3 at B1.
  2. **Review stop — instruction language.** The draft used German for activity titles, the first instruction line, success criteria, checklists and the unit goals, with an *italic English support line* under German instructions, and kept explanations, interference notes and error tables in English. Compared against CD-10 ("B1.1: simple German with English support") this is correct, but the standard did not say **which elements** or **how often** the support line appears, which would have produced drift across twelve units.
     - **Decision (recorded in `04` A7.1, v1.2):** a per-element table for B1.1 and B1.2, plus five rules — repeating formulas keep the support line only on first use in a unit; a German instruction must never hide the task; the support line is a separate italic English line, never mixed in; it is a plain restatement, not a translation; support lines disappear from B1-U07 (B1.2) and comprehension answers switch to German there, announced to the learner.
     - B1-U01 was then conformed to the rule and its `standard:` field set to v1.2.
  3. `PED`, PASS. L1 discovery text (a migration biography) → L2 an interview → L3 two versions of the same year (list vs connected) → L4 presentation. The L3 discovery task makes the learner **compare a badly and a well-connected text**, which is the clearest possible motivation for time conjunctions.
  4. `SPK`, PASS. Each lesson has a ⏱️ retrieval drill, an AI role-play (interview, podcast, presentation audience) and a 2-minute monologue; L4 has the 4/3/2 retelling. The presentation prompt asks the AI for structure feedback, not only error correction — appropriate at B1.
  5. `CEF`/`LNG`, PASS with two notes: the reading texts are 190–260 words (B1 range per `03`), the listening texts 180–220. *zu*-infinitives appear in the reading texts and are glossed with a forward reference to B1-U03; one *zu*-infinitive was removed from a sample answer so that production stays inside the unit's grammar.
  6. `LNG`, **Minor (fixed), 4 items:** a garbled sort-task answer key in L1; a Cyrillic character inside an error-table cell in L1; an unclear vowel-length pronunciation example in L1; a *zu*-infinitive in an L3 sample answer.
  7. `VOC`/`DEP`, PASS. "Recycled from" covers eight earlier units including A1; the word bank is built around the biography field; `check_vocab` passes after two additions.
  8. `WRK`, PASS (estimate). Lessons 85–90 min, unit ≈345 min. No learner trial yet (KI-11).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed; the review-stop decision is in `04` v1.2 and `06` [012].
- **Result:** **PASS WITH NOTES** — M6 WP1 continues with B1-U02.
- **Approval status:** – (autonomous mode)

---

## V-013 — M6 WP1 complete: B1-U02 Menschen beschreiben, B1-U03 Arbeit & Beruf

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/B1/B1-U02_Menschen_beschreiben/` (5 files), `B1/B1-U03_Arbeit_und_Beruf/` (5 files), the B1 sections added to Resources, `Resources/Anki/B1.tsv`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The M6 criteria in `03` (instruction language per `04` A7.1, B1-length texts, relative clauses used for talking around words from U02 on, unit map fidelity to Appendix B); the `04` v1.2 Part C checklist; the per-unit checklist in `00` §6.
- **Method:**
  - `check_structure.py` → 96 files, 0 problems
  - `check_vocab.py` → U02: 28 ★, 0 below 3 (after adding practice for *widersprechen*, *ansprechen*, *schlank/kräftig/sportlich*) · U03: 27 ★, 0 below 3 (after adding practice for *abgeben* and *ausbilden*)
  - `check_links.py` → 1367 links, 0 broken, 3 planned
  - `build_anki.py` → `B1.tsv` 170 cards (U01–U03)
  - manual reread of all German; answer keys item by item; every instruction checked against `04` A7.1
- **Findings:**
  1. `STR`/`DEP`, PASS. U02 matches Appendix B: relative clauses in nominative, accusative, dative and with prepositions; adjective endings stage 2 (dative and article-less); n-declension; *sich* = each other; main tasks "Wer ist das?" and Taboo-style describing. U03 matches: *zu* + infinitive, *um … zu* vs *damit*, *da*-word + clause; main tasks job-interview simulation and application letter.
  2. `PED`, PASS. U02 L3 makes the paraphrase strategy an explicit skill with a four-move toolkit (category, function, material/form, comparison) plus rescue phrases — this is CD-18's "describe things whose name you don't know" implemented as a trainable routine rather than a remark. U03 L4 contrasts two application letters (empty adjectives vs concrete examples with numbers), which teaches the register lesson faster than any rule could.
  3. `SPK`, PASS. Every lesson has a ⏱️ drill, an AI role-play and a 2-minute monologue; U02 L4 records Story Bank Task 8 and U03 L4 Task 1 at B1, both as 4/3/2 retellings, with an explicit comparison against the earlier recordings.
  4. `LNG`, **Minor (fixed), 5 items:** a garbled error-table row in U03 L1 (*zurückzurufen*); a malformed ✓/✗ row in U03 L2; a wrong anchor for the *um zu / damit* table (em dash produces a double hyphen in the slug); *ansprechen/widersprechen* and *abgeben/ausbilden* were listed as ★ but barely practised; *schlank/kräftig/sportlich* had no example sentences.
  5. `CEF`, PASS. Reading texts 180–260 words (WG profiles, forum posts, two application letters); listening 180–230 words (photo talk, colleague discussion, interview, rejection call). Forward references glossed: *obwohl* → B1-U07, genitive → B1-U05.
  6. `VOC`/`DEP`, PASS. "Recycled from" tables cover seven and eight earlier units including A1; both units build directly on A2-U06 (endings), A2-U08 (verbs + prepositions) and B1-U01 (Präteritum).
  7. `A7.1`, PASS. The instruction language follows the new rule: German activity titles, German success criteria and checklists, English support lines only on first use of a formula, English explanations, role-play prompts in English.
  8. `WRK`, PASS (estimate). Lessons 85–90 min; each unit ≈345 min. No learner trial yet (KI-11).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before the commits.
- **Result:** **PASS WITH NOTES** — M6 WP1 (B1 README, U01, U02, U03 + review stop) is complete; WP2 (B1-R1, U04, U05) follows.
- **Approval status:** – (autonomous mode)

---

## V-014 — M6 WP2: B1-R1, B1-U04 Gesundheit & Wohlbefinden, B1-U05 Reisen & Kulturen

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/B1/B1-R1_Wiederholung.md`, `B1/B1-U04_Gesundheit_und_Wohlbefinden/` (5 files), `B1/B1-U05_Reisen_und_Kulturen/` (5 files), the B1 sections added to Resources, `Resources/Anki/B1.tsv`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The M6 criteria in `03`; `04` v1.2 including rule A7.1 (instruction language); the per-unit checklist in `00` §6; CD-15 (Konjunktiv II staged: chunks at A2-U10, full system at B1-U04) and CD-17 (adjective endings) for the sequencing.
- **Method:**
  - `check_structure.py` → 107 files, 0 problems
  - `check_vocab.py` → U04: 27 ★, 0 below 3 (after adding practice for *einschlafen/aufwachen* and *Sorge/Termindruck*) · U05: 29 ★, 0 below 3 (after adding practice for *Sehenswürdigkeit*, *mitteilen*, *ankündigen*)
  - `check_links.py` → 1521 links, 0 broken, 3 planned
  - `build_anki.py` → `B1.tsv` 283 cards (U01–U05)
  - manual reread of all German; answer keys item by item; review weighting counted; a targeted scan for Konjunktiv I (`sei/werde/solle`), which does not belong at this stage
- **Findings:**
  1. `STR`/`DEP`, PASS. U04 matches Appendix B (Konjunktiv II in full: unreal *wenn*-clauses, wishes, polite forms; "What would you do?" scenarios and an advice-column reply) and stays inside CD-15: no Konjunktiv I, no reported speech. U05 matches (genitive + *wegen/trotz/während/statt*, paired connectors; formal complaint email and culture-comparison talk).
  2. `PED`, PASS. U04 L3 turns advice into a **graded ladder** (question → *könnte* → *sollte* → *An deiner Stelle* → *Es wäre gut, wenn* → imperative → *müsste*) with a rule that the learner asks three questions before advising — this is the pragmatics layer CEFR B1 asks for and lessons usually skip. U05 L3 teaches the complaint by **contrasting two letters**, so the register lesson is discovered rather than asserted.
  3. `SPK`, PASS. Each lesson has a ⏱️ drill, an AI role-play and a 2-minute monologue. Story Bank at B1: U04 → Task 2, U05 → Task 5, both as 4/3/2 retellings with an explicit comparison against the A2 recording.
  4. `REV`, PASS. B1-R1 weighting counted: warm-up 12/5/3 = 60/25/15 %, quiz 25 items across the three units plus older material; three sittings, error clinic, four role-plays, timed writing and a 4/3/2 retelling, as specified in Appendix G.
  5. `LNG`, **Minor (fixed), 8 items:** four Konjunktiv-I forms in transcripts and samples (*solle, sei, werde* ×2) replaced by indicative or Konjunktiv II, since Konjunktiv I is B1.2 material; *obwohl* glossed with its forward reference to B1-U07; a garbled error-table row in U03 L1 and a malformed ✓/✗ row in U03 L2 (found while cross-checking) fixed in the previous batch; the *um zu / damit* anchor corrected; four ★ items given real practice.
  6. `CEF`, PASS. Reading texts 200–320 words (survey, advice page, article on the holiday effect, station notice, blog on cultural differences, two complaint letters, Overtourism article); listening 180–260 words. Forward references glossed: *obwohl* → B1-U07, Passiv → B1-U06.
  7. `VOC`/`DEP`, PASS. "Recycled from" tables cover seven units each, including A1 and A2; U05 explicitly builds the complaint out of U04's Konjunktiv II, U03's *zu*-infinitive and its own genitive.
  8. `WRK`, PASS (estimate). Lessons 85–90 min; units ≈345 min; B1-R1 ≈165 min in three sittings. No learner trial yet (KI-11).
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before the commits.
- **Result:** **PASS WITH NOTES** — M6 WP2 complete; WP3 (B1-U06 Passiv, B1 Midpoint) closes M6.
- **Approval status:** – (autonomous mode)

---

## V-015 — M6 WP3 and M6 closure: B1-U06 Medien & Nachrichten, B1 Midpoint Checkpoint

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/B1/B1-U06_Medien_und_Nachrichten/` (5 files), `B1/B1_Midpoint_Checkpoint.md`, the B1 passive and argumentation sections added to Resources, `B1/README.md`, `Resources/Anki/B1.tsv`; and M6 as a whole.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The M6 criteria in `03`; `04` v1.2 including rule A7.1; the per-unit checklist in `00` §6; Appendix B for the unit's main tasks; CD-29 (Story Bank) for Task 7.
- **Method:**
  - `check_structure.py` → 113 files, 0 problems
  - `check_vocab.py GERMAN_LEARNING_PLAN/B1/B1-U06_Medien_und_Nachrichten` → 27 ★, **0 below 3** on the first run
  - `check_links.py` → 1611 links, 0 broken, 3 planned (all three to the not-yet-written `B1-U07_Umwelt_und_Nachhaltigkeit/`)
  - `build_anki.py` → `B1.tsv` 339 cards (U01–U06, +56)
  - manual reread of all German; answer keys checked item by item; a targeted scan for Konjunktiv I, which is B1.2 material
- **Findings:**
  1. `STR`/`DEP`, PASS. B1-U06 follows Appendix B: Passiv Präsens/Präteritum, impersonal passive, *von/durch*, passive with modals, passive in subordinate clauses, Vorgangs- vs Zustandspassiv, *man* as the spoken alternative. The two main tasks (describe a process, pros-and-cons discussion) are both in L4 Aktivität 2.
  2. `PED`, PASS. L1 derives the passive from a text about **how a news item is made**, so the grammar and the topic are the same thing. L2 teaches the modal passive through a real editorial meeting and ends in task distribution, which is where learners actually need the form. L3 separates *arguing* from *having an opinion* and teaches "concede first, then object".
  3. `SPK`, PASS. Each lesson has a ⏱️ drill, an AI role-play and a 2-minute monologue; L4 adds the two-part main task and **Story Bank Task 7 (Meine Meinung)** as a 4/3/2 retelling with a comparison against the A2 recording. With this, B1.1 has recorded Story Bank tasks 3, 8, 1, 2, 5 and 7.
  4. `ASS`, PASS. The **B1 Midpoint** covers U01–U06 over five parts (Lesen 12, Sprache im Kontext 24, Hören 10, Sprechen with monologue/discussion/integrated situation, Schreiben 160–200 words), is explicitly **diagnostic, not a gate**, and ends in a profile table plus a refresh map that points at the exact lessons. Reference values are stated as "what solid looks like", not as pass marks.
  5. `LNG`, **Minor (fixed), 4 items:** one Konjunktiv I form (*sei*) in the Midpoint reading text replaced by Konjunktiv II; a confused bullet about *-ieren* verbs in L1's pronunciation section rewritten as two clean groups (*-ieren* and inseparable prefixes); a redundant gloss in L2 Übung 3 item 6 clarified (*sollte* as Präteritum, with the pointer to the identical Konjunktiv II form); five numbered explanation subheadings in L3 changed to plain H3 so they are not read as activities.
  6. `CEF`, PASS. Reading 200–330 words (how a news item is made, editorial meeting transcript, three opinions, "Wem gehört die Nachricht?", three reactions, plus the Midpoint's company email, blog text and forum thread); listening 150–260 words. No forward references beyond the glossed *obwohl* → B1-U07.
  7. `VOC`/`DEP`, PASS. "Recycled from" covers eight earlier units including A1-U04 (modal verbs) and A2-U01 (Partizip II) — the two halves the passive is built from.
  8. `REV`, PASS. The Midpoint's gap-fill and sentence tasks are weighted one grammar block per unit (2×U01, 2×U02, 3×U03, 2×U04, 2×U05, 1×U06 in 2A; the same spread in 2B), so no unit can hide.
  9. `WRK`, PASS (estimate). Unit ≈345 min; Midpoint ≈130 min in two sittings. No learner trial yet (KI-11).
- **M6 as a whole:** B1-U01 to U06, B1-R1, the B1 Midpoint, `B1/README.md`, `Resources/Anki/B1.tsv` and all B1.1 resource content exist and pass the four tools. The B1-U01 review stop happened and produced `04` v1.2 / rule A7.1.
- **Required changes:** None remaining.
- **Resolution:** All findings fixed before the commit.
- **Result:** **PASS WITH NOTES** — M6 (B1.1) complete.
- **Approval status:** – (autonomous mode)

---

## V-016 — Recap system (CP-002): A1, A2 and B1 recap folders

- **Date:** 2026-09-12
- **Object:** `GERMAN_LEARNING_PLAN/A1/A1_Recap/`, `A2/A2_Recap/`, `B1/B1_Recap/` (4 files each: `00_Overview`, `01_Wortschatz`, `02_Redemittel`, `03_Grammatik`), plus the links added to the three level READMEs, the course README and the three checkpoints.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The user's specification of 2026-09-12 (exactly three recap sections; detailed, not a checklist; CEFR-appropriate progression; built out of the existing curriculum; fits the existing architecture; no new parallel structure; levels that do not exist are not invented); CP-002 as recorded in `01`; `04` format rules.
- **Method:**
  - Inventory first: the existing levels were read off the filesystem (A1, A2, B1 exist; **B2, C1, C2 do not exist and were not created**), and the sources of each section were located — vocabulary in the A1 unit `## 📚 Wortschatz` tables and the A2/B1 `### ★ Aktiver Kern` tables, phrases in `Resources/Redemittel.md` plus the per-unit Redemittel blocks, grammar in `Resources/Grammar_Tables.md` plus the unit explanations.
  - `check_structure.py` → 125 files, 0 problems
  - `check_links.py` → 1789 links, 0 broken, 3 planned (all three to the unwritten `B1-U07_Umwelt_und_Nachhaltigkeit/`)
  - `build_anki.py` → unchanged (A1 124 / A2 561 / B1 339): the recaps deliberately carry **no** flashcard tables, so they cannot duplicate the decks
  - manual reread: every article and plural checked against the unit word banks; every grammar table checked against `Resources/Grammar_Tables.md`; every phrase checked for naturalness and level
- **Findings:**
  1. `STR`, PASS. One folder per level inside the level's own folder, named like the existing `A1_Checkpoint.md` / `B1_Midpoint_Checkpoint.md` files; files numbered `00`–`03` like the unit folders' `00_Overview_und_Wortschatz.md`. No `Recaps/` root folder, no file moved, no existing structure changed.
  2. `STR`, PASS. **Exactly three** content sections per level — Wortschatz, Redemittel, Grammatik. `00_Overview.md` is navigation only (what the three sheets are, how to use them, what is deliberately absent) and adds no fourth category.
  3. `CEF`, PASS. Progression is real, not cosmetic: A1 = concrete everyday items, fixed phrases, one-clause grammar; A2 = topic vocabulary with Perfekt forms, phrases that give reasons and compare, the dative and subordinate clauses; B1 = **abstract nouns, collocations and verb-preposition patterns**, argumentation language, and the joining structures (relative clauses, Konjunktiv II, genitive, passive).
  4. `VOC`, PASS. Curated, not copied: each level's sheet groups the material into semantic categories and adds what a reference needs and a lesson does not — gender rules, plural patterns, the frequent-verb and frequent-adjective lists, word-formation tables, and at B1 a collocation table.
  5. `PED`, PASS. Each sheet states how to revise with it (cover the German, say it, 10–15-minute blocks, go back to the named unit) and ends in a self-test; nothing is presented as an exercise to be completed in the file.
  6. `LNG`, **Minor (fixed), 1 item:** *der Rat* was carried over from the A2-U10 word bank as *der Rat, ¨-e*; in the meaning "advice" it has no plural, so the recap now gives *der Rat (Sg., Pl. Ratschläge)*.
  7. `DEP`, PASS. Each sheet says what it assumes (A2 assumes A1, B1 assumes A1 and A2) and links to the level below instead of repeating it.
  8. `ASS`, PASS. The B1 recap is marked `status: in-progress` and carries a **Was noch fehlt** table listing U07–U12 and what each will add, so the sheet is honest about covering only B1.1 and is trivially extendable.
  9. `WRK`, PASS (estimate). A1 ≈ 2 300 words, A2 ≈ 3 400, B1 ≈ 3 900 across the three sheets — a reference, not a second curriculum.
- **Required changes:** None remaining.
- **Resolution:** The single `LNG` finding was fixed before the commit.
- **Result:** **PASS WITH NOTES** — the recap system is complete for every level that exists; B1 grows with B1.2.
- **Approval status:** CP-002 approved by the user (2026-09-12).

---

## V-017 — CP-003: die oberen Stufen B2, C1, C2 angelegt

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/README.md`, `C1/README.md`, `C2/README.md` and the three recap folders `B2/B2_Recap/`, `C1/C1_Recap/`, `C2/C2_Recap/` (4 files each: `00_Overview`, `01_Wortschatz`, `02_Redemittel`, `03_Grammatik`); the stage table and recap row in the course README; the forward link in `B1/README.md`; Docs 00/01/03/05/06.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** The user's request of 2026-09-13 ("advance this and extend the project to B2, C1, C2, written the same way"); CP-003 as recorded in `01`; the CP-002 recap shape (exactly three sheets plus a navigation overview); `04` format rules; CEFR descriptors for B2, C1 and C2.
- **Method:**
  - `check_structure.py` → 140 files, 0 problems
  - `check_links.py` → 1906 links, 0 broken, 3 planned (all three to the unwritten `B1-U07`)
  - `build_anki.py` → unchanged (A1 124 / A2 561 / B1 339): the new sheets deliberately carry no flashcard tables
  - manual reread of every German example; every grammatical claim checked against the structures it describes; register marks (⬇ / neutral / ⬆) checked for plausibility
- **Findings:**
  1. `STR`, PASS. The three new stages reuse the existing architecture exactly: a stage `README.md` plus a `<Level>_Recap/` folder with `00`–`03`. No new top-level structure, no file moved, no change to A1–B1.
  2. `STR`, PASS. **Exactly three** content sections per level, as in CP-002. No reading/writing/listening/speaking/culture/exam sheets were added.
  3. `CEF`, PASS. The progression is substantive, not cosmetic: **B2** = precision, compression (participles, nominal style, passive substitutes) and stance (Konjunktiv I, subjective modals, hedging); **C1** = choice between correct structures, connotation, cohesion, genre; **C2** = nuance, implicature, irony, rhythm, register mastery and editing. Each sheet opens with the CEFR descriptors for that level in summarised form.
  4. `PED`, **Honesty finding, resolved by design:** the B2/C1/C2 units do not exist, so these recaps cannot consolidate a course. Every file therefore carries `status: planned` and says in its header that it is built from the CEFR descriptors and will be consolidated when the units are written. The stage READMEs repeat this in a status block. The earlier instruction "do not pretend a recap is complete" is thereby honoured under the extended scope.
  5. `PED`, PASS. The C2 stage page states plainly that C2 is reached through volume, real stakes and feedback rather than through a course, and describes what a course can and cannot do. Nothing on that page promises what it cannot deliver.
  6. `LNG`, **Minor (fixed), 2 items:** a garbled cell in the B2 vocabulary table (*„plot · character |ic"*) was rewritten with a proper collocation; the part label in the B2 Redemittel header read *„Teil 1 von 3 → 2"* and was corrected to *„Teil 2 von 3"*.
  7. `VOC`, PASS. The upper-level word sheets are organised by **distinction**, not by topic list: connotation pairs, near-synonym ladders, register scales, metaphor fields, Nomen-Verb-Verbindungen, verb-prefix families, Amtsdeutsch for reading. This is what separates them from an enlarged B1 list.
  8. `ASS`, PASS (deferred). No assessment material was written for the new stages; the checkpoints are listed as planned in `03` under M9–M11, including the C2 portfolio-plus-defence decision.
  9. `WRK`, PASS (estimate). B2 ≈ 4 400 words across four files, C1 ≈ 4 600, C2 ≈ 4 800 — references, not curricula.
- **Required changes:** None remaining.
- **Resolution:** Both `LNG` findings were fixed before the commit.
- **Result:** **PASS WITH NOTES** — the upper stages exist as stage pages and recaps; the units are milestones M9–M11.
- **Approval status:** CP-003 approved by the user (2026-09-13).

---

## V-018 — M9 WP1: B2-U01 Identität & Gesellschaft, und der B2-Review-Stop

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/B2-U01_Identitaet_und_Gesellschaft/` (5 Dateien), die B2-Abschnitte in `Resources/Grammar_Tables.md`, `Redemittel.md`, `English_German_Interference.md`, `Pronunciation_Guide.md`, die Stufe B2 in `Learner_Workbook/Story_Bank.md`, `Resources/Anki/B2.tsv`, `tools/build_anki.py`, `Docs/03/04/05/06`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** M9-Kriterien in `03`; `04` v1.3 einschließlich der neuen Regel **A7.2**; CP-003; der Einheitenplan in `01` Appendix H.1; CEFR-B2-Deskriptoren.
- **Method:**
  - `check_structure.py` → 145 Dateien, 0 Probleme
  - `check_vocab.py B2-U01` → 31 ★, **0 unter 3** (nach Nachbesserung bei *beruhen auf* und *sich identifizieren mit*)
  - `check_links.py` → 1958 Links, 0 broken, 3 planned
  - `build_anki.py` → **`B2.tsv` neu, 61 Karten**; A1/A2/B1 unverändert
  - vollständige Wiederlesung aller deutschen Texte; jede Partizipform gegen ihre Auflösung als Relativsatz geprüft
- **Findings:**
  1. `STR`, PASS. Fünf Dateien in der bekannten Form (`00_Overview_und_Wortschatz`, `L1`–`L3`, `L4_Anwenden`), 9 bzw. 8 nummerierte Aktivitäten mit Zeitangaben, Karteikartentabelle in jeder Datei.
  2. **Review-Stop (wie bei A2-U01 und B1-U01 vorgesehen): PASS mit Standardänderung.** Die B2-Vorlage warf genau eine Grundsatzfrage auf — die Sprache der Erklärungen. Entschieden und als **`04` v1.3, Regel A7.2** festgeschrieben: ab B2 ist die Lektion einsprachig Deutsch; Ausnahmen bleiben nur die KI-Rollenspielblöcke, die englischen Prompts in Abruf- und Karteikartentabellen und die zitierten englischen Kalken in den Interferenzkästen.
  3. `PED`, PASS. Die Grammatik ist nicht additiv, sondern **transformativ** aufgebaut: L1 leitet das Attribut aus dem Relativsatz ab, L2 erweitert es und liefert die **Lesetechnik rückwärts**, L3 verschiebt den Fokus vom Bauen zum Abwägen. L2 enthält bewusst ein **stilistisch schlechtes, grammatisch korrektes** Beispiel und macht daraus die Lektion (Attribut ≠ immer besser).
  4. `CEF`, PASS. Lesetexte 340 / 200 / 330 / 520 Wörter, der Hauptkommentar in L4 mit klar erkennbarer Haltung; Hörtexte 3 × 90–120 Wörter mit unterschiedlichem Register; Schreibaufgabe 250–300 Wörter; Sprechziel 3 Minuten plus Podium.
  5. `SPK`, PASS. Jede Lektion: ⏱️-Abruf, KI-Rollenspiel, Zwei-Minuten-Monolog. L4 fordert das Podium **in beiden Rollen** und **Story Bank Task 1 auf B2**; dafür wurde die Stufe B2 im Story Bank ergänzt (alle acht Aufgaben, plus Spalte im Aufnahme-Log).
  6. `LNG`, **Minor (behoben), 2 Punkte:** fünf nummerierte Erklärungs-Zwischenüberschriften in L3 wurden zu einfachen H3 (sonst zählt der Checker sie als Aktivitäten); *beruhen auf* und *sich identifizieren mit* bekamen echte Übung statt bloßer Nennung (inkl. Hinweis auf *sich identifizieren **mit*** + Dativ gegen die englische Kalke *identify as*).
  7. `ASS`, PASS. Unit-Test mit 10 Items und Reparaturplan; Selbstcheck an den Einheitszielen; Workbook-Eintrag vorgesehen.
  8. `VOC`, PASS. 31 ★-Einträge, thematisch kohärent (Identität, Zugehörigkeit, Wandel) **und** grammatisch funktional: *zunehmend, wachsend, geltend, entscheidend, betroffen* sind zugleich die Partizipien, die die Einheit übt.
  9. `WRK`, PASS (Schätzung). 90 + 90 + 90 + 95 min = 365 min für die Einheit, konsistent mit Appendix J für die Oberstufe.
  10. `DEP`, PASS. „Wiederholt aus" nennt sieben frühere Einheiten bis zurück zu A1-U01; die Einheit setzt Relativsätze, Passiv und Adjektivendungen voraus und sagt das ausdrücklich.
- **Required changes:** Keine offen.
- **Resolution:** Beide `LNG`-Punkte vor dem Commit behoben; die Standardfrage wurde als A7.2 entschieden statt vertagt.
- **Result:** **PASS WITH NOTES** — M9 WP1 abgeschlossen, Review-Stop erledigt, B2-Vorlage freigegeben für U02–U12.
- **Approval status:** – (autonomous mode; Sequenzabweichung auf Nutzerwunsch)

---

## V-019 — M9 WP2 (Teil 1): B2-U02 Arbeitswelt & Karriere

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/B2-U02_Arbeitswelt_und_Karriere/` (5 Dateien), die B2-U02-Abschnitte in `Resources/Grammar_Tables.md`, `Redemittel.md`, `English_German_Interference.md`, `Pronunciation_Guide.md`, `Resources/Anki/B2.tsv`, `B2/README.md`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** M9-Kriterien in `03`; `04` v1.3 inkl. A7.2 (einsprachig Deutsch); Einheitenplan in `01` Appendix H.1; CEFR-B2-Deskriptoren; die in V-018 freigegebene B2-Vorlage.
- **Method:**
  - `check_structure.py` → 150 Dateien, 0 Probleme
  - `check_vocab.py B2-U02` → 32 ★, **0 unter 3** (nach Nachbesserung bei *einlenken / zusagen*)
  - `check_links.py` → 2010 Links, 0 broken, 3 planned
  - `build_anki.py` → `B2.tsv` **120 Karten** (U01 + U02); A1/A2/B1 unverändert
  - vollständige Wiederlesung; jedes Funktionsverbgefüge gegen Artikel, Präposition und Kasus geprüft; jede Nominalkonstruktion gegen ihre verbale Auflösung
- **Findings:**
  1. `STR`, PASS. Fünf Dateien in der Vorlagenform; 9/9/9/8 nummerierte Aktivitäten mit Zeitangaben; Karteikartentabelle in jeder Datei; durchgehend Deutsch nach A7.2.
  2. `PED`, PASS. Die Einheit ist um **eine** Idee gebaut: dieselbe Sache in zwei Registern. L1 liefert die Bausteine (Funktionsverbgefüge), L2 die Satzebene (Nominal ↔ Verbal), L3 die mündliche Anwendung (Kritik, Eskalation), L4 verbindet beides — Gespräch **und** Schriftstück zur selben Situation.
  3. `PED`, PASS. L2 enthält bewusst einen **korrekten, aber unlesbaren** Nominalsatz und macht die Stilkritik zur Aufgabe; L3 arbeitet mit drei Fassungen derselben Kritik (salopp/kollegial/Leitung), statt Höflichkeit zu behaupten.
  4. `CEF`, PASS. Lesetexte: Protokoll 260 Wörter, E-Mail-Paar 2 × 90, drei Gesprächsversuche 210, Fachartikel 480; Hörtexte 3 × 110–130 mit unterschiedlichem Register; Schreibaufgabe 250–300 Wörter (Eskalations-E-Mail); Sprechen: Konfliktgespräch in beiden Rollen plus 2-Minuten-Monolog.
  5. `SPK`, PASS. **Story Bank Task 5 auf B2** als Verhandlung statt Beschwerde, mit Vergleich zur B1-Aufnahme; drei KI-Rollenspiele, davon zwei mit vorgeschriebenem Gegenvorwurf, damit die Reaktion geübt wird.
  6. `LNG`, **Minor (behoben), 2 Punkte:** *einlenken* und *zusagen* waren nur genannt, nicht geübt → eigene Zeile in der Reaktionstabelle, Zusatzaufgabe und Quizeintrag ergänzt, mit der Unterscheidung *einlenken ≠ nachgeben* und *zusagen* als verbindlicher als *versprechen*. Im Fachartikel stand eine Konjunktiv-I-Form (*die andere kümmere sich*), obwohl Konjunktiv I erst B2-U03 ist → in den Indikativ geändert.
  7. `VOC`, PASS. 32 ★-Einträge; die Hälfte davon sind **Gefüge**, nicht Einzelwörter — genau die Lernform, die B2 verlangt. Kollokation, Artikel und Präposition stehen in der Tabelle.
  8. `ASS`, PASS. Unit-Test mit 10 Items und Reparaturplan; Selbstcheck; Workbook-Eintrag.
  9. `DEP`, PASS. „Wiederholt aus" nennt sieben frühere Einheiten; der Genitiv aus B1-U05 wird ausdrücklich als Voraussetzung des Nominalstils benannt.
  10. `WRK`, PASS (Schätzung). 90 + 90 + 90 + 95 = 365 min, wie B2-U01.
- **Required changes:** Keine offen.
- **Resolution:** Beide `LNG`-Punkte vor dem Commit behoben.
- **Result:** **PASS WITH NOTES** — B2-U02 abgeschlossen; M9 WP2 zu einem Drittel erledigt.
- **Approval status:** – (autonomous mode)

---

## V-020 — M9 WP2 (Teil 2): B2-U03 Bildung & Lernen

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/B2-U03_Bildung_und_Lernen/` (5 Dateien), die B2-U03-Abschnitte in `Resources/Grammar_Tables.md` und `Resources/Redemittel.md`, `Resources/Anki/B2.tsv`, `B2/README.md`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** M9-Kriterien in `03`; `04` v1.3 inkl. A7.2; Einheitenplan in `01` Appendix H.1; CEFR-B2-Deskriptoren; die in V-018 freigegebene B2-Vorlage.
- **Method:**
  - `check_structure.py` → 155 Dateien, 0 Probleme
  - `check_vocab.py B2-U03` → 32 ★, **0 unter 3** (nach Nachbesserung bei *die Stellungnahme* und *entgegenhalten / einwenden*)
  - `check_links.py` → 2063 Links, 0 broken, 3 planned
  - `build_anki.py` → `B2.tsv` **177 Karten** (U01–U03)
  - **zusätzlicher Scan des gesamten Kurses auf kyrillische und griechische Zeichen** (Regex über alle 155 Dateien) → nach der Korrektur **0 Treffer**
  - vollständige Wiederlesung; jede Konjunktiv-I-Form einzeln gegen die Ersatzregel geprüft
- **Findings:**
  1. `STR`, PASS. Fünf Dateien in der Vorlagenform; 9/9/9/8 nummerierte Aktivitäten mit Zeitangaben; Karteikartentabellen vollständig; durchgehend Deutsch nach A7.2.
  2. `PED`, PASS. Der Aufbau trennt konsequent **Form** (L1), **Text** (L2) und **Inhalt** (L3): L1 gibt die Formen und die Ersatzregel, L2 zeigt an zwei Fassungen desselben Vortrags, warum fünfmal *sie sagte* kein Referat ist, L3 liefert Bildungswortschatz plus Zahlenversprachlichung. L4 verlangt beides zugleich — erst referieren ohne Wertung, dann Position beziehen.
  3. `PED`, PASS. Die didaktische Kernidee der Einheit ist **die Trennung der Stimmen**: Konjunktiv I = Quelle, Indikativ = ich. Sie wird in L2 explizit gemacht, in L4 geprüft (Aufgabe 6 „Wer spricht?") und im Rollenspiel abgefragt („Ist das Ihre Meinung oder die des Autors?").
  4. `CEF`, PASS. Lesetexte: Meldung 300 Wörter, zwei Wiedergaben 2 × 90, drei Bildungswege 300, Artikel 520; Hörtexte 3 × 120–140; Schreibaufgabe 250–300 Wörter (Zusammenfassung mit abgetrenntem Bewertungsteil); Sprechen: Referat + Debatte in beiden Rollen.
  5. `SPK`, PASS. **Story Bank Task 3 auf B2** mit der neuen Anforderung „Erzählung ↔ Deutung markieren"; drei KI-Rollenspiele, jedes mit einer Frage, die der Text **nicht** beantwortet, damit *Dazu sagt der Text nichts* geübt wird.
  6. `LNG`, **Minor (behoben), 3 Punkte:** (a) In L4 stand in einem Sprechernamen eine **kyrillische Zeichenfolge** (*Brандt*) — korrigiert; der anschließende Scan des Gesamtkurses ergab keine weiteren Treffer. (b) *die Stellungnahme* und *entgegenhalten / einwenden* waren nur genannt → eigene Tabellenzeile, zwei Übungsitems und Quizeinträge ergänzt. (c) Ein Anker von L2 nach L1 zeigte auf eine Überschrift ohne Zeitangabe — korrigiert.
  7. `VOC`, PASS. 32 ★-Einträge in zwei funktionalen Gruppen: **Redeeinleitungsverben** (die Grammatik der Einheit) und **Bildungswortschatz** (das Thema). Zahlenausdrücke (*rund, knapp, gut, der Anteil, der Anstieg*) sind als eigene Gruppe aufgenommen, weil sie in L3 systematisch geübt werden.
  8. `ASS`, PASS. Unit-Test mit 10 Items und Reparaturplan; Selbstcheck an den Einheitszielen; Workbook-Eintrag.
  9. `DEP`, PASS. Sieben Rückverweise; der Kontrast Konjunktiv I ↔ Konjunktiv II (B1-U04) wird an drei Stellen ausdrücklich thematisiert, weil er die Hauptfehlerquelle ist.
  10. `WRK`, PASS (Schätzung). 90 + 90 + 90 + 95 = 365 min, wie B2-U01 und B2-U02.
- **Required changes:** Keine offen.
- **Resolution:** Alle drei `LNG`-Punkte vor dem Commit behoben.
- **Result:** **PASS WITH NOTES** — B2-U03 abgeschlossen; M9 WP2 zu zwei Dritteln erledigt.
- **Approval status:** – (autonomous mode)

---

## V-021 — M9 WP2 abgeschlossen: B2-U04 Medien & Öffentlichkeit und B2-R1

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/B2-U04_Medien_und_Oeffentlichkeit/` (5 Dateien), `B2/B2-R1_Wiederholung.md`, die B2-U04-Abschnitte in `Resources/Grammar_Tables.md` und `Resources/Redemittel.md`, `Resources/Anki/B2.tsv`, `B2/README.md`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** M9-Kriterien in `03`; `04` v1.3 inkl. A7.2; Appendix G (Wiederholungsspezifikation 50/30/20, drei Sitzungen); Einheitenplan in `01` Appendix H.1; CEFR-B2-Deskriptoren.
- **Method:**
  - `check_structure.py` → 161 Dateien, 0 Probleme
  - `check_vocab.py B2-U04` → 29 ★, **0 unter 3** (nach Nachbesserung bei *die Berichterstattung*)
  - `check_links.py` → 2137 Links, 0 broken, 3 planned
  - `build_anki.py` → `B2.tsv` **228 Karten** (U01–U04)
  - vollständige Wiederlesung; jede der acht Passivformen gegen ihre Rückübersetzung ins Passiv geprüft
- **Findings:**
  1. `STR`, PASS. B2-U04 in der Vorlagenform (5 Dateien, 9/9/9/8 Aktivitäten mit Zeitangaben, Karteikarten). B2-R1 folgt der Wiederholungsspezifikation aus Appendix G: **drei Sitzungen**, zwölf nummerierte Aufgaben, Gewichtung 50 % B2-U01–U04 / 30 % B1.1 / 20 % A2.
  2. `PED`, PASS. U04 ist bewusst als **System-Einheit** gebaut: L1 (Möglichkeit) und L2 (Pflicht) ergeben zusammen eine Tabelle mit **acht Formen, einer Bedeutung und acht Registern**; L3 macht daraus eine Anwendung (Faktencheck), L4 verbindet beides in einer Aufgabe mit zwei Adressaten.
  3. `PED`, PASS. Die Übung „Dasselbe dreimal" (L2, Aufgabe 8) verlangt denselben Sachverhalt für Team, Leitung und Vorschrift — das ist die Registerprüfung in ihrer schärfsten Form. L3 Aufgabe 8 („Das Gespräch am Küchentisch") übt ausdrücklich das **Nicht-Belehren**, was die häufigste Ursache für abgebrochene Gespräche ist.
  4. `REV` (B2-R1), PASS. Gewichtung ausgezählt: Aufwärmen 28 Items (7/8/8/5 aus U01–U04), Formen-Klinik 24 Items über alle vier Einheiten, Fehlerklinik 16 Fehler mit Fehlertyp, Test 20 Items. Dazu vier Sprechsituationen, Schreiben unter Zeitdruck, ein 4/3/2-Referat und ein Reparaturplan mit **Zwei-Auffrischungen-Regel**.
  5. `CEF`, PASS. U04: Lesetexte 260 / 2 × 120 / 300 / 560 Wörter; Hörtexte 3 × 120–150; Schreibaufgabe 250–300 Wörter. R1: vier Textsortenausschnitte, vier Hörminiaturen, 180–220 Wörter unter Zeitdruck.
  6. `SPK`, PASS. **Story Bank Task 7 auf B2** (Meinung **mit Beleglage**, inkl. der Angabe, wie gut jeder Beleg ist) und in R1 ein 4/3/2-Referat mit der didaktisch wichtigen Beobachtung, dass beim Kürzen zuerst die Belege verschwinden.
  7. `LNG`, **Minor (behoben), 2 Punkte:** *die Berichterstattung* war nur einmal verwendet → eigene Tabellenzeile und ein Übungspaar ergänzt. Beim Nachbessern per Skript wurde eine Tabellenzeile mehrfach eingefügt; das Duplikat wurde erkannt und entfernt (Prüfung: jetzt genau ein Vorkommen).
  8. `VOC`, PASS. 29 ★-Einträge, davon ein Drittel **Formen** statt Wörter (*sich lassen* + Infinitiv, *Es ist davon auszugehen, dass …*) — angemessen für eine Einheit, deren Lernziel ein grammatisches System ist.
  9. `ASS`, PASS. Unit-Test (10) und R1-Test (20), beide mit Reparaturplan auf Lektionsebene.
  10. `WRK`, PASS (Schätzung). U04 365 min; R1 170 min in drei Sitzungen, konsistent mit B1-R1.
- **Required changes:** Keine offen.
- **Resolution:** Beide `LNG`-Punkte vor dem Commit behoben.
- **Result:** **PASS WITH NOTES** — **M9 WP2 abgeschlossen** (U02, U03, U04, R1). B2 hat vier Einheiten und eine Wiederholung.
- **Approval status:** – (autonomous mode)

---

## V-022 — M9 WP3 (Teil 1): B2-U05 Wirtschaft & Konsum

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/B2-U05_Wirtschaft_und_Konsum/` (5 Dateien), die B2-U05-Abschnitte in `Resources/Grammar_Tables.md` und `Resources/Redemittel.md`, `Resources/Anki/B2.tsv`, `B2/README.md`.
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** M9-Kriterien in `03`; `04` v1.3 inkl. A7.2 (einsprachig Deutsch ab B2); Einheitenplan in `01` Appendix H.1; CEFR-B2-Deskriptoren (Aushandeln, Argumentieren, Einräumen).
- **Method:**
  - `check_structure.py` → **166 Dateien, 0 Probleme**
  - `check_vocab.py B2-U05` → **31 ★, 0 unter 3** (nach Nachbesserung bei *in Frage kommen*)
  - `check_links.py` → **2190 Links, 0 broken, 3 planned** (alle drei auf das noch ungeschriebene B1-U07)
  - `build_anki.py` → `B2.tsv` **281 Karten** (U01–U05)
  - vollständige Wiederlesung; jede Bedingungsform gegen ihre *wenn*-Entsprechung rückgeprüft, jede konzessive Form gegen die Wortstellungsregel
- **Findings:**
  1. `STR`, PASS. Vorlagenform eingehalten: `00_Overview_und_Wortschatz.md` + L1–L3 (je ~90 min, 8–9 nummerierte Aktivitäten mit Zeitangabe) + `L4_Anwenden.md` (Integration, ~95 min). Karteikartentabellen in allen vier Lektionen.
  2. `PED`, PASS. Die Einheit ist als **Paar** gebaut: L1 gibt die Bedingung, L2 die Einräumung — zusammen sind das die beiden Bewegungen jeder Verhandlung, die L3 dann als Fünf-Phasen-Modell operationalisiert und L4 in einer Aufgabe mit Zielkonflikt zusammenführt.
  3. `PED`, PASS. L2 trennt ausdrücklich das **echte Einräumen** (etwas Konkretes zugeben) vom rhetorischen *zwar … aber*, das nichts zugibt. Das ist der Punkt, an dem B2-Lernende sonst hängen bleiben.
  4. `LNG`, PASS. Die Registerübersicht zu *wenn / falls / sofern / soweit* nennt für jede Form eine Nuance statt sie als Synonyme zu behandeln; *es sei denn* ist korrekt mit **Hauptsatzstellung** dargestellt.
  5. `CEF`, PASS. Lesetext „Die Armutsprämie" 480 Wörter; drei Stimmen je 120–150 Wörter als Hörvorlage; Schreibaufgabe (Leserbrief) 250–300 Wörter; Vereinbarung 6–8 Sätze. Passend zu B2.2.
  6. `SPK`, PASS. **Story Bank Task 6 auf B2** („Etwas planen") ist bewusst mit **Zielkonflikt** angesetzt — der Unterschied zur B1-Aufnahme ist damit hörbar: Plan → Abwägung.
  7. `VOC`, **Minor (behoben):** *in Frage kommen* erreichte nur ein Vorkommen, weil alle Varianten typografisch aufgeteilt waren (`**kommt** … **in Frage**`) und die Prüfung auf die zusammenhängende Kleinschreibung testet. Behoben durch einen echten Erklärkasten in L3 (Bedeutung, Verneinungstendenz, Schreibung *in Frage / infrage*) und eine zusätzliche Reflexionsfrage in L4. Danach 0 unter 3.
  8. `ASS`, PASS. 10-Item-Test in L4 mit Reparaturkarte auf Lektionsebene.
  9. `WRK`, PASS (Schätzung). 4 Lektionen, zusammen ca. 365 min, konsistent mit U01–U04.
- **Required changes:** Keine offen.
- **Resolution:** Der `VOC`-Punkt wurde vor dem Commit behoben; die Nachbesserung ist inhaltlich (Erklärung + Aufgabe), nicht kosmetisch.
- **Result:** **PASS WITH NOTES** — B2-U05 ist Teil des Kurses. M9 WP3 läuft weiter mit U06.
- **Approval status:** – (autonomous mode)

---

## V-023 — M9 WP3 (Teil 2): B2-U06 Wissenschaft & Forschung

- **Date:** 2026-09-13
- **Object:** `GERMAN_LEARNING_PLAN/B2/B2-U06_Wissenschaft_und_Forschung/` (5 Dateien), die B2-U06-Abschnitte in `Resources/Grammar_Tables.md`, `Resources/Redemittel.md`, `Resources/English_German_Interference.md` und `Resources/Pronunciation_Guide.md`, `Resources/Anki/B2.tsv`, `B2/README.md`, `B2/B2_Recap/00_Overview.md` und `B2/B2_Recap/03_Grammatik.md` (§ 4 konsolidiert).
- **Validator:** Claude (autonomous mode; no learner trial)
- **Criteria:** M9-Kriterien in `03`; `04` v1.3 inkl. A7.2 (einsprachig Deutsch ab B2); Einheitenplan in `01` Appendix H.1; CEFR-B2-Deskriptoren (komplexe Argumentation verstehen, Standpunkte erkennen, Informationen aus Fachtexten zusammenfassen).
- **Method:**
  - `check_structure.py` → **171 Dateien, 0 Probleme**
  - `check_vocab.py B2-U06` → **40 ★, 0 unter 3** (ohne Nachbesserung)
  - `check_links.py` → **2232 Links, 0 broken, 3 planned** (alle drei auf das noch ungeschriebene B1-U07)
  - `build_anki.py` → `B2.tsv` **330 Karten** (U01–U06)
  - vollständige Wiederlesung; jede Stufe der Gewissheitsskala gegen ihre Adverb-Entsprechung geprüft; jede Vergangenheitsform gegen die Regel „Tempus am Vollverb“
- **Findings:**
  1. `STR`, PASS. Vorlagenform eingehalten: `00_Overview_und_Wortschatz.md` + L1–L3 (je ~90 min, 9 nummerierte Aktivitäten mit Zeitangabe) + `L4_Anwenden.md` (Integration, 8 Aktivitäten, ~95 min). Karteikartentabellen in allen vier Lektionen.
  2. `PED`, PASS. Die Einheit trennt bewusst **zwei Achsen**, die Lehrwerke meist vermischen: L1 = **Quelle** (*sollen*/*wollen*), L2 = **Sicherheit** (*muss … kann nicht*). Erst L4 bringt beide zusammen. Das erklärt, warum Lernende sonst *soll* und *dürfte* verwechseln: Sie liegen auf verschiedenen Achsen.
  3. `PED`, PASS. L3 ist keine Wortschatzliste, sondern eine **Denkoperation**: die vier Erklärungen für jeden Zusammenhang (A→B, B→A, Drittvariable, Zufall) und fünf benennbare Fehlschlüsse. Die Aufgabe „Der Faktencheck am Küchentisch“ verlangt ausdrücklich, einen Fehlschluss zu benennen, **ohne** das Wort *falsch* zu benutzen.
  4. `LNG`, PASS. Vier Adverbien, die im Englischen zusammenfallen, werden konsequent getrennt gehalten: *angeblich* (fremde Behauptung) · *vermeintlich* (trifft **nicht** zu) · *anscheinend* (Eindruck) · *offenbar* (belegt). Die Falle *dürfte nicht* = Verbot ist als eigene Fehlerzeile aufgenommen.
  5. `CEF`, PASS. Lesetext „Die Wiederholung, die keiner macht“ 430 Wörter mit sechs eigenen Abstufungen im Text (Aufgabe 4 verlangt, sie zu finden); drei Hörtexte je 110–140 Wörter; Schreibaufgabe 250–300 Wörter in fünf vorgegebenen Abschnitten.
  6. `SPK`, PASS. **Story Bank Task 2 auf B2** („Mein Alltag“) verlangt den Alltag als **Beispiel für eine größere Entwicklung** — mit einer ausdrücklichen Angabe, wofür er **kein** gutes Beispiel ist. Damit übt die Aufgabe genau den Fehlschluss, den L3 behandelt (Einzelfall als Beleg), an der eigenen Biografie.
  7. `VOC`, PASS. 40 ★-Einträge, alle beim ersten Lauf über der Schwelle. Ein Drittel sind **Formen und Adverbien** statt Nomen — angemessen für eine Einheit, deren Lernziel eine Haltung ist.
  8. `ASS`, PASS. 10-Item-Test in L4 mit Reparaturkarte auf Lektionsebene (1–4 → L1, 5–7 → L2, 8–10 → L3).
  9. `WRK`, PASS (Schätzung). 4 Lektionen, zusammen ca. 365 min, konsistent mit U01–U05.
  10. `DEP`, PASS. Der B2-Recap (§ 4 Subjektive Modalverben) wurde von der CEFR-Referenz auf die geprüfte Fassung aus U06 umgestellt; die Statuszeile des Recaps nennt jetzt korrekt **U01–U06** statt nur U01 und benennt, was weiterhin unkonsolidiert ist (Futur I/II, Modalpartikeln, Wortstellung zur Betonung).
- **Required changes:** Keine offen.
- **Resolution:** –
- **Result:** **PASS** — B2-U06 ist Teil des Kurses. M9 WP3 läuft weiter mit U07.
- **Approval status:** – (autonomous mode)

