"""Verify recorded results without building the solver or running any search.

Run from any directory with Python 3.11+: python3 -I /path/to/verify_results.py
Pass --output PATH to retain the report. Requires the frozen model/corpus caches.
Shortlist and ciphertext cache checks are optional and report explicit skips.
Only plant generation reuses existing code; encryption, decryption, scoring and
recovery metrics below are independent of the solver and its driver.
"""
import argparse
import array
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def stream(kind, tag, index):
    value = f"24|{kind}|{tag}|{index}".encode()
    return int.from_bytes(hashlib.sha256(value).digest()[:8], "big")


def key(value):
    result = list(map(int, value.split(",")))
    require(sorted(result) == list(range(len(result))), "invalid recorded key")
    return result


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


def verify():
    report = ["Independent verification of experiment 24 recorded results.",
              "No build, solver, or search process is invoked."]
    manifest_path = HERE / "build-manifest.json"
    manifest = read_json(manifest_path)
    protocol = read_json(HERE / "protocol.json")
    require(protocol["build"] == manifest, "protocol/build mismatch")
    paths = {
        "binary": HERE / "out/seedsolve", "wrapper": HERE / "seedsolve.c",
        "engine": HERE.parent / "21-dc-method/dcm.c", "keys": HERE / "out/keys.tsv",
        "driver": HERE / "run.py", "keys_json": HERE / "out/keys.json",
        "model2": HERE.parent / "21-dc-method/out/lm_es_2.bin",
        "model4": HERE.parent / "21-dc-method/out/lm_es_4.bin",
    }
    for name, path in paths.items():
        require(sha(path) == manifest[name + "_sha256"], f"frozen {name} hash mismatch")
    for relative, expected in manifest["plant_inputs"].items():
        require(sha(HERE.parent / relative) == expected, f"plant input hash mismatch: {relative}")
    report.append("PASS: protocol, binary, sources, candidate files, models and plant-input hashes.")

    # Import only after checking the frozen generator and corpus hashes.
    sys.path[:0] = [str(HERE.parent / "21-dc-method"), str(HERE.parent / "01-solver")]
    import run21
    run21.load_words("es")
    records = read_json(paths["keys_json"])
    q = array.array("f")
    q.frombytes(paths["model4"].read_bytes())
    require(len(q) == 26**4, "quadgram model size mismatch")
    params, build_id = manifest["params"], sha(manifest_path)

    def check_row(row, ciphertext):
        require(row["build_id"] == build_id and row["params"] == params, "row provenance mismatch")
        require(row["climb"] == protocol["climb"] == 1, "row climb mismatch")
        require(row["n"] == len(ciphertext) == 615, "row length mismatch")
        result = row["best"]
        require(result["conv"] == "CC", "unexpected stage convention")
        k1, k2 = key(result["k1"]), key(result["k2"])
        require((len(k1), len(k2)) == (result["w1"], result["w2"]), "key width mismatch")
        require(params["wmin"] <= len(k1) <= params["wmax"] and 18 <= len(k2) <= 28,
                "returned key outside calibrated width range")
        plaintext = decrypt(decrypt(ciphertext, k2), k1)
        require(plaintext == result["pt"], "independent decryption mismatch")
        values = [ord(c) - 65 for c in plaintext]
        score = sum(q[((a*26+b)*26+c)*26+d]
                    for a, b, c, d in zip(values, values[1:], values[2:], values[3:])) / (len(values)-3)
        require(abs(score-result["score"]) < 0.0001, "independent quadgram score mismatch")
        require(row["candidate"] == (score > params["threshold"]), "candidate threshold mismatch")
        cache = HERE / "out" / row["tag"] / "ct.txt"
        if cache.exists():
            require(cache.read_text() == ciphertext, "ciphertext cache mismatch")
        else:
            report.append(f"SKIP: absent ciphertext cache for {row['tag']} (ciphertext reconstructed).")
        return plaintext

    control_path = HERE / "results" / protocol["control_file"]
    require(sha(control_path) == protocol["control_sha256"], "control-file hash mismatch")
    controls = [json.loads(line) for line in control_path.read_text().splitlines()]
    require(len(controls) == 30, "expected 30 holdout controls")
    for row in controls:
        d, i = row["distance"], row["trial"]
        require(d in (0, 1, 2), "unknown distance stratum")
        require(row["tag"] == f"holdout24_d{d}_{i}", "holdout tag mismatch")
        rng = random.Random(stream("plant", "holdout24", f"{d}:{i}"))
        w2 = rng.randint(18, 28)
        base = rng.choice([record for record in records if len(record["key"]) == w2])
        w1 = rng.randint(12, 22)
        plaintext = run21.plaintext.telegram(615, rng, "es", "telegraph")
        k1, k2 = rng.sample(range(w1), w1), list(base["key"])
        positions = rng.sample(range(w2), 2*d)
        for a, b in zip(positions[::2], positions[1::2]):
            k2[a], k2[b] = k2[b], k2[a]
        require((w1, w2, base["id"]) == (row["plant_w1"], row["plant_w2"], row["plant_seed_id"]),
                "reconstructed plant metadata mismatch")
        require(hashlib.sha256(plaintext.encode()).hexdigest() == row["plaintext_sha256"],
                "reconstructed plaintext hash mismatch")
        got = check_row(row, encrypt(encrypt(plaintext, k1), k2))
        n = len(plaintext)
        shifted = max(sum(got[j] == plaintext[(j+s) % n] for j in range(n)) / n for s in range(-40, 41))
        inplace = sum(a == b for a, b in zip(got, plaintext)) / n
        require(round(shifted, 4) == row["acc"] and round(inplace, 4) == row["acc_inplace"],
                "reconstructed recovery accuracy mismatch")
        require((got == plaintext) == row["exact"] and (shifted >= 0.95) == row["recovered"],
                "reconstructed recovery classification mismatch")
    distances = protocol["required_distances"]
    require(distances in ([0], [0, 1], [0, 1, 2]), "invalid protocol distance range")
    for d in (0, 1, 2):
        rows = [row for row in controls if row["distance"] == d]
        require(sorted(row["trial"] for row in rows) == list(range(10)), "missing/duplicate control trial")
        recovered, exact = sum(row["recovered"] for row in rows), sum(row["exact"] for row in rows)
        if d in distances:
            require(recovered >= 8, "protocol control gate failed")
        report.append(f"PASS: distance {d}: {recovered}/10 recovered; {exact}/10 exact in-place; "
                      f"CPU seconds {sum(row['cpu'] for row in rows):.3f}.")
    report.append(f"PASS: all 30 plants, ciphertexts, decryptions, scores and recovery metrics; gate {distances}.")

    failures = [row for row in controls if not row["recovered"]]
    diagnostic_path = HERE / "results/failure-diagnostics.json"
    if diagnostic_path.exists():
        diagnostics = read_json(diagnostic_path)
        expected = {(row["distance"], row["trial"]) for row in failures}
        require(len(diagnostics) == len(expected) and
                {(row["distance"], row["trial"]) for row in diagnostics} == expected,
                "failure diagnostic coverage mismatch")
        for row in failures:
            diagnostic = next(x for x in diagnostics if
                              (x["distance"], x["trial"]) == (row["distance"], row["trial"]))
            require(diagnostic["tag"] == row["tag"], "failure diagnostic tag mismatch")
            cache = HERE / "out" / row["tag"] / "shortlist.json"
            if not cache.exists():
                report.append(f"SKIP: absent shortlist cache for {row['tag']}; diagnostic not rechecked.")
                continue
            require(sha(cache) == diagnostic["shortlist_sha256"], "shortlist hash mismatch")
            retained = any(x["id"] == row["plant_seed_id"] and x["w1"] == row["plant_w1"]
                           for x in read_json(cache))
            require(retained == diagnostic["base_seed_retained_at_true_w1"], "shortlist diagnostic mismatch")
            report.append(f"PASS: {row['tag']} failure diagnostic; base seed retained at true width: {retained}.")
    else:
        report.append("SKIP: failure-diagnostics.json absent.")

    target_path = HERE / "results/target24.jsonl"
    try:
        targets = [json.loads(line) for line in target_path.read_text().splitlines()]
    except (FileNotFoundError, json.JSONDecodeError):
        targets = []
    if len(targets) == 2 and {row.get("body") for row in targets} == {"T1", "T1-shuffle"}:
        source = (HERE.parent.parent / "sources/telegram-1.txt").read_text().upper()
        ciphertext = "".join(c for c in source if "A" <= c <= "Z")
        require(len(ciphertext) == 615 and hashlib.sha256(ciphertext.encode()).hexdigest().startswith("e266615d"),
                "target source mismatch")
        noise = list(ciphertext)
        random.Random(stream("shuffle", "target24", 0)).shuffle(noise)
        texts = {"T1": ciphertext, "T1-shuffle": "".join(noise)}
        require(Counter(texts["T1"]) == Counter(texts["T1-shuffle"]), "shuffle letter-count mismatch")
        for row in targets:
            require(row["tag"] == f"target24_{row['body']}", "target tag mismatch")
            check_row(row, texts[row["body"]])
            report.append(f"PASS: {row['body']}: independent decryption/score; score {row['best']['score']:.4f}; "
                          f"candidate {row['candidate']}; CPU seconds {row['cpu']:.3f}.")
    else:
        report.append("SKIP: target24.jsonl absent or incomplete; verified controls only.")
    report.append("Scope: 615-letter literary-proxy controls; first widths 12–22; second lengths 18–28; "
                  "5,284 contextual seeds. Exact/one-swap strata pass; two-swap stratum fails.")
    report.append("Shortlist loss does not prove refinement would succeed if an omitted seed were retained. "
                  "One shuffle is a false-positive check, not a p-value estimate.")
    return "\n".join(report) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.write_text(result)
    print(result, end="")
