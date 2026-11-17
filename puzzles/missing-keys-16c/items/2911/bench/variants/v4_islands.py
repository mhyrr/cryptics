"""Extend a sparse seed through stretches with several unresolved signs."""
from collections import Counter, defaultdict
from functools import lru_cache
import math

import v3_seed
from v3_seed import Match, align


def indices(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


class Plain:
    def __init__(self, text, lacunae=()):
        self.text = text
        self.length = len(text)
        self.lacunae = tuple(lacunae)
        self.all = (1 << (self.length + 1)) - 1
        self.cuts = sum(1 << cut for cut in self.lacunae)

    @lru_cache(maxsize=32768)
    def positions(self, value):
        starts = []
        j = self.text.find(value)
        while j >= 0:
            if not any(j < cut < j + len(value) for cut in self.lacunae):
                starts.append(j)
            j = self.text.find(value, j + 1)
        return starts

    @lru_cache(maxsize=32768)
    def starts(self, value):
        return sum(1 << j for j in self.positions(value))

    def move(self, mask, value, reverse=False):
        if value is None:
            if reverse:
                return (mask >> 1) | ((mask >> 2) & ~(self.cuts >> 1))
            return ((mask << 1) | ((mask & ~(self.cuts >> 1)) << 2)) & self.all
        if reverse:
            return (mask >> len(value)) & self.starts(value)
        return (mask & self.starts(value)) << len(value)

    def placements(self, span, start_mask, end_mask):
        """The start/end pairs surviving the entire span, without enumerating paths."""
        for stop in indices(end_mask):
            mask = 1 << stop
            for value in reversed(span):
                mask = self.move(mask, value, reverse=True)
                if not mask:
                    break
            for start in indices(mask & start_mask):
                yield start, stop

    def observations(self, span, start, stop):
        """Yield unresolved positions whose text agrees across all paths."""
        forward = [1 << start]
        for value in span:
            forward.append(self.move(forward[-1], value))
        right = 1 << stop
        for index in range(len(span) - 1, -1, -1):
            value = span[index]
            if value is None:
                candidates = {
                    self.text[j:j+length]
                    for length in (1, 2)
                    for j in indices((right >> length) & forward[index])
                    if length == 1 or not (self.cuts & (1 << (j+1)))
                }
                if len(candidates) == 1:
                    yield index, candidates.pop()
            right = self.move(right, value, reverse=True) & forward[index]


def window(n, m, i, stop, anchors):
    if not anchors:
        width = math.ceil(.22 * m)
        return max(0, round(i*m/n) - width), min(m, round(i*m/n) + width)
    before = next((a for a in reversed(anchors) if a.stop <= i), None)
    after = next((a for a in anchors if a.start >= stop), None)
    return before.right if before else 0, after.left if after else m


def islands(cipher, plain, key, anchors=()):
    emissions = [key.get(s) for s in cipher]
    n, m = len(cipher), plain.length
    for i, first in enumerate(emissions):
        if first is None:
            continue
        low, high = window(n, m, i, i+1, ())
        start_mask = plain.starts(first) & ((1 << (high + 1)) - (1 << low))
        ends = start_mask << len(first)
        fixed, unknown = len(first), 0
        best = {}
        for k in range(i+1, min(n, i+19)):
            value = emissions[k]
            ends = plain.move(ends, value)
            if not ends:
                break
            if value is None:
                unknown += 1
                if unknown > 7:
                    break
                continue
            fixed += len(value)
            if fixed < 6:
                continue
            lo, hi = window(n, m, i, k+1, anchors)
            if hi < lo:
                continue
            possible_starts = start_mask & ~((1 << lo) - 1)
            possible_ends = ends & ((1 << (hi + 1)) - 1)
            if not 0 < possible_ends.bit_count() <= 4:
                continue
            found = list(plain.placements(emissions[i:k+1], possible_starts, possible_ends))
            if len(found) != 1:
                continue
            left, right = found[0]
            if any(left < cut < right for cut in plain.lacunae):
                continue
            match = Island(i, k+1, left, right, fixed, unknown)
            best[unknown] = match
        yield from best.values()


class Island(Match):
    def __init__(self, start, stop, left, right, fixed, unknown):
        super().__init__(start, stop, left, right)
        self.fixed = fixed
        self.unknown = unknown

    @property
    def weight(self):
        return (self.fixed - 4) ** 2 * 4 // (self.unknown + 1)


def unanimous_votes(cipher, plain, key, matches):
    seen = defaultdict(set)
    emissions = [key.get(s) for s in cipher]
    for match in matches:
        for offset, value in plain.observations(emissions[match.start:match.stop],
                                                match.left, match.right):
            i = match.start + offset
            if cipher[i] is not None:
                seen[i].add(value)
    votes = defaultdict(lambda: defaultdict(set))
    for i, values in seen.items():
        if len(values) == 1:
            votes[cipher[i]][values.pop()].add(i)
    return votes


def extend(cipher, plain, signature):
    key = dict(signature)
    support = {}
    for _ in range(12):
        candidates = list(islands(cipher, plain, key))
        _, anchors = v3_seed.chain(candidates, len(cipher), plain.length)
        positions = set(anchors)
        # Use overlapping locks only when their ordering agrees with the chain.
        for match in islands(cipher, plain, key, anchors):
            if any(match.start < a.stop and a.start < match.stop
                   and (match.left >= a.right or match.right <= a.left) for a in anchors):
                continue
            positions.add(match)
        votes = unanimous_votes(cipher, plain, key, positions)
        proposals = {}
        for sign, values in votes.items():
            options = sorted(values.items(), key=lambda kv: (-len(kv[1]), kv[0]))
            value, places = options[0]
            total = sum(map(len, values.values()))
            if len(places) >= 3 and 4 * len(places) >= 3 * total:
                proposals[sign] = value
                support[sign] = len(places), total - len(places)
        if not proposals:
            break
        key.update(proposals)
    score, _ = v3_seed.chain(islands(cipher, plain, key), len(cipher), plain.length)
    matches = [match for match in v3_seed.exact_matches(cipher, key, plain.positions, minimum=7)
               if abs(match.start / len(cipher) - match.left / plain.length) <= .22]
    exact, chain = v3_seed.chain(matches, len(cipher), plain.length)
    confirmations = defaultdict(set)
    for match in chain:
        for i in range(match.start, match.stop):
            confirmations[cipher[i]].add(i)
    return exact, score, key, support, confirmations


def build(cipher_path, plain_path, log):
    units, text, _, lac, _ = align.load_pair(cipher_path, plain_path)
    plain = Plain(text, [i for i, cut in enumerate(lac) if cut])
    cipher = v3_seed.symbols(units)
    candidates = v3_seed.seed_candidates(cipher, text, plain.lacunae)
    shortlist = v3_seed.rank_seeds(cipher, text, plain.positions, candidates)[:32]
    best = None
    for rank, (_, _, signature, _) in enumerate(shortlist, 1):
        trial = extend(cipher, plain, signature)
        exact, score, key, votes, confirmed = trial
        log(f"seed rank {rank}: initial {len(signature)}, final {len(key)}, exact {exact}, island {score}")
        if best is None or trial[:2] > best[:2]:
            best = trial
    if best is None:
        return []
    exact, score, key, votes, confirmed = best
    log(f"chosen exact {exact}, island {score}, values {len(key)}, independently added {len(votes)}")
    rows = []
    for sign, value in sorted(key.items()):
        support, conflict = votes.get(sign, (0, 0))
        support = max(support, len(confirmed[sign]))
        share = support / max(1, support + conflict)
        status = "certain" if support >= 5 and share >= .8 else "probable" if support >= 3 and share >= .75 else "unknown"
        rows.append(dict(unit=sign, value=value, type=align.unit_type(value), support=support, conflict=conflict,
                         share=round(share, 3), status=status, alts="", positions=""))
    return rows


def synthetic():
    plain = Plain("xabpcdymnabrxy")
    span = ["ab", None, None, "dy"]
    assert list(plain.placements(span, 1 << 1, 1 << 7)) == [(1, 7)]
    assert dict(plain.observations(span, 1, 7)) == {2: "c", 1: "p"}
    assert dict(Plain("abcdxyzgh").observations(["abcd", None, None, "gh"], 0, 9)) == {}
    plain = Plain("qwertyuvabdefg")
    truncated = ["qw", "er", None, None, "uv"]
    assert dict(plain.observations(truncated, 0, 8)) == {2: "t", 3: "y"}
    plain = Plain("abcde", (2,))
    assert not (plain.move(1 << 1, None) & (1 << 3))
    print("Multi-sign lock controls passed")


if __name__ == "__main__":
    synthetic()
