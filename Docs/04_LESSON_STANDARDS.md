# 04 — Lesson Standards

> **Purpose:** The authoritative standard for every course file: how lessons are built, how files are formatted, and when a file counts as complete.
>
> **Version:** 1.0 (2026-09-11)
>
> **Status:** Provisional. It will be validated by the **M4 pilot** (A2-U01) and, for the B1 variant, by the **review stop after B1-U01** (M6 WP1). Revisions after validation become v1.1, v1.2… and are logged in [06_CHANGELOG.md](06_CHANGELOG.md).
>
> **Relationship to other Docs:**
> - Turns CD-38 and Appendix I of [01_CURRICULUM_DECISIONS.md](01_CURRICULUM_DECISIONS.md) into concrete rules.
> - [02_DESIGN_PRINCIPLES.md](02_DESIGN_PRINCIPLES.md) gives the *why*; this file gives the *how*.
> - On architecture (what is taught where, thresholds), `01` wins. On file format and lesson construction, this file wins.
> - Changing the component list or the mandatory/optional rules is a global change (change control in `01`).
>
> This is a stable standard, not a project log.

## Contents
- [Part A — Lesson architecture](#part-a--lesson-architecture)
- [Part B — File standards](#part-b--file-standards)
- [Part C — Quality checklist](#part-c--quality-checklist)
- [Part D — File skeletons](#part-d--file-skeletons)

---

# Part A — Lesson architecture

## A1. File types

| Type | `type:` key | Where | Purpose | Target length |
|---|---|---|---|---|
| A1 unit | `a1-unit` | `A1/A1-U0x_*.md` | Compressed, gated consolidation (CD-02) | Full route 2–5 h, split into sittings of ≤90 min |
| Unit overview | `overview` | `<unit>/00_Overview_und_Wortschatz.md` | Unit map, objectives, word bank, recycling list | Reference, not a session |
| New-content lesson | `lesson` | `<unit>/L1_*.md` to `L3_*.md` | New language → practice → task | 60–90 min (target 75) |
| Integration lesson | `integration` | `<unit>/L4_Anwenden.md` | Main task, mixed review, skills, unit quiz; **no new grammar** | 60–90 min |
| Cumulative review | `review` | `A2-R1_Wiederholung.md` etc. | Review weighted 50/30/20, error clinic | 2–3 h, split into 2–3 sittings |
| Checkpoint | `checkpoint` | `A1_Checkpoint.md` etc. | Assessment against Appendix G thresholds | 2–3 h, splittable |

## A2. Components

Each component's purpose and rules. Section icons are fixed (see [B11](#b11-section-icons)).

| # | Component | Icon | Purpose | Rules |
|---|---|---|---|---|
| 0 | Header / metadata | – | Orientation and tooling | YAML front matter + visible header (B4) |
| 1 | Retrieval warm-up | 🔁 | Spaced recall of older material | 3-2-1 formula (A5); 5–10 min; production only |
| 2 | Objectives | 🎯 | What the learner will be able to *do* | 2–4 "You can…" statements tied to situations |
| 3 | Discovery | 🔍 | Input first; the learner spots the pattern | A short dialogue or text with the target form in natural use, plus 2–4 noticing questions |
| 4 | Explanation | 📘 | Intuitive, systematic understanding | 10-point standard for major topics (A9); Sentence Map for verb structures |
| 5 | Examples | 💬 | Natural models | 5–10 examples, register-tagged (B9), idiomatic translations |
| 6 | Guided practice | ✍️ | Controlled use | 6–10 items per exercise; every item meaningful in the unit's topic |
| 7 | Active retrieval | 🧠 | Meaning or situation → German | Timed where possible; answers hidden |
| 8 | Communicative task | 🎭 | Use German to achieve something | A realistic goal; needs the lesson's language |
| 9 | Speaking | 🗣️ | Oral production, moving toward spontaneity | Speaking level S1–S4 (A6); success criteria stated |
| 10 | Reading | 📖 | Comprehension + strategies | Task before the text (predict, gist, detail); original texts only |
| 11 | Listening | 🎧 | Understanding by ear | TTS-first: text hidden under `Transkript`; or an external source + task sheet |
| 12 | Writing | 📝 | Real text types | Text type, reader, purpose, length; correct → rewrite → log loop |
| 13 | Pronunciation | 👄 | "Aussprache-Minute" | 3–5 min, uses this lesson's words |
| 14 | Typical mistakes | ⚠️ | Head off predictable errors | ❌ → ✅ pairs, English interference flagged where relevant |
| 15 | Links to previous material | 🔗 | Make the spiral visible | Back-links to the units where material was introduced |
| 16 | Self-check | ✅ | Learner's judgement of readiness | "I can…" checklist; what to do if not |
| 17 | Challenge | 🚀 | Deeper practice for motivated learners | Harder, more open; never needed for later lessons |
| 18 | Flashcards | 🃏 | Feed spaced repetition | Production-direction cards (B8) |
| 19 | Answer key | 🔑 | Check after recall | In `<details>` directly after each activity (B6), not a separate section |

## A3. Mandatory and optional components by file type

Codes:
- **M** = mandatory.
- **M\*** = mandatory when the lesson introduces a new structure. A lesson focused on vocabulary or skills replaces Discovery with a situational input text and may shorten the Explanation.
- **U** = unit-level requirement: it must appear in **at least two** of `L1`–`L4` in every unit, and `L4` always has Writing.
- **O** = optional: use it when it serves the lesson.
- **–** = not used.

| Component | A1 unit | Overview | L1–L3 | L4 | Review | Checkpoint |
|---|---|---|---|---|---|---|
| Header / metadata | M | M | M | M | M | M |
| 🔁 Retrieval warm-up | M (the Schnelltest) | – | M | M | M (extended) | – |
| 🎯 Objectives | M | M | M | M | M | M (what is assessed) |
| 🔍 Discovery | O | – | M\* | – | – | – |
| 📘 Explanation | M (short refresh) | Summary only | M\* | – | O (mini-recap) | – |
| 💬 Examples | M | O | M | O | O | – |
| ✍️ Guided practice | M | – | M | O | M (interleaved) | – |
| 🧠 Active retrieval | M (timed) | – | M | M | M | M |
| 🎭 Communicative task | M | Names the main task | M | M (unit main task) | M | M (integrated scenario) |
| 🗣️ Speaking | M | – | M | M (timed or unscripted) | M | M |
| 📖 Reading | O | – | U | U | O | M |
| 🎧 Listening | O | – | U | U | O | M |
| 📝 Writing | O | – | U | M | O | M |
| 👄 Pronunciation | M | – | M | O | O | Via the speaking rubric |
| ⚠️ Typical mistakes | M | – | M | O | M (error clinic) | – |
| 🔗 Links to previous | M | M | M | M | M | M (remediation map) |
| ✅ Self-check | M | – | M | M (can-do list + unit quiz) | M | Scoring sheet |
| 🚀 Challenge | O | – | O (recommended) | O | O | – |
| 🃏 Flashcards | M | M (unit deck list) | M | O (review set) | – | – |
| 🔑 Answer key | M | – | M | M | M | M |

**Do not add components mechanically.** If a component would feel forced, leave it out and add a one-line note in the file's validation record (Part C), e.g. "no pronunciation minute: no suitable new sounds". A component marked **M** can only be dropped through a documented exception approved at validation.

## A4. Lesson length and activity count

- Every activity heading states its estimated time, e.g. `### 4. Wer hat was gemacht? (~10 min)`.
- The sum of the estimates must fall inside the file's target length (A1) with a tolerance of ±10%.
- In the M4 pilot, estimates are compared with the time the learner actually takes, and corrected.

| Lesson length | Activities (excluding warm-up and self-check) |
|---|---|
| 45–60 min (light lessons) | 4–6 |
| 60–75 min | 6–8 |
| 75–90 min | 7–10 |
| Hard cap | 12 |

**Time budget for a new-content lesson (guideline):**

| Share | Component |
|---|---|
| ≥20% | Retrieval (warm-up + retrieval activities + end recall) |
| ≥20% | Speaking |
| ≤20% | Reading the explanation |
| 10–20% | Reading/listening input |
| 0–20% | Writing |
| rest | Guided practice and task |

- Controlled exercises have **6–10 items**, never 20+. Depth comes from variety, not from repetition.
- Longer files (A1 units, reviews, checkpoints) mark natural break points with `> ⏸️ Good place for a break.`

## A5. How retrieval is distributed

1. **Start — the 3-2-1 warm-up** (5–10 min):
   - **3** items from the previous lesson
   - **2** from about a week ago (3–5 lessons back)
   - **1–2** from a month or more ago (12+ lessons back, or the previous stage)

   Mix vocabulary, chunks and grammar. Production only.
2. **Middle.** After each new input block, a short retrieval check (2–4 items) before moving on. Retrieval is spread through the lesson, not saved for the end.
3. **End.** Blank-page recall: "Close the lesson. Write or say everything you remember: 10 words, 3 chunks, the rule in your own words." Then the flashcards.
4. **Share of production.** At least **60%** of all practice items require production. Recognition items (matching, choosing) are warm-ups for production, not substitutes for it.
5. **Retrieval under time.** From A2 on, every lesson contains at least one timed retrieval, e.g. "answer each in ≤5 seconds, aloud".
6. **Cue progression.** How retrieval prompts change by stage:

   | Stage | Typical cues | English cues |
   |---|---|---|
   | A1–A2 | English meaning, situation description, first-letter cloze (`Ich h___ gestern …`) | Allowed freely |
   | B1.1 | Situations, German definitions, paraphrase | ≤50% of cues |
   | B1.2 | Situations, German definitions, paraphrase | ≤25% of cues |

   These are target values to be confirmed in the pilot and B1 review stop.
7. **Beyond the lesson.** Flashcards (daily), `L4` (unit), cumulative reviews (50/30/20), Story Bank (per stage). See CD-34.

## A6. How speaking progresses

**Speaking levels:**

| Level | Name | What it looks like |
|---|---|---|
| **S1** | Controlled | Repeat, read aloud, oral chunk and transformation drills |
| **S2** | Guided | Answer prompts that must include given elements; describe a situation using given phrases |
| **S3** | Communicative | Role-play or info gap with a goal and a complication; target language suggested, not required |
| **S4** | Spontaneous | Unscripted, timed, no specified structure: 4/3/2 retelling, surprise prompts, open discussion |

**Rules:**
- Every `L1`–`L3` has at least one speaking activity. Each unit's `L3` reaches **S3** at least.
- Every `L4` contains **S4**, and its main speaking performance is **recorded** and checked with the self-recording checklist.
- Every unit has at least one **timed** and at least one **unscripted** speaking activity.
- Stage targets (Appendix F in `01`): A1 turns of 1–2 sentences; A2 30–60 s; B1 2–3 min. In B1.2, at least 50% of speaking activities are S3–S4 **without phrase lists**.
- Each speaking activity states:
  - **setup**: solo recording / AI partner / human partner (optional)
  - **time**
  - **success criteria**: content points and target language for S1–S3; only the communicative goal for S4
- An AI partner is offered through the standard prompt block (A12).

## A7. How scaffolding decreases

| | A1 | A2.1 | A2.2 | B1.1 | B1.2 |
|---|---|---|---|---|---|
| Task instructions | English | English | English | Simple German + English support | German |
| Grammar explanations | English | English | English | English | English + German key terms |
| Phrase support in tasks | Full phrase lists | Phrase lists | Phrase hints | Phrases on request (`Hinweis`) | Goal only |
| Model answer before the task | Yes | Yes | Sometimes | Rarely | No (only after, as `Beispielantwort`) |
| Glossing in texts | All unknown words | Key unknown words | Key words | Only words that can't be guessed | Learner guesses first; gloss hidden |

**Within a unit:** `L1` has the most support, `L4` the least.

**Within an activity:** give hints in a `Hinweis` `<details>` block so the learner opts in, rather than printing them openly.

## A8. How vocabulary recycling works

1. **Context before list.** New ★ items first appear in the discovery or input text. The canonical entry is in the unit's word bank (B7).
2. **Three uses per unit.** The learner must *produce* each new ★ item at least **3 times** within the unit (practice, retrieval, task). It then reappears in `L4` and in at least one later unit or review.
3. **Older vocabulary per lesson.** Each lesson's tasks require at least **5 (A2)** or **8 (B1)** items from earlier units. At least one of them comes from a unit older than the previous one.
4. **"Recycled from" list.** Each unit's list names at least **15 (A2)** or **20 (B1)** items from at least **3 earlier units**, including at least one earlier stage (A2 recycles A1; B1 recycles A1 and A2). Tasks must actually need these items.
5. **Pace.** At most about **15 new ★ items per new-content lesson** (unit totals in Appendix E of `01`).
6. **Chunks count.** Chunks and collocations count as items and are preferred over isolated words.
7. **Warm-ups** always include vocabulary.

## A9. How grammar serves communicative tasks

1. **Need first.** Each grammar point opens with a one-line **"Why you need this"** tied to the lesson's task. Example: "To tell someone about your weekend, you need the Perfekt."
2. **The task needs the structure.** The communicative task must be impossible or unnatural without the target structure. If it isn't, redesign the task.
3. **10-point standard for major topics** (CD-24): meaning · why it exists · when used · form · word order · common patterns · common mistakes · important exceptions · difference from earlier structures · real communicative use. **Minor topics:** form + use + one pattern + one typical mistake.
4. **Verb structures always appear on the Sentence Map** (CD-05 table format, unchanged).
5. **Terminology.** German term + English gloss on first use in each unit. Allowed core terms: *Satzklammer, Vorfeld, Mittelfeld, Nominativ, Akkusativ, Dativ, Genitiv, Perfekt, Präteritum, Plusquamperfekt, Konjunktiv II, Nebensatz, Relativsatz, trennbares Verb, Modalverb, reflexives Verb, Passiv*. Avoid other terminology unless it clearly helps.
6. **No meaningless drills.** Every controlled item is a plausible sentence in the unit's topic.
7. **Exceptions** are taught only if they are frequent at the current level. Rare ones wait or are skipped (CD-21).
8. **Chunks first** (CD-06). Forms used before their system is taught are marked *"use now — explained in [unit]"* with a forward link.

## A10. How natural German examples are selected

Check every example against these criteria:

1. **A plausible speaker and situation.** You can say who says it, to whom, and where.
2. **Frequent, current vocabulary.** Standard German (Germany) by default. Austrian/Swiss variants are mentioned in prose, not with tags.
3. **Level-appropriate.** Known structures plus at most the lesson's target (i+1). Anything above that is glossed or avoided.
4. **Natural shape:**
   - short answers and ellipsis in dialogue (*Ja, klar. — Morgen um drei?*)
   - modal particles from A2 on
   - spoken contractions (*hab, gibt's, geht's*) only in `[spoken]` contexts
   - correct *du/Sie* for the relationship
5. **No textbook tells:**
   - full-sentence echo answers (*Ja, ich habe am Wochenende Fußball gespielt.* as the reply to every question)
   - an unnatural density of the target structure
   - stilted formality in casual scenes
   - English calques
6. **Correct ≠ natural.** Mark contrast pairs with ✅ natural · ⚠️ correct but unusual · ❌ wrong.
7. **No uncertain facts.** No factual claims about institutions, prices, laws or culture unless certain. Keep prices, times and places plausible and generic.
8. **People.** Diverse names reflecting today's German-speaking world. No stereotypes.
9. **Translations are idiomatic English**, not word-for-word. A literal gloss appears only when it shows structure, marked *lit.*
10. **When in doubt, choose the more common alternative.**

## A11. Activity variety

Activity types to rotate (the tag goes in the activity heading or first line):

`role-play` · `info-gap` · `problem-solving` · `story-reconstruction` · `scene-description` · `short-debate` · `opinion` · `ranking` · `decision` · `simulation` · `dialogue-completion` · `error-correction` · `translation-challenge` · `paraphrase` · `transformation` · `listening-specific` · `prediction` · `reading-comprehension` · `summary` · `retelling` · `timed-speaking` · `spontaneous-speaking` · `vocab-retrieval` · `grammar-discovery` · `pattern-noticing` · `mini-project` · `what-would-you-do` · `compare-contrast`

**Rules:**
- Each unit uses at least **6 different types**.
- No two consecutive lessons use the same sequence of activity types.
- The unit's main-task type is not repeated in the next unit.
- Activities get more open with level (A7).

## A12. AI role-play prompt block (standard format)

Always put it in a `text` code block so it can be copied. Fill in the `{placeholders}`.

```text
[ROLE-PLAY — copy this into your AI app, voice mode if possible]
You are {role} in {place}. I am a German learner at level {level}.
Scenario: {situation}. My goal: {goal}.
Rules:
- Speak only German, at {level} level, in short turns (1–3 sentences).
- Stay in role. Ask me follow-up questions. At some point add this complication: {complication}.
- Do NOT correct me during the conversation.
- After {N} turns, or when I say "Ende", step out of the role and give me:
  1. up to 5 of my errors, each with the correction,
  2. 3 more natural phrases I could have used,
  3. one thing I did well.
Start now with your first line.
```

**Writing feedback** uses a separate standard prompt. It is defined in `Resources/Writing_Toolkit.md` when that file is created.

---

# Part B — File standards

## B1. Markdown conventions

- **Flavour:** GitHub-flavoured Markdown, UTF-8. Every file must render correctly in VS Code preview, Obsidian and GitHub.
- **HTML:** only `<details>`, `<summary>` and `<br>`. No other HTML, no CSS, no scripts.
- **Tables** for structured data (word banks, Sentence Map, rubrics). Keep them to 6 columns or fewer where possible.
- **Emphasis:**
  - target forms **bold** in examples
  - English translations in *italics*
  - `code` only for filenames, keys and TSV lines
- **Example line format:**
  `**Ich habe** gestern lange **geschlafen**. → *I slept in yesterday.* [spoken]`
- **Emoji** only as the fixed section icons (B11) and as naturalness markers (B9).
- **No images or audio files** in the repository. Listening uses TTS or external sources (CD-30).

## B2. Heading hierarchy

- `#` **H1**: exactly one per file, the file title.
  - Lessons: `# A2-U01 · L1 — Mein Wochenende`
  - Overview: `# A2-U01 — Erlebnisse · Überblick & Wortschatz`
- `##` **H2**: components, with icon + name, e.g. `## 🔁 Aufwärmen (3-2-1)`, `## 📘 Explanation`
- `###` **H3**: activities, **numbered continuously through the whole file**, with estimated time, e.g. `### 5. Wer hat was gemacht? (~10 min)`
- `####` **H4**: only for subsections inside long explanations.
- Never skip a level. Never use bold text as a fake heading.

## B3. Naming conventions

**IDs** (used in metadata, links, flashcard tags):

| Kind | Format | Examples |
|---|---|---|
| Stage | `A1`, `A2`, `B1` | Sub-stages `A2.1`, `A2.2`, `B1.1`, `B1.2` appear in metadata only |
| Unit | `<stage>-U<nn>` | `A2-U01`, `B1-U12` |
| Lesson | `<unit>-L<n>` | `A2-U01-L1`; `L4` is always the integration lesson |
| A1 section | `<unit>-§<letter>` | `A1-U02-§B` (Schnelltest routing targets) |
| Activity reference | `<lesson> #<number>` | `A2-U01-L2 #5` |
| Review | `<stage>-R<n>` | `A2-R1` |
| Checkpoint | `A1-CP`, `A2-MID`, `A2-EXIT`, `B1-MID`, `B1-EXIT` | |

**File and folder names:**
- ASCII only. Transliterate `ä→ae, ö→oe, ü→ue, ß→ss`. Write `und` instead of `&`.
- Words joined with `_`. No spaces. German title words.
- Unit folders exactly as in Appendix H of `01`: `A2-U01_Erlebnisse/`, `B1-U04_Gesundheit_und_Wohlbefinden/`, …
- Fixed names inside a unit folder:
  - `00_Overview_und_Wortschatz.md`
  - `L4_Anwenden.md`
- New-content lessons: `L1_<Topic>.md`, `L2_<Topic>.md`, `L3_<Topic>.md`, where `<Topic>` is 1–4 ASCII words, e.g. `L1_Mein_Wochenende.md`.
- A1 units: `A1-U01_Ich_und_du.md`.
- Reviews: `A2-R1_Wiederholung.md`.
- Checkpoints: `A1_Checkpoint.md`, `A2_Midpoint_Checkpoint.md`, `A2_Exit_Checkpoint.md`, `B1_Midpoint_Checkpoint.md`, `B1_Exit_Checkpoint.md`.
- Renaming is a local change, provided every link and Appendix H are updated in the same step.

## B4. Metadata and header requirements

**1. YAML front matter** (machine-readable, for audits):

```yaml
---
id: A2-U01-L1
title: Mein Wochenende
level: A2.1
type: lesson            # a1-unit | overview | lesson | integration | review | checkpoint
unit: A2-U01
est_minutes: 75
load: 3                 # 1 light · 2 medium · 3 heavy
prerequisites: [A1-U03, A1-U05]
introduces: [perfekt]   # grammar keys, see table below
recycles: [separable-verbs, time-expressions]
standard: 04_LESSON_STANDARDS v1.0
status: draft           # draft | validated | approved
---
```

**2. Visible header** directly below the H1:

```markdown
> **Level:** A2.1 · **Unit:** [A2-U01 Erlebnisse](00_Overview_und_Wortschatz.md) · **Lesson 1 of 4** · **~75 min** · **Load:** ●●●
> **Before this lesson:** [A1-U03 Mein Tag](../../A1/A1-U03_Mein_Tag.md) · [A1-U05 In der Stadt](../../A1/A1-U05_In_der_Stadt.md)
> **You will be able to:** tell someone what you did at the weekend.
```

**3. Navigation footer** at the end of every lesson:

`← [Previous](…) · [Unit overview](00_Overview_und_Wortschatz.md) · [Next](…) →`

**Grammar keys** for `introduces` / `recycles`. These are kebab-case and follow the rows of Appendix D in `01`. Sub-aspects use a colon, e.g. `perfekt:sein`, `dative:verbs`.

| Area | Keys |
|---|---|
| A1 basics | `present-tense`, `v2-word-order`, `questions`, `gender-plural`, `nom-acc`, `negation`, `possessives`, `separable-verbs`, `modal-verbs`, `imperative`, `time-expressions`, `place-chunks` |
| A2 | `perfekt`, `dative`, `two-way-prepositions`, `verb-final-clauses`, `reflexive-verbs`, `praeteritum-modals`, `adjective-endings`, `comparison`, `indirect-questions`, `verbs-with-prepositions`, `konjunktiv-2`, `connectors`, `future`, `modal-particles` |
| B1 | `praeteritum`, `plusquamperfekt`, `temporal-clauses`, `relative-clauses`, `n-declension`, `zu-infinitive`, `genitive`, `paired-connectors`, `passive`, `lassen`, `word-formation`, `konjunktiv-1` |

Adding a key is a local change. Record it here in the same step.

## B5. Internal linking

- **Relative paths only**, forward slashes, including `.md`. Never absolute paths. Never wiki-links (`[[…]]`).
- **Link text** = ID + title, e.g. `[A1-U03 Mein Tag](../../A1/A1-U03_Mein_Tag.md)`.
- **Link to files, not headings.** Anchors are allowed only to emoji-free headings in `Resources/` and `Docs/`. Lesson headings carry icons, which make anchors unreliable, so they are never anchor targets.
- **Mandatory links:**
  - prerequisites (header)
  - unit overview and previous/next lesson (footer)
  - resources used (Sentence Map, rubrics, toolkits)
  - back-links in 🔗
  - forward links on "use now — explained in …" chunks
- **Forward links to files not yet built** are allowed only to paths fixed in Appendix H of `01`. For future units, always target the unit's `00_Overview_und_Wortschatz.md`, never an `L1_<Topic>.md` whose name isn't known yet. Link checks report these as *planned*, not *broken*. The M8 audit requires zero unresolved links.
- **Learner-facing files never link into `Docs/`.**

## B6. Answer-key conventions

Put the answer in `<details>` **directly after the activity**. Keep a blank line after `</summary>` and before `</details>`; without them, Markdown inside will not render.

```markdown
<details>
<summary>Lösung</summary>

1. **habe** … **gemacht**
2. **bin** … **gefahren** (movement → *sein*)

</details>
```

| Summary label | Use |
|---|---|
| `Lösung` | Closed items with definite answers. Alternatives separated by ` / `. Short reason in brackets when the answer is not obvious. |
| `Beispielantwort` | Open tasks: one natural sample + "other answers are possible" + the success criteria |
| `Hinweis` | Optional hint, placed *before* the `Lösung` block |
| `Transkript` | The hidden text of a TTS listening activity |

**Rules:**
- Every closed item has an answer.
- Every open task has a sample and success criteria.
- Answer keys are checked **item by item** during validation.

## B7. Vocabulary-list conventions

The canonical word bank lives only in `00_Overview_und_Wortschatz.md`. Lessons show a short "New words" box listing the German items, linked to the bank, and do not repeat full entries.

**Word bank sections, in this order:**
1. ★ Active core
2. Recognition
3. Verbs & collocations
4. Chunks & sentence frames
5. Redemittel (by function)
6. Words + prepositions
7. Recycled from

**Table format:**

```markdown
| ★ | Deutsch | Formen | Englisch | Beispiel / Kollokation |
|---|---|---|---|---|
| ★ | die Wohnung | -en | flat, apartment | eine Wohnung **suchen / mieten** |
| ★ | an\|rufen | ruft an – hat angerufen | to call (phone) | Ich **rufe** dich morgen **an**. [spoken] |
```

**Notation:**

| Word class | Notation |
|---|---|
| Nouns | Article + plural: `die Wohnung, -en`. n-declension: `der Kollege, -n (n-Dekl.)`. `(Sg.)` = singular only, `(Pl.)` = plural only |
| Verbs | Separable verbs with `\|` (`an\|rufen`). Irregular forms: A2 gives present + Perfekt (`fahren – fährt – ist gefahren`); from B1 Präteritum is added (`fahren – fährt – fuhr – ist gefahren`). Case and preposition: `helfen + D`, `warten auf + A`, `sich freuen über + A` |
| Adjectives | Irregular comparison: `gut – besser – am besten` |

**Order and tags:** Order entries by topic or function, **not** alphabetically. Register tags go in the example column.

## B8. Flashcard conventions

**In lessons:** a table of 5–15 cards, always production-direction:

```markdown
| You see (prompt) | You say (Deutsch) |
|---|---|
| I went to the cinema yesterday. (Perfekt) | Ich **bin** gestern ins Kino **gegangen**. |
| Situation: you ask a friend about their weekend | Was hast du am Wochenende gemacht? |
| Ich ___ gestern lange ___. (sleep) | habe … geschlafen |
```

**Stage files** (`Resources/Anki/A1.tsv`, `A2.tsv`, `B1.tsv`) use the Anki text-import header and are tab-separated:

```text
#separator:tab
#html:true
#columns:Front	Back	Tags
#tags column:3
I went to the cinema yesterday. (Perfekt)	Ich <b>bin</b> gestern ins Kino <b>gegangen</b>.	A2-U01 A2-U01-L1 grammar
```

- **Tags:** unit ID, lesson ID, and one type out of `vocab`, `chunk`, `grammar`, `phrase`.
- **Front** is never a German prompt asking for English.

## B9. Register labels and naturalness markers

- **Fixed register tags** (CD-11): `[spoken]` `[written]` `[formal]` `[informal]` `[uncommon]`. Combine with a comma: `[spoken, informal]`. Place them after the example.
- **Naturalness markers** for contrast pairs: ✅ natural · ⚠️ correct but unusual · ❌ wrong.
- **Regional variants** are named in prose ("in Austria: *Jänner*"), not with tags.
- **New tags** require updating `01` (CD-11) and `02` first. That is a global change.

## B10. CEFR labelling

- The **level is labelled in metadata and the visible header**, using the sub-stage: A1, A2.1, A2.2, B1.1, B1.2.
- **Objectives and self-checks** use CEFR-style can-do wording tied to a concrete situation: "You can arrange a meeting time by phone", not "You know the dative".
- **Material above the level** that appears in texts is marked `(preview: B1)` and treated as recognition only.
- **Individual exercises** are not CEFR-labelled.
- **Checkpoints** reference the can-do targets in Appendix A of `01`.

## B11. Section icons

Fixed set. Use the same icon and the same heading wording in every file:

🔁 Aufwärmen · 🎯 Ziele · 🔍 Entdecken · 📘 Explanation · 💬 Beispiele · ✍️ Übung · 🧠 Abrufen · 🎭 Aufgabe · 🗣️ Sprechen · 📖 Lesen · 🎧 Hören · 📝 Schreiben · 👄 Aussprache · ⚠️ Typische Fehler · 🔗 Rückblick · ✅ Selbstcheck · 🚀 Challenge · 🃏 Karteikarten

The German section names are a small, fixed piece of immersion. From B1.1 on, `📘 Explanation` becomes `📘 Erklärung`; the explanation itself stays in English (CD-10).

---

# Part C — Quality checklist

**A file is complete only when every item passes.** Results are recorded per batch in [05_VALIDATION_LOG.md](05_VALIDATION_LOG.md). An item that doesn't apply is marked N/A with a reason.

**Linguistic correctness**
- [ ] Every German sentence is grammatically correct: gender, case, endings, verb position, spelling (new orthography)
- [ ] Translations are accurate and idiomatic
- [ ] Every answer key has been checked item by item and is complete

**Naturalness**
- [ ] Every example passes A10 (plausible speaker and situation, no textbook tells)
- [ ] Register tags are used where register matters; correct-but-unusual forms are flagged ⚠️

**CEFR appropriateness**
- [ ] Texts and tasks fit the level in the metadata; anything above level is glossed or marked `(preview)`
- [ ] Objectives are can-do statements tied to situations

**Prerequisite correctness**
- [ ] The file requires nothing scheduled later in Appendices B–D of `01` (except marked chunks)
- [ ] `prerequisites` / `introduces` / `recycles` metadata is accurate

**Scope fidelity**
- [ ] Content matches the unit map (Appendix B); no unapproved additions, removals or moves

**Vocabulary recycling**
- [ ] A8 met: ≥5 (A2) / ≥8 (B1) earlier items needed per lesson; the unit's "Recycled from" list complete; each new ★ item produced ≥3 times

**Retrieval practice**
- [ ] 3-2-1 warm-up present; retrieval spread through the lesson; ≥60% production items; a timed retrieval (A2+); answers hidden

**Communicative usefulness**
- [ ] The task is realistic and needs the lesson's language; grammar is introduced through a need (A9)

**Speaking opportunity**
- [ ] A6 met (at least one speaking activity; the right S-level for the lesson type; success criteria stated)

**Activity variety**
- [ ] A11 met; no repeated sequence of activity types from the previous lesson

**Answer-key completeness**
- [ ] B6 met for every activity

**Internal links**
- [ ] All links resolve, or are *planned* targets fixed in Appendix H; header and footer navigation present

**No unnecessary duplication**
- [ ] No repeated explanations or word-bank entries; references link to `Resources/` instead of copying

**Realistic workload**
- [ ] Time estimates sum within target ±10%; activity count within A4

**Progressive difficulty**
- [ ] More open than the previous lesson or unit where appropriate; scaffolding matches A7; the unit's load rhythm is respected (CD-39)

**Format**
- [ ] YAML front matter + visible header (B4); heading hierarchy (B2); naming (B3); icons (B11)

---

# Part D — File skeletons

These skeletons show structure only. Replace the `{…}` placeholders. Leave out optional components per A3.

## D1. New-content lesson (`L1`–`L3`)

```markdown
---
{YAML per B4}
---
# {Unit ID} · L{n} — {Title}
> {visible header per B4}

## 🔁 Aufwärmen (3-2-1)
### 1. {…} (~7 min)

## 🎯 Ziele
- You can …

## 🔍 Entdecken
### 2. {dialogue/text + noticing questions} (~8 min)

## 📘 Explanation
{Why you need this → 10-point standard → Sentence Map}

## 💬 Beispiele

## ✍️ Übung
### 3. {…} (~10 min)

## 🧠 Abrufen
### 4. {…} (~8 min)

## 🎭 Aufgabe
### 5. {…} (~12 min)

## 🗣️ Sprechen
### 6. {…} (~10 min)

## 📖 Lesen / 🎧 Hören / 📝 Schreiben   {per A3 unit-level rule}

## 👄 Aussprache
## ⚠️ Typische Fehler
## 🔗 Rückblick
## ✅ Selbstcheck
## 🚀 Challenge   {optional}
## 🃏 Karteikarten

← [Previous](…) · [Unit overview](00_Overview_und_Wortschatz.md) · [Next](…) →
```

## D2. Integration lesson (`L4_Anwenden.md`)

Sections in order:
1. YAML + header
2. 🔁 Aufwärmen (whole unit + older material)
3. 🎯 Ziele (the unit can-dos)
4. 🎭 Aufgabe: the unit **main task** (Appendix B)
5. 🗣️ Sprechen: S4, recorded; link to the Story Bank where relevant
6. 📖 Lesen and/or 🎧 Hören (integrated)
7. 📝 Schreiben (mandatory)
8. Mixed review (unit + older units)
9. ✅ Unit quiz: 10 min, production, pass ≥80%, with a "what to redo if not" map
10. ✅ Selbstcheck: unit can-do list
11. 🃏 Review card set (optional)
12. Footer

## D3. Unit overview (`00_Overview_und_Wortschatz.md`)

Sections in order:
1. YAML + header
2. 🎯 Unit can-dos
3. Unit roadmap: a table of `L1`–`L4` with times and links
4. Prerequisites
5. Grammar in this unit: a summary with links, not a re-explanation
6. Main task
7. Word bank: B7 sections, ending with "Recycled from"
8. Story Bank link
9. Flashcard note: cards go to `Resources/Anki/<stage>.tsv`

## D4. A1 unit (`A1-U0x_*.md`)

Sections in order:
1. YAML + header
2. 🎯 Ziele
3. Schnelltest: 10 min, production, timed
4. Routing table: score/speed → which `§` sections to do
5. `## §A {Topic}`, `## §B …`. Each section has a short refresh explanation → examples → timed retrieval → practice. Each carries its ID `A1-U0x-§X`.
6. 🎭 Fluency task and 🗣️ Sprechen (everyone does these)
7. 👄 Aussprache
8. ⚠️ Typische Fehler
9. ✅ Selbstcheck
10. 🃏 Karteikarten
11. Footer

## D5. Cumulative review (`<stage>-R<n>_Wiederholung.md`)

Sections in order:
1. YAML + header
2. Scope and weighting table (50/30/20, naming the units)
3. Sittings 1–3, each with interleaved mixed practice (retrieval + grammar choices + vocabulary)
4. Error clinic: top 5 from the Error Log
5. Speaking recycling: a role-play or Story Bank task
6. Progress Tracker update instructions
7. ✅ Selbstcheck
8. 🔑 Answer keys inline

## D6. Checkpoint

Sections in order:
1. YAML + header
2. What is assessed (Appendix A can-dos)
3. Instructions and timing
4. Parts: Lesen · Hören · Schreiben · Sprechen · integrated scenario (+ fluency for the A1 Gate)
5. Scoring with `Resources/Rubrics.md`
6. Thresholds (Appendix G)
7. Results table
8. Remediation map
9. 🔑 Answer keys
