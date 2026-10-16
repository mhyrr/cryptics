"""Cross-check: the C solver's decryption must equal the Python reference (independent code).
Also times a pure-Python IDP, to record why the inner loop is in C. Usage: python3 test_engine.py"""
import array, os, random, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transpo

def cross_check(trials=300):
    rnd = random.Random(7); ok = 0
    for _ in range(trials):
        n = rnd.randint(30, 700); pt = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(n))
        a, b = rnd.randint(2, 30), rnd.randint(2, 30); k1 = rnd.sample(range(a), a); k2 = rnd.sample(range(b), b)
        conv = rnd.choice(["CC", "CR"]); open("out/_t.txt", "w").write(transpo.double_enc(pt, k1, k2, conv))
        o = subprocess.run(["out/dtsolve", "decrypt", "out/_t.txt", ",".join(map(str, k1)), ",".join(map(str, k2)), conv],
                           capture_output=True, text=True).stdout.strip()
        ok += o == pt
    print(f"C decrypt == Python reference: {ok}/{trials}")
    return ok == trials

def python_idp_timing():
    B = array.array("f"); B.fromfile(open("out/lm_es_2.bin", "rb"), 676)
    t = [ord(c) - 65 for c in open("out/t1.txt").read() if c.isalpha()]
    n, w1 = len(t), 20; r, ex = divmod(n, w1)
    lo = [k * r + max(0, ex - (w1 - k)) for k in range(w1)]; hi = [k * r + min(k, ex) for k in range(w1)]
    t0 = time.time(); reps = 3
    for _ in range(reps):
        best = {}
        for i in range(w1):
            for j in range(w1):
                if i != j:
                    best[i, j] = max(sum(B[t[a + x] * 26 + t[b + x]] for x in range(r))
                                     for a in range(lo[i], hi[i] + 1) for b in range(lo[j], hi[j] + 1))
    print(f"pure-Python IDP (no greedy step), w1=20: {reps / (time.time() - t0):.2f} per second")

if __name__ == "__main__":
    good = cross_check(); python_idp_timing(); sys.exit(0 if good else 1)
