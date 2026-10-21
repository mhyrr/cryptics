"""Fetch open sources for 17-distal-tephra into data/ and record sha256.

Run: python3 -I fetch17.py   (from this folder)
Only standard library. Downloads are data; parse them with `python3 -I`.
"""
import hashlib, os, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh) cryptics-ue1453/17'}

SOURCES = [
    # Tephrabase calendar-date search: tephra layers (tepherup=1) and eruptions (2) 1400-1520 CE
    ('tb_chrono_tephra_1400_1520.html',
     'https://www.tephrabase.org/cgi-bin/tbase_chrono1b.pl?tepherup=1&limiter=BT&year1=1400&year2=1520'),
    ('tb_chrono_erup_1400_1520.html',
     'https://www.tephrabase.org/cgi-bin/tbase_chrono1b.pl?tepherup=2&limiter=BT&year1=1400&year2=1520'),
    # Tephrabase radiocarbon-dated tephra search: 14C ages 250-700 BP (uncalibrated)
    ('tb_c14_250_700.html',
     'https://www.tephrabase.org/cgi-bin/tbase_ice_c14a.pl?limiter=BT&year1=250&year2=700'),
    # Garry Bog (N. Ireland) profile
    ('tb_site85_garrybog.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=85'),
    # Mackay et al. 2016 QSR 132 (CC BY), Newcastle eprint
    ('mackay2016.pdf',
     'https://eprints.ncl.ac.uk/fulltext.aspx?url=217810%2f43A6E4A1-C718-44F9-8669-73A5F19E4375.pdf&pub_id=217810'),
    # Chen et al. 2019 Lake Kushu glass data (Mendeley, CC BY)
    ('kushu_supp.xlsx',
     'https://data.mendeley.com/public-files/datasets/bf76cyncdj/files/6e4998ec-feb5-41a6-96a0-e22692ca56b0/file_downloaded'),
    # Tephrabase detail pages (tephra layer distribution, eruption records, 14C dates)
    ('tb_tephra86_grim1457.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=0&tephra=86&geochem=1'),
    ('tb_tephra85_grim1432.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=0&tephra=85&geochem=1'),
    ('tb_erup182_grim1457.html', 'https://www.tephrabase.org/cgi-bin/tbase_ice_erup2.pl?eruption=182'),
    ('tb_erup181_grim1432.html', 'https://www.tephrabase.org/cgi-bin/tbase_ice_erup2.pl?eruption=181'),
    ('tb_c14_tephra12.html', 'https://www.tephrabase.org/cgi-bin/tbase_ice_c14b.pl?tephra=12'),
    ('tb_site31_lochportain.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=31'),
    ('tb_tephra12_lochportainB.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=8&tephra=12'),
    ('tb_geo97.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_geo1.pl?tephra=97'),
    ('tb_geo86_NOT_grim1457_slethill.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_geo1.pl?tephra=86'),
    ('tb_geo109_lairg_LPB.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_geo1.pl?tephra=109'),
    ('tb_geo96_lochportain_H1510.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_geo1.pl?tephra=96'),
    ('tb_site1331_getvaltjarnen.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1331'),
    # Tephrabase: all-European distribution pages for local/unsourced and 15th-c layers
    ('tb_eu_tephra58.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=58&geochem=1'),
    ('tb_eu_tephra57.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=57&geochem=1'),
    ('tb_eu_tephra85.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=85&geochem=1'),
    ('tb_eu_tephra86.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=86&geochem=1'),
    ('tb_eu_tephra80.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=80&geochem=1'),
    ('tb_eu_tephra175.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=175&geochem=1'),
    ('tb_eu_tephra105.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=105&geochem=1'),
    ('tb_eu_tephra158.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=158&geochem=1'),
    ('tb_eu_tephra106.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=106&geochem=1'),
    ('tb_eu_tephra147.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=147&geochem=1'),
    ('tb_eu_tephra55.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=55&geochem=1'),
    ('tb_eu_tephra56.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=56&geochem=1'),
    ('tb_eu_tephra177.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=177&geochem=1'),
    ('tb_eu_tephra182.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=182&geochem=1'),
    ('tb_eu_tephra183.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=183&geochem=1'),
    ('tb_eu_tephra9.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=9&geochem=1'),
    ('tb_eu_tephra171.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=171&geochem=1'),
    ('tb_eu_tephra151.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=151&geochem=1'),
    ('tb_eu_tephra152.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=152&geochem=1'),
    ('tb_eu_tephra153.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=153&geochem=1'),
    ('tb_eu_tephra154.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=154&geochem=1'),
    ('tb_eu_tephra155.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=155&geochem=1'),
    ('tb_eu_tephra156.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=156&geochem=1'),
    ('tb_eu_tephra157.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=157&geochem=1'),
    ('tb_eu_tephra165.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=165&geochem=1'),
    ('tb_eu_tephra166.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=166&geochem=1'),
    ('tb_eu_tephra5.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro1.pl?country=999&tephra=5&geochem=1'),
    # Tephrabase site profiles (distal sites that caught 15th-c. or local layers)
    ('tb_site1486_lontjornane.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1486'),
    ('tb_site1305_cors_fochno.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1305'),
    ('tb_site1307_anlochmor.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1307'),
    ('tb_site1308_claraghmore_lake.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1308'),
    ('tb_site1309_claraghmore_bog.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1309'),
    ('tb_site1332_romanlode.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1332'),
    ('tb_site253_barnesmore.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=253'),
    ('tb_site260_mongan.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=260'),
    ('tb_site262_portmagee.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=262'),
    ('tb_site1314_sammakovuoma_lake.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1314'),
    ('tb_site1315_sammakovuoma_peat.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1315'),
    ('tb_site1312_svartkalsjarn.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1312'),
    ('tb_site1313_degero.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_teph1.pl?site=1313'),
    ('tb_geo3867_MOR-T1.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_geo1.pl?tephra=3867'),
    ('tb_geo3868_MOR-T2.html', 'https://www.tephrabase.org/cgi-bin/tbase_euro_geo1.pl?tephra=3868'),
    # Streeter & Dugmore 2014 QSR 86 (accepted text; dating basis of Grímsvötn 1432/1457)
    ('streeter_dugmore2014.pdf', 'https://research-repository.st-andrews.ac.uk/bitstream/10023/10712/1/accepted_text.pdf'),
    # Payne & Blackford 2008 Arctic 61(3), Kenai peat tephras (White Rose eprint)
    ('payne_blackford2008_kenai.pdf', 'https://eprints.whiterose.ac.uk/88124/1/Payne_BlackfordproofKenaiTephra.pdf'),
]


def main(only=None):
    out = []
    for name, url in SOURCES:
        if only and name not in only:
            continue
        path = os.path.join(DATA, name)
        try:
            d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
        except Exception as e:  # record failures, never hide them
            out.append(f'{name}\tFAILED\t{e}\t{url}')
            continue
        with open(path, 'wb') as f:
            f.write(d)
        out.append(f'{name}\t{hashlib.sha256(d).hexdigest()}\t{len(d)}\t{url}')
        time.sleep(1)
    with open(os.path.join(HERE, 'results', 'fetch_sha256.txt'), 'a') as f:
        f.write(f'# fetched {time.strftime("%Y-%m-%d %H:%M")}\n' + '\n'.join(out) + '\n')
    print('\n'.join(out))


if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
