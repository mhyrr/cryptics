"""Independent verifier for experiment 29. Shares no code with rowcol.py, run29.py or setsolve.py: its own
row-and-column encryption, rearrangement, decryption and quadgram score (same model file, lm_es_4.bin).

Checks, from the stored records:
- controls.jsonl and calibration.jsonl: the stored ciphertext is the stored body-encryption under the stored
  keys (body regenerated: controls from plaintext.telegram(plant_seed), calibration from the P1/M1 slice);
  the solver's stored order re-scores to the stored score and re-measures to the stored adjacency/recovery.
- noise.jsonl and target.jsonl: the shuffled or real telegram, rearranged, decrypted with the stored order,
  re-scores to the stored score; the target reading's first 80 letters are re-derived.
Run (from this folder): python3 -I verify29.py
"""
import array, json, os, random, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
DIVE = os.path.join(HERE, "..", "..")
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Q4 = array.array("f")
with open(os.path.join(HERE, "..", "01-solver", "out", "lm_es_4.bin"), "rb") as fh:
    Q4.fromfile(fh, 26 ** 4)


def tel(name):
    t = "".join(c for c in open(os.path.join(DIVE, "sources", f"telegram-{name[1]}.txt")).read().upper() if c.isalpha())
    assert len(t) == {"T1": 615, "T2": 160}[name]
    return t


def enc(seq, w, ck, rk, d):
    h = len(seq) // w
    cols = sorted(range(w), key=ck.__getitem__); rows = sorted(range(h), key=rk.__getitem__)
    cell = (lambda r, c: seq[r * w + c]) if d == "D1" else (lambda r, c: seq[c * h + r])
    if d == "D1":
        return [cell(r, c) for c in cols for r in rows]
    return [cell(r, c) for r in rows for c in cols]


def sets_of(ct, w, d):
    """Rearranged sets, by direct formula."""
    L = len(ct); h = L // w
    if d == "D1":
        return [[ct[k * h + i] for k in range(w)] for i in range(h)]
    return [[ct[j + i * w] for i in range(h)] for j in range(w)]


def score(rows):
    tot = cnt = 0.0
    for r in rows:
        v = [ord(x) - 65 for x in r]
        for t in range(len(v) - 3):
            tot += Q4[((v[t] * 26 + v[t + 1]) * 26 + v[t + 2]) * 26 + v[t + 3]]; cnt += 1
    return tot / cnt


def adjacency(idx_sets, order):
    good = tot = 0
    for s in idx_sets:
        v = [s[j] for j in order]
        for x, y in zip(v, v[1:]):
            tot += 1; good += (y == x + 1)
    return good / tot


def calib_text(name):
    md = open(os.path.join(DIVE, "sources", "historical-evidence", "calibration-telegrams.md"), encoding="utf-8").read()
    head = "\n## P1." if name == "P1" else "\n### M1 "
    raw = re.search(r"```\n(.*?)```", md[md.index(head):], re.S).group(1)
    return "".join(c for c in unicodedata.normalize("NFD", raw.upper()) if c in AZ)


def check_plants(path, body_of):
    bad = 0; recs = [json.loads(l) for l in open(path) if l.strip()]
    for x in recs:
        body = body_of(x); w, d = x["w"], x["direction"]
        ct = "".join(enc(body, w, x["ckey"], x["rkey"], d))
        ok = ct == x["ct"]
        rows = ["".join(s[j] for j in x["order"]) for s in sets_of(ct, w, d)]
        isets = sets_of(enc(list(range(len(body))), w, x["ckey"], x["rkey"], d), w, d)
        a = adjacency(isets, x["order"])
        ok &= abs(score(rows) - x["score"]) < 1e-3 and abs(a - x["adj"]) < 1e-3 and (a >= 0.90) == x["recovered"]
        bad += not ok
    return len(recs), bad


def main():
    sys.path.insert(0, os.path.join(HERE, "..", "01-solver")); os.chdir(os.path.join(HERE, "..", "01-solver"))
    import plaintext
    L = {"T1": 615, "T2": 160}
    n, b = check_plants(os.path.join(HERE, "controls.jsonl"),
                        lambda x: plaintext.telegram(L[x["text"]], random.Random(x["plant_seed"])))
    print(f"controls: {n} re-checked, {b} mismatches")
    if os.path.exists(os.path.join(HERE, "calibration.jsonl")):
        C = {k: calib_text(k) for k in ("P1", "M1")}
        n, b = check_plants(os.path.join(HERE, "calibration.jsonl"), lambda x: C[x["source"]][x["start"]:x["start"] + 615])
        print(f"calibration: {n} re-checked, {b} mismatches")
    for name in ("noise", "target"):
        p = os.path.join(HERE, f"{name}.jsonl")
        if not os.path.exists(p):
            continue
        bad = 0; recs = [json.loads(l) for l in open(p) if l.strip()]
        for x in recs:
            letters = list(tel(x["text"]))
            if x.get("shuffle_seed") is not None:
                random.Random(x["shuffle_seed"]).shuffle(letters)
            rows = ["".join(s[j] for j in x["order"]) for s in sets_of(letters, x["w"], x["direction"])]
            ok = abs(score(rows) - x["score"]) < 1e-3
            if "reading" in x:
                ok &= "".join(rows)[:80] == x["reading"]
            bad += not ok
        print(f"{name}: {len(recs)} re-decrypted and re-scored, {bad} mismatches")
        if name == "target":
            for x in sorted(recs, key=lambda x: (x["cell"], x["kind"])):
                if x["kind"] == "telegram":
                    rows = ["".join(s[j] for j in x["order"]) for s in sets_of(tel(x["text"]), x["w"], x["direction"])]
                    print(f"  {x['cell']}: {score(rows):.4f}  {''.join(rows)[:80]}")


if __name__ == "__main__":
    main()
