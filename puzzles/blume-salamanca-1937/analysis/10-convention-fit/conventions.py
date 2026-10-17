"""Plaintext generators for the writing conventions tested in 10-convention-fit.

generate() is a copy of 01-solver/plaintext.telegram (telegraph style) with hooks for each convention. With its
default arguments it consumes the random stream exactly as plaintext.telegram(n, rnd, lang, "telegraph") does and
returns the same text; fit.py checks this before it runs. The word stream is plaintext.heldout_words, so the
caller must chdir into 01-solver first (as 08's fit.py does). 01-solver is not edited.
"""
import os, sys
SOLVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "01-solver")
sys.path.insert(0, SOLVER)
from plaintext import DROP, STOP, QTY, UNIT, heldout_words

AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Every upper-case word in the first column of the crib table, sources/context-cribs.md section 3 (fit.py checks).
CRIBS = ("LANA LANAS BURGOS HISMA SEVILLA SANSEBASTIAN SALAMANCA OFICINA REABRIR ABRIR COMPENSACION CREDITOS "
         "SALDOS DIVISAS FRANCOS SUIZOS PESETAS EXPORTACION SUIZA ZURICH PATVAG HOVAG VICTOR VIKTOR OSWALD STOP "
         "MONEDA EXTRANJERA JUNTA TECNICA KILOS").split()
CRIBS_NO_XF = [w for w in CRIBS if "X" not in w and "F" not in w]
TABLE_AJ = "ABCDEFGHIJ"      # digit d -> TABLE[(d - 1) % 10]: 1 -> A ... 9 -> I, 0 -> J
TABLE_QWERTY = "QWERTYUIOP"  # 1 -> Q ... 9 -> O, 0 -> P (typewriter top row)


def generate(n, rnd, lang="es", stop=None, stop_frac=1.0, qty_rate=0.03, number_table=None,
             crib_rate=0.0, cribs=CRIBS, null_rate=0.0, null_letters="X"):
    """stop: None = the language's own word (PUNTO/STOP/PONTO); "" = no stop word; else that string.
    stop_frac < 1: a stop is written at only that fraction of sentence ends (sweep only).
    number_table: if set, the inserted quantity is a 2-6 digit number written by this table, not spelled.
    crib_rate: probability per kept word that a word drawn uniformly from cribs is inserted before it.
    null_rate: probability per letter that a null from null_letters is inserted before it (after the
    plaintext is built, before any transposition)."""
    w = heldout_words(lang)
    sw = STOP[lang] if stop is None else stop
    i = rnd.randrange(len(w) - 5000)
    out, length = [], 0
    while length < n:
        t = w[i]; i += 1
        if t == ".":
            if sw and out and out[-1] != sw and (stop_frac >= 1.0 or rnd.random() < stop_frac):
                out.append(sw); length += len(sw)
            continue
        if t in DROP[lang] and rnd.random() < 0.7:
            continue
        if rnd.random() < qty_rate:
            if number_table:
                k = rnd.randint(2, 6)
                digits = [rnd.randint(1, 9)] + [rnd.randint(0, 9) for _ in range(k - 1)]
                q = "".join(number_table[(d - 1) % 10] for d in digits)
            else:
                q = rnd.choice(QTY[lang]) + rnd.choice(UNIT[lang])
            out.append(q); length += len(q)
        if crib_rate and rnd.random() < crib_rate:
            c = rnd.choice(cribs)
            out.append(c); length += len(c)
        out.append(t); length += len(t)
    s = "".join(out)[:n]
    if null_rate:
        res = []
        for ch in s:
            if len(res) >= n:
                break
            if rnd.random() < null_rate:
                res.append(rnd.choice(null_letters))
            res.append(ch)
        s = "".join(res)[:n]
    return s


def g(**kw):
    return lambda n, rnd, lang: generate(n, rnd, lang, **kw)

# Pre-set parameters (README, Method). Values are (generator, telegrams it is scored on).
GENERATORS = {
    "g0":  (g(), "T1 T2"),
    "g1":  (g(stop="STOP"), "T1 T2"),
    "g2":  (g(stop="X"), "T1 T2"),
    "g3":  (g(stop=""), "T1 T2"),
    "g4a": (g(qty_rate=0.06), "T1 T2"),
    "g4b": (g(qty_rate=0.09), "T1 T2"),
    "g5a": (g(number_table=TABLE_AJ), "T1 T2"),
    "g5b": (g(number_table=TABLE_QWERTY), "T1 T2"),
    "g6a": (g(null_rate=5 / 615, null_letters="X"), "T1 T2"),
    "g6b": (g(null_rate=0.03, null_letters=AZ), "T1 T2"),
    "g7a": (g(crib_rate=0.15), "T1 T2"),
    "g7b": (g(crib_rate=0.15, cribs=CRIBS_NO_XF), "T1 T2"),
    "g8":  (g(stop="F"), "T2"),
    "g9a": (g(stop="STOP", crib_rate=0.15), "T1 T2"),
    "g9b": (g(stop="X", crib_rate=0.15), "T1 T2"),
    "g9c": (g(stop="X", qty_rate=0.06), "T1 T2"),
    "g9d": (g(stop="X", qty_rate=0.09), "T1 T2"),
}

# Rate sweep (README, Method): a pass here is "possible at a tuned rate" only.
SWEEP = (
    [(f"g2 q={q}", g(stop="X", stop_frac=q), "T1 T2") for q in (0.25, 0.5, 0.75)]
    + [(f"g6a {k}/615", g(null_rate=k / 615, null_letters="X"), "T1 T2") for k in (1, 2, 3, 8, 12)]
    + [(f"g6b {r}", g(null_rate=r, null_letters=AZ), "T1 T2") for r in (0.01, 0.05, 0.10)]
    + [(f"g7a {r}", g(crib_rate=r), "T1 T2") for r in (0.05, 0.10, 0.20, 0.30)]
    + [(f"g4 {r}", g(qty_rate=r), "T1 T2") for r in (0.12, 0.15)]
    + [(f"g8 q={q}", g(stop="F", stop_frac=q), "T2") for q in (0.25, 0.5, 0.75)]
)
