"""Driver for 21-dc-method: plants, fitness-distance probes, K2-stage searches and full controls.

Plants: Spanish telegraph-style text from 01-solver's held-out books (01's plaintext.telegram, unchanged),
or English prose from this folder's held-out books (en_manifest.json). Keys and plaintext offsets come
from the PLANT stream, solver seeds from the SOLVER stream; both are string-keyed SHA-256, so they cannot
coincide by construction, and the solver aborts if a random start equals the planted K2.

Usage (from this folder):
  python3 -I run21.py probe TAG LANG N W1 W2 TRIALS WORKERS [k=v ...]     -> out/TAG.jsonl
  python3 -I run21.py k2    TAG LANG N "W1xW2,..." TRIALS WORKERS [k=v ...]  -> out/TAG.jsonl  (K2 stage only)
  python3 -I run21.py solve TAG LANG N "W1xW2,..." TRIALS WORKERS [k=v ...]  -> out/TAG.jsonl  (full solve)
  "W1xW2" may use ranges, "16-17x18-20": each trial draws its lengths from the PLANT stream.
  k=v pairs go to out/dcm unchanged (budget=, climb=, idp=, k1climb=, nclimb=, nbasin=, ...).
  style=telegraph|prose picks the plaintext style (default telegraph for es, prose for en).
  ptag=NAME draws plants (and solver seeds) under NAME instead of TAG, so variants can share plants.
"""
import hashlib, json, os, random, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
S01 = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, S01)
sys.path.insert(0, HERE)
import transpo, plaintext  # noqa: E402  (01-solver, read only)
from lm import normalise, strip_gutenberg, EXCLUDE  # noqa: E402
from fetch_en import normalise_en  # noqa: E402

DCM = os.path.join(HERE, "out", "dcm")  # bin=NAME picks out/NAME instead (a build that must not disturb a running control)


def stream(kind, tag, i):
    return int.from_bytes(hashlib.sha256(f"{kind}|{tag}|{i}".encode()).digest()[:8], "big") >> 2


def load_words(lang):
    """Fill 01's plaintext cache with absolute paths (01 reads relative to its own folder)."""
    if lang in plaintext._cache:
        return
    toks = []
    if lang == "en":
        for b in json.load(open(os.path.join(HERE, "en_manifest.json"))):
            if b["split"] != "heldout":
                continue
            raw = strip_gutenberg(open(os.path.join(HERE, "out", "raw_en", f"{b['id']}.txt"), encoding="utf-8", errors="replace").read())
            for tok in re.findall(r"[^\W\d_]+|[.!?;]", raw):
                toks.append("." if tok in ".!?;" else normalise_en(tok))
    else:
        for b in json.load(open(os.path.join(S01, "corpus_manifest.json")))[lang]:
            if b["split"] != "heldout" or b["id"] in EXCLUDE or b["id"] in plaintext.HELDOUT_EXCLUDE:
                continue
            raw = strip_gutenberg(open(os.path.join(S01, "out", f"raw_{lang}", f"{b['id']}.txt"), encoding="utf-8", errors="replace").read())
            for tok in re.findall(r"[^\W\d_]+|[.!?;]", raw):
                toks.append("." if tok in ".!?;" else normalise(tok, lang))
    plaintext._cache[lang] = [t for t in toks if t]


def parse_range(s):
    a, _, b = s.partition("-")
    return int(a), int(b or a)


def plant(tag, i, lang, n, spec, style):
    """Plaintext, keys and ciphertext for trial i, all from the PLANT stream."""
    rnd = random.Random(stream("plant", tag, i))
    a, b = spec.split("x")
    w1, w2 = rnd.randint(*parse_range(a)), rnd.randint(*parse_range(b))
    load_words(lang)
    pt = plaintext.telegram(n, rnd, lang, style)
    k1, k2 = rnd.sample(range(w1), w1), rnd.sample(range(w2), w2)
    return pt, k1, k2, transpo.double_enc(pt, k1, k2, "CC")


def shift_acc(dec, pt, maxs=40):
    """01's rule: best fraction in place over cyclic shifts |s| <= 40."""
    n = len(pt)
    return max(sum(dec[i] == pt[(i + s) % n] for i in range(n)) for s in range(-maxs, maxs + 1)) / n


def one(job):
    mode, tag, ptag, i, lang, n, spec, style, extra = job
    pt, k1, k2, ct = plant(ptag, i, lang, n, spec, style)
    seed = stream("solver", ptag, i)
    assert seed != stream("plant", ptag, i)
    d = os.path.join(HERE, "out", tag)
    os.makedirs(d, exist_ok=True)
    cf, pf = os.path.join(d, f"{i}_ct.txt"), os.path.join(d, f"{i}_pt.txt")
    open(cf, "w").write(ct)
    open(pf, "w").write(pt)
    w1, w2 = len(k1), len(k2)
    dcm = next((os.path.join(HERE, "out", a[4:]) for a in extra if a.startswith("bin=")), DCM)
    extra = [a for a in extra if not a.startswith("bin=")]
    args = [dcm, mode, cf, f"w1={w1}", f"w2={w2}", f"lang={lang}", f"seed={seed}", "truek2=" + ",".join(map(str, k2)),
            "truek1=" + ",".join(map(str, k1))]
    if mode == "solve":
        args.append(f"pt={pf}")
    args += extra
    out = subprocess.run(args, capture_output=True, text=True, cwd=HERE)
    lines = [l for l in out.stdout.strip().splitlines() if l.startswith("{")]
    if out.returncode != 0 or not lines:
        raise RuntimeError(f"{args}: rc={out.returncode} {out.stderr[-500:]}")
    rec = {"trial": i, "tag": tag, "ptag": ptag, "lang": lang, "n": n, "style": style, "w1": w1, "w2": w2, "seed": seed, "args": extra, "bin": os.path.basename(dcm)}
    if mode == "probe":
        rec.update(json.loads(lines[-1]))
    else:
        fin = json.loads(lines[-1])
        rec.update({k: fin[k] for k in ("t", "cpu", "iter", "n_idp", "n_q", "idp", "score", "k2same", "hit_at")})
        if mode == "k2":
            rec["true_idp"] = json.loads(lines[0])["idp"]
            rec["hit"] = fin["hit_at"] >= 0
        else:
            rec["acc"] = round(shift_acc(fin["pt"], pt), 4)
            rec["acc_inplace"] = fin["acc"]
            rec["full"] = rec["acc"] >= 0.95
            rec["first_ok_nidp"] = next((json.loads(l)["n_idp"] for l in lines if shift_acc(json.loads(l)["pt"], pt) >= 0.95), None)
            rec["hit"] = fin["hit_at"] >= 0
    return rec


def main():
    mode, tag, lang, n = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
    if mode == "probe":
        spec, trials, workers, rest = f"{sys.argv[5]}x{sys.argv[6]}", int(sys.argv[7]), int(sys.argv[8]), sys.argv[9:]
    else:
        spec, trials, workers, rest = sys.argv[5], int(sys.argv[6]), int(sys.argv[7]), sys.argv[8:]
    style = next((a.split("=", 1)[1] for a in rest if a.startswith("style=")), "telegraph" if lang != "en" else "prose")
    ptag = next((a.split("=", 1)[1] for a in rest if a.startswith("ptag=")), tag)
    extra = [a for a in rest if not a.startswith(("style=", "ptag="))]
    jobs, i = [], 0
    for part in spec.split(","):
        for _ in range(trials):
            jobs.append((mode, tag, ptag, i, lang, n, part, style, extra))
            i += 1
    load_words(lang)
    with open(os.path.join(HERE, "out", f"{tag}.jsonl"), "w") as f, ThreadPoolExecutor(workers) as ex:
        for rec in ex.map(one, jobs):
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if mode == "probe":
                D = rec["D"]
                print(f"{tag} {rec['w1']}x{rec['w2']} true={rec['true']:.2f} D1={D['1'][0]:.2f} D2={D['2'][0]:.2f} D4={D['4'][0]:.2f} "
                      f"rand={rec['random'][0]:.2f}±{rec['random'][1]:.2f} climbs={[c[0] for c in rec['climbs']]} basin={rec['basin']}", flush=True)
            elif mode == "k2":
                print(f"{tag} {rec['w1']}x{rec['w2']} hit={rec['hit']} at={rec['hit_at']} same={rec['k2same']} idp={rec['idp']:.3f} true={rec['true_idp']:.3f} n_idp={rec['n_idp']} cpu={rec['cpu']}", flush=True)
            else:
                print(f"{tag} {rec['w1']}x{rec['w2']} acc={rec['acc']:.3f} full={rec['full']} hit={rec['hit']} score={rec['score']:.3f} first_ok={rec['first_ok_nidp']} n_idp={rec['n_idp']} cpu={rec['cpu']}", flush=True)


if __name__ == "__main__":
    main()
