"""Freeze12–17 letter keys from24's FULL metadata plus one rank-position swap.

Candidate-only operation: no ciphertext, plaintext or solver is read.
Byte records are width followed by ranks, sorted by(width,ranks).
"""
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
S24=HERE.parent / "24-phrase-seeded"


def main():
    start=time.process_time()
    path=S24 / "out/keys.json"
    source=path.read_bytes()
    expected=json.loads((S24 / "build-manifest.json").read_text())["keys_json_sha256"]
    assert hashlib.sha256(source).hexdigest()==expected
    records=[r for r in json.loads(source) if 12<=len(r["key"])<=17]
    counts=Counter(len(r["key"]) for r in records)
    per_width={}
    bounds={}
    for w in range(12,18):
        # Unsigned Stirling coefficients for permutation distance at most3.
        ball=1+math.comb(w,2)+2*math.comb(w,3)+9*math.comb(w,4)+20*math.comb(w,5)+15*math.comb(w,6)
        bounds[str(w)]=dict(original_keys=counts[w],radius3_ball=ball,
                            union_upper_bound=counts[w]*ball,permutations=math.factorial(w))
        assert 0<counts[w] and counts[w]*ball<math.factorial(w)
    for r in records:
        k=list(r["key"])
        assert sorted(k)==list(range(len(k)))
        pool=per_width.setdefault(len(k),set())
        pool.add(bytes(k))
        for a,b in itertools.combinations(range(len(k)),2):
            k[a],k[b]=k[b],k[a]; pool.add(bytes(k)); k[a],k[b]=k[b],k[a]
    out=HERE / "out"; out.mkdir(exist_ok=True)
    (out / "active-keys.json").write_text(json.dumps(records,indent=1)+"\n")
    expanded=out / "expanded.bin"
    with expanded.open("wb") as f:
        for w in sorted(per_width):
            for k in sorted(per_width[w]): f.write(bytes([w])+k)
    manifest=dict(source_keys_sha256=expected,
                  active_keys_sha256=hashlib.sha256((out / "active-keys.json").read_bytes()).hexdigest(),
                  expanded_sha256=hashlib.sha256(expanded.read_bytes()).hexdigest(),
                  original_keys=len(records),original_by_length=dict(sorted(counts.items())),
                  keys=sum(map(len,per_width.values())),
                  by_length={str(w):len(v) for w,v in sorted(per_width.items())},
                  radius3_bounds=bounds,
                  construction="union of exact short-band list keys and every single arbitrary rank-position swap",
                  cpu_seconds=round(time.process_time()-start,3))
    (HERE / "expanded-manifest.json").write_text(json.dumps(manifest,indent=1)+"\n")
    print(json.dumps(manifest))


if __name__=="__main__": main()
