/* dcm.c — 21-dc-method: the double columnar solver of 01-solver/dtsolve.c, copied, with switches for
 * the factors under test. 01's file is not modified. Shared code (stages, IDP, 01's moves, K1 stage) is
 * 01's, line for line, except where a switch selects a variant.
 *
 * Switches (key=value arguments):
 *   idp=0   01's IDP: greedy links, no cycle, w1-1 links.
 *   idp=1   Lasry's IDP as in his CrypTool 2 code (IDPAnalyser.cs, GetMatrixScore): the same greedy path,
 *           then the closing link tail->head, w1 links.
 *   climb=0 01's K2 climb: stochastic first improvement over 01's four random moves, stop after
 *           3*w2^2 consecutive failures.
 *   climb=1 full-neighbourhood climb: Lasry's transformation set (his TranspositionTransformations.cs in
 *           CrypTool 2's ADFGVX analyzer: cyclic segment slides of every length and shift, whole-key
 *           rotations, segment swaps up to w/4, 3-segment rotations of length 1-3, 3-cycles), deduplicated,
 *           scanned in random order with first improvement, until one full pass gives no improvement.
 *   k1climb=0|1  the same choice for the K1 stage and the refinement (quadgram score).
 *   oracle=1 truek1=..  (probe only) the IDP uses the true K1 segment starts instead of sweeping them: an
 *           upper bound on what better alignment handling could give.
 *   pmi=1   IDP bigram table as pointwise mutual information instead of joint log-probability.
 *   space=0 moves act on the rank array key[c] (01, and Lasry's notation); space=1 on the reading order.
 *   budget=N  stop after N IDP evaluations (load-independent; checked inside climbs).
 *
 * Modes:
 *   dcm probe CT truek2=.. w1=.. lang=.. seed=.. [idp= nclimb= nbasin= climb=]   fitness-distance + basins
 *   dcm k2    CT w1=.. w2=.. lang=.. seed=.. budget=.. [climb= idp= truek2= stophit=1]  K2 stage only
 *   dcm solve CT w1=.. w2=.. lang=.. seed=.. budget=.. [climb= idp= k1climb= pt= truek2= conv=CC]
 *   dcm k1    CT k2=.. w1=.. lang=.. seed=.. [k1climb= pt= restarts=]       K1 stage given K2
 *   dcm decrypt CT K1 K2 CONV
 * LANG selects out/lm_<LANG>_2.bin and out/lm_<LANG>_4.bin.
 * Build: cc -O3 -march=native -o out/dcm dcm.c -lm
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
static int PMI = 0;
static float Q4[26 * 26 * 26 * 26];

/* ---------- RNG (xorshift64*) ---------- */
static uint64_t rs = 88172645463325252ULL;
static inline uint64_t rnd64(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline int rndint(int n) { return (int)(rnd64() % (uint64_t)n); }
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
static double cpu(void) { return (double)clock() / CLOCKS_PER_SEC; }

/* ---------- options ---------- */
static int argc_g; static char **argv_g;
static const char *opt(const char *k, const char *def) {
    size_t L = strlen(k);
    for (int i = 3; i < argc_g; i++) if (!strncmp(argv_g[i], k, L) && argv_g[i][L] == '=') return argv_g[i] + L + 1;
    return def;
}
static long long iopt(const char *k, long long def) { const char *s = opt(k, NULL); return s ? atoll(s) : def; }

static void load_lm(const char *lang) {
    char p[256]; FILE *f;
    snprintf(p, sizeof p, "out/lm_%s_2.bin", lang);
    if (!(f = fopen(p, "rb")) || fread(B2, sizeof(float), 26 * 26, f) != 26 * 26) { fprintf(stderr, "cannot read %s\n", p); exit(1); }
    fclose(f);
    if (PMI) {   /* pointwise mutual information: log P(a,b) - log P(a) - log P(b), marginals from the same table */
        double pa[26] = {0}, pb[26] = {0};
        for (int a = 0; a < 26; a++) for (int b = 0; b < 26; b++) { double q = pow(10.0, B2[a * 26 + b]); pa[a] += q; pb[b] += q; }
        for (int a = 0; a < 26; a++) for (int b = 0; b < 26; b++) B2[a * 26 + b] -= (float)(log10(pa[a]) + log10(pb[b]));
    }
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

/* ---------- transposition stages (01) ---------- */
static void col_dec(const unsigned char *in, unsigned char *out, int n, const int *key, int w) {
    int order[MAXW], rows = n / w, ex = n % w, pos = 0;
    for (int c = 0; c < w; c++) order[key[c]] = c;
    for (int k = 0; k < w; k++) { int c = order[k], len = rows + (c < ex); for (int r = 0; r < len; r++) out[r * w + c] = in[pos++]; }
}
static void col_enc(const unsigned char *in, unsigned char *out, int n, const int *key, int w) {
    int order[MAXW], rows = n / w, ex = n % w, pos = 0;
    for (int c = 0; c < w; c++) order[key[c]] = c;
    for (int k = 0; k < w; k++) { int c = order[k], len = rows + (c < ex); for (int r = 0; r < len; r++) out[pos++] = in[r * w + c]; }
}
static void undo_stage(char st, const unsigned char *in, unsigned char *out, int n, const int *key, int w) {
    if (st == 'C') col_dec(in, out, n, key, w); else col_enc(in, out, n, key, w);
}
static double quad_score(const unsigned char *t, int n) {
    double s = 0;
    for (int i = 0; i + 3 < n; i++) s += Q4[((t[i] * 26 + t[i + 1]) * 26 + t[i + 2]) * 26 + t[i + 3]];
    return s;
}

/* ---------- IDP (01's, with Lasry's closing link as an option) ---------- */
typedef struct { float v; short i, j; } Pair;
static int cmp_pair(const void *a, const void *b) { float x = ((const Pair *)a)->v, y = ((const Pair *)b)->v; return (x < y) - (x > y); }
static int IDPMODE = 0;
static long long n_idp = 0, n_q = 0;
static int ORACLE = 0, OSTART[MAXW];   /* idp oracle: true K1 segment starts (probe only, from truek1) */

static double idp(const unsigned char *inter, int n, int w1, int *chain) {
    static Pair pairs[MAXW * MAXW];
    static float Bm[MAXW][MAXW];
    n_idp++;
    int r = n / w1, ex = n % w1, lo[MAXW], hi[MAXW];
    for (int k = 0; k < w1; k++) {
        int mlo = ex - (w1 - k); if (mlo < 0) mlo = 0;
        int mhi = k < ex ? k : ex;
        lo[k] = k * r + mlo; hi[k] = k * r + mhi;
        if (ORACLE) lo[k] = hi[k] = OSTART[k];
    }
    int np = 0;
    for (int i = 0; i < w1; i++) for (int j = 0; j < w1; j++) {
        if (i == j) continue;
        float best = -1e30f;
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
        Bm[i][j] = best / r;
        pairs[np].v = best / r; pairs[np].i = (short)i; pairs[np].j = (short)j; np++;
    }
    qsort(pairs, np, sizeof(Pair), cmp_pair);
    int right[MAXW], left[MAXW];
    for (int k = 0; k < w1; k++) right[k] = left[k] = -1;
    double sum = 0; int links = 0;
    for (int p = 0; p < np && links < w1 - 1; p++) {
        int i = pairs[p].i, j = pairs[p].j;
        if (right[i] >= 0 || left[j] >= 0) continue;
        int h = i; while (left[h] >= 0) h = left[h];
        if (h == j) continue;
        right[i] = j; left[j] = i; sum += pairs[p].v; links++;
    }
    int head = 0; while (left[head] >= 0) head = left[head];
    if (IDPMODE == 1) { int tail = head; while (right[tail] >= 0) tail = right[tail]; sum += Bm[tail][head]; }
    if (chain) { int s = head; for (int k = 0; k < w1; k++) { chain[k] = s; s = right[s]; } }
    return sum;
}

/* ---------- 01's random moves ---------- */
static void rotate(int *a, int i, int j, int k) {
    int tmp[MAXW], t = 0;
    for (int x = j; x < k; x++) tmp[t++] = a[x];
    for (int x = i; x < j; x++) tmp[t++] = a[x];
    for (int x = 0; x < t; x++) a[i + x] = tmp[x];
}
static void random_move(int *key, int w) {
    int type = rndint(4);
    if (w < 3) type = 0;
    if (type == 0) { int i = rndint(w), j = rndint(w); while (j == i) j = rndint(w); int t = key[i]; key[i] = key[j]; key[j] = t; }
    else if (type == 1) { int i = rndint(w - 1), k = i + 2 + rndint(w - i - 1); if (k > w) k = w; int j = i + 1 + rndint(k - i - 1); rotate(key, i, j, k); }
    else if (type == 2) { int L = 1 + rndint(w / 2), i = rndint(w - 2 * L + 1), j = i + L + rndint(w - i - 2 * L + 1);
        for (int x = 0; x < L; x++) { int t = key[i + x]; key[i + x] = key[j + x]; key[j + x] = t; } }
    else { int i = rndint(w), j = rndint(w), k = rndint(w); while (j == i) j = rndint(w); while (k == i || k == j) k = rndint(w);
        int t = key[i]; key[i] = key[j]; key[j] = key[k]; key[k] = t; }
}
static void random_key(int *key, int w) {
    for (int i = 0; i < w; i++) key[i] = i;
    for (int i = w - 1; i > 0; i--) { int j = rndint(i + 1), t = key[i]; key[i] = key[j]; key[j] = t; }
}

/* ---------- Lasry's neighbourhood (TranspositionTransformations.cs), deduplicated ---------- */
typedef struct { int w, n, cap; unsigned char *m; } Nbhd;   /* move t: to[j] = from[m[t*w + j]] */
static uint64_t hperm(const unsigned char *p, int w) { uint64_t h = 1469598103934665603ULL; for (int i = 0; i < w; i++) { h ^= p[i]; h *= 1099511628211ULL; } return h; }
static void nb_add(Nbhd *N, int *hs, int hcap, const int *tk) {
    unsigned char p[MAXW]; int ident = 1, seen[MAXW] = {0};
    for (int i = 0; i < N->w; i++) { if (tk[i] < 0 || tk[i] >= N->w || seen[tk[i]]++) return; p[i] = (unsigned char)tk[i]; if (tk[i] != i) ident = 0; }
    if (ident) return;
    uint64_t h = hperm(p, N->w); int s = (int)(h & (uint64_t)(hcap - 1));
    while (hs[s] >= 0) { if (!memcmp(N->m + (size_t)hs[s] * N->w, p, N->w)) return; s = (s + 1) & (hcap - 1); }
    if (N->n == N->cap) { N->cap *= 2; N->m = realloc(N->m, (size_t)N->cap * N->w); }
    memcpy(N->m + (size_t)N->n * N->w, p, N->w); hs[s] = N->n++;
}
static void nb_build(Nbhd *N, int w) {
    N->w = w; N->n = 0; N->cap = 4096; N->m = malloc((size_t)N->cap * w);
    int hcap = 1 << 20, *hs = malloc(sizeof(int) * hcap); for (int i = 0; i < hcap; i++) hs[i] = -1;
    int id[MAXW], t[MAXW];
    for (int i = 0; i < w; i++) id[i] = i;
    /* cyclic segment slides, every length, shift and start */
    for (int len = w; len > 0; len--) for (int sh = 1; sh < w; sh++) for (int p1 = 0; p1 < w; p1++) {
        int aff = len + sh; if (aff > w) continue;
        memcpy(t, id, sizeof(int) * w);
        for (int i = 0; i < aff; i++) t[(p1 + (i + sh) % aff) % w] = id[(p1 + i) % w];
        nb_add(N, hs, hcap, t);
    }
    /* whole-key rotations */
    for (int sh = 1; sh < w; sh++) { for (int i = 0; i < w; i++) t[(i + sh) % w] = id[i]; nb_add(N, hs, hcap, t); }
    /* segment swaps up to w/4 (at least 1) */
    int maxl = w / 4 > 0 ? w / 4 : 1;
    for (int len = maxl; len > 0; len--) for (int p1 = 0; p1 + 2 * len <= w; p1++) for (int p2 = p1 + len; p2 + len <= w; p2++) {
        memcpy(t, id, sizeof(int) * w);
        for (int x = 0; x < len; x++) { t[p2 + x] = id[p1 + x]; t[p1 + x] = id[p2 + x]; }
        nb_add(N, hs, hcap, t);
    }
    /* 3-segment rotations, segment length 1-3, both directions */
    for (int len = 1; len < 4; len++) for (int p1 = 0; p1 + 3 * len <= w; p1++) for (int p2 = p1 + len; p2 + 2 * len <= w; p2++) for (int p3 = p2 + len; p3 + len <= w; p3++) {
        memcpy(t, id, sizeof(int) * w);
        for (int x = 0; x < len; x++) { t[p2 + x] = id[p1 + x]; t[p3 + x] = id[p2 + x]; t[p1 + x] = id[p3 + x]; }
        nb_add(N, hs, hcap, t);
        memcpy(t, id, sizeof(int) * w);
        for (int x = 0; x < len; x++) { t[p3 + x] = id[p1 + x]; t[p1 + x] = id[p2 + x]; t[p2 + x] = id[p3 + x]; }
        nb_add(N, hs, hcap, t);
    }
    /* 3-cycles of single elements */
    for (int a = 0; a < w; a++) for (int b = 0; b < w; b++) for (int c = 0; c < w; c++) {
        if (a == b || a == c || b == c) continue;
        memcpy(t, id, sizeof(int) * w); t[a] = id[b]; t[b] = id[c]; t[c] = id[a];
        nb_add(N, hs, hcap, t);
    }
    free(hs);
}
static int SPACE = 0;
static void nb_apply(const Nbhd *N, int t, const int *from, int *to) {
    const unsigned char *m = N->m + (size_t)t * N->w; int w = N->w;
    if (SPACE == 0) { for (int j = 0; j < w; j++) to[j] = from[m[j]]; return; }
    int ord[MAXW], o2[MAXW];
    for (int c = 0; c < w; c++) ord[from[c]] = c;
    for (int j = 0; j < w; j++) o2[j] = ord[m[j]];
    for (int k = 0; k < w; k++) to[o2[k]] = k;
}

/* ---------- problem state ---------- */
typedef struct {
    unsigned char ct[MAXN], pt[MAXN];
    int n, w1, w2, havept, havetk2, tk2[MAXW];
    char conv[3];
} Prob;
static Prob P;
static unsigned char inter[MAXN], dec[MAXN];
static long long BUDGET = (long long)4e18;
static Nbhd NB1, NB2;

static double k2_idp(const int *k2) { undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2); return idp(inter, P.n, P.w1, NULL); }
static double full_score(const int *k1, const int *k2) {
    n_q++;
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    undo_stage(P.conv[0], inter, dec, P.n, k1, P.w1);
    return quad_score(dec, P.n) / (P.n - 3);
}
typedef double (*ScoreFn)(const int *k, const int *other);
static double f_idp(const int *k2, const int *unused) { (void)unused; return k2_idp(k2); }
static double f_k1(const int *k1, const int *k2) { return full_score(k1, k2); }
static double f_k2(const int *k2, const int *k1) { return full_score(k1, k2); }
static int over_budget(void) { return n_idp >= BUDGET; }

/* 01's stochastic first-improvement climb */
static double climb_stoch(int *key, int w, const int *other, ScoreFn f, int patience) {
    int cand[MAXW]; double best = f(key, other); int fails = 0;
    while (fails < patience && !(f == f_idp && over_budget())) {
        memcpy(cand, key, sizeof(int) * w); random_move(cand, w);
        double s = f(cand, other);
        if (s > best) { best = s; memcpy(key, cand, sizeof(int) * w); fails = 0; } else fails++;
    }
    return best;
}
/* full-neighbourhood first-improvement climb over Lasry's set, random order, until a pass fails */
static int *nb_order; static int nb_order_n = 0;
static double climb_full(int *key, int w, const int *other, ScoreFn f, const Nbhd *N) {
    if (nb_order_n < N->n) { nb_order = realloc(nb_order, sizeof(int) * N->n); nb_order_n = N->n; }
    int *ord = nb_order; for (int i = 0; i < N->n; i++) ord[i] = i;
    int cand[MAXW]; double best = f(key, other);
    for (;;) {
        for (int i = N->n - 1; i > 0; i--) { int j = rndint(i + 1), t = ord[i]; ord[i] = ord[j]; ord[j] = t; }
        int improved = 0;
        for (int i = 0; i < N->n; i++) {
            if (f == f_idp && over_budget()) return best;
            nb_apply(N, ord[i], key, cand);
            double s = f(cand, other);
            if (s > best + 1e-9) { best = s; memcpy(key, cand, sizeof(int) * w); improved = 1; }
        }
        if (!improved) return best;
    }
}
static int CLIMB2 = 0, CLIMB1 = 0;
static double climb_k2(int *k2) { return CLIMB2 ? climb_full(k2, P.w2, NULL, f_idp, &NB2) : climb_stoch(k2, P.w2, NULL, f_idp, 3 * P.w2 * P.w2); }
static double climb_k1q(int *k1, const int *k2) { return CLIMB1 ? climb_full(k1, P.w1, k2, f_k1, &NB1) : climb_stoch(k1, P.w1, k2, f_k1, 4 * P.w1 * P.w1); }
static double climb_k2q(int *k2, const int *k1) { return CLIMB1 ? climb_full(k2, P.w2, k1, f_k2, &NB2) : climb_stoch(k2, P.w2, k1, f_k2, 3 * P.w2 * P.w2); }

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
static int same_k2(const int *k) { int s = 0; for (int c = 0; c < P.w2; c++) s += k[c] == P.tk2[c]; return s; }
static void print_key(FILE *f, const int *k, int w) { for (int i = 0; i < w; i++) fprintf(f, i ? ",%d" : "%d", k[i]); }

static double t0w, t0c;
static void report(const char *tag, long iter, double idpv, double sc, const int *k1, const int *k2, long long hit_at) {
    undo_stage(P.conv[1], P.ct, inter, P.n, k2, P.w2);
    undo_stage(P.conv[0], inter, dec, P.n, k1, P.w1);
    printf("{\"tag\":\"%s\",\"t\":%.1f,\"cpu\":%.1f,\"iter\":%ld,\"n_idp\":%lld,\"n_q\":%lld,\"w1\":%d,\"w2\":%d,\"conv\":\"%s\",\"idp\":%.4f,\"score\":%.4f,\"acc\":%.4f,\"k2same\":%d,\"hit_at\":%lld,\"k1\":\"",
           tag, now() - t0w, cpu() - t0c, iter, n_idp, n_q, P.w1, P.w2, P.conv, idpv, sc, accuracy(k1, k2), P.havetk2 ? same_k2(k2) : -1, hit_at);
    print_key(stdout, k1, P.w1); printf("\",\"k2\":\""); print_key(stdout, k2, P.w2); printf("\",\"pt\":\"");
    for (int i = 0; i < P.n; i++) putchar('A' + dec[i]);
    printf("\"}\n"); fflush(stdout);
}

/* steps 1-3 of one iteration: random K2s, left-to-right, climbs. Returns the iteration's best K2. */
static int NRAND = 200, KEEP = 10, NSTART = 3;
static double k2_iteration(int *k2out) {
    static int pool[64][MAXW]; double pv[64];
    int w2 = P.w2;
    for (int s = 0; s < KEEP; s++) pv[s] = -1e30;
    for (int r = 0; r < NRAND; r++) {
        int k[MAXW]; random_key(k, w2);
        if (P.havetk2 && same_k2(k) == w2) { fprintf(stderr, "solver drew the planted K2; abort\n"); exit(3); }
        double v = k2_idp(k);
        int worst = 0; for (int s = 1; s < KEEP; s++) if (pv[s] < pv[worst]) worst = s;
        if (v > pv[worst]) { pv[worst] = v; memcpy(pool[worst], k, sizeof(int) * w2); }
    }
    for (int s = 0; s < KEEP; s++) pv[s] = left_to_right(pool[s], w2);
    for (int a = 0; a < NSTART && a < KEEP; a++) {
        int b = a; for (int s = a + 1; s < KEEP; s++) if (pv[s] > pv[b]) b = s;
        double tv = pv[a]; pv[a] = pv[b]; pv[b] = tv;
        int tk[MAXW]; memcpy(tk, pool[a], sizeof(int) * w2); memcpy(pool[a], pool[b], sizeof(int) * w2); memcpy(pool[b], tk, sizeof(int) * w2);
    }
    double bidp = -1e30;
    for (int s = 0; s < NSTART && !over_budget(); s++) {
        double v = climb_k2(pool[s]);
        if (v > bidp) { bidp = v; memcpy(k2out, pool[s], sizeof(int) * w2); }
    }
    if (bidp < -1e29) { memcpy(k2out, pool[0], sizeof(int) * w2); bidp = pv[0]; }
    return bidp;
}

static void k2_only(void) {
    double true_idp = P.havetk2 ? k2_idp(P.tk2) : 1e30; n_idp = 0;
    int stophit = (int)iopt("stophit", 1);
    int best[MAXW], k1dummy[MAXW]; double bv = -1e30; long iter = 0; long long hit_at = -1;
    for (int c = 0; c < P.w1; c++) k1dummy[c] = c;
    printf("{\"tag\":\"true\",\"idp\":%.4f}\n", P.havetk2 ? true_idp : 0.0);
    while (!over_budget()) {
        iter++;
        int k2[MAXW]; double v = k2_iteration(k2);
        if (v >= true_idp - 1e-6 && hit_at < 0) hit_at = n_idp;
        if (v > bv) { bv = v; memcpy(best, k2, sizeof(int) * P.w2); report("improve", iter, bv, 0, k1dummy, best, hit_at); }
        if (hit_at >= 0 && stophit) break;
    }
    report("final", iter, bv, 0, k1dummy, best, hit_at);
}

/* K1 stage given K2 (01's step 4a): chain seed + random restarts, then 4b refinement. */
static double k1_stage(int *k1, int *k2, int restarts, int refine) {
    int kk[MAXW]; double sc1 = -1e9;
    k1_from_chain(k2, kk);
    for (int rr = 0; rr < restarts; rr++) {
        if (rr) random_key(kk, P.w1);
        double v = climb_k1q(kk, k2);
        if (v > sc1) { sc1 = v; memcpy(k1, kk, sizeof(int) * P.w1); }
        if (rr == 0) k1_from_chain(k2, kk);
    }
    double sc = sc1;
    for (int round = 0; refine && round < 6; round++) {
        double v2 = climb_k2q(k2, k1);
        double v1 = climb_k1q(k1, k2);
        double v = v1 > v2 ? v1 : v2;
        if (v <= sc + 1e-9) break;
        sc = v;
    }
    return sc;
}

static void solve(void) {
    double true_idp = P.havetk2 ? k2_idp(P.tk2) : 1e30; n_idp = 0;
    int bestk1[MAXW], bestk2[MAXW]; double bestsc = -1e9, bestidp = 0; long iter = 0; long long hit_at = -1;
    int restarts = (int)iopt("restarts", 4);
    while (!over_budget()) {
        iter++;
        int k2[MAXW], k1[MAXW];
        double bidp = k2_iteration(k2);
        if (bidp >= true_idp - 1e-6 && hit_at < 0) hit_at = n_idp;
        double sc = k1_stage(k1, k2, restarts, 1);
        if (sc > bestsc) {
            bestsc = sc; bestidp = bidp; memcpy(bestk1, k1, sizeof(int) * P.w1); memcpy(bestk2, k2, sizeof(int) * P.w2);
            report("improve", iter, bestidp, bestsc, bestk1, bestk2, hit_at);
        }
    }
    report("final", iter, bestidp, bestsc, bestk1, bestk2, hit_at);
}

/* fitness-distance and basins of attraction */
static void perturb(int *k, const int *tk, int w, int x) {   /* x swaps of two still-correct elements (Lasry 9.4.5.3) */
    memcpy(k, tk, sizeof(int) * w);
    for (int y = 0; y < x; y++) {
        int i, j, tries = 0;
        do { i = rndint(w); j = rndint(w); tries++; } while ((i == j || k[i] != tk[i] || k[j] != tk[j]) && tries < 10000);
        int t = k[i]; k[i] = k[j]; k[j] = t;
    }
}
static void probe(void) {
    int w2 = P.w2, nclimb = (int)iopt("nclimb", 10), nbasin = (int)iopt("nbasin", 10);
    double tv = k2_idp(P.tk2);
    printf("{\"w1\":%d,\"w2\":%d,\"n\":%d,\"idpmode\":%d,\"climb\":%d,\"true\":%.4f", P.w1, w2, P.n, IDPMODE, CLIMB2, tv);
    printf(",\"D\":{");
    for (int x = 1; x <= w2 / 2; x++) {
        double a = 0, a2 = 0; int R = 200;
        for (int r = 0; r < R; r++) { int k[MAXW]; perturb(k, P.tk2, w2, x); double v = tv - k2_idp(k); a += v; a2 += v * v; }
        printf(x > 1 ? ",\"%d\":[%.4f,%.4f]" : "\"%d\":[%.4f,%.4f]", x, a / R, sqrt(a2 / R - (a / R) * (a / R)));
    }
    double a = 0, a2 = 0, mx = -1e9; int R = 2000;
    for (int r = 0; r < R; r++) { int k[MAXW]; random_key(k, w2); double v = k2_idp(k); a += v; a2 += v * v; if (v > mx) mx = v; }
    printf("},\"random\":[%.4f,%.4f,%.4f]", tv - a / R, sqrt(a2 / R - (a / R) * (a / R)), tv - mx);
    printf(",\"rot\":[");
    for (int s = 1; s < w2; s++) { int k[MAXW]; for (int c = 0; c < w2; c++) k[c] = P.tk2[(c + s) % w2]; printf(s > 1 ? ",%.3f" : "%.3f", tv - k2_idp(k)); }
    printf("],\"climbs\":[");
    for (int r = 0; r < nclimb; r++) {
        int k[MAXW]; random_key(k, w2); left_to_right(k, w2); double v = climb_k2(k);
        printf(r ? ",[%.4f,%d]" : "[%.4f,%d]", tv - v, same_k2(k)); fflush(stdout);
    }
    printf("],\"basin\":{");
    int xs[] = {1, 2, 3, 4, 5, 6, 8, 10}, first = 1, bmax = (int)iopt("bmax", 10);
    for (int xi = 0; xi < 8; xi++) {
        int x = xs[xi]; if (x > w2 / 2 || x > bmax) break;
        int back = 0; double dsum = 0;
        for (int r = 0; r < nbasin; r++) {
            int k[MAXW]; perturb(k, P.tk2, w2, x); double v = climb_k2(k);
            back += v >= tv - 1e-6; dsum += tv - v;
        }
        printf(first ? "\"%d\":[%d,%d,%.3f]" : ",\"%d\":[%d,%d,%.3f]", x, back, nbasin, dsum / nbasin); first = 0; fflush(stdout);
    }
    printf("},\"n_idp\":%lld,\"cpu\":%.1f}\n", n_idp, cpu() - t0c);
}

int main(int argc, char **argv) {
    argc_g = argc; argv_g = argv;
    if (argc < 3) { fprintf(stderr, "see header for usage\n"); return 1; }
    const char *mode = argv[1];
    t0w = now(); t0c = cpu();
    if (!strcmp(mode, "decrypt") && argc == 6) {
        unsigned char ct[MAXN], tmp[MAXN], out[MAXN]; int k1[MAXW], k2[MAXW];
        int n = read_text(argv[2], ct), w1 = parse_key(argv[3], k1), w2 = parse_key(argv[4], k2);
        undo_stage(argv[5][1], ct, tmp, n, k2, w2); undo_stage(argv[5][0], tmp, out, n, k1, w1);
        for (int i = 0; i < n; i++) putchar('A' + out[i]); putchar('\n'); return 0;
    }
    memset(&P, 0, sizeof P);
    P.n = read_text(argv[2], P.ct);
    strncpy(P.conv, opt("conv", "CC"), 2);
    IDPMODE = (int)iopt("idp", 0); CLIMB2 = (int)iopt("climb", 0); CLIMB1 = (int)iopt("k1climb", 0); SPACE = (int)iopt("space", 0);
    NRAND = (int)iopt("nrand", 200); KEEP = (int)iopt("keep", 10); NSTART = (int)iopt("nstart", 3);
    BUDGET = iopt("budget", (long long)4e18);
    rs ^= (uint64_t)iopt("seed", 1) * 0x9E3779B97F4A7C15ULL; for (int i = 0; i < 10; i++) rnd64();
    PMI = (int)iopt("pmi", 0);
    load_lm(opt("lang", "es"));
    P.w1 = (int)iopt("w1", 0); P.w2 = (int)iopt("w2", 0);
    const char *tk = opt("truek2", NULL);
    if (tk && strcmp(tk, "-")) { int w = parse_key(tk, P.tk2); if (P.w2 && w != P.w2) { fprintf(stderr, "truek2 length\n"); return 1; } P.w2 = w; P.havetk2 = 1; }
    const char *tk1 = opt("truek1", NULL);
    if (tk1 && iopt("oracle", 0)) {   /* segment k starts at k*r1 + (long columns among ranks < k); long = column < n % w1 */
        int k1[MAXW], w = parse_key(tk1, k1), ord[MAXW], r1 = P.n / w, ex1 = P.n % w, m = 0;
        for (int c = 0; c < w; c++) ord[k1[c]] = c;
        for (int k = 0; k < w; k++) { OSTART[k] = k * r1 + m; m += ord[k] < ex1; }
        ORACLE = 1;
    }
    const char *ptp = opt("pt", NULL);
    if (ptp && strcmp(ptp, "-")) { int m = read_text(ptp, P.pt); P.havept = (m == P.n); }
    if (!P.w1 || !P.w2) { fprintf(stderr, "need w1 and w2 (or truek2)\n"); return 1; }
    if (CLIMB2) nb_build(&NB2, P.w2);
    if (CLIMB1) { nb_build(&NB1, P.w1); if (!CLIMB2) nb_build(&NB2, P.w2); }
    if (!strcmp(mode, "nbsize")) { printf("{\"w2\":%d,\"n\":%d}\n", P.w2, NB2.n); return 0; }
    if (!strcmp(mode, "probe")) { probe(); return 0; }
    if (!strcmp(mode, "k2")) { k2_only(); return 0; }
    if (!strcmp(mode, "solve")) { solve(); return 0; }
    if (!strcmp(mode, "k1")) {
        int k2[MAXW], k1[MAXW]; parse_key(opt("k2", ""), k2);
        double sc = k1_stage(k1, k2, (int)iopt("restarts", 4), (int)iopt("refine", 0));
        report("k1", 0, 0, sc, k1, k2, -1); return 0;
    }
    fprintf(stderr, "bad mode\n"); return 1;
}
