"""Download the inputs for 03-latitude-posterior and print sha256 for each.

Usage: python3 -I fetch.py <out_dir>      (e.g. data)
Files are untrusted data. Nothing here executes them.
"""
import hashlib, os, sys, urllib.request

OUT = sys.argv[1]
CEMAC = 'https://raw.githubusercontent.com/cemac/volcanic-forcing-deposition/6201f4e13401dfdeee4dee33c391056d718b3acf/'
EPMC = 'https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML'
FILES = [('evolv2k_v4.tab', 'https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile')]
FILES += [(f'cemac/{p.replace("/", "_")}', CEMAC + p) for p in
          ['README.md', 'js/site.js'] + [f'data/{n}.json' for n in
          ['axes', 'greenland_jan', 'greenland_jul', 'antarctica_jan', 'antarctica_jul', 'forcing_jan', 'forcing_jul', 'null']]]
FILES += [('papers/marshall2021.pdf', 'https://shura.shu.ac.uk/28799/1/2020JD033578.pdf'),
          ('papers/marshall2019.pdf', 'https://shura.shu.ac.uk/26683/1/Marshall2019.pdf'),
          ('papers/burke2019.pdf', 'https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/20111/Burke_2019_EPSL_S_ice_accepted.pdf?sequence=1&isAllowed=y'),
          ('papers/burke2023.xml', EPMC.format('PMC10666123')),
          ('papers/hutchison2025.xml', EPMC.format('PMC11725861')),
          ('papers/pearson2022.xml', EPMC.format('PMC9802406'))]
for name, url in FILES:
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
    open(path, 'wb').write(data)
    print(hashlib.sha256(data).hexdigest(), len(data), name)
