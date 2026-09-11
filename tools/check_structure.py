"""Structure checker for course files (see Docs/04_LESSON_STANDARDS.md).

Usage:  python tools/check_structure.py [path ...]      (default: all of GERMAN_LEARNING_PLAN)

Checks every Markdown file:
  - exactly one H1 (outside code blocks)
  - <details> / </details> balanced, and every <summary> followed by a blank line
  - no heading level skipped (e.g. H2 -> H4)
For files with YAML front matter (lessons, units, reviews, checkpoints, diagnostic):
  - required keys present: id, title, level, type, est_minutes, standard, status
  - activity headings "### N. ..." numbered 1..n without gaps or repeats
  - activity headings carry a time estimate "(~N min)" (except for type diagnostic)
  - type a1-unit: every section ID "A1-Uxx-§X" listed in Docs/03 section map appears in the file
  - flashcard table present ("| You see") for a1-unit, lesson, integration, overview
Exit code 1 if any problem is found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "GERMAN_LEARNING_PLAN"
REQUIRED = ["id", "title", "level", "type", "est_minutes", "standard", "status"]
CARD_TYPES = {"a1-unit", "lesson", "integration", "overview"}
A1_SECTIONS = {
    "A1-U01": "ABCD", "A1-U02": "ABCDE", "A1-U03": "ABC", "A1-U04": "ABCD", "A1-U05": "ABC",
}


def strip_fences(lines):
    out, fence = [], False
    for line in lines:
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            out.append("")
        else:
            out.append("" if fence else line)
    return out


def yaml_block(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            data[k.strip()] = v.split("#")[0].strip()
    return data


def check(path):
    problems = []
    text = path.read_text(encoding="utf-8")
    lines = strip_fences(text.splitlines())
    h1 = [l for l in lines if re.match(r"^# ", l)]
    if len(h1) != 1:
        problems.append(f"{len(h1)} H1 headings")
    if text.count("<details>") != text.count("</details>"):
        problems.append(f"<details> {text.count('<details>')} vs </details> {text.count('</details>')}")
    raw = text.splitlines()
    for i, l in enumerate(raw):
        if l.strip().startswith("<summary>") and i + 1 < len(raw) and raw[i + 1].strip() != "":
            problems.append(f"line {i+2}: no blank line after <summary>")
    last = 0
    for l in lines:
        m = re.match(r"^(#{1,6}) ", l)
        if m:
            lvl = len(m.group(1))
            if last and lvl > last + 1:
                problems.append(f"heading level skip before: {l[:50]}")
            last = lvl
    meta = yaml_block(text)
    if meta is not None:
        for k in REQUIRED:
            if k not in meta:
                problems.append(f"YAML key missing: {k}")
        nums = [int(m.group(1)) for l in lines for m in [re.match(r"^### (\d+)\. ", l)] if m]
        if nums and nums != list(range(1, len(nums) + 1)):
            problems.append(f"activity numbering not 1..n: {nums}")
        if meta.get("type") != "diagnostic":
            for l in lines:
                if re.match(r"^### \d+\. ", l) and not re.search(r"~\d+(–\d+)? min", l):
                    problems.append(f"activity without time estimate: {l[:60]}")
        if meta.get("type") == "a1-unit":
            uid = meta.get("id", "")
            for letter in A1_SECTIONS.get(uid, ""):
                if f"`{uid}-§{letter}`" not in text:
                    problems.append(f"section ID {uid}-§{letter} missing")
        if meta.get("type") in CARD_TYPES and "| You see" not in text:
            problems.append("flashcard table missing")
    return problems


def main():
    targets = [Path(a) for a in sys.argv[1:]] or [COURSE]
    files = []
    for t in targets:
        files += sorted(t.rglob("*.md")) if t.is_dir() else [t]
    bad = 0
    for f in files:
        probs = check(f)
        if probs:
            bad += 1
            print(f"✗ {f.relative_to(ROOT)}")
            for p in probs:
                print(f"    - {p}")
    print(f"{len(files)} files checked, {bad} with problems")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
