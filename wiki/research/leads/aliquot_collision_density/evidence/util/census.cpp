// Exact collision census for s(n) = sigma(n) - n over composite n <= X.
//
// Usage: census WORKDIR WBITS X_0,X_1,...,X_{J-1} H_0,H_1,... MODE
//
// The checkpoints X_0 < X_1 < ... < X_{J-1} = X (J <= 32) are the scales at
// which the census is reported; H_0, H_1, ... are the checkpoint indices at
// which fiber-size histograms are reported. A segmented sieve computes
// sigma(n) exactly for every n <= X. Primes and n = 1 are tallied but not
// recorded. For every composite n it records
//
//   ell(n)  = min(15, min{k >= 0 : 2^k s(n) >= n}),
//   flag(n) = [Omega(n) >= 3] when MODE = 0, and [P(n)^2 > n] when
//             MODE = 1, where P(n) is the largest prime factor,
//   j(n)    = min{j : n <= X_j},
//
// with the low WBITS bits of s(n), in the bucket file floor(s(n) / 2^WBITS)
// under WORKDIR. Each bucket is then sorted. For every value m, every ordered
// pair (n, n') of recorded inputs with s(n) = s(n') = m, the diagonal n = n'
// included, is tallied by (number of flagged inputs in the pair, max ell,
// max j). The classes
//
//   D_k  = {n composite : ell(n) <= k}             (k = 0, ..., 15)
//   DF_k = {n in D_k : flag(n) = 1}
//   DN_k = {n in D_k : flag(n) = 0}
//
// therefore get, at every checkpoint, the input count R and the ordered
// pair count C = sum_m r(m)^2 by prefix sums. Since ell is clipped at 15,
// D_15 is the set of all composites; for k <= 14, ell(n) <= k exactly when
// 2^k s(n) >= n, that is when sigma(n) >= (1 + 2^-k) n. All arithmetic is
// exact unsigned integer arithmetic. Pair counts use 128 bits (their sum is
// at most X^2); the other quantities fit in 64 bits for X <= 2e10. Bucket
// counts and bucket sizes have explicit caps, so an unsupported memory
// requirement fails instead of attempting an unbounded allocation.

#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <string>
#include <vector>

typedef unsigned long long u64;
typedef unsigned __int128 u128;
typedef uint32_t u32;

static const int NCLS = 48;      // D_0..D_15, DF_0..DF_15, DN_0..DN_15
static const int TCAP = 4096;    // dense histogram cap; larger sizes go to a map
static const u64 SEG = 1 << 18;  // sieve segment length
static const size_t MAX_BUCKETS = 1 << 16;
static const size_t MAX_BUCKET_RECORDS = 1 << 29;  // 2 GiB of sorted records

static void die(const char* msg) {
    fprintf(stderr, "census: %s\n", msg);
    exit(2);
}

static void add(u64& acc, u64 v) {
    if (__builtin_add_overflow(acc, v, &acc)) die("accumulator overflow");
}

static std::string decimal(u128 value) {
    std::string out;
    do {
        out.push_back(char('0' + value % 10));
        value /= 10;
    } while (value);
    std::reverse(out.begin(), out.end());
    return out;
}

static std::vector<u64> parse_list(const char* s) {
    std::vector<u64> out;
    const char* p = s;
    while (*p) {
        char* end;
        u64 v = strtoull(p, &end, 10);
        if (end == p) die("bad list");
        out.push_back(v);
        p = end;
        if (*p == ',') p++;
    }
    return out;
}

int main(int argc, char** argv) {
    if (argc != 6) die("usage: census WORKDIR WBITS X0,X1,... H0,H1,... MODE");
    std::string workdir = argv[1];
    int wbits = atoi(argv[2]);
    if (wbits < 1 || wbits > 22) die("WBITS must lie in [1, 22]");
    std::vector<u64> xs = parse_list(argv[3]);
    std::vector<u64> hs = parse_list(argv[4]);
    int mode = atoi(argv[5]);
    if (mode != 0 && mode != 1) die("MODE must be 0 or 1");
    int J = (int)xs.size();
    if (J < 1 || J > 32) die("need 1 to 32 checkpoints");
    for (int j = 1; j < J; j++)
        if (xs[j] <= xs[j - 1]) die("checkpoints must increase");
    if (xs[0] < 1) die("checkpoints must be positive");
    for (u64 h : hs)
        if (h >= (u64)J) die("histogram index out of range");
    u64 X = xs[J - 1];
    if (X > 20000000000ULL) die("X above 2e10 is not supported");

    // primes up to sqrt(X)
    u64 root = 1;
    while ((root + 1) * (root + 1) <= X) root++;
    std::vector<u64> primes;
    {
        std::vector<char> comp(root + 1, 0);
        for (u64 i = 2; i <= root; i++) {
            if (comp[i]) continue;
            primes.push_back(i);
            for (u64 k = i * i; k <= root; k += i) comp[k] = 1;
        }
    }

    // per-checkpoint tallies (not cumulative): primes, Omega = 2
    std::vector<u64> nprime(J, 0), nomega2(J, 0);
    // records by key (flag, ell, j): counts of inputs
    static u64 rcount[2][16][32];
    memset(rcount, 0, sizeof(rcount));
    u64 clipped = 0, records = 0, maxs = 0;

    // bucket files, opened lazily
    std::vector<FILE*> files;
    std::vector<std::vector<u32>> bufs;
    const size_t BUFN = 8192;
    auto bucket_path = [&](size_t b) {
        char name[64];
        snprintf(name, sizeof(name), "/bucket_%06zu.bin", b);
        return workdir + name;
    };
    auto flush = [&](size_t b) {
        std::vector<u32>& v = bufs[b];
        if (v.empty()) return;
        if (fwrite(v.data(), sizeof(u32), v.size(), files[b]) != v.size()) die("write failed");
        v.clear();
    };

    std::vector<u64> rem(SEG), sig(SEG), maxp(SEG);
    std::vector<unsigned char> om(SEG);
    int jcur = 0;
    for (u64 lo = 1; lo <= X; lo += SEG) {
        u64 hi = std::min(X + 1, lo + SEG);  // segment [lo, hi)
        u64 len = hi - lo;
        for (u64 i = 0; i < len; i++) {
            rem[i] = lo + i;
            sig[i] = 1;
            om[i] = 0;
            maxp[i] = 1;
        }
        for (u64 p : primes) {
            if (p * p >= hi) break;
            u64 start = ((lo + p - 1) / p) * p;
            for (u64 m = start; m < hi; m += p) {
                u64 i = m - lo;
                u64 r = rem[i], pk = 1;
                unsigned char e = 0;
                do {
                    r /= p;
                    pk *= p;
                    e++;
                } while (r % p == 0);
                rem[i] = r;
                om[i] += e;
                maxp[i] = p;
                sig[i] *= (pk * p - 1) / (p - 1);
            }
        }
        for (u64 i = 0; i < len; i++) {
            u64 n = lo + i;
            if (rem[i] > 1) {
                sig[i] *= rem[i] + 1;
                om[i] += 1;
                maxp[i] = rem[i];
            }
            while (n > xs[jcur]) jcur++;
            if (om[i] <= 1) {
                if (om[i] == 1) nprime[jcur]++;
                continue;
            }
            if (om[i] == 2) nomega2[jcur]++;
            u64 s = sig[i] - n;
            unsigned ell = 0;
            u64 t = s;
            while (t < n && ell < 15) {
                t <<= 1;
                ell++;
            }
            if (t < n) clipped++;
            unsigned o3;
            if (mode == 0)
                o3 = om[i] >= 3 ? 1 : 0;
            else
                o3 = maxp[i] > n / maxp[i] ? 1 : 0;  // P^2 > n
            if (s > maxs) maxs = s;
            size_t b = (size_t)(s >> wbits);
            if (b >= MAX_BUCKETS) die("bucket index exceeds the memory cap; increase WBITS");
            u32 off = (u32)(s & ((1ULL << wbits) - 1));
            u32 rec = (off << 10) | ((u32)jcur << 5) | (ell << 1) | o3;
            if (b >= files.size()) {
                files.resize(b + 1, nullptr);
                bufs.resize(b + 1);
            }
            if (!files[b]) {
                files[b] = fopen(bucket_path(b).c_str(), "wb");
                if (!files[b]) die("cannot open bucket file");
                bufs[b].reserve(BUFN);
            }
            bufs[b].push_back(rec);
            if (bufs[b].size() >= BUFN) flush(b);
            rcount[o3][ell][jcur]++;
            records++;
        }
    }
    for (size_t b = 0; b < files.size(); b++) {
        if (!files[b]) continue;
        flush(b);
        if (fclose(files[b]) != 0) die("close failed");
        std::vector<u32>().swap(bufs[b]);
    }

    // pair tallies by (flagged inputs in the pair, max ell, max j)
    static u128 delta[3][16][32];
    memset(delta, 0, sizeof(delta));
    // histograms: for each histogram checkpoint and class, counts of values
    // m with exactly t inputs of the class up to that checkpoint
    int NH = (int)hs.size();
    std::vector<std::vector<std::vector<u64>>> hist(
        NH, std::vector<std::vector<u64>>(NCLS, std::vector<u64>(TCAP, 0)));
    std::vector<std::vector<std::map<u64, u64>>> hbig(NH, std::vector<std::map<u64, u64>>(NCLS));
    static u64 hsingle[2][16][32];  // values with exactly one input, by key
    memset(hsingle, 0, sizeof(hsingle));
    u64 maxrun = 0;

    for (size_t b = 0; b < files.size(); b++) {
        if (!files[b]) continue;
        std::string path = bucket_path(b);
        FILE* f = fopen(path.c_str(), "rb");
        if (!f) die("cannot reopen bucket file");
        fseek(f, 0, SEEK_END);
        long sz = ftell(f);
        fseek(f, 0, SEEK_SET);
        if (sz < 0 || sz % 4 != 0) die("bad bucket size");
        if ((size_t)sz / 4 > MAX_BUCKET_RECORDS)
            die("bucket exceeds the 2 GiB sort cap; decrease WBITS");
        std::vector<u32> v((size_t)sz / 4);
        if (fread(v.data(), 4, v.size(), f) != v.size()) die("read failed");
        fclose(f);
        if (remove(path.c_str()) != 0) die("cannot remove bucket file");
        std::sort(v.begin(), v.end());
        size_t N = v.size(), i = 0;
        while (i < N) {
            size_t k = i + 1;
            u32 offi = v[i] >> 10;
            while (k < N && (v[k] >> 10) == offi) k++;
            size_t L = k - i;
            if (L > maxrun) maxrun = L;
            if (L == 1) {
                u32 key = v[i] & 1023;
                unsigned o3 = key & 1, ell = (key >> 1) & 15, j = key >> 5;
                delta[2 * o3][ell][j]++;
                hsingle[o3][ell][j]++;
            } else {
                for (size_t a = i; a < k; a++) {
                    u32 ka = v[a] & 1023;
                    unsigned oa = ka & 1, la = (ka >> 1) & 15, ja = ka >> 5;
                    for (size_t c = i; c < k; c++) {
                        u32 kc = v[c] & 1023;
                        unsigned oc = kc & 1, lc = (kc >> 1) & 15, jc = kc >> 5;
                        delta[oa + oc][la > lc ? la : lc][ja > jc ? ja : jc]++;
                    }
                }
                for (int h = 0; h < NH; h++) {
                    u64 cnt[2][16];
                    memset(cnt, 0, sizeof(cnt));
                    for (size_t a = i; a < k; a++) {
                        u32 ka = v[a] & 1023;
                        if ((ka >> 5) <= hs[h]) cnt[ka & 1][(ka >> 1) & 15]++;
                    }
                    u64 A = 0, B = 0, N0 = 0;
                    for (int l = 0; l < 16; l++) {
                        A += cnt[0][l] + cnt[1][l];
                        B += cnt[1][l];
                        N0 += cnt[0][l];
                        u64 tv[3] = {A, B, N0};
                        for (int w = 0; w < 3; w++) {
                            u64 t = tv[w];
                            if (t == 0) continue;
                            int cls = w * 16 + l;
                            if (t < (u64)TCAP)
                                hist[h][cls][t]++;
                            else
                                hbig[h][cls][t]++;
                        }
                    }
                }
            }
            i = k;
        }
    }
    // single-input values enter the histograms with t = 1
    for (int h = 0; h < NH; h++)
        for (int o = 0; o < 2; o++)
            for (int l = 0; l < 16; l++)
                for (u64 j = 0; j <= hs[h]; j++) {
                    u64 c = hsingle[o][l][j];
                    if (!c) continue;
                    for (int k = l; k < 16; k++) {
                        add(hist[h][k][1], c);
                        add(hist[h][(o == 1 ? 16 : 32) + k][1], c);
                    }
                }

    // cumulative reports
    printf("X %d", J);
    for (u64 x : xs) printf(" %llu", x);
    printf("\n");
    printf("RECORDS %llu\nMAXS %llu\nCLIPPED %llu\nMAXRUN %llu\nWBITS %d\nMODE %d\n", records,
           maxs, clipped, maxrun, wbits, mode);
    u64 cp = 0, c2 = 0;
    for (int j = 0; j < J; j++) {
        add(cp, nprime[j]);
        add(c2, nomega2[j]);
        printf("PRIMES %d %llu\nOMEGA2 %d %llu\n", j, cp, j, c2);
    }
    static const char* names[3] = {"D", "DF", "DN"};
    for (int cls = 0; cls < NCLS; cls++) {
        int w = cls / 16, k = cls % 16;
        u64 R = 0;
        u128 C = 0;
        for (int j = 0; j < J; j++) {
            for (int l = 0; l <= k; l++) {
                if (w != 2) add(R, rcount[1][l][j]);
                if (w != 1) add(R, rcount[0][l][j]);
                if (w != 2) C += delta[2][l][j];
                if (w == 0) C += delta[1][l][j];
                if (w != 1) C += delta[0][l][j];
            }
            printf("R %s%d %d %llu\nC %s%d %d %s\n", names[w], k, j, R, names[w], k, j,
                   decimal(C).c_str());
        }
    }
    for (int h = 0; h < NH; h++)
        for (int cls = 0; cls < NCLS; cls++) {
            int w = cls / 16, k = cls % 16;
            for (int t = 1; t < TCAP; t++)
                if (hist[h][cls][t])
                    printf("H %llu %s%d %d %llu\n", hs[h], names[w], k, t, hist[h][cls][t]);
            for (auto& kv : hbig[h][cls])
                printf("H %llu %s%d %llu %llu\n", hs[h], names[w], k, kv.first, kv.second);
        }
    printf("END\n");
    return 0;
}
