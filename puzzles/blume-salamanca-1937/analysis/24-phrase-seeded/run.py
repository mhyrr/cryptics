"""Build, verify, calibrate and run the phrase-seeded solver. Standard library only.

From any directory:
  python3 -I run.py build
  python3 -I run.py verify
  python3 -I run.py controls TAG TRIALS_PER_STRATUM [WORKERS]
  python3 -I run.py target TAG [CLIMB=1]
  python3 -I run.py summary TAG

Targets require a passing controls file and a frozen protocol (see README).
No true key/plaintext is supplied to either C search phase.
"""
import array
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import random
import subprocess
import sys

HERE = Path(__file__).resolve().parent
S21 = HERE.parent / "21-dc-method"
S01 = HERE.parent / "01-solver"
sys.path[:0] = [str(HERE), str(S21), str(S01)]
import phrases
import run21
import transpo

OUT = HERE / "out"
RESULTS = HERE / "results"
BIN = OUT / "seedsolve"
PARAMS = dict(wmin=12, wmax=22, keep=4, samples=64, budget=20000, restarts=12, threshold=-5.10)


def seed(kind, tag, i):
    return int.from_bytes(hashlib.sha256(f"24|{kind}|{tag}|{i}".encode()).digest()[:8], "big")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n")


def execute(args):
    p = subprocess.run([str(BIN)] + list(map(str, args)), cwd=S21, capture_output=True, text=True, check=True)
    return [json.loads(l) for l in p.stdout.splitlines() if l.startswith("{")], p.stderr


def parse_key(s):
    key = list(map(int, s.split(",")))
    assert sorted(key) == list(range(len(key)))
    return key


def check_reading(ct, r):
    k1, k2 = parse_key(r["k1"]), parse_key(r["k2"])
    got = transpo.double_dec(ct, k1, k2)
    assert got == r["pt"], "independent decryption mismatch"
    q = array.array("f")
    with (S21 / "out/lm_es_4.bin").open("rb") as f:
        q.fromfile(f, 26**4)
    vals = [ord(c)-65 for c in got]
    sc = sum(q[((a*26+b)*26+c)*26+d] for a,b,c,d in zip(vals, vals[1:], vals[2:], vals[3:])) / (len(got)-3)
    assert abs(sc-r["score"]) < 0.0001, (sc, r["score"])
    return got


def build():
    phrases.main()
    subprocess.run(["cc", "-O3", "-march=native", "-o", str(BIN), str(HERE / "seedsolve.c"), "-lm"], check=True)
    manifest = dict(params=PARAMS, binary_sha256=sha(BIN), wrapper_sha256=sha(HERE / "seedsolve.c"),
                    engine_sha256=sha(S21 / "dcm.c"), keys_sha256=sha(OUT / "keys.tsv"),
                    driver_sha256=sha(__file__), keys_json_sha256=sha(OUT / "keys.json"),
                    plant_inputs=plant_inputs(), model2_sha256=sha(S21 / "out/lm_es_2.bin"),
                    model4_sha256=sha(S21 / "out/lm_es_4.bin"))
    dump(HERE / "build-manifest.json", manifest)


def plant_inputs():
    files=[S01 / n for n in ("plaintext.py","lm.py","transpo.py","corpus_manifest.json")]
    files += [S21 / "run21.py", HERE / "phrases.py"]
    manifest=json.loads((S01 / "corpus_manifest.json").read_text())
    files += [S01 / "out/raw_es" / f"{b['id']}.txt" for b in manifest["es"]
              if b["split"]=="heldout" and b["id"] not in run21.EXCLUDE
              and b["id"] not in run21.plaintext.HELDOUT_EXCLUDE]
    return {str(p.relative_to(HERE.parent)):sha(p) for p in files}


def check_build():
    m = json.loads((HERE / "build-manifest.json").read_text())
    assert m["params"] == PARAMS
    for field, path in [("binary", BIN), ("wrapper", HERE / "seedsolve.c"), ("engine", S21 / "dcm.c"),
                        ("keys", OUT / "keys.tsv"), ("keys_json", OUT / "keys.json"), ("driver", Path(__file__)),
                        ("model2", S21 / "out/lm_es_2.bin"), ("model4", S21 / "out/lm_es_4.bin")]:
        assert sha(path) == m[field + "_sha256"], f"{field} changed since build"
    assert m["plant_inputs"]==plant_inputs(), "plant generator/corpus changed"
    return m


def pipeline(ct, tag, climb=1):
    check_build()
    work = OUT / tag
    work.mkdir(exist_ok=True)
    cf = work / "ct.txt"
    cf.write_text(ct)
    p = PARAMS
    rr, err = execute(["scan", cf, OUT / "keys.tsv", p["wmin"], p["wmax"], p["keep"], p["samples"], seed("scan", tag, 0)])
    scan_cost = json.loads(err.strip().splitlines()[-1])
    dump(work / "shortlist.json", rr)
    best, readings = None, []
    for i, cand in enumerate(sorted(rr, key=lambda r: -r["z"])):
        got, _ = execute(["seed", cf, cand["k2"], cand["w1"], climb, p["budget"], p["restarts"], seed("refine", tag, i)])
        r = got[-1]
        check_reading(ct, r)
        r.update(seed_id=cand["id"], seed_k2=cand["k2"], seed_z=cand["z"])
        readings.append(r)
        if best is None or r["score"] > best["score"]:
            best = r
        if best["score"] > p["threshold"]:
            break  # Identical score-only stop on controls and targets; no plant feedback.
    dump(work / "readings.json", readings)
    result = dict(tag=tag, n=len(ct), climb=climb, build_id=sha(HERE / "build-manifest.json"),
                  params=PARAMS, scan=scan_cost, seeds_tried=len(readings),
                  cpu=round(scan_cost["cpu"]+sum(r["cpu"] for r in readings), 3),
                  candidate=best["score"]>p["threshold"], best=best)
    dump(work / "result.json", result)
    return result


def verify():
    check_build()
    assert phrases.rank("REFERENCE") == (7,1,5,2,8,3,6,0,4)
    assert phrases.rank("AAAA", True) == (3,2,1,0)
    rnd = random.Random(24)
    # Retain the fixture with the other experiment artifacts; no deletion permission is needed.
    cf = OUT / "verify_ct.txt"
    for _ in range(100):
        n = rnd.randint(100, 700)
        pt = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(n))
        a,b = rnd.randint(2,30),rnd.randint(8,32)
        k1,k2 = rnd.sample(range(a),a),rnd.sample(range(b),b)
        cf.write_text(transpo.double_enc(pt,k1,k2))
        got = subprocess.check_output([str(BIN),"decrypt",str(cf),",".join(map(str,k1)),",".join(map(str,k2)),"CC"],text=True)
        assert got.strip() == pt
    print("100/100 C decryptions match independent Python encryption; keyword/tie examples pass")


def control_one(job):
    tag, distance, i = job
    rng = random.Random(seed("plant",tag,f"{distance}:{i}"))
    records = json.loads((OUT / "keys.json").read_text())
    w2 = rng.randint(18,28)
    base = rng.choice([r for r in records if len(r["key"]) == w2])
    w1 = rng.randint(12,22)
    pt = run21.plaintext.telegram(615,rng,"es","telegraph")
    k1,k2 = rng.sample(range(w1),w1),list(base["key"])
    positions = rng.sample(range(w2),2*distance)
    for a,b in zip(positions[::2],positions[1::2]):
        k2[a],k2[b] = k2[b],k2[a]
    # The plant's keys exist only here and in its independent verification, never in search arguments.
    ct = transpo.double_enc(pt,k1,k2)
    result = pipeline(ct,f"{tag}_d{distance}_{i}",climb=1)
    dec = result["best"]["pt"]
    acc = run21.shift_acc(dec,pt)
    result.update(distance=distance,trial=i,plant_w1=w1,plant_w2=w2,plant_seed_id=base["id"],
                  acc=round(acc,4),acc_inplace=round(sum(a==b for a,b in zip(dec,pt))/len(pt),4),
                  exact=dec==pt,recovered=acc>=0.95,plaintext_sha256=hashlib.sha256(pt.encode()).hexdigest())
    return result


def controls(tag, trials, workers):
    check_build()
    RESULTS.mkdir(exist_ok=True)
    run21.load_words("es")
    jobs=[(tag,d,i) for d in (0,1,2) for i in range(trials)]
    path = RESULTS / f"{tag}.jsonl"
    if path.exists():
        raise SystemExit("result exists; choose a fresh tag")
    with ThreadPoolExecutor(workers) as pool, path.open("w") as f:
        futs = [pool.submit(control_one,j) for j in jobs]
        for future in as_completed(futs):
            r=future.result()
            f.write(json.dumps(r)+"\n"); f.flush()
            print(f"d={r['distance']} trial={r['trial']} {r['plant_w1']}x{r['plant_w2']} "
                  f"acc={r['acc']} score={r['best']['score']} cpu={r['cpu']} seeds={r['seeds_tried']}",flush=True)


def target(tag, climb):
    protocol=json.loads((HERE / "protocol.json").read_text())
    assert protocol["build"] == check_build()
    ctl_path=RESULTS / protocol["control_file"]
    assert sha(ctl_path) == protocol["control_sha256"]
    cr=[json.loads(l) for l in ctl_path.read_text().splitlines()]
    distances=protocol["required_distances"]
    assert distances in ([0],[0,1],[0,1,2]), "require a nonempty, declared distance range"
    assert protocol["climb"]==1 and all(r["climb"]==1 for r in cr)
    assert all(r["build_id"]==sha(HERE / "build-manifest.json") and r["params"]==PARAMS for r in cr)
    for d in distances:
        rr=[r for r in cr if r["distance"]==d]
        assert len({r["trial"] for r in rr})==len(rr), "duplicate control trial"
        assert len(rr)>=10 and sum(r["recovered"] for r in rr)/len(rr)>=0.8, "control gate failed"
    assert climb == protocol["climb"]
    src=HERE.parent.parent / "sources/telegram-1.txt"
    ct="".join(c for c in src.read_text().upper() if "A"<=c<="Z")
    assert len(ct)==615 and hashlib.sha256(ct.encode()).hexdigest().startswith("e266615d")
    RESULTS.mkdir(exist_ok=True)
    outpath=RESULTS / f"{tag}.jsonl"
    if outpath.exists():
        raise SystemExit("result exists; choose a fresh tag")
    rng=random.Random(seed("shuffle",tag,0))
    noise=list(ct); rng.shuffle(noise)
    with outpath.open("w") as f:
        for label,text in [("T1",ct),("T1-shuffle","".join(noise))]:
            r=pipeline(text,f"{tag}_{label}",climb=climb)
            r["body"]=label
            f.write(json.dumps(r)+"\n"); f.flush()
            print(f"{label} best={r['best']['score']} candidate={r['candidate']} cpu={r['cpu']}",flush=True)


def summary(tag):
    rr=[json.loads(l) for l in (RESULTS / f"{tag}.jsonl").read_text().splitlines()]
    for d in (0,1,2):
        ss=[r for r in rr if r.get("distance")==d]
        if ss:
            print(f"distance {d}: {sum(r.get('recovered',r.get('full',False)) for r in ss)}/{len(ss)} recovered (>=95%, shift <=40); "
                  f"CPU seconds {sum(r['cpu'] for r in ss):.1f}; "
                  f"accuracies {[r['acc'] for r in sorted(ss,key=lambda r:r['trial'])]}")
            if all("exact" in r for r in ss):
                print(f"  exact in-place: {sum(r['exact'] for r in ss)}/{len(ss)}")
    for r in rr:
        if "body" in r:
            print(r["body"],r["best"]["score"],"candidate",r["candidate"],"cpu",r["cpu"])


if __name__ == "__main__":
    command=sys.argv[1]
    if command=="build": build()
    elif command=="verify": verify()
    elif command=="controls": controls(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]) if len(sys.argv)>4 else 2)
    elif command=="target": target(sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1)
    elif command=="summary": summary(sys.argv[2])
    else: raise SystemExit("unknown command")
