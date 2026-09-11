# CLAUDE.md — German A1 → B1 Curriculum Project

This workspace holds a long-running project: a CEFR-aligned German course from A1/A2 to the end of B1, written as Markdown and built over many sessions in milestones.

- **`Docs/` is the authoritative project and build source of truth.** If anything (including this file or chat history) disagrees with `Docs/`, `Docs/` wins.
- **The course itself lives in `GERMAN_LEARNING_PLAN/`.** It is learner-facing and never links into `Docs/`.

## Start of every session

1. **Read `Docs/00_PROJECT_STATE.md` first.** It gives the current milestone, status, open decisions and next action.
2. Read the relevant parts of:
   - `Docs/01_CURRICULUM_DECISIONS.md`: approved architecture (decisions CD-xx, Appendices A–J, change control)
   - `Docs/02_DESIGN_PRINCIPLES.md`: the design constitution
   - `Docs/03_MILESTONES.md`: scope, deliverables and validation criteria per milestone
   - `Docs/04_LESSON_STANDARDS.md`: how every lesson file is built and checked
   - `Docs/05_VALIDATION_LOG.md`: what has been validated and approved
3. **Check the current milestone before doing any work.**

## Rules

- **Work only on the current milestone.** Never start the next one on your own.
- **Never generate the entire curriculum in one operation.** Build in milestones and work packages.
- Follow **Design → Build → Validate → Approve → Scale.** Pilot before scaling.
- **Never silently change the approved architecture.** Use change control at the end of `Docs/01`: problem → reason → proposal → register entry → user approval → apply.
- **Record important changes** in `Docs/06_CHANGELOG.md` and validations in `Docs/05_VALIDATION_LOG.md`. Record only validations that actually happened.
- **Update `Docs/00_PROJECT_STATE.md` after meaningful work**, including after each work package, so the project can always be resumed from the filesystem.
- **When the current milestone is complete:**
  1. Update `00`, `03` and `06`.
  2. Validate and log the validation in `05`.
  3. Summarise what was created and list open issues.
  4. Commit.
  5. **STOP and wait for explicit user approval.**
- Commit with clear messages at milestone and work-package boundaries. Do not rewrite history.
