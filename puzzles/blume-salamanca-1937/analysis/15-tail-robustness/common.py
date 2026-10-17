"""Shared pieces for 15-tail-robustness: plants with t untransposed letters at one end, the two fills,
and body recovery.

Imports 01-solver the way 08-letter-fit/fit.py does: its folder goes on sys.path and becomes the working
directory, because plaintext.py opens relative paths. No solver here ever sees a real telegram. The only
telegram letters read are T1's last 20, as a letter distribution for one of the two fills.
"""
import array, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext, transpo  # noqa: E402
from control import shift_acc  # noqa: E402  (cyclic shift up to 40, as the 01 controls)

AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Q = array.array("f"); Q.fromfile(open("out/lm_es_4.bin", "rb"), 26 ** 4)


def _t1_tail20():
    t = "".join(c for c in open(os.path.join(HERE, "../../sources/telegram-1.txt")).read().upper() if c.isalpha())
    assert len(t) == 615
    return t[-20:]


TAIL20 = _t1_tail20()          # used only as a bag of letters for the "t1tail" fill
PASS = 0.90                    # body letters in place, after the cyclic-shift tolerance


def fill(t, rnd, kind):
    """t letters: 'uniform' over A-Z, or 't1tail' drawn i.i.d. from the letters of T1's last 20."""
    if kind == "uniform":
        return "".join(rnd.choice(AZ) for _ in range(t))
    return "".join(rnd.choice(TAIL20) for _ in range(t))


def assemble(body_ct, extra, end):
    return body_ct + extra if end == "end" else extra + body_ct


def body_acc(dec, body_pt, t, end):
    """Fraction of body letters in place: the body's window of the full decryption against the body
    plaintext, with control.py's shift_acc (cyclic, |s| <= 40). At t = 0 this is control.py's measure."""
    o = 0 if end == "end" else t
    return shift_acc(dec[o:o + len(body_pt)], body_pt)


def qscore(v):
    """Spanish quadgram score per quadgram, for a list of letter values 0-25."""
    return sum(Q[((a * 26 + b) * 26 + c) * 26 + d] for a, b, c, d in zip(v, v[1:], v[2:], v[3:])) / (len(v) - 3)


def conditions(ts_end=(5, 10, 15, 20), ts_start=(5, 10, 15)):
    """(t, end) cells; t = 0 is the baseline."""
    return [(0, "none")] + [(t, "end") for t in ts_end] + [(t, "start") for t in ts_start]
