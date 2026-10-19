/*
 * Single Singer-subgroup orbits of PG(2, p) as blocking sets.
 *
 * usage: orbitscan lo hi
 *
 * For each prime p in [lo, hi], find the first cubic x^3 = a x^2 + b x + c
 * (lexicographic in (a, b, c), c != 0) whose root w makes the classes of
 * w^i modulo F_p^* run through all N = p^2 + p + 1 points, form the
 * planar difference set D = {i : Tr(w^i) = 0}, and for every divisor m of N
 * with m >= 2 and m <= p + 1 <= 8 m print the least and largest number of elements of D
 * in a residue class modulo m. The orbit {i : i = 0 mod m} of the subgroup of
 * index m meets the line D + t in |{d in D : d = -t mod m}| points, so it is
 * blocking with cap C exactly when every class count lies in [1, C].
 * This is the same construction as util/singer.py, in C for speed.
 */
#include <stdio.h>
#include <stdlib.h>

static int is_prime(int n) {
    if (n < 2) return 0;
    for (int d = 2; (long)d * d <= n; d++)
        if (n % d == 0) return 0;
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "usage: orbitscan lo hi\n");
        return 2;
    }
    int lo = atoi(argv[1]), hi = atoi(argv[2]);
    for (int p = lo; p <= hi; p++) {
        if (!is_prime(p)) continue;
        long n = (long)p * p + p + 1;
        int a0 = -1, b0 = -1, c0 = -1;
        for (int a = 0; a < p && a0 < 0; a++)
            for (int b = 0; b < p && a0 < 0; b++)
                for (int c = 1; c < p && a0 < 0; c++) {
                    long u0 = 1, u1 = 0, u2 = 0, i;
                    int ok = 1;
                    for (i = 1; i <= n; i++) {
                        long v0 = (c * u2) % p, v1 = (u0 + b * u2) % p, v2 = (u1 + a * u2) % p;
                        u0 = v0; u1 = v1; u2 = v2;
                        if (u1 == 0 && u2 == 0) {
                            if (i < n) ok = 0;
                            break;
                        }
                    }
                    if (ok && i == n) { a0 = a; b0 = b; c0 = c; }
                }
        if (a0 < 0) {
            printf("p=%d ERROR no cubic\n", p);
            return 1;
        }
        long t0 = 3 % p, t1 = a0 % p, t2 = ((long)a0 * a0 + 2L * b0) % p;
        int *diff = malloc(sizeof(int) * (p + 2));
        int nd = 0;
        long u0 = 1, u1 = 0, u2 = 0;
        for (long i = 0; i < n; i++) {
            if ((t0 * u0 + t1 * u1 + t2 * u2) % p == 0) {
                if (nd <= p) diff[nd] = (int)i;
                nd++;
            }
            long v0 = (c0 * u2) % p, v1 = (u0 + b0 * u2) % p, v2 = (u1 + a0 * u2) % p;
            u0 = v0; u1 = v1; u2 = v2;
        }
        if (nd != p + 1) {
            printf("p=%d ERROR difference set size %d\n", p, nd);
            return 1;
        }
        for (long m = 2; m <= p + 1; m++) {
            if (n % m || p + 1 > 8 * m) continue;
            int *h = calloc(m, sizeof(int));
            for (int k = 0; k < nd; k++) h[diff[k] % m]++;
            int mn = 1 << 30, mx = 0;
            for (long r = 0; r < m; r++) {
                if (h[r] < mn) mn = h[r];
                if (h[r] > mx) mx = h[r];
            }
            printf("%d %d %d %d %ld %d %d\n", p, a0, b0, c0, m, mn, mx);
            free(h);
        }
        free(diff);
        fflush(stdout);
    }
    return 0;
}
