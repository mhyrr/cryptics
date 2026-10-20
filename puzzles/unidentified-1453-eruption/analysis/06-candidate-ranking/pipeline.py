"""Shared code for 06-candidate-ranking. Imported by the scripts in this folder.

Nothing here reads the network. Every rule below is the pre-registered one in
README.md ("Pre-registration"); changing a constant here changes the experiment.
"""
import csv, math, random, re

# ---------------------------------------------------------------- constants
GRID_STEP = 0.1                    # calendar-year grid for date pdfs
WIN_IN, WIN_OUT = 1.0, 0.2         # window likelihood inside the band window / elsewhere in the wide prior
# Offsets relative to the Greenland sulfate onset (1453: 1453.05, mean of NEEM 1453.13 and TUNU 1453.00).
ONSET_1453 = 1453.05
WIN_NHET = (1452.90 - ONSET_1453, 1453.50 - ONSET_1453)    # 08 window.txt, NHET (ice + summer 1453)
WIN_NHET_ICE = (1452.90 - ONSET_1453, 1453.70 - ONSET_1453)  # 02 ice-only NHET window; used for calibration
WIN_TROP = (1452.00 - ONSET_1453, 1453.10 - ONSET_1453)    # 08 window.txt, tropical
WIN_PRIOR = (1451.50 - ONSET_1453, 1453.60 - ONSET_1453)   # wide prior (brief)
LIST_SPAN = (-13, 17)              # candidate filter: year +- unc overlaps onset year + this (1440-1470 for 1453)
SIG_14C_DEFAULT = 50.0             # 14C row with +-0 in GVP
SIG_OTHER_DEFAULT = 50.0           # tephrochronology / anthropology row with +-0
SIG_BLANK = 100.0                  # no dating method recorded
SIG_LAB_SYNTH = 40.0               # mode-2 synthetic radiocarbon measurement error (1 sigma, 14C yr)
SIZE_FACTOR = 2.0                  # sensitivity size likelihood: VSSI within [obs/F, obs*F]
SIZE_MIN_N = 3                     # cells with fewer GVP eruptions borrow the pooled-class estimate
SIZE_PERIOD = (1500, 1900)         # years used to estimate P(size | VEI, class)
BANDS = ['NHET', 'NTROP', 'STROP', 'SHET']
PRECISE = {'Observations: Reported', 'Sidereal: Dendrochronology', 'Sidereal: Varve Count'}


def band4(lat):
    if lat > 30: return 'NHET'
    if lat < -30: return 'SHET'
    return 'NTROP' if lat >= 0 else 'STROP'


def as_int(s, default=None):
    try: return int(s)
    except (TypeError, ValueError): return default


# ---------------------------------------------------------------- GVP
def load_gvp(eruptions_csv, volcanoes_csv):
    vol = {r['Volcano_Number']: r for r in csv.DictReader(open(volcanoes_csv, encoding='utf-8'))}
    rows = []
    for r in csv.DictReader(open(eruptions_csv, encoding='utf-8')):
        y = as_int(r['StartDateYear'])
        m = re.match(r'POINT \(([-\d.]+) ([-\d.]+)\)', r['GeoLocation'])
        if y is None or not m: continue
        v = vol.get(r['Volcano_Number'], {})
        rock = v.get('Major_Rock_Type', '')
        tect = v.get('Tectonic_Setting', '')
        rows.append(dict(
            vnum=r['Volcano_Number'], name=r['Volcano_Name'], enum=r['Eruption_Number'],
            confirmed=r['Activity_Type'].startswith('Confirmed'),
            vei=as_int(r['ExplosivityIndexMax']), method=r['StartEvidenceMethod'] or '',
            mod=r['StartDateYearModifier'], year=y, unc=as_int(r['StartDateYearUncertainty'], 0) or 0,
            month=as_int(r['StartDateMonth'], 0) or 0, unit=r['ActivityUnit'], area=r['ActivityArea'],
            end=as_int(r['EndDateYear']),
            lat=float(m.group(1)), lon=float(m.group(2)), region=v.get('Region', ''), subregion=v.get('Subregion', ''),
            rock=rock, tect=tect,
            sclass='rift-basalt' if rock.startswith('Basalt') and tect.startswith('Rift') else 'other'))
    return rows


# ---------------------------------------------------------------- IntCal20
class IntCal:
    def __init__(self, path):
        cal, c14, sig = [], [], []
        for line in open(path, encoding='utf-8'):
            if line.startswith('#') or not line.strip(): continue
            f = line.split(',')
            cal.append(1950.0 - float(f[0])); c14.append(float(f[1])); sig.append(float(f[2]))
        z = sorted(zip(cal, c14, sig))
        self.cal = [a for a, _, _ in z]; self.c14 = [b for _, b, _ in z]; self.sig = [c for _, _, c in z]

    def at(self, t):
        """Linear interpolation of (14C age, sigma) at calendar year CE t."""
        cal = self.cal
        if t <= cal[0]: return self.c14[0], self.sig[0]
        if t >= cal[-1]: return self.c14[-1], self.sig[-1]
        lo, hi = 0, len(cal) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if cal[mid] <= t: lo = mid
            else: hi = mid
        w = (t - cal[lo]) / (cal[hi] - cal[lo])
        return (self.c14[lo] + w * (self.c14[hi] - self.c14[lo]),
                self.sig[lo] + w * (self.sig[hi] - self.sig[lo]))

    def likelihood(self, age, err, grid):
        out = []
        for t in grid:
            mu, s = self.at(t)
            v = err * err + s * s
            out.append(math.exp(-0.5 * (age - mu) ** 2 / v) / math.sqrt(v))
        return out


def make_grid(lo, hi, step=GRID_STEP):
    n = int(round((hi - lo) / step))
    return [lo + (i + 0.5) * step for i in range(n)]


def normalise(p):
    s = sum(p)
    return [x / s for x in p] if s > 0 else p


def pdf_uniform(grid, a, b):
    """Uniform on [a, b), weighted by the overlap of each grid cell (cells are GRID_STEP wide)."""
    h = GRID_STEP / 2
    return normalise([max(0.0, min(b, t + h) - max(a, t - h)) for t in grid])


def pdf_normal(grid, mu, sd):
    return normalise([math.exp(-0.5 * ((t - mu) / sd) ** 2) for t in grid])


def pdf_14c(ic, grid, ages):
    """Product of IntCal20 likelihoods for ages that date the same event (rule: README).
    ages: list of (age_bp, err). A flat calendar prior over the grid."""
    p = [1.0] * len(grid)
    for a, e in ages:
        p = [x * y for x, y in zip(p, ic.likelihood(a, e, grid))]
    return normalise(p)


def hpd(grid, p, mass=0.954):
    """Highest-density region as a list of (start, end) intervals."""
    order = sorted(range(len(p)), key=lambda i: -p[i])
    keep, acc = set(), 0.0
    for i in order:
        keep.add(i); acc += p[i]
        if acc >= mass: break
    ivs, start = [], None
    for i in range(len(grid)):
        if i in keep and start is None: start = i
        if (i not in keep or i == len(grid) - 1) and start is not None:
            end = i if i in keep else i - 1
            ivs.append((grid[start] - GRID_STEP / 2, grid[end] + GRID_STEP / 2)); start = None
    return ivs


# ---------------------------------------------------------------- date pdf of a GVP row
def row_pdf(r, grid, ic, mode, true_date=None, rng=None, include_ice=False):
    """Calendar pdf for a GVP row's start date, or None if the row is dropped.
    mode 'as-is': GVP dates as stored. mode 'degraded': precise dates are replaced by a
    synthetic 14C age (IntCal20 mean at the date, + N(0, SIG_LAB_SYNTH) if rng is given)."""
    meth = r['method']
    if meth == 'Sidereal: Ice Core' and not include_ice:
        return None, 'dropped: ice-core date (leakage rule)'
    y, unc = r['year'], r['unc']
    precise = meth in PRECISE or meth == 'Sidereal: Ice Core'
    if precise and unc <= 1:
        if r['end'] is not None and r['end'] > y:
            a, b = y, r['end'] + 1          # multi-year eruption: climax anywhere in [start, end]
        elif r['month']:
            a = y + (r['month'] - 1) / 12.0; b = a + 1 / 12.0
        else:
            a, b = y, y + 1
        if mode == 'degraded':
            t = true_date if true_date is not None else (a + b) / 2
            mu, _ = ic.at(t)
            age = mu + (rng.gauss(0, SIG_LAB_SYNTH) if rng else 0.0)
            return pdf_14c(ic, grid, [(age, SIG_LAB_SYNTH)]), 'synthetic 14C'
        return pdf_uniform(grid, a, b), 'calendar'
    if precise:  # varve / ice counts with an uncertainty
        return pdf_normal(grid, y + 0.5, unc), 'normal (counted)'
    if meth == 'Isotopic: 14C (uncalibrated)':
        return pdf_14c(ic, grid, [(1950 - y, unc if unc > 0 else SIG_14C_DEFAULT)]), 'IntCal20 of 1950-year'
    if meth == 'Isotopic: 14C (calibrated)':
        return pdf_normal(grid, y + 0.5, unc if unc > 0 else SIG_14C_DEFAULT), 'normal (GVP cal)'
    if meth == '':
        return pdf_normal(grid, y + 0.5, max(unc, SIG_BLANK)), 'normal (no method)'
    return pdf_normal(grid, y + 0.5, unc if unc > 0 else SIG_OTHER_DEFAULT), 'normal (other)'


# ---------------------------------------------------------------- likelihood pieces
def window_lik(grid, onset, band, use_window=True, nhet=WIN_NHET):
    lo_p, hi_p = onset + WIN_PRIOR[0], max(onset + WIN_PRIOR[1], onset + nhet[1])
    w = nhet if band in ('NHET', 'SHET') else WIN_TROP
    lo_w, hi_w = onset + w[0], onset + w[1]
    out = []
    for t in grid:
        if not (lo_p <= t < hi_p): out.append(0.0)
        elif not use_window or lo_w <= t < hi_w: out.append(WIN_IN)
        else: out.append(WIN_OUT)
    return out


def p_date(pdf, lik):
    return sum(a * b for a, b in zip(pdf, lik))


def candidate_filter(rows, onset_year):
    lo, hi = onset_year + LIST_SPAN[0], onset_year + LIST_SPAN[1]
    out = []
    for r in rows:
        if r['vei'] is not None and r['vei'] < 4: continue
        if r['year'] + r['unc'] < lo or r['year'] - r['unc'] > hi: continue
        out.append(r)
    return out


# ---------------------------------------------------------------- size
class SizeModel:
    """P(VSSI in [obs/F, obs*F] | VEI, class), estimated as
    (# eVolv2k-attributed events in SIZE_PERIOD with that VEI/class and VSSI in range + 0.5)
    / (# GVP confirmed eruptions in SIZE_PERIOD with that VEI/class + 1).
    Unknown VEI: mixture over VEI with weights P(VEI | 14C- or tephra-dated, 1000-1900)."""
    def __init__(self, rows, attributed, exclude=None):
        self.rows, self.att = rows, [a for a in attributed if a is not exclude]
        lo, hi = SIZE_PERIOD
        self.den = {}
        for r in rows:
            if r['confirmed'] and r['vei'] is not None and lo <= r['year'] < hi:
                k = (min(r['vei'], 7), r['sclass']); self.den[k] = self.den.get(k, 0) + 1
        w = {}
        for r in rows:
            if (r['confirmed'] and r['vei'] is not None and 1000 <= r['year'] < 1900 and
                    (r['method'].startswith('Isotopic: 14C') or r['method'] == 'Correlation: Tephrochronology')):
                w[min(r['vei'], 7)] = w.get(min(r['vei'], 7), 0) + 1
        s = sum(w.values())
        self.vei_unknown = {v: c / s for v, c in sorted(w.items())}

    def p(self, vei, sclass, thr_lo, thr_hi=float('inf'), unknown_as=None):
        """Monotone in VEI: P(v) is capped by P(v') for every larger v' (isotonic cap, pre-registered)."""
        if vei is None:
            if unknown_as is not None: return self.p(unknown_as, sclass, thr_lo, thr_hi)
            return sum(wt * self.p(v, sclass, thr_lo, thr_hi) for v, wt in self.vei_unknown.items())
        v = min(vei, 7)
        return min(self._p(u, sclass, thr_lo, thr_hi) for u in range(v, 8))

    def _p(self, vei, sclass, thr_lo, thr_hi):
        """P(thr_lo <= VSSI <= thr_hi | VEI, class). Headline: thr_lo = obs - 1 sigma, no upper bound."""
        if vei is None:
            if unknown_as is not None: return self.p(unknown_as, sclass, thr_lo, thr_hi)
            return sum(wt * self.p(v, sclass, thr_lo, thr_hi) for v, wt in self.vei_unknown.items())
        v = min(vei, 7)
        lo, hi = SIZE_PERIOD
        classes = [sclass] if self.den.get((v, sclass), 0) >= SIZE_MIN_N else ['rift-basalt', 'other']
        k = sum(1 for a in self.att if a['vei'] is not None and min(a['vei'], 7) == v and a['sclass'] in classes
                and lo <= a['year'] < hi and thr_lo <= a['vssi'] <= thr_hi)
        n = sum(self.den.get((v, c), 0) for c in classes)
        n = max(n, k)
        return (k + 0.5) / (n + 1)


# ---------------------------------------------------------------- eVolv2k attributed events
GVP_NUM = {  # copied from ../03-latitude-posterior/calib_asymmetry.py (hand map, 2026-10-20)
    'Okataina-Tarawera': '241050', 'Krakatao': '262000', 'Askja': '373060',
    'Grímsvötn': '373010', 'Makian': '268070', 'Hokkaido-Komagatake': '285020', 'Toya': '285030',
    'Cosigüina': '344010', 'Zavaritskii-Simushir': '290180', 'Galunggung': '263140',
    'Tambora': '264040', 'Laki': '373010', 'Hekla': '372070', 'Katla': '372030',
    'Shikotsu': '285040', 'Tarumae': '285040', 'Fujisan': '283030', 'Gamkonora': '268040',
    'Mount Parker': '271011', 'Huaynaputina': '354030', 'Nevado del Ruiz': '351020',
    'Colima': '341040', 'Veiðivötn': '373030', 'Kuwae': '257070', 'Samalas': '264030',
    'Changbaishan': '305060', 'Churchill': '315030', 'Shiveluch': '300270',
    'Ilopango': '343060', 'Taup': '241070', 'Okmok': '311290',
}


def load_evolv2k(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('*/')) + 2
    ev = []
    for l in lines[start:]:
        if not l.strip(): continue
        f = l.split('\t')
        ev.append(dict(year=int(f[0]), month=int(f[2]), day=int(f[3]), lat=float(f[4]), dg=float(f[5]),
                       da=float(f[6]), vssi=float(f[7]), vssi_sd=float(f[8]), asy=float(f[9]), loc=f[10], teph=f[11]))
    return ev


def attribute(ev, rows):
    """Join named eVolv2k events to a GVP eruption row (same volcano, |year diff| <= 2, largest VEI)."""
    vol = {}
    for r in rows: vol.setdefault(r['vnum'], []).append(r)
    out = []
    for e in ev:
        if e['loc'] == 'N/A' or e['loc'].startswith('Unidentif'): continue
        key = next((k for k in GVP_NUM if e['loc'].startswith(k)), None)
        if key is None or key == 'Kuwae': continue
        vn = GVP_NUM[key]
        cands = [r for r in vol.get(vn, []) if abs(r['year'] - e['year']) <= 2 or
                 (r['end'] is not None and r['year'] <= e['year'] <= r['end'])]
        cands.sort(key=lambda r: (-(r['vei'] if r['vei'] is not None else -1), abs(r['year'] - e['year'])))
        g = cands[0] if cands else None
        anyrow = vol[vn][0]
        out.append(dict(e, key=key, vnum=vn, gvp=g, vei=g['vei'] if g else None,
                        sclass=anyrow['sclass'], glat=anyrow['lat'], band=band4(anyrow['lat'])))
    return out


# ---------------------------------------------------------------- asymmetry band likelihood (LOO)
def asym_kde_lik(asy, train, h=0.05):
    """03's KDE likelihood of ASY by band (SHET pool adds mirrored NHET), normalised."""
    out = {}
    for b in BANDS:
        mem = [a['asy'] for a in train if a['band'] == b]
        if b == 'SHET': mem = mem + [1 - a['asy'] for a in train if a['band'] == 'NHET']
        out[b] = (sum(math.exp(-0.5 * ((asy - m) / h) ** 2) for m in mem) / len(mem)) if mem else 0.0
        out[b] += 1e-3  # floor so that no band is impossible
    s = sum(out.values())
    return {b: v / s for b, v in out.items()}


def asym_window_lik(asy, train, half=0.125):
    out = {}
    for b in BANDS:
        mem = [a['asy'] for a in train if a['band'] == b]
        if b == 'SHET': mem = mem + [1 - a['asy'] for a in train if a['band'] == 'NHET']
        lo, hi = asy - half, asy + half
        if asy >= 1.0: lo, hi = 1.0 - 1e-9, 1.0 + 1e-9
        if asy <= 0.0: lo, hi = -1e-9, 1e-9
        k = sum(lo <= m <= hi for m in mem)
        out[b] = (k + 0.5) / (len(mem) + 1)
    s = sum(out.values())
    return {b: v / s for b, v in out.items()}


# ---------------------------------------------------------------- scorer
def score_candidates(cands, grid, ic, onset, band_lik, size_model, thr, mode='as-is', truth=None,
                     rng=None, nhet=WIN_NHET, use_window=True, overrides=None, unknown_as=None,
                     include_ice=False, thr_hi=float('inf')):
    """score = P(date | window) x P(band) x P(size). Returns scored rows, best first, and dropped rows.
    truth: (vnum, true_date) for calibration; the true volcano's rows get true_date in degraded mode."""
    out, dropped = [], []
    for r in cands:
        if overrides and r['enum'] in overrides:
            pdf, how = overrides[r['enum']]
        else:
            td = truth[1] if (truth and r['vnum'] == truth[0] and mode == 'degraded') else None
            pdf, how = row_pdf(r, grid, ic, mode, true_date=td, rng=rng, include_ice=include_ice)
        if pdf is None:
            dropped.append((r, how)); continue
        b = band4(r['lat'])
        pd = p_date(pdf, window_lik(grid, onset, b, use_window, nhet))
        pb = band_lik[b]
        ps = size_model.p(r['vei'], r['sclass'], thr, thr_hi, unknown_as=unknown_as)
        out.append(dict(r, band=b, p_date=pd, p_band=pb, p_size=ps, score=pd * pb * ps, how=how))
    out.sort(key=lambda x: -x['score'])
    return out, dropped


# ---------------------------------------------------------------- fast synthetic-14C date term (calibration, degraded mode)
class FastCal:
    """IntCal20 evaluated once on a coarse grid (1 yr, for normalisation) and a fine grid
    (0.1 yr, over the wide prior) around one onset."""
    def __init__(self, ic, onset, half=400):
        self.coarse = [t + 0.5 for t in range(int(onset) - half, min(int(onset) + half, 1950))]
        lo, hi = onset + WIN_PRIOR[0] - 0.05, onset + max(WIN_PRIOR[1], WIN_NHET_ICE[1]) + 0.05
        self.fine = make_grid(lo, hi)
        self.cc = [ic.at(t) for t in self.coarse]
        self.cf = [ic.at(t) for t in self.fine]
        self.onset = onset

    @staticmethod
    def _lik(age, err, curve):
        out = []
        for mu, s in curve:
            v = err * err + s * s
            out.append(math.exp(-0.5 * (age - mu) ** 2 / v) / math.sqrt(v))
        return out

    def p_date(self, age, err, band, nhet):
        norm = sum(self._lik(age, err, self.cc))  # per 1 yr
        if norm <= 0: return 0.0
        L = window_lik(self.fine, self.onset, band, True, nhet)
        num = sum(a * b for a, b in zip(self._lik(age, err, self.cf), L)) * GRID_STEP
        return num / norm
