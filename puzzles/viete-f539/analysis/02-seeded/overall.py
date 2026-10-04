"""Secondary measure (reported, not gating): whole-text token accuracy = coverage + (1 - coverage) * unseeded accuracy."""
import re
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
cells = defaultdict(list)
for line in (HERE / "runs.txt").read_text().splitlines():
    m = re.match(r"(\w+) (\d+) seed \d+: unseeded acc ([\d.]+) coverage ([\d.]+)", line)
    kind, k, acc, cov = m.group(1), int(m.group(2)), float(m.group(3)), float(m.group(4))
    cells[(kind, k)].append(cov + (1 - cov) * acc)
for (kind, k), v in sorted(cells.items()):
    v.sort()
    print(f"{kind:4s} {k:3d}  whole-text accuracy {[round(x, 3) for x in v]}  median {v[len(v)//2]:.3f}")
