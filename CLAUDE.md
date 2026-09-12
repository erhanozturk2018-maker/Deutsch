# CLAUDE.md — German A1 → B1 Curriculum Project

This workspace holds a long-running project: a CEFR-aligned German course from A1/A2 to the end of B1, written as Markdown and built over many sessions in milestones.

- **`Docs/` is the authoritative project and build source of truth.** If anything (including this file or chat history) disagrees with `Docs/`, `Docs/` wins.
- **The course itself lives in `GERMAN_LEARNING_PLAN/`.** It is learner-facing and never links into `Docs/`.
- **`tools/`** holds maintained helper scripts. Run them at every batch boundary:
  - `check_links.py`: links and anchors
  - `check_structure.py`: `04` format rules
  - `build_anki.py`: regenerates `Resources/Anki/*.tsv` from the lesson flashcard tables
  - `check_vocab.py <unit folder>`: are the ★ words really practised (≥3 times) in L1–L4?

## Start of every session

1. **Read `Docs/00_PROJECT_STATE.md` first.** It gives the current milestone, batch, status, open decisions and the exact next task.
2. Read the relevant parts of:
   - `Docs/01_CURRICULUM_DECISIONS.md`: approved architecture (decisions CD-xx, Appendices A–J, change control)
   - `Docs/02_DESIGN_PRINCIPLES.md`: the design constitution
   - `Docs/03_MILESTONES.md`: scope, deliverables, validation criteria, work packages
   - `Docs/04_LESSON_STANDARDS.md`: how every course file is built and checked
   - `Docs/05_VALIDATION_LOG.md`: what has been validated
   - `Docs/06_CHANGELOG.md`: history
3. **Determine the current milestone from the filesystem.** Never rebuild a milestone marked COMPLETE. Resume at the recorded next task.

## Rules

- **Never generate the entire curriculum in one operation.** Follow **Design → Build → Validate → Correct → Record → Commit → Continue**, by milestone and work package. Pilot before scaling.
- **Autonomous mode (authorised by the user on 2026-09-11 for M2 → M8).**
  - After a milestone or batch: validate, record, commit, push, then continue with the next one without waiting for approval.
  - Stop only if:
    - a genuine architectural contradiction makes continuing unsafe
    - a required resource is unavailable and cannot be substituted
    - the filesystem becomes inaccessible
    - a decision would fundamentally change the approved architecture
  - For non-blocking uncertainties: make the most defensible choice, record it in `Docs/`, continue.
- **Never silently change the approved architecture.** Use change control at the end of `Docs/01`. Changes to `04` standards are recorded in `06` with the reason.
- **Record** changes in `Docs/06_CHANGELOG.md` and validations in `Docs/05_VALIDATION_LOG.md`. Record only validations that actually happened. Never invent learner results.
- **Update `Docs/00_PROJECT_STATE.md` at every milestone or batch boundary**: current milestone and batch, completed work, the exact next task, decisions, open issues.
- **Context limits.** Before the conversation gets too long: save state to `Docs/` (00, 03, 06), commit, record the exact next file or task, then stop. A new session resumes from `CLAUDE.md` + `Docs/`.

## Git

- Commit at milestone and batch boundaries with meaningful messages. Never commit temporary scripts or junk.
- **Never add `Co-Authored-By`, "Generated with …" or any other AI-attribution lines to commit messages** (user instruction, 2026-09-11). Authorship attribution is the user's decision.
- **Do not push (user instruction, 2026-09-12).** Commit at every batch boundary and stop there; **the user pushes to `origin main` themselves**. Never force-push. If the user later asks for pushes again, resume pushing after each commit.
