"""Combine 08's summer verdicts with 02's ice-onset windows. Standard library only.

Usage: python3 -I window.py results/target_schneider.txt [more target files ...]

02 windows (analysis/02-ice-onset/README.md, "Implied eruption date"):
  extratropical analogues 1452.9-1453.7, tropical analogues 1452.0-1453.1.
08 season segments (decimal years): Jan-Jun 1452 = [1452.0, 1452.5),
  Jul-Dec 1452 = [1452.5, 1453.0), Jan-Jun 1453 = [1453.0, 1453.5),
  Jul-Dec 1453 = [1453.5, 1454.0).
Rules (README pre-registration): XE_1452 governs Jan-Jun 1452 for X, TE_1452 for T;
late_1452 governs Jul-Dec 1452 for both; Jan-Jun 1453 is always allowed (1453 is cold);
late_1453 governs Jul-Dec 1453 for both.
"""
import sys

ICE = {"X": (1452.9, 1453.7), "T": (1452.0, 1453.1)}
SEG = {"jan-jun 1452": (1452.0, 1452.5), "jul-dec 1452": (1452.5, 1453.0),
       "jan-jun 1453": (1453.0, 1453.5), "jul-dec 1453": (1453.5, 1454.0)}


def verdicts(path):
    v = {}
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if p[0] == "VERDICT":
            v[p[1]] = p[2]
    return v


def allowed_segments(v, cls):
    key = {"X": "XE_1452", "T": "TE_1452"}[cls]
    return {"jan-jun 1452": v[key] == "allowed",
            "jul-dec 1452": v["late_1452"] == "allowed",
            "jan-jun 1453": True,
            "jul-dec 1453": v["late_1453"] == "allowed"}


def intersect(a, b):
    lo, hi = max(a[0], b[0]), min(a[1], b[1])
    return (lo, hi) if hi > lo else None


def merge(iv):
    iv = sorted(i for i in iv if i)
    out = []
    for lo, hi in iv:
        if out and lo <= out[-1][1] + 1e-9:
            out[-1] = (out[-1][0], max(out[-1][1], hi))
        else:
            out.append((lo, hi))
    return out


def main(paths):
    for path in paths:
        v = verdicts(path)
        print(f"# {path}: " + "  ".join(f"{k}={x}" for k, x in sorted(v.items())))
        for cls in ("X", "T"):
            seg = allowed_segments(v, cls)
            pieces = []
            for name, (lo, hi) in SEG.items():
                part = intersect((lo, hi), ICE[cls])
                status = "allowed" if seg[name] else "disfavored"
                shown = f"[{part[0]:.2f}, {part[1]:.2f})" if part else "empty"
                print(f"  {cls} {name:13s} summer verdict {status:10s}  ∩ ice {ICE[cls]} = {shown}")
                if seg[name] and part:
                    pieces.append(part)
            win = merge(pieces)
            print(f"  {cls} combined window: " + (" ∪ ".join(f"{a:.2f}-{b:.2f}" for a, b in win) or "empty"))
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
