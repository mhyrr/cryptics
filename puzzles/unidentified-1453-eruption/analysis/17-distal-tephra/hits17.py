"""Write results/hits.tsv: every layer the 17 sweep found in or near 1440-1470 CE,
with its dating evidence, proposed source, glass availability, source URL and
tier, plus great-circle distance (km) from the site to each candidate vent.

Run (from this folder):
    python3 -I hits17.py ../06-candidate-ranking/data/gvp_holocene_volcanoes.csv > results/hits.tsv

The rows are typed from the sources read in this experiment (README lists them).
Vent coordinates come from the GVP volcano list in 06's data (not typed here).
Site coordinates: from each paper; the Mackay 2016 ones are parsed from garbled
PDF text (degree-minute-second run together), good to ~0.02 deg. Kenai sites: not given.
"""
import csv, math, sys

VENTS = {  # label: GVP volcano number
    'Aniakchak': '312090', 'Shiveluch': '300270', 'Zavaritzki': '290180',
    'Grimsvotn': '373010', 'Katla': '372030', 'Hekla': '372070',
    'Furnas': '382100', 'Pinatubo': '273083', 'Rausudake': '285082',
}

COLS = ['id', 'layer', 'site', 'region', 'lat', 'lon', 'archive', 'dating_evidence',
        'age_CE', 'covers_1453', 'proposed_source', 'source_status', 'glass',
        'bears_on', 'url', 'tier', 'note']

HITS = [
    ['AHK04', 'Ahklun "0.4-ka tephra" (UA 1966; UA 1779 = 1974)',
     'Lone Spruce Pond; soil pit near Cascade Lake (Ahklun Mts)', 'SW Alaska', 60.01, -159.14,
     'lake core; soil pit',
     'LSP: clam age-depth model on 14C macrofossils, 377+-62 cal BP; soil pit: 14C 435+-15 BP (UCIAMS-23856) on wood & leaves BELOW the tephra (maximum age)',
     'LSP 1511-1635; soil-pit max 1435-1468 (calib17)', 'LSP no; soil-pit max yes',
     'Aniakchak (glass indistinguishable from CFE II; authors: may be redeposited)', 'tentative',
     'yes: Kaufman 2012 Table 6 + Table S1 (bimodal 59.8 / 71.3 wt% SiO2)',
     'H10', 'https://doi.org/10.1002/jqs.1552', 'SCHOLARLY',
     'rhyodacite mode 71.3 wt% SiO2 is outside the Half Cone Pink glass range 68.3-69.8 (glass17); the two sites disagree on age'],
    ['KEN-MP39', 'MP 39 (visible, 4 mm)', 'Moose Pass mire', 'Kenai Peninsula, Alaska', None, None,
     'peat', 'linear extrapolation from one bulk-peat 14C 510+-100 BP (Gd-15806, 40-50 cm)', 'c. 1520 (authors); date bracket 1282-1633 (calib17)', 'possible (weak dating)',
     '"previously unidentified eruption"; glass closest to Crater Peak (Spurr) c. 300 BP', 'unsourced',
     'yes: Payne & Blackford 2008 Table 1 + Appendix (andesite 60.6 wt% SiO2)', 'H10',
     'https://doi.org/10.14430/arctic22', 'SCHOLARLY',
     'screen: Crater Peak SC6 0.97 and Aniakchak CFE II andesite SC6 0.96: cannot separate (glass17)'],
    ['KEN-ST24', 'ST 24 (visible, 5 mm)', 'Sterling mire', 'Kenai Peninsula, Alaska', None, None,
     'peat', 'linear interpolation from one bulk-peat 14C 850+-65 BP (URCRM-1273, 35-40 cm)', 'c. 1480 (authors)', 'possible (weak dating)',
     'closest to Katmai 1912 / Augustine 1883, "cannot be reliably determined"', 'unsourced',
     'yes: Table 1 (rhyolite 76.9 wt% SiO2)', 'H10 (against)', 'https://doi.org/10.14430/arctic22', 'SCHOLARLY',
     'SiO2 76.9 is far from Half Cone Pink glass (68.3-69.8): not Half Cone Pink'],
    ['KEN-micro', 'unanalysed microtephras', 'Moose Pass (c. 510, 550 cal BP); Sterling (c. 590 cal BP)', 'Kenai Peninsula, Alaska', None, None,
     'peat', 'linear inter/extrapolation from single bulk-peat 14C ages', 'c. 1360-1440', 'possible (weak dating)',
     'none', 'unsourced', 'no', 'H10, H6', 'https://doi.org/10.14430/arctic22', 'SCHOLARLY', 'no geochemistry'],
    ['CL7', 'CL-7 cryptotephra', 'Cascade Lake (Brooks Range)', 'Arctic Alaska', 68.38, -154.61,
     'lake core', 'Bayesian age model (14C + 210Pb)', '1325-1875 (625-75 cal BP, 2 sigma)', 'yes (broad)',
     'Aniakchak (dominant population; not tied to CFE II or a named post-caldera eruption); six KO-like points', 'tentative',
     'yes: Davies et al. 2022 supplement (not downloaded)', 'H10', 'https://doi.org/10.5194/gchron-4-121-2022', 'SCHOLARLY',
     'canon line 184-186 says it matches CFE II; the paper says Aniakchak in general and does not rule out younger eruptions. Not the Ahklun Cascade Lake'],
    ['FBB12-47', 'FBB12-47 cryptotephra (15 shards/cm3, 2 analysed)', 'Framboise Bog', 'Nova Scotia', 45.717, -60.553,
     'peat', 'Bacon 14C age-depth model', '1374-1677 (2 sigma)', 'yes (broad)',
     'possibly MSH set W (1479-82); authors: insufficient data', 'tentative',
     'yes: Mackay 2016 Table 1 (n=2)', 'none (MSH)', 'https://doi.org/10.1016/j.quascirev.2015.11.011', 'SCHOLARLY',
     'screen: MSH We SC6 0.98 (glass17)'],
    ['SCH10-57', 'SCH10-57 cryptotephra', 'Saco Heath', 'Maine', 43.551, -70.334,
     'peat', 'Bacon 14C age-depth model; age shown only in Fig. 2 / Appendix D', 'not stated in text (below SCH10-42, AD 1572-1762)', 'unknown',
     'none ("not correlated")', 'unsourced', 'yes: Table 1 (n=4, dacite-rhyolite 70.8 wt%)', 'H6, H10', 'https://doi.org/10.1016/j.quascirev.2015.11.011', 'SCHOLARLY',
     'screen: no reference >= 0.95; nearest MSH T and Aniakchak CFE II rhyodacite (SC6 0.92, 0.91)'],
    ['VDB12-53', 'VDB12-53 cryptotephra', 'Villagedale Bog', 'Nova Scotia', 43.519, -65.518,
     'peat', 'Bacon 14C age-depth model; age shown only in Fig. 2 / Appendix D', 'not stated in text (below VDB12-42, AD 1517-1750)', 'unknown',
     'authors: "similarities with Japanese tephra", too few shards', 'unsourced', 'yes: Table 1 (n=2)', 'H6', 'https://doi.org/10.1016/j.quascirev.2015.11.011', 'SCHOLARLY',
     'screen: Augustine B 0.95, Ta-c2 0.94 (glass17); n=2'],
    ['VILLAGEDALE', 'Villagedale tephra (VDB12-42, SCH10-42 pop 1)', 'Villagedale Bog; Saco Heath', 'Nova Scotia; Maine', 43.519, -65.518,
     'peat', 'Bacon 14C age-depth models', '1517-1750; 1572-1762 (2 sigma)', 'no',
     'authors: within Icelandic and Aleutian range, uncorrelated', 'unsourced', 'yes: Table 1', 'none',
     'https://doi.org/10.1016/j.quascirev.2015.11.011', 'SCHOLARLY',
     'out of window; screen: MSH layer T (1800) SC6 0.96-0.97, post hoc and younger than the model ages'],
    ['LPB', 'Loch Portain B Tephra', 'Loch Portain (North Uist); Lairg AG3 (Sutherland)', 'Scotland', 57.633, -7.10,
     'peat', '14C on peat: GU-3009 540+-50 BP at 0.15-0.16 m (below); GU-3010 360+-70 BP at 0.13-0.14 m (inside); same 0.10-0.15 m interval as Hekla 1510',
     'below-date 1304-1447; level date 1428-1660 (calib17)', 'yes',
     'unassigned (Tephrabase lists it among Icelandic layers)', 'unsourced',
     'yes: Tephrabase 6 shards (Loch Portain) + 2 (Lairg); rhyolite 74-77 wt% SiO2, K2O 3.0-4.9', 'H5, H6',
     'https://www.tephrabase.org/cgi-bin/tbase_ice_c14b.pl?tephra=12', 'SCHOLARLY (via Tephrabase, SECONDARY)',
     'Dugmore, Larsen & Newton 1995 not read; screen: unlike all Alaskan/Cascade/Kamchatka references in hand (SC6 <= 0.89)'],
    ['MOR-T2', 'MOR-T2 cryptotephra (trachyte)', 'An Loch Mor, Inis Oirr', 'W Ireland', 53.0593, -9.5074,
     'lake core', 'Chambers et al. 2004 age model (not read); "c. 1400 AD" per Ramalho et al. 2023', 'c. 1400 (age model)', 'no (correlated to 1439-43)',
     'Furnas I (Sao Miguel, Azores; 1439-43 CE, historical)', 'sourced (conference abstract)',
     'yes: Tephrabase 27 shards (trachyte ~64.7 wt% SiO2, K2O 5.7)', 'H3 (NHET Atlantic), new: Azores',
     'https://doi.org/10.5194/egusphere-egu23-541', 'SCHOLARLY (abstract)',
     'Chambers 2004 had assigned the trachytes to Jan Mayen; Azores reassignment is a 2023 abstract. Shows a VEI-4 Azores eruption reached Ireland'],
    ['GRIM1457', 'Grimsvotn 1457 Tephra', '141 soil sections, Skaftartunga', 'S Iceland', 63.74, -18.61,
     'soil (aeolian)', 'sediment accumulation-rate date between historical tephras (Streeter & Dugmore 2014); uncertainty definition not read', '1457 +- 5', 'edge (1452-1462 if +-5 is a range)',
     'Grimsvotn', 'sourced', 'Tephrabase: 9 of 141 sites have a data link; 132 "no data"', 'H5 (Grimsvotn)',
     'https://www.tephrabase.org/cgi-bin/tbase_ice_erup2.pl?eruption=182', 'SECONDARY (database; source SCHOLARLY, not read)',
     'proximal-regional, not distal; no non-Iceland occurrence in Tephrabase'],
    ['GRIM1432', 'Grimsvotn 1432 Tephra', '88 soil sections, S Iceland', 'S Iceland', None, None,
     'soil (aeolian)', 'as GRIM1457', '1432 +- 5', 'no', 'Grimsvotn', 'sourced', 'Tephrabase', 'H5 (Grimsvotn)',
     'https://www.tephrabase.org/cgi-bin/tbase_ice_erup2.pl?eruption=181', 'SECONDARY', 'no non-Iceland occurrence in Tephrabase'],
    ['RA1', 'Ra-1 (Rausu 1) tephra', 'Rausudake (Shiretoko)', 'E Hokkaido', 44.076, 145.122,
     'proximal tephra', 'GVP: 14C calibrated, 1350 +- 100; Cabinet Office table: "500-700" (yr BP)', '1250-1450', 'edge',
     'Rausudake', 'sourced', 'not found', 'H6 (Hokkaido), size',
     'https://www.bousai.go.jp/kaigirep/chuobou/senmon/nihonkaiko_chisimajishin/10/pdf/siryou4.pdf', 'SECONDARY (GVP; government table)',
     'GVP VEI 3; same size problem as Karymsky (13)'],
]


def hav(a, b, c, d):
    r = math.radians
    h = math.sin(r(c - a) / 2) ** 2 + math.cos(r(a)) * math.cos(r(c)) * math.sin(r(d - b) / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(h))


def main(gvp):
    coords = {}
    for row in csv.DictReader(open(gvp, encoding='utf-8')):
        for k, num in VENTS.items():
            if row['Volcano_Number'] == num:
                coords[k] = (float(row['Latitude']), float(row['Longitude']))
    w = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    w.writerow(COLS + [f'km_{k}' for k in VENTS])
    for h in HITS:
        lat, lon = h[4], h[5]
        km = [f'{hav(lat, lon, *coords[k]):.0f}' if lat is not None else '' for k in VENTS]
        w.writerow(['' if x is None else x for x in h] + km)


if __name__ == '__main__':
    main(sys.argv[1])
