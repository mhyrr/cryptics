"""Calibrate the radiocarbon ages that bracket the 17 hits, and say whether a
tephra in that position could be 1453.

Run (from this folder):
    python3 -I calib17.py ../06-candidate-ranking/data/intcal20.14c > results/calib17.txt

Uses 06's IntCal20 code unchanged (../06-candidate-ranking/pipeline.py).
Each age is calibrated alone, flat calendar prior 1000-1950 CE.

Position rule:
  'below'  the dated material lies under the tephra, so the tephra is younger
           than the material. A 1453 tephra needs material age <= 1453:
           P(material <= 1453) is reported.
  'level'  the dated material is at the tephra's depth (bulk peat, mixed
           ages). P(within +-25 yr of 1453) and the 95% HPD are reported.
  'model'  an age-depth model published by the authors; only re-stated in CE.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '06-candidate-ranking'))
import pipeline as P  # noqa: E402

AGES = [
    # (hit id, lab code, 14C BP, 1 sigma, material, position, source)
    ('LPB', 'GU-3009', 540, 50, 'peat 0.15-0.16 m, under Loch Portain B (0.10-0.15 m)', 'below',
     'Tephrabase c14 tephra=12; Dugmore, Larsen & Newton 1995'),
    ('LPB', 'GU-3010', 360, 70, 'peat 0.13-0.14 m, inside the Loch Portain B / Hekla 1510 interval', 'level',
     'Tephrabase c14 tephra=12; Dugmore, Larsen & Newton 1995'),
    ('AHK04', 'UCIAMS-23856', 435, 15, 'wood & leaves under the 0.4-ka tephra, soil pit near Cascade Lake (Ahklun)', 'below',
     'Kaufman et al. 2012 Table 2'),
    ('KEN-MP', 'Gd-15806', 510, 100, 'bulk peat 40-50 cm, Moose Pass (Kenai); MP39 at 39 cm and microtephras extrapolated from it', 'level',
     'Payne & Blackford 2008 p. 3'),
]

MODELS = [
    # (hit id, what, cal BP centre, half-width of 95% range, source)
    ('AHK04', 'Lone Spruce Pond 0.4-ka tephra, clam model', 377, 62, 'Kaufman et al. 2012 Table 4'),
    ('AHK04', 'Cascade soil pit 0.4-ka tephra (maximum age)', 505, 20, 'Kaufman et al. 2012 Table 4'),
    ('AHK04', 'Mean age of the 0.4-ka tephra as published', 441, 64, 'Kaufman et al. 2012 Table 4'),
]

TARGET = 1453.0


def main(intcal_path):
    ic = P.IntCal(intcal_path)
    grid = P.make_grid(1000, 1950, 1.0)
    print('# 17-distal-tephra: IntCal20 calibration of bracketing ages (06 code, flat prior 1000-1950 CE)')
    print(f'# target year {TARGET:.0f} CE = {1950 - TARGET:.0f} cal BP\n')
    for hit, lab, age, err, mat, pos, src in AGES:
        p = P.pdf_14c(ic, grid, [(age, err)])
        ivs = P.hpd(grid, p, 0.954)
        hpd = ', '.join(f'{a:.0f}-{b:.0f}' for a, b in ivs)
        le = sum(x for t, x in zip(grid, p) if t <= TARGET)
        near = sum(x for t, x in zip(grid, p) if abs(t - TARGET) <= 25)
        print(f'{hit:7} {lab:13} {age}+-{err} BP  [{pos}]  95% HPD {hpd} CE')
        if pos == 'below':
            print(f'        P(material <= {TARGET:.0f}) = {le:.2f}   (a 1453 tephra above it needs this)')
        else:
            print(f'        P(within +-25 yr of {TARGET:.0f}) = {near:.2f}')
        print(f'        {mat}; {src}')
    print('\n# Published age-depth model ages, restated in CE (no recalculation)')
    for hit, what, bp, hw, src in MODELS:
        lo, hi = 1950 - (bp + hw), 1950 - (bp - hw)
        inside = 'includes' if lo <= TARGET <= hi else 'excludes'
        print(f'{hit:7} {what}: {bp} +- {hw} cal BP = {lo}-{hi} CE ({inside} 1453); {src}')


if __name__ == '__main__':
    main(sys.argv[1])
