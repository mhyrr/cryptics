"""Seed from recurring spans and extend using exact locks. See bench README."""
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "line"))
import align
import v1_gap

VOWELS = frozenset("aeiou")
# The bench checks the group rule before the first scored run.
POOL_GROUPS = False


def symbols(units):
    return [u.sym if u.kind == "sign" and not u.doubt and u.sym != "?" else None for u in units]


def near_repeats(cipher):
    """Return substitutions in five fixed neighbours, and independently witnessed deletions."""
    pairs = set()
    for left, right in ((2, 3), (3, 2)):
        buckets = defaultdict(set)
        for i in range(left, len(cipher) - right):
            block = cipher[i-left:i+right+1]
            if None not in block:
                buckets[tuple(block[:left] + block[left+1:])].add(cipher[i])
        for middle in buckets.values():
            pairs.update(combinations(sorted(middle), 2))

    plain_flanks = {tuple(cipher[i:i+6]) for i in range(len(cipher) - 5)}
    deletions = defaultdict(set)
    for i in range(3, len(cipher) - 3):
        flanks = tuple(cipher[i-3:i] + cipher[i+1:i+4])
        if None not in flanks and cipher[i] and flanks in plain_flanks:
            deletions[cipher[i]].add(flanks)
    return sorted(pairs), {sign for sign, contexts in deletions.items() if len(contexts) >= 2}


def groups(cipher, pairs):
    labels = {s: s for s in cipher if s is not None}
    for a, b in pairs:
        left, right = labels[a], labels[b]
        labels = {s: left if g == right else g for s, g in labels.items()}
    sizes = Counter(labels.values())
    counts = Counter(labels[s] for s in cipher if s in labels)
    return labels, sorted(counts[g] for g in sizes if sizes[g] > 1), sum(n for n in sizes.values() if n > 1)


def pieces(text, count):
    """Partitions into letters and open syllables. A prior for seeds only."""
    if count == 0:
        if not text:
            yield ()
        return
    if not count <= len(text) <= 2 * count:
        return
    lengths = [1]
    if len(text) >= 2 and text[0] not in VOWELS and text[1] in VOWELS:
        lengths.append(2)
    for size in lengths:
        for tail in pieces(text[size:], count - 1):
            yield (text[:size],) + tail


def repeats(seq, size, usable):
    index = defaultdict(list)
    for i in range(len(seq) - size + 1):
        span = seq[i:i+size]
        if usable(i, i+size, span):
            index[span].append(i)
    return {span: starts for span, starts in index.items() if starts[-1] - starts[0] >= size}


def seed_candidates(cipher, plain, lacunae):
    n, m = len(cipher), len(plain)
    lacunae = set(lacunae)
    texts = {size: repeats(plain, size, lambda a, b, _: not lacunae.intersection(range(a+1, b)))
             for size in range(5, 17)}
    candidates = {}
    for size in range(5, 9):
        motifs = repeats(tuple(cipher), size, lambda a, b, span: None not in span)
        for motif, starts in motifs.items():
            for length in range(size, 2 * size + 1):
                for span, positions in texts[length].items():
                    witnesses = [
                        (i, k, j, l)
                        for i, k in combinations(starts, 2) if k-i >= size
                        for j, l in combinations(positions, 2) if l-j >= length
                        if abs(i/n - j/m) <= .22 and abs(k/n - l/m) <= .22
                        and l-j <= 2.1 * (k-i) + 10
                        and l-j >= .6 * (k-i) - 10
                    ]
                    for values in pieces(span, size) if witnesses else ():
                        key = dict(zip(motif, values))
                        if any(key[s] != v for s, v in zip(motif, values)):
                            continue
                        signature = tuple(sorted(key.items()))
                        i, k, j, l = min(witnesses, key=lambda w: abs(w[0]/n - w[2]/m) + abs(w[1]/n - w[3]/m))
                        weight = (length, -abs(i/n - j/m) - abs(k/n - l/m))
                        if signature not in candidates or weight > candidates[signature][0]:
                            candidates[signature] = weight, ((i, j, values), (k, l, values))
    return candidates


@dataclass(frozen=True)
class Match:
    start: int
    stop: int
    left: int
    right: int

    @property
    def weight(self):
        return (self.right - self.left - 4) ** 2


def exact_matches(cipher, key, positions, minimum=5):
    n = len(cipher)
    for i, sign in enumerate(cipher):
        if not key.get(sign):
            continue
        block = ""
        for k in range(i, min(n, i+14)):
            value = key.get(cipher[k])
            if value is None:
                break
            block += value
            if len(block) >= minimum:
                starts = positions(block)
                if not starts:
                    break
                for j in starts:
                    yield Match(i, k+1, j, j+len(block))


def chain(matches, n, m):
    """Highest-weight nonoverlapping monotone chain via prefix maxima."""
    starts = [[] for _ in range(n+1)]
    ends = [[] for _ in range(n+1)]
    for match in matches:
        starts[match.start].append(match)
    tree = [(0, None)] * (m+2)
    prev = {}
    best = (0, None)
    for i in range(n+1):
        for total, match in ends[i]:
            j = match.right + 1
            while j < len(tree):
                if total > tree[j][0]:
                    tree[j] = total, match
                j += j & -j
            if total > best[0]:
                best = total, match
        for match in starts[i]:
            j, max_before = match.left + 1, (0, None)
            while j:
                if tree[j][0] > max_before[0]:
                    max_before = tree[j]
                j -= j & -j
            prev[match] = max_before[1]
            ends[match.stop].append((max_before[0] + match.weight, match))
    path = []
    match = best[1]
    while match:
        path.append(match)
        match = prev[match]
    return best[0], path[::-1]


def rank_seeds(cipher, plain, positions, candidates):
    n, m = len(cipher), len(plain)
    ranked = []
    for signature, (prior, seeds) in candidates.items():
        held = {i for start, _, values in seeds for i in range(start, start+len(values))}
        matches = (x for x in exact_matches(cipher, dict(signature), positions)
                   if abs(x.start/n - x.left/m) <= .22
                   and held.isdisjoint(range(x.start, x.stop)))
        score, _ = chain(matches, n, m)
        if score:
            ranked.append((score, prior, signature, seeds))
    return sorted(ranked, reverse=True)


def locks(cipher, plain, key, positions, path, nulls):
    """Lock unique exact flanks with enough fixed letters and one unknown value."""
    n, m = len(cipher), len(plain)
    prefix = [a.stop for a in path]
    suffix = [a.start for a in path]
    for i, sign in enumerate(cipher):
        if sign is None:
            continue
        # Remove this occurrence from the evidence even if the key already values it.
        a, b = i, i+1
        while a and i-a < 6 and key.get(cipher[a-1]):
            a -= 1
        while b < n and b-i <= 6 and key.get(cipher[b]):
            b += 1
        left = "".join(key[cipher[k]] for k in range(a, i))
        right = "".join(key[cipher[k]] for k in range(i+1, b))
        if not left or not right:
            continue
        before = bisect_right(prefix, a) - 1
        after = bisect_left(suffix, b)
        lo = path[before].right if before >= 0 else 0
        hi = path[after].left if after < len(path) else m
        close = before >= 0 and after < len(path) and path[after].start - path[before].stop <= 20
        fixed = len(left + right)
        if fixed < (4 if close else 7):
            continue
        starts = positions(left)
        ends = positions(right)
        begin = bisect_left(starts, lo)
        stop = bisect_right(starts, hi - fixed)
        hits = set()
        for start in starts[begin:stop]:
            if abs(a/n - start/m) > .22:
                continue
            middle = start + len(left)
            first = bisect_left(ends, middle + (sign not in nulls))
            last = bisect_right(ends, min(middle+3, hi-len(right)))
            for end in ends[first:last]:
                hits.add((middle, end))
        if len(hits) == 1:
            j, k = hits.pop()
            yield i, j, k, plain[j:k]


def add_witnesses(key, observations, cipher):
    votes = defaultdict(lambda: defaultdict(set))
    for i, j, k, val in observations:
        votes[cipher[i]][val].add((i, j, k))
    for sign, vals in votes.items():
        if sign in key:
            continue
        ranked = sorted(vals.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        value, witnessed = ranked[0]
        independent = min(len({i for i, j, k in witnessed}), len({j for i, j, k in witnessed}))
        if independent >= 2 and independent >= 2 * sum(len(w) for _, w in ranked[1:]):
            key[sign] = value


def extend(cipher, plain, positions, signature, seeds, nulls):
    key = dict(signature)
    observations = set()
    for i, j, values in seeds:
        for k, val in enumerate(values):
            observations.add((i+k, j, j+len(val), val))
            j += len(val)
    while True:
        matches = (x for x in exact_matches(cipher, key, positions)
                   if abs(x.start/len(cipher) - x.left/len(plain)) <= .22)
        score, path = chain(matches, len(cipher), len(plain))
        for match in path:
            if match.right - match.left < 7:
                continue
            j = match.left
            for i in range(match.start, match.stop):
                val = key[cipher[i]]
                observations.add((i, j, j+len(val), val))
                j += len(val)
        observations.update(locks(cipher, plain, key, positions, path, nulls))
        old = len(key)
        add_witnesses(key, observations, cipher)
        if len(key) == old:
            return score, key, observations


def assess_gaps(units, plain, wb, lac, key, log):
    """Use the learned table in the existing gap model once the start is dense."""
    prior_null = align.P_LEN[0]
    try:
        align.P_LEN[0] = 0.0
        segment = v1_gap.GapSegment(units, plain, wb, lac)
        table = align.Table()
        for sign, val in key.items():
            if val:
                table.add(sign, val, 20)
        for i in range(2):
            new = align.Table()
            likelihood, gapped = segment.estep(table, new)
            log(f"gap pass {i+1}: log likelihood {likelihood:.1f}, gapped units {gapped:.0f}")
            table = new
    finally:
        align.P_LEN[0] = prior_null


def build(cipher_path, plain_path, log):
    units, plain, wb, lac, _ = align.load_pair(cipher_path, plain_path)
    cipher = symbols(units)
    pairs, nulls = near_repeats(cipher)
    labels, occurrences, grouped = groups(cipher, pairs)
    log(f"group rule: pairs {len(pairs)}, signs {grouped}, group frequencies {occurrences}; pooled {POOL_GROUPS}")
    log(f"null rule: {len(nulls)} signs witnessed in two contexts")
    if POOL_GROUPS:
        cipher = [labels.get(s, s) for s in cipher]
        nulls = {labels[s] for s in nulls}
    lacunae = [i for i, cut in enumerate(lac) if cut]

    @lru_cache(maxsize=32768)
    def positions(block):
        out = []
        j = plain.find(block)
        while j >= 0:
            p = bisect_right(lacunae, j)
            if p == len(lacunae) or lacunae[p] >= j+len(block):
                out.append(j)
            j = plain.find(block, j+1)
        return out

    clear = [u.text for u in units if u.kind == "clear"]
    log(f"clear units {len(clear)}; uniquely present in print {sum(len(positions(w)) == 1 for w in clear)}")
    candidates = seed_candidates(cipher, plain, lacunae)
    ranked = rank_seeds(cipher, plain, positions, candidates)
    log(f"repeat seed segmentations {len(candidates)}; corroborated beyond seed {len(ranked)}")
    if not ranked:
        return []
    starts = [extend(cipher, plain, positions, signature, seeds, nulls)
              for _, _, signature, seeds in ranked[:32]]
    support, key, observations = max(starts, key=lambda x: (x[0], len(x[1])))
    good = {(i, j, k, val) for i, j, k, val in observations if key.get(cipher[i]) == val}
    counts = Counter(cipher)
    frequent = {s for s, n in counts.items() if s is not None and n >= 10}
    log(f"best chain score {support}; valued signs {len(key)}; valued frequent {len(frequent & key.keys())} / {len(frequent)}; locked observations {len(good)}")
    if len(frequent & key.keys()) > len(frequent) / 2:
        assess_gaps(units, plain, wb, lac, key, log)
    # Keep one vote per cipher position. A tie across positions in the print adds no evidence.
    placed = defaultdict(set)
    for i, j, k, val in observations:
        placed[i].add((j, k, val))
    path = [(units[i], j, k, val) for i, spans in sorted(placed.items()) if len(spans) == 1
            for j, k, val in spans]
    return align.key_from_path(path)


if __name__ == "__main__":
    units, _, _ = align.parse_cipher(Path(sys.argv[1]).read_text(encoding="utf-8"))
    pairs, _ = near_repeats(symbols(units))
    print("left\tright")
    for left, right in pairs:
        print(left, right, sep="\t")
