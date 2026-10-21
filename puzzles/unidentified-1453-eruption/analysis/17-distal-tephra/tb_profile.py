"""Print each saved Tephrabase site profile as a depth-ordered layer list.
Run: python3 -I tb_profile.py data/tb_site*.html > results/tb_profiles.txt"""
import html, re, sys

for path in sys.argv[1:]:
    t = html.unescape(open(path, encoding='latin-1').read())
    site = re.search(r'tephra layers? at ([^<|]+)', t)
    print(f'## {path.split("/")[-1]}: {site.group(1).strip() if site else "?"}')
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', t, flags=re.S):
        cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip()
                 for c in re.findall(r'<td[^>]*>(.*?)</td>', r, flags=re.S)]
        depth = [c for c in cells if re.fullmatch(r'\d+\.\d+ - \d+\.\d+', c)]
        if depth:
            name = [c for c in cells if 'Tephra' in c or re.search(r'[A-Z]{2,}-?\d', c)]
            refs = [c for c in cells if re.fullmatch(r'\d{2,4}', c)]
            print(f'   {depth[0]:>14}  {" | ".join(name)[:90]}  ref {refs[-1] if refs else "?"}')
    for ref in re.findall(r'(\d{2,4}): ([^<]{0,160})', t):
        if any(w in ref[1] for w in ('(19', '(20', ' 19', ' 20')):
            print(f'   [{ref[0]}] {ref[1].strip()}')
