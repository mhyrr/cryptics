"""Do T1 and T2 come from the same language, the same convention and the same system?
C1 homogeneity of letter counts (split null, per-letter Fisher p with min-p calibration);
C2 which of Spanish / Italian / Portuguese each telegram picks, with a plant null;
C3 the X and F counts under each other's rates and under Spanish plants;
C4 letter class and odd letters by position inside the five-letter group (shuffle null);
C5 charge-per-word arithmetic from the forms (sources/headers.md).
Definitions: README.md, Method. Usage (from this folder): python3 -I one_or_two.py > result.txt
C1 seed stability: python3 -I one_or_two.py --seeds > seeds.txt
"""
import bisect, math, os, random, sys
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext

AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LANGS = ("es", "it", "pt")

def load(p):
    return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())

def pearson(table):
    """Pearson chi-square of a list of rows; cells with zero expected count are skipped."""
    rows = [sum(r) for r in table]; cols = [sum(c) for c in zip(*table)]; n = sum(rows)
    chi = 0.0
    for i, r in enumerate(table):
        for j, o in enumerate(r):
            e = rows[i] * cols[j] / n
            if e > 0:
                chi += (o - e) ** 2 / e
    return chi

def hyper_two_sided(K, n, N):
    """Two-sided hypergeometric p for every possible count k (0..min(K, n)) of a letter in the n-letter part,
    given K of it in N pooled letters: the sum of every outcome no more probable than k."""
    lo, hi = max(0, n - (N - K)), min(K, n)
    tot = math.comb(N, n)
    pmf = {k: math.comb(K, k) * math.comb(N - K, n - k) / tot for k in range(lo, hi + 1)}
    return {k: min(1.0, sum(q for q in pmf.values() if q <= pk * (1 + 1e-9))) for k, pk in pmf.items()}

def binom_cdf(k, n, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))

# ---------------- C1
def c1(t1, t2, seed=11001, verbose=True):
    if verbose:
        print("== C1 homogeneity: T1 (615) vs T2 (160), 2 x 26 letter table")
    c1c, c2c = Counter(t1), Counter(t2)
    pooled = t1 + t2; N, n2 = len(pooled), len(t2)
    K = {x: c1c[x] + c2c[x] for x in AZ}
    live = [x for x in AZ if K[x] > 0]
    def chi_from_t2(k2):
        return pearson([[K[x] - k2[x] for x in live], [k2[x] for x in live]])
    obs = chi_from_t2(c2c)
    ptab = {x: hyper_two_sided(K[x], n2, N) for x in AZ}
    pobs = {x: ptab[x][c2c[x]] for x in AZ}
    rnd = random.Random(seed)
    letters = list(pooled); S = 20000
    chis = []; minps = []
    for _ in range(S):
        rnd.shuffle(letters)
        k2 = Counter(letters[:n2])
        chis.append(chi_from_t2(k2))
        minps.append(min(ptab[x][k2[x]] for x in AZ))
    ge = sum(v >= obs - 1e-9 for v in chis)
    chis.sort(); minps.sort()
    cal = {x: bisect.bisect_right(minps, pobs[x] * (1 + 1e-9)) / S for x in AZ}
    if not verbose:
        return (ge + 1) / (S + 1), cal["F"]
    print(f"letters entering: {len(live)} (W absent from both)")
    print(f"chi2 = {obs:.1f}; split-null median {chis[S // 2]:.1f}, 95th percentile {chis[int(0.95 * S)]:.1f}; "
          f"global p = {(ge + 1) / (S + 1):.4f} ({S} splits)")
    print("per letter, sorted by Fisher p (T1 count, T2 count, T2 expected from pooled, Fisher p, min-p calibrated p):")
    for x in sorted(AZ, key=lambda x: pobs[x]):
        e2 = K[x] * n2 / N
        print(f"  {x}: T1 {c1c[x]:3d}  T2 {c2c[x]:3d}  T2 exp {e2:5.2f}  p {pobs[x]:.4f}  calibrated {cal[x]:.4f}")
    print(f"X: T1 6 / T2 0 -> Fisher p {pobs['X']:.4f}, calibrated {cal['X']:.4f}")
    print(f"F: T1 5 / T2 7 -> Fisher p {pobs['F']:.4f}, calibrated {cal['F']:.4f}")
    print(f"min-p null: 5th percentile {minps[int(0.05 * S)]:.4f}, 1st percentile {minps[int(0.01 * S)]:.4f}")

# ---------------- C2
def c2(tel):
    print("\n== C2 same language: log-likelihood of letter counts under telegraph-style es / it / pt")
    rnd = random.Random(12001)
    logf = {}
    for lang in LANGS:
        ref = Counter()
        for _ in range(40):
            ref.update(plaintext.telegram(10000, rnd, lang, "telegraph"))
        tot = sum(ref.values())
        logf[lang] = {x: math.log((ref[x] + 0.5) / (tot + 13)) for x in AZ}
    def ll(t):
        c = Counter(t)
        return {lang: sum(c[x] * logf[lang][x] for x in AZ) for lang in LANGS}
    def rank(lls):
        r = sorted(LANGS, key=lambda g: -lls[g]); return tuple(r), lls[r[0]] - lls[r[1]]
    prnd = random.Random(12002); P = 1000
    picks = {}
    for name, t in tel.items():
        L = ll(t); r, llr = rank(L)
        picks[name] = r[0]
        print(f"{name} ({len(t)} letters): LL es {L['es']:.2f}, it {L['it']:.2f}, pt {L['pt']:.2f}; "
              f"ranking {' > '.join(r)}; LLR best vs second = {llr:.2f} (natural log)")
        print(f"  plants of each language at {len(t)} letters ({P} each):")
        print(f"  {'plant':5} {'first es':>8} {'first it':>8} {'first pt':>8} {'same ranking':>12} "
              f"{'first ' + r[0] + ' & LLR>=obs':>18} {'median LLR':>10}")
        for lang in LANGS:
            first = Counter(); same = 0; strong = 0; llrs = []
            for _ in range(P):
                pr, pl = rank(ll(plaintext.telegram(len(t), prnd, lang, "telegraph")))
                first[pr[0]] += 1; llrs.append(pl)
                same += pr == r
                strong += pr[0] == r[0] and pl >= llr
            llrs.sort()
            print(f"  {lang:5} {first['es'] / P:8.3f} {first['it'] / P:8.3f} {first['pt'] / P:8.3f} "
                  f"{same / P:12.3f} {strong / P:18.3f} {llrs[P // 2]:10.2f}")
    print(f"T1 picks {picks['T1']}, T2 picks {picks['T2']}: "
          f"{'same' if picks['T1'] == picks['T2'] else 'DIFFERENT'} language")

# ---------------- C3
def c3(t1, t2):
    print("\n== C3 same convention: X and F counts")
    nx1, nf1, nf2 = t1.count("X"), t1.count("F"), t2.count("F")
    nx2 = t2.count("X")
    p0x = (1 - nx1 / len(t1)) ** len(t2)
    pf = binom_cdf(nf1, len(t1), nf2 / len(t2))
    print(f"at T1's X rate {nx1}/{len(t1)}: P({nx2} X in {len(t2)} letters) = {p0x:.4f} (binomial)")
    print(f"at T2's F rate {nf2}/{len(t2)}: P(<= {nf1} F in {len(t1)} letters) = {pf:.3g} (binomial; "
          f"expected {len(t1) * nf2 / len(t2):.1f})")
    rnd = random.Random(13001); P = 2000
    s160 = [plaintext.telegram(len(t2), rnd, "es", "telegraph") for _ in range(P)]
    s615 = [plaintext.telegram(len(t1), rnd, "es", "telegraph") for _ in range(P)]
    q = lambda xs, f: sum(map(f, xs)) / P
    print(f"Spanish telegraph plants, {P} at each length:")
    print(f"  P(0 X at 160)  = {q(s160, lambda s: s.count('X') == 0):.3f}   "
          f"(mean X at 160: {sum(s.count('X') for s in s160) / P:.2f})")
    print(f"  P(<=5 F at 615) = {q(s615, lambda s: s.count('F') <= nf1):.3f}   "
          f"(mean F at 615: {sum(s.count('F') for s in s615) / P:.2f})")
    print(f"  P(>=6 X at 615) = {q(s615, lambda s: s.count('X') >= nx1):.4f}   "
          f"(mean X at 615: {sum(s.count('X') for s in s615) / P:.2f})")
    print(f"  P(>=7 F at 160) = {q(s160, lambda s: s.count('F') >= nf2):.4f}   "
          f"(mean F at 160: {sum(s.count('F') for s in s160) / P:.2f})")

# ---------------- C4
VOW, FREQ, ODD = set("AEIOU"), set("NRSTLCDMP"), "XFKZQYJ"

def pos_table(labels, k):
    t = [[0] * 5 for _ in range(k)]
    for i, c in enumerate(labels):
        t[c][i % 5] += 1
    return t

def perm_test(labels, k, seed, S=10000):
    obs = pearson(pos_table(labels, k))
    rnd = random.Random(seed); lab = list(labels); ge = 0
    for _ in range(S):
        rnd.shuffle(lab)
        ge += pearson(pos_table(lab, k)) >= obs - 1e-9
    return obs, (ge + 1) / (S + 1)

def c4(tel):
    print("\n== C4 group structure: position inside the five-letter group (1-5)")
    for name, t in tel.items():
        cls = [0 if c in VOW else 1 if c in FREQ else 2 for c in t]
        odd = [1 if c in ODD else 0 for c in t]
        ca, pa = perm_test(cls, 3, 14001)
        cb, pb = perm_test(odd, 2, 14002)
        ta, tb = pos_table(cls, 3), pos_table(odd, 2)
        print(f"{name}: (a) class x position chi2 = {ca:.2f} (df 8), p = {pa:.4f}")
        for lab, row in zip(("vowels", "freq cons", "rare cons"), ta):
            print(f"      {lab:10} " + " ".join(f"{v:4d}" for v in row))
        print(f"    (b) {{{','.join(ODD)}}} vs rest x position chi2 = {cb:.2f} (df 4), p = {pb:.4f}")
        print(f"      {'odd set':10} " + " ".join(f"{v:4d}" for v in tb[1]))
        print("      by letter (positions 1-5):")
        for x in ODD:
            row = [0] * 5
            for i, c in enumerate(t):
                if c == x:
                    row[i % 5] += 1
            if sum(row):
                print(f"        {x}: " + " ".join(f"{v:3d}" for v in row) + f"   (n {sum(row)})")

# ---------------- C5
def c5():
    print("\n== C5 paperwork arithmetic (readings from sources/headers.md)")
    w1, w2 = 125, 34
    a, b, pencil = 49.90 / w1, 14.00 / w2, 15.98 / w2
    print(f"T1: 49.90 / {w1} words = {a:.4f} per word")
    print(f"T2: 14.00 / {w2} words = {b:.4f} per word (stamped); 15.98 / {w2} = {pencil:.4f} (pencilled, = 0.47)")
    print(f"ratio T2/T1 per word: stamped {b / a:.4f}; pencilled {pencil / a:.4f}")
    print(f"T2 stamped / pencilled: 14.00 / 15.98 = {14.00 / 15.98:.4f}")
    print(f"0.47 x {w1} = {0.47 * w1:.2f}; 49.90 / {0.47 * w1:.2f} = {49.90 / (0.47 * w1):.4f}")
    print(f"0.47 x 100 = {0.47 * 100:.2f}; 0.47 x 20 = {0.47 * 20:.2f}; 0.47 x 5 = {0.47 * 5:.2f} "
          "(compare figures pencilled on T1's reverse: 47.-, 9.40)")

# ---------------- C4 controls (added after the first result, at the coordinator's request)
import transpo
CONS = [c for c in AZ if c not in VOW]

def fast_perm_p(labels, k, rnd, smax=1000, stop_at=None):
    """Permutation p of the Pearson chi-square of label x group position, the same null as perm_test.
    With every group full the columns all hold n/5, so chi2 = sum_i (5/R_i) sum_j o_ij^2 - n. A random
    relabelling is drawn by sampling positions for every class but the largest. If stop_at is set, stop once
    that many null values reach the observed one (Besag-Clifford); p is then already above the 0.05 line."""
    n = len(labels); g = n // 5
    R = [labels.count(c) for c in range(k)]
    big = max(range(k), key=lambda c: R[c])
    small = [c for c in range(k) if c != big]
    def chi(tab):
        s = 0.0
        for c in range(k):
            if R[c]:
                s += 5 / R[c] * sum(v * v for v in tab[c])
        return s - n
    obs = chi(pos_table(labels, k))
    m = n - R[big]; ge = 0; done = 0
    for _ in range(smax):
        pos = rnd.sample(range(n), m)
        tab = [[0] * 5 for _ in range(k)]; j = 0
        for c in small:
            row = tab[c]
            for q in pos[j:j + R[c]]:
                row[q % 5] += 1
            j += R[c]
        tab[big] = [g - sum(tab[c][p] for c in small) for p in range(5)]
        done += 1
        if chi(tab) >= obs - 1e-9:
            ge += 1
            if stop_at and ge >= stop_at:
                return obs, (ge + 1) / (smax + 1)  # a lower bound; the full run could only be larger
    return obs, (ge + 1) / (done + 1)

def telegram_words(k, rnd, lang="es"):
    """Word-level twin of plaintext.telegram: same drops, stops and spelled quantities, kept as words."""
    w = plaintext.heldout_words(lang); i = rnd.randrange(len(w) - 5000); out = []
    while len(out) < k:
        t = w[i]; i += 1
        if t == ".":
            if out and out[-1] != plaintext.STOP[lang]:
                out.append(plaintext.STOP[lang])
            continue
        if t in plaintext.DROP[lang] and rnd.random() < 0.7:
            continue
        if rnd.random() < 0.03:
            out.append(rnd.choice(plaintext.QTY[lang]) + rnd.choice(plaintext.UNIT[lang]))
        out.append(t)
    return out[:k]

def codeword(kind, rnd):
    if kind == "random":
        return "".join(rnd.choice(AZ) for _ in range(5))
    pat = "CVCVC" if kind == "cvcvc" or rnd.random() < 0.5 else "VCVCV"
    return "".join(rnd.choice(CONS) if p == "C" else rnd.choice("AEIOU") for p in pat)

def code_plant(n, kind, rnd):
    book = {}
    return "".join(book.setdefault(wd, codeword(kind, rnd)) for wd in telegram_words(n // 5, rnd))

def dc_null_plant(n, every, rnd):
    """Spanish telegraph plaintext, forward double columnar (widths 8-25), then a uniform random null at group
    position 3 of every group (every=1), of groups 1, 3, 5, ... (every=2), or none (every=0)."""
    G = n // 5
    nulled = [every and gi % every == 0 for gi in range(G)]
    pt = plaintext.telegram(n - sum(nulled), rnd, "es", "telegraph")
    w1, w2 = rnd.randint(8, 25), rnd.randint(8, 25)
    ct = transpo.double_enc(pt, rnd.sample(range(w1), w1), rnd.sample(range(w2), w2), "CC")
    out, j = [], 0
    for gi in range(G):
        if nulled[gi]:
            out.append(ct[j:j + 2] + rnd.choice(AZ) + ct[j + 2:j + 4]); j += 4
        else:
            out.append(ct[j:j + 5]); j += 5
    s = "".join(out); assert len(s) == n and j == len(ct)
    return s

def c4_controls(tel):
    print("\n== C4 controls (added after the first result): power of the two C4 tests")
    vrnd = random.Random(16001)
    print("check: fast null (10,000 draws, no early stop) on the telegrams, against the shuffle p values above")
    for name, t in tel.items():
        cls = [0 if c in VOW else 1 if c in FREQ else 2 for c in t]
        odd = [1 if c in ODD else 0 for c in t]
        _, pa = fast_perm_p(cls, 3, vrnd, 10000); _, pb = fast_perm_p(odd, 2, vrnd, 10000)
        print(f"  {name}: (a) p = {pa:.4f}, (b) p = {pb:.4f}")
    fams = [("code, uniform random codewords", lambda n, r: code_plant(n, "random", r)),
            ("code, CVCVC codewords", lambda n, r: code_plant(n, "cvcvc", r)),
            ("code, CVCVC or VCVCV per codeword", lambda n, r: code_plant(n, "mixed", r)),
            ("DC + null at position 3, every group", lambda n, r: dc_null_plant(n, 1, r)),
            ("DC + null at position 3, every 2nd group", lambda n, r: dc_null_plant(n, 2, r)),
            ("DC, no nulls (negative control)", lambda n, r: dc_null_plant(n, 0, r))]
    P = 200
    print(f"{P} plants per family per length; null up to 1,000 draws, stopped once 51 reach the observed value")
    print(f"  {'family':42} {'n':>4} {'(a) p<.01':>9} {'(a) p<.05':>9} {'(b) p<.01':>9} {'(b) p<.05':>9} "
          f"{'either<.01':>10}")
    for fi, (fname, make) in enumerate(fams):
        for n in (615, 160):
            prnd = random.Random(17000 + 10 * fi + (n == 160))
            trnd = random.Random(18000 + 10 * fi + (n == 160))
            a1 = a5 = b1 = b5 = e1 = 0
            for _ in range(P):
                t = make(n, prnd)
                cls = [0 if c in VOW else 1 if c in FREQ else 2 for c in t]
                odd = [1 if c in ODD else 0 for c in t]
                _, pa = fast_perm_p(cls, 3, trnd, 1000, 51)
                _, pb = fast_perm_p(odd, 2, trnd, 1000, 51)
                a1 += pa < 0.01; a5 += pa < 0.05; b1 += pb < 0.01; b5 += pb < 0.05
                e1 += pa < 0.01 or pb < 0.01
            print(f"  {fname:42} {n:4d} {a1 / P:9.3f} {a5 / P:9.3f} {b1 / P:9.3f} {b5 / P:9.3f} {e1 / P:10.3f}")

def main():
    t1, t2 = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")
    assert len(t1) == 615 and len(t2) == 160
    tel = {"T1": t1, "T2": t2}
    if "--seeds" in sys.argv:  # C1 stability: python3 -I one_or_two.py --seeds > seeds.txt
        for sd in (11001, 11002, 11003, 11004, 11005):
            g, f = c1(t1, t2, sd, verbose=False)
            print(f"C1 seed {sd}: global p = {g:.4f}, F calibrated p = {f:.4f}")
        return
    c1(t1, t2)
    c2(tel)
    c3(t1, t2)
    c4(tel)
    c5()
    c4_controls(tel)

if __name__ == "__main__":
    main()
