"""List the Lake Kushu (RK12) layers with glass analyses in Chen et al. 2019's
Mendeley supplement, shallowest first, with shard counts and mean SiO2/K2O.
Run: python3 -I kushu17.py data/kushu_supp.xlsx > results/kushu_layers.txt"""
import re, sys, zipfile
import xml.etree.ElementTree as ET

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
z = zipfile.ZipFile(sys.argv[1])
ss = [''.join(t.text or '' for t in si.iter(NS + 't'))
      for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter(NS + 'si')]
rows = []
for row in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).iter(NS + 'row'):
    vals = []
    for c in row.iter(NS + 'c'):
        v = c.find(NS + 'v')
        vals.append('' if v is None else ss[int(v.text)] if c.get('t') == 's' else v.text)
    rows.append(vals)
hdr = next(r for r in rows if r and r[0] == 'Sample')
iS, iK = hdr.index('SiO2'), hdr.index('K2O')
layers = {}
for r in rows:
    if r and re.fullmatch(r'RK12-\d{4}', r[0].strip()):
        try:
            layers.setdefault(r[0].strip(), []).append((float(r[iS]), float(r[iK])))
        except (ValueError, IndexError):
            pass
print('# Chen et al. 2019 supplement, sheet "Kushu glass by layer" (unnormalised SiO2, K2O means)')
print('# RK12-0151 is B-Tm (946 CE) per the "Kushu glass by correlation" sheet; no shallower layer has glass in the supplement')
for k in sorted(layers):
    a = layers[k]
    print(f'{k}  depth {int(k[5:])} cm(?)  n={len(a):3d}  SiO2 {sum(x for x, _ in a)/len(a):.2f}  K2O {sum(y for _, y in a)/len(a):.2f}')
