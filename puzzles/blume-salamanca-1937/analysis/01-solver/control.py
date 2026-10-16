"""Matched planted controls for the double columnar solver.

Each trial: telegraph-style held-out plaintext (plaintext.py), random keys of the given
lengths, encrypted by the Python reference (transpo.py), solved by out/dtsolve exactly as
the target will be (same convention, language model, seconds). Results to out/<tag>.jsonl.

Usage: python3 control.py TAG N SECONDS WORKERS CONV LANG "w1xw2,w1xw2,..." TRIALS_EACH [N2]
  N2 > 0 adds a second plaintext of N2 letters under the same keys (joint attack).
  "RxS" with R, S as ranges "12-14x15-17" draws lengths uniformly from the ranges.
"""
import json, os, random, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transpo, plaintext

def parse_range(s):
    a, _, b = s.partition("-"); return int(a), int(b or a)

def shift_acc(dec, pt, maxs=40):
    """Best fraction of letters in place over cyclic shifts |s| <= maxs. An incomplete
    rectangle admits keys that read the right text displaced by a letter or a row."""
    n = len(pt)
    return max(sum(dec[i] == pt[(i + s) % n] for i in range(n)) for s in range(-maxs, maxs + 1)) / n

def one(job):
    tag, i, n, n2, secs, conv, lang, w1, w2, seed = job
    rnd = random.Random(seed)
    pt = plaintext.telegram(n, rnd, lang)
    k1 = rnd.sample(range(w1), w1); k2 = rnd.sample(range(w2), w2)
    d = f"out/{tag}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/{i}_ct.txt", "w").write(transpo.double_enc(pt, k1, k2, conv))
    open(f"{d}/{i}_pt.txt", "w").write(pt)
    args = ["out/dtsolve", "solve", f"{d}/{i}_ct.txt", str(w1), str(w2), conv, lang, str(seed), str(secs), f"{d}/{i}_pt.txt"]
    if n2:
        pt2 = plaintext.telegram(n2, rnd, lang)
        open(f"{d}/{i}_ct2.txt", "w").write(transpo.double_enc(pt2, k1, k2, conv)); args.append(f"{d}/{i}_ct2.txt")
    out = subprocess.run(args, capture_output=True, text=True).stdout.strip().splitlines()
    fin = json.loads(out[-1])
    open(f"{d}/{i}_dec.txt", "w").write(fin["pt"])
    first_ok = next((json.loads(l)["t"] for l in out if shift_acc(json.loads(l)["pt"], pt) >= 0.95), None)
    rec = {"trial": i, "w1": w1, "w2": w2, "n": n, "n2": n2, "secs": secs, "conv": conv, "lang": lang, "seed": seed,
           "acc": round(shift_acc(fin["pt"], pt), 4), "acc_inplace": fin["acc"], "score": fin["score"], "idp": fin["idp"], "iters": fin["iter"], "t_first_ok": first_ok,
           "true_score": None}
    # score of the true plaintext under the same model, via the solver's decrypt + an independent Python scorer
    return rec, pt

def quad_per_letter(t, lang, _c={}):
    import array
    if lang not in _c:
        a = array.array("f"); a.fromfile(open(f"out/lm_{lang}_4.bin", "rb"), 26 ** 4); _c[lang] = a
    q = _c[lang]; v = [ord(c) - 65 for c in t]
    return sum(q[((v[i] * 26 + v[i + 1]) * 26 + v[i + 2]) * 26 + v[i + 3]] for i in range(len(v) - 3)) / (len(v) - 3)

def main():
    tag, n, secs, workers, conv, lang, spec, each = sys.argv[1:9]
    n, secs, workers, each = int(n), int(secs), int(workers), int(each)
    n2 = int(sys.argv[9]) if len(sys.argv) > 9 else 0
    rnd = random.Random(hash(tag) & 0xffffffff)
    jobs, i = [], 0
    for part in spec.split(","):
        a, b = part.split("x"); r1, r2 = parse_range(a), parse_range(b)
        for _ in range(each):
            jobs.append((tag, i, n, n2, secs, conv, lang, rnd.randint(*r1), rnd.randint(*r2), rnd.randrange(1 << 30))); i += 1
    with open(f"out/{tag}.jsonl", "w") as f, ThreadPoolExecutor(workers) as ex:
        for rec, pt in ex.map(one, jobs):
            rec["true_score"] = round(quad_per_letter(pt, lang), 4)
            f.write(json.dumps(rec) + "\n"); f.flush()
            print(f"{rec['w1']}x{rec['w2']} acc={rec['acc']:.3f} score={rec['score']:.3f} true={rec['true_score']:.3f} first_ok={rec['t_first_ok']} iters={rec['iters']}", flush=True)

if __name__ == "__main__":
    main()
