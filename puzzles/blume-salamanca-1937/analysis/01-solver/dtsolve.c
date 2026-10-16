/* dtsolve.c — divide-and-conquer solver for double columnar transposition,
 * after Lasry, Kopal and Wacker (Cryptologia 2014; Lasry thesis 2018, ch. 9.4.5–9.4.6).
 *
 * Keys are rank arrays: key[c] = reading rank of column c (0-based). Columns are
 * read in increasing rank; the first n % w columns are one letter longer.
 * Stage 'C' = write rows, read columns. Stage 'R' = write columns, read rows.
 * conv "CC" is the forward double columnar; "CR" ends with an 'R' stage. The IDP
 * needs the first stage to be 'C', so "RC" and "RR" are not supported here.
 *
 * Build: cc -O3 -march=native -o out/dtsolve dtsolve.c -lm
 * Modes:
 *   dtsolve decrypt CT K1 K2 CONV               (keys as comma ranks) -> plaintext
 *   dtsolve idp CT K2 W1 CONV LANG               -> IDP of a K2 for width W1
 *   dtsolve solve CT W1 W2 CONV LANG SEED SECONDS [PT] [CT2] [PT2]
 *        -> one JSON line per improvement and a final JSON line.
 *        PT (optional) is the true plaintext, used only to report accuracy (controls).
 *        CT2 (optional) is a second ciphertext under the same keys (joint attack);
 *        its IDP and quadgram score are added, weighted by length.
 *   dtsolve bench CT W1 W2 LANG                  -> IDP evaluations per second
 * LANG selects out/lm_<LANG>_2.bin and out/lm_<LANG>_4.bin.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdint.h>

#define MAXN 2048
#define MAXW 64

static float B2[26 * 26];
static float Q4[26 * 26 * 26 * 26];

/* ---------- RNG (xorshift64*) ---------- */
static uint64_t rs = 88172645463325252ULL;
static inline uint64_t rnd64(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline int rndint(int n) { return (int)(rnd64() % (uint64_t)n); }
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }

static void load_lm(const char *lang) {
    char p[256]; FILE *f;
    snprintf(p, sizeof p, "out/lm_%s_2.bin", lang);
    if (!(f = fopen(p, "rb")) || fread(B2, sizeof(float), 26 * 26, f) != 26 * 26) { fprintf(stderr, "cannot read %s\n", p); exit(1); }
    fclose(f);
    snprintf(p, sizeof p, "out/lm_%s_4.bin", lang);
    if (!(f = fopen(p, "rb")) || fread(Q4, sizeof(float), 26 * 26 * 26 * 26, f) != 26 * 26 * 26 * 26) { fprintf(stderr, "cannot read %s\n", p); exit(1); }
    fclose(f);
}

static int read_text(const char *path, unsigned char *out) {
    FILE *f = fopen(path, "r"); if (!f) { fprintf(stderr, "cannot open %s\n", path); exit(1); }
    int n = 0, c;
    while ((c = fgetc(f)) != EOF && n < MAXN) { if (c >= 'a' && c <= 'z') c -= 32; if (c >= 'A' && c <= 'Z') out[n++] = (unsigned char)(c - 'A'); }
    fclose(f); return n;
}

static int parse_key(const char *s, int *key) {
    int w = 0; const char *p = s;
    while (*p) { key[w++] = atoi(p); while (*p && *p != ',') p++; if (*p == ',') p++; }
    return w;
}

/* ---------- transposition stages ---------- */
/* 'C' decryption (inverse of write-rows/read-columns) */
static void col_dec(const unsigned char *in, unsigned char *out, int n, const int *key, int w) {
    int order[MAXW], rows = n / w, ex = n % w, pos = 0;
    for (int c = 0; c < w; c++) order[key[c]] = c;
    for (int k = 0; k < w; k++) {
        int c = order[k], len = rows + (c < ex);
        for (int r = 0; r < len; r++) out[r * w + c] = in[pos++];
    }
}
/* 'C' encryption == 'R' decryption */
static void col_enc(const unsigned char *in, unsigned char *out, int n, const int *key, int w) {
    int order[MAXW], rows = n / w, ex = n % w, pos = 0;
    for (int c = 0; c < w; c++) order[key[c]] = c;
    for (int k = 0; k < w; k++) {
        int c = order[k], len = rows + (c < ex);
        for (int r = 0; r < len; r++) out[pos++] = in[r * w + c];
    }
}
static void undo_stage(char st, const unsigned char *in, unsigned char *out, int n, const int *key, int w) {
    if (st == 'C') col_dec(in, out, n, key, w); else col_enc(in, out, n, key, w);
}

static double quad_score(const unsigned char *t, int n) {
    double s = 0;
    for (int i = 0; i + 3 < n; i++) s += Q4[((t[i] * 26 + t[i + 1]) * 26 + t[i + 2]) * 26 + t[i + 3]];
    return s;
}

/* ---------- IDP (Lasry thesis 9.4.5.2) ----------
 * inter = intermediate text (the K1 ciphertext). Segment k (k-th column read) starts at
 * k*r + m, m = number of long columns among the first k segments, m in
 * [max(0, ex-(w1-k)), min(k, ex)]. B[i][j] = best over starts of the mean bigram
 * log-probability of column j placed right of column i, over r rows.
 * Then greedy: take the best pair, fix i->j, invalidate row i and column j, repeat.
 * Difference from the thesis: we refuse links that would close a cycle, so the result
 * is one path of w1-1 links (it doubles as a K1 seed); the thesis assigns w1 links. */
typedef struct { float v; short i, j; } Pair;
static int cmp_pair(const void *a, const void *b) { float x = ((const Pair *)a)->v, y = ((const Pair *)b)->v; return (x < y) - (x > y); }

static double idp(const unsigned char *inter, int n, int w1, int *chain /* out, may be NULL */) {
    static Pair pairs[MAXW * MAXW];
    int r = n / w1, ex = n % w1, lo[MAXW], hi[MAXW];
    for (int k = 0; k < w1; k++) {
        int mlo = ex - (w1 - k); if (mlo < 0) mlo = 0;
        int mhi = k < ex ? k : ex;
        lo[k] = k * r + mlo; hi[k] = k * r + mhi;
    }
    int np = 0;
    for (int i = 0; i < w1; i++) for (int j = 0; j < w1; j++) {
        if (i == j) continue;
        float best = -1e30f;
        /* diagonals d = b - a; for each, slide a over the allowed run */
        for (int d = lo[j] - hi[i]; d <= hi[j] - lo[i]; d++) {
            int a0 = lo[i] > lo[j] - d ? lo[i] : lo[j] - d;
            int a1 = hi[i] < hi[j] - d ? hi[i] : hi[j] - d;
            if (a0 > a1) continue;
            float s = 0;
            for (int t = 0; t < r; t++) s += B2[inter[a0 + t] * 26 + inter[a0 + d + t]];
            if (s > best) best = s;
            for (int a = a0 + 1; a <= a1; a++) {
                s += B2[inter[a + r - 1] * 26 + inter[a + r - 1 + d]] - B2[inter[a - 1] * 26 + inter[a - 1 + d]];
                if (s > best) best = s;
            }
        }
        pairs[np].v = best / r; pairs[np].i = (short)i; pairs[np].j = (short)j; np++;
    }
    qsort(pairs, np, sizeof(Pair), cmp_pair);
    int right[MAXW], left[MAXW], head[MAXW], tail[MAXW];
    for (int k = 0; k < w1; k++) { right[k] = left[k] = -1; head[k] = tail[k] = k; }
    double sum = 0; int links = 0;
    for (int p = 0; p < np && links < w1 - 1; p++) {
        int i = pairs[p].i, j = pairs[p].j;
        if (right[i] >= 0 || left[j] >= 0) continue;
        /* path endpoints: i must be a tail, j a head, and not of the same path */
        int hi_ = i; while (left[hi_] >= 0) hi_ = left[hi_];
        if (hi_ == j) continue;
        right[i] = j; left[j] = i; sum += pairs[p].v; links++;
    }
    (void)head; (void)tail;
    if (chain) {
        int s = 0; while (left[s] >= 0) s = left[s];
        for (int k = 0; k < w1; k++) { chain[k] = s; s = right[s]; }
    }
    return sum;
}

/* ---------- key moves (on the rank array, as Lasry's segment transformations) ---------- */
static void rotate(int *a, int i, int j, int k) { /* move block a[i..j) to after a[j..k) */
    int tmp[MAXW], t = 0;
    for (int x = j; x < k; x++) tmp[t++] = a[x];
    for (int x = i; x < j; x++) tmp[t++] = a[x];
    for (int x = 0; x < t; x++) a[i + x] = tmp[x];
}
static void random_move(int *key, int w) {
    int type = rndint(4);
    if (w < 3) type = 0;
    if (type == 0) { int i = rndint(w), j = rndint(w); while (j == i) j = rndint(w); int t = key[i]; key[i] = key[j]; key[j] = t; }
    else if (type == 1) { /* segment slide */
        int i = rndint(w - 1), k = i + 2 + rndint(w - i - 1); if (k > w) k = w;
        int j = i + 1 + rndint(k - i - 1); rotate(key, i, j, k);
    } else if (type == 2) { /* segment swap, equal lengths */
        int L = 1 + rndint(w / 2), i = rndint(w - 2 * L + 1), j = i + L + rndint(w - i - 2 * L + 1);
        for (int x = 0; x < L; x++) { int t = key[i + x]; key[i + x] = key[j + x]; key[j + x] = t; }
    } else { /* 3-partite swap */
        int i = rndint(w), j = rndint(w), k = rndint(w);
        while (j == i) j = rndint(w); while (k == i || k == j) k = rndint(w);
        int t = key[i]; key[i] = key[j]; key[j] = key[k]; key[k] = t;
    }
}
static void random_key(int *key, int w) {
    for (int i = 0; i < w; i++) key[i] = i;
    for (int i = w - 1; i > 0; i--) { int j = rndint(i + 1), t = key[i]; key[i] = key[j]; key[j] = t; }
}

/* ---------- problem state ---------- */
typedef struct {
    unsigned char ct[MAXN], ct2[MAXN], pt[MAXN], pt2[MAXN];
    int n, n2, w1, w2, havept, havept2;
    char conv[3];
} Prob;
static Prob P;
static unsigned char inter[MAXN], inter2[MAXN], dec[MAXN], dec2[MAXN];

static double k2_idp(const int *k2) {
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    double s = idp(inter, P.n, P.w1, NULL);
    if (P.n2) { undo_stage(P.conv[1], P.ct2, inter2, P.n2, k2, P.w2); s += idp(inter2, P.n2, P.w1, NULL) * ((double)P.n2 / P.n); }
    return s;
}
/* per-letter quadgram score of the full decryption (both texts, length-weighted) */
static double full_score(const int *k1, const int *k2) {
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    undo_stage(P.conv[0], inter, dec, P.n, k1, P.w1);
    double s = quad_score(dec, P.n); int m = P.n - 3;
    if (P.n2) {
        undo_stage(P.conv[1], P.ct2, inter2, P.n2, k2, P.w2);
        undo_stage(P.conv[0], inter2, dec2, P.n2, k1, P.w1);
        s += quad_score(dec2, P.n2); m += P.n2 - 3;
    }
    return s / m;
}

/* stochastic first-improvement hill climb; stops after `patience` consecutive failures */
typedef double (*ScoreFn)(const int *k, const int *other);
static double climb(int *key, int w, const int *other, ScoreFn f, int patience, double deadline) {
    int cand[MAXW]; double best = f(key, other); int fails = 0;
    while (fails < patience && now() < deadline) {
        memcpy(cand, key, sizeof(int) * w); random_move(cand, w);
        double s = f(cand, other);
        if (s > best) { best = s; memcpy(key, cand, sizeof(int) * w); fails = 0; } else fails++;
    }
    return best;
}
static double f_idp(const int *k2, const int *unused) { (void)unused; return k2_idp(k2); }
static double f_k1(const int *k1, const int *k2) { return full_score(k1, k2); }
static double f_k2(const int *k2, const int *k1) { return full_score(k1, k2); }

/* Lasry's left-to-right improvement: for each i, the best swap with some j > i, if it improves */
static double left_to_right(int *k2, int w) {
    double best = k2_idp(k2);
    for (int i = 0; i < w - 1; i++) {
        int bj = -1;
        for (int j = i + 1; j < w; j++) {
            int t = k2[i]; k2[i] = k2[j]; k2[j] = t;
            double s = k2_idp(k2);
            if (s > best) { best = s; bj = j; }
            t = k2[i]; k2[i] = k2[j]; k2[j] = t;
        }
        if (bj >= 0) { int t = k2[i]; k2[i] = k2[bj]; k2[bj] = t; }
    }
    return best;
}

/* K1 from the IDP chain: chain[c] = segment (reading rank) holding plaintext column c */
static void k1_from_chain(const int *k2, int *k1) {
    int chain[MAXW];
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    idp(inter, P.n, P.w1, chain);
    for (int c = 0; c < P.w1; c++) k1[c] = chain[c];
}

static double accuracy(const int *k1, const int *k2) {
    if (!P.havept) return -1;
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    undo_stage(P.conv[0], inter, dec, P.n, k1, P.w1);
    int ok = 0; for (int i = 0; i < P.n; i++) ok += dec[i] == P.pt[i];
    return (double)ok / P.n;
}

static void print_key(FILE *f, const int *k, int w) { for (int i = 0; i < w; i++) fprintf(f, i ? ",%d" : "%d", k[i]); }

static void report(const char *tag, double t0, long iter, double idpv, double sc, const int *k1, const int *k2) {
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    undo_stage(P.conv[0], inter, dec, P.n, k1, P.w1);
    printf("{\"tag\":\"%s\",\"t\":%.1f,\"iter\":%ld,\"w1\":%d,\"w2\":%d,\"conv\":\"%s\",\"idp\":%.4f,\"score\":%.4f,\"acc\":%.4f,\"k1\":\"",
           tag, now() - t0, iter, P.w1, P.w2, P.conv, idpv, sc, accuracy(k1, k2));
    print_key(stdout, k1, P.w1); printf("\",\"k2\":\""); print_key(stdout, k2, P.w2); printf("\",\"pt\":\"");
    for (int i = 0; i < P.n; i++) putchar('A' + dec[i]);
    printf("\"}\n"); fflush(stdout);
}

/* One full Lasry cycle per iteration (thesis 9.4.6 steps 1-4), repeated until the deadline. */
static void solve(int seconds) {
    double t0 = now(), deadline = t0 + seconds;
    int w1 = P.w1, w2 = P.w2;
    int NRAND = 200, KEEP = 10;           /* step 1: random K2, keep the best KEEP */
    int pat_idp = 3 * w2 * w2, pat_k1 = 4 * w1 * w1, pat_k2 = 3 * w2 * w2;
    int bestk1[MAXW], bestk2[MAXW]; double bestsc = -1e9, bestidp = 0;
    long iter = 0;
    static int pool[64][MAXW]; double pv[64];
    while (now() < deadline) {
        iter++;
        /* step 1 */
        for (int s = 0; s < KEEP; s++) pv[s] = -1e30;
        for (int r = 0; r < NRAND; r++) {
            int k[MAXW]; random_key(k, w2); double v = k2_idp(k);
            int worst = 0; for (int s = 1; s < KEEP; s++) if (pv[s] < pv[worst]) worst = s;
            if (v > pv[worst]) { pv[worst] = v; memcpy(pool[worst], k, sizeof(int) * w2); }
        }
        /* step 2: left-to-right on each, keep the best 3 */
        for (int s = 0; s < KEEP; s++) pv[s] = left_to_right(pool[s], w2);
        for (int a = 0; a < 3; a++) {
            int b = a; for (int s = a + 1; s < KEEP; s++) if (pv[s] > pv[b]) b = s;
            double tv = pv[a]; pv[a] = pv[b]; pv[b] = tv;
            int tk[MAXW]; memcpy(tk, pool[a], sizeof(int) * w2); memcpy(pool[a], pool[b], sizeof(int) * w2); memcpy(pool[b], tk, sizeof(int) * w2);
        }
        /* step 3: hill climb each on IDP, keep the overall best */
        int k2[MAXW]; double bidp = -1e30;
        for (int s = 0; s < 3 && now() < deadline; s++) {
            double v = climb(pool[s], w2, NULL, f_idp, pat_idp, deadline);
            if (v > bidp) { bidp = v; memcpy(k2, pool[s], sizeof(int) * w2); }
        }
        /* step 4a: K1 by hill climbing on quadgrams, seeded from the IDP chain, plus random restarts */
        int k1[MAXW], kk[MAXW]; double sc1 = -1e9;
        k1_from_chain(k2, kk);
        for (int rr = 0; rr < 4 && now() < deadline; rr++) {
            if (rr) random_key(kk, w1);
            double v = climb(kk, w1, k2, f_k1, pat_k1, deadline);
            if (v > sc1) { sc1 = v; memcpy(k1, kk, sizeof(int) * w1); }
            if (rr == 0) k1_from_chain(k2, kk);
        }
        /* step 4b: refine K2 on the full decryption with K1 fixed, then K1 again, until stable */
        double sc = sc1;
        for (int round = 0; round < 6 && now() < deadline; round++) {
            double v2 = climb(k2, w2, k1, f_k2, pat_k2, deadline);
            double v1 = climb(k1, w1, k2, f_k1, pat_k1, deadline);
            double v = v1 > v2 ? v1 : v2;
            if (v <= sc + 1e-9) break;
            sc = v;
        }
        if (sc > bestsc) {
            bestsc = sc; bestidp = bidp; memcpy(bestk1, k1, sizeof(int) * w1); memcpy(bestk2, k2, sizeof(int) * w2);
            report("improve", t0, iter, bestidp, bestsc, bestk1, bestk2);
        }
    }
    report("final", t0, iter, bestidp, bestsc, bestk1, bestk2);
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "see header for usage\n"); return 1; }
    const char *mode = argv[1];
    if (!strcmp(mode, "decrypt") && argc == 6) {
        unsigned char ct[MAXN], tmp[MAXN], out[MAXN]; int k1[MAXW], k2[MAXW];
        int n = read_text(argv[2], ct), w1 = parse_key(argv[3], k1), w2 = parse_key(argv[4], k2);
        undo_stage(argv[5][1], ct, tmp, n, k2, w2); undo_stage(argv[5][0], tmp, out, n, k1, w1);
        for (int i = 0; i < n; i++) putchar('A' + out[i]); putchar('\n'); return 0;
    }
    if (!strcmp(mode, "idp") && argc == 7) {
        load_lm(argv[6]);
        unsigned char ct[MAXN], tmp[MAXN]; int k2[MAXW];
        int n = read_text(argv[2], ct), w2 = parse_key(argv[3], k2), w1 = atoi(argv[4]);
        undo_stage(argv[5][1], ct, tmp, n, k2, w2);
        printf("%.4f\n", idp(tmp, n, w1, NULL)); return 0;
    }
    if (!strcmp(mode, "bench") && argc == 6) {
        load_lm(argv[5]);
        P.n = read_text(argv[2], P.ct); P.w1 = atoi(argv[3]); P.w2 = atoi(argv[4]); strcpy(P.conv, "CC");
        int k[MAXW]; random_key(k, P.w2); double t = now(); long c = 0; double acc = 0;
        while (now() - t < 3) { random_move(k, P.w2); acc += k2_idp(k); c++; }
        printf("{\"idp_per_sec\":%.0f,\"chk\":%.1f}\n", c / (now() - t), acc); return 0;
    }

    if (!strcmp(mode, "probe") && argc == 9) {
        /* fitness-distance: IDP of the true K2, of K2 after x random swaps, of random K2,
           and of IDP hill-climb optima from random starts */
        load_lm(argv[6]); memset(&P, 0, sizeof P);
        P.n = read_text(argv[2], P.ct); int tk[MAXW]; P.w2 = parse_key(argv[3], tk); P.w1 = atoi(argv[4]);
        strncpy(P.conv, argv[5], 2); rs ^= (uint64_t)atoll(argv[7]) * 0x9E3779B97F4A7C15ULL; int restarts = atoi(argv[8]);
        printf("{\"true\":%.4f", k2_idp(tk));
        for (int x = 1; x <= P.w2; x += (x < 6 ? 1 : 3)) {
            double acc = 0; for (int r = 0; r < 200; r++) { int k[MAXW]; memcpy(k, tk, sizeof(int) * P.w2);
                for (int y = 0; y < x; y++) { int i = rndint(P.w2), j = rndint(P.w2); while (j == i) j = rndint(P.w2); int t = k[i]; k[i] = k[j]; k[j] = t; }
                acc += k2_idp(k); }
            printf(",\"swap%d\":%.4f", x, acc / 200);
        }
        /* same-length swaps only: column c is long iff c < n % w2; such swaps move no segment */
        int ex2 = P.n % P.w2;
        for (int x = 1; x <= P.w2; x += (x < 6 ? 1 : 3)) {
            double acc = 0; for (int r = 0; r < 200; r++) { int k[MAXW]; memcpy(k, tk, sizeof(int) * P.w2);
                for (int y = 0; y < x; y++) { int i, j; do { i = rndint(P.w2); j = rndint(P.w2); } while (j == i || ((i < ex2) != (j < ex2)));
                    int t = k[i]; k[i] = k[j]; k[j] = t; }
                acc += k2_idp(k); }
            printf(",\"tswap%d\":%.4f", x, acc / 200);
        }
        double acc = 0, mx = -1e9; for (int r = 0; r < 2000; r++) { int k[MAXW]; random_key(k, P.w2); double v = k2_idp(k); acc += v; if (v > mx) mx = v; }
        printf(",\"random_mean\":%.4f,\"random_max2000\":%.4f,\"climbs\":[", acc / 2000, mx);
        for (int r = 0; r < restarts; r++) { int k[MAXW]; random_key(k, P.w2); left_to_right(k, P.w2);
            double v = climb(k, P.w2, NULL, f_idp, 3 * P.w2 * P.w2, now() + 60);
            int same = 0; for (int c = 0; c < P.w2; c++) same += k[c] == tk[c];
            printf(r ? ",[%.4f,%d]" : "[%.4f,%d]", v, same); fflush(stdout); }
        printf("]}\n"); return 0;
    }
    if (!strcmp(mode, "solve") && argc >= 9) {
        load_lm(argv[6]);
        memset(&P, 0, sizeof P);
        P.n = read_text(argv[2], P.ct); P.w1 = atoi(argv[3]); P.w2 = atoi(argv[4]);
        strncpy(P.conv, argv[5], 2);
        rs ^= (uint64_t)atoll(argv[7]) * 0x9E3779B97F4A7C15ULL; for (int i = 0; i < 10; i++) rnd64();
        int secs = atoi(argv[8]);
        if (argc > 9 && strcmp(argv[9], "-")) { int m = read_text(argv[9], P.pt); P.havept = (m == P.n); }
        if (argc > 10) P.n2 = read_text(argv[10], P.ct2);
        solve(secs); return 0;
    }
    fprintf(stderr, "bad arguments; see header\n"); return 1;
}
