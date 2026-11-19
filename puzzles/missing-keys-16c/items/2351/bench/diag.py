"""diag.py - why the two builders fail on this pair. Counts only, never values.

    python3 diag.py beam      align.beam_read: where the pointer goes, what the path is made of
    python3 diag.py tied      tied.search in both modes (an unmarked base spells its consonant, or is free)
    python3 diag.py signs     how often the things each builder must learn are seen
Reads inputs/ only. Prints no sign value and no table.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
sys.path.insert(0, os.path.join(HERE, ".."))
import align, tied  # noqa: E402

CIPHER, PLAIN = os.path.join(HERE, "inputs", "cipher-A.txt"), os.path.join(HERE, "inputs", "plain-A.txt")


def kinds(ops):
    c = {}
    for o in ops:
        c[o[0]] = c.get(o[0], 0) + 1
    return " ".join(f"{k}={c[k]}" for k in sorted(c))


def track(ops, n, m):
    """pointer at every 100th unit, beside the place a straight line would put it"""
    return " ".join(f"{i}:{ops[i][1]}/{round(i * m / n)}" for i in range(0, n, 100))


def gaps(ops, lac):
    """runs of units in a gap: how many, how many open at a hole, the longest"""
    runs, at_hole, cur = [], 0, 0
    for o in ops:
        if o[0] == "G":
            if cur == 0 and lac[o[1]]:
                at_hole += 1
            cur += 1
        elif cur:
            runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    return f"gap runs {len(runs)}, opened at a hole {at_hole}, longest {max(runs or [0])} units, units in gaps {sum(runs)}"


def main():
    what = sys.argv[1]
    units, P, wb, lac, _ = align.load_pair(CIPHER, PLAIN)
    n, m = len(units), len(P)
    print(f"units {n}, of them unread {sum(u.sym == '?' for u in units)}; plain letters {m}; holes {sum(lac)}")
    if what == "beam":
        known = {}
        for k in range(align.AB_PASSES):
            sc, tab, ops = align.beam_read(units, P, lac, None, known)
            rows = align.beam_rows(units, P, tab, ops, known)
            known = {r["unit"]: r["value"] for r in rows if r["status"] == "certain"}
            st = {}
            for r in rows:
                st[r["status"]] = st.get(r["status"], 0) + 1
            print(f"pass {k + 1}: score {sc:.1f}; path {kinds(ops)}; rows {st}")
            print(f"  pointer ends at {ops[-1][2]} of {m}; {gaps(ops, lac)}")
            print(f"  unit:pointer/straight line  {track(ops, n, m)}")
        last = ops[-1][2]
        print(f"the soft pass needs the corridor (band {align.AB_BAND} round the beam's path) to reach the last "
              f"letter: the path ends {m - last} letters short, so {'no path' if m - last > align.AB_BAND + 3 else 'a path'}")
    elif what == "tied":
        mk = tied.markable(units)
        for free in (False, True):
            tied.BARE_FREE[0] = free
            sc, tab, ops = tied.search(units, P, lac, mk)
            rows = tied.rows_from(P, tab, ops)
            st, kinds_of = {}, {}
            for r in rows:
                st[r["status"]] = st.get(r["status"], 0) + 1
                if r["status"] != "unknown":
                    kinds_of[r["unit"][0]] = kinds_of.get(r["unit"][0], 0) + 1
            print(f"unmarked base {'free' if free else 'spells its consonant'}: score {sc:.1f}; path {kinds(ops)}; "
                  f"rows {st}; marked by kind {kinds_of}")
            print(f"  pointer ends at {ops[-1][2]} of {m}; {gaps(ops, lac)}")
            print(f"  unit:pointer/straight line  {track(ops, n, m)}")
    elif what == "signs":
        cnt = {}
        for u in units:
            if u.sym != "?":
                cnt[u.sym] = cnt.get(u.sym, 0) + 1
        mk = tied.markable(units)
        marked = {s: c for s, c in cnt.items() if tied.split(s)[0] in mk and tied.split(s)[1] in tied.VMARKS}
        bare = {s: c for s, c in cnt.items() if s in mk}
        other = {s: c for s, c in cnt.items() if s not in marked and s not in bare}
        f = lambda d, k: sum(1 for c in d.values() if c >= k)
        for name, d in (("base with a vowel mark", marked), ("markable base, unmarked", bare), ("other sign", other)):
            print(f"{name}: {len(d)} kinds over {sum(d.values())} places; seen 3+ {f(d, 3)}, 5+ {f(d, 5)}, 10+ {f(d, 10)}")
        print(f"tied entries a marked sign needs: {len(mk)} bases and {len(tied.VMARKS)} marks for "
              f"{sum(marked.values())} places ({sum(marked.values()) / (len(mk) + 5):.0f} places an entry; "
              f"untied, {sum(marked.values()) / max(1, len(marked)):.0f} places a sign)")


if __name__ == "__main__":
    main()
