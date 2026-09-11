# 02 — Design Principles

> **The design constitution.** Every file in the course must follow these principles. This is not a project log: keep it short and stable.
> Architecture-specific decisions (which unit teaches what, thresholds, file layout) live in [01_CURRICULUM_DECISIONS.md](01_CURRICULUM_DECISIONS.md).
>
> **Version:** 1.0 (2026-09-11). **Amendments:** only with explicit user approval, recorded in [06_CHANGELOG.md](06_CHANGELOG.md).

Each principle has three parts:
- **Rule**: what must hold.
- **In practice**: how it shows up in the files.
- **Red flag**: what a violation looks like.

---

### 1. Production over recognition
- **Rule:** The learner produces German far more often than they recognise it.
- **In practice:** Prompts give a meaning or situation and ask for German. German → English only for checking comprehension.
- **Red flag:** A lesson that is mostly reading examples and ticking boxes.

### 2. Active retrieval: recall before you check
- **Rule:** The learner pulls German from memory before seeing the answer.
- **In practice:** Answers live in `<details>` blocks. Every lesson starts with the 3-2-1 warm-up. Flashcards are production-direction.
- **Red flag:** The solution is printed directly under the question.

### 3. Spiral learning
- **Rule:** Structures and words come back in harder contexts until they are used spontaneously (recognise → controlled → in context → spontaneous).
- **In practice:** Each unit's tasks require earlier structures listed in the grammar spiral (`01`, Appendix D).
- **Red flag:** A topic taught once and never needed again.

### 4. Task-based learning
- **Rule:** Language is used to get something done.
- **In practice:** Every unit ends with a realistic task that needs the unit's language. Lessons contain smaller tasks.
- **Red flag:** "Write five sentences using the dative" is the communicative part of the lesson.

### 5. Communicative progression
- **Rule:** New language moves from discovery to controlled practice to guided production to a communicative task to free production.
- **In practice:** Input first (dialogue or text), then the pattern, then practice that gets steadily more open.
- **Red flag:** An explanation first, followed by drills only.

### 6. Prerequisite-based sequencing
- **Rule:** Nothing is taught before what it depends on.
- **In practice:** Check the dependency graph (`01`, Appendix C). List prerequisites with links in every lesson header.
- **Red flag:** A lesson requires a structure that is scheduled for a later unit (unless it is marked as a chunk).

### 7. Progressive reduction of scaffolding
- **Rule:** Support shrinks as proficiency grows.
- **In practice:** Phrases are given early; later only a goal is given. Instruction language moves to German in B1.
- **Red flag:** B1 tasks that still tell the learner which phrases to use.

### 8. Vocabulary: useful, frequent, reusable, and recycled
- **Rule:** Every item has a reason to be there, and it comes back.
- **In practice:** Chunks and collocations, not lone words. Nouns with article and plural. A "Recycled from" list in every unit. Tasks that need older words.
- **Red flag:** Long exhaustive lists; words that appear in one unit only.

### 9. Realistic, natural German
- **Rule:** Examples are things a German speaker would really say or write.
- **In practice:** Register tags `[spoken]` `[written]` `[formal]` `[informal]` `[uncommon]`. Correct-but-unnatural sentences are flagged. Colloquial reality is named.
- **Red flag:** Stiff textbook sentences presented as normal speech.

### 10. Grammar serves communication
- **Rule:** Grammar is taught because a task needs it, and explained intuitively.
- **In practice:** Chunks first, system later. The 10-point explanation for major topics. Terminology only when it helps. No rare exceptions before they are useful.
- **Red flag:** A lesson that is mainly a grammar table.

### 11. Speaking must become spontaneous
- **Rule:** Speaking moves from scripted to timed to unscripted.
- **In practice:** Every lesson has speaking. Every unit has a timed or unscripted activity. Story Bank, 4/3/2 retelling, role-plays, talking around missing words.
- **Red flag:** Speaking tasks that are only reading a written text aloud.

### 12. Review must include older material
- **Rule:** Review reaches back beyond the last lesson.
- **In practice:** 3-2-1 warm-ups; cumulative reviews weighted 50/30/20; error clinic.
- **Red flag:** A review that covers only the unit before it.

### 13. Retention over coverage
- **Rule:** Better fewer topics used well than many topics seen once.
- **In practice:** When a lesson is too full, cut coverage, never retrieval or speaking time.
- **Red flag:** Adding "one more" grammar point to fill a unit.

### 14. Variety over routine
- **Rule:** Activity types rotate. Tasks get more open with level.
- **In practice:** Rotate role-plays, info gaps, problem-solving, ranking, story reconstruction, error correction, paraphrasing, prediction, debates, simulations and so on.
- **Red flag:** Every lesson uses the same exercise sequence.

### 15. Integrated skills
- **Rule:** Listening, reading, writing and pronunciation are part of normal lessons, not separate courses.
- **In practice:** Aussprache-Minute uses lesson words; listening via TTS and task sheets; writing as real text types with the correct–rewrite–log loop.
- **Red flag:** A standalone phonetics drill unrelated to the lesson.

### 16. English as a tool, not a crutch
- **Rule:** English explains; German must become its own system.
- **In practice:** Flag interference where it causes real errors (false friends, prepositions, word order, *seit* + present). Don't compare everything to English.
- **Red flag:** Every German sentence explained through its English structure.

### 17. Manageable load
- **Rule:** Difficulty follows a rhythm, and lesson length is realistic.
- **In practice:** Lessons of 60–90 minutes. Heavy units followed by lighter ones. New concept → practice → consolidation → integration → review.
- **Red flag:** Three heavy lessons in a row with no consolidation.

### 18. Do not create unnecessary files
- **Rule:** One file = one meaningful study session or one meaningful reference.
- **In practice:** Follow the file architecture (`01`, Appendix H). Extend existing resource files instead of creating new ones.
- **Red flag:** Micro-files, duplicate references, files nobody links to.

### 19. Do not silently change architectural decisions
- **Rule:** Architecture changes only through the change-control procedure in `01`.
- **In practice:** Problem → explanation → proposal → register entry → user approval → apply → changelog.
- **Red flag:** A unit quietly teaches a different grammar topic than Appendix B says.

---

## File-level check (apply before marking any course file done)

- [ ] Header with level, prerequisites (linked), time, load
- [ ] Most practice is production; answers hidden in `<details>`
- [ ] Recycles earlier material, including older than the last unit
- [ ] Contains a realistic task and a speaking activity
- [ ] German examples sound natural; register tags where useful
- [ ] Typical mistakes (with English interference where relevant)
- [ ] Links resolve; nothing references a structure not yet taught (except marked chunks)
- [ ] Matches the unit map (`01`, Appendix B); no unapproved scope change
