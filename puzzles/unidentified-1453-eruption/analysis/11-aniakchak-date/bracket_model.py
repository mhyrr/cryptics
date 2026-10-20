"""Shared code for 11-aniakchak-date: a one-event bracket model on an IntCal20 grid.

The IntCal20 reader and the calibration helpers (IntCal, make_grid, pdf_14c, hpd, normalise)
are imported from ../06-candidate-ranking/pipeline.py (written for experiment 06, recal14c.py).
Nothing here reads the network. The rules are the pre-registration in README.md.

Model. One event T with a flat prior over [LO, HI). Each date i has a calendar age t_i with a flat
prior over the wide calibration grid and an IntCal20 likelihood. Constraints:
  below: t_i <= T   -> factor F_i(T)      (cumulative of the calibrated pdf)
  above: t_i >= T   -> factor 1 - F_i(T)
  same : t_i == T   -> factor L_i(T)      (calibrated pdf)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '06-candidate-ranking'))
import pipeline as P  # noqa: E402  (06's IntCal20 code, credited above)

LO, HI = 1300.0, 1800.0          # pre-registered model range (CE)
CAL_LO, CAL_HI = 800.0, 1950.0   # calibration grid for each date's own pdf
STEP = P.GRID_STEP               # 0.1 yr


class Model:
    def __init__(self, intcal_path, lo=LO, hi=HI):
        self.ic = P.IntCal(intcal_path)
        self.cal = P.make_grid(CAL_LO, CAL_HI)
        self.grid = P.make_grid(lo, hi)
        i0 = int(round((lo - CAL_LO) / STEP))
        self.slice = (i0, i0 + len(self.grid))

    def calpdf(self, age, err):
        return P.pdf_14c(self.ic, self.cal, [(age, err)])

    def factor(self, age, err, position):
        p = self.calpdf(age, err)
        a, b = self.slice
        if position == 'same':
            return p[a:b]
        cum, acc = [], 0.0
        for x in p:
            acc += x
            cum.append(acc)
        F = cum[a:b]
        if position == 'below':
            return F
        if position == 'above':
            return [1.0 - f for f in F]
        if position.startswith('gap'):
            # post hoc (README, "Post hoc: gap model"): t_i = T - g, g ~ U(0, G). Factor (F(T) - F(T - G)) / G.
            G = float(position[3:])
            k = int(round(G / STEP))
            return [(cum[a + j] - (cum[a + j - k] if a + j - k >= 0 else 0.0)) / G for j in range(b - a)]
        raise ValueError(position)

    def posterior(self, dates):
        """dates: list of (age, err, position). Returns normalised p(T) on self.grid."""
        p = [1.0] * len(self.grid)
        for age, err, pos in dates:
            p = [x * y for x, y in zip(p, self.factor(age, err, pos))]
        return P.normalise(p)

    def prob(self, p, a, b):
        return sum(x for t, x in zip(self.grid, p) if a <= t < b)

    def hpd(self, p):
        return P.hpd(self.grid, p)

    def mean(self, p):
        return sum(t * x for t, x in zip(self.grid, p))

    def quantile(self, p, q):
        acc = 0.0
        for t, x in zip(self.grid, p):
            acc += x
            if acc >= q:
                return t
        return self.grid[-1]

    def loo(self, dates):
        """P(constraint i holds | all other dates), for each date."""
        out = []
        for i, (age, err, pos) in enumerate(dates):
            rest = dates[:i] + dates[i + 1:]
            p = self.posterior(rest)
            f = self.factor(age, err, pos)
            if pos == 'same':   # agreement-like: overlap of the date's pdf with the rest, relative to flat
                f = [x * len(f) for x in P.normalise(f)]
                val = sum(a * b for a, b in zip(p, f))
            else:
                val = sum(a * b for a, b in zip(p, f))
            out.append(val)
        return out


def fmt_hpd(h):
    return ', '.join(f'{a:.0f}-{b:.0f}' for a, b in h)


def summary(m, p, label, win=(1451.0, 1454.0)):
    h = m.hpd(p)
    W = sum(b - a for a, b in h)
    P_ = m.prob(p, *win)
    B = (win[1] - win[0]) / W
    inside = any(a < 1454.0 and b > 1452.0 for a, b in h)
    return dict(label=label, hpd=h, W=W, P=P_, B=B, inside=inside,
                median=m.quantile(p, 0.5), q025=m.quantile(p, 0.025), q975=m.quantile(p, 0.975))


def verdict(s):
    """Pre-registered decision rule (README)."""
    if not s['inside']:
        return 'refuted'
    if s['P'] < 0.5 * s['B']:
        return 'weakened'
    if s['W'] <= 30 and any(a <= 1453.0 <= b for a, b in s['hpd']):
        return 'supported'
    return 'not excluded'


def print_summary(s):
    print(f"  {s['label']}")
    print(f"    95.4% HPD {fmt_hpd(s['hpd'])} CE  (width {s['W']:.0f} yr); median {s['median']:.0f}; "
          f"central 95% {s['q025']:.0f}-{s['q975']:.0f}")
    print(f"    P(1451.0-1454.0) = {s['P']:.4f}; flat-over-HPD baseline B = {s['B']:.4f}; ratio P/B = {s['P'] / s['B']:.2f}")
    print(f"    rule -> {verdict(s)}")
