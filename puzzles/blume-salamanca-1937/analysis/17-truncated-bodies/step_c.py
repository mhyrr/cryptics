"""Step C of 17-truncated-bodies: 4 x 4 turning grille on T2 with a preamble of a letters (a = 1-15).

Body T2[a : a + 144] = nine blocks of 16. Code path: 06-grille/grille.py, imported and called unchanged:
grille.best over all 1,024 keys (grille.ALL), standard use (grille.dec) and inverse use (grille.enc), score
grille.qscore (Spanish quadgrams per letter). The search is exhaustive, so no solver seed exists.

Plants (C2): 10 per offset class a = 5, 10, 15, from a separate named stream. A plant is a uniform random
preamble of a letters, then 144 letters of Spanish telegraph plaintext (01-solver/plaintext.telegram, 27738
excluded) through the grille in the standard use (as 06's controls), then 16 - a plaintext letters in clear,
160 letters in all. The search sees letters a .. a + 143, as the target does.

Usage (from this folder, in this order):
  python3 -I step_c.py controls      -> out/c_controls.jsonl, prints C2 and C3
  python3 -I step_c.py target        -> out/c_target.jsonl (refuses unless thresholds-AC.md holds the C3 line)
  python3 -I step_c.py summary > result-C.txt
"""
import hashlib, json, os, random, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, SOLVER); sys.path.insert(0, os.path.join(HERE, "..", "06-grille")); os.chdir(SOLVER)
import plaintext  # noqa: E402
import grille  # noqa: E402  (chdirs to 01-solver too)

OUT = os.path.join(HERE, "out")
THRESH_FILE = os.path.join(HERE, "thresholds-AC.md")
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BODY = 144
CLASSES = (5, 10, 15)
PER_CLASS = 10
PASS_CLASS = 0.80
OFFSETS = range(1, 16)
USES = (("standard", grille.dec), ("inverse", grille.enc))

assert 27738 in plaintext.HELDOUT_EXCLUDE
assert len(grille.ALL) == 1024


def t2():
    t = "".join(c for c in open(os.path.join(HERE, "../../sources/telegram-2.txt")).read().upper() if c.isalpha())
    h = hashlib.sha256(t.encode()).hexdigest()
    assert len(t) == 160 and h.startswith("8fd5cfb8") and h.endswith("e17a644"), h
    return t


def scan(body):
    """Every key in both uses, 06's grille.best; returns [(score, use, name, decryption)] best first."""
    rows = []
    for use, f in USES:
        for s, name, o, bc in grille.best(body, len(grille.ALL), f):
            rows.append((s, use, name, f(body, o, bc)))
    rows.sort(key=lambda r: -r[0])
    return rows


def control_jobs():
    rng = random.Random("17-C-plant")
    return [dict(i=n, a=a, plant_seed=rng.randrange(1 << 30)) for n, a in enumerate(a for a in CLASSES
                                                                                    for _ in range(PER_CLASS))]


def run_control(job):
    a = job["a"]; rnd = random.Random(job["plant_seed"])
    pt = plaintext.telegram(160 - a, rnd); body, clear = pt[:BODY], pt[BODY:]
    name, o, bc = rnd.choice(grille.ALL)
    pre = "".join(rnd.choice(AZ) for _ in range(a))
    ct = pre + grille.enc(body, o, bc) + clear
    assert len(ct) == 160 and grille.dec(ct[a:a + BODY], o, bc) == body
    rows = scan(ct[a:a + BODY])
    best = rows[0]
    tw = next(r for r in rows if r[3] != body)          # best wrong key: any decryption that is not the body
    return dict(job, true_key=str(name), true_score=round(grille.qscore(body), 4), best_score=round(best[0], 4),
                best_use=best[1], best_key=str(best[2]), exact=best[3] == body, wrong_max=round(tw[0], 4),
                wrong_use=tw[1], wrong_key=str(tw[2]), wrong_in_place=round(sum(x == y for x, y in zip(tw[3], body)) / BODY, 4),
                wrong_relation=relation(name, tw[2]) if tw[1] == "standard" else "inverse use")


def relation(true, other):
    """'start rotated by r' when other is the true grille started r quarter-turns on (same direction, same
    grid reading); otherwise 'other'."""
    (c0, cw0, b0), (c1, cw1, b1) = true, other
    for r in (1, 2, 3):
        if (cw1, b1) == (cw0, b0) and tuple((c + r) % 4 for c in c0) == tuple(c1):
            return f"start rotated by {r}"
    return "other"


def threshold(ctrl):
    low_true = min(r["true_score"] for r in ctrl)
    wrong = max(r["wrong_max"] for r in ctrl)
    return low_true, wrong, round((low_true + wrong) / 2, 4)


def read(name):
    p = os.path.join(OUT, name)
    return [json.loads(x) for x in open(p)] if os.path.exists(p) else []


def main():
    mode = sys.argv[1]
    os.makedirs(OUT, exist_ok=True)
    if mode == "controls":
        recs = [run_control(j) for j in control_jobs()]
        with open(os.path.join(OUT, "c_controls.jsonl"), "w") as f:
            for r in recs:
                f.write(json.dumps(r) + "\n")
        print_controls(recs)
    elif mode == "target":
        ctrl = read("c_controls.jsonl"); assert len(ctrl) == len(CLASSES) * PER_CLASS
        low, wrong, thr = threshold(ctrl)
        assert f"THRESHOLD-C: {thr:.4f}" in open(THRESH_FILE).read(), "C3 threshold not written first"
        assert all(class_pass(ctrl, a) for a in CLASSES), "a control class failed; targets not read"
        t = t2(); recs = []
        for a in OFFSETS:
            rows = scan(t[a:a + BODY])
            s, use, name, dec = rows[0]
            r = dict(a=a, body=f"T2[{a}:{a + BODY}]", score=round(s, 4), use=use, key=str(name),
                     second=round(rows[1][0], 4), median=round(statistics.median(x[0] for x in rows), 4),
                     threshold=thr, candidate=s > thr)
            if r["candidate"]:
                r["dec200"] = dec[:200]      # recorded for the main thread; not read further here
            recs.append(r)
            print(f"a={a:2} best {s:.4f} ({use}, {name}) second {rows[1][0]:.4f} median {r['median']:.4f}"
                  + ("  *** ABOVE THRESHOLD ***" if r["candidate"] else ""), flush=True)
        with open(os.path.join(OUT, "c_target.jsonl"), "w") as f:
            for r in recs:
                f.write(json.dumps(r) + "\n")
    elif mode == "summary":
        summary()


def class_pass(ctrl, a):
    rs = [r for r in ctrl if r["a"] == a]
    return len(rs) == PER_CLASS and sum(r["exact"] for r in rs) >= PASS_CLASS * len(rs)


def print_controls(ctrl):
    print("C2. Controls: 4 x 4 grille, standard use, preamble of a letters; search over 1,024 keys x 2 uses")
    print("  a   exact   true-key score min..max   best wrong-key score")
    for a in CLASSES:
        rs = [r for r in ctrl if r["a"] == a]
        print(f"  {a:2}  {sum(r['exact'] for r in rs):2}/{len(rs)} {'pass' if class_pass(ctrl, a) else 'FAIL'}   "
              f"{min(r['true_score'] for r in rs):.4f}..{max(r['true_score'] for r in rs):.4f}         "
              f"{max(r['wrong_max'] for r in rs):.4f}")
    rel = {}
    for r in ctrl:
        rel[r["wrong_relation"]] = rel.get(r["wrong_relation"], 0) + 1
    print(f"  Best wrong key per plant: letters in place {min(r['wrong_in_place'] for r in ctrl):.2f}.."
          f"{max(r['wrong_in_place'] for r in ctrl):.2f}; relation to the true key: "
          + ", ".join(f"{k} {v}" for k, v in sorted(rel.items())))
    above = sum(r["true_score"] < max(x["wrong_max"] for x in ctrl) for r in ctrl)
    low, wrong, thr = threshold(ctrl)
    print(f"  Within every plant the true key ranks first. Across plants the ranges overlap: {above}/{len(ctrl)} "
          f"true-key scores lie below the highest wrong-key score.")
    print(f"C3. Lowest true-key score {low:.4f}; highest wrong-key score {wrong:.4f}; halfway:")
    print(f"THRESHOLD-C: {thr:.4f}")


def summary():
    ctrl, tgt = read("c_controls.jsonl"), read("c_target.jsonl")
    print("17-truncated-bodies, step C: 4 x 4 turning grille on T2[a : a + 144] (06-grille/grille.py code path)\n")
    print_controls(ctrl)
    print("\n  per plant: a, true key, true score, best score, best use, exact; best wrong key: score, letters in")
    print("  place, relation to the true key")
    for r in ctrl:
        print(f"    a={r['a']:2} {r['true_key']} true {r['true_score']:.4f} best {r['best_score']:.4f} "
              f"{r['best_use']} exact={r['exact']} | wrong {r['wrong_max']:.4f} {r['wrong_use']} in place "
              f"{r['wrong_in_place']:.2f} {r['wrong_relation']}")
    print("\nC4. Target: best key over both uses per offset; * = above threshold")
    print("  a   body           best     use       key                          second   median")
    for r in tgt:
        print(f"  {r['a']:2}  {r['body']:13}  {r['score']:.4f}{'*' if r['candidate'] else ' '} {r['use']:9} "
              f"{r['key']:28} {r['second']:.4f}  {r['median']:.4f}")
    if tgt:
        b = max(tgt, key=lambda r: r["score"])
        print(f"\nBest over all offsets: {b['score']:.4f} at a={b['a']}; threshold {b['threshold']:.4f}; "
              f"margin {b['score'] - b['threshold']:+.4f}")
    cands = [r for r in tgt if r["candidate"]]
    print(f"Candidates (score above threshold): {len(cands)}")
    for r in cands:
        print(f"  {r['body']} {r['use']} {r['key']} score {r['score']:.4f}\n  letters: {r['dec200']}")


if __name__ == "__main__":
    main()
