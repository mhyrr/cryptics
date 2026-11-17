"""queue.py - rebuild the class A work queue from a Bourdeau catalogue pull (PIPELINE.md, "The queue").

    python3 queue.py <catalogue.json> [--prev <older catalogue.json>] [--ledger ledger.tsv] > queue.tsv

Keep: cls A; desk-workable (access online, or needs_archive_scan "no"); not reserved; no write-up;
not closed in the ledger (gated-out, walled, key-built, read).
With --prev: the changes since the older pull go to stderr, and items whose status text changed are dropped.
Order: readable language (Spanish, French, Italian, Latin) first; solvability high; difficulty low;
then items whose repository already has a key-built or read ledger row; then id.
Note: this file shadows the standard-library module 'queue' for scripts run from line/. Nothing here needs it.
"""
import argparse, csv, json, os, re, sys
from collections import Counter

CLOSED = {"gated-out", "walled", "key-built", "read"}
DONE = {"key-built", "read"}
READABLE = re.compile(r"spanish|french|italian|latin", re.I)
WATCH = ("status", "outcome", "reserved", "writeup")
COLS = ["rank", "id", "year", "language", "repository", "solvability", "difficulty", "outcome", "title", "shelfmark"]


def load_entries(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    return d["entries"] if isinstance(d, dict) else d


def read_ledger(path):
    """-> list of row dicts; [] if the path is None or the file is missing."""
    if not path:
        return []
    try:
        with open(path, encoding="utf-8", newline="") as f:
            return [r for r in csv.DictReader(f, delimiter="\t") if r.get("id")]
    except FileNotFoundError:
        return []


def readable(lang):
    lang = (lang or "").strip()
    if not lang or lang.lower().startswith("unknown"):
        return False
    return bool(READABLE.search(lang))


def desk(e):
    return e.get("access") == "online" or e.get("needs_archive_scan") == "no"


def candidate(e):
    """Catalogue-side filter (rule 1 without the ledger)."""
    return e.get("cls") == "A" and desk(e) and not e.get("reserved") and not e.get("writeup")


def num(v, default):
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


def build(entries, ledger=(), prev=None, log=None):
    """-> ordered list of kept entries. prev: older entries, or None. log: callable for stderr lines."""
    log = log or (lambda s: None)
    closed = {str(r["id"]).strip() for r in ledger if r.get("status", "").strip() in CLOSED}
    done_repos = {r.get("repository", "").strip() for r in ledger if r.get("status", "").strip() in DONE}
    done_repos.discard("")
    kept = [e for e in entries if candidate(e) and str(e["id"]) not in closed]

    if prev is not None:
        now = {e["id"]: e for e in entries}
        old = {e["id"]: e for e in prev}
        watched = sorted({e["id"] for e in kept} | {e["id"] for e in prev if candidate(e)})
        changed_status = set()
        for i in watched:
            if i not in now:
                log(f"vanished\t{i}\t{old[i].get('title', '')}")
                continue
            if i not in old:
                log(f"new\t{i}\t{now[i].get('title', '')}")
                continue
            for k in WATCH:
                a, b = old[i].get(k), now[i].get(k)
                if a != b:
                    log(f"changed\t{i}\t{k}\t{json.dumps(a, ensure_ascii=False)}\t->\t{json.dumps(b, ensure_ascii=False)}")
                    if k == "status":
                        changed_status.add(i)
        dropped = [e["id"] for e in kept if e["id"] in changed_status]
        if dropped:
            log(f"dropped (status text changed since the older pull): {' '.join(map(str, dropped))}")
        kept = [e for e in kept if e["id"] not in changed_status]

    kept.sort(key=lambda e: (not readable(e.get("language")),
                             -num(e.get("solvability"), 0),
                             num(e.get("difficulty"), 9),
                             (e.get("repository") or "") not in done_repos,
                             num(e.get("id"), 10 ** 9)))
    return kept


def cell(v):
    return "" if v is None else re.sub(r"[\t\r\n]+", " ", str(v))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("catalogue")
    ap.add_argument("--prev")
    ap.add_argument("--ledger", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledger.tsv"),
                    help="default: ledger.tsv beside this script")
    a = ap.parse_args(argv)
    log = lambda s: print(s, file=sys.stderr)
    prev = load_entries(a.prev) if a.prev else None
    q = build(load_entries(a.catalogue), read_ledger(a.ledger), prev, log)
    out = sys.stdout
    out.write("\t".join(COLS) + "\n")
    for k, e in enumerate(q, 1):
        row = dict(e, rank=k)
        out.write("\t".join(cell(row.get(c)) for c in COLS) + "\n")
    log(f"queue: {len(q)} items")
    for repo, n in Counter(e.get("repository") or "" for e in q).most_common():
        log(f"  {repo or '(none)'}\t{n}")


if __name__ == "__main__":
    main()
