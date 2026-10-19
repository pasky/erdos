---
name: research/erdos_699/methods/details/prime_power_strips
title: "Erdős 699: certifying entire strips of prime-power exponents"
desc: "A modular coefficient bound replaces the quadratic exponent search by a short, exactly checked covering of exponent quadrants; height caps with millions of digits become practical."
created: 2026-09-22T04:59:21Z
updated: 2026-09-22T04:59:21Z
---

# Erdős 699: certifying entire strips of prime-power exponents

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/finite_prime_pairs|Finite prime-pair certificates]]

***

The finite prime-pair inequalities can be checked without visiting every
pair of exponents. A single modular inverse gives coefficient lower bounds
throughout two entire strips of larger exponents. Removing those strips
leaves another quadrant, so the argument repeats.

For example, the exact certificates for differences at most 19 and heights
at most $10^{4\,000\,000}$ give:

| Pair | Lower height threshold | Modular-inverse anchors | Exact boundary pairs |
| --- | ---: | ---: | ---: |
| $2,3$ | $5104$ | $61$ | $23$ |
| $17,19$ | $4333$ | $51$ | $2$ |

Each row proves $\max(u,v)^3\ge\min(p^a u,q^b v)$ throughout the stated
height range. These are the same types of finite-range inequalities used
by the earlier interval proofs. They make no assertion beyond the stated
height cap.

The [checker](../../computations/erdos_699_prime_pair_strips.py) and
[retained certificates](../../computations/erdos_699_prime_pair_strips_benchmark.json)
record every anchor, its certified advances, and every exceptional minimal
solution. The observed number of anchors is small; a logarithmic worst-case
complexity bound is not asserted.

The completed binomial proofs use four further retained collections:

| Use | Prime graph | Exponent | Height cap | Difference bound |
| --- | --- | ---: | --- | ---: |
| [Index 18](../../computations/erdos_699_prime_pair_strips_k6.json) | Complete graph on $2,3,5,7,11,13$ | $1/3$ | $10^{1\,200\,000}$ | $19$ |
| [Index 15](../../computations/erdos_699_prime_pair_strips_15.json) | Same complete graph | $1/3$ | $10^{15\,170\,264}$ | $14$ |
| [Index 20](../../computations/erdos_699_prime_pair_strips_20.json) | Triangles $\{2,3,5\}$ and $\{7,11,13\}$, plus $17,19$ | $2/5$ | $10^{27\,027\,659}$ | $19$ |
| [Index-10 extensions](../../computations/erdos_699_prime_pair_strips_10_global.json) | Pairs $3,7$ and $5,7$ | $2/5$ | $10^{15\,000\,000}$ | $9$ |

The rational-exponent version is proved below. The
[complete interval proof](../../proofs/details/further_interval_certificates.md)
explains how these finite-range statements combine with the independently
proved infinite tails.

## 1. A coefficient bound on an entire strip

Fix distinct primes $p,q$, a difference bound $D$, and an anchor

$$
P=p^a>D,\qquad Q=q^b>D.
$$

For each signed $d$ with $0<|d|\le D$, let

$$
Pu_d-Qv_d=d,\qquad 1\le u_d<Q,\quad1\le v_d<P
$$

be the unique minimal positive solution. Put

$$\mu_u=\min_{0<|d|\le D}u_d,\qquad
  \mu_v=\min_{0<|d|\le D}v_d.$$

Consider any larger exponents and any positive solution

$$P'=Pp^A,\qquad Q'=Qq^B,\qquad P'u'-Q'v'=d,
\qquad A,B\ge0.$$

Reduction modulo $Q$ and cancellation of the unit $P$ give

$$
p^A u'\equiv u_d\pmod Q.
$$

Since $p^A u'>0$ and $u_d$ is the least positive residue, this implies

$$
u'\ge u_d/p^A\ge\mu_u/p^A.\tag{1}
$$

Consequently, if an integer $A_0\ge0$ satisfies

$$
\mu_u^2\ge Pp^{3A_0},\tag{2}
$$

then every exponent pair in the **entire strip**

$$
a\le a'\le a+A_0,\qquad b'\ge b
$$

satisfies $u'^2\ge P'$. It follows that

$$\max(u',v')^3\ge u'^3\ge P'u'
\ge\min(P'u',Q'v').\tag{3}$$

There is no upper restriction on $b'$ in this implication. Symmetrically,
if $B_0\ge0$ satisfies

$$
\mu_v^2\ge Qq^{3B_0},\tag{4}
$$

then the same desired inequality holds throughout
$a'\ge a$, $b\le b'\le b+B_0$.

## 2. Covering the remaining quadrant

Start at the first exponents for which $p^a,q^b>D$. The smaller-power
cases are already covered by the elementary implication

$$h^2\ge D^3\ \Longrightarrow\ \max(u,v)^3\ge h,
\qquad h=\min(p^a u,q^b v),$$

proved in the earlier prime-pair note. Zero differences are also covered
there by coprimality.

At each anchor, find the largest nonnegative $A_0,B_0$ satisfying (2)
and (4), when they exist. The complement of the union of the two
certified strips, inside the current quadrant, is precisely

$$
a'\ge a+A_0+1,\qquad b'\ge b+B_0+1.
$$

This gives the next anchor. If just one strip is available, advance only
its corresponding exponent; the unadvanced exponent keeps its old lower
bound. Every removed exponent pair has therefore been proved good by
(3), for every positive choice of its cofactors.

If neither strip is available, remove the two boundary lines by exact
minimal-solution checks. These are finite lines: a violating pair must
satisfy

$$
\bigl(\max(P',Q')-D\bigr)^2<\min(P',Q')^3.\tag{5}
$$

Thus, on the vertical line with fixed $P$, only powers
$Q'\le\lfloor\sqrt{P^3}\rfloor+D$ need checking. On the horizontal
line with fixed $Q$, only powers
$P'\le\lfloor\sqrt{Q^3}\rfloor+D$ need checking. The common corner
is checked once. The earlier minimal-solution lemma covers every
nonminimal positive solution automatically.

After those two boundary lines have been removed, advance both exponents
by one. This again leaves precisely one quadrant. The checker records
every exceptional minimal solution on the checked boundaries.

The height cap $T=10^K$ gives exact upper limits on both prime-power
exponents. Once either lower exponent of the remaining quadrant exceeds
its upper limit, the entire bounded domain has been covered. Taking the
lower height threshold above every recorded exceptional height, and above
the elementary small-power threshold, proves the certificate.

## 3. Exact computation

All proof decisions use integer arithmetic. Floating point only proposes
the initial integer logarithms; direct comparisons of integer powers
adjust and certify them. Each strip is accepted only after checking (2)
or (4) exactly.

The standard Python integer backend suffices for moderate caps. The
optional GMP backend performs the same integer operations efficiently on
the much larger powers. The two $10^{4\,000\,000}$ certificates above
each took approximately ten seconds using `gmpy2` 2.3.1. This elapsed time
is descriptive, not part of the proof.

As a comparison with the earlier exhaustive method, the strip checker
was run on all ten retained index-21 prime pairs through $10^{1732}$.
Every exceptional solution, not just the largest height, agreed exactly.
The standard Python backend completed those ten strip certificates in
less than a second.

Reproduce the large certificates with the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt),
including `gmpy2`, installed in the repository's `.venv/`, writing under
the ignored repository `tmp/`:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --pairs 2,3 17,19 --cap 4000000 --difference 19 --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_benchmark.json
```

Compare the regenerated file with the retained one on its mathematical
fields; elapsed times differ between runs.

A boundary-pair budget is an explicit stopping safeguard. Exhausting it
raises an error and supplies no complete certificate.

## 4. Other rational cofactor exponents

The same argument works for any rational $\delta=r/s$ with
$0<r/s\le1/2$. The target inequality becomes

$$
\max(u,v)^s\ge h^r.
$$

Replace (2) by

$$
\mu_u^{s-r}\ge P^r p^{sA_0}.
$$

Then (1) implies $u'^{s-r}\ge P'^r$, and hence
$u'^s\ge(P'u')^r\ge h^r$. The symmetric condition covers the other
strip. The exact boundary-line cutoff is obtained from

$$
\bigl(\max(P',Q')-D\bigr)^{s-r}<\min(P',Q')^s,
$$

and the small-power threshold from $h^{s-r}\ge D^s$.
Nonminimal solutions remain automatically good because $M^2\ge h$ and
$s\ge2r$. These formulas are implemented by the `--exponent` option.

For $\delta=2/5$, differences at most 9 and heights at most $10^{1732}$,
the [retained certificate](../../computations/erdos_699_prime_pair_strips_two_fifths.json)
proves $\max(u,v)^5\ge h^2$ above the following thresholds:

| Pair | $H$ |
| --- | ---: |
| $2,3$ | $1\,449\,982$ |
| $2,5$ | $5626$ |
| $2,7$ | $2\,553\,806\,844$ |
| $3,5$ | $39\,367$ |
| $3,7$ | $1\,226\,908$ |
| $5,7$ | $2\,061\,328\,126$ |

The generalized checker was also compared with an exhaustive exponent-pair
calculation through $10^{12}$ for these six pairs. Every exceptional
minimal solution agreed exactly. The larger certificates are reproduced by:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --pairs 2,3 2,5 2,7 3,5 3,7 5,7 --cap 1732 --difference 9 \
  --exponent 2/5 --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_two_fifths.json
```

Compare the regenerated file with the retained one on its mathematical
fields; elapsed times differ between runs.

## 5. Restricting an exceptional pair to its possible rows

Taking $H$ above the largest exceptional height is convenient, but loses
information. A recorded exception $(x,y)=(P_pu_p,P_qu_q)$ can occur among
the selected numerator positions of an index-$i$ row only if

$$
\max(x,y)\le n\le\min(x,y)+i-1.
$$

This is an interval of at most $i$ integers. Therefore, above the elementary
small-power threshold, an edge remains valid on every row interval that
avoids all of its recorded exceptional row intervals. The bound on the
height cap still applies. This permits using a strong edge below the
largest exceptional height, while omitting it only on the small intervals
where one of its explicit exceptions could occur.

## 6. Reproducing the large application tables

These commands require `gmpy2`, pinned with the other
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt),
in the repository's `.venv/`. They perform exact integer computations and
regenerate, under the ignored repository `tmp/`, the source tables used by
the interval checkers.

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --clique 2 3 5 7 11 13 --cap 1200000 --difference 19 --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_k6.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --clique 2 3 5 7 11 13 --cap 15170264 --difference 14 --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_15.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --pairs 2,3 2,5 3,5 7,11 7,13 11,13 17,19 \
  --cap 27027659 --difference 19 --exponent 2/5 --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_20.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --pairs 3,7 5,7 --cap 15000000 --difference 9 --exponent 2/5 --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_10_global.json
```

Compare each regenerated table with the retained file of the same name
under `computations/` on its mathematical fields; elapsed times differ
between runs.
