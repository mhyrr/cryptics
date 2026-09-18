"""Compare separately recorded published figures with experiment 06 sequences."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / "06-construction-evidence" / "examples.json"


def build():
    readings = json.loads((HERE / "readings.json").read_text())["records"]
    prior = {r["id"]: r for r in json.loads(PRIOR.read_text())["examples"]}
    ids = [r["id"] for r in readings]
    if len(ids) != len(set(ids)) or set(ids) != set(prior):
        raise ValueError("Reading IDs must match the prior audit exactly")
    records = []
    for reading in readings:
        rows = reading["rows"]
        n = len(rows)
        if not n or any(len(row) != n for row in rows):
            raise ValueError(f"Non-square reading: {reading['id']}")
        old = prior[reading["id"]]
        path = old["path"]
        r, c = path["start"]
        dr, dc = path["step"]
        letters = "".join(rows[r - 1 + i * dr][c - 1 + i * dc]
                          for i in range(path["length"]))
        records.append({"id": reading["id"], "page": reading["page"],
                        "figure": reading["figure"],
                        "exact_case_sensitive_rows_match": rows == old["rows_raw"],
                        "prior_nominated_path": path, "path_letters": letters,
                        "path_matches_prior_string": letters == old["square_string"]})
    return {"status": "Discovery transcription comparison; not historical validation",
            "structural_draft_figures_verified": False,
            "historical_performance": None,
            "hashes": {str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in [PRIOR, HERE / "readings.json", HERE / "compare.py"]},
            "exact_matches": sum(r["exact_case_sensitive_rows_match"] for r in records),
            "records": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    target = HERE / "results.json"
    if args.check:
        if target.read_text() != output:
            raise SystemExit("Saved comparison differs")
        print("Published-diagram comparison verified.")
    else:
        target.write_text(output)
        print("Published-diagram comparison written.")
