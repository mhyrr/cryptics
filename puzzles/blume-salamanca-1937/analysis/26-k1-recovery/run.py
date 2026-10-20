"""Frozen, bounded K1-stage experiment; no target before both control gates.

python3 -I run.py build | verify | development
python3 -I run.py isolated iso26 3
python3 -I run.py controls holdout26 3
python3 -I run.py target target26 3
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
S25=HERE.parent / "25-seed-retention"
spec=importlib.util.spec_from_file_location("blume25",S25 / "run.py")
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
previous=old.previous
OUT=HERE / "out"
RESULTS=HERE / "results"
BIN=OUT / "seedsolve"
EXPANDED=S25 / "out/expanded.bin"
PARAMS=dict(old.PARAMS)
BANDS={"low":(12,15),"middle":(16,18),"high":(19,22)}
ISO_STRATA=(*BANDS,"wrong-width","shuffle")


def seed(kind,tag,index):
    return int.from_bytes(hashlib.sha256(f"26|{kind}|{tag}|{index}".encode()).digest()[:8],"big")


sha=old.sha
dump=old.dump


def build():
    old.check_build()
    OUT.mkdir(exist_ok=True); RESULTS.mkdir(exist_ok=True)
    subprocess.run(["cc","-O3","-march=native","-o",str(BIN),str(HERE / "seedsolve.c"),"-lm"],check=True)
    manifest=dict(params=PARAMS,source_sha256=sha(HERE / "seedsolve.c"),driver_sha256=sha(__file__),
                  binary_sha256=sha(BIN),parent_manifest_sha256=sha(S25 / "build-manifest.json"),
                  expanded_sha256=sha(EXPANDED),engine_sha256=sha(HERE.parent / "21-dc-method/dcm.c"),
                  cpu_caps_seconds=dict(scan=180,refinement_process=60),k1_neighbourhood="full",
                  k2_quad_neighbourhood="stochastic",retained_seed_stop="all four, no score stop")
    dump(HERE / "build-manifest.json",manifest)


def check_build():
    old.check_build()
    m=json.loads((HERE / "build-manifest.json").read_text())
    assert m["params"]==PARAMS
    for field,path in [("source",HERE / "seedsolve.c"),("driver",Path(__file__)),("binary",BIN),
                       ("parent_manifest",S25 / "build-manifest.json"),("expanded",EXPANDED),
                       ("engine",HERE.parent / "21-dc-method/dcm.c")]:
        assert sha(path)==m[field+"_sha256"],f"{field} changed"
    return m


def call(args):
    process=subprocess.run([str(BIN)]+list(map(str,args)),cwd=previous.S21,
                           capture_output=True,text=True,check=True)
    return [json.loads(s) for s in process.stdout.splitlines() if s.startswith("{")],process.stderr


def locked(ct,k2,w1,tag):
    check_build()
    work=OUT / tag; work.mkdir(exist_ok=True)
    cf=work / "ct.txt"; cf.write_text(ct)
    readings,_=call(["locked",cf,",".join(map(str,k2)),w1,0,PARAMS["budget"],PARAMS["restarts"],seed("locked",tag,0)])
    best=readings[-1]
    previous.check_reading(ct,best)
    assert previous.parse_key(best["k2"])==k2, "locked mode changed supplied K2"
    result=dict(tag=tag,n=len(ct),first_width_hypothesis=w1,best=best,cpu=best["cpu"],
                candidate=best["score"]>PARAMS["threshold"],params=PARAMS,
                build_id=sha(HERE / "build-manifest.json"))
    dump(work / "result.json",result)
    return result


def metrics(result,pt):
    got=result["best"]["pt"]
    acc=previous.run21.shift_acc(got,pt)
    result.update(acc=round(acc,4),acc_inplace=round(sum(a==b for a,b in zip(got,pt))/len(pt),4),
                  exact=got==pt,recovered=acc>=.95,plaintext_sha256=hashlib.sha256(pt.encode()).hexdigest())
    return result


def isolated_plant(tag,stratum,i):
    rng=random.Random(seed("isolated-plant",tag,f"{stratum}:{i}"))
    lo,hi=BANDS.get(stratum,(12,22))
    w1,w2=rng.randint(lo,hi),rng.randint(18,28)
    pt=previous.run21.plaintext.telegram(615,rng,"es","telegraph")
    k1,k2=rng.sample(range(w1),w1),rng.sample(range(w2),w2)
    ct=previous.transpo.double_enc(pt,k1,k2)
    stated=w1
    if stratum=="wrong-width": stated=rng.choice([w for w in range(12,23) if w!=w1])
    if stratum=="shuffle":
        noise=list(ct); rng.shuffle(noise); ct="".join(noise)
    return pt,k1,k2,ct,stated


def isolated_one(job):
    tag,stratum,i=job
    pt,k1,k2,ct,stated=isolated_plant(tag,stratum,i)
    result=metrics(locked(ct,k2,stated,f"{tag}_{stratum}_{i}"),pt)
    result.update(stratum=stratum,trial=i,positive=stratum in BANDS,plant_w1=len(k1),plant_w2=len(k2))
    return result


def make_plant(tag,stratum,i):
    # Same minimum-distance distribution as25, independent26 seed stream.
    rng=random.Random(seed("plant",tag,f"{stratum}:{i}"))
    records=json.loads((previous.HERE / "out/keys.json").read_text())
    w2=rng.randint(18,28)
    same=[r for r in records if len(r["key"])==w2]
    for _ in range(10000):
        if stratum=="random":
            k2=rng.sample(range(w2),w2); base=None
            md=old.min_distance(k2,same)
            if md>3: break
        else:
            d={"exact":0,"one":1,"two":2}[stratum]
            base=rng.choice(same); k2=list(base["key"])
            pos=rng.sample(range(w2),2*d)
            for a,b in zip(pos[::2],pos[1::2]): k2[a],k2[b]=k2[b],k2[a]
            md=old.min_distance(k2,same)
            if md==d: break
    else: raise RuntimeError("cannot sample distance stratum")
    w1=rng.randint(12,22)
    pt=previous.run21.plaintext.telegram(615,rng,"es","telegraph")
    k1=rng.sample(range(w1),w1)
    return pt,k1,k2,md,None if base is None else base["id"]


def pipeline(ct,tag,w1):
    check_build()
    work=OUT / tag; work.mkdir(exist_ok=True)
    cf=work / "ct.txt"; cf.write_text(ct)
    p=PARAMS
    shortlist,err=call(["scanbin",cf,EXPANDED,w1,0,p["keep"],p["samples"],seed("scan",tag,0)])
    cost=json.loads(err.strip().splitlines()[-1])
    assert cost["keys"]==1286188 and len(shortlist)==p["keep"]
    dump(work / "shortlist.json",shortlist)
    readings=[]
    for i,cand in enumerate(shortlist):
        got,_=call(["seed",cf,cand["k2"],w1,1,p["budget"],p["restarts"],seed("refine",tag,i)])
        r=got[-1]; previous.check_reading(ct,r)
        r.update(seed_id=cand["id"],seed_k2=cand["k2"],seed_z=cand["z"])
        readings.append(r)
    best=max(readings,key=lambda r:r["score"])
    dump(work / "readings.json",readings)
    result=dict(tag=tag,n=len(ct),first_width_hypothesis=w1,params=p,build_id=sha(HERE / "build-manifest.json"),
                scan=cost,seeds_tried=len(readings),best=best,candidate=best["score"]>p["threshold"],
                cpu=round(cost["cpu"]+sum(r["cpu"] for r in readings),3))
    dump(work / "result.json",result)
    return result


def control_one(job):
    tag,stratum,i=job
    pt,k1,k2,md,base=make_plant(tag,stratum,i)
    result=metrics(pipeline(previous.transpo.double_enc(pt,k1,k2),f"{tag}_{stratum}_{i}",len(k1)),pt)
    shortlist=json.loads((OUT / result["tag"] / "shortlist.json").read_text())
    retained=[previous.parse_key(x["k2"]) for x in shortlist]
    same=[k for k in retained if len(k)==len(k2)]
    result.update(stratum=stratum,trial=i,plant_w1=len(k1),plant_w2=len(k2),min_list_swap_distance=md,
                  min_expanded_swap_distance=max(0,md-1),base_id=base,
                  true_key_shortlisted=k2 in retained,
                  min_retained_swap_distance=min((old.swap_distance(k,k2) for k in same),default=None))
    return result


def batch(tag,strata,fn,workers):
    check_build(); previous.run21.load_words("es")
    assert 1<=workers<=3
    path=RESULTS / f"{tag}.jsonl"
    if path.exists(): raise SystemExit("existing results cannot be overwritten")
    with ThreadPoolExecutor(workers) as pool,path.open("w") as f:
        futures=[pool.submit(fn,(tag,s,i)) for s in strata for i in range(10)]
        for future in as_completed(futures):
            try: r=future.result()
            except BaseException:
                for pending in futures: pending.cancel()
                raise
            f.write(json.dumps(r)+"\n"); f.flush()
            print(f"{r['stratum']} {r['trial']} acc={r['acc']} exact={r['exact']} "
                  f"score={r['best']['score']} candidate={r['candidate']} cpu={r['cpu']}",flush=True)


def gate(tag,isolated):
    rr=[json.loads(s) for s in (RESULTS / f"{tag}.jsonl").read_text().splitlines()]
    strata=ISO_STRATA if isolated else old.STRATA
    expected={(s,i) for s in strata for i in range(10)}
    assert len(rr)==len(expected) and {(r["stratum"],r["trial"]) for r in rr}==expected,"incomplete batch"
    assert all(r["build_id"]==sha(HERE / "build-manifest.json") and r["params"]==PARAMS for r in rr)
    required=BANDS if isolated else ("exact","one")
    assert all(sum(r["recovered"] for r in rr if r["stratum"]==s)>=8 for s in required),"recovery gate failed"
    assert not any(r["candidate"] and (not r["recovered"] or (isolated and not r["positive"])) for r in rr),"false candidate"
    return rr


def development():
    previous.run21.load_words("es")
    pt,k1,k2,_,_=old.make_plant("holdout25","two",8)
    path=RESULTS / "development.json"
    if path.exists(): raise SystemExit("development result already exists")
    result=metrics(locked(previous.transpo.double_enc(pt,k1,k2),k2,len(k1),"development_old25_two8"),pt)
    result.update(role="assisted development; true K2 and width supplied",old_stratum="two",old_trial=8)
    dump(path,result)
    print(json.dumps(result),flush=True)


def target(tag,workers):
    protocol=json.loads((HERE / "protocol.json").read_text())
    assert protocol["build"]==check_build()
    for field,is_iso in [("isolated",True),("controls",False)]:
        info=protocol[field]
        assert sha(RESULTS / (info["tag"]+".jsonl"))==info["sha256"]
        gate(info["tag"],is_iso)
    ct="".join(c for c in (HERE.parent.parent / "sources/telegram-1.txt").read_text().upper() if "A"<=c<="Z")
    assert len(ct)==615 and hashlib.sha256(ct.encode()).hexdigest().startswith("e266615d")
    noise=list(ct); random.Random(seed("shuffle",tag,0)).shuffle(noise)
    path=RESULTS / f"{tag}.jsonl"
    if path.exists(): raise SystemExit("existing results cannot be overwritten")
    assert 1<=workers<=3
    jobs=[(body,text,w) for body,text in [("T1",ct),("T1-shuffle","".join(noise))] for w in range(12,23)]
    def one(job):
        body,text,w=job
        r=pipeline(text,f"{tag}_{body}_{w}",w); r["body"]=body
        return r
    with ThreadPoolExecutor(workers) as pool,path.open("w") as f:
        for future in as_completed([pool.submit(one,j) for j in jobs]):
            r=future.result(); f.write(json.dumps(r)+"\n"); f.flush()
            print(f"{r['body']} w1={r['first_width_hypothesis']} score={r['best']['score']} "
                  f"candidate={r['candidate']} cpu={r['cpu']}",flush=True)


def verify():
    check_build()
    rng=random.Random(26)
    for _ in range(100):
        n=rng.randint(100,700); a,b=rng.randint(12,22),rng.randint(18,28)
        pt="".join(rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(n))
        k1,k2=rng.sample(range(a),a),rng.sample(range(b),b)
        cf=OUT / "verify_ct.txt"; cf.write_text(previous.transpo.double_enc(pt,k1,k2))
        got=subprocess.check_output([str(BIN),"decrypt",str(cf),",".join(map(str,k1)),",".join(map(str,k2)),"CC"],text=True)
        assert got.strip()==pt
    print("100/100 independent C/Python transposition checks")


if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="build": build()
    elif cmd=="verify": verify()
    elif cmd=="development": development()
    elif cmd=="isolated": batch(sys.argv[2],ISO_STRATA,isolated_one,int(sys.argv[3]))
    elif cmd=="controls":
        plan=json.loads((HERE / "control-plan.json").read_text())
        gate(plan["isolated_tag"],True)
        batch(sys.argv[2],old.STRATA,control_one,int(sys.argv[3]))
    elif cmd=="target": target(sys.argv[2],int(sys.argv[3]))
    else: raise SystemExit("unknown command")
