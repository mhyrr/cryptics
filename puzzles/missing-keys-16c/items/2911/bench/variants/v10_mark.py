"""v10: v9_rounds, with rows marked by evidence, not by share.

align.key_from_path marks a row when 60% of the sign's places agree. On a loose abridgement a right value
agrees at about half its places (vx_beam_oracle: 55%), so right rows with 15 of 28 places stay unmarked.
Here a row is judged against chance. pc = 3 x the share of plain positions where the value's letters stand
(3: the path may choose among neighbouring places), capped at 0.5.
  evidence = hits * log(HIT / pc) + misses * log((1 - HIT) / (1 - pc)),  HIT = 0.55
  certain   evidence >= 10 and 5 hits;   probable  evidence >= 4 and 3 hits
A row key_from_path left unknown because its places are ragged (they touch unaccounted letters) stays so.
"""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, v9_rounds  # noqa: E402

HIT = 0.55
CERT, PROB = float(os.environ.get("V10_CERT", 10)), float(os.environ.get("V10_PROB", 4))


def remark(rows, P, log=None):
    n = {}
    for ln in (1, 2, 3):
        for j in range(len(P) - ln + 1):
            s = P[j:j + ln]
            n[s] = n.get(s, 0) + 1
    st = {}
    for r in rows:
        v, h, x = r["value"], r["support"], r["conflict"]
        if not v or len(v) > 3:
            continue
        ragged = r["status"] == "unknown" and h >= 5 and r["share"] >= 0.8
        pc = min(0.5, 3.0 * n.get(v, 0) / len(P))
        ev = h * math.log(HIT / pc) + x * math.log((1 - HIT) / (1 - pc))
        r["status"] = ("unknown" if ragged else "certain" if ev >= CERT and h >= 5
                       else "probable" if ev >= PROB and h >= 3 else "unknown")
        st[r["status"]] = st.get(r["status"], 0) + 1
    if log:
        log(f"rows by evidence: {st}")
    return rows


def build(cipher, plain, log):
    rows = v9_rounds.build(cipher, plain, log)
    P = align.load_pair(cipher, plain)[1]
    return remark(rows, P, log)
