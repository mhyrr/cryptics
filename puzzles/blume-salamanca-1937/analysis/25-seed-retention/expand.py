"""Freeze the exact plus one-transposition neighbourhood of experiment24's keys.

Candidate generation only; no ciphertext is read. Byte records: one width byte,
then that many rank bytes, in deterministic (width, ranks) order.
"""
import hashlib
import itertools
import json
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
S24=HERE.parent / "24-phrase-seeded"


def main():
    start=time.process_time()
    source=(S24 / "out/keys.tsv").read_bytes()
    expected=json.loads((S24 / "build-manifest.json").read_text())["keys_sha256"]
    assert hashlib.sha256(source).hexdigest()==expected
    per_width={}
    for line in source.decode().splitlines():
        _,text=line.split("\t")
        k=list(map(int,text.split(",")))
        pool=per_width.setdefault(len(k),set())
        pool.add(bytes(k))
        for a,b in itertools.combinations(range(len(k)),2):
            k[a],k[b]=k[b],k[a]
            pool.add(bytes(k))
            k[a],k[b]=k[b],k[a]
    path=HERE / "out/expanded.bin"
    with path.open("wb") as f:
        for width in sorted(per_width):
            for key in sorted(per_width[width]):
                f.write(bytes([width])+key)
    manifest=dict(source_keys_sha256=expected,expanded_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  keys=sum(map(len,per_width.values())),by_length={str(w):len(v) for w,v in sorted(per_width.items())},
                  construction="union of exact list keys and every single arbitrary swap of two rank positions",
                  cpu_seconds=round(time.process_time()-start,3))
    (HERE / "expanded-manifest.json").write_text(json.dumps(manifest,indent=1)+"\n")
    print(json.dumps(manifest))


if __name__=="__main__": main()
