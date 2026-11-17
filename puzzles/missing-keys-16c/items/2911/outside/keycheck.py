"""keycheck.py - the registered outside check of ../README.md section 5: score ../key-v1.tsv against truth.tsv.

    python3 keycheck.py   -> keycheck.tsv (three measures and the per-unit comparison; HOLDS VALUES)

A key row's unit (`a+o`) is looked up in truth.tsv by its joined form. Right: same letters after the aligner's
normalisation (u/v, i/j merged) for a letter, syllable, word or name; a null is right if the sheet gives a null.
A key unit that truth.tsv has no sheet sign for (type none, or absent) is counted apart, in neither the numerator
nor the denominator. Measure 3 counts the truth.tsv signs (single names and sequences) that occur ten times or
more in ../work/cipher-primary.txt as decoded by decode.py; a sequence (`a a`) can only be right in the key if
the key has that sequence as a unit, which key-v1.tsv, built on single tokens, cannot.
"""
import os, sys, csv, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decode

truth = {r["unit"]: r for r in csv.DictReader(open(os.path.join(HERE, "truth.tsv"), encoding="utf-8"), delimiter="\t")}
key = list(csv.DictReader(open(os.path.join(HERE, "..", "key-v1.tsv"), encoding="utf-8"), delimiter="\t"))
rows, tally = [], collections.Counter()
kv = {}
for k in key:
    t = truth.get(k["unit"])
    kv[k["unit"]] = k
    if k["unit"] == "?" or t is None or t["type"] == "none":
        verdict = "apart (not a sheet sign)"
    else:
        right = decode.norm(k["value"]) == decode.norm(t["value"]) and (k["value"] == "") == (t["type"] == "null")
        verdict = "right" if right else "wrong"
    tally[(k["status"], verdict)] += 1
    rows.append((k["unit"], k["status"], k["type"], k["value"] or "(null)", t["value"] or "(null)" if t and t["type"] != "none" else "-", verdict))
def share(statuses):
    r = sum(tally[(s, "right")] for s in statuses); w = sum(tally[(s, "wrong")] for s in statuses)
    return r, r + w, (r / (r + w) if r + w else float("nan"))
items = [it for row in decode.decode_file(os.path.join(HERE, "..", "work", "cipher-primary.txt"), decode.load_truth()) for it in row]
cnt = collections.Counter(" ".join(it["names"]).replace("^", "+") for it in items if it["type"] not in ("clear", "unread", "missing"))
freq = [u for u, n in cnt.items() if n >= 10]
def has_right(u, statuses):
    k = kv.get(u)
    if not k or k["status"] not in statuses:
        return False
    t = truth[u]
    return decode.norm(k["value"]) == decode.norm(t["value"]) and (k["value"] == "") == (t["type"] == "null")
out = ["measure\tright\tof\tshare\tbar\tmet"]
r, n, s = share(["certain"]); out.append("values marked certain that agree with VI/82\t%d\t%d\t%.3f\t0.95\t%s" % (r, n, s, "yes" if s >= 0.95 else "no"))
r, n, s = share(["certain", "probable"]); out.append("values marked certain or probable that agree\t%d\t%d\t%.3f\t0.85\t%s" % (r, n, s, "yes" if s >= 0.85 else "no"))
r = sum(has_right(u, ("certain", "probable")) for u in freq)
out.append("VI/82 signs occurring ten times or more that key-v1 has right\t%d\t%d\t%.3f\t0.75\t%s" % (r, len(freq), r / len(freq), "yes" if r / len(freq) >= 0.75 else "no"))
single = [u for u in freq if " " not in u]
r = sum(has_right(u, ("certain", "probable")) for u in single)
out.append("  same, single-token signs only (not registered)\t%d\t%d\t%.3f\t-\t-" % (r, len(single), r / len(single)))
out.append("# key rows counted apart (unit is not a sheet sign): %d of %d" % (sum(v for (s, vd), v in tally.items() if vd.startswith("apart")), len(key)))
out.append("# per unit")
out.append("unit\tstatus\tkey_type\tkey_value\ttruth_value\tverdict")
out += ["\t".join(r) for r in rows]
open(os.path.join(HERE, "keycheck.tsv"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out[:6]))
