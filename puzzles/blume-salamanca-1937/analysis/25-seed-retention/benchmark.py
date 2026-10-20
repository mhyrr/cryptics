"""Benchmark the revised scan on old development ciphertext, never on T1.

Run diagnose.py first to reconstruct out/old_d1_9.txt.
python3 -I benchmark.py   -> results/benchmark.json
Widths are supplied hypotheses; neither result is a fresh blind control.
"""
from concurrent.futures import ThreadPoolExecutor,as_completed
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("blume25",HERE / "run.py")
experiment=importlib.util.module_from_spec(spec)
spec.loader.exec_module(experiment)


def main():
    ct=(HERE / "out/old_d1_9.txt").read_text()
    with ThreadPoolExecutor(2) as pool:
        futures=[pool.submit(experiment.pipeline,ct,f"benchmark25_w{w}",w) for w in (19,22)]
        rows=[]
        for future in as_completed(futures):
            r=future.result(); rows.append(r)
            print(r["first_width_hypothesis"],r["best"]["score"],r["cpu"],flush=True)
    experiment.dump(HERE / "results/benchmark.json",rows)


if __name__=="__main__": main()
