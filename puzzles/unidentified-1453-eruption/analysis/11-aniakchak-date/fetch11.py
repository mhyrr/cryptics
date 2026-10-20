"""Download the open sources read for 11-aniakchak-date and print their sha256 (compare with README).

Usage: python3 -I fetch11.py <out_dir>

The extracted dates are already in brackets.csv and knowncase.csv; this script only lets a reader
check them against the papers. Some hosts failed TLS verification on the machine used here; the script
retries those without verification and says so.
"""
import hashlib, os, ssl, sys, urllib.request

SOURCES = [
    ('browne2022_pr126.pdf', 'https://dggs.alaska.gov/webpubs/dggs/pr/text/pr126.pdf'),
    ('neal2001_of00-519.pdf', 'https://pubs.usgs.gov/of/2000/0519/pdf/of00-519.pdf'),
    ('kaufman2012_jqs_ahklun.pdf', 'https://sites.ualberta.ca/~areyes/BertoPage/Publications_files/JQS_Ahklun.pdf'),
    ('dugmore1995.pdf', 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/'
                        '34B88E5246C25EA9837A5534E7A4A22D/S003382220003085Xa.pdf/'
                        'radiocarbon-dating-tephra-layers-in-britain-and-iceland.pdf'),
    ('cadb_master.txt', 'https://www.cadb.pitt.edu/bartoncarbon/master.txt'),
    ('cadb_carbon.txt', 'https://www.cadb.pitt.edu/bartoncarbon/carbon.txt'),
]
# Bacon et al. 2014 (PP 1810) is read from ../06-candidate-ranking/data/lit/pp1810.pdf (fetched by 06).

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for name, url in SOURCES:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        b = urllib.request.urlopen(req, timeout=180).read()
    except Exception as e:  # noqa: BLE001
        print(f'  {name}: verified fetch failed ({e.__class__.__name__}); retrying without TLS verification')
        b = urllib.request.urlopen(req, timeout=180, context=ssl._create_unverified_context()).read()
    open(os.path.join(out, name), 'wb').write(b)
    print(f'{hashlib.sha256(b).hexdigest()}  {name}  ({len(b)} bytes)')
