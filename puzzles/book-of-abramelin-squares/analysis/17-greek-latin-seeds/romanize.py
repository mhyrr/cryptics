#!/usr/bin/env python3
"""Frozen romanization of the dictionary's Greek glosses. See PROTOCOL.md.

One Greek word gives a small closed set of Latin-letter spellings, the ways a
German compiler around 1600 could plausibly write it. Nothing is fitted.
"""
import itertools, unicodedata

BASE = {"α": "A", "β": "B", "γ": "G", "δ": "D", "ε": "E", "ζ": "Z", "η": "E", "θ": "TH",
        "ι": "I", "κ": "K", "λ": "L", "μ": "M", "ν": "N", "ξ": "X", "ο": "O", "π": "P",
        "ρ": "R", "σ": "S", "ς": "S", "τ": "T", "υ": "Y", "φ": "PH", "χ": "CH", "ψ": "PS",
        "ω": "O", "ϊ": "I", "ϋ": "Y"}
ROUGH = "̔"
# Ligature and variant code points the OCR emits, mapped to plain letters first.
FOLD = {"ϐ": "β", "ϑ": "θ", "ϕ": "φ", "ϖ": "π", "ϰ": "κ", "ϱ": "ρ", "ϲ": "σ", "ϛ": "στ", "ȣ": "ου"}
MAX_VARIANTS = 32


def letters(word):
    """Lower-case base letters, and whether the word opens with a rough breathing."""
    d = unicodedata.normalize("NFD", word.lower())
    rough = False
    seen_letter = 0
    out = []
    for ch in d:
        if ch == ROUGH and seen_letter <= 2:
            rough = True
        if unicodedata.combining(ch):
            continue
        ch = FOLD.get(ch, ch)
        for c in ch:
            if c in BASE:
                out.append(c)
                seen_letter += 1
            else:
                return None, False          # a non-Greek character: not a clean Greek word
    return "".join(out), rough


def variants(word):
    """All frozen spellings of one Greek word, upper case A-Z."""
    base, rough = letters(word)
    if not base or len(base) < 3:
        return set()
    slots, i = [], 0
    while i < len(base):
        two = base[i:i + 2]
        c = base[i]
        if two == "ου":
            slots.append(("OU", "U")); i += 2; continue
        if two in ("γγ", "γκ", "γξ", "γχ"):
            slots.append(("N", "G")); i += 1; continue
        if c == "υ":
            slots.append(("Y", "U"))
        elif c == "κ":
            slots.append(("K", "C"))
        elif c == "φ":
            slots.append(("PH", "F"))
        else:
            slots.append((BASE[c],))
        i += 1
    out = set()
    for combo in itertools.islice(itertools.product(*slots), MAX_VARIANTS):
        w = "".join(combo)
        out.add(w)
        if rough:
            out.add("H" + w)
    return out


if __name__ == "__main__":
    import sys
    for w in sys.argv[1:]:
        print(w, sorted(variants(w)))
