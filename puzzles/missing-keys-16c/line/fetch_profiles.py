"""fetch_profiles.py - pull every targets/<name>/profile.json from Bourdeau's public repository.

    python3 fetch_profiles.py ../sources/cache/bourdeau-profiles-<date>.json [--tree tree.json]

Lists the repository tree (GitHub API, one call), then fetches each profile from
raw.githubusercontent.com, 16 at a time. Output: a JSON map {path: text}, the input of taken.py.
The tree is also saved (--tree) so a later run can see which targets are new.
No credentials and no personal details are sent.
"""
import json, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

REPO = "dbourdeau/cyphersolver"
UA = {"User-Agent": "cryptics-research-script"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def main(out, tree_out=None):
    tree = json.loads(get(f"https://api.github.com/repos/{REPO}/git/trees/main?recursive=1"))
    if tree.get("truncated"):
        print("warning: tree listing truncated", file=sys.stderr)
    paths = sorted(t["path"] for t in tree["tree"]
                   if t["path"].startswith("targets/") and t["path"].endswith("/profile.json")
                   and t["path"].count("/") == 2)
    if tree_out:
        json.dump([t["path"] for t in tree["tree"] if t["path"].startswith("targets/") and t["path"].count("/") == 1],
                  open(tree_out, "w"), indent=0)

    def fetch(p):
        try:
            return p, get(f"https://raw.githubusercontent.com/{REPO}/main/{p}")
        except Exception as e:
            return p, None

    with ThreadPoolExecutor(16) as ex:
        got = dict(ex.map(fetch, paths))
    failed = [p for p, t in got.items() if t is None]
    json.dump({p: t for p, t in got.items() if t is not None}, open(out, "w"), ensure_ascii=False)
    print(f"# {len(paths)} profiles listed, {len(paths) - len(failed)} fetched, {len(failed)} failed", file=sys.stderr)
    for p in failed:
        print("failed", p, file=sys.stderr)


if __name__ == "__main__":
    a = sys.argv[1:]
    tree_out = a[a.index("--tree") + 1] if "--tree" in a else None
    main(a[0], tree_out)
