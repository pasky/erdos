---
name: research/leads/aliquot_collision_density/evidence
title: Evidence
desc: Exact census of collisions s(n) = s(n') through 10^10 in classes cut out by s(n)/n, by the number of prime factors and by the largest prime factor, with an independent small-range reference and external count checks.
created: 2026-10-16T14:07:43Z
updated: 2026-10-16T23:12:27Z
---

# Evidence

[[research/leads/aliquot_collision_density/_index|..]]

[[research/leads/aliquot_collision_density/evidence/verify/_index|verify/]]: Independent analytic review and separate grading, with exact subjects and source-interface limits.

***

The [entry point](main.py) builds the compiled census
[`util/census.cpp`](util/census.cpp) and recomputes the findings recorded in
[`assets/census.json`](assets/census.json), through $10^9$ in both modes
below, and in [`assets/census_1e10.json`](assets/census_1e10.json), through
$10^{10}$ in mode 0. The [research account](../_index.md) reports them.

**What the census computes.** A segmented sieve computes $\sigma(n)$ exactly
for every $n\le X$. Each composite $n$ is written, with the low bits of
$s(n)=\sigma(n)-n$, its level $\ell(n)=\min(15,\min\{k\ge0:2^ks(n)\ge n\})$, a
flag and the index of the first checkpoint at least $n$, into a bucket file
chosen by the high bits of $s(n)$. Each bucket is sorted, and every ordered
pair of inputs with equal values, the diagonal included, is tallied by the
number of flagged inputs in the pair, the larger level and the larger
checkpoint index. Prefix sums then give, at every checkpoint
$x=\lfloor10^{3+j/4}\rfloor$ ($j=0,\dots,24$ through $10^9$ and
$j=0,\dots,28$ through $10^{10}$), the input count $R$ and the
ordered pair count $C=\sum_mr_x(m)^2$ for the classes $D_k$ of composites with
$2^ks(n)\ge n$ ($D_{15}$: all composites) and their flagged and unflagged
parts $DF_k$ and $DN_k$, together with fiber-size histograms at the decades.
Mode 0 flags the inputs with at least three prime factors counted with
multiplicity, so $DF_{15}$ is the class $T$ of the account; mode 1 flags the
inputs whose largest prime factor exceeds their square root. Primes and $1$
are counted but not recorded. All arithmetic is exact unsigned integer
arithmetic. The finite result has no unbounded mathematical conclusion.

**Coverage and bounds.** Every integer from $1$ through $X$ is factored in
one segment, and every composite produces one record. A value $s(n)$ has
one bucket and one low-bit key, so all its records are processed together.
Pairing every record in that group with every record, including itself,
counts precisely the ordered pairs. The maximum of the two checkpoint tags
is the first checkpoint containing both inputs; the maximum level is the
first restricted class containing both. These observations justify the
prefix sums, rather than treating histogram agreement alone as a coverage
argument.

The program refuses $X>2\cdot10^{10}$. Individual counts are at most $X$;
$\sigma(n)\le X(1+\log X)<25X$; and each prime-power intermediate is at
most $X\sqrt X$. These fit in 64 unsigned bits. Pair counts use 128 bits,
since $X^2<4.01\cdot10^{20}<2^{69}$ on the supported domain and need not
fit in 64 bits. The packing uses at most 22 value bits and 10 tag bits.
The sieve holds $2^{18}$ integers at a time. There are at most $2^{16}$
bucket buffers of 8192 four-byte records, and a sorted bucket is capped at
$2^{29}$ records (2 GiB). The buffers are released before sorting. An
exceeded bucket cap terminates with failure; it never truncates the data.
No array of all $n\le X$ or of all possible $s(n)$ is kept in memory.

**Checked clauses.**

1. Through $x=10^5$ the compiled census agrees exactly, in both modes, with
   [`util/brute.py`](util/brute.py), which sums proper divisors by a divisor
   sieve and counts collisions with dictionaries. The comparison uses bucket
   widths of $2^6$ and $2^5$, so that the bucket logic is exercised across
   thousands of boundaries, and covers every $R$, $C$, histogram, prime count
   and two-prime-factor count at the 9 checkpoints. A further direct
   comparison at $2^{18}-1$, $2^{18}$ and $2^{18}+1$ checks both sides of
   the first segmented-sieve boundary in both modes.
2. The prime counts at $10^3,\dots,10^9$ equal the known values of
   $\pi(10^k)$, and the counts of $n\le10^k$ with exactly two prime factors
   equal the known values $299, 2625, 23378, 210035, 1904324, 17427258$ and
   $160788536$; through $10^{10}$ also $\pi(10^{10})=455052511$ and
   $1493776443$. Below $2^{30}$ no level is clipped at 15, as
   $s(n)>\sqrt n$ for composite $n$ requires.
3. At every checkpoint, $C\ge R$ with $C-R$ even, $R$ and $C$ are
   nondecreasing in $x$ and in $k$, $R(D_k)=R(DF_k)+R(DN_k)$,
   $C(D_k)\ge C(DF_k)+C(DN_k)$, and at the decades every histogram has first
   moment $R$ and second moment $C$.
4. Every recorded count and histogram in both assets is reproduced
   exactly, and their overlapping mode-0 data through $10^9$ agree.
   Executed checkpoints agree with the requested ones, and the number of
   records equals $X-1-\pi(X)$ and the all-composite input count.

Run from the repository root:

```sh
uv run --no-sync python wiki/research/leads/aliquot_collision_density/evidence/main.py
```

It needs the root `tools` package and a C++17 compiler with unsigned 128-bit
integer support on the path. The default runs mode 0 through $10^{10}$ and
mode 1 through $10^9$, checking both assets in about forty minutes on one
core. Its scratch files, about 40 GB at the peak, go under the ignored
`output/` folder unless `--workdir` names another place. `--quick` runs
clause 1 and checks clauses 2 to 4 through $10^7$ only, in about thirty
seconds. `--top-exponent 9` checks only the first asset through $10^9$ in
both modes, in about five minutes. Both reduced modes explicitly leave the
$10^{10}$ extension unchecked. Every failed
check exits nonzero, including under `python -O`, and a single changed
recorded value fails clause 4. A negative control increasing the recorded
$C_{D_0}(10^3)$ by one in a scratch copy triggers that clause and exits 1
under `python -O`.

[`produce.py`](produce.py) runs the same census and writes a proposed
findings file to `output/` (`--top 10 --modes 0` for the second asset); a
file becomes an asset only when copied there.

**Limitations.** The census is exact but finite. It proves no asymptotic
statement about $C/x$, and the account's reading of its trend is exploratory.
The direct reference uses a different algorithm written by the author; it
does not constitute independent review or confer a verification tier.
