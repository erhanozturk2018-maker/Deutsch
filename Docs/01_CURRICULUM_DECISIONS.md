# 01 — Curriculum Decisions

> **Purpose:** The binding architectural and pedagogical decisions of the curriculum, with the reasons behind them. Future sessions must preserve these decisions. To change one, follow **[Change control](#change-control)** at the end of this file.
>
> **Baseline:** Architecture **v1.0**, the Phase 1 blueprint, approved by the user on 2026-09-11.
>
> **Authority:** This file and its appendices are the **authoritative record** of the approved architecture. The original blueprint text exists only in the chat history of session 1. Anything binding from it has been captured here; if a detail is not in this file, it is not binding. Learner-facing documents (e.g. `GERMAN_LEARNING_PLAN/00_Curriculum/02_Curriculum_Map.md`) must be derived from this file. If they ever disagree, this file wins until a change is approved.

## How to read an entry

Each decision has an ID (`CD-xx`) and three parts:
- **Decision**: what was decided.
- **Reason**: why it was designed this way.
- **Consequence**: what it means for the files you build.

## Contents

- [A. Goal and learner](#a-goal-and-learner) (CD-01 to CD-03)
- [B. Core pedagogy](#b-core-pedagogy) (CD-04 to CD-12)
- [C. Grammar sequencing](#c-grammar-sequencing) (CD-13 to CD-24)
- [D. Vocabulary](#d-vocabulary) (CD-25 to CD-27)
- [E. Skills](#e-skills) (CD-28 to CD-33)
- [F. Review and assessment](#f-review-and-assessment) (CD-34 to CD-36)
- [G. Structure and build process](#g-structure-and-build-process) (CD-37 to CD-43)
- [Appendices A–J: architecture baseline reference](#appendices--architecture-baseline-v10-reference)
- [Change control](#change-control)

---

## A. Goal and learner

### CD-01: The goal is functional B1, not topic coverage
- **Decision:** Success means the learner can understand and produce German independently at about B1 level in everyday, social, practical and moderately abstract situations. Grammar and vocabulary coverage are means, not goals.
- **Reason:** This is the user's explicit primary goal. Covering a topic is not mastering it.
- **Consequence:** Every unit ends in a communicative task. Checkpoints test performance, not topic knowledge. A structure counts as "done" only when it reaches spontaneous use (tracked in the Progress Tracker). When space or time is tight, cut coverage; never cut retrieval or speaking practice.

### CD-02: A1 is gated consolidation, not a restart
- **Decision:** A1 is called **"Fundament"**: 5 compact units, one file each. Every unit opens with a 10-minute **Schnelltest** (quick test) that routes the learner:
  - **≥85% and fast:** do only the speaking/fluency task.
  - **60–84%:** do only the sections the test flagged.
  - **<60%:** do the full unit.

  An **A1 Gate** checkpoint must be passed before A2.
- **Reason:** The learner already has A1 and partial A2. Re-teaching from zero wastes time and motivation. The real A1 deficit is **retrieval speed**, not missing knowledge.
- **Consequence:**
  - A1 files are *not* beginner lessons. Explanations are short "refresh" explanations; the files are heavy on timed retrieval and fluency.
  - Every A1 section needs a label the Schnelltest can route to.
  - Nothing may assume zero prior knowledge.
  - If the diagnostic shows solid A2, A1 can shrink to the Gate test only.

### CD-03: The diagnostic measures accuracy and speed
- **Decision:** The entry diagnostic (built in M2) contains:
  - a can-do self-assessment
  - about 40 grammar-in-context **production** items, each mapped to a unit
  - about 40 vocabulary retrieval items (meaning/situation → German)
  - a **timed fluency check**
  - reading
  - 3 writing prompts of rising level (A1 note, A2 email, B1 opinion)
  - 6 recorded speaking prompts
  - an optional listening part (via TTS or an external source)

  It produces a route through A1 and a list of weak areas.
- **Reason:** The working hypothesis is that the learner is receptive about A2-, productive about A1+, which is a recognition–production gap. Recognition tests overrate such learners. A correct answer that takes 8 seconds is knowledge, not a working skill.
- **Consequence:**
  - Multiple choice is not the main format; items require production.
  - Timing thresholds are defined.
  - Each item is tagged with the unit or section it routes to.
  - Results are recorded in `Learner_Workbook/Progress_Tracker.md` and summarised in `Docs/00_PROJECT_STATE.md` (learner profile).

---

## B. Core pedagogy

### CD-04: Production over recognition
- **Decision:** Most practice runs **meaning → German**, and later **situation → German**. German → English is used only to check comprehension.
- **Reason:** The learner's stated problem is going from "I recognise this word" to "I can retrieve it while speaking".
- **Consequence:**
  - Flashcards are production-direction.
  - Exercises are cued by an English meaning, a situation, a scene description, or a first-letter prompt.
  - Answers are hidden in `<details>` so recall comes before checking.
  - A lesson that is mostly reading and recognising is not acceptable.

### CD-05: The Sentence Map (Satzklammer) is the backbone of the grammar
- **Decision:** One positional model is introduced in A1-U01:

  | Vorfeld | Pos. 2 (Verb 1) | Mittelfeld | Satzende (Verb 2) |
  |---|---|---|---|
  | Heute | muss | ich meine Mutter | anrufen. |
  | Gestern | habe | ich meine Mutter | angerufen. |
  | *(empty)* | weil | ich meine Mutter | anrufen muss. |

  In a verb-final clause the conjunction (*weil, dass, wenn* …) takes the Position-2 seat, so the whole verb cluster moves to the Satzende. (This example row was corrected on 2026-09-11; the original row wrongly put *weil* in the Vorfeld. See `06` [005].)

  Every verb structure taught later is presented as a new way of filling this same map: separable verbs, modals, Perfekt, verb-final clauses, relative clauses, zu-infinitive, future, passive, Konjunktiv II.
- **Reason:** German word order is one system. Learners who learn it as separate rules fall apart under time pressure. English SVO order, which keeps verbs together, is the main interference, and one visual model counters it best. Each new structure then feels like an extension of the model, not a new rule.
- **Consequence:**
  - `Resources/Sentence_Map.md` is a core shared resource. It must exist before the first lesson that uses it (A1-U01; see `03_MILESTONES.md` for the milestone that creates it).
  - Every lesson that introduces a verb structure shows it in this table format and links to that resource.
  - The table format must stay identical across all files.

### CD-06: Chunks first, system later (grammar serves communication)
- **Decision:** High-value forms are taught as fixed chunks before their grammar, for example:
  - *mit dem Bus, zum Bahnhof* before the dative
  - *im Park / in den Park* before two-way prepositions
  - *ich hätte gern, könnten Sie* before Konjunktiv II

  Later, the system explains what the learner already says.
- **Reason:** Communication needs these forms long before the system can be learned. Systematising known chunks is easier and more motivating than learning abstract tables first.
- **Consequence:** Early units mark such chunks "use now, explained in [unit]" with a forward link. The "Discover" section of the later unit starts from those chunks and links back.

### CD-07: Spiral learning with four stages
- **Decision:** Every important structure moves through **recognise → controlled → in context → spontaneous**. It reappears in later units until it reaches the spontaneous stage. [Appendix D](#appendix-d--grammar-spiral) defines where each structure is introduced, consolidated and demanded.
- **Reason:** Covering is not mastering. Retention needs repeated meetings in new contexts.
- **Consequence:**
  - Later units must **require** earlier structures in their tasks, not just mention them.
  - Before writing a unit, the builder checks Appendix D to see what it must recycle.
  - Review files update the stage per structure in the Progress Tracker.

### CD-08: Task-based units
- **Decision:** Every unit ends with a realistic main task that cannot be completed without the unit's language. Individual lessons also contain smaller tasks.
- **Reason:** The goal is communication. Tasks create the need that makes grammar meaningful.
- **Consequence:** Each unit's main task is fixed in [Appendix B](#appendix-b--unit-map). The unit's `L4_Anwenden.md` is built around it.

### CD-09: Communicative progression inside lessons
- **Decision:** Lessons follow the principle **Discover (input first) → controlled practice → guided production → communicative task → free production**. This is not a rigid five-section format.
- **Reason:** It moves the learner from noticing a form to using it spontaneously. Input-first discovery gives better understanding than explanation-first.
- **Consequence:** New-content lessons open with a dialogue or text in which the learner spots the pattern *before* the explanation. Activities become more open towards the end of each lesson and each unit.

### CD-10: Scaffolding is reduced, including the instruction language
- **Decision:**

  | Stage | Task instructions | Grammar explanations |
  |---|---|---|
  | A1, A2 | English | English |
  | B1.1 | Simple German with English support | English |
  | B1.2 | German | English, with German key terms |

  Tasks also shift from "use these phrases" to "achieve this goal".
- **Reason:** Independence. A B1 learner should operate in German.
- **Consequence:** B1 lesson files differ from A2 files, so the B1 variant of the template needs its own validation (see `03_MILESTONES.md`, M6 work package 1).

### CD-11: Realistic German with register tags
- **Decision:** Examples are tagged `[spoken]` `[written]` `[formal]` `[informal]` `[uncommon]`. Sentences that are correct but unnatural are flagged. Colloquial realities are named. Example: *weil* + verb-second order (*weil ich hab keine Zeit*) is common in speech but wrong in writing.
- **Reason:** The learner wants natural communication. Textbook German misleads.
- **Consequence:** This tag set is fixed; do not invent new tags without updating `02_DESIGN_PRINCIPLES.md` and the templates. Every example must be something a German speaker would plausibly say or write.

### CD-12: English interference is targeted, not constant
- **Decision:** When relevant, flag English interference: false friends (*bekommen, also, will, Chef, Handy, sensibel, aktuell*…), preposition differences, word order, tense use (*seit* + present tense), *Mir ist kalt*, the missing progressive, *kennen/wissen/können*. Do **not** compare everything to English.
- **Reason:** Interference is real for an English speaker, but German must become an independent system in the learner's mind.
- **Consequence:** Every lesson's "Typical mistakes" section flags the relevant interference. The central list `Resources/English_German_Interference.md` grows with each milestone.

---

## C. Grammar sequencing

### CD-13: Perfekt comes before full Präteritum
- **Decision:**

  | Where | What |
  |---|---|
  | A1-U05 | Perfekt, recognition only |
  | A2-U01 | Perfekt, full control |
  | A1 | *war/hatte* |
  | A2-U05 | Präteritum of modal verbs |
  | B1-U01 | Full Präteritum, together with Plusquamperfekt |

- **Reason:** Perfekt is the spoken past tense. It closes the biggest A1→A2 communication gap and reuses the bracket the learner already has. Full Präteritum is mainly needed for reading narratives, which is a B1 need.
- **Consequence:** A2 narration uses Perfekt plus *war/hatte* and modal Präteritum (the natural spoken mix). B1-U01 teaches the written/spoken distinction explicitly.

### CD-14: Dative comes before two-way prepositions
- **Decision:** The dative system is taught in A2-U02; two-way prepositions follow in A2-U03.
- **Reason:** Location vs direction only makes sense once accusative and dative are both solid. Many learners fail two-way prepositions because they meet them too early.
- **Consequence:** A2-U03 may assume the dative article and pronoun system without re-teaching it.

### CD-15: *weil/dass* come early (A2-U04)
- **Decision:** Verb-final clauses start in A2-U04 with *weil, dass, denn* and opinion starters.
- **Reason:** Giving reasons adds a lot of communicative value for little morphology; the only new thing is verb-final order, which the Sentence Map already prepares.
- **Consequence:** From A2-U04 on, every unit's tasks demand reasons and justifications.

### CD-16: *wenn* in A2, *als vs wenn* in B1
- **Decision:** *wenn* (condition, repeated time) comes in A2-U05. The contrast *als vs wenn* comes only in B1-U01.
- **Reason:** The *als/wenn* contrast belongs with past narration. At A2 the learner narrates with Perfekt and time words.
- **Consequence:** A2 files must not require temporal *als*. It may appear in A2 texts as recognition only.

### CD-17: Adjective endings in three stages
- **Decision:**

  | Stage | Unit | Scope |
  |---|---|---|
  | 1 | A2-U06 | Nominative/accusative after *der-* and *ein-* words |
  | 2 | B1-U02 | Dative and forms without an article |
  | 3 | B1-U05 | Genitive |

- **Reason:** The full table at once overwhelms learners. Endings automate slowly.
- **Consequence:** The accuracy target is "understandable by B1", not error-free. Adjective-ending errors should not fail a speaking task unless communication breaks down.

### CD-18: Relative clauses come early in B1 (B1-U02)
- **Decision:** Relative clauses (nominative, accusative, dative, with prepositions) come in B1-U02, before Konjunktiv II and the passive.
- **Reason:** They unlock **describing things you don't know the word for** (*ein Ding, mit dem man…*). That is the key strategy for spontaneous speaking.
- **Consequence:** From B1-U02 on, word-finding tasks such as Taboo and paraphrasing are a regular speaking activity.

### CD-19: Konjunktiv II moves from chunks to the full system
- **Decision:**

  | Stage | Where | What |
  |---|---|---|
  | Chunks | A1–A2-U07 | *möchte, hätte gern, könnten Sie, würde gern* |
  | Advice and wishes | A2-U10 | *würde, könnte, solltest* |
  | Full hypothetical | B1-U04 | Unreal *wenn*-clauses, wishes, polite forms |
  | Past | B1-U10 | *hätte … gemacht, wäre … gegangen*; *hätte … sollen* as a chunk |

- **Reason:** This is a classic spiral. The forms are useful long before the system can be learned.
- **Consequence:** A2-U10 must not teach full unreal conditionals. B1-U04 builds on the known chunks.

### CD-20: *werden* is one verb with three uses
- **Decision:** Full verb (*Ich will Ärztin werden*, A2-U08) → future (introduced A2-U09, full B1-U09) → passive (B1-U06; with modals B1-U06/U11).
- **Reason:** Presenting it as one verb with three uses reduces confusion. The passive depends on all earlier verb forms.
- **Consequence:** The B1-U06 explanation explicitly connects all three uses.

### CD-21: Late or recognition-only structures, and exclusions
- **Decision:**
  - Genitive: B1-U05, mainly written.
  - Konjunktiv I: recognition only, B1-U11 (news).
  - Zustandspassiv (*ist geöffnet*): recognition only, B1-U11.
  - Excluded before the end of B1: extended participial attributes, Konjunktiv I production, rare exceptions.
- **Reason:** These are low-frequency in speech. Time is better spent on communication.
- **Consequence:** Do not add excluded structures. If a text contains one, gloss it; don't teach it.

### CD-22: Modal particles spiral
- **Decision:**
  - A1: *mal*
  - A2: *doch, denn, ja* (focus on *doch* in A2-U09)
  - B1: *halt, eben, eigentlich, wohl* (focus in B1-U08)
- **Reason:** Particles are essential for natural spoken German but are only learnable once the basic grammar is in place.
- **Consequence:** Examples should use particles naturally from A2 on. Tag them `[spoken]` where relevant.

### CD-23: Verbs with prepositions
- **Decision:** Reflexive verbs (A2-U05) → verbs + prepositions and *wo-/da-* words, introduction (A2-U08) → *da-* word + clause (*Ich freue mich darauf, … zu …*) (B1-U03).
- **Reason:** This is the dependency chain. *da-* + clause needs the zu-infinitive, which comes in B1-U03.
- **Consequence:** `Resources/Verb_Lists.md` holds the growing verb + preposition list. It is recycled in reviews.

### CD-24: Standard for grammar explanations
- **Decision:** For every major grammar topic, the explanation covers 10 points: (1) what it means, (2) why it exists, (3) when Germans use it, (4) how it is formed, (5) word order, (6) common patterns, (7) common mistakes, (8) important exceptions, (9) how it differs from earlier structures, (10) real communicative use. Minor topics get lighter treatment.
- **Reason:** User requirement; intuitive understanding before rules.
- **Consequence:** The lesson template includes this as a checklist. Avoid unnecessary terminology; introduce a term only when it helps.

---

## D. Vocabulary

### CD-25: Selection by usefulness, frequency and reuse
- **Decision:** Vocabulary is chosen for being useful, frequent and reusable, never for completeness. Size targets are in [Appendix E](#appendix-e--vocabulary-targets). Each unit's word bank (in `00_Overview_und_Wortschatz.md`) contains:
  - ★ core items the learner must be able to say
  - recognition items
  - verb + collocation pairs (*eine Entscheidung treffen, Zeit verbringen, einen Termin vereinbaren*)
  - chunks and sentence frames
  - prepositions attached to words (*Angst vor, stolz auf*)
  - functional phrases (Redemittel)
  - a "Recycled from" list

  Nouns are always given as article + noun + plural (*die Wohnung, -en*). Gender clues from word endings are taught in A1-U02.
- **Reason:** User requirement: useful + frequent + reusable, not exhaustive.
- **Consequence:** Every word-bank item must be needed by at least one task in its unit. Isolated word lists without chunks or collocations are not acceptable.

### CD-26: Vocabulary recycling is built in
- **Decision:** Each unit lists the older vocabulary its tasks require. Tasks are designed to need earlier vocabulary; for example, the B1 environment unit needs A2 shopping and transport words. Cumulative reviews weight material 50% recent block, 30% previous block, 20% older.
- **Reason:** Retention needs spaced re-encounter. Words not met again are lost.
- **Consequence:** The builder checks the earlier units' word banks when writing tasks. The M8 audit checks recycling explicitly.

### CD-27: Rotation of retrieval drills
- **Decision:** Retrieval activities rotate between:
  - situation → phrase
  - first-letter gap-fill
  - Taboo-style describing
  - 60-second word lists ("everything in a kitchen")
  - collocation completion (*eine Entscheidung ___*)
  - paraphrasing
  - "say it three ways"
  - blank-page recall

  Word formation (compounds, prefixes, suffixes) is taught gradually as a way to guess meanings, and formally in B1-U09.
- **Reason:** Variety keeps motivation up and trains different retrieval routes.
- **Consequence:** No lesson relies only on "memorise this list, then write five sentences".

---

## E. Skills

### CD-28: Speaking is a major priority
- **Decision:** Speaking follows the progression in [Appendix F](#appendix-f--skills-progression). The main techniques are:
  - **4/3/2 retelling**: tell the same story in 4, then 3, then 2 minutes (at A2 scaled down to 2/1.5/1)
  - **shadowing**: repeat audio aloud just behind the speaker
  - self-talk and narrating your day
  - weekly self-recording, reviewed with a checklist
  - **AI role-play prompts** for the learner to paste into an AI app, voice mode preferred, with *delayed* correction (errors listed at the end, not mid-sentence)
  - photo description using the learner's own phone photos
  - question-generation drills
  - "What would you do?" scenarios
  - timed opinions
- **Reason:** The user's top priority is spontaneous speaking. Retrieval under time pressure is what turns knowledge into skill.
- **Consequence:**
  - Every lesson contains speaking.
  - Every unit contains at least one timed or unscripted speaking activity.
  - AI role-play prompts follow one standard block format (defined in `Docs/04_LESSON_STANDARDS.md`, A12).
  - Scaffolding shrinks: A1/A2 give the phrases to use; B1.2 gives only a goal.

### CD-29: The Story Bank (recurring speaking tasks)
- **Decision:** 8 fixed tasks come back at every stage (A1, A2, B1) with higher demands:
  1. Wer bin ich? (who I am)
  2. Mein Alltag (my routine)
  3. Ein Erlebnis (an experience)
  4. Mein Ort (my home or city)
  5. Ein Problem lösen (solving a problem)
  6. Etwas planen (planning something with someone)
  7. Meine Meinung (my opinion)
  8. Ein Mensch, der mir wichtig ist (a person who matters to me)

  The learner records each one per stage and compares the recordings. For example:
  - **A1:** *Am Samstag gehe ich ins Kino.*
  - **A2:** *Am Samstag bin ich mit Freunden ins Kino gegangen, aber der Film war langweilig.*
  - **B1:** *Nachdem wir gegessen hatten, sind wir ins Kino gegangen, obwohl ich eigentlich keine Lust hatte…*
- **Reason:** It makes progress audible (motivation) and forces spiral recycling of grammar in speech.
- **Consequence:** `Learner_Workbook/Story_Bank.md` holds the prompts and stage requirements. Units that match a Story Bank theme (e.g. A2-U01 → task 3) must link to it.

### CD-30: Listening without produced audio
- **Decision:** Claude cannot produce audio, so listening uses two sources:
  1. **Lesson dialogues and texts** are hidden in `<details>`. The learner listens first via a text-to-speech voice (e.g. Edge "Read aloud" German voices, or an AI in voice mode) and reads only afterwards.
  2. **External sources** named per level (e.g. DW *Nicos Weg*, Easy German, Slow German, DW *Langsam gesprochene Nachrichten* / *Top-Thema*, *Tagesschau in 100 Sekunden*, *logo!*, *nachrichtenleicht*), worked with **reusable task sheets** that fit any episode.

  Listening routine: predict → gist → details → read the transcript → shadow. The learner is trained to tolerate unknown words.
- **Reason:** It is the best available approach within the constraint. Generic task sheets stay usable if outside content changes.
- **Consequence:**
  - Never claim a specific episode's content unless it has been verified.
  - Cite sources by name.
  - Audio moves from learner audio (A1–A2) to slowed authentic speech (late A2) to natural standard German (B1).
  - This remains a known weakness (see `00_PROJECT_STATE.md`, known issues).

### CD-31: Reading progression and strategies
- **Decision:** Text types grow as in [Appendix F](#appendix-f--skills-progression). Strategies are taught along the way: predicting from the title, skimming and scanning, guessing from context and word parts, spotting connectors, reading for the argument, summarising. Free reading with graded readers starts in A2.
- **Reason:** Reading supplies input volume and is how Präteritum, genitive and nominal style are met.
- **Consequence:** Texts are original (written for the course) or cited external sources. Never reproduce copyrighted texts.

### CD-32: Writing: correct, rewrite, log
- **Decision:** Writing text types grow as in [Appendix F](#appendix-f--skills-progression). Every text goes through the self-editing checklist in this order: verb position → case → gender → connectors → register. Then it is corrected (an AI with a fixed feedback prompt, or a tutor), rewritten, and the errors are logged in the Error Log.
- **Reason:** Writing reinforces grammar and vocabulary, and feedback without a rewrite rarely sticks.
- **Consequence:** `Resources/Writing_Toolkit.md` holds the checklist and the AI feedback prompt. Writing tasks are real text types, not grammar exercises in disguise.

### CD-33: Pronunciation is integrated
- **Decision:** A short pronunciation minute ("Aussprache-Minute") in each lesson uses the lesson's own words. The focus per stage is in [Appendix F](#appendix-f--skills-progression). It is not a separate phonetics course.
- **Reason:** User requirement. Pronunciation sticks when tied to words in active use.
- **Consequence:** `Resources/Pronunciation_Guide.md` is the reference. The key point for English speakers is the glottal stop before vowel-initial words (A2).

---

## F. Review and assessment

### CD-34: Layered review system
- **Decision:** Review happens at five levels:
  1. **Every lesson:** a **3-2-1 retrieval warm-up** (3 items from the last lesson, 2 from about a week ago, 1–2 from a month or more ago); new flashcards at the end.
  2. **Every unit:** `L4_Anwenden` mixes the unit with older material and ends with a 10-minute production quiz.
  3. **Every 3 units:** a cumulative review of 2–3 hours, weighted 50/30/20, using **mixed (interleaved) practice**, e.g. choosing between *weil / denn / deshalb*.
  4. **Error Log:** each review includes a session on the learner's personal "top 5" recurring errors.
  5. **Progress Tracker:** the stage of each structure is updated at every review.
- **Reason:** Reviewing only the last lesson is not enough; older material must return at expanding intervals.
- **Consequence:** No review file may cover only the preceding unit. Review files must pull from A1 material even during B1.

### CD-35: Assessment gates, not lesson counts
- **Decision:** Checkpoints and thresholds are as in [Appendix G](#appendix-g--review-and-assessment-specifications). Finishing lessons does **not** mean readiness. A failed gate leads to a remediation map pointing to specific lessons. External validation: the free official Goethe *Modellsatz* is recommended at the A2 exit and at the B1 exit. Exit tests follow an exam-*like* structure with **original** tasks and include **integrated scenarios**, e.g. a cancelled flight: read the email → listen to the announcement → call the airline → write a complaint → tell a friend.
- **Reason:** The user explicitly said completing lessons must not equal CEFR readiness. Self-made tests cannot certify a level.
- **Consequence:** Never reproduce official exam material; write original tasks in the same format.

### CD-36: One rubric
- **Decision:** A 0–4 scale on five criteria: task completion, range, accuracy, fluency and coherence, plus pronunciation (speaking) or organisation (writing).
- **Reason:** One scale across all checkpoints makes progress comparable.
- **Consequence:** `Resources/Rubrics.md` is the only rubric source. It must exist before the diagnostic (M2) uses it. Checkpoints reference it and do not redefine it.

---

## G. Structure and build process

### CD-37: File architecture
- **Decision:** The structure is in [Appendix H](#appendix-h--file-architecture).
  - A1 units are **single files** (compressed track).
  - Each A2/B1 unit is a **folder of 5 files**: `00_Overview_und_Wortschatz.md`, `L1`, `L2`, `L3` (new content, 60–90 minutes each), and `L4_Anwenden.md` (integration).
  - About 157 course files in total.
  - Filenames avoid umlauts.
  - Standard relative Markdown links (work in VS Code, Obsidian and GitHub).
  - Answer keys in `<details>` blocks.
- **Reason:** User requirement: a navigable structure without lots of tiny files. Each lesson file is one real study session.
- **Consequence:** Don't split lessons into micro-files and don't merge whole units into one file without a change proposal. Adjusting a filename is a local change if all links and Docs are updated.

### CD-38: Lesson template
- **Decision:** The standard lesson sections are in [Appendix I](#appendix-i--lesson-template). They are used flexibly: a section is left out if forcing it would make the lesson unnatural.
- **Reason:** A consistent, predictable structure without mechanical rigidity.
- **Consequence:** The template is formalised in `Docs/04_LESSON_STANDARDS.md` (created in M1). It is validated in the M4 pilot before scaling, and the B1 variant again at the review stop after B1-U01.

### CD-39: Load rhythm
- **Decision:** Heavy units alternate with medium and light ones (loads are in Appendix B).
  - Designated light units: A2-U09 and B1-U08.
  - B1-U12 is integration only, with no new grammar.
  - Load within a unit follows: new concept → practice → consolidation → integration → review.
- **Reason:** The learner should feel steady progress rather than constant overload.
- **Consequence:** Do not add new major grammar to light units.

### CD-40: Workload target
- **Decision:** About 230 hours of guided study plus about 105 hours of exposure (free listening and reading) and flashcards. That is about 12 months at 7 hours a week, or about 8 months at 10 hours a week. The weekly rhythm and the 15-minute minimum day are in [Appendix J](#appendix-j--workload).
- **Reason:** A realistic estimate for going from A1+/A2- to B1, consistent with common CEFR hour estimates.
- **Consequence:** Lesson files target 60–90 minutes. The M4 pilot measures actual time, and estimates are corrected if needed.

### CD-41: Pilot before scaling
- **Decision:** One complete A2 unit (M4) is built and validated, by user review and ideally by the learner actually doing it, **before** any other A2 or B1 unit is built. If the pilot reveals problems, the template or architecture is revised first.
- **Reason:** It avoids copying a flawed template across about 120 files.
- **Consequence:** The pilot unit is **A2-U01 *Erlebnisse*** (approved 2026-09-11, OD-08). The B1 template variant gets a mandatory second validation at the review stop after B1-U01 (M6 WP1, approved 2026-09-11, OD-09).

### CD-42: Incremental, milestone-based build with persistent memory
- **Decision:** The course is built in milestones M0–M8 (`03_MILESTONES.md`) following **Design → Build → Validate → Approve → Scale**. Rules:
  - Only the current milestone is worked on.
  - Every milestone ends with an update of the state files, validation, a summary, and a **STOP** until explicit approval.
  - Project state lives in `Docs/`, never only in chat.
- **Reason:** About 157 high-quality files cannot be produced reliably in one generation, and the project will span many sessions.
- **Consequence:** A new session must be able to resume from `Docs/` alone. Update `00_PROJECT_STATE.md` whenever the state changes, including after each work package inside a milestone.

### CD-43: Roles of `Docs/` and the course folder
- **Decision:**
  - `Docs/` is builder-facing and authoritative: project memory, decisions, principles, milestones, changelog.
  - The course folder `Deutch/GERMAN_LEARNING_PLAN/` is learner-facing (approved 2026-09-11, OD-05).
  - A future `00_Curriculum/` area inside the course **may** contain shorter learner-facing explanations and navigation derived from `Docs/`. It never adds architecture of its own (approved 2026-09-11, OD-06).
  - Workspace-level `CLAUDE.md` is a concise recovery pointer into `Docs/`, not a second source of truth (approved 2026-09-11, OD-10).
- **Reason:** It separates "how and why we build" from "what the learner uses", and avoids two competing sources of truth.
- **Consequence:** Learner-facing files must not introduce architecture that is absent from `Docs/01`.

---

# Appendices — Architecture Baseline v1.0 Reference

These appendices are the compact, authoritative record of the approved blueprint. Changing anything here is a **global change** (see [Change control](#change-control)).

## Appendix A — Stages and CEFR can-do targets

| Stage | Name | Units | Main change in ability |
|---|---|---|---|
| 0 | Start | Diagnostic + Sentence Map | The learner knows exactly where they are |
| A1 | **Fundament** (consolidation) | 5 short units + A1 Gate | From "I know this" to "I can say it without thinking" |
| A2.1 | **Erleben & Erzählen** (experiencing & telling) | U01–U06 + R1, R2 + Midpoint | From single sentences to talking about the past, people and places |
| A2.2 | **Organisieren & Begründen** (organising & giving reasons) | U07–U10 + R3 + Exit | From talking to getting things done: arranging, comparing, giving reasons, advising |
| B1.1 | **Erzählen & Beschreiben** (telling & describing) | U01–U06 + R1 + Midpoint | From simple past to rich stories; describing without knowing the word |
| B1.2 | **Argumentieren & Handeln** (arguing & acting) | U07–U12 + R2, R3 + Exit | From opinions to arguments, negotiation and moderately abstract topics |

**Can-do targets:**
- **End of A1:** Handle simple, predictable exchanges about yourself and your immediate needs with a cooperative partner. Answer basic questions within about 3 seconds.
- **End of A2:**
  - Describe routine and past experiences in 6–10 connected sentences.
  - Handle routine transactions: shops, travel, doctor, offices, phone calls.
  - Make and change arrangements.
  - Give simple reasons (*weil, deshalb*).
  - Write short personal and semi-formal messages.
  - Understand the main point of short, clear announcements and conversations.
- **End of B1:**
  - Deal with most situations when travelling or living in a German-speaking country, including unexpected ones (complaints, problems).
  - Narrate experiences, dreams and plans in detail.
  - Give reasons and counter-arguments.
  - Keep a conversation going and talk around missing words.
  - Follow the main points of clear standard German on familiar topics, including slower news.
  - Write connected texts: opinion posts, formal emails, stories.

## Appendix B — Unit map

Load: ● light · ●● medium · ●●● heavy.

### A1 Fundament (about 2–5 h per unit, depending on the Schnelltest route)

| Unit | Load | Can-do | Grammar | Main task | Pronunciation |
|---|---|---|---|---|---|
| **A1-U01 Ich & du** | ● | Introduce yourself; ask and answer personal questions with follow-ups | Present tense, *sein/haben*, question words, yes/no questions, verb-second order, *du/Sie*, **Sentence Map** | Interview → introduce the partner | Vowel length, umlauts |
| **A1-U02 Essen & Einkaufen** | ●● | Buy things; talk about food and what you have or need | Gender and gender clues from word endings, plural, nominative/accusative, *ein/kein*, *nicht* vs *kein*, possessives, *möchte* | Market/bakery role-play; "what's in my fridge" | Final devoicing, *ch* (ich/ach) |
| **A1-U03 Mein Tag** | ●● | Describe your routine; arrange a time | Separable verbs (first bracket), *um/am/im*, inversion with time first, frequency words | Find a meeting time from two schedules (info gap) | *r*, *ei/ie/eu* |
| **A1-U04 Können, müssen, dürfen** | ●● | Ask for help, make requests, understand rules | Modal verbs (second bracket), imperative, position of *nicht* (basics), *mal* | Flat-share rules; asking favours | *s/z/sch/sp/st* |
| **A1-U05 In der Stadt** | ● | Ask for and give directions; buy a ticket | Place phrases as fixed chunks (*zum Bahnhof, im Park, nach Hause*), *war/hatte*, Perfekt recognition | Directions role-play; ticket-machine problem | Stress in compound words |
| **A1 Checkpoint** | | Gate into A2 | | | |

### A2.1 Erleben & Erzählen (about 7 h per unit)

| Unit | Load | Can-do | Grammar | Main task |
|---|---|---|---|---|
| **A2-U01 Erlebnisse** | ●●● | Narrate a weekend or trip in sequence; ask follow-up questions about experiences | **Perfekt** (*haben/sein*, regular/irregular, separable/inseparable participles); *zuerst / dann / danach* | Reconstruct a partner's weekend (info gap); Story Bank #3 |
| **A2-U02 Menschen & Geschenke** | ●●● | Talk about likes, family and friends; choose a gift; say what fits or suits someone | **Dative system**: articles, pronouns, dative verbs (*gefallen, gehören, helfen, schmecken, passen, stehen*); order of dative and accusative objects | Choose and justify a gift for a friend together |
| **A2-U03 Wohnen** | ●●● | Describe a flat; give and follow placing instructions; do a flat viewing | **Two-way prepositions**, *stellen/stehen, legen/liegen, hängen*; dative prepositions *aus, bei, mit, nach, seit, von, zu* | Furnish a room from spoken instructions; flat-viewing call |
| **A2-R1** | | Cumulative review: A1 + U01–U03; first error-log session | | |
| **A2-U04 Essen & Gewohnheiten** | ●● | Order with special requests; explain habits and preferences with reasons | ***weil / dass / denn***; opinion starters; spoken *weil* + verb-second explained | Restaurant role-play; mini-debate "Is cooking at home worth it?" |
| **A2-U05 Gesundheit** | ●● | Describe symptoms; see a doctor; call in sick; give simple advice | **Reflexive verbs** (accusative + dative for body parts); ***wenn*** (condition); **Präteritum of modals**; *sollen* | Doctor's visit; phone call to call in sick |
| **A2-U06 Einkaufen & Kleidung** | ●●● | Describe and compare items; return something defective | **Adjective endings stage 1** (nominative/accusative after *der-/ein-* words); *welch-/dies-* | Complaint and return in a shop |
| **A2-R2 + Midpoint** | | Cumulative review + diagnostic mid-test | | |

### A2.2 Organisieren & Begründen (about 7 h per unit)

| Unit | Load | Can-do | Grammar | Main task |
|---|---|---|---|---|
| **A2-U07 Reisen & Verkehr** | ●● | Compare travel options; book; handle a delay; ask for information politely | **Comparative/superlative**; *an/auf/in/nach* with places; **indirect questions** (*ob*, question word); *hätte gern / würde gern* chunks | Trip planning by comparing options; missed-connection role-play |
| **A2-U08 Arbeit & Termine** | ●● | Describe your job or studies; make and move appointments; leave a phone message | **Verbs + prepositions**, *wo-/da-* words (introduction); *seit/ab/vor/für/bis*; *werden* as full verb; middle-field order | Reschedule a meeting by phone; typical working day |
| **A2-U09 Feste & Pläne** | ● (recycling) | Invite someone, accept/decline, negotiate plans | Future with present tense + time phrase, *werden* (introduction); *Hättest du Lust…? / Wie wäre es mit…?*; particle *doch* | **Plan an event together** (A2-exam style) |
| **A2-U10 Medien & Technik** | ●● | Explain a technical problem; give advice; express wishes | **Konjunktiv II advice/wishes** (*würde, könnte, solltest*); ***deshalb / trotzdem / sondern***; *man / jemand / niemand* | Tech-support call; forum advice post |
| **A2-R3 + A2 Exit** | | Readiness gate for B1 | | |

### B1.1 Erzählen & Beschreiben (about 9–10 h per unit)

| Unit | Load | Can-do | Grammar | Main task |
|---|---|---|---|---|
| **B1-U01 Lebenswege** | ●●● | Tell a life story or biography; read short narratives | **Präteritum of all verbs** (written vs spoken); ***als* vs *wenn***; **Plusquamperfekt** with *nachdem/bevor*; *während, seit, bis, sobald* | Biography presentation; 4/3/2 retelling |
| **B1-U02 Menschen beschreiben** | ●●● | Describe people and personalities; describe things whose name you don't know | **Relative clauses** (nom/acc/dat, with prepositions); **adjective endings stage 2**; n-declension; *sich* = "each other" | "Wer ist das?" guessing game; Taboo-style describing |
| **B1-U03 Arbeit & Beruf** | ●● | Apply for a job; do an interview; explain goals | **zu + infinitive**; ***um…zu* vs *damit***; *da-* word + clause | Job-interview simulation; application email |
| **B1-R1** | | Cumulative review | | |
| **B1-U04 Gesundheit & Wohlbefinden** | ●●● | Discuss hypothetical situations; give nuanced advice; talk about stress and lifestyle | **Konjunktiv II, full** (unreal *wenn*-clauses, wishes, polite forms) | "What would you do?" scenarios; advice-column reply |
| **B1-U05 Reisen & Kulturen** | ●● | Compare cultures; write a formal complaint | **Genitive** + *wegen, trotz, während, statt*; paired connectors (*entweder…oder, weder…noch, sowohl…als auch, nicht nur…sondern auch*) | Formal complaint email; culture-comparison talk |
| **B1-U06 Medien & Nachrichten** | ●●● | Understand simple news; describe processes; discuss social media | **Passive**: present, Präteritum, with modals | Explain how something is made or done; pros/cons discussion |
| **B1 Midpoint** (includes review) | | | | |

### B1.2 Argumentieren & Handeln (about 9–10 h per unit)

| Unit | Load | Can-do | Grammar | Main task |
|---|---|---|---|---|
| **B1-U07 Umwelt & Nachhaltigkeit** | ●● | Build an argument; take a position in a forum | ***obwohl* vs *trotzdem***; ***sodass / so…dass***; ***je…desto***; argument structure | Opinion forum post (B1-exam style); debate |
| **B1-U08 Zusammenleben** | ● (light) | Settle a conflict with a neighbour or flatmate; talk about volunteering | ***lassen***; modal particles in depth (*doch, ja, halt, eben, eigentlich*) | Neighbour-conflict negotiation |
| **B1-U09 Bildung & Zukunft** | ●● | Give a structured presentation; talk about the future | **Future I** incl. guesses (*wird wohl*); word formation (*-ung, -heit, -keit, -bar, -los, un-*); recognising nominal style | **Structured 3–4-minute presentation** (B1-exam style) |
| **B1-R2** | | Cumulative review | | |
| **B1-U10 Geld & Entscheidungen** | ●● | Weigh options; negotiate a decision; talk about regrets | **Konjunktiv II past**; *hätte … sollen* as chunk; decision chunks (*eine Entscheidung treffen*) | Joint decision task; "a decision I'd make differently" |
| **B1-U11 Wissenschaft & Technik** | ●● | Summarise an article; talk about future technology | **Konjunktiv I, recognition**; genitive prepositions (*innerhalb, aufgrund*); Zustandspassiv, recognition | Article summary + opinion |
| **B1-U12 Diskussion** | ●● (integration, no new grammar) | Take part in a full discussion: interrupt, clarify, concede, summarise | Discussion strategies; grammar clinic from the error log | Moderated debate; argumentative essay |
| **B1-R3 + B1 Exit** | | Final assessment | | |

## Appendix C — Dependency graph

```
Present tense + verb-second (A1-U01)
 ├─ Bracket: separable verbs (A1-U03) → modals (A1-U04)
 │    ├─ Perfekt (A2-U01) → Präteritum of modals (A2-U05) → Präteritum of all verbs (B1-U01) → Plusquamperfekt (B1-U01)
 │    └─ Verb-final: weil/dass (A2-U04) → wenn (A2-U05) → ob/question word (A2-U07) → temporal clauses (B1-U01)
 │                   → relative clauses (B1-U02) → zu-infinitive / um…zu (B1-U03) → obwohl/sodass (B1-U07)
 │
Nominative/Accusative (A1-U02)
 ├─ Dative (A2-U02) → two-way prepositions (A2-U03) → adjective endings I (A2-U06)
 │                  → adjective endings II + relative pronouns (B1-U02) → genitive (B1-U05)
 └─ Reflexive verbs (A2-U05) → verbs + prepositions (A2-U08) → da-words + clauses (B1-U03)

möchte / hätte gern chunks (A1–A2) → Konjunktiv II advice (A2-U10) → Konjunktiv II full (B1-U04) → Konjunktiv II past (B1-U10)
werden as full verb (A2-U08) → future (A2-U09, B1-U09) → passive (B1-U06) → passive with modals (B1-U06/U11)
```

## Appendix D — Grammar spiral

| Structure | Intro / chunk | Controlled → in context | Spontaneous use demanded in |
|---|---|---|---|
| Verb-second / bracket | A1-U01, U03, U04 | all A2 units | everywhere |
| Nominative / accusative | A1-U02 | A2-U02, U03 | ongoing |
| Dative | A1-U05 (chunks) | **A2-U02**, U03 | B1-U02 (adjectives, relative pronouns) |
| Perfekt | A1-U05 (recognition) | **A2-U01** | A2-U05, U07, U09; B1-U01 (contrast with Präteritum); Story Bank |
| Präteritum | A1 *war/hatte*; A2-U05 modals | **B1-U01** | B1 reading and storytelling |
| Verb-final clauses | – | **A2-U04** *weil/dass* → U05 *wenn* → U07 *ob* | B1-U01, U02, U07 |
| Two-way prepositions | A1-U05 chunks | **A2-U03** | A2-U07; B1 descriptions |
| Reflexive verbs / verbs + prepositions | – | A2-U05, **U08** | B1-U03 (*da-* + clause) |
| Comparison | – | **A2-U07** | B1-U05, U10 |
| Adjective endings | chunks | **A2-U06** → **B1-U02** → B1-U05 | B1 writing |
| Konjunktiv II | *möchte, hätte gern* | A2-U07, **U10** → **B1-U04** | B1-U07–U12; past form in B1-U10 |
| *werden* / future / passive | A2-U08 | A2-U09 → **B1-U06** | B1-U09, U11 |
| Relative clauses | – | **B1-U02** | talking around missing words, everywhere |
| zu-infinitive / *um…zu* | – | **B1-U03** | B1-U07–U12 |
| Genitive, Konjunktiv I | – | B1-U05, U11 | recognition + written use |
| Modal particles | *mal* (A1) | *doch, denn, ja* (A2) | *halt, eben, eigentlich, wohl* (B1-U08) |

## Appendix E — Vocabulary targets

| | A1 | A2 | B1 |
|---|---|---|---|
| Active target (cumulative) | about 600 | about 1,300 | about 2,400 |
| Recognition (cumulative) | about 900 | about 2,000 | about 4,000+ |
| Per unit | gap-fill only | ~45 ★ active + ~40 recognition | ~50 ★ active + ~60 recognition |

Sizes roughly match the Goethe exam word lists.

**Topic areas:**
- **A1:** self, food, daily routine, time, the city, rules and abilities.
- **A2:** experiences, people and relationships, housing, food habits, health, shopping, travel, work, celebrations, media and technology.
- **B1:** life stories, personality, career, wellbeing, cultures, news, environment, living together, education, money and decisions, science, plus abstract vocabulary (*Vorteil, Nachteil, Entwicklung, Verantwortung*…).

## Appendix F — Skills progression

### Speaking

| | A1 | A2 | B1 |
|---|---|---|---|
| Length of a turn | 1–2 sentences | 30–60 s of connected speech | 2–3 min monologue |
| Interaction | Scripted exchanges | Transactions, arranging, simple reasons, follow-up questions | Negotiating, persuading, discussing, handling the unexpected |
| Strategy focus | Quick answers, asking someone to repeat | Asking for clarification, gaining time (*Moment, wie sagt man…*) | Talking around missing words, repairing, disagreeing politely, summarising |
| Fluency technique | Fast answer drills, reading aloud | Shadowing, self-talk, 2/1.5/1 retelling | 4/3/2 retelling, timed opinions, unscripted role-plays |

### Reading

| Level | Texts |
|---|---|
| A1 | Signs, forms, timetables, short messages |
| A2 | Emails, blog posts, instructions, ads, graded stories |
| B1 | Simplified news (*nachrichtenleicht*), then regular news, opinion and forum posts, narrative extracts, informational texts |

### Listening

| Level | Audio |
|---|---|
| A1–A2 | Learner audio (lesson dialogues via TTS; *Nicos Weg*) |
| Late A2 | Slowed authentic speech (Easy German with subtitles, Slow German) |
| B1 | Natural standard German (*Langsam gesprochene Nachrichten*, *Top-Thema*, Easy German podcast, *Tagesschau in 100 Sekunden*, *logo!*) |

Skills trained: gist, specific information, prediction, recognising familiar words in connected speech, speaker intention, context, coping with unknown words.

### Writing

| Level | Tasks |
|---|---|
| A1 | Sentences, forms, notes |
| A2 | Messages and emails of 30–60 words (invite, apologise, ask); descriptions; past-tense diary |
| B1 | Informal email (~80 words), forum opinion post (~80 words), formal email (~40–60 words), stories, complaints, summaries, pro/con texts |

### Pronunciation

- **A1:** vowel length and spelling clues, umlauts, *ch*, *r* (including vowel-like *-er*), final devoicing, *s/z/sch/st/sp*, *ei/ie/eu*.
- **A2:** word stress (separable vs inseparable prefixes, compounds, *-ieren*, *-tion*); **glottal stop** before vowel-initial words; *-ig*; weak *-en*; question intonation.
- **B1:** sentence rhythm and emphasis, contrastive stress, recognising connected speech (*haste, isses, wir ham*), intonation for politeness and emotion.

## Appendix G — Review and assessment specifications

### Review layers

| Layer | Where | Specification |
|---|---|---|
| 3-2-1 warm-up | Start of every lesson | 3 items from last lesson, 2 from about a week ago, 1–2 from a month or more ago |
| Unit quiz | End of `L4_Anwenden` | 10-minute production quiz, ≥80% required, otherwise targeted revisit |
| Cumulative review | After every 3 units (A2-R1/R2/R3, B1-R1/R2/R3; B1 Midpoint includes one) | 2–3 h; 50% recent block / 30% previous block / 20% older; interleaved |
| Error clinic | Every cumulative review | Learner's top-5 recurring errors from the Error Log |
| Story Bank | Once per stage | 8 recurring speaking tasks, recorded and compared |
| Flashcards | Daily, 10–15 min | Production-direction cards; exported per stage as `Resources/Anki/A1.tsv`, `A2.tsv`, `B1.tsv` |

### Checkpoints

| Checkpoint | When | Content | Threshold |
|---|---|---|---|
| **Diagnostic** | Start | See CD-03 | Decides the route through A1 |
| Unit exit | Each `L4_Anwenden` | Can-do checklist + production quiz + main task | ≥80% |
| **A1 Gate** | End of A1 | 4 skills + fluency | ≥75%; speaking rubric ≥2.5/4 |
| A2 Midpoint | After A2-U06 (with R2) | Mixed, diagnostic only (not a gate) | Redirects to weak units |
| **A2 Exit** | End of A2 (with R3) | 4 skills in an A2-exam-like structure (original tasks), an integrated scenario, Story Bank recordings | ≥70% per receptive skill; ≥3/4 task completion in speaking and writing |
| B1 Midpoint | After B1-U06 | As above | Redirects to weak units |
| **B1 Exit** | End (with R3) | B1-exam-like structure + integrated scenarios + official Goethe *Modellsatz* as external validation | ≥70% per skill (real exams pass at 60%; set higher on purpose) |

**Rubric:** 0–4 per criterion. Criteria: task completion, range, accuracy, fluency and coherence, plus pronunciation (speaking) or organisation (writing).

## Appendix H — File architecture

Planned layout. The course root `Deutch/GERMAN_LEARNING_PLAN/` was confirmed on 2026-09-11 (OD-05). Each file is created in the milestone that first needs it (see `03_MILESTONES.md`).

```
Deutch/
├── CLAUDE.md                              ← recovery pointer for new sessions
├── .gitignore
├── Docs/                                  ← builder-facing project memory (authoritative)
│   ├── 00_PROJECT_STATE.md  01_CURRICULUM_DECISIONS.md  02_DESIGN_PRINCIPLES.md
│   ├── 03_MILESTONES.md     04_LESSON_STANDARDS.md      05_VALIDATION_LOG.md
│   └── 06_CHANGELOG.md
└── GERMAN_LEARNING_PLAN/                  ← learner-facing course
    ├── README.md                          ← start here: how the course works, navigation, weekly rhythm
    ├── 00_Curriculum/                     ← 01–08 optional, learner-facing, derived from Docs/ (OD-06)
    │   ├── 01_Teaching_Philosophy.md
    │   ├── 02_Curriculum_Map.md
    │   ├── 03_Grammar_Spiral.md
    │   ├── 04_Vocabulary_Plan.md
    │   ├── 05_Skills_Progression.md
    │   ├── 06_Review_and_Retrieval.md
    │   ├── 07_Assessment_System.md
    │   ├── 08_Study_Schedule.md
    │   └── 09_Diagnostic_Test.md          ← M2
    ├── A1/
    │   ├── README.md
    │   ├── A1-U01_Ich_und_du.md
    │   ├── A1-U02_Essen_und_Einkaufen.md
    │   ├── A1-U03_Mein_Tag.md
    │   ├── A1-U04_Koennen_muessen_duerfen.md
    │   ├── A1-U05_In_der_Stadt.md
    │   └── A1_Checkpoint.md
    ├── A2/
    │   ├── README.md
    │   ├── A2-U01_Erlebnisse/
    │   │   ├── 00_Overview_und_Wortschatz.md
    │   │   ├── L1_<topic>.md
    │   │   ├── L2_<topic>.md
    │   │   ├── L3_<topic>.md
    │   │   └── L4_Anwenden.md
    │   ├── A2-U02_Menschen_und_Geschenke/   A2-U03_Wohnen/
    │   ├── A2-U04_Essen_und_Gewohnheiten/   A2-U05_Gesundheit/
    │   ├── A2-U06_Einkaufen_und_Kleidung/   A2-U07_Reisen_und_Verkehr/
    │   ├── A2-U08_Arbeit_und_Termine/       A2-U09_Feste_und_Plaene/
    │   ├── A2-U10_Medien_und_Technik/
    │   ├── A2-R1_Wiederholung.md   A2-R2_Wiederholung.md   A2-R3_Wiederholung.md
    │   ├── A2_Midpoint_Checkpoint.md
    │   └── A2_Exit_Checkpoint.md
    ├── B1/
    │   ├── README.md
    │   ├── B1-U01_Lebenswege/               B1-U02_Menschen_beschreiben/
    │   ├── B1-U03_Arbeit_und_Beruf/         B1-U04_Gesundheit_und_Wohlbefinden/
    │   ├── B1-U05_Reisen_und_Kulturen/      B1-U06_Medien_und_Nachrichten/
    │   ├── B1-U07_Umwelt_und_Nachhaltigkeit/ B1-U08_Zusammenleben/
    │   ├── B1-U09_Bildung_und_Zukunft/      B1-U10_Geld_und_Entscheidungen/
    │   ├── B1-U11_Wissenschaft_und_Technik/ B1-U12_Diskussion/
    │   ├── B1-R1_Wiederholung.md   B1-R2_Wiederholung.md   B1-R3_Wiederholung.md
    │   ├── B1_Midpoint_Checkpoint.md
    │   └── B1_Exit_Checkpoint.md
    ├── Resources/
    │   ├── Sentence_Map.md
    │   ├── Grammar_Tables.md
    │   ├── Verb_Lists.md
    │   ├── Redemittel.md
    │   ├── Pronunciation_Guide.md
    │   ├── English_German_Interference.md
    │   ├── Speaking_Toolkit.md
    │   ├── Listening_Reading_Sources.md
    │   ├── Writing_Toolkit.md
    │   ├── Rubrics.md
    │   └── Anki/  A1.tsv  A2.tsv  B1.tsv
    └── Learner_Workbook/
        ├── Progress_Tracker.md
        ├── Error_Log.md
        ├── Chunk_Bank.md
        ├── Story_Bank.md
        └── Writing_Portfolio.md
```

**Count:** root README 1 + 00_Curriculum 9 + A1 7 + A2 56 + B1 66 + Resources 13 + Learner_Workbook 5 = **about 157 course files**.

## Appendix I — Lesson template

Sections are used where they fit, not forced into every lesson.

1. **Header**: level, prerequisites (linked), estimated time, load
2. **3-2-1 retrieval warm-up**
3. **Objectives** ("By the end you can…")
4. **Discover**: a dialogue or text first; the learner finds the pattern
5. **Explanation**: the 10-point standard for major grammar (CD-24)
6. **Examples** with register tags
7. **Guided practice**
8. **Active retrieval** (meaning or situation → German)
9. **Communicative task**
10. **Speaking**, often with an AI role-play prompt block
11. **Reading / listening**
12. **Writing**
13. **Aussprache-Minute** (pronunciation minute), using the lesson's words
14. **Typical mistakes**, with English interference flagged
15. **Links back** to earlier material
16. **Self-check** ("I can…")
17. **Optional challenge**
18. **New flashcards** + answer keys in `<details>`

Lesson types: new-content lessons (`L1`–`L3`), integration lesson (`L4_Anwenden`), cumulative review, checkpoint. A1 units follow a compressed single-file variant: Schnelltest → routed sections → fluency task → self-check.

## Appendix J — Workload

| Stage | Guided study | Extra listening/reading + flashcards | Weeks at about 7 h/week |
|---|---|---|---|
| Diagnostic | 2–3 h | – | 0.5 |
| A1 Fundament | 8–25 h (depends on route) | about 5 h | 2–4 |
| A2 | about 85 h | about 40 h | about 18 |
| B1 | about 125 h | about 60 h | about 27 |
| **Total** | **about 230 h** | **about 105 h** | **about 12 months** (about 8 at 10 h/week) |

**Weekly rhythm at about 7 h:**
- 4 lessons of about 75 minutes
- 1 speaking session with an AI, tandem partner or tutor (about 45 minutes)
- flashcards for 10–15 minutes a day
- 2 sessions of free listening or reading (about 30 minutes each)

**Minimum day:** 15 minutes (flashcards + one spoken recording).

---

## Change control

### What counts as a global (architectural) change
Anything that alters a CD decision or Appendices A–J:
- unit order or allocation of grammar to units
- adding, removing, merging or splitting units
- stage boundaries
- checkpoint thresholds
- file architecture
- lesson template sections
- instruction-language policy
- design principles

**Procedure (mandatory):**
1. Identify the problem.
2. Explain why it is a problem.
3. Propose a modification.
4. Record it in the register below with status `PROPOSED`.
5. Ask the user for approval.
6. Only after approval: apply it, bump the architecture version, log it in `06_CHANGELOG.md`, and update `00_PROJECT_STATE.md`.

### What counts as a local change (no approval needed)
- wording, examples, choice and order of exercises within a lesson
- fixing errors
- moving material between `L1`–`L3` *within the same unit*
- recognition vocabulary within the Appendix E ranges
- filename adjustments with all links updated

Log significant local changes in `06_CHANGELOG.md`.

### Versioning
- **v2.0, v3.0…** (major): structural change to stages, units or sequence.
- **v1.1, v1.2…** (minor): approved change to content allocation, thresholds or templates.
- Local changes do not change the version.

**Current version: v1.0.**

### Change proposal register

| ID | Date | Proposal | Reason | Status |
|---|---|---|---|---|
| CP-001 | 2026-09-11 | *(Candidate, not yet formally proposed.)* Add an explicit **mediation** strand (explaining German content in English and vice versa) beyond the light coverage in B1-U11/U12 | Known gap from the Phase 1 internal audit | **Must be decided before M7 starts** |
