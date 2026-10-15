"""check_b engine: direct dynamic programming over L/R words from the definition (state: heading h, per-label
usage counts, number of L's so far), for small n only."""
def dp_row(m, n):
    total = m * (n + 1); cap = n + 1
    # first symbol L: h 0 -> 1, label 1
    start = [0] * m; start[1 % m] = 1
    states = {(1 % m, tuple(start), 1): 1}
    for step in range(1, total):
        new = {}
        for (h, cnt, nl), w in states.items():
            # L: label h+1, h -> h+1
            lab = (h + 1) % m
            if cnt[lab] < cap:
                c = list(cnt); c[lab] += 1; key = (lab, tuple(c), nl + 1)
                new[key] = new.get(key, 0) + w
            # R: label h, h -> h-1
            if cnt[h] < cap:
                c = list(cnt); c[h] += 1; key = ((h - 1) % m, tuple(c), nl)
                new[key] = new.get(key, 0) + w
        states = new
    row = [0] * (n + 1)
    for (h, cnt, nl), w in states.items():
        if nl % m == 0 and nl >= m: row[nl // m - 1] += w
    return row
