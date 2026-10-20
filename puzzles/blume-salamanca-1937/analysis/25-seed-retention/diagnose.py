"""Rank and force-refine the five OLD failures. Assisted development diagnostics only.

python3 -I diagnose.py > results/development.json
No target text is used. The forced step supplies the true width AND base phrase key.
"""
import json
from pathlib import Path
import random
import subprocess
import sys

HERE=Path(__file__).resolve().parent
S24=HERE.parent / "24-phrase-seeded"
sys.path.insert(0,str(S24))
import run as old


def call(args):
    p=subprocess.run([str(HERE / "out/seedsolve")]+list(map(str,args)),cwd=old.S21,
                     check=True,capture_output=True,text=True)
    return [json.loads(x) for x in p.stdout.splitlines() if x.startswith("{")]


def main():
    old.check_build()
    old.run21.load_words("es")
    records=json.loads((S24 / "out/keys.json").read_text())
    rows=[json.loads(x) for x in (S24 / "results/holdout24.jsonl").read_text().splitlines()]
    results=[]
    for row in rows:
        if row["recovered"]:
            continue
        d,i=row["distance"],row["trial"]
        rng=random.Random(old.seed("plant","holdout24",f"{d}:{i}"))
        w2=rng.randint(18,28)
        base=rng.choice([r for r in records if len(r["key"])==w2])
        w1=rng.randint(12,22)
        pt=old.run21.plaintext.telegram(615,rng,"es","telegraph")
        k1,k2=rng.sample(range(w1),w1),list(base["key"])
        pos=rng.sample(range(w2),2*d)
        for a,b in zip(pos[::2],pos[1::2]): k2[a],k2[b]=k2[b],k2[a]
        ct=old.transpo.double_enc(pt,k1,k2)
        path=HERE / "out" / f"old_d{d}_{i}.txt"
        path.write_text(ct)
        ranked=call(["scan",path,S24 / "out/keys.tsv",12,22,0,64,old.seed("scan",row["tag"],0)])
        old.dump(HERE / "out" / f"ranks_d{d}_{i}.json",ranked)
        hit=next(r for r in ranked if r["w1"]==w1 and r["id"]==base["id"])
        keystr=",".join(map(str,base["key"]))
        forced=call(["seed",path,keystr,w1,1,20000,12,old.seed("diagnostic25",row["tag"],0)])[-1]
        old.check_reading(ct,forced)
        acc=old.run21.shift_acc(forced["pt"],pt)
        rec=dict(distance=d,trial=i,w1=w1,w2=w2,seed_id=base["id"],rank_at_true_width=hit["rank"]+1,
                 assisted=True,supplied=["true first width","base phrase key"],
                 assisted_accuracy=acc,assisted_exact=forced["pt"]==pt,cpu=forced["cpu"],best=forced)
        results.append(rec)
        print(f"old d{d}/{i}: rank={rec['rank_at_true_width']}, assisted acc={acc}",file=sys.stderr,flush=True)
    print(json.dumps(results,indent=1))


if __name__=="__main__": main()
