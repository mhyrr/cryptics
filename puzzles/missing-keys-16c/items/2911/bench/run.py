"""run.py - run one aligner variant on the frozen 2911 pair and score its table against the period key.

    python3 run.py <variant> [p1|full] [--plain print|consensus] [--note <label for a parameter trial>]
variant: a module in variants/ with build(cipher_path, plain_path, log) -> key rows (align.py's row dicts).
p1 (default): the first page of V/140 (33 lines) and the printed text up to where that page ends. full: all.
Writes runs/<variant>-<subset>.key.tsv (HOLDS VALUES), .log, and appends one row to runs/results.tsv
(no values): variant, subset, plain, seconds, then score.py's measures.
"""
import importlib, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "variants"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
import align, score  # noqa: E402


def main():
    a = sys.argv[1:]
    variant = a[0]
    subset = a[1] if len(a) > 1 and not a[1].startswith("--") else "p1"
    plain_kind = a[a.index("--plain") + 1] if "--plain" in a else "print"
    cipher = os.path.join(HERE, "inputs", f"cipher-{subset}.txt")
    plain = os.path.join(HERE, "inputs", f"plain-{subset}.txt" if plain_kind == "print" else "plain-consensus.txt")
    note = a[a.index("--note") + 1] if "--note" in a else ""
    tag = f"{variant}-{subset}" + ("" if plain_kind == "print" else "-consensus") + ("-" + note if note else "")
    logf = open(os.path.join(HERE, "runs", tag + ".log"), "w")
    log = lambda s: (logf.write(s + "\n"), logf.flush())
    t0 = time.time()
    rows = importlib.import_module(variant).build(cipher, plain, log)
    secs = time.time() - t0
    kp = os.path.join(HERE, "runs", tag + ".key.tsv")
    align.write_key(rows, kp)
    res = score.score(kp, cipher)
    head = ["variant", "note", "subset", "plain", "seconds"] + [k for k, _ in res]
    line = [variant, note, subset, plain_kind, f"{secs:.0f}"] + [str(v) for _, v in res]
    rp = os.path.join(HERE, "runs", "results.tsv")
    new = not os.path.exists(rp)
    with open(rp, "a") as f:
        if new:
            f.write("\t".join(head) + "\n")
        f.write("\t".join(line) + "\n")
    for h, v in zip(head, line):
        print(f"{h}\t{v}")


if __name__ == "__main__":
    main()
