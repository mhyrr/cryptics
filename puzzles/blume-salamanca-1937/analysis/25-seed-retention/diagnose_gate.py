"""Explain failed acceptance controls without invoking a solver or changing settings.

python3 -I diagnose_gate.py
Reconstructs only synthetic controls from the frozen generator. This is a
post-search diagnostic, never fresh calibration or a target result.
"""
import array
import hashlib
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("retention25",HERE / "run.py")
run=importlib.util.module_from_spec(spec)
spec.loader.exec_module(run)


def main():
    run.check_build()
    run.previous.run21.load_words("es")
    path=HERE / "results/holdout25.jsonl"
    rows=[json.loads(line) for line in path.read_text().splitlines()]
    q=array.array("f")
    q.frombytes((HERE.parent / "21-dc-method/out/lm_es_4.bin").read_bytes())
    def score(pt):
        values=[ord(c)-65 for c in pt]
        return sum(q[((a*26+b)*26+c)*26+d] for a,b,c,d in
                   zip(values,values[1:],values[2:],values[3:]))/(len(values)-3)
    failed=[]
    for r in rows:
        if not r["candidate"] or r["recovered"]: continue
        pt,k1,k2,_,_=run.make_plant("holdout25",r["stratum"],r["trial"])
        assert hashlib.sha256(pt.encode()).hexdigest()==r["plaintext_sha256"]
        ct=run.previous.transpo.double_enc(pt,k1,k2)
        run.previous.check_reading(ct,r["best"])
        a,b=run.previous.parse_key(r["best"]["k1"]),run.previous.parse_key(r["best"]["k2"])
        assert abs(score(r["best"]["pt"])-r["best"]["score"])<.0001
        failed.append(dict(stratum=r["stratum"],trial=r["trial"],widths=[len(k1),len(k2)],
                           score=r["best"]["score"],true_plaintext_score=round(score(pt),6),
                           candidate=r["candidate"],recovered=r["recovered"],acc=r["acc"],
                           acc_inplace=r["acc_inplace"],seeds_tried=r["seeds_tried"],
                           second_key_exact=b==k2,first_key_exact=a==k1,
                           true_plaintext=pt,returned_plaintext=r["best"]["pt"]))
    result=dict(control_sha256=run.sha(path),build_id=run.sha(HERE / "build-manifest.json"),
                false_candidates=failed,target_run=False,
                interpretation="Post-search diagnostic only. No threshold, budget, control or target change.")
    run.dump(HERE / "results/gate-diagnostic.json",result)
    print(json.dumps(result,indent=2))


if __name__=="__main__": main()
