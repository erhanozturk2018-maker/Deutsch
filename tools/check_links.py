"""Link checker for the German A1->B1 curriculum.

Usage:  python tools/check_links.py [--strict]

Checks every relative Markdown link and GitHub-style heading anchor in all
.md files of the workspace (code blocks and inline code are ignored).

A link to a file that does not exist yet is reported as PLANNED (not BROKEN)
if its target is a planned course file listed in Docs/01_CURRICULUM_DECISIONS.md,
Appendix H (see Docs/04_LESSON_STANDARDS.md, B5). With --strict (used in the
M8 audit), PLANNED links count as failures too.

Exit code 1 if any BROKEN link (or, with --strict, any PLANNED link) is found.
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "GERMAN_LEARNING_PLAN"
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")


def strip_code(text):
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else re.sub(r"`[^`]*`", "", line))
    return out


def slug(heading):
    s = heading.strip().lower()
    s = "".join(ch for ch in s if ch in " -_" or unicodedata.category(ch)[0] in "LN")
    return s.replace(" ", "-")


def anchors(path):
    result, counts = set(), {}
    for line in strip_code(path.read_text(encoding="utf-8")):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            base = slug(m.group(2))
            n = counts.get(base, 0)
            result.add(base if n == 0 else f"{base}-{n}")
            counts[base] = n + 1
    return result


def planned_targets():
    """Course paths (relative to GERMAN_LEARNING_PLAN, '/'-separated) planned in Appendix H."""
    text = (ROOT / "Docs" / "01_CURRICULUM_DECISIONS.md").read_text(encoding="utf-8")
    planned = {"README.md"}
    for folder in set(re.findall(r"\b((A1|A2|B1)-U\d\d_[A-Za-z_]+)/", text)):
        stage = folder[1]
        for f in ("00_Overview_und_Wortschatz.md", "L4_Anwenden.md"):
            planned.add(f"{stage}/{folder[0]}/{f}")
    for name in set(re.findall(r"\b([A-Za-z0-9_-]+\.(?:md|tsv))\b", text)):
        m = re.match(r"^(A1|A2|B1)[-_]", name)
        if m:
            planned.add(f"{m.group(1)}/{name}")
        for sub in ("Resources", "Resources/Anki", "Learner_Workbook", "00_Curriculum"):
            planned.add(f"{sub}/{name}")
    for stage in ("A1", "A2", "B1"):
        planned.add(f"{stage}/README.md")
    return planned


def main():
    strict = "--strict" in sys.argv
    planned = planned_targets()
    counts = {"OK": 0, "PLANNED": 0, "BROKEN": 0}
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for lineno, line in enumerate(strip_code(md.read_text(encoding="utf-8")), 1):
            for target in LINK.findall(line):
                if re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
                    continue
                file_part, _, anchor = target.partition("#")
                dest = md if not file_part else (md.parent / file_part).resolve()
                if dest.exists():
                    status = "OK" if not anchor or anchor in anchors(dest) else "BROKEN"
                else:
                    try:
                        rel = dest.relative_to(COURSE).as_posix()
                    except ValueError:
                        rel = None
                    status = "PLANNED" if rel in planned and not anchor else "BROKEN"
                counts[status] += 1
                if status != "OK":
                    print(f"{status:8} {md.relative_to(ROOT)}:{lineno} -> {target}")
    total = sum(counts.values())
    print(f"{total} links: {counts['OK']} ok, {counts['PLANNED']} planned, {counts['BROKEN']} broken")
    failed = counts["BROKEN"] or (strict and counts["PLANNED"])
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
