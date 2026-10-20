"""Size check for 13-kamchatka-date: P(VSSI >= thr | VEI, class) from 06's size model.

Usage: python3 -I size13.py <gvp_eruptions.csv> <gvp_volcanoes.csv> <evolv2k_v4.tab>
Reuses ../06-candidate-ranking/pipeline.py (SizeModel), unchanged.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '06-candidate-ranking'))
import pipeline as P  # noqa: E402

rows = P.load_gvp(sys.argv[1], sys.argv[2])
att = P.attribute(P.load_evolv2k(sys.argv[3]), rows)
sm = P.SizeModel(rows, att)
thr = 9.97 - 3.07
lo, hi = P.SIZE_PERIOD
print(f'UE 1453 threshold VSSI >= {thr:.2f} Tg S; counting period {lo}-{hi - 1}')
for v in [2, 3, 4, 5, 6]:
    num = [a for a in att if a['vei'] is not None and a['vei'] == v and a['sclass'] == 'other' and lo <= a['year'] < hi and a['vssi'] >= thr]
    print(f'  VEI {v} other: P = {sm.p(v, "other", thr):.4f}   n(GVP) = {sm.den.get((v, "other"), 0)}   numerator: ' +
          (', '.join(f"{a['loc'][:22]} {a['year']} ({a['vssi']:.1f})" for a in num) or 'none'))
p3, p4, p5 = (sm.p(v, 'other', thr) for v in (3, 4, 5))
print(f'  likelihood ratios: VEI3/VEI5 = {p3 / p5:.3f}; VEI4/VEI5 = {p4 / p5:.3f}')
print('\neVolv2k v4 events in Kamchatka/Kurils/Hokkaido (any VSSI):')
for a in att:
    if any(s in a['loc'] for s in ('Kuril', 'Shiveluch', 'Kamchat', 'Tarumae', 'Shikotsu', 'Komagatake', 'Toya')):
        print(f"  {a['year']:>5} {a['loc'][:40]:40} VSSI {a['vssi']:.2f}  GVP row: {'yes' if a['gvp'] else 'none'}")
