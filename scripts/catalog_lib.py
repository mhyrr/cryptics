"""Shared loader for catalog entries. Standard library only (Python 3.11+)."""
from __future__ import annotations

import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "catalog" / "entries"

AXES = ("mystery", "material", "solvable", "compute", "verifiable", "crowding")
KINDS = {
    "cipher", "constructed-text", "allegory", "emblem", "fragment", "inscription",
    "riddle", "attribution", "scripture", "musical", "visual-text",
}
STATUSES = {"unsolved", "partial", "contested", "solved", "likely-hoax", "likely-noise"}
CONFIDENCES = {"high", "medium", "low"}
REQUIRED_SECTIONS = (
    "What it is",
    "What is unsolved",
    "What survives",
    "Prior attempts and current consensus",
    "What a solution would have to do",
    "Why the scores",
    "Sources",
)

FENCE = re.compile(r"^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n(.*)\Z", re.S)


@dataclass
class Entry:
    path: Path
    meta: dict
    body: str
    problems: list[str] = field(default_factory=list)

    @property
    def slug(self) -> str:
        return self.meta.get("slug", self.path.stem)

    @property
    def scores(self) -> dict[str, int]:
        return self.meta.get("scores", {})

    def score(self, axis: str) -> int:
        return int(self.scores.get(axis, 0))


def parse(path: Path) -> Entry:
    text = path.read_text(encoding="utf-8")
    m = FENCE.match(text)
    if not m:
        return Entry(path, {}, text, [f"{path.name}: no +++ frontmatter fence"])
    front, body = m.group(1), m.group(2)
    problems: list[str] = []
    try:
        meta = tomllib.loads(front)
    except tomllib.TOMLDecodeError as e:
        return Entry(path, {}, body, [f"{path.name}: TOML error: {e}"])
    return Entry(path, meta, body, problems)


def validate(entry: Entry) -> list[str]:
    p = list(entry.problems)
    if p:
        return p
    name = entry.path.name
    meta = entry.meta
    for key in ("title", "slug", "kind", "era", "origin", "language", "status", "confidence", "tags"):
        if key not in meta:
            p.append(f"{name}: missing field '{key}'")
    if meta.get("slug") != entry.path.stem:
        p.append(f"{name}: slug '{meta.get('slug')}' != filename stem '{entry.path.stem}'")
    if meta.get("kind") not in KINDS:
        p.append(f"{name}: kind '{meta.get('kind')}' not in {sorted(KINDS)}")
    if meta.get("status") not in STATUSES:
        p.append(f"{name}: status '{meta.get('status')}' not in {sorted(STATUSES)}")
    if meta.get("confidence") not in CONFIDENCES:
        p.append(f"{name}: confidence '{meta.get('confidence')}' not in {sorted(CONFIDENCES)}")
    scores = meta.get("scores")
    if not isinstance(scores, dict):
        p.append(f"{name}: missing [scores] table")
    else:
        for axis in AXES:
            v = scores.get(axis)
            if not isinstance(v, int) or not 1 <= v <= 5:
                p.append(f"{name}: scores.{axis} = {v!r}, must be an integer 1–5")
        extra = set(scores) - set(AXES)
        if extra:
            p.append(f"{name}: unknown score axes {sorted(extra)}")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", entry.body, re.M):
            p.append(f"{name}: missing section '## {section}'")
    if not re.search(r"^- (PRIMARY|SCHOLARLY|SECONDARY|CLAIMANT|POPULAR)\b", entry.body, re.M):
        p.append(f"{name}: Sources section has no tiered '- TIER — ...' lines")
    return p


def load_all(strict: bool = True) -> list[Entry]:
    entries = [parse(p) for p in sorted(ENTRIES.glob("*.md"))]
    bad = [msg for e in entries for msg in validate(e)]
    if bad and strict:
        print("\n".join(bad), file=sys.stderr)
        sys.exit(1)
    return entries
