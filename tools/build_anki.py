"""Build Anki import files from the flashcard tables in the course.

Usage:  python tools/build_anki.py

For each stage folder (A1, A2, B1) under GERMAN_LEARNING_PLAN/, every Markdown
table whose header starts with "| You see" is read (see Docs/04_LESSON_STANDARDS.md,
B8). Rows become cards in GERMAN_LEARNING_PLAN/Resources/Anki/<stage>.tsv:

    Front (prompt) <TAB> Back (German) <TAB> Tags

Tags = stage, unit ID and lesson ID (from the file's YAML `id`).
Markdown **bold** / *italic* become <b> / <i>. Exact duplicate cards are dropped.
The lesson tables are the single source: never edit the .tsv files by hand.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "GERMAN_LEARNING_PLAN"
OUT = COURSE / "Resources" / "Anki"
HEADER = "#separator:tab\n#html:true\n#columns:Front\tBack\tTags\n#tags column:3\n"


def yaml_id(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("id:"):
                return line.split(":", 1)[1].strip()
    return None


def md_to_html(cell):
    cell = cell.strip().replace("\\|", "|")
    cell = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", cell)
    cell = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<i>\1</i>", cell)
    return cell.replace("\t", " ")


def cards_in(path):
    text = path.read_text(encoding="utf-8")
    fid = yaml_id(text) or path.stem
    unit = re.match(r"^(A1|A2|B1)-(U\d\d|R\d)", fid)
    tags = [fid.split("-")[0]]
    if unit:
        tags.append(unit.group(0))
    if fid not in tags:
        tags.append(fid)
    lines = text.splitlines()
    cards, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith("| You see"):
            i += 2  # skip header + separator row
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                row = lines[i].strip().replace("\\|", "\x00")
                cells = [c.replace("\x00", "\\|") for c in row.strip("|").split("|")]
                if len(cells) >= 2 and cells[0].strip() and cells[1].strip():
                    cards.append((md_to_html(cells[0]), md_to_html(cells[1]), " ".join(tags)))
                i += 1
        else:
            i += 1
    return cards


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for stage in ("A1", "A2", "B1"):
        folder = COURSE / stage
        if not folder.exists():
            continue
        seen, cards = set(), []
        for md in sorted(folder.rglob("*.md")):
            for card in cards_in(md):
                if card[:2] not in seen:
                    seen.add(card[:2])
                    cards.append(card)
        if not cards:
            continue
        out = OUT / f"{stage}.tsv"
        with out.open("w", encoding="utf-8", newline="\n") as f:
            f.write(HEADER)
            for front, back, tags in cards:
                f.write(f"{front}\t{back}\t{tags}\n")
        print(f"{stage}: {len(cards)} cards -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
