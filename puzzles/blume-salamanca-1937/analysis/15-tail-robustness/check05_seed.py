"""Does 05's control start its solver at the true key? No solving here; this only replays the seed streams.

05-periodic/periodic.py (job, kind "plant") and nihilist_control.py (one) draw the plant key as
random.Random(seed).sample(range(n), n), then call periodic.solve(texts, n, seed). solve seeds its own
generator with random.Random(seed) and draws its first restart as rnd.sample(range(n), n): the same call on
the same stream. This script replays both scripts' seed streams and counts how often the first restart
equals the planted key.
Usage (from this folder): python3 -I check05_seed.py > check05-seed.txt
"""
import random


def first_restart(seed, n):
    return random.Random(seed).sample(range(n), n)  # periodic.solve, first restart


def main():
    # periodic.py main(): master Random(20261016); per n, two plant seeds then two target seeds.
    rnd = random.Random(20261016); same = tot = 0
    for n in range(2, 41):
        for _ in range(2):
            s = rnd.randrange(10 ** 9); same += random.Random(s).sample(range(n), n) == first_restart(s, n); tot += 1
        rnd.randrange(10 ** 9); rnd.randrange(10 ** 9)
    print(f"05 periodic.py plants: first restart == planted key in {same}/{tot}")
    # nihilist_control.py main(): master Random(7); one seed per (n, joint).
    rnd = random.Random(7); same = tot = 0
    for n in range(5, 41):
        for _ in (False, True):
            s = rnd.randrange(10 ** 9); same += random.Random(s).sample(range(n), n) == first_restart(s, n); tot += 1
    print(f"05 nihilist_control.py plants: first restart == planted key in {same}/{tot}")
    print("15 run.py draws plant and solver seeds separately from its master stream, so this does not occur there.")


if __name__ == "__main__":
    main()
