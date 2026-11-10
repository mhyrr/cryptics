"""Re-download the open datasets for 18 into data/ and record sha256.

Run (from this folder):  python3 -I fetch18.py
Kaufman 2012 Table S1 is not fetched here: Wiley answers 403 to scripts.
Open https://onlinelibrary.wiley.com/doi/full/10.1002/jqs.1552 in a browser,
download JQS_1552_sm_SupplTabS1.pdf, save it as data/kaufman2012_supp_TabS1.pdf
and run  pdftotext -layout data/kaufman2012_supp_TabS1.pdf data/kaufman2012_tableS1.txt
"""
import hashlib, io, os, urllib.request, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
UA = {'User-Agent': 'Mozilla/5.0 (research script; stdlib urllib)'}
GET = {
    'pr126_Appendix-G.zip': 'https://dggs.alaska.gov/webpubs/data/pr126_Appendix-G.zip',
    'pr126_Appendix-A.zip': 'https://dggs.alaska.gov/webpubs/data/pr126_Appendix-A.zip',
    'davies2022_supp.zip': 'https://gchron.copernicus.org/articles/4/121/2022/gchron-4-121-2022-supplement.zip',
}


def main():
    os.makedirs(DATA, exist_ok=True)
    lines = []
    for name, url in GET.items():
        b = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()
        open(os.path.join(DATA, name), 'wb').write(b)
        lines.append(f'{hashlib.sha256(b).hexdigest()}  {name}  {url}')
    z = zipfile.ZipFile(os.path.join(DATA, 'pr126_Appendix-G.zip'))
    for m in z.namelist():
        if m.endswith('.csv'):
            open(os.path.join(DATA, os.path.basename(m)), 'wb').write(z.read(m))
    z = zipfile.ZipFile(os.path.join(DATA, 'davies2022_supp.zip'))
    open(os.path.join(DATA, 'davies2022_SI_tables.xlsx'), 'wb').write(z.read('SI_tables.xlsx'))
    for f in ('kaufman2012_supp_TabS1.pdf', 'kaufman2012_supp_TabS2.pdf', 'kaufman2012_tableS1.txt',
              'pr126-appendix_g_tephra_glass_data.csv', 'davies2022_SI_tables.xlsx'):
        p = os.path.join(DATA, f)
        if os.path.exists(p):
            lines.append(f'{hashlib.sha256(open(p, "rb").read()).hexdigest()}  {f}')
    out = os.path.join(HERE, 'results', 'fetch_sha256.txt')
    with open(out, 'a') as fh:
        fh.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
