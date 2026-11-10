"""Loaders for the three single-shard glass datasets used in 18.

Standard library only. Every shard is returned as a dict with keys
  set, sample, label, lab, pop, ox (dict of the 8 oxides, as published)
and normalisation is done by the caller (glass18.py), so the loaders stay
transcription-only.

Sources (see README for URLs, access dates, tiers, sha256):
  Browne et al. 2022, DGGS PR 126, appendix G CSV        -> load_browne()
  Kaufman et al. 2012, JQS, Table S1 (pdftotext -layout) -> load_kaufman()
  Davies, Jensen & Kaufman 2022, GChron, SI Table S2     -> load_davies()
"""
import csv, os, re, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
OX8 = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MgO', 'CaO', 'Na2O', 'K2O']


# ------------------------------------------------------------------ Browne 2022
def load_browne(path=os.path.join(DATA, 'pr126-appendix_g_tephra_glass_data.csv')):
    out = []
    with open(path, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            ox = {'SiO2': r['SiO2'], 'TiO2': r['TiO2'], 'Al2O3': r['Al2O3'], 'FeO': r['FeOT'],
                  'MgO': r['MgO'], 'CaO': r['CaO'], 'Na2O': r['Na2O'], 'K2O': r['K2O']}
            ox = {k: float(v) for k, v in ox.items()}
            out.append(dict(set='browne2022', sample=r['sample_id'].strip(),
                            label=r['eruptive_phase'].strip().strip('"'),
                            lab='UAF/UCLA' if r['geologist'] != 'J. Rhiele' else 'USGS (Riehle 2000)',
                            pop=None, ox=ox, total=float(r['total']) if r['total'] else None,
                            desc=r['description'].strip()))
    return out


# ------------------------------------------------------------------ Kaufman 2012 S1
ROW = re.compile(r'^(UA\s?\d{4}[-\w]*|UA\d{4}[-\w]*)\s+((?:-?\d+\.\d+\s+){11}-?\d+\.\d+)(.*)$')
STAT = re.compile(r'^(Mean|StDev|GrandMean)\b')
ORDER_K = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'Na2O', 'K2O', 'Cl', 'Total', 'H2Odiff']


def load_kaufman(path=os.path.join(DATA, 'kaufman2012_tableS1.txt')):
    """Return shards with pop = running population index (a population ends at a
    'Mean' row, as laid out by the authors) and note = the free-text annotation
    carried by the first rows of each sample block (e.g. '"0.4 ka Aniakchak"')."""
    out, pop, note, lines = [], 0, '', open(path, encoding='utf-8').read().splitlines()
    pending = []
    for ln, line in enumerate(lines, 1):
        s = line.strip()
        if not s:
            continue
        if STAT.match(s):
            if (s.startswith('Mean') or s.startswith('GrandMean')) and pending:
                pop += 1
                pending = []
            continue
        m = ROW.match(s)
        if not m:
            # unlabelled numeric rows (Sunday Lake Tephra B block) carry no sample id
            continue
        sid = m.group(1).replace(' ', '')
        nums = [float(x) for x in m.group(2).split()]
        tail = m.group(3).strip()
        if tail and not re.match(r'^\d+(\.\d+)?$', tail):
            if tail.startswith('"') or tail in ('Tephra B', 'Tephra C', 'Tephra D', 'Tephra E', 'Tephra F', 'Tephra B?') \
                    or tail.startswith('Tephra') or tail.startswith('Aniakchak') or tail.startswith('mid-SiO2') \
                    or tail.startswith('5.8') or tail.startswith('outlier'):
                note = tail
        d = dict(zip(ORDER_K, nums))
        unum = re.match(r'UA(\d{4})', sid).group(1)
        shard = dict(set='kaufman2012', sample='UA' + unum, shard=sid, line=ln, label=note,
                     lab='U Alberta (JEOL 8900)', pop=pop + 1, ox={k: d[k] for k in OX8},
                     total=None, desc=tail)
        out.append(shard)
        pending.append(shard)
    return out


# ------------------------------------------------------------------ Davies 2022 S2
def _xlsx_rows(path, sheet_name):
    z = zipfile.ZipFile(path)
    wb = z.read('xl/workbook.xml').decode()
    rels = z.read('xl/_rels/workbook.xml.rels').decode()
    rid = re.search(r'<sheet [^>]*name="%s"[^>]*r:id="([^"]+)"' % re.escape(sheet_name), wb).group(1)
    tgt = re.search(r'<Relationship [^>]*Id="%s"[^>]*Target="([^"]+)"' % rid, rels) or \
        re.search(r'<Relationship [^>]*Target="([^"]+)"[^>]*Id="%s"' % rid, rels)
    t = tgt.group(1).lstrip('/')
    t = t if t.startswith('xl/') else 'xl/' + t
    ss = [re.sub(r'<[^>]+>', '', s) for s in
          re.findall(r'<si>(.*?)</si>', z.read('xl/sharedStrings.xml').decode(), re.S)]
    rows = []
    for r in re.findall(r'<row[^>]*>(.*?)</row>', z.read(t).decode(), re.S):
        row = {}
        for c in re.finditer(r'<c r="([A-Z]+)\d+"([^>]*?)(?:/>|>(.*?)</c>)', r, re.S):
            col, attrs, body = c.groups()
            v = re.search(r'<v>(.*?)</v>', body or '', re.S)
            if 't="s"' in attrs and v:
                val = ss[int(v.group(1))]
            elif 't="inlineStr"' in attrs:
                val = re.sub(r'<[^>]+>', '', body)
            else:
                val = v.group(1) if v else ''
            n = 0
            for ch in col:
                n = n * 26 + ord(ch) - 64
            row[n - 1] = val
        rows.append([row.get(i, '') for i in range(max(row) + 1)] if row else [])
    return rows


def load_davies(path=os.path.join(DATA, 'davies2022_SI_tables.xlsx')):
    """Reference blocks only (rows from a 'REF' marker to the next sample block).
    Columns 0-16 are the accepted analyses (normalised by the authors);
    a population ends at a 'Mean' row; shards after the last Mean of a block
    (author outliers) are kept with pop=None."""
    rows = _xlsx_rows(path, 'Table S2')
    out, cur, pop, popn = [], None, 0, None
    for i, r in enumerate(rows):
        r = (r + [''] * 17)[:17]
        c0 = r[0].strip()
        if c0 == 'REF':
            cur = {'name': None, 'rows': []}
            pop += 1
            popn = pop
        elif c0 and cur is not None and cur['name'] is None:
            cur['name'] = c0
        elif c0 and cur is not None:
            cur = None  # a new Cascade Lake sample block starts
        if cur is None:
            continue
        uid = r[3].strip()
        if uid in ('Mean',):
            pop += 1
            popn = pop
            continue
        if uid.startswith('St. Dev') or uid.startswith('StDev') or not uid:
            continue
        try:
            nums = [float(x) for x in r[4:14]]
        except ValueError:
            continue
        d = dict(zip(['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'Na2O', 'K2O', 'Cl'], nums))
        out.append(dict(set='davies2022', sample=re.match(r'(UA\s?\d+)', uid).group(1).replace(' ', '') if uid.startswith('UA') else uid.split('-')[0],
                        shard=uid, block=cur, lab='U Alberta (JEOL 8900)',
                        pop=popn, ox={k: d[k] for k in OX8}, total=None, desc=r[1]))
    for s in out:
        s['label'] = s.pop('block')['name']
    return out


if __name__ == '__main__':
    import collections
    for name, rows in (('browne', load_browne()), ('kaufman', load_kaufman()), ('davies', load_davies())):
        print('#', name, len(rows), 'shards')
        g = collections.OrderedDict()
        for s in rows:
            key = (s['label'], s['sample'], s['pop'])
            g.setdefault(key, []).append(s['ox']['SiO2'])
        for (lab, smp, pop), v in g.items():
            print(f'  pop {str(pop):>4}  {smp:22} n={len(v):3}  SiO2 {min(v):6.2f}-{max(v):6.2f}  {lab[:50]}')
