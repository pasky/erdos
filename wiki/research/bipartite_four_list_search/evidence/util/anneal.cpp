// Simulated-annealing hunt for a bad signed four-list system (discovery only, not evidence).
//
// State: V k-subsets of an N-colour palette, each on side L or R, pairwise distinct
// when crossDup = 0. With crossDup = 1, replacements reject same-side repeats,
// but side flips can introduce them. This discovery limitation is retained so
// the recorded searches remain reproducible; explicit witnesses need a checker.
// cnt[T] = #{left blocks disjoint from T} + #{right blocks inside T}, for all T.
// U = #{T : cnt[T] == 0}; objective = U + w * #{uncovered colour pairs}.
// A state with U == 0 is a bad assignment on the complete bipartite graph
// (every palette subset misses a left list or contains a right list); it must be
// re-checked by an independent program before any use.
//
// build: clang++ -O2 -std=c++17 -o output/anneal anneal.cpp
// usage: anneal N K V seed restarts steps T0 T1 w amin amax outprefix [init [dumpU [crossDup]]]
//   init: 0 = random blocks; 1 = AG(2,4) + point at infinity seeds (N=17, K=4, V=26)
//   dumpU: write the best state of a restart as JSON when its U is at most dumpU (default 2)
//   crossDup: 1 lets a list sit once on each side (default 0: all lists distinct)
//   Keep 0 <= amin <= amax <= V for a valid internal side counter. The
//   permissive amax=100 probes initialize it incorrectly when V<50; U still
//   counts uncovered subsets of the actual state, and proves no exclusion.
// Each restart reseeds from the printed seed, so a restart is reproducible from its line.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cmath>
#include <vector>
#include <random>
#include <algorithm>
#include <string>

static int N, K, V;
static uint32_t FULL;
static std::vector<uint8_t> cnt;
static long long U;
static std::vector<int> pairCnt;  // N*N
static long long uncPairs;

static inline void addLeft(uint32_t A, int d) {  // T subset of ~A
  uint32_t C = FULL & ~A;
  uint32_t s = C;
  while (true) {
    uint8_t &c = cnt[s];
    if (d > 0) { if (c == 0) U--; c++; } else { c--; if (c == 0) U++; }
    if (s == 0) break;
    s = (s - 1) & C;
  }
}
static inline void addRight(uint32_t B, int d) {  // T superset of B
  uint32_t C = FULL & ~B;
  uint32_t s = C;
  while (true) {
    uint8_t &c = cnt[s | B];
    if (d > 0) { if (c == 0) U--; c++; } else { c--; if (c == 0) U++; }
    if (s == 0) break;
    s = (s - 1) & C;
  }
}
static inline void addPairs(uint32_t X, int d) {
  for (int i = 0; i < N; i++) if (X >> i & 1)
    for (int j = i + 1; j < N; j++) if (X >> j & 1) {
      int &p = pairCnt[i * N + j];
      if (d > 0) { if (p == 0) uncPairs--; p++; } else { p--; if (p == 0) uncPairs++; }
    }
}
static inline void place(uint32_t X, int side, int d) {
  if (side == 0) addLeft(X, d); else addRight(X, d);
  addPairs(X, d);
}

int main(int argc, char **argv) {
  if (argc < 13) { fprintf(stderr, "usage\n"); return 2; }
  N = atoi(argv[1]); K = atoi(argv[2]); V = atoi(argv[3]);
  unsigned seed = (unsigned)atol(argv[4]);
  int restarts = atoi(argv[5]);
  long long steps = atoll(argv[6]);
  double T0 = atof(argv[7]), T1 = atof(argv[8]), w = atof(argv[9]);
  int amin = atoi(argv[10]), amax = atoi(argv[11]);
  std::string outp = argv[12];
  int init = argc > 13 ? atoi(argv[13]) : 0;
  long long dumpU = argc > 14 ? atoll(argv[14]) : 2;
  int crossDup = argc > 15 ? atoi(argv[15]) : 0;  // 1: a block may sit once on each side
  FULL = (N == 32) ? 0xffffffffu : ((1u << N) - 1);
  cnt.assign(1u << N, 0);
  pairCnt.assign(N * N, 0);
  std::mt19937_64 rng(seed);
  auto rnd = [&](int m) { return (int)(rng() % (uint64_t)m); };
  auto randBlock = [&]() {
    uint32_t X = 0; int c = 0;
    while (c < K) { int x = rnd(N); if (!(X >> x & 1)) { X |= 1u << x; c++; } }
    return X;
  };
  long long globalBest = -1;
  std::mt19937_64 master(seed);
  for (int r = 0; r < restarts; r++) {
    rng.seed(seed);
    std::fill(cnt.begin(), cnt.end(), 0);
    std::fill(pairCnt.begin(), pairCnt.end(), 0);
    U = 1LL << N; uncPairs = (long long)N * (N - 1) / 2;
    std::vector<uint32_t> blk(V);
    std::vector<int> side(V);
    if (init == 1 && N == 17 && K == 4 && V == 26) {
      // AG(2,4): points (x,y) in GF(4)^2 -> index 4x+y; GF(4) = {0,1,w,w^2} as 0..3, add = xor
      static const int mul[4][4] = {{0,0,0,0},{0,1,2,3},{0,2,3,1},{0,3,1,2}};
      std::vector<uint32_t> lines;
      for (int m = 0; m < 4; m++) for (int b = 0; b < 4; b++) {  // y = m x + b
        uint32_t L = 0; for (int x = 0; x < 4; x++) L |= 1u << (4 * x + (mul[m][x] ^ b)); lines.push_back(L);
      }
      for (int c = 0; c < 4; c++) { uint32_t L = 0; for (int y = 0; y < 4; y++) L |= 1u << (4 * c + y); lines.push_back(L); }
      // random relabelling of the 16 affine points
      std::vector<int> perm(16); for (int i = 0; i < 16; i++) perm[i] = i;
      std::shuffle(perm.begin(), perm.end(), rng);
      for (int i = 0; i < 20; i++) { uint32_t L = 0; for (int p = 0; p < 16; p++) if (lines[i] >> p & 1) L |= 1u << perm[p]; blk[i] = L; }
      // six triples through point 16 covering all 16 points: a random partition into 5 triples + 1 point, plus 2 more
      std::vector<int> pts(16); for (int i = 0; i < 16; i++) pts[i] = i;
      std::shuffle(pts.begin(), pts.end(), rng);
      for (int t = 0; t < 5; t++) blk[20 + t] = (1u << 16) | (1u << pts[3*t]) | (1u << pts[3*t+1]) | (1u << pts[3*t+2]);
      uint32_t last; do { last = (1u << 16) | (1u << pts[15]); int c = 1; while (c < 3) { int x = rnd(16); if (!(last >> x & 1)) { last |= 1u << x; c++; } } }
      while (std::find(blk.begin(), blk.begin() + 25, last) != blk.begin() + 25);
      blk[25] = last;
    } else {
      for (int i = 0; i < V; i++) {
        uint32_t X; do { X = randBlock(); } while (std::find(blk.begin(), blk.begin() + i, X) != blk.begin() + i);
        blk[i] = X;
      }
    }
    int a = (amin + amax) / 2;
    std::vector<int> idx(V); for (int i = 0; i < V; i++) idx[i] = i;
    std::shuffle(idx.begin(), idx.end(), rng);
    for (int i = 0; i < V; i++) side[idx[i]] = (i < a) ? 0 : 1;
    int nleft = a;
    for (int i = 0; i < V; i++) place(blk[i], side[i], +1);
    auto obj = [&]() { return (double)U + w * (double)uncPairs; };
    double cur = obj(), best = cur;
    std::vector<uint32_t> bestBlk = blk; std::vector<int> bestSide = side; long long bestU = U, bestP = uncPairs;
    for (long long st = 0; st < steps; st++) {
      double temp = T0 * pow(T1 / T0, (double)st / (double)steps);
      int mv = rnd(10);
      int i = rnd(V);
      uint32_t oldX = blk[i]; int oldS = side[i];
      uint32_t newX = oldX; int newS = oldS;
      if (mv < 2) {  // flip side
        newS = 1 - oldS;
        int nl = nleft + (newS == 0 ? 1 : -1);
        if (nl < amin || nl > amax) continue;
      } else if (mv < 9) {  // replace one colour
        int out, in;
        do { out = rnd(N); } while (!(oldX >> out & 1));
        do { in = rnd(N); } while (oldX >> in & 1);
        newX = (oldX & ~(1u << out)) | (1u << in);
      } else {  // replace the whole block
        newX = randBlock();
      }
      if (newX != oldX) {
        bool dup = false; for (int j = 0; j < V; j++) if (j != i && blk[j] == newX && (!crossDup || side[j] == newS)) { dup = true; break; }
        if (dup) continue;
      }
      place(oldX, oldS, -1); place(newX, newS, +1);
      double nw = obj();
      double dlt = nw - cur;
      if (dlt <= 0 || std::uniform_real_distribution<double>(0, 1)(rng) < exp(-dlt / temp)) {
        blk[i] = newX; if (newS != oldS) nleft += (newS == 0 ? 1 : -1); side[i] = newS; cur = nw;
        if (cur < best) { best = cur; bestBlk = blk; bestSide = side; bestU = U; bestP = uncPairs; }
        if (U == 0 && uncPairs == 0) break;
      } else {
        place(newX, newS, -1); place(oldX, oldS, +1);
      }
    }
    int bl = 0; for (int i = 0; i < V; i++) bl += bestSide[i] == 0;
    printf("restart %d seed %u bestU %lld uncPairs %lld left %d\n", r, seed, bestU, bestP, bl);
    fflush(stdout);
    if (globalBest < 0 || bestU < globalBest) globalBest = bestU;
    if (bestU <= dumpU) {
      std::string fn = outp + "_r" + std::to_string(r) + "_U" + std::to_string(bestU) + ".json";
      FILE *f = fopen(fn.c_str(), "w");
      fprintf(f, "{\"n\": %d, \"k\": %d, \"seed\": %u, \"restart\": %d, \"U\": %lld, \"uncovered_pairs\": %lld, \"left\": [", N, K, seed, r, bestU, bestP);
      bool first = true;
      for (int s = 0; s < 2; s++) {
        if (s == 1) { fprintf(f, "], \"right\": ["); first = true; }
        for (int j = 0; j < V; j++) if (bestSide[j] == s) {
          fprintf(f, "%s[", first ? "" : ", "); first = false; bool f2 = true;
          for (int c = 0; c < N; c++) if (bestBlk[j] >> c & 1) { fprintf(f, "%s%d", f2 ? "" : ", ", c); f2 = false; }
          fprintf(f, "]");
        }
      }
      fprintf(f, "]}\n"); fclose(f);
    }
    // keep going with next restart using a new derived seed
    seed = (unsigned)(master() & 0x7fffffff);
  }
  printf("globalBestU %lld\n", globalBest);
  return 0;
}
