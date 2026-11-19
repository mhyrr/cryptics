"""compare_tables.py - the blind table of the bench (run 2, `tied.py blind`) against key-v0.tsv, sign by sign.

    python3 compare_tables.py            -> results/compare-v2-v0.tsv

The bench is closed (bench/README.md, "Result"), so values may now be looked at. Both tables were built from
letter A alone. key-v0.tsv has entries (B: base, M: mark, W: whole sign); it is expanded to every sign of
letter A's merged text that it gives a value to, exactly as bench/score.py does. Of the blind table only rows
marked `certain` or `probable` count. bench/runs/v2_soft.key.tsv is untracked; `python3 tied.py blind
bench/inputs/cipher-A.txt bench/inputs/plain-PE.txt out.tsv` writes the same file.
Each sign is also reduced to the entry that carries the difference (a mark, a base, or the whole sign), which
is what a test can decide.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
VM = ("1", "3", "4", "5", "~")
BLIND = os.path.join(HERE, "bench", "runs", "v2_soft.key.tsv")
CIPHER = os.path.join(HERE, "bench", "inputs", "cipher-A.txt")
OUT = os.path.join(HERE, "results", "compare-v2-v0.tsv")


def read(path):
    return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))


def expand(t, signs):
    out = {}
    for s in signs:
        b, _, m = s.partition("+")
        if "W:" + s in t:
            out[s] = t["W:" + s]
        elif m in VM and "B:" + b in t and "M:" + m in t:
            out[s] = t["B:" + b] + t["M:" + m]
    return out


def entry(sign, blind_value, t):
    """The key entry a blind sign value would add or change, given key-v0's entries t."""
    b, _, m = sign.partition("+")
    if m not in VM:
        return "W:" + sign, blind_value
    if "M:" + m not in t and "B:" + b in t and blind_value.startswith(t["B:" + b]):
        return "M:" + m, blind_value[len(t["B:" + b]):]
    if "B:" + b not in t and "M:" + m in t and blind_value.endswith(t["M:" + m]):
        return "B:" + b, blind_value[:-len(t["M:" + m])]
    if "M:" + m in t and blind_value.endswith(t["M:" + m]):
        return "B:" + b, blind_value[:-len(t["M:" + m])]
    return "W:" + sign, blind_value


def main():
    toks = [x for ln in open(CIPHER, encoding="utf-8") if not ln.startswith("#") for x in ln.split() if x != "?"]
    t = {r["unit"]: r["value"] for r in read(os.path.join(HERE, "key-v0.tsv"))}
    ans = expand(t, set(toks))
    rows = read(BLIND)
    blind = {r["unit"]: r for r in rows if r["status"] in ("certain", "probable")}
    out = ["class\tsign\tblind_value\tblind_status\tblind_hits\tblind_misses\tv0_value\tplaces_in_A\tentry\tentry_value"]
    n = {"agree": 0, "differ": 0, "blind_only": 0, "v0_only": 0}
    entries = {}
    for s in sorted(set(blind) | set(ans), key=lambda s: (-toks.count(s), s)):
        r = blind.get(s)
        if r and s in ans:
            cl = "agree" if r["value"] == ans[s] else "differ"
        else:
            cl = "blind_only" if r else "v0_only"
        n[cl] += 1
        e, ev = entry(s, r["value"], t) if r and cl in ("differ", "blind_only") else ("", "")
        if e:
            entries.setdefault((e, ev), []).append(s)
        out.append("\t".join([cl, s, r["value"] if r else "", r["status"] if r else "", r["support"] if r else "",
                              r["conflict"] if r else "", ans.get(s, ""), str(toks.count(s)), e, ev]))
    out.append("")
    out.append(f"# signs of letter A that key-v0 values\t{len(ans)}")
    out.append(f"# blind rows marked certain or probable\t{len(blind)}")
    out += [f"# {k}\t{v}" for k, v in n.items()]
    out.append("# entries that carry the differences (entry, blind value, key-v0 value, signs)")
    for (e, ev), ss in sorted(entries.items()):
        out.append(f"# {e}\t{ev}\t{t.get(e, '-')}\t{' '.join(sorted(ss))}")
    open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(o for o in out if o.startswith("#") or o.startswith("differ") or o.startswith("blind_only")))


if __name__ == "__main__":
    main()
