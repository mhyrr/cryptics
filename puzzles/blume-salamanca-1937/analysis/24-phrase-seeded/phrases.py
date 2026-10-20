"""Fixed contextual key guesses. None is an attested historical key.

Sources for the entities: ../../sources/context-cribs.md and headers.md.
Compound phrases, both tie directions, and spelling variants are search assumptions.
"""
import hashlib
import itertools
import json
from pathlib import Path
import unicodedata

HERE = Path(__file__).resolve().parent
PEOPLE = ["OSWALD", "VIKTOR", "VICTOR", "WERNER", "BLUME", "VIKTOR OSWALD",
          "VICTOR OSWALD", "WERNER OSWALD", "W E OSWALD", "DR ING W E OSWALD"]
PLACES = ["SALAMANCA", "BURGOS", "ZURICH", "ZUERICH", "MADRID", "SEVILLA", "SEVILLE",
          "SAN SEBASTIAN", "SUIZA", "SCHWEIZ", "ESPANA", "SPANIEN", "BAHNHOFSTRASSE"]
FIRMS = ["PATVAG", "HOVAG", "HISMA", "RO WAK", "EMSER WERKE", "BAHNHOFSTRASSE ZWOLF",
         "BAHNHOFSTRASSE DOCE", "BUREAU BAHNHOFSTRASSE"]
TRADE = ["LANAS", "NEGOCIO DE LANAS", "COMPRA DE LANAS", "EXPORTACION DE LANAS",
         "CREDITOS SUIZOS", "CREDITOS DE EXPORTACION", "OFICINA EN ESPANA",
         "OFICINA DE BURGOS", "COMPENSACION", "FRANCOS SUIZOS", "WOLLGESCHAEFT",
         "WOLLGESCHAFT", "SCHWEIZER EXPORTKREDITE", "EXPORTGUTHABEN", "SCHWEIZER WOLLE"]


def normalize(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s).upper() if "A" <= c <= "Z")


def rank(s, reverse_ties=False):
    order = sorted(range(len(s)), key=lambda i: (s[i], -i if reverse_ties else i))
    key = [0] * len(s)
    for r, i in enumerate(order):
        key[i] = r
    return tuple(key)


def build():
    # Fixed templates, not permutations of an unlimited vocabulary. One to three contextual components.
    guesses = set(PEOPLE + PLACES + FIRMS + TRADE)
    for a, b in itertools.product(PEOPLE + PLACES + FIRMS + TRADE, repeat=2):
        if a != b:
            guesses.add(a + " " + b)
    for person, place, firm in itertools.product(PEOPLE, PLACES, FIRMS):
        for parts in ((person, place, firm), (firm, person, place), (place, firm, person)):
            guesses.add(" ".join(parts))
    keys = {}
    for phrase in sorted(guesses):
        s = normalize(phrase)
        if not 8 <= len(s) <= 32:
            continue
        for reverse in (False, True):
            k = rank(s, reverse)
            keys.setdefault(k, dict(phrase=phrase, normalized=s, ties="right" if reverse else "left"))
    return [dict(id=i, key=list(k), **keys[k]) for i, k in enumerate(sorted(keys))]


def main():
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    records = build()
    active = [r for r in records if 18 <= len(r["key"]) <= 28]
    raw = "".join(f"{r['id']}\t{','.join(map(str, r['key']))}\n" for r in active)
    (out / "keys.tsv").write_text(raw)
    (out / "keys.json").write_text(json.dumps(records, ensure_ascii=False, indent=1) + "\n")
    manifest = dict(keys=len(records), active_keys=len(active), active_lengths=[18,28], keys_sha256=hashlib.sha256(raw.encode()).hexdigest(),
                    by_length={str(n): sum(len(r["key"]) == n for r in records) for n in range(8, 33)},
                    assumptions="contextual guesses, not attested keys; stable alphabetic ranks, both tie directions")
    (HERE / "candidate-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest))


if __name__ == "__main__":
    main()
