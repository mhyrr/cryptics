"""v0: line/align.py as it stood at the pilot (complete-pair model), with the log-space E-step. The baseline."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
import align_log, align  # noqa: E402


def build(cipher, plain, log):
    units, P, wb, lac, pairs = align.load_pair(cipher, plain)
    segs = [(a, c, align_log.LogSegment(s.units, s.P, s.wb, s.lac)) for a, c, s in align.make_segments(units, P, wb, lac, pairs)]
    table = align.train(segs, log=log)
    path, skipped = align.best_path(segs, table)
    return align.key_from_path(path, skipped)
