"""Reference columnar transposition (pure Python). Shares no code with the C solver.

A key is a list of ranks: key[c] = reading rank of column c (0-based), as derived
from a keyword (ties left to right). Columns are read in increasing rank.
Incomplete rectangles: the first len(text) % w columns are one letter longer.

Stage conventions:
  'C'  write rows, read columns  (the forward stage, German Doppelwürfel)
  'R'  write columns, read rows  (the inverse operation of 'C')
A double transposition is two stages; conv 'CC' is the forward double columnar.
"""

def key_from_word(word):
    order = sorted(range(len(word)), key=lambda i: (word[i], i))
    ranks = [0] * len(word)
    for r, i in enumerate(order):
        ranks[i] = r
    return ranks

def col_enc(text, key):
    w, n = len(key), len(text)
    cols = [text[c::w] for c in range(w)]
    return "".join(cols[c] for c in sorted(range(w), key=lambda c: key[c]))

def col_dec(text, key):
    w, n = len(key), len(text)
    rows, extra = divmod(n, w)
    lens = [rows + (1 if c < extra else 0) for c in range(w)]
    cols, pos = [None] * w, 0
    for c in sorted(range(w), key=lambda c: key[c]):
        cols[c] = text[pos:pos + lens[c]]
        pos += lens[c]
    return "".join(cols[i % w][i // w] for i in range(n))

STAGE_ENC = {"C": col_enc, "R": col_dec}
STAGE_DEC = {"C": col_dec, "R": col_enc}

def double_enc(pt, k1, k2, conv="CC"):
    return STAGE_ENC[conv[1]](STAGE_ENC[conv[0]](pt, k1), k2)

def double_dec(ct, k1, k2, conv="CC"):
    return STAGE_DEC[conv[0]](STAGE_DEC[conv[1]](ct, k2), k1)

def _tests():
    # Hand-worked: WEAREDISCOVEREDFLEEATONCE, key ZEBRAS (ranks 5,2,1,3,0,4).
    # Rows: WEARED/ISCOVE/REDFLE/EATONC/E. Columns: WIREE ESEA ACDT ROFO EVLN DEEC.
    # Read A,B,E,R,S,Z -> EVLN ACDT ESEA ROFO DEEC WIREE (the textbook answer, unpadded).
    k = key_from_word("ZEBRAS")
    assert k == [5, 2, 1, 3, 0, 4], k
    assert col_enc("WEAREDISCOVEREDFLEEATONCE", k) == "EVLNACDTESEAROFODEECWIREE"
    assert col_dec("EVLNACDTESEAROFODEECWIREE", k) == "WEAREDISCOVEREDFLEEATONCE"
    # Hand-worked tie handling: REFERENCE -> ranks of E E E E first (Lasry: 8,2,6,3,9,4,7,1,5 one-based)
    assert [r + 1 for r in key_from_word("REFERENCE")] == [8, 2, 6, 3, 9, 4, 7, 1, 5]
    # Double, hand-worked second stage: intermediate EVLNACDTESEAROFODEECWIREE with key CAB (ranks 2,0,1):
    # rows EVL/NAC/DTE/SEA/ROF/ODE/ECW/IRE/E ; col0 ENDSROEIE col1 VATEODCR col2 LCEAFEWE
    # read rank0=col1, rank1=col2, rank2=col0
    k2 = key_from_word("CAB")
    assert double_enc("WEAREDISCOVEREDFLEEATONCE", k, k2) == "VATEODCRLCEAFEWEENDSROEIE"
    import random
    rnd = random.Random(1)
    for _ in range(2000):
        n = rnd.randint(20, 700)
        t = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(n))
        a, b = rnd.randint(2, 30), rnd.randint(2, 30)
        k1 = rnd.sample(range(a), a); k2 = rnd.sample(range(b), b)
        for conv in ("CC", "CR", "RC", "RR"):
            assert double_dec(double_enc(t, k1, k2, conv), k1, k2, conv) == t
    print("transpo.py: all tests pass")

if __name__ == "__main__":
    _tests()
