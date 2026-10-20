"""Exact one-swap neighbourhood scan, conditional on one stated first width.

python3 -I run.py build | verify | controls TAG N WORKERS | summary TAG
python3 -I run.py target TAG WORKERS       # gated, all 11 widths, T1 + shuffle
No control plaintext or true key enters either C process.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import subprocess
import sys

HERE=Path(__file__).resolve().parent
S24=HERE.parent / "24-phrase-seeded"
sys.path.insert(0,str(S24))
_spec=importlib.util.spec_from_file_location("blume_phrase24",S24 / "run.py")
previous=importlib.util.module_from_spec(_spec)
sys.modules[_spec.name]=previous
_spec.loader.exec_module(previous)

OUT=HERE / "out"
RESULTS=HERE / "results"
BIN=OUT / "seedsolve"
PARAMS=dict(wmin=12,wmax=22,keep=4,samples=64,budget=20000,restarts=12,threshold=-5.10)
STRATA=("exact","one","two","random")


def seed(kind,tag,i):
    return int.from_bytes(hashlib.sha256(f"25|{kind}|{tag}|{i}".encode()).digest()[:8],"big")


def dump(path,value): previous.dump(path,value)
def sha(path): return previous.sha(path)


def build():
    previous.check_build()
    OUT.mkdir(exist_ok=True); RESULTS.mkdir(exist_ok=True)
    subprocess.run(["cc","-O3","-march=native","-o",str(BIN),str(HERE / "seedsolve.c"),"-lm"],check=True)
    m=dict(params=PARAMS,source_sha256=sha(HERE / "seedsolve.c"),driver_sha256=sha(__file__),
           expand_source_sha256=sha(HERE / "expand.py"),binary_sha256=sha(BIN),
           expanded_sha256=sha(OUT / "expanded.bin"),expanded_manifest=json.loads((HERE / "expanded-manifest.json").read_text()),
           previous_manifest_sha256=sha(S24 / "build-manifest.json"))
    dump(HERE / "build-manifest.json",m)


def check_build():
    previous.check_build()
    m=json.loads((HERE / "build-manifest.json").read_text())
    assert m["params"]==PARAMS
    for field,path in [("source",HERE / "seedsolve.c"),("driver",Path(__file__)),("expand_source",HERE / "expand.py"),
                       ("binary",BIN),("expanded",OUT / "expanded.bin"),("previous_manifest",S24 / "build-manifest.json")]:
        assert m[field+"_sha256"]==sha(path),f"{field} changed"
    return m


def call(args):
    p=subprocess.run([str(BIN)]+list(map(str,args)),cwd=previous.S21,capture_output=True,text=True,check=True)
    return [json.loads(s) for s in p.stdout.splitlines() if s.startswith("{")],p.stderr


def swap_distance(a,b):
    inv=[0]*len(a)
    for i,v in enumerate(a): inv[v]=i
    p=[inv[v] for v in b]
    seen=set(); cycles=0
    for i in range(len(p)):
        if i not in seen:
            cycles+=1
            while i not in seen: seen.add(i); i=p[i]
    return len(a)-cycles


def min_distance(k,records):
    return min(swap_distance(r["key"],k) for r in records if len(r["key"])==len(k))


def make_plant(tag,stratum,i):
    rng=random.Random(seed("plant",tag,f"{stratum}:{i}"))
    records=json.loads((S24 / "out/keys.json").read_text())
    w2=rng.randint(18,28)
    same=[r for r in records if len(r["key"])==w2]
    for _ in range(10000):
        if stratum=="random":
            k2=rng.sample(range(w2),w2); base=None
            md=min_distance(k2,same)
            if md>3: break
        else:
            d={"exact":0,"one":1,"two":2}[stratum]
            base=rng.choice(same); k2=list(base["key"])
            pos=rng.sample(range(w2),2*d)
            for a,b in zip(pos[::2],pos[1::2]): k2[a],k2[b]=k2[b],k2[a]
            md=min_distance(k2,same)
            if md==d: break
    else: raise RuntimeError("cannot draw the specified distance stratum")
    w1=rng.randint(12,22)
    pt=previous.run21.plaintext.telegram(615,rng,"es","telegraph")
    k1=rng.sample(range(w1),w1)
    return pt,k1,k2,md,None if base is None else base["id"]


def pipeline(ct,tag,w1):
    check_build()
    work=OUT / tag; work.mkdir(exist_ok=True)
    cf=work / "ct.txt"; cf.write_text(ct)
    p=PARAMS
    shortlist,err=call(["scanbin",cf,OUT / "expanded.bin",w1,0,p["keep"],p["samples"],seed("scan",tag,0)])
    cost=json.loads(err.strip().splitlines()[-1])
    assert cost["keys"]==1286188 and len(shortlist)==p["keep"]
    dump(work / "shortlist.json",shortlist)
    readings=[]; best=None
    for i,cand in enumerate(shortlist):
        got,_=call(["seed",cf,cand["k2"],w1,1,p["budget"],p["restarts"],seed("refine",tag,i)])
        r=got[-1]; previous.check_reading(ct,r)
        r.update(seed_id=cand["id"],seed_k2=cand["k2"],seed_z=cand["z"])
        readings.append(r)
        if best is None or r["score"]>best["score"]: best=r
        if best["score"]>p["threshold"]: break
    dump(work / "readings.json",readings)
    result=dict(tag=tag,n=len(ct),first_width_hypothesis=w1,params=p,build_id=sha(HERE / "build-manifest.json"),
                scan=cost,seeds_tried=len(readings),best=best,candidate=best["score"]>p["threshold"],
                cpu=round(cost["cpu"]+sum(r["cpu"] for r in readings),3))
    dump(work / "result.json",result)
    return result


def control_one(job):
    tag,stratum,i=job
    pt,k1,k2,md,base=make_plant(tag,stratum,i)
    ct=previous.transpo.double_enc(pt,k1,k2)
    r=pipeline(ct,f"{tag}_{stratum}_{i}",len(k1))
    got=r["best"]["pt"]
    acc=previous.run21.shift_acc(got,pt)
    ss=json.loads((OUT / r["tag"] / "shortlist.json").read_text())
    same_length=[previous.parse_key(x["k2"]) for x in ss if x["w2"]==len(k2)]
    r.update(stratum=stratum,trial=i,plant_w1=len(k1),plant_w2=len(k2),min_list_swap_distance=md,
             min_expanded_swap_distance=max(0,md-1),
             base_id=base,acc=round(acc,4),acc_inplace=round(sum(a==b for a,b in zip(got,pt))/615,4),
             exact=got==pt,recovered=acc>=.95,plaintext_sha256=hashlib.sha256(pt.encode()).hexdigest(),
             true_key_shortlisted=any(previous.parse_key(x["k2"])==k2 for x in ss),
             min_retained_swap_distance=min((swap_distance(k,k2) for k in same_length),default=None))
    return r


def controls(tag,n,workers):
    check_build(); previous.run21.load_words("es")
    path=RESULTS / f"{tag}.jsonl"
    if path.exists(): raise SystemExit("result exists; choose a fresh tag")
    with ThreadPoolExecutor(workers) as pool,path.open("w") as f:
        jobs=[(tag,s,i) for s in STRATA for i in range(n)]
        futures=[pool.submit(control_one,j) for j in jobs]
        for future in as_completed(futures):
            try: r=future.result()
            except BaseException:
                for pending in futures: pending.cancel()
                raise  # Preserve the incomplete file. Never replace a failed/capped plant.
            f.write(json.dumps(r)+"\n"); f.flush()
            print(f"{r['stratum']} {r['trial']} {r['plant_w1']}x{r['plant_w2']} acc={r['acc']} "
                  f"exact={r['exact']} retained={r['true_key_shortlisted']} cpu={r['cpu']}",flush=True)


def verify():
    check_build()
    assert swap_distance([0,1,2,3],[0,1,2,3])==0
    assert swap_distance([0,1,2,3],[1,0,2,3])==1
    assert swap_distance([0,1,2,3],[1,0,3,2])==2
    rng=random.Random(25)
    path=OUT / "verify_ct.txt"
    for _ in range(100):
        n=rng.randint(100,700); pt="".join(rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(n))
        a,b=rng.randint(12,22),rng.randint(18,28)
        k1,k2=rng.sample(range(a),a),rng.sample(range(b),b)
        path.write_text(previous.transpo.double_enc(pt,k1,k2))
        p=subprocess.check_output([str(BIN),"decrypt",str(path),",".join(map(str,k1)),",".join(map(str,k2)),"CC"],text=True)
        assert p.strip()==pt
    print("100/100 independent transformation checks; swap-distance examples pass")


def target(tag,workers):
    protocol=json.loads((HERE / "protocol.json").read_text())
    assert protocol["build"]==check_build()
    path=RESULTS / protocol["control_file"]
    assert sha(path)==protocol["control_sha256"]
    cr=[json.loads(l) for l in path.read_text().splitlines()]
    bid=sha(HERE / "build-manifest.json")
    assert len(cr)==40 and all(r["params"]==PARAMS and r["build_id"]==bid for r in cr)
    assert all(not r["candidate"] or r["recovered"] for r in cr), "false candidate in controls"
    assert protocol["required_strata"]==["exact","one"]
    for s in STRATA:
        rr=[r for r in cr if r["stratum"]==s]
        assert sorted(r["trial"] for r in rr)==list(range(10))
        if s in protocol["required_strata"]:
            assert sum(r["recovered"] for r in rr)>=8
    ct="".join(c for c in (HERE.parent.parent / "sources/telegram-1.txt").read_text().upper() if "A"<=c<="Z")
    assert len(ct)==615 and hashlib.sha256(ct.encode()).hexdigest().startswith("e266615d")
    noise=list(ct); random.Random(seed("shuffle",tag,0)).shuffle(noise)
    path=RESULTS / f"{tag}.jsonl"
    if path.exists(): raise SystemExit("result exists; choose a fresh tag")
    def one(job):
        body,text,w=job
        r=pipeline(text,f"{tag}_{body}_{w}",w); r["body"]=body
        return r
    jobs=[(body,text,w) for body,text in [("T1",ct),("T1-shuffle","".join(noise))] for w in range(12,23)]
    with ThreadPoolExecutor(workers) as pool,path.open("w") as f:
        for future in as_completed([pool.submit(one,j) for j in jobs]):
            r=future.result(); f.write(json.dumps(r)+"\n"); f.flush()
            print(f"{r['body']} w1={r['first_width_hypothesis']} score={r['best']['score']} "
                  f"candidate={r['candidate']} cpu={r['cpu']}",flush=True)


def summary(tag):
    rr=[json.loads(x) for x in (RESULTS / f"{tag}.jsonl").read_text().splitlines()]
    for s in STRATA:
        ss=[r for r in rr if r.get("stratum")==s]
        if ss: print(s,len(ss),"recovered",sum(r["recovered"] for r in ss),"exact",sum(r["exact"] for r in ss),
                     "cpu",round(sum(r["cpu"] for r in ss),3))
    for body in ["T1","T1-shuffle"]:
        ss=[r for r in rr if r.get("body")==body]
        if ss: print(body,"widths",len(ss),"best",max(r["best"]["score"] for r in ss),"candidates",sum(r["candidate"] for r in ss),
                     "cpu",round(sum(r["cpu"] for r in ss),3))


if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="build": build()
    elif cmd=="verify": verify()
    elif cmd=="controls": controls(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
    elif cmd=="target": target(sys.argv[2],int(sys.argv[3]))
    elif cmd=="summary": summary(sys.argv[2])
    else: raise SystemExit("unknown command")
