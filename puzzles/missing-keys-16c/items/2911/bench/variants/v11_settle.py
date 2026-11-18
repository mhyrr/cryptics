"""v11: v10_mark, with rounds run until the path settles (it moves less than 0.2 letters a unit), 12 at most.
v10 stops after 4 rounds. On p1 the path had stopped by then; on the full pair it was still moving."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v9_rounds, v10_mark  # noqa: E402


def build(cipher, plain, log):
    old = (v9_rounds.ROUNDS, v9_rounds.SETTLE)
    v9_rounds.ROUNDS, v9_rounds.SETTLE = 12, 0.2
    try:
        return v10_mark.build(cipher, plain, log)
    finally:
        v9_rounds.ROUNDS, v9_rounds.SETTLE = old
