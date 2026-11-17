"""Join two repeat starts when a new exact anchor uses values from both."""
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache

import v3_seed
import v4_islands
from v3_seed import align


@dataclass(frozen=True)
class Start:
    key: tuple
    origins: frozenset


def compatible(left, right):
    return all(left[sign] == value for sign, value in right.items() if sign in left)


def beam_search(cipher, plain, seeds, log):
    n, m = len(cipher), plain.length

    @lru_cache(maxsize=4096)
    def measure(signature):
        key = dict(signature)
        matches = tuple(x for x in v3_seed.exact_matches(cipher, key, plain.positions, minimum=7)
                        if abs(x.start/n - x.left/m) <= .22)
        score, _ = v3_seed.chain(matches, n, m)
        return score, matches

    def rank(start):
        return measure(start.key)[0], len(start.origins), -len(start.key)

    choices = []
    per_origin = defaultdict(int)
    for _, _, sig, witnesses in seeds:
        origin = tuple(i for i, _, _ in witnesses)
        if per_origin[origin] < 8:
            choices.append(Start(sig, frozenset((origin,))))
            per_origin[origin] += 1
        if len(choices) == 192:
            break
    frontier = sorted(choices, key=rank, reverse=True)[:40]
    for round_no in range(1, 6):
        next_start = {s.key: s for s in frontier}
        for start in frontier:
            left = dict(start.key)
            score_left = measure(start.key)[0]
            for seed in choices:
                if seed.origins & start.origins:
                    continue
                right = dict(seed.key)
                right_only, left_only = right.keys() - left.keys(), left.keys() - right.keys()
                if not right_only or not left_only or not compatible(left, right):
                    continue
                signature = tuple(sorted((left | right).items()))
                if signature in next_start:
                    continue
                score, matches = measure(signature)
                if score <= max(score_left, measure(seed.key)[0]):
                    continue
                for match in matches:
                    signs = set(cipher[match.start:match.stop])
                    if signs & right_only and signs & left_only:
                        next_start[signature] = Start(signature, start.origins | seed.origins)
                        break
        ranked = sorted(next_start.values(), key=rank, reverse=True)
        grown = ranked[:40]
        log(f"merge round {round_no}: candidates {len(ranked)}, best signs {len(grown[0].key)}, "
            f"best origins {len(grown[0].origins)}, best exact score {rank(grown[0])[0]}")
        if [x.key for x in frontier] == [x.key for x in grown]:
            break
        frontier = grown
    return frontier


def build(cipher_path, plain_path, log):
    units, text, _, lac, _ = align.load_pair(cipher_path, plain_path)
    plain = v4_islands.Plain(text, [i for i, cut in enumerate(lac) if cut])
    cipher = v3_seed.symbols(units)
    candidates = v3_seed.seed_candidates(cipher, text, plain.lacunae)
    seeds = v3_seed.rank_seeds(cipher, text, plain.positions, candidates)
    if not seeds:
        return []
    frontier = beam_search(cipher, plain, seeds, log)
    best = max((v4_islands.extend(cipher, plain, s.key) for s in frontier[:20]), key=lambda s: s[:2])
    exact, _, key, inferred, confirmed = best
    log(f"chosen exact {exact}, provisional values {len(key)}, new multi-sign locks {len(inferred)}")
    rows = []
    for sign, value in sorted(key.items()):
        locked, conflict = inferred.get(sign, (0, 0))
        support = max(len(confirmed[sign]), locked)
        share = support / max(1, support+conflict)
        status = "certain" if support >= 5 and share >= .8 else "probable" if support >= 3 and share >= .75 else "unknown"
        rows.append(dict(unit=sign, value=value, type=align.unit_type(value), support=support,
                         conflict=conflict, share=round(share, 3), status=status, alts="", positions=""))
    return rows
