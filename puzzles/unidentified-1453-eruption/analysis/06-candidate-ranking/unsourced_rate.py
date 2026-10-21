"""How often is an eVolv2k v4 eruption of UE 1453's size without a named source?

Run: python3 -I unsourced_rate.py ../02-ice-onset/data/evolv2k_v4.tab
Writes results/unsourced_rate.txt.
"""
import pathlib
import sys

UNSOURCED = {"N/A", "Unidentifed", "Unidentified", ""}


def load(path):
    rows, body = [], False
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("*/"):
            body = True
            continue
        if not body or not line[:1].isdigit() and not line[:1] == "-":
            continue
        f = line.split("\t")
        rows.append((int(f[0]), float(f[7]), f[10].strip()))
    return rows


def main():
    rows = load(sys.argv[1])
    rows.sort(key=lambda r: -r[1])
    out = [f"eVolv2k v4: {len(rows)} events, {min(r[0] for r in rows)} to {max(r[0] for r in rows)} CE"]
    rank = next(i for i, r in enumerate(rows, 1) if r[0] == 1453)
    out.append(f"1453: {rows[rank - 1][1]:.2f} Tg S, rank {rank} of {len(rows)} by VSSI")
    for floor in (5.0, 9.0):
        for label, sel in (("all years", rows), ("before 1500", [r for r in rows if r[0] < 1500])):
            big = [r for r in sel if r[1] >= floor]
            n_u = sum(r[2] in UNSOURCED for r in big)
            out.append(f">= {floor:g} Tg S, {label}: {len(big)} events, {n_u} without a named source")
    out.append("")
    out.append("Top 30 by VSSI (year, Tg S, location):")
    out += [f"  {y}\t{s:.2f}\t{loc}" for y, s, loc in rows[:30]]
    text = "\n".join(out) + "\n"
    res = pathlib.Path(__file__).parent / "results" / "unsourced_rate.txt"
    res.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
