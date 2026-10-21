"""Summarise saved Tephrabase distribution pages: tephra name, number of sites,
and the sites outside Iceland (name, country, lat, lon).
Run: python3 -I tb_sites.py data/tb_eu_tephra*.html > results/tb_distal_sites.txt"""
import html, re, sys

for path in sys.argv[1:]:
    t = html.unescape(open(path, encoding='latin-1').read())
    m = re.search(r'found (?:the )?(.+?) at (\d+) sites|found (\d+) sites with the (.+?) in', t)
    head = m.group(0) if m else 'no site count'
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', t, flags=re.S)
    distal = []
    for r in rows:
        cells = [re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', r, flags=re.S)]
        if len(cells) >= 5 and 'Iceland' not in ' '.join(cells) and re.search(r'\d+\.\d+°N', ' '.join(cells)):
            distal.append(' / '.join(c for c in cells[:5] if c))
    print(f'## {path.split("/")[-1]}: {head}; non-Iceland sites: {len(distal)}')
    for d in distal:
        print('   ', d)
