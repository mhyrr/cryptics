"""Record descriptive timings from existing result/cache files, never run a search.

python3 -I timing.py
File timestamps approximate pipeline elapsed time (ct write to result write),
excluding plant construction and initial input hashing. They depend on this run's
host/filesystem load. They are not portable algorithm benchmarks or work limits.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def main():
    batches=[]
    for tag in ("holdout26","target26"):
        path=HERE / "results" / f"{tag}.jsonl"
        if not path.exists(): continue
        rows=[json.loads(s) for s in path.read_text().splitlines()]
        timings=[]
        for r in rows:
            work=HERE / "out" / r["tag"]
            if not (work / "ct.txt").exists() or not (work / "result.json").exists(): continue
            start=(work / "ct.txt").stat().st_mtime
            end=(work / "result.json").stat().st_mtime
            assert end>=start
            stamp=lambda t:datetime.fromtimestamp(t,timezone.utc).isoformat()
            timings.append(dict(tag=r["tag"],start_utc=stamp(start),end_utc=stamp(end),
                                elapsed_seconds=round(end-start,3),recorded_cpu_seconds=r["cpu"]))
        batches.append(dict(tag=tag,result_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                            rows=len(rows),timings=timings))
    result=dict(scope="Descriptive cache timestamps; excludes prep/hashing. Host load affects elapsed time.",batches=batches)
    (HERE / "results/timing.json").write_text(json.dumps(result,indent=1)+"\n")
    for batch in batches:
        tt=batch["timings"]
        if tt:
            print(batch["tag"],len(tt),"timed completions; elapsed seconds range",
                  min(r["elapsed_seconds"] for r in tt),max(r["elapsed_seconds"] for r in tt))


if __name__=="__main__": main()
