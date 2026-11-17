"""Find longer starts by testing variable-width substitution inside one window."""
from collections import Counter, defaultdict
from dataclasses import dataclass
import re

import v3_seed
import v4_islands
from v3_seed import align


# One encrypted symbol is normally a letter or an open syllable.
ATOM = r"(?:[a-z]|[b-df-hj-np-tv-z][aeiou])"
WINDOWS = ((18, 6), (22, 7), (26, 8), (30, 10))


def crib_pattern(cipher):
    counts = Counter(cipher)
    groups = {}
    parts = []
    for symbol in cipher:
        if symbol is None or counts[symbol] == 1:
            parts.append(ATOM)
        elif symbol in groups:
            parts.append(f"(?P={groups[symbol]})")
        else:
            name = f"g{len(groups)}"
            groups[symbol] = name
            parts.append(f"(?P<{name}>{ATOM})")
    return re.compile("(?=" + "".join(parts) + ")")


def segment(cipher, plain, start, limit):
    """Enumerate maps for the matches found by the regular expression."""
    table = {}

    def visit(i, j):
        if i == len(cipher):
            yield j, tuple(sorted(table.items()))
            return
        sign = cipher[i]
        known = table.get(sign)
        if known is not None:
            if j + len(known) <= limit and plain.startswith(known, j):
                yield from visit(i+1, j+len(known))
            return
        if j >= limit:
            return
        lengths = [1]
        if j+1 < limit and plain[j] not in v3_seed.VOWELS and plain[j+1] in v3_seed.VOWELS:
            lengths.append(2)
        for length in lengths:
            if sign is not None:
                table[sign] = plain[j:j+length]
            yield from visit(i+1, j+length)
        if sign is not None:
            del table[sign]

    yield from visit(0, start)


@dataclass(frozen=True)
class Crib:
    start: int
    stop: int
    left: int
    right: int


def cribs(cipher, plain):
    n, m = len(cipher), plain.length
    candidates = {}
    cuts = [0, *plain.lacunae, m]
    for size, minimum in WINDOWS:
        last_use = defaultdict(lambda: -size)
        for i in range(n-size+1):
            block = cipher[i:i+size]
            counts = Counter(s for s in block if s)
            repeats = sum(n-1 for n in counts.values())
            if repeats < minimum or block.count(None) > size // 5:
                continue
            recurrent = tuple(sorted((s, n) for s, n in counts.items() if n > 1))
            if i - last_use[recurrent] < size // 3:
                continue
            last_use[recurrent] = i
            pattern = crib_pattern(block)
            lo = max(0, int((i/n - .22) * m))
            hi = min(m, int((i/n + .22) * m) + 1)
            for left, right in zip(cuts, cuts[1:]):
                if hi < left or lo + size > right:
                    continue
                for match in pattern.finditer(plain.text, max(left, lo), min(right, hi+2*size)):
                    start = match.start()
                    if start > hi:
                        break
                    for end, signature in segment(block, plain.text, start, right):
                        if signature not in candidates:
                            candidates[signature] = Crib(i, i+size, start, end)
    return candidates


def external_matches(cipher, plain, key, crib, minimum=6):
    n, m = len(cipher), plain.length
    for match in v3_seed.exact_matches(cipher, key, plain.positions, minimum):
        if abs(match.start/n - match.left/m) > .22:
            continue
        if match.stop <= crib.start and match.right <= crib.left:
            yield match
        if match.start >= crib.stop and match.left >= crib.right:
            yield match


def shortlist(cipher, plain, candidates):
    ranked = []
    for signature, crib in candidates.items():
        key = dict(signature)
        score, chain = v3_seed.chain(external_matches(cipher, plain, key, crib), len(cipher), plain.length)
        if score:
            evidence = {i for m in chain for i in range(m.start, m.stop)}
            ranked.append((score, len(evidence), signature, crib))
    return sorted(ranked, key=lambda row: row[:2], reverse=True)


def rows_from_key(cipher, plain, key, crib, inferred):
    matches = list(external_matches(cipher, plain, key, crib))
    score, chain = v3_seed.chain(matches, len(cipher), plain.length)
    supports = defaultdict(set)
    for match in chain:
        for i in range(match.start, match.stop):
            supports[cipher[i]].add(i)
    rows = []
    for sign, value in sorted(key.items()):
        external = len(supports[sign])
        learned, conflict = inferred.get(sign, (0, 0))
        support = max(external, learned)
        share = support / max(1, support+conflict)
        status = "certain" if support >= 5 and share >= .8 else "probable" if support >= 3 and share >= .75 else "unknown"
        rows.append(dict(unit=sign, value=value, type=align.unit_type(value), support=support,
                         conflict=conflict, share=round(share, 3), status=status, alts="", positions=""))
    return score, rows


def build(cipher_path, plain_path, log):
    units, text, _, lac, _ = align.load_pair(cipher_path, plain_path)
    plain = v4_islands.Plain(text, [i for i, cut in enumerate(lac) if cut])
    cipher = v3_seed.symbols(units)
    candidates = cribs(cipher, plain)
    log(f"crib maps {len(candidates)}")
    ranked = shortlist(cipher, plain, candidates)
    log(f"crib maps with external evidence {len(ranked)}")
    best_score, best_rows = 0, []
    for rank, (_, _, seed, crib) in enumerate(ranked[:24], 1):
        _, _, key, inferred, _ = v4_islands.extend(cipher, plain, seed)
        score, rows = rows_from_key(cipher, plain, key, crib, inferred)
        marked = sum(row["status"] != "unknown" for row in rows)
        log(f"rank {rank}: seed {len(seed)}, extended {len(key)}, marked {marked}, external score {score}")
        if score > best_score:
            best_score, best_rows = score, rows
    return best_rows


def synthetic():
    cipher = tuple("abaca")
    plain = "xzpacopaspaycap"
    match = crib_pattern(cipher).search(plain)
    assert match.start() == 2
    values = list(segment(cipher, plain, match.start(), len(plain)))
    assert (11, (("a", "pa"), ("b", "co"), ("c", "s"))) in values
    assert crib_pattern(cipher).search("abcdefghijkl") is None
    assert not list(segment(cipher, "abcdefghijkl", 0, 12))
    print("Repeated-sign crib controls passed")


if __name__ == "__main__":
    synthetic()
