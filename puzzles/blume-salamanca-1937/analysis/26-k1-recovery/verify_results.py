"""Verify experiment26 records without importing its driver or invoking a solver.

python3 -I /path/to/verify_results.py --output /path/to/results/verification.txt
Requires the frozen corpus/model/candidate caches. Per-run caches are optional;
missing cache checks are reported. Partial JSONL snapshots never pass a gate.
The only reused computation is the pinned literary plaintext generator.
"""
import argparse
import array
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
S25, S24 = HERE.parent / "25-seed-retention", HERE.parent / "24-phrase-seeded"
PLAN_SHA256 = "cbc6a328283d304ffa882528f1873570c75298910507997f60307dc4199aa4dd"
BANDS = {"low": (12, 15), "middle": (16, 18), "high": (19, 22)}
ISO_STRATA = (*BANDS, "wrong-width", "shuffle")
STRATA = ("exact", "one", "two", "random")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stream(number, kind, tag, index):
    return int.from_bytes(hashlib.sha256(f"{number}|{kind}|{tag}|{index}".encode()).digest()[:8], "big")


def key(text):
    ranks = list(map(int, text.split(",")))
    require(sorted(ranks) == list(range(len(ranks))), "invalid recorded permutation")
    return ranks


def distance(a, b):
    require(len(a) == len(b), "distance requires equal key lengths")
    following, unused, cycles = dict(zip(a, b)), set(a), 0
    while unused:
        current = next(iter(unused))
        cycles += 1
        while current in unused:
            unused.remove(current)
            current = following[current]
    return len(a)-cycles


def encrypt(text, ranks):
    return "".join(text[c::len(ranks)] for c in sorted(range(len(ranks)), key=ranks.__getitem__))


def decrypt(text, ranks):
    n, w = len(text), len(ranks)
    columns, offset = {}, 0
    for c in sorted(range(w), key=ranks.__getitem__):
        size = n//w + (c < n % w)
        columns[c] = text[offset:offset+size]
        offset += size
    return "".join(columns[i % w][i//w] for i in range(n))


def snapshot(path):
    if not path.exists():
        return [], False, None
    data = path.read_bytes()
    rows, intact = [], data.endswith(b"\n")
    lines = data.splitlines()
    for i, line in enumerate(lines):
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            require(i == len(lines)-1 and not intact, f"malformed JSONL in {path}")
            intact = False
    return rows, intact, hashlib.sha256(data).hexdigest()


def check_development_sources(development, current, report):
    require({k: v for k, v in development.items() if k not in ("source_sha256", "driver_sha256")} ==
            {k: v for k, v in current.items() if k not in ("source_sha256", "driver_sha256")},
            "development/frozen binary, parameters or input pins differ")
    base = "puzzles/blume-salamanca-1937/analysis/26-k1-recovery/"
    try:
        c = subprocess.check_output(["git", "show", "e27f692:"+base+"seedsolve.c"], cwd=HERE.parents[3], stderr=subprocess.DEVNULL)
        driver = subprocess.check_output(["git", "show", "e27f692:"+base+"run.py"], cwd=HERE.parents[3], stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError):
        report.append("SKIP: development git sources unavailable; binary/input equality and independent result checks remain.")
        return
    require(hashlib.sha256(c).hexdigest() == development["source_sha256"] and
            hashlib.sha256(driver).hexdigest() == development["driver_sha256"], "development source pins mismatch")
    strip_comments = lambda text: re.sub(r"/\*.*?\*/|//[^\n]*", "", text, flags=re.S)
    require(strip_comments(c.decode()) == strip_comments((HERE / "seedsolve.c").read_text()),
            "C changed beyond comments since development")
    before, after = ast.parse(driver.decode()), ast.parse((HERE / "run.py").read_text())
    def excluded(node):
        return (isinstance(node, ast.FunctionDef) and node.name in ("check_plan", "target")) or isinstance(node, ast.If)
    require(ast.dump(ast.Module(body=[n for n in before.body if not excluded(n)], type_ignores=[])) ==
            ast.dump(ast.Module(body=[n for n in after.body if not excluded(n)], type_ignores=[])),
            "driver algorithm changed since development")
    old_target = next(n for n in before.body if isinstance(n, ast.FunctionDef) and n.name == "target")
    new_target = next(n for n in after.body if isinstance(n, ast.FunctionDef) and n.name == "target")
    guard = ast.parse('assert protocol["target_tag"]==tag').body[0]
    new_target.body = [n for n in new_target.body if ast.dump(n) != ast.dump(guard)]
    require(ast.dump(new_target) == ast.dump(old_target), "target algorithm changed beyond tag guard")
    report.append("PASS: development/frozen binary and search inputs identical; git-pinned C differs only in comments; "
                  "driver algorithms unchanged apart from stage/tag guards.")


def verify():
    report = ["Independent verification of experiment26 recorded results.",
              "No solver, build or search is invoked; experiment26's driver is not imported."]
    plan_path, build_path = HERE / "control-plan.json", HERE / "build-manifest.json"
    require(sha(plan_path) == PLAN_SHA256, "frozen control-plan SHA mismatch")
    plan, build = load(plan_path), load(build_path)
    require(plan["build"] == build and plan["n"] == 615 and plan["trials_per_stratum"] == 10, "plan/build mismatch")
    require(plan["isolated_strata"] == list(ISO_STRATA) and plan["pipeline_strata"] == list(STRATA) and
            plan["positive_bands"] == {k: list(v) for k, v in BANDS.items()}, "stratum plan mismatch")
    paths = {"source": HERE / "seedsolve.c", "driver": HERE / "run.py", "binary": HERE / "out/seedsolve",
             "parent_manifest": S25 / "build-manifest.json", "expanded": S25 / "out/expanded.bin",
             "engine": HERE.parent / "21-dc-method/dcm.c"}
    for field, path in paths.items():
        require(sha(path) == build[field+"_sha256"], f"frozen26 {field} hash mismatch")
    old25 = load(paths["parent_manifest"])
    paths25 = {"source": S25 / "seedsolve.c", "driver": S25 / "run.py", "expand_source": S25 / "expand.py",
               "binary": S25 / "out/seedsolve", "expanded": paths["expanded"],
               "previous_manifest": S24 / "build-manifest.json"}
    for field, path in paths25.items():
        require(sha(path) == old25[field+"_sha256"], f"inherited25 {field} hash mismatch")
    old24 = load(paths25["previous_manifest"])
    paths24 = {"binary": S24 / "out/seedsolve", "wrapper": S24 / "seedsolve.c", "driver": S24 / "run.py",
               "engine": paths["engine"], "keys": S24 / "out/keys.tsv", "keys_json": S24 / "out/keys.json",
               "model2": HERE.parent / "21-dc-method/out/lm_es_2.bin",
               "model4": HERE.parent / "21-dc-method/out/lm_es_4.bin"}
    for field, path in paths24.items():
        require(sha(path) == old24[field+"_sha256"], f"inherited24 {field} hash mismatch")
    for relative, expected in old24["plant_inputs"].items():
        require(sha(HERE.parent / relative) == expected, f"plant input hash mismatch: {relative}")
    require(build["params"] == old25["params"] and build["cpu_caps_seconds"] == plan["cpu_caps_seconds"] ==
            {"scan": 180, "refinement_process": 60}, "search/cap parameters changed")
    report.append(f"PASS: frozen plan/build/parent/source/binary/candidate/model/corpus pins; plan SHA256 {PLAN_SHA256}.")
    development_manifest_path = HERE / "development-build-manifest.json"
    development_manifest = load(development_manifest_path)
    check_development_sources(development_manifest, build, report)
    sys.path[:0] = [str(HERE.parent / "21-dc-method"), str(HERE.parent / "01-solver")]
    import run21
    run21.load_words("es")
    records = load(paths24["keys_json"])
    by_width = {w: [r for r in records if len(r["key"]) == w] for w in range(18, 29)}
    q = array.array("f")
    q.frombytes(paths24["model4"].read_bytes())
    require(len(q) == 26**4, "quadgram model size mismatch")
    params, build_id = build["params"], sha(build_path)

    def quad_score(plaintext):
        t = [ord(c)-65 for c in plaintext]
        return sum(q[((a*26+b)*26+c)*26+d] for a, b, c, d in zip(t, t[1:], t[2:], t[3:]))/(len(t)-3)

    def reading(ciphertext, result):
        a, b = key(result["k1"]), key(result["k2"])
        require(result["conv"] == "CC" and (len(a), len(b)) == (result["w1"], result["w2"]), "reading geometry mismatch")
        got = decrypt(decrypt(ciphertext, b), a)
        require(got == result["pt"] and abs(quad_score(got)-result["score"]) < .0001,
                "independent decryption/quadgram score mismatch")
        return got

    def check_row(row, ciphertext, supplied_k2=None, expected_build=build_id):
        require(row["params"] == params and row["build_id"] == expected_build and row["n"] == len(ciphertext) == 615,
                "result provenance/length mismatch")
        require(row["best"]["w1"] == row["first_width_hypothesis"] and
                12 <= row["first_width_hypothesis"] <= 22 and 18 <= row["best"]["w2"] <= 28, "result width mismatch")
        require(row["candidate"] == (row["best"]["score"] > params["threshold"]), "candidate classification mismatch")
        got = reading(ciphertext, row["best"])
        work = HERE / "out" / row["tag"]
        if (work / "ct.txt").exists():
            require((work / "ct.txt").read_text() == ciphertext, "ciphertext cache mismatch")
        else:
            report.append(f"SKIP: {row['tag']} ciphertext cache absent; ciphertext reconstructed independently.")
        if supplied_k2 is not None:
            require(row["best"]["tag"] == "locked" and key(row["best"]["k2"]) == supplied_k2, "locked K2 changed")
            require(row["cpu"] == row["best"]["cpu"], "locked CPU mismatch")
        else:
            require(row["scan"]["keys"] == 1286188 and row["scan"]["n_idp"] == 1286188+11*params["samples"],
                    "incomplete expanded scan")
            require(row["seeds_tried"] == params["keep"] == 4, "pipeline did not complete all four seeds")
            if (work / "readings.json").exists():
                readings = load(work / "readings.json")
                require(len(readings) == 4, "reading cache incomplete")
                for item in readings:
                    reading(ciphertext, item)
                    require(item["w1"] == row["first_width_hypothesis"], "refinement width mismatch")
                require(row["best"] == max(readings, key=lambda x: x["score"]), "best selection mismatch")
                require(abs(row["cpu"]-round(row["scan"]["cpu"]+sum(x["cpu"] for x in readings), 3)) < .0001,
                        "pipeline CPU total mismatch")
            else:
                report.append(f"SKIP: {row['tag']} reading cache absent; all-four work verified only from recorded count.")
        return got

    def metrics(row, got, plaintext):
        require(hashlib.sha256(plaintext.encode()).hexdigest() == row["plaintext_sha256"], "plaintext SHA mismatch")
        alignments = [(sum(got[j] == plaintext[(j+s) % 615] for j in range(615))/615, s) for s in range(-40, 41)]
        accuracy, shift = max(alignments, key=lambda item: item[0])
        inplace = sum(a == b for a, b in zip(got, plaintext))/615
        require(round(accuracy, 4) == row["acc"] and round(inplace, 4) == row["acc_inplace"] and
                (got == plaintext) == row["exact"] and (accuracy >= .95) == row["recovered"], "recovery metrics mismatch")
        if row["recovered"] and not row["exact"]:
            report.append(f"SHIFT CASE: {row['tag']}; shift {shift}; accuracy {accuracy:.4f}; in-place {inplace:.4f}.")

    def pipeline_plant(number, tag, stratum, index):
        rng = random.Random(stream(number, "plant", tag, f"{stratum}:{index}"))
        w2 = rng.randint(18, 28)
        choices = by_width[w2]
        for _ in range(10000):
            if stratum == "random":
                k2, base = rng.sample(range(w2), w2), None
            else:
                d = {"exact": 0, "one": 1, "two": 2}[stratum]
                base = rng.choice(choices)
                k2 = list(base["key"])
                pos = rng.sample(range(w2), 2*d)
                for a, b in zip(pos[::2], pos[1::2]):
                    k2[a], k2[b] = k2[b], k2[a]
            md = min(distance(r["key"], k2) for r in choices)
            if (stratum == "random" and md > 3) or (stratum != "random" and md == d):
                break
        else:
            raise ValueError("rejection sampling exhausted")
        w1 = rng.randint(12, 22)
        plaintext = run21.plaintext.telegram(615, rng, "es", "telegraph")
        return plaintext, rng.sample(range(w1), w1), k2, md, None if base is None else base["id"]

    development = load(HERE / "results/development.json")
    pt, k1, k2, _, _ = pipeline_plant(25, "holdout25", "two", 8)
    old_rows = [json.loads(s) for s in (S25 / "results/holdout25.jsonl").read_text().splitlines()]
    old_failure = next(r for r in old_rows if r["stratum"] == "two" and r["trial"] == 8)
    require(old_failure["plaintext_sha256"] == hashlib.sha256(pt.encode()).hexdigest(), "old plant pin mismatch")
    got = check_row(development, encrypt(encrypt(pt, k1), k2), k2, sha(development_manifest_path))
    metrics(development, got, pt)
    require(got == pt and development["first_width_hypothesis"] == len(k1), "assisted development did not exactly fix old plant")
    report.append(f"PASS: assisted DEVELOPMENT old25 two/trial8 exactly recovered with K2 locked; "
                  f"score {development['best']['score']:.4f}; CPU seconds {development['cpu']:.3f}; excluded from fresh gates.")

    isolated_path = HERE / "results" / (plan["isolated_tag"]+".jsonl")
    isolated, iso_intact, iso_sha = snapshot(isolated_path)
    def check_trials(rows, strata):
        actual = [(r["stratum"], r["trial"]) for r in rows]
        expected = {(s, i) for s in strata for i in range(10)}
        require(len(actual) == len(set(actual)) and set(actual) <= expected, "duplicate/unexpected trial")
        return set(actual) == expected
    iso_complete = check_trials(isolated, ISO_STRATA) and iso_intact
    for row in isolated:
        s, i = row["stratum"], row["trial"]
        require(row["tag"] == f"{plan['isolated_tag']}_{s}_{i}", "isolated tag mismatch")
        rng = random.Random(stream(26, "isolated-plant", plan["isolated_tag"], f"{s}:{i}"))
        lo, hi = BANDS.get(s, (12, 22))
        w1, w2 = rng.randint(lo, hi), rng.randint(18, 28)
        pt = run21.plaintext.telegram(615, rng, "es", "telegraph")
        k1, k2 = rng.sample(range(w1), w1), rng.sample(range(w2), w2)
        ct = encrypt(encrypt(pt, k1), k2)
        stated = rng.choice([w for w in range(12, 23) if w != w1]) if s == "wrong-width" else w1
        if s == "shuffle":
            letters = list(ct)
            rng.shuffle(letters)
            noise = "".join(letters)
            require(Counter(noise) == Counter(ct), "isolated shuffle count mismatch")
            ct = noise
        require((row["plant_w1"], row["plant_w2"], row["first_width_hypothesis"], row["positive"]) ==
                (w1, w2, stated, s in BANDS), "isolated geometry/positive-band classification mismatch")
        metrics(row, check_row(row, ct, k2), pt)
    iso_false = [r for r in isolated if r["candidate"] and (not r["recovered"] or not r["positive"])]
    iso_gate = iso_complete and not iso_false and all(sum(r["recovered"] for r in isolated if r["stratum"] == s) >= 8 for s in BANDS)
    for s in ISO_STRATA:
        rows = [r for r in isolated if r["stratum"] == s]
        report.append(f"VERIFIED ISOLATED {s}: {len(rows)}/10; {sum(r['recovered'] for r in rows)} recovered; "
                      f"{sum(r['exact'] for r in rows)} exact; {sum(r['candidate'] for r in rows)} candidates; "
                      f"CPU seconds {sum(r['cpu'] for r in rows):.3f}.")
    report.append(f"{'PASS' if iso_gate else 'FAIL' if iso_complete else 'INCOMPLETE'}: isolated gate; "
                  f"{len(isolated)}/50 unique controls, {len(iso_false)} false candidates; CPU seconds "
                  f"{sum(r['cpu'] for r in isolated):.3f}; snapshot SHA256 {iso_sha}.")

    control_path = HERE / "results" / (plan["control_tag"]+".jsonl")
    controls, intact, control_sha = snapshot(control_path)
    complete = check_trials(controls, STRATA) and intact
    if controls:
        require(iso_gate, "pipeline controls exist without passing isolated gate")
    checked_shortlists = 0
    for row in controls:
        s, i = row["stratum"], row["trial"]
        require(row["tag"] == f"{plan['control_tag']}_{s}_{i}", "pipeline control tag mismatch")
        pt, k1, k2, md, base = pipeline_plant(26, plan["control_tag"], s, i)
        require((row["plant_w1"], row["plant_w2"], row["first_width_hypothesis"], row["base_id"],
                 row["min_list_swap_distance"], row["min_expanded_swap_distance"]) ==
                (len(k1), len(k2), len(k1), base, md, max(0, md-1)), "pipeline plant/distance metadata mismatch")
        metrics(row, check_row(row, encrypt(encrypt(pt, k1), k2)), pt)
        cache = HERE / "out" / row["tag"] / "shortlist.json"
        if cache.exists():
            seeds = load(cache)
            require(len(seeds) == 4, "shortlist count mismatch")
            retained = [key(x["k2"]) for x in seeds]
            nearest = min((distance(k, k2) for k in retained if len(k) == len(k2)), default=None)
            require(row["true_key_shortlisted"] == (k2 in retained) and row["min_retained_swap_distance"] == nearest,
                    "post-search shortlist diagnostics mismatch")
            readings_path = cache.parent / "readings.json"
            if readings_path.exists():
                require([r["seed_k2"] for r in load(readings_path)] == [r["k2"] for r in seeds],
                        "not all four retained seeds processed in order")
            checked_shortlists += 1
        else:
            report.append(f"SKIP: {row['tag']} shortlist cache absent; retention diagnostics not rechecked.")
    false = [r for r in controls if r["candidate"] and not r["recovered"]]
    control_gate = complete and not false and all(sum(r["recovered"] for r in controls if r["stratum"] == s) >= 8 for s in ("exact", "one"))
    for s in STRATA:
        rows = [r for r in controls if r["stratum"] == s]
        report.append(f"VERIFIED PIPELINE {s}: {len(rows)}/10; {sum(r['recovered'] for r in rows)} recovered; "
                      f"{sum(r['exact'] for r in rows)} exact; CPU seconds {sum(r['cpu'] for r in rows):.3f}.")
    status = "PASS" if control_gate else "FAIL" if complete else "NOT RUN" if iso_complete and not iso_gate and not controls else "INCOMPLETE"
    report.append(f"{status}: pipeline gate; {len(controls)}/40 unique controls, {len(false)} false candidates; "
                  f"{checked_shortlists} shortlist diagnostics checked; CPU seconds {sum(r['cpu'] for r in controls):.3f}; "
                  f"snapshot SHA256 {control_sha}.")
    for r in (*iso_false, *false):
        report.append(f"FALSE CANDIDATE: {r['tag']}; score {r['best']['score']:.4f}; accuracy {r['acc']:.4f}; "
                      f"in-place {r['acc_inplace']:.4f}.")

    target_path = HERE / "results" / (plan["target_tag"]+".jsonl")
    targets, target_intact, target_sha = snapshot(target_path)
    cells = [(r["body"], r["first_width_hypothesis"]) for r in targets]
    expected = {(body, w) for body in ("T1", "T1-shuffle") for w in range(12, 23)}
    require(len(cells) == len(set(cells)) and set(cells) <= expected, "duplicate/unexpected target cell")
    if targets:
        require(iso_gate and control_gate, "target exists without both passing gates")
        protocol = load(HERE / "protocol.json")
        require(protocol["build"] == build and protocol["target_tag"] == plan["target_tag"], "target protocol mismatch")
        for field, tag, digest in (("isolated", plan["isolated_tag"], iso_sha), ("controls", plan["control_tag"], control_sha)):
            require(protocol[field] == {"tag": tag, "sha256": digest}, f"target {field} pin mismatch")
        source = (HERE.parent.parent / "sources/telegram-1.txt").read_text().upper()
        ct = "".join(c for c in source if "A" <= c <= "Z")
        require(len(ct) == 615 and hashlib.sha256(ct.encode()).hexdigest().startswith("e266615d"), "T1 source mismatch")
        letters = list(ct)
        random.Random(stream(26, "shuffle", plan["target_tag"], 0)).shuffle(letters)
        texts = {"T1": ct, "T1-shuffle": "".join(letters)}
        for row in targets:
            require(row["tag"] == f"{plan['target_tag']}_{row['body']}_{row['first_width_hypothesis']}", "target tag mismatch")
            check_row(row, texts[row["body"]])
        report.append(f"PASS: {len(targets)} available target rows independently decrypted/rescored, all-four work and protocol pins checked.")
    if target_intact and set(cells) == expected:
        report.append("PASS: all22 target cells present, unique and verified; no global early stop.")
    elif not targets and ((iso_complete and not iso_gate) or (complete and not control_gate)):
        report.append("NOT RUN: target withheld because a complete prerequisite gate failed.")
    else:
        report.append(f"INCOMPLETE: target {len(targets)}/22 width/body cells; full target verification unavailable.")
    if not (HERE / "protocol.json").exists() and not list((HERE / "results").glob("target*.jsonl")):
        report.append("NO TARGET ARTIFACTS: protocol.json absent; no results/target*.jsonl files present.")
    report.append(f"Target snapshot SHA256: {target_sha}.")
    report.append("Scope: assisted locked-K2 isolated calibration; conditional per-first-width pipeline calibration; "
                  "615-letter literary proxy. Scores are provisional candidates, not decipherment certificates. "
                  "One shuffle is not a p-value estimate.")
    return "\n".join(report)+"\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.write_text(result)
    print(result, end="")
