"""Count the years that have entries in Sigurður Þór Guðjónsson's transcription of Icelandic annal weather
entries (vedur.is, annalar_sig-th.pdf, converted with `pdftotext` without -layout).

Usage: python3 -I annals_gap.py <vedur_annalar.txt> > results/annals_gap.txt
An entry is a line that starts with a 4-digit year followed by an annal name. This measures the weather
compilation only; it is a proxy for annal density, not a list of eruptions.
"""
import re, sys, collections

pat = re.compile(r'^(1[0-9]{3})\s+(?:[IVX]+\.\s*)?([A-ZÁÉÍÓÚÝÞÆÖ][^\s:]*(?:\s[^\s:]+)?):')
src = collections.defaultdict(set)
for line in open(sys.argv[1], encoding='utf-8'):
    m = pat.match(line.lstrip("\f"))
    if m:
        src[int(m.group(1))].add(m.group(2).strip())
print('Years with annal weather entries, 1380-1560, and the source annals:')
prev = None
for y in sorted(k for k in src if 1380 <= k <= 1560):
    gap = f'   <- gap of {y - prev - 1} yr' if prev and y - prev > 5 else ''
    print(f'  {y}: {", ".join(sorted(src[y]))}{gap}')
    prev = y
for a, b in ((1400, 1430), (1431, 1472), (1473, 1520)):
    n = sum(1 for k in src if a <= k <= b)
    print(f'{a}-{b}: {n} years with entries of {b - a + 1}')
print('1452 or 1453 present:', any(k in src for k in (1452, 1453)))
