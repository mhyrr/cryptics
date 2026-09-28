#!/usr/bin/env python3
"""Score caption-to-seed derivation. Every rule is in PROTOCOL.md. Run once.

python3 score.py            write results.json
python3 score.py --check    verify results.json reproduces

The pure functions take data structures, so test_score.py runs them on
synthetic inputs without touching a seed.
"""
import collections, hashlib, importlib.util, itertools, json, random, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = HERE.parent
SEED = 20260927
NPERM = 2000
LAT_TIERS = ["exact", "aspirate", "skeleton", "near"]
GRK_TIERS = ["greek", "greek_itacist"]
PRIMARY = 2                                  # index of skeleton in LAT_TIERS
DIGRAPHS = ["SCH", "CH", "PH", "TH", "BH", "DH", "GH", "KH"]
ASPIRATE = {"SCH": "S", "CH": "C", "BH": "B", "TH": "T"}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sys.path.insert(0, str(A / "14-caption-seed-test"))                          # run.py imports lookup
e14 = load_module("e14_run", A / "14-caption-seed-test" / "run.py")          # skeleton, near: unchanged
l14 = load_module("e14_lookup", A / "14-caption-seed-test" / "lookup.py")    # key, strip_frame: unchanged
rom = load_module("e17_romanize", A / "17-greek-latin-seeds" / "romanize.py")  # variants, letters: frozen


# ---------------------------------------------------------------- normalization

def strip_marks(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def norm(s):
    """Experiment 14's exact() with diacritics stripped first: upper, long s S, J I, V W U, A-Z only."""
    s = strip_marks(s.replace("ſ", "s").replace("æ", "ae").replace("Æ", "AE").replace("œ", "oe").replace("Œ", "OE"))
    s = s.upper().replace("J", "I").replace("V", "U").replace("W", "U")
    return "".join(c for c in s if "A" <= c <= "Z")


def skel(s):
    return e14.skeleton(norm(s))


def lat_agree_key(form):
    """Reader-agreement key for a Latin-script form. PROTOCOL.md, Agreement."""
    s = form.replace("ſ", "s").replace("æ", "ae").replace("Æ", "ae").replace("œ", "oe").replace("Œ", "oe")
    s = strip_marks(s).lower()
    s = "".join(c if ("a" <= c <= "z" or c == "?") else " " if c.isspace() or c in "-" else "" for c in s)
    return " ".join(s.split())


ROUGH = "̔"


def grk_agree_key(form):
    s = unicodedata.normalize("NFD", form.lower())
    out = []
    for c in s:
        if c == ROUGH:
            out.append(c)
        elif unicodedata.combining(c):
            continue
        else:
            c = rom.FOLD.get(c, c)
            c = "σ" if c == "ς" else c
            if c.isspace():
                out.append(" ")
            elif c == "?" or "α" <= c <= "ω" or c in "ϊϋ" or c in "στου":
                out.append(c)
    return " ".join("".join(out).split())


def agreed(forms_a, forms_b, keyf):
    """Multiset intersection of the two readers' forms, '?' forms dropped."""
    ca = collections.Counter(k for k in map(keyf, forms_a or []) if k and "?" not in k)
    cb = collections.Counter(k for k in map(keyf, forms_b or []) if k and "?" not in k)
    return sorted((ca & cb).elements())


def tokens(form):
    words = form.split()
    return words + (["".join(words)] if len(words) > 1 else [])


# ---------------------------------------------------------------- tiers

def aspirate_variants(n):
    """All spellings of an A-Z form after any subset of the four aspirate types, each type everywhere."""
    units, i = [], 0
    while i < len(n):
        if n[i:i + 3] == "SCH":
            units.append("SCH"); i += 3
        elif n[i:i + 2] in ("CH", "BH", "TH"):
            units.append(n[i:i + 2]); i += 2
        else:
            units.append(n[i]); i += 1
    present = sorted({u for u in units if u in ASPIRATE})
    out = set()
    for r in range(len(present) + 1):
        for chosen in itertools.combinations(present, r):
            out.add("".join(ASPIRATE[u] if u in chosen else u for u in units))
    return out


def greek_sets(g):
    """Frozen experiment 17 variants, and the itacist additions (its post hoc code, declared here)."""
    g = "".join(c for c in g if not c.isspace())
    base, rough = rom.letters(g)
    if not base:
        return set(), set()
    frozen = {norm(v) for v in rom.variants(g)}
    ita = set(frozen)
    it = base.replace("ει", "ι").replace("η", "ι")
    if it != base:
        for v in rom.variants(it):
            ita.add(norm(v))
            if rough:
                ita.add("H" + norm(v))
    return frozen, ita


class Candidates:
    """One caption's candidate forms, with provenance, and precomputed tier sets."""

    def __init__(self, lat, grk):
        # lat, grk: lists of (token, provenance dict)
        self.lat, self.grk = lat, grk
        self.exact = collections.defaultdict(list)
        self.asp = collections.defaultdict(list)
        self.sk = collections.defaultdict(list)
        for tok, prov in lat:
            n = norm(tok)
            if not n:
                continue
            self.exact[n].append((tok, prov))
            for v in aspirate_variants(n):
                self.asp[v].append((tok, prov))
            self.sk[e14.skeleton(n)].append((tok, prov))
        self.g0 = collections.defaultdict(list)
        self.g1 = collections.defaultdict(list)
        for tok, prov in grk:
            f, i = greek_sets(tok)
            for v in f:
                self.g0[v].append((tok, prov))
            for v in i:
                self.g1[v].append((tok, prov))

    def lat_level(self, target):
        """Lowest Latin-script tier at which the target matches, or None."""
        n = norm(target)
        if n in self.exact:
            return 0
        if n in self.asp:
            return 1
        s = e14.skeleton(n)
        if s in self.sk:
            return 2
        if any(e14.near(s, k) for k in self.sk):
            return 3
        return None

    def grk_level(self, target):
        n = norm(target)
        if n in self.g0:
            return 0
        if n in self.g1:
            return 1
        return None

    def matches(self, target, level):
        """Candidate (token, provenance) pairs matching the target at exactly this Latin tier."""
        n = norm(target)
        s = e14.skeleton(n)
        if level == 0:
            return self.exact.get(n, [])
        if level == 1:
            return self.asp.get(n, [])
        if level == 2:
            return self.sk.get(s, [])
        return [m for k, ms in self.sk.items() if e14.near(s, k) for m in ms]

    def grk_matches(self, target, level):
        n = norm(target)
        return (self.g0 if level == 0 else self.g1).get(n, [])


def level_of(cands, targets):
    """Best (lat, grk) levels over a list of target strings (one grid's seed, or its S1 readings)."""
    lat = [l for l in (cands.lat_level(t) for t in targets) if l is not None]
    grk = [l for l in (cands.grk_level(t) for t in targets) if l is not None]
    return (min(lat) if lat else None, min(grk) if grk else None)


# ---------------------------------------------------------------- counting and controls

def counts(levels):
    """Cumulative hit counts per tier from a list of (lat, grk) levels."""
    out = {t: sum(1 for l, _ in levels if l is not None and l <= i) for i, t in enumerate(LAT_TIERS)}
    for i, t in enumerate(GRK_TIERS):
        out[t] = sum(1 for _, g in levels if g is not None and g <= i)
    out["all_tiers"] = sum(1 for l, g in levels if (l is not None and l <= PRIMARY) or g is not None)
    out["all_with_near"] = sum(1 for l, g in levels if l is not None or g is not None)
    return out


def permutation_test(grids, matrix, groups, draws=NPERM, seed=SEED):
    """grids: list of ids; matrix[(g, c)] -> (lat, grk) for grid g read against caption c's candidates.
    groups: lists of grid ids whose captions are permuted among themselves."""
    observed = counts([matrix[(g, g)] for g in grids])
    rng = random.Random(seed)
    tallies = collections.defaultdict(list)
    for _ in range(draws):
        assign = {}
        for grp in groups:
            perm = rng.sample(grp, len(grp))
            assign.update(zip(grp, perm))
        c = counts([matrix[(g, assign[g])] for g in grids])
        for t, v in c.items():
            tallies[t].append(v)
    out = {}
    for t, obs in observed.items():
        xs = tallies[t]
        out[t] = {"observed": obs, "control_mean": round(sum(xs) / len(xs), 2), "control_max": max(xs),
                  "p": round((1 + sum(x >= obs for x in xs)) / (1 + len(xs)), 4)}
    return out


def build_matrix(grids, targets, cands, pairs):
    """(lat, grk) level for every needed (grid, caption) pair."""
    return {(g, c): level_of(cands[c], targets[g]) for g, c in pairs}


def score_cohort(grids, chapter_of, targets, cands, draws=NPERM, seed=SEED):
    """Observed counts with both controls. grids: eligible grid ids (caption id = grid id)."""
    by_ch = collections.defaultdict(list)
    for g in grids:
        by_ch[chapter_of[g]].append(g)
    pairs = {(g, c) for g in grids for c in grids}
    matrix = build_matrix(grids, targets, cands, pairs)
    within = permutation_test(grids, matrix, list(by_ch.values()), draws, seed)
    across = permutation_test(grids, matrix, [list(grids)], draws, seed + 1)
    return matrix, {"within_chapter": within, "across_cohort": across}


def verdict(n_eligible, observed, p):
    if n_eligible < 100:
        return "too few seeds"
    share = observed / n_eligible
    if share >= 0.60 and p < 0.001:
        return "seed layer derived"
    if p < 0.01 and share < 0.60:
        return "partial"
    if p >= 0.05:
        return "not supported"
    return "open"


# ---------------------------------------------------------------- S4 spelling

def units_of(n):
    """Units of an A-Z form for S4: digraphs, lone H, doubled runs, other letters."""
    out, i = [], 0
    while i < len(n):
        if n[i:i + 3] == "SCH":
            out.append(("SCH", "SCH", "S")); i += 3; continue
        two = n[i:i + 2]
        if two in DIGRAPHS:
            out.append((two, two, two[0])); i += 2; continue
        if n[i] == "H":
            out.append(("H", "H", "")); i += 1; continue
        j = i + 1
        while j < len(n) and n[j] == n[i] and n[j:j + 2] not in DIGRAPHS and n[j:j + 3] != "SCH":
            j += 1
        if j - i >= 2:
            out.append(("double", n[i:j], n[i])); i = j; continue
        out.append((None, n[i], n[i])); i += 1
    return out


def s4_marks(seed, form):
    """Per variable unit of the printed form: 'kept', 'reduced' or 'ambiguous'; None if no assignment fits."""
    units = units_of(norm(form))
    var = [k for k, u in enumerate(units) if u[0] is not None]
    if len(var) > 14:
        return None
    target = norm(seed)
    fits = []
    for choice in itertools.product((0, 1), repeat=len(var)):
        pick = dict(zip(var, choice))
        s = "".join(u[2] if pick.get(k) else u[1] for k, u in enumerate(units))
        if s == target:
            fits.append(pick)
    if not fits:
        return None
    marks = []
    for k in var:
        vals = {f[k] for f in fits}
        marks.append((units[k][0], "ambiguous" if len(vals) > 1 else ("reduced" if vals == {1} else "kept")))
    return marks


# ---------------------------------------------------------------- inputs

def load_readings(folder):
    """Raw dictionary readings: {entry_id: {'A': item, 'B': item}}."""
    out = collections.defaultdict(dict)
    for f in sorted(Path(folder).glob("readings-R*-*.json")):
        side = re.search(r"-([AB])\.json$", f.name).group(1)
        for it in json.load(open(f, encoding="utf8"))["items"]:
            out[it["crop"]][side] = it
    return out


def agreed_entries(readings):
    """Agreed forms per entry and column, and the agreed printed headword."""
    out = {}
    for eid, sides in readings.items():
        a, b = sides.get("A", {}), sides.get("B", {})
        ha, hb = lat_agree_key(a.get("headword_printed") or ""), lat_agree_key(b.get("headword_printed") or "")
        out[eid] = {"hebrew": agreed(a.get("hebrew"), b.get("hebrew"), lat_agree_key),
                    "latin": agreed(a.get("latin"), b.get("latin"), lat_agree_key),
                    "greek": agreed(a.get("greek"), b.get("greek"), grk_agree_key),
                    "headword": ha if ha and ha == hb and "?" not in ha else None,
                    "found": [bool(a.get("entry_found")), bool(b.get("entry_found"))]}
    return out


def headword_identity(printed, nomination):
    """D3: the agreed printed headword has the nomination's experiment 14 key (any '/' segment)."""
    if not printed:
        return False
    want = {l14.key(nomination)} | {l14.key(c) for c in l14.strip_frame(nomination)}
    segs = [s.strip(" .,:;") for s in re.split(r"[/|]", printed)]
    return any(l14.key(s) in want for s in segs if s)


def caption_candidates(noms, headword_entries, entries, manifest_by_id):
    """noms: list of {'german', 'nominator'}. Returns Candidates and a stage summary."""
    lat, grk, located, with_forms = [], [], [], []
    for n in noms:
        for eid in headword_entries.get(n["german"].strip(), []):
            located.append(eid)
            e = entries.get(eid)
            if not e:
                continue
            m = manifest_by_id[eid]
            base = {"headword": n["german"].strip(), "nominator": n.get("nominator"), "entry": eid,
                    "volume": m["volume"], "scan": m["scan"], "column": m["column"],
                    "box": m["parts"][0]["box"], "printed_headword": e["headword"],
                    "identity": headword_identity(e["headword"], n["german"].strip())}
            for col in ("hebrew", "latin"):
                for form in e[col]:
                    with_forms.append(eid)
                    for t in tokens(form):
                        lat.append((t, dict(base, form=form, language=col)))
            for form in e["greek"]:
                with_forms.append(eid)
                for t in tokens(form):
                    grk.append((t, dict(base, form=form, language="greek")))
    return Candidates(lat, grk), {"nominations": len(noms), "located": len(set(located)),
                                  "with_forms": len(set(with_forms))}


def top_consensus(ra, rb):
    """Experiment 25's consensus rule on the whole grid; returns rows with '?' for unknown, or None."""
    if not ra or not rb or list(map(len, ra)) != list(map(len, rb)):
        return None
    f = lambda c: "I" if c == "J" else c
    return ["".join(f(x) if f(x) == f(y) and "A" <= f(x) <= "Z" else "?" for x, y in zip(a, b))
            for a, b in zip(ra, rb)]


def dresden_grids():
    out = {}
    for reader in "AB":
        for f in sorted((A / "25-dresden-blind-test" / "readings" / reader).glob("R*.json")):
            for it in json.load(open(f))["items"]:
                out.setdefault(it["locator_id"], {})[reader] = [r.upper() for r in it.get("rows") or []]
    return {k: top_consensus(v.get("A"), v.get("B")) for k, v in out.items()}


def pilot_seeds():
    out = {}
    for g in json.load(open(A / "22-dresden-witness-pilot" / "posthoc-collation.json"))["grids"]:
        cells = [c for c in (g.get("cells") or []) if c["row_group"] == 1]
        cells.sort(key=lambda c: c["position"])
        out[g["locator_id"]] = "".join(c["consensus"] if "A" <= c["consensus"] <= "Z" else "?" for c in cells) if cells else None
    return out


def warburg_seeds():
    """Experiment 20's load_reader and top-row rule, unchanged."""
    def load(name):
        out = {}
        for it in json.load(open(A / "20-warburg-witness" / name))["items"]:
            rows = ["".join(c if ("A" <= c <= "Z" or c in ".?") else "" for c in r.upper().replace(" ", "").replace("J", "I"))
                    for r in it["rows"]]
            out[(it["chapter"], it["number"])] = [r for r in rows if r]
        return out
    a, b = load("readings-A.json"), load("readings-B.json")
    out = {}
    for key in set(a) | set(b):
        ra, rb = a.get(key, []), b.get(key, [])
        out[key] = ra[0] if ra and rb and ra[0] == rb[0] and "?" not in ra[0] and "." not in ra[0] else None
    return out


# ---------------------------------------------------------------- reporting

def chains(g, seed, cands, lat, grk):
    out = []
    if lat is not None and lat <= PRIMARY:
        for tok, prov in cands.matches(seed, lat):
            out.append(dict(prov, token=tok, tier=LAT_TIERS[lat]))
    if grk is not None:
        for tok, prov in cands.grk_matches(seed, grk):
            out.append(dict(prov, token=tok, tier=GRK_TIERS[grk]))
    seen, uniq = set(), []
    for c in out:
        k = (c["entry"], c["form"], c["token"], c["tier"], c["headword"])
        if k not in seen:
            seen.add(k)
            uniq.append(c)
    return uniq


def failure(g, stage, lat, grk, other, elsewhere):
    if stage["nominations"] == 0:
        return "F1 no nomination", []
    if stage["located"] == 0:
        return "F2 no entry located", []
    if stage["with_forms"] == 0:
        return "F3 entry located, no agreed form", []
    flags = []
    if lat == 3:
        flags.append("near")
    if grk is not None:
        flags.append("greek_itacist" if grk == 1 else "greek")
    if other:
        flags.append("other_caption")
    if elsewhere:
        flags.append("elsewhere")
    return "F4 agreed forms, no match", flags


def run_cohort(name, ids, chapter_of, seeds, cands, stages, read_set, extra_targets=None):
    """Score one cohort. ids: all grid ids of the cohort; seeds: id -> seed or None (ineligible)."""
    eligible = [g for g in ids if seeds.get(g) and "?" not in seeds[g]]
    ineligible = sorted(g if isinstance(g, str) else f"{g[0]}/{g[1]}" for g in ids if g not in eligible)
    targets = {g: [seeds[g]] for g in eligible}
    matrix, tests = score_cohort(eligible, chapter_of, targets, cands)
    derivations, failures = [], []
    for g in eligible:
        lat, grk = matrix[(g, g)]
        gid = g if isinstance(g, str) else f"{g[0]}/{g[1]}"
        if (lat is not None and lat <= PRIMARY) or grk is not None:
            derivations.append({"grid": gid, "chapter": chapter_of[g], "seed": seeds[g],
                                "tier": LAT_TIERS[lat] if lat is not None and lat <= PRIMARY else None,
                                "greek_tier": GRK_TIERS[grk] if grk is not None else None,
                                "chains": chains(g, seeds[g], cands[g], lat, grk)})
        if lat is None or lat > PRIMARY:
            other = sorted(str(c if isinstance(c, str) else f"{c[0]}/{c[1]}") for c in eligible
                           if c != g and chapter_of[c] == chapter_of[g]
                           and (matrix[(g, c)][0] is not None and matrix[(g, c)][0] <= PRIMARY))
            elsewhere = read_set.lat_level(seeds[g]) is not None and read_set.lat_level(seeds[g]) <= PRIMARY
            stage, flags = failure(g, stages[g], lat, grk, other, elsewhere)
            failures.append({"grid": gid, "chapter": chapter_of[g], "seed": seeds[g], "stage": stage,
                             "flags": flags, "other_caption": other})
    n = len(eligible)
    prim = tests["within_chapter"]["skeleton"]
    return {"cohort": name, "grids": len(ids), "eligible": n, "ineligible": ineligible,
            "tests": tests, "share_skeleton": round(prim["observed"] / n, 4) if n else None,
            "verdict": verdict(n, prim["observed"], prim["p"]),
            "failure_stages": dict(sorted(collections.Counter(f["stage"] for f in failures).items())),
            "failure_flags": dict(sorted(collections.Counter(x for f in failures for x in f["flags"]).items())),
            "derivations": derivations, "failures": failures}, matrix, eligible


def language_columns(derivs):
    tally = collections.Counter()
    for d in derivs:
        cols = sorted({c["language"] for c in d["chains"]})
        tally["+".join(cols)] += 1
    return dict(sorted(tally.items()))


def spelling(derivs):
    per = collections.defaultdict(collections.Counter)
    unexplained = []
    for d in derivs:
        seen = set()
        for c in d["chains"]:
            if c["language"] == "greek" or c["form"] in seen:
                continue
            seen.add(c["form"])
            marks = s4_marks(d["seed"], c["token"])
            if marks is None:
                unexplained.append({"grid": d["grid"], "seed": d["seed"], "form": c["token"]})
                continue
            for kind, m in marks:
                per[kind][m] += 1
    return {"per_unit": {k: dict(v) for k, v in sorted(per.items())}, "no_per_occurrence_fit": unexplained}


def identity_split(derivs):
    ident = sum(1 for d in derivs if d["tier"] and any(c["identity"] for c in d["chains"] if c["language"] != "greek"))
    return {"skeleton_derivations": sum(1 for d in derivs if d["tier"]), "with_identity_entry": ident}


def centre_targets(rows):
    n = len(rows)
    if n < 5 or n % 2 == 0 or any(len(r) != n for r in rows):
        return None, None
    row = rows[n // 2]
    if "?" in row:
        return None, None
    h = (n + 1) // 2
    half = sorted({row[:h], row[::-1][:h]})
    full = [row, row[::-1]] if row != row[::-1] else None
    return half, full


# ---------------------------------------------------------------- main

def main():
    cohort = json.load(open(HERE / "cohort.json", encoding="utf8"))
    noms = {it["key"]: [dict(n, nominator=it.get("_nominator") or n.get("nominator")) for n in it["nominations"]]
            for it in json.load(open(HERE / "nominations.json", encoding="utf8"))["items"]}
    manifest = json.load(open(HERE / "entries-manifest.json", encoding="utf8"))
    by_id = {e["entry_id"]: e for e in manifest["entries"]}
    hw = manifest["headword_entries"]
    entries = agreed_entries(load_readings(HERE / "readings"))
    # the whole read set, for the F4 'elsewhere' flag
    all_lat = [(t, {}) for e in entries.values() for col in ("hebrew", "latin") for f in e[col] for t in tokens(f)]
    read_set = Candidates(all_lat, [])

    dres = dresden_grids()
    grids = {g["key"]: g for g in cohort["grids"]}
    cands, stages = {}, {}
    for key in grids:
        cands[key], stages[key] = caption_candidates(noms.get(key, []), hw, entries, by_id)
    chapter_of = {k: g["chapter"] for k, g in grids.items()}
    seeds = {k: (rows[0] if rows else None) for k, rows in dres.items()}
    pilot = pilot_seeds()
    seeds.update(pilot)

    results = {"protocol": "PROTOCOL.md", "seed": SEED, "draws": NPERM, "cohorts": {}}
    for name in ("P", "P-bare", "A", "A-bare"):
        ids = [k for k, g in grids.items() if g["cohort"] == name]
        res, matrix, eligible = run_cohort(name, ids, chapter_of, seeds, cands, stages, read_set)
        res["language_columns"] = language_columns(res["derivations"])
        res["identity"] = identity_split(res["derivations"])
        results["cohorts"][name] = res
        if name == "P":
            results["S2_language_columns"] = res["language_columns"]
            results["S4_spelling"] = spelling([d for d in res["derivations"] if d["tier"]])
            results["D3_identity"] = res["identity"]
            # S1: centre half-word and full centre row
            half_t, full_t = {}, {}
            for g in ids:
                rows = dres.get(g)
                if not rows:
                    continue
                h, f = centre_targets(rows)
                if h:
                    half_t[g] = h
                if f:
                    full_t[g] = f
            s1 = {}
            for label, tg in (("half_word", half_t), ("full_row", full_t)):
                el = sorted(tg)
                m, tests = score_cohort(el, chapter_of, tg, cands)
                hits = [{"grid": g, "targets": tg[g], "tier": LAT_TIERS[m[(g, g)][0]] if m[(g, g)][0] is not None else None,
                         "greek_tier": GRK_TIERS[m[(g, g)][1]] if m[(g, g)][1] is not None else None,
                         "chains": [dict(c, target=t) for t in tg[g] for c in chains(g, t, cands[g], *level_of(cands[g], [t]))]}
                        for g in el if (m[(g, g)][0] is not None and m[(g, g)][0] <= PRIMARY) or m[(g, g)][1] is not None]
                s1[label] = {"eligible": len(el), "tests": tests, "hits": hits}
            results["S1_centre"] = s1

    # S3: Warburg print, experiment 18's nominations unchanged
    wnoms = {(c["chapter"], c["number"]): [dict(n, nominator="exp18") for n in c["nominations"]]
             for c in json.load(open(A / "18-german-captions" / "nominations-de.json", encoding="utf8"))["captions"]}
    wseeds = warburg_seeds()
    wids = sorted(wnoms)
    wc, ws = {}, {}
    for k in wids:
        wc[k], ws[k] = caption_candidates(wnoms[k], hw, entries, by_id)
    wch = {k: k[0] for k in wids}
    s3, _, _ = run_cohort("B", wids, wch, wseeds, wc, ws, read_set)
    s3["language_columns"] = language_columns(s3["derivations"])
    s3_wo5, _, _ = run_cohort("B-without-5", [k for k in wids if k[0] != 5], wch, wseeds, wc, ws, read_set)
    results["S3_warburg"] = s3
    results["S3_warburg_without_chapter_5"] = {k: s3_wo5[k] for k in ("eligible", "tests", "share_skeleton", "verdict")}

    text = json.dumps(results, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        assert (HERE / "results.json").read_text(encoding="utf8") == text, "results differ"
        print("results reproduce")
        return
    (HERE / "results.json").write_text(text, encoding="utf8")
    p = results["cohorts"]["P"]
    t = p["tests"]["within_chapter"]
    print("P eligible", p["eligible"], "| skeleton", t["skeleton"], "| verdict", p["verdict"])
    for tier in LAT_TIERS + GRK_TIERS + ["all_tiers"]:
        print(f"  {tier:14s} within {t[tier]}  across {p['tests']['across_cohort'][tier]}")
    print("failure stages", p["failure_stages"], p["failure_flags"])


if __name__ == "__main__":
    main()
