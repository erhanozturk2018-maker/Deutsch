"""Vocabulary-recycling checker (see Docs/04_LESSON_STANDARDS.md, A8).

Usage:  python tools/check_vocab.py <unit folder> [--min N]
        e.g. python tools/check_vocab.py GERMAN_LEARNING_PLAN/A2/A2-U01_Erlebnisse

Reads the ★ rows of the unit's word bank (00_Overview_und_Wortschatz.md) and counts
how often each item's key word occurs in the unit's lesson files (L1–L4), outside
answer keys is NOT distinguished: this is a heuristic exposure count, not a proof
of production. Items below --min (default 3) are listed for review.

Key word = the first word of the "Deutsch" cell after removing articles, "sich",
separable bars and bracketed parts; for verbs, the Perfekt participle from the
"Formen" cell is also counted (e.g. "ist angekommen" -> "angekommen").
"""
import re
import sys
from pathlib import Path

ARTICLES = {"der", "die", "das", "sich", "ein", "eine"}


def stems(deutsch, formen):
    keys = set()
    for alt in re.split(r"[·/]", deutsch):
        words = [w for w in re.sub(r"\(.*?\)|\*|\\\|", "", alt).replace("|", "").split()
                 if w.lower() not in ARTICLES]
        if words:
            w = words[0].strip(".,!?–")
            if len(w) > 2:
                keys.add(w[:-2] if w.endswith("en") and len(w) > 5 else w)
    m = re.search(r"(?:hat|ist)\s+([\wäöüß]+)", formen)
    if m:
        keys.add(m.group(1))
    return keys


def main():
    folder = Path(sys.argv[1])
    minimum = int(sys.argv[sys.argv.index("--min") + 1]) if "--min" in sys.argv else 3
    bank = (folder / "00_Overview_und_Wortschatz.md").read_text(encoding="utf-8")
    lessons = " ".join(p.read_text(encoding="utf-8") for p in sorted(folder.glob("L*.md"))).lower()
    low = []
    rows = [l for l in bank.splitlines() if l.startswith("| ★ |")]
    for row in rows:
        cells = [c.strip().replace("\x00", "|") for c in
                 row.replace("\\|", "\x00").strip("|").split("|")]
        deutsch, formen = cells[1], cells[2] if len(cells) > 2 else ""
        keys = stems(deutsch, formen)
        count = max((len(re.findall(re.escape(k.lower()), lessons)) for k in keys), default=0)
        if count < minimum:
            low.append((count, deutsch))
    print(f"{len(rows)} ★ items; {len(low)} below {minimum} occurrences in the lessons:")
    for count, item in sorted(low):
        print(f"  {count:2}  {item}")
    sys.exit(1 if low else 0)


if __name__ == "__main__":
    main()
