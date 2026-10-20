"""Independently verify experiment25 records without invoking any solver/search.

python3 -I /path/to/verify_results.py --output /path/to/results/verification.txt
The frozen corpus/models/binary candidate cache are required. Missing per-run
shortlists/readings are reported as skipped cache checks. Incomplete JSONL files
produce an INCOMPLETE report and can never produce a passing control gate.
Only the pre-existing literary plant generator is imported. Plant selection,
rejection sampling, permutation distance, transformations and scores are checked
here without importing experiment25's driver or search implementation.
"""
import argparse
import array
import ast
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
S24 = HERE.parent / "24-phrase-seeded"
STRATA = ("exact", "one", "two", "random")
ORIGINAL_PLAN_SHA256 = "41f6d57e5870a9cca543b925ab3ca9f729482ac60a26626962cd99bdc3bac8de"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def stream(kind, tag, index):
    return int.from_bytes(hashlib.sha256(f"25|{kind}|{tag}|{index}".encode()).digest()[:8], "big")


def key(value):
    result = list(map(int, value.split(",")))
    require(sorted(result) == list(range(len(result))), "invalid recorded permutation")
    return result


def distance(a, b):
    require(len(a) == len(b), "swap distance requires equal key lengths")
    following = dict(zip(a, b))
    unused, cycles = set(a), 0
    while unused:
        current = next(iter(unused))
        cycles += 1
        while current in unused:
            unused.remove(current)
            current = following[current]
    return len(a) - cycles


def encrypt(text, ranks):
    return "".join(text[c::len(ranks)] for c in sorted(range(len(ranks)), key=ranks.__getitem__))


def decrypt(text, ranks):
    n, w = len(text), len(ranks)
    columns, offset = {}, 0
    for c in sorted(range(w), key=ranks.__getitem__):
        length = n // w + (c < n % w)
        columns[c] = text[offset:offset + length]
        offset += length
    return "".join(columns[i % w][i // w] for i in range(n))


def snapshot(path):
    """Accept an append-in-progress final line, but never call it complete."""
    if not path.exists():
        return [], False, None
    data = path.read_bytes()
    lines = data.splitlines()
    rows, intact = [], data.endswith(b"\n")
    for i, line in enumerate(lines):
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            require(i == len(lines)-1 and not intact, f"malformed JSONL record in {path}")
            intact = False
    return rows, intact, hashlib.sha256(data).hexdigest()


def check_diagnostic_fix(build, plan, report):
    """Prove the archived/new drivers differ only in the post-search diagnostic."""
    old_source = HERE / "run-before-diagnostic-fix.py"
    if not old_source.exists():
        report.append("SKIP: archived pre-diagnostic-fix driver absent; no archive equivalence check.")
        return
    old_build_path = HERE / "build-manifest-before-diagnostic-fix.json"
    old_build = load(old_build_path)
    old_plan_path = HERE / "control-plan-before-diagnostic-fix.json"
    old_plan = load(old_plan_path)
    require(sha(old_plan_path) == ORIGINAL_PLAN_SHA256, "original frozen control-plan pin mismatch")
    require(old_plan["build"] == old_build and sha(old_source) == old_build["driver_sha256"],
            "archived build/plan/driver mismatch")
    require({k: v for k, v in old_build.items() if k not in ("driver_sha256", "binary_sha256")} ==
            {k: v for k, v in build.items() if k not in ("driver_sha256", "binary_sha256")},
            "search parameters, C source or inputs changed across diagnostic fix")
    require({k: v for k, v in old_plan.items() if k != "build"} ==
            {k: v for k, v in plan.items() if k != "build"}, "control plan changed beyond build pin")
    before, after = ast.parse(old_source.read_text()), ast.parse((HERE / "run.py").read_text())
    is_control = lambda node: isinstance(node, ast.FunctionDef) and node.name == "control_one"
    require(ast.dump(ast.Module(body=[node for node in before.body if not is_control(node)], type_ignores=[])) ==
            ast.dump(ast.Module(body=[node for node in after.body if not is_control(node)], type_ignores=[])),
            "driver changed outside control_one; search/import/plant/target equality failed")
    old_control = next(node for node in before.body if is_control(node))
    new_control = next(node for node in after.body if is_control(node))
    def core(function):
        function = copy.deepcopy(function)
        function.body = [node for node in function.body if not
                         (isinstance(node, ast.Assign) and len(node.targets) == 1 and
                          isinstance(node.targets[0], ast.Name) and node.targets[0].id == "same_length")]
        for node in ast.walk(function):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "update":
                node.keywords = [kw for kw in node.keywords if kw.arg != "min_retained_swap_distance"]
        return ast.dump(function)
    require(core(old_control) == core(new_control), "control logic changed beyond nearest-retained diagnostic")
    expected_assignment = ast.parse('same_length=[previous.parse_key(x["k2"]) for x in ss if x["w2"]==len(k2)]').body[0]
    assignments = [node for node in new_control.body if isinstance(node, ast.Assign) and
                   any(isinstance(target, ast.Name) and target.id == "same_length" for target in node.targets)]
    require(len(assignments) == 1 and ast.dump(assignments[0]) == ast.dump(expected_assignment),
            "unexpected same-length diagnostic assignment")
    expected_distance = ast.parse('min((swap_distance(k,k2) for k in same_length),default=None)', mode="eval").body
    values = [kw.value for node in ast.walk(new_control) if isinstance(node, ast.Call)
              for kw in node.keywords if kw.arg == "min_retained_swap_distance"]
    require(len(values) == 1 and ast.dump(values[0]) == ast.dump(expected_distance), "unexpected diagnostic fix expression")
    report.append("PASS: archived/new ASTs differ only in post-search nearest-retained diagnostic; "
                  "PARAMS, seed logic, make_plant, pipeline, target, C source, list and inputs unchanged.")
    archive = HERE / "results/holdout25-before-diagnostic-fix.jsonl"
    rows, _, archive_sha = snapshot(archive)
    if archive.exists():
        require(all(row["build_id"] == sha(old_build_path) and row["params"] == old_build["params"] for row in rows),
                "mixed provenance in archived aborted batch")
        report.append(f"ARCHIVED: aborted pre-fix batch {len(rows)} records; SHA256 {archive_sha}; "
                      "excluded from the fresh control gate.")
    else:
        report.append("INCOMPLETE: aborted batch archive not yet available.")


def verify(target_tag):
    report = ["Independent verification of experiment25 recorded results.",
              "No build, solver or search process is invoked."]
    build_path = HERE / "build-manifest.json"
    build, plan = load(build_path), load(HERE / "control-plan.json")
    require(plan["build"] == build, "control plan/build mismatch")
    require(plan["tag"] == "holdout25" and plan["n"] == 615 and plan["trials_per_stratum"] == 10,
            "unexpected control plan")
    require(plan["strata"] == list(STRATA) and plan["required_strata"] == ["exact", "one"],
            "unexpected stratum/gate plan")
    require(plan["cpu_caps_seconds"] == {"scan": 180, "refinement_process": 60}, "CPU-cap plan mismatch")
    paths = {"source": HERE / "seedsolve.c", "driver": HERE / "run.py", "expand_source": HERE / "expand.py",
             "binary": HERE / "out/seedsolve", "expanded": HERE / "out/expanded.bin",
             "previous_manifest": S24 / "build-manifest.json"}
    for name, path in paths.items():
        require(sha(path) == build[name+"_sha256"], f"frozen {name} hash mismatch")
    require(load(HERE / "expanded-manifest.json") == build["expanded_manifest"], "expansion manifest mismatch")
    old = load(paths["previous_manifest"])
    old_paths = {"binary": S24 / "out/seedsolve", "wrapper": S24 / "seedsolve.c", "driver": S24 / "run.py",
                 "engine": HERE.parent / "21-dc-method/dcm.c", "keys": S24 / "out/keys.tsv",
                 "keys_json": S24 / "out/keys.json", "model2": HERE.parent / "21-dc-method/out/lm_es_2.bin",
                 "model4": HERE.parent / "21-dc-method/out/lm_es_4.bin"}
    for name, path in old_paths.items():
        require(sha(path) == old[name+"_sha256"], f"inherited {name} hash mismatch")
    for relative, expected in old["plant_inputs"].items():
        require(sha(HERE.parent / relative) == expected, f"inherited plant input hash mismatch: {relative}")
    report.append(f"PASS: frozen build/inherited input hashes and control-plan build pin; "
                  f"control-plan SHA256 {sha(HERE / 'control-plan.json')}.")
    check_diagnostic_fix(build, plan, report)
    sys.path[:0] = [str(HERE.parent / "21-dc-method"), str(HERE.parent / "01-solver")]
    import run21
    run21.load_words("es")
    records = load(old_paths["keys_json"])
    by_width = {w: [row for row in records if len(row["key"]) == w] for w in range(18, 29)}
    q = array.array("f")
    q.frombytes(old_paths["model4"].read_bytes())
    require(len(q) == 26**4, "quadgram model size mismatch")
    params, build_id = build["params"], sha(build_path)
    expanded_count = build["expanded_manifest"]["keys"]
    require(expanded_count == 1286188, "unexpected expansion count")

    def quad_score(plaintext):
        values = [ord(c)-65 for c in plaintext]
        return sum(q[((a*26+b)*26+c)*26+d]
                   for a, b, c, d in zip(values, values[1:], values[2:], values[3:])) / (len(values)-3)

    def score_reading(ciphertext, result):
        a, b = key(result["k1"]), key(result["k2"])
        require(result["conv"] == "CC" and (len(a), len(b)) == (result["w1"], result["w2"]),
                "reading key geometry mismatch")
        plaintext = decrypt(decrypt(ciphertext, b), a)
        require(plaintext == result["pt"], "independent decryption mismatch")
        score = quad_score(plaintext)
        require(abs(score-result["score"]) < 0.0001, "independent quadgram score mismatch")
        return plaintext

    def check_row(row, ciphertext, expected_build_id=None):
        require(row["build_id"] == (expected_build_id or build_id) and row["params"] == params,
                "row provenance mismatch")
        require(row["n"] == len(ciphertext) == 615, "row text length mismatch")
        width = row["first_width_hypothesis"]
        require(12 <= width <= 22 and row["best"]["w1"] == width, "first-width mismatch")
        require(18 <= row["best"]["w2"] <= 28, "second-width outside calibration range")
        require(row["scan"]["keys"] == expanded_count and
                row["scan"]["n_idp"] == expanded_count + 11*params["samples"], "incomplete scan work")
        require(row["candidate"] == (row["best"]["score"] > params["threshold"]), "candidate classification mismatch")
        got = score_reading(ciphertext, row["best"])
        work = HERE / "out" / row["tag"]
        if (work / "ct.txt").exists():
            require((work / "ct.txt").read_text() == ciphertext, "ciphertext cache mismatch")
        else:
            report.append(f"SKIP: ciphertext cache absent for {row['tag']}; ciphertext reconstructed.")
        if (work / "readings.json").exists():
            readings = load(work / "readings.json")
            require(len(readings) == row["seeds_tried"] and 1 <= len(readings) <= params["keep"],
                    "refinement count mismatch")
            for reading in readings:
                score_reading(ciphertext, reading)
                require(reading["w1"] == width, "refinement first-width mismatch")
            require(row["best"] == max(readings, key=lambda result: result["score"]), "best reading mismatch")
            require(all(reading["score"] <= params["threshold"] for reading in readings[:-1]),
                    "refinement continued after score-only stop")
            require(len(readings) == params["keep"] or readings[-1]["score"] > params["threshold"],
                    "premature refinement stop")
            require(abs(row["cpu"]-round(row["scan"]["cpu"]+sum(x["cpu"] for x in readings), 3)) < 0.0001,
                    "recorded CPU total mismatch")
        else:
            report.append(f"SKIP: reading cache absent for {row['tag']}; best reading independently verified.")
        return got

    benchmark_path = HERE / "results/benchmark.json"
    benchmark_manifest_path = HERE / "benchmark-build-manifest.json"
    if benchmark_path.exists() and benchmark_manifest_path.exists():
        benchmark_build = load(benchmark_manifest_path)
        for field in ("params", "source_sha256", "expand_source_sha256", "expanded_sha256",
                      "expanded_manifest", "previous_manifest_sha256"):
            require(benchmark_build[field] == build[field], f"benchmark/search input mismatch: {field}")
        old_protocol = load(S24 / "protocol.json")
        old_controls_path = S24 / "results" / old_protocol["control_file"]
        require(sha(old_controls_path) == old_protocol["control_sha256"], "old control-file pin mismatch")
        old_controls = [json.loads(line) for line in old_controls_path.read_text().splitlines()]
        old_failed = [row for row in old_controls if row["distance"] == 1 and row["trial"] == 9]
        require(len(old_failed) == 1, "old benchmark plant record missing/duplicated")
        rng = random.Random(int.from_bytes(hashlib.sha256(b"24|plant|holdout24|1:9").digest()[:8], "big"))
        w2 = rng.randint(18, 28)
        base = rng.choice(by_width[w2])
        w1 = rng.randint(12, 22)
        plaintext = run21.plaintext.telegram(615, rng, "es", "telegraph")
        k1, k2 = rng.sample(range(w1), w1), list(base["key"])
        a, b = rng.sample(range(w2), 2)
        k2[a], k2[b] = k2[b], k2[a]
        require(w1 == 22 and hashlib.sha256(plaintext.encode()).hexdigest() == old_failed[0]["plaintext_sha256"],
                "old benchmark plaintext reconstruction mismatch")
        ciphertext = encrypt(encrypt(plaintext, k1), k2)
        benchmark_ct = HERE / "out/old_d1_9.txt"
        if benchmark_ct.exists():
            require(benchmark_ct.read_text() == ciphertext, "old benchmark ciphertext cache mismatch")
        benchmark_rows = load(benchmark_path)
        require(sorted(row["first_width_hypothesis"] for row in benchmark_rows) == [19, 22],
                "benchmark width records missing/duplicated")
        for row in benchmark_rows:
            width = row["first_width_hypothesis"]
            require(row["tag"] == f"benchmark25_w{width}", "benchmark tag mismatch")
            got = check_row(row, ciphertext, sha(benchmark_manifest_path))
            if width == 22:
                require(got == plaintext, "benchmark at true first width did not exactly recover old plant")
            report.append(f"PASS: DEVELOPMENT benchmark width{width}: independent decryption/score "
                          f"{row['best']['score']:.4f}; exact old-plant recovery {got == plaintext}; "
                          f"CPU seconds {row['cpu']:.3f}; excluded from fresh gate.")
    else:
        report.append("INCOMPLETE: development benchmark records/build manifest unavailable; "
                      "benchmark verification deferred, never counted toward fresh gate.")

    controls_path = HERE / "results" / f"{plan['tag']}.jsonl"
    controls, intact, control_sha = snapshot(controls_path)
    expected_trials = {(s, i) for s in STRATA for i in range(10)}
    actual_trials = [(row["stratum"], row["trial"]) for row in controls]
    require(len(actual_trials) == len(set(actual_trials)) and set(actual_trials) <= expected_trials,
            "duplicate or unexpected control trial")
    diagnostics_checked = 0
    false_details = []
    expected_gate_diagnostics = []
    for row in controls:
        s, i = row["stratum"], row["trial"]
        require(row["tag"] == f"{plan['tag']}_{s}_{i}", "control tag mismatch")
        rng = random.Random(stream("plant", plan["tag"], f"{s}:{i}"))
        w2 = rng.randint(18, 28)
        candidates = by_width[w2]
        for _ in range(10000):
            if s == "random":
                k2, base = rng.sample(range(w2), w2), None
            else:
                d = {"exact": 0, "one": 1, "two": 2}[s]
                base = rng.choice(candidates)
                k2 = list(base["key"])
                positions = rng.sample(range(w2), 2*d)
                for a, b in zip(positions[::2], positions[1::2]):
                    k2[a], k2[b] = k2[b], k2[a]
            md = min(distance(x["key"], k2) for x in candidates)
            if (s == "random" and md > 3) or (s != "random" and md == d):
                break
        else:
            raise ValueError("independent rejection sampling exhausted")
        w1 = rng.randint(12, 22)
        plaintext = run21.plaintext.telegram(615, rng, "es", "telegraph")
        k1 = rng.sample(range(w1), w1)
        require((w1, w2, None if base is None else base["id"]) ==
                (row["plant_w1"], row["plant_w2"], row["base_id"]), "plant selection mismatch")
        require(row["first_width_hypothesis"] == w1, "control does not use stated true first width")
        require(row["min_list_swap_distance"] == md and row["min_expanded_swap_distance"] == max(0, md-1),
                "minimum-distance classification mismatch")
        require(hashlib.sha256(plaintext.encode()).hexdigest() == row["plaintext_sha256"], "plaintext SHA mismatch")
        got = check_row(row, encrypt(encrypt(plaintext, k1), k2))
        shifted = max(sum(got[j] == plaintext[(j+shift) % 615] for j in range(615))/615
                      for shift in range(-40, 41))
        inplace = sum(a == b for a, b in zip(got, plaintext))/615
        require(round(shifted, 4) == row["acc"] and round(inplace, 4) == row["acc_inplace"], "accuracy mismatch")
        require((got == plaintext) == row["exact"] and (shifted >= .95) == row["recovered"], "recovery mismatch")
        if row["candidate"] and not row["recovered"]:
            alignment = max(range(-40, 41), key=lambda shift:
                            sum(got[j] == plaintext[(j+shift) % 615] for j in range(615)))
            true_quads = {plaintext[j:j+4] for j in range(612)}
            matching_quads = sum(got[j:j+4] in true_quads for j in range(612))
            final_k2 = key(row["best"]["k2"])
            final_distance = distance(final_k2, k2) if len(final_k2) == len(k2) else None
            false_details.append(
                f"FALSE CANDIDATE: {row['tag']}; score {row['best']['score']:.4f} > threshold "
                f"{params['threshold']:.2f}; shifted accuracy {row['acc']:.4f}, in-place accuracy "
                f"{row['acc_inplace']:.4f}; best reference cyclic shift {alignment}; "
                f"true plaintext quadgram score {quad_score(plaintext):.4f}; final K2 swap distance "
                f"from true key {final_distance}; {matching_quads}/612 output quadgrams occur in true plaintext."
            )
            expected_gate_diagnostics.append(dict(
                stratum=s, trial=i, widths=[len(k1), len(k2)], score=row["best"]["score"],
                true_plaintext_score=round(quad_score(plaintext), 6), candidate=row["candidate"],
                recovered=row["recovered"], acc=row["acc"], acc_inplace=row["acc_inplace"],
                seeds_tried=row["seeds_tried"], second_key_exact=final_k2 == k2,
                first_key_exact=key(row["best"]["k1"]) == k1,
                true_plaintext=plaintext, returned_plaintext=got))
        shortlist = HERE / "out" / row["tag"] / "shortlist.json"
        if shortlist.exists():
            seeds = load(shortlist)
            require(len(seeds) == params["keep"], "shortlist length mismatch")
            retained = [key(x["k2"]) for x in seeds]
            same_width = [k for k in retained if len(k) == len(k2)]
            nearest = min((distance(k, k2) for k in same_width), default=None)
            require(row["true_key_shortlisted"] == (k2 in retained), "retention diagnostic mismatch")
            require(row["min_retained_swap_distance"] == nearest, "nearest-retained diagnostic mismatch")
            diagnostics_checked += 1
        else:
            report.append(f"SKIP: shortlist cache absent for {row['tag']}; retention/nearest diagnostics not rechecked.")
    report.append(f"PASS: {len(controls)} available controls independently reconstructed/decrypted/rescored; "
                  f"all accuracy, minimum-distance and recovery metrics match; {diagnostics_checked} cached diagnostics checked.")
    for s in STRATA:
        rows = [row for row in controls if row["stratum"] == s]
        report.append(f"VERIFIED: {s}: {len(rows)}/10 records; {sum(row['recovered'] for row in rows)} recovered; "
                      f"{sum(row['exact'] for row in rows)} exact; CPU seconds {sum(row['cpu'] for row in rows):.3f}.")
    controls_complete = intact and set(actual_trials) == expected_trials
    false_candidates = sum(row["candidate"] and not row["recovered"] for row in controls)
    gate = controls_complete and false_candidates == 0 and all(
        sum(row["recovered"] for row in controls if row["stratum"] == s) >= 8 for s in plan["required_strata"])
    if not controls_complete:
        report.append(f"INCOMPLETE: controls {len(controls)}/40; no passing gate; observed false candidates {false_candidates}.")
    else:
        report.append(f"{'PASS' if gate else 'FAIL'}: control gate; >=8/10 exact and one strata; "
                      f"zero false candidates required; observed false candidates {false_candidates}.")
    report.extend(false_details)
    report.append(f"VERIFIED COST: recorded controls CPU seconds {sum(row['cpu'] for row in controls):.3f}; "
                  f"scanning {sum(row['scan']['cpu'] for row in controls):.3f}; "
                  f"refinement {sum(row['cpu']-row['scan']['cpu'] for row in controls):.3f}. "
                  "Development benchmarks and aborted batch excluded.")
    report.append(f"Control snapshot SHA256: {control_sha}.")
    gate_diagnostic_path = HERE / "results/gate-diagnostic.json"
    if gate_diagnostic_path.exists():
        gate_diagnostic = load(gate_diagnostic_path)
        require(gate_diagnostic["control_sha256"] == control_sha and gate_diagnostic["build_id"] == build_id,
                "gate diagnostic provenance mismatch")
        require(gate_diagnostic["false_candidates"] == expected_gate_diagnostics,
                "independently reconstructed gate diagnostic mismatch")
        require(gate_diagnostic["target_run"] is False, "unexpected target-run claim in gate diagnostic")
        report.append("PASS: gate-diagnostic.json independently verified against reconstructed plaintext/keys, "
                      "both plaintext scores, returned reading, metrics and control/build pins.")
    else:
        report.append("SKIP: gate-diagnostic.json absent.")

    target_path = HERE / "results" / f"{target_tag}.jsonl"
    targets, target_intact, target_sha = snapshot(target_path)
    expected_cells = {(body, w) for body in ("T1", "T1-shuffle") for w in range(12, 23)}
    actual_cells = [(row["body"], row["first_width_hypothesis"]) for row in targets]
    require(len(actual_cells) == len(set(actual_cells)) and set(actual_cells) <= expected_cells,
            "duplicate or unexpected target width/body cell")
    if targets:
        require(gate, "target records exist without a passing complete control gate")
        protocol = load(HERE / "protocol.json")
        require(protocol["build"] == build and protocol["control_file"] == controls_path.name and
                protocol["control_sha256"] == control_sha and protocol["required_strata"] == plan["required_strata"],
                "target protocol/build/control pins mismatch")
        source = (HERE.parent.parent / "sources/telegram-1.txt").read_text().upper()
        ciphertext = "".join(c for c in source if "A" <= c <= "Z")
        require(len(ciphertext) == 615 and hashlib.sha256(ciphertext.encode()).hexdigest().startswith("e266615d"),
                "T1 source mismatch")
        noise = list(ciphertext)
        random.Random(stream("shuffle", target_tag, 0)).shuffle(noise)
        texts = {"T1": ciphertext, "T1-shuffle": "".join(noise)}
        require(Counter(ciphertext) == Counter(texts["T1-shuffle"]), "shuffle counts mismatch")
        for row in targets:
            require(row["tag"] == f"{target_tag}_{row['body']}_{row['first_width_hypothesis']}", "target tag mismatch")
            check_row(row, texts[row["body"]])
        report.append(f"PASS: {len(targets)} available target rows independently decrypted/rescored; protocol pins match.")
        for body in ("T1", "T1-shuffle"):
            rows = [row for row in targets if row["body"] == body]
            if rows:
                report.append(f"VERIFIED: {body}: {len(rows)}/11 widths; best score {max(row['best']['score'] for row in rows):.4f}; "
                              f"{sum(row['candidate'] for row in rows)} candidates; CPU seconds {sum(row['cpu'] for row in rows):.3f}.")
    if target_intact and set(actual_cells) == expected_cells:
        report.append("PASS: all22 target width/body cells present, unique and checked; no global early stop.")
    elif controls_complete and not gate and not targets:
        report.append("NOT RUN: target search withheld because the complete control batch failed its gate.")
    else:
        report.append(f"INCOMPLETE: target {len(targets)}/22 width/body cells; full target verification unavailable.")
    report.append(f"Target snapshot SHA256: {target_sha}.")
    protocol_exists = (HERE / "protocol.json").exists()
    target_artifacts = sorted((HERE / "results").glob("target*.jsonl"))
    if not protocol_exists and not target_artifacts:
        report.append("NO TARGET ARTIFACTS: protocol.json absent and no results/target*.jsonl files present.")
    report.append("Scope: conditional recovery with first width supplied; 615-letter literary proxy; first widths12–22; "
                  "second lengths18–28. Off-list results do not exclude cipher families. One shuffle is not a p-value estimate.")
    return "\n".join(report) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--target-tag", default="target25")
    args = parser.parse_args()
    result = verify(args.target_tag)
    if args.output:
        args.output.write_text(result)
    print(result, end="")
