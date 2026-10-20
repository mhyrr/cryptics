"""Verify experiment27 records without importing its driver or running a solver.

python3 -I /path/to/verify_results.py --output /path/to/results/verification.txt
Rebuilds the candidate union in memory, not a cryptanalytic search. Requires
frozen corpus/model/binary caches. Missing per-run caches are explicit skips.
Only the pinned literary plaintext generator is reused. Partial JSONL snapshots
are reported as INCOMPLETE and never pass a gate.
"""
import argparse
import array
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import random
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
S26, S25, S24 = (HERE.parent / name for name in ("26-k1-recovery", "25-seed-retention", "24-phrase-seeded"))
PLAN_SHA256 = "d46a676311ac124e7395b3c33de97a94fda91af9536dc2edfab701af3f8392f7"
SOURCE_FREEZE_COMMIT = "fa32d99"
STRATA = ("exact", "one", "two", "random")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stream(kind, tag, index):
    return int.from_bytes(hashlib.sha256(f"27|{kind}|{tag}|{index}".encode()).digest()[:8], "big")


def key(value):
    ranks = list(map(int, value.split(",")))
    require(sorted(ranks) == list(range(len(ranks))), "invalid recorded permutation")
    return ranks


def distance(a, b):
    require(len(a) == len(b), "swap distance requires equal key lengths")
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


def verify():
    report = ["Independent verification of experiment27 recorded results.",
              "No solver, build or cryptanalytic search is invoked; experiment27's driver is not imported."]
    plan_path, build_path = HERE / "control-plan.json", HERE / "build-manifest.json"
    require(sha(plan_path) == PLAN_SHA256, "frozen control-plan SHA mismatch")
    try:
        frozen_plan = subprocess.check_output(
            ["git", "show", SOURCE_FREEZE_COMMIT+":puzzles/blume-salamanca-1937/analysis/27-short-k2/control-plan.json"],
            cwd=HERE.parents[3], stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError):
        report.append(f"SKIP: git source-freeze commit {SOURCE_FREEZE_COMMIT} unavailable; literal plan hash still checked.")
    else:
        require(hashlib.sha256(frozen_plan).hexdigest() == PLAN_SHA256, "source-freeze commit/plan mismatch")
        report.append(f"PASS: source/control-plan freeze commit {SOURCE_FREEZE_COMMIT} matches pinned plan bytes.")
    plan, build = load(plan_path), load(build_path)
    require(plan["build"] == build and plan["n"] == 615 and plan["trials_per_stratum"] == 10 and
            plan["pipeline_strata"] == list(STRATA), "plan/build mismatch")
    paths = {"source": HERE / "seedsolve.c", "driver": HERE / "run.py", "binary": HERE / "out/seedsolve",
             "parent_manifest": S25 / "build-manifest.json", "optimizer_parent_manifest": S26 / "build-manifest.json",
             "expanded": HERE / "out/expanded.bin", "expand_source": HERE / "expand.py",
             "expanded_manifest": HERE / "expanded-manifest.json", "engine": HERE.parent / "21-dc-method/dcm.c"}
    for name, path in paths.items():
        require(sha(path) == build[name+"_sha256"], f"frozen27 {name} hash mismatch")
    old26, old25 = load(paths["optimizer_parent_manifest"]), load(paths["parent_manifest"])
    require(sha(S26 / "seedsolve.c") == old26["source_sha256"] and
            old26["engine_sha256"] == build["engine_sha256"], "optimizer parent source/engine mismatch")
    strip_comments = lambda text: re.sub(r"/\*.*?\*/|//[^\n]*", "", text, flags=re.S)
    c26 = strip_comments((S26 / "seedsolve.c").read_text())
    require(c26.count("for(int w=18;w<=28;w++)") == 1 and c26.count("if(w<18 || w>28 || fread(") == 1,
            "unexpected parent scanner source")
    expected = c26.replace("for(int w=18;w<=28;w++)", "for(int w=12;w<=17;w++)").replace(
        "if(w<18 || w>28 || fread(", "if(w<12 || w>17 || fread(")
    require(expected == strip_comments(paths["source"].read_text()), "C changed beyond comments/two scan-band bounds")
    params = dict(old26["params"], wmin=16, wmax=22, k2_min=12, k2_max=17)
    require(build["params"] == params and build["cpu_caps_seconds"] == plan["cpu_caps_seconds"] ==
            {"scan": 180, "refinement_process": 60}, "search/cap parameters changed")
    paths25 = {"source": S25 / "seedsolve.c", "driver": S25 / "run.py", "expand_source": S25 / "expand.py",
               "binary": S25 / "out/seedsolve", "expanded": S25 / "out/expanded.bin",
               "previous_manifest": S24 / "build-manifest.json"}
    for name, path in paths25.items():
        require(sha(path) == old25[name+"_sha256"], f"inherited25 {name} hash mismatch")
    old24 = load(paths25["previous_manifest"])
    paths24 = {"binary": S24 / "out/seedsolve", "wrapper": S24 / "seedsolve.c", "driver": S24 / "run.py",
               "engine": paths["engine"], "keys": S24 / "out/keys.tsv", "keys_json": S24 / "out/keys.json",
               "model2": HERE.parent / "21-dc-method/out/lm_es_2.bin",
               "model4": HERE.parent / "21-dc-method/out/lm_es_4.bin"}
    for name, path in paths24.items():
        require(sha(path) == old24[name+"_sha256"], f"inherited24 {name} hash mismatch")
    for relative, digest in old24["plant_inputs"].items():
        require(sha(HERE.parent / relative) == digest, f"plant input hash mismatch: {relative}")
    report.append(f"PASS: frozen plan/build/parent/source/binary/model/corpus pins; plan SHA256 {PLAN_SHA256}.")
    report.append("PASS: complete C source equals pinned26 after removing comments and changing only two scanner bounds; optimizer unchanged.")

    full_records = load(paths24["keys_json"])
    records = [r for r in full_records if 12 <= len(r["key"]) <= 17]
    expansion = load(paths["expanded_manifest"])
    active_path = HERE / "out/active-keys.json"
    require(load(active_path) == records and sha(active_path) == expansion["active_keys_sha256"] and
            expansion["source_keys_sha256"] == sha(paths24["keys_json"]), "short-band source metadata mismatch")
    counts = Counter(len(r["key"]) for r in records)
    require(len(records) == expansion["original_keys"] and
            {str(w): counts[w] for w in range(12, 18)} == expansion["original_by_length"], "original key counts mismatch")
    expanded_by_width = {}
    digest = hashlib.sha256()
    for w in range(12, 18):
        original = [r["key"] for r in records if len(r["key"]) == w]
        union = set()
        for ranks in original:
            require(sorted(ranks) == list(range(w)), "invalid source key")
            union.add(bytes(ranks))
            for a in range(w):
                for b in range(a+1, w):
                    swapped = list(ranks)
                    swapped[a], swapped[b] = swapped[b], swapped[a]
                    union.add(bytes(swapped))
        expanded_by_width[w] = sorted(union)
        for packed in expanded_by_width[w]:
            digest.update(bytes([w])+packed)
        # Coefficients of product(1+j*x), j=1..w-1, independently count
        # permutations at transposition distances0..3 (Stirling recurrence).
        coefficient = [1, 0, 0, 0]
        for j in range(1, w):
            for d in range(3, 0, -1):
                coefficient[d] += j*coefficient[d-1]
        ball = sum(coefficient)
        bound = dict(original_keys=counts[w], radius3_ball=ball, union_upper_bound=counts[w]*ball,
                     permutations=math.factorial(w))
        require(expansion["radius3_bounds"][str(w)] == bound and 0 < counts[w] and
                bound["union_upper_bound"] < bound["permutations"], "radius3 existence bound mismatch")
        require(len(union) == expansion["by_length"][str(w)], "expanded width count mismatch")
        report.append(f"PASS SHORT BAND w2={w}: {counts[w]} original, {len(union)} expanded; "
                      f"radius3 union upper bound {bound['union_upper_bound']} < {bound['permutations']} permutations.")
    expanded_count = sum(map(len, expanded_by_width.values()))
    require(expanded_count == expansion["keys"] == 160327 and digest.hexdigest() ==
            expansion["expanded_sha256"] == sha(paths["expanded"]), "independent candidate-union reconstruction mismatch")
    report.append(f"PASS: independently regenerated {len(records)} original/{expanded_count} expanded short-band keys, exact sorted-byte hash and off-list existence bounds.")

    def expanded_key(index):
        require(index >= 0, "negative expanded seed ID")
        for w, ranks in expanded_by_width.items():
            if index < len(ranks):
                return list(ranks[index])
            index -= len(ranks)
        raise ValueError("expanded seed ID out of range")

    sys.path[:0] = [str(HERE.parent / "21-dc-method"), str(HERE.parent / "01-solver")]
    import run21
    run21.load_words("es")
    by_width = {w: [r for r in records if len(r["key"]) == w] for w in range(12, 18)}
    q = array.array("f")
    q.frombytes(paths24["model4"].read_bytes())
    require(len(q) == 26**4, "quadgram model size mismatch")
    build_id = sha(build_path)

    def quad_score(plaintext):
        t = [ord(c)-65 for c in plaintext]
        return sum(q[((a*26+b)*26+c)*26+d] for a, b, c, d in zip(t, t[1:], t[2:], t[3:]))/(len(t)-3)

    def reading(ciphertext, result):
        a, b = key(result["k1"]), key(result["k2"])
        require(result["conv"] == "CC" and (len(a), len(b)) == (result["w1"], result["w2"]), "reading geometry mismatch")
        require(16 <= len(a) <= 22 and 12 <= len(b) <= 17, "reading outside short band")
        got = decrypt(decrypt(ciphertext, b), a)
        require(got == result["pt"] and abs(quad_score(got)-result["score"]) < .0001,
                "independent decryption/score mismatch")
        return got

    def check_row(row, ciphertext):
        require(row["params"] == params and row["build_id"] == build_id and row["n"] == len(ciphertext) == 615,
                "result provenance/length mismatch")
        require(row["first_width_hypothesis"] == row["best"]["w1"], "first-width hypothesis mismatch")
        require(row["scan"]["keys"] == expanded_count and row["scan"]["n_idp"] == expanded_count+6*params["samples"],
                "incomplete short-band scan/reference work")
        require(row["seeds_tried"] == 4 and row["candidate"] == (row["best"]["score"] > params["threshold"]),
                "seed count/candidate classification mismatch")
        got = reading(ciphertext, row["best"])
        work = HERE / "out" / row["tag"]
        if (work / "ct.txt").exists():
            require((work / "ct.txt").read_text() == ciphertext, "ciphertext cache mismatch")
        else:
            report.append(f"SKIP: {row['tag']} ciphertext cache absent; ciphertext reconstructed independently.")
        seeds = load(work / "shortlist.json") if (work / "shortlist.json").exists() else None
        readings = load(work / "readings.json") if (work / "readings.json").exists() else None
        if seeds is not None:
            require(len(seeds) == 4 and [s["rank"] for s in seeds] == list(range(4)), "shortlist count/rank mismatch")
            for s in seeds:
                ranks = key(s["k2"])
                require(ranks == expanded_key(s["id"]) and len(ranks) == s["w2"] and
                        s["w1"] == row["first_width_hypothesis"], "shortlist seed ID/key geometry mismatch")
        else:
            report.append(f"SKIP: {row['tag']} shortlist cache absent; seed identity/order/retention not rechecked.")
        if readings is not None:
            require(len(readings) == 4, "incomplete refinement cache")
            for item in readings:
                reading(ciphertext, item)
                require(item["w1"] == row["first_width_hypothesis"], "refinement first width mismatch")
            require(row["best"] == max(readings, key=lambda r: r["score"]), "best selection mismatch")
            require(abs(row["cpu"]-round(row["scan"]["cpu"]+sum(r["cpu"] for r in readings), 3)) < .0001, "CPU sum mismatch")
            if seeds is not None:
                for s, r in zip(seeds, readings):
                    require((s["id"], s["k2"], s["z"]) == (r["seed_id"], r["seed_k2"], r["seed_z"]),
                            "not all four retained seeds processed in order")
        else:
            report.append(f"SKIP: {row['tag']} refinement cache absent; best reading independently verified only.")
        return got, seeds

    control_path = HERE / "results" / (plan["control_tag"]+".jsonl")
    controls, intact, control_sha = snapshot(control_path)
    actual = [(r["stratum"], r["trial"]) for r in controls]
    expected = {(s, i) for s in STRATA for i in range(10)}
    require(len(actual) == len(set(actual)) and set(actual) <= expected, "duplicate/unexpected control trial")
    complete = intact and set(actual) == expected
    checked_shortlists = 0
    for row in controls:
        s, i = row["stratum"], row["trial"]
        require(row["tag"] == f"{plan['control_tag']}_{s}_{i}", "control tag mismatch")
        rng = random.Random(stream("plant", plan["control_tag"], f"{s}:{i}"))
        w2 = rng.randint(12, 17)
        choices = by_width[w2]
        for _ in range(10000):
            if s == "random":
                k2, base = rng.sample(range(w2), w2), None
            else:
                d = {"exact": 0, "one": 1, "two": 2}[s]
                base = rng.choice(choices)
                k2 = list(base["key"])
                positions = rng.sample(range(w2), 2*d)
                for a, b in zip(positions[::2], positions[1::2]):
                    k2[a], k2[b] = k2[b], k2[a]
            md = min(distance(r["key"], k2) for r in choices)
            if (s == "random" and md > 3) or (s != "random" and md == d):
                break
        else:
            raise ValueError("independent rejection sampling exhausted")
        w1 = rng.randint(16, 22)
        pt = run21.plaintext.telegram(615, rng, "es", "telegraph")
        k1 = rng.sample(range(w1), w1)
        require((row["plant_w1"], row["plant_w2"], row["first_width_hypothesis"], row["base_id"],
                 row["min_list_swap_distance"], row["min_expanded_swap_distance"]) ==
                (w1, w2, w1, None if base is None else base["id"], md, max(0, md-1)), "plant/distance metadata mismatch")
        require(hashlib.sha256(pt.encode()).hexdigest() == row["plaintext_sha256"], "plaintext SHA mismatch")
        got, seeds = check_row(row, encrypt(encrypt(pt, k1), k2))
        accuracy, shift = max(((sum(got[j] == pt[(j+shift) % 615] for j in range(615))/615, shift)
                              for shift in range(-40, 41)), key=lambda x: x[0])
        inplace = sum(a == b for a, b in zip(got, pt))/615
        require(round(accuracy, 4) == row["acc"] and round(inplace, 4) == row["acc_inplace"] and
                (got == pt) == row["exact"] and (accuracy >= .95) == row["recovered"], "recovery metrics mismatch")
        if row["recovered"] and not row["exact"]:
            report.append(f"SHIFT CASE: {row['tag']}; shift {shift}; agreement {accuracy:.4f}; in-place {inplace:.4f}.")
        if seeds is not None:
            retained = [key(x["k2"]) for x in seeds]
            nearest = min((distance(k, k2) for k in retained if len(k) == len(k2)), default=None)
            require(row["true_key_shortlisted"] == (k2 in retained) and row["min_retained_swap_distance"] == nearest,
                    "post-search shortlist diagnostic mismatch")
            checked_shortlists += 1
    false = [r for r in controls if r["candidate"] and not r["recovered"]]
    gate = complete and not false and all(sum(r["recovered"] for r in controls if r["stratum"] == s) >= 8 for s in ("exact", "one"))
    for s in STRATA:
        rows = [r for r in controls if r["stratum"] == s]
        report.append(f"VERIFIED PIPELINE {s}: {len(rows)}/10; {sum(r['recovered'] for r in rows)} recovered; "
                      f"{sum(r['exact'] for r in rows)} exact; {sum(r['candidate'] for r in rows)} candidates; "
                      f"CPU seconds {sum(r['cpu'] for r in rows):.3f}.")
    report.append(f"{'PASS' if gate else 'FAIL' if complete else 'INCOMPLETE'}: pipeline gate; {len(controls)}/40 unique controls, "
                  f"{len(false)} false candidates; {checked_shortlists} shortlist diagnostics checked; "
                  f"snapshot SHA256 {control_sha}.")
    report.append(f"VERIFIED CONTROL COST: total CPU seconds {sum(r['cpu'] for r in controls):.3f}; "
                  f"scanning {sum(r['scan']['cpu'] for r in controls):.3f}; "
                  f"refinement {sum(r['cpu']-r['scan']['cpu'] for r in controls):.3f}; "
                  f"{sum(r['seeds_tried'] for r in controls)} retained-seed refinements.")
    for r in false:
        report.append(f"FALSE CANDIDATE: {r['tag']}; score {r['best']['score']:.4f}; accuracy {r['acc']:.4f}.")

    target_path = HERE / "results" / (plan["target_tag"]+".jsonl")
    targets, target_intact, target_sha = snapshot(target_path)
    cells = [(r["body"], r["first_width_hypothesis"]) for r in targets]
    expected_cells = {(body, w) for body in ("T1", "T1-shuffle") for w in range(16, 23)}
    require(len(cells) == len(set(cells)) and set(cells) <= expected_cells, "duplicate/unexpected target cell")
    if targets:
        require(gate, "target exists without complete passing control gate")
        protocol = load(HERE / "protocol.json")
        require(protocol["build"] == build and protocol["target_tag"] == plan["target_tag"] and
                protocol["control_plan_sha256"] == PLAN_SHA256 and
                protocol["controls"] == {"tag": plan["control_tag"], "sha256": control_sha}, "target protocol/control pins mismatch")
        source = (HERE.parent.parent / "sources/telegram-1.txt").read_text().upper()
        ct = "".join(c for c in source if "A" <= c <= "Z")
        require(len(ct) == 615 and hashlib.sha256(ct.encode()).hexdigest().startswith("e266615d"), "T1 source mismatch")
        letters = list(ct)
        random.Random(stream("shuffle", plan["target_tag"], 0)).shuffle(letters)
        texts = {"T1": ct, "T1-shuffle": "".join(letters)}
        for row in targets:
            require(row["tag"] == f"{plan['target_tag']}_{row['body']}_{row['first_width_hypothesis']}", "target tag mismatch")
            check_row(row, texts[row["body"]])
        for body in ("T1", "T1-shuffle"):
            rows = [r for r in targets if r["body"] == body]
            if rows:
                report.append(f"VERIFIED TARGET {body}: {len(rows)}/7 widths; "
                              f"best score {max(r['best']['score'] for r in rows):.4f}; {sum(r['candidate'] for r in rows)} candidates; "
                              f"{sum(r['seeds_tried'] for r in rows)} seed refinements; CPU seconds {sum(r['cpu'] for r in rows):.3f}.")
        report.append(f"VERIFIED TARGET COST: total CPU seconds {sum(r['cpu'] for r in targets):.3f}; "
                      f"scanning {sum(r['scan']['cpu'] for r in targets):.3f}; "
                      f"refinement {sum(r['cpu']-r['scan']['cpu'] for r in targets):.3f}; "
                      f"{sum(r['seeds_tried'] for r in targets)} retained-seed refinements checked.")
    if target_intact and set(cells) == expected_cells:
        report.append("PASS: all14 target cells present, unique and independently verified; no global early stop.")
    elif complete and not gate and not targets:
        report.append("NOT RUN: target withheld because the complete control gate failed.")
    else:
        report.append(f"INCOMPLETE: target {len(targets)}/14 width/body cells; full target verification unavailable.")
    report.append(f"Target snapshot SHA256: {target_sha}.")
    if not (HERE / "protocol.json").exists() and not list((HERE / "results").glob("target*.jsonl")):
        report.append("NO TARGET ARTIFACTS: protocol.json absent; no results/target*.jsonl files present.")
    report.append("Scope: first widths16–22 supplied per control; second widths12–17; existing short phrase-neighbourhood only; "
                  "615-letter literary proxy. Off-list recoveries are allowed. A negative target cannot exclude arbitrary keys, "
                  "other widths/preparation or the cipher family. One shuffle is not a p-value estimate.")
    return "\n".join(report)+"\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.write_text(result)
    print(result, end="")
