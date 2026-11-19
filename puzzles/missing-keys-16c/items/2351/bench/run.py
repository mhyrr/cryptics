"""run.py - build a table for the real pair with a variant. Prints counts only, never values.

    python3 run.py <variant> <label> [--set NAME=value ...]
Writes runs/<label>.key.tsv (holds values: not checked in, not to be quoted) and runs/<label>.log.
It does not score. Register the run in README.md first, then `python3 score.py runs/<label>.key.tsv <label>`.
"""
import importlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "variants"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
import align  # noqa: E402

CIPHER, PLAIN = os.path.join(HERE, "inputs", "cipher-A.txt"), os.path.join(HERE, "inputs", "plain-A.txt")


def main():
    variant, label = sys.argv[1], sys.argv[2]
    mod = importlib.import_module(variant)
    for k, a in enumerate(sys.argv):
        if a == "--set":
            name, _, val = sys.argv[k + 1].partition("=")
            setattr(mod, name, type(getattr(mod, name))(val))
    logs = []
    rows = mod.build(CIPHER, PLAIN, logs.append)
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    align.write_key(rows, os.path.join(HERE, "runs", label + ".key.tsv"))
    toks = [t for ln in open(CIPHER) if not ln.startswith("#") for t in ln.split() if t != "?"]
    kinds = set(toks)
    marked = {r["unit"] for r in rows if r["status"] in ("certain", "probable")}
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    logs.append(f"rows by status {st}; marked rows that are signs of the cipher text {len(marked & kinds)} of "
                f"{len(marked)}; with a vowel mark {sum('+' in s for s in marked)}; places they cover "
                f"{sum(t in marked for t in toks)} of {len(toks)}")
    open(os.path.join(HERE, "runs", label + ".log"), "w").write("\n".join(logs) + "\n")
    print("\n".join(logs))


if __name__ == "__main__":
    main()
