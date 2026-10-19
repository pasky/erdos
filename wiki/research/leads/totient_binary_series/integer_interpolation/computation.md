---
name: research/leads/totient_binary_series/integer_interpolation/computation
title: Finite Integer Interpolation Certificates
desc: |
  Exact finite certificates for the first full shifted-totient integer image
  and weighted costs of specified inhomogeneous solutions.
sources: []
problems:
- 249
review_status: unreviewed
created: 2026-09-17T08:47:10Z
updated: 2026-09-17T08:47:10Z
---

***

This computation serves the quantitative question in the
[[research/leads/totient_binary_series/integer_interpolation/_index|integer
interpolation argument]]. Its finite outputs concern the nine orders
$k\in\{3,4,8,12,16,24,32,48,64\}$ and indices at most $4096$. They do
not prove a coefficient optimum, an asymptotic estimate, or irrationality.
The certificates and their checks are author-produced evidence, without
independent review or formal verification.

## Exact contract

Set $B=k+2$. For rows $s=-k+1,\ldots,k$ in that order and columns
$n=B,\ldots,R$, use the integer matrix
$A_R[s,n]=\varphi(n+s)/2$. The smallest totient argument is three,
so every entry is integral. A successful endpoint is retained with an
integer matrix $Y$ of shape $(R-B+1)\times2k$ satisfying $A_RY=I$.
It is accompanied by a modulus $d\ge2$ and a row $a\not\equiv0\pmod d$
with $aA_{R-1}\equiv0\pmod d$.

The first relation proves that every standard basis vector belongs to the
integer image. The second proves the preceding image proper: a nonzero
homomorphism $\mathbb Z^{2k}\to\mathbb Z/d\mathbb Z$ cannot vanish on
all of $\mathbb Z^{2k}$. Prefixes are nested, so these two relations
certify the least endpoint without replaying the discovery search.
Dimension already requires $R\ge3k+1$. Rational rank alone does not
establish this property. Composite obstruction moduli are accepted.

A cap obstruction at $R=4096$ would instead certify every prefix through
that cap proper. A missing witness or unfinished computation certifies
nothing about existence. The consumer distinguishes those outcomes;
missing or uncertified input causes the retained checker to fail.

Every retained target solution is a finite integer vector supported on
$B\le n\le4096$, checked against all $2k$ equations

$$
\sum_ny_n\varphi(n+s)=
\begin{cases}0,&-k<s\le0,\\-2\varphi(s),&1\le s\le k.\end{cases}
$$

Thus the normalized target is $t_s=0$ or $-\varphi(s)$, respectively;
in particular $t_1=-1$. The cost is recomputed from the same coefficients:

$$
C_k(y)=2(k+2)+\sum_n|y_n|(n+k+2).
$$

The record gives the actual nonzero support, maximum absolute coefficient,
cost, reduced exact ratio $C_k/2^k$, and the largest excluded positive
denominator, $\lfloor(2^k-1)/C_k\rfloor$. Zero means this criterion
excludes no positive denominator. Its interpretation uses precisely the
parent argument's strict inequality $bC_k<2^k$ and complete infinite-tail
bound. A support used for cost reduction can extend beyond the first
full-image prefix, and is recorded separately. No minimum-cost claim is
made.

## Certificate format and replay

The [checker](evidence/main.py) reads `evidence/assets/kNNN.json.gz` for
every listed order, independently of the current directory. Schema 1
records `k`, `B`, `cap`, ordered `shifts`, and `status`. For `full_image`,
`minimal_R` fixes the dense right-inverse dimensions and `predecessor`
contains `R`, `modulus`, and `row`. For `proper_at_cap`, `cap_obstruction`
contains the same obstruction fields. `solutions` contains labeled
inhomogeneous witnesses; each gives its allowed support endpoint `R`,
sorted nonzero `[n,y_n]` pairs, and recomputed statistics. The `support`
triple is `[minimum index, maximum index, cardinality]`; `ratio` is the
reduced `[numerator,denominator]` pair. Labels distinguish constructions,
not mathematical standing.

Only exact JSON integers are accepted for mathematical data. Duplicate
object keys, booleans masquerading as integers, missing orders, invalid
dimensions, support outside the domain, a zero annihilator, and any
failed equation or statistic cause nonzero exit. Totients are recomputed
by trial division; small and cap-boundary values are also compared with
direct coprime counts. The checker multiplies the complete declared
matrices, checks every predecessor column, and recomputes every target
and cost. It imports no discovery algebra package.

From the repository root, using its ordinary prepared environment:

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/main.py
uv run --no-sync python -O wiki/research/leads/totient_binary_series/integer_interpolation/evidence/main.py
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/controls.py
```

Default replay checks all nine orders. `--quick` checks exactly $k=3,4$
and supplies no coverage for the other seven. The
[failure controls](evidence/controls.py) replay those two valid inputs and
an additional valid composite-modulus obstruction and twelve deliberately
corrupted cases, both normally and with optimization.
They exercise the actual checker, including a changed right inverse, zero
obstruction, wrong predecessor, doubled target, altered cost, invalid
support, wrong shifts, invalid modulus, noninteger entry, endpoints exceeding
the cap, and missing order. They write only temporary ignored output. The
main replay needs
only Python's standard library and the root `tools` reporting helpers.

## Discovery and its limits

The optional [producer](evidence/produce.py) uses python-flint 0.9.0 on
one numerical thread. It sieves totients, brackets and bisects the
monotone full-image predicate using row Hermite normal forms of
$A_R^{\mathsf T}$, and obtains $UA_R^{\mathsf T}=H$ at the first endpoint.
When the first $2k$ rows of $H$ are the identity, the corresponding rows
of $U$, transposed, give $Y$. It checks the transform relation in exact
arithmetic during discovery. For a full-rank proper predecessor with square
row basis $H_0$, choose a nonintegral column $q=H_0^{-1}e_j$, clear its
denominators with $d$, and use the row $a=(dq)^{\mathsf T}\pmod d$.
Then $H_0a^{\mathsf T}\equiv0\pmod d$
and $a\not\equiv0\pmod d$. This avoids factoring the determinant.
A rank-deficient predecessor instead supplies a nullvector modulo two.
The retained checker verifies the resulting relations anew;
no normal-form verdict is itself a certificate.

The transformation interface is documented by
[python-flint](https://python-flint.readthedocs.io/en/latest/fmpz_mat.html)
and [FLINT](https://flintlib.org/doc/fmpz_mat.html).

The [coset search](evidence/reduce.py) constructs a solution and integer
kernel rows at each endpoint $R=4k+2,6k+2,8k+2$. It weights coordinate
$n$ by $n+k+2$, reduces the weighted kernel rows with LLL, and uses
nearest-plane rounding to propose integer kernel combinations to subtract
from the initial solution. LLL and MPFR nearest-plane selection are
heuristic discovery; no reduction-quality guarantee is consumed. The code
checks that the proposed kernel directions are integral and satisfy the
exact homogeneous equations, and checks the final inhomogeneous equations.
Up to eight further passes try exact improving integer multiples of each
kernel direction, using weighted medians of the one-dimensional absolute
value cost. These steps preserve the affine integer coset. They do not
exhaust it or prove a minimum. All retained proposals then pass the separate
checker, which recomputes their entire cost.

Discovery writes candidates to
ignored `evidence/output/`. Its environment and intermediate state are
not retained evidence.

The observed discovery environment used Python 3.12.13, python-flint 0.9.0,
fpylll 0.6.4, and cysignals 1.12.6. Both numerical libraries were limited
to one thread. A separate optional environment, created outside the repository's lockfile
with Python 3.12, python-flint 0.9.0, fpylll 0.6.4 and cysignals 1.12.6, can
reproduce discovery without changing the repository environment; run the
two discovery programs from it with the numerical libraries limited to one
thread, then replay the retained certificates with the repository's own
environment:

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/produce.py
python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/reduce.py --factors 4 6 8
uv run --no-sync python wiki/research/leads/totient_binary_series/integer_interpolation/evidence/main.py --assets wiki/research/leads/totient_binary_series/integer_interpolation/evidence/output
```

The current endpoint production took under one second, and the 27 coset
reductions took about 45 seconds in total on one core.
The retained certificates are sufficient for replay; repeating this optional
discovery is unnecessary for acceptance. Different heuristic reductions
may produce different valid costs and are accepted only by their exact
relations, not by matching a discovery transcript.

## Results and remaining obligations

All nine least endpoints are certified. In this finite list, only one,
two, or three columns beyond the dimension lower bound are needed.
The complete prefix question through 4096 is settled for these orders by
the endpoint and predecessor relations and nesting. There is no unfinished
order or cap-only result.

The following chooses the least cost among the four retained solutions
for each order: the initial right-inverse solution and the three coset
searches. The support column gives the smallest and largest nonzero index
and the number of nonzero coefficients; the full sparse support is in
the corresponding certificate. $R_y$ is the allowed support endpoint of
the selected search, which may exceed its actual last nonzero index.
$b_{\max}=\lfloor(2^k-1)/C_k\rfloor$ has the literal finite meaning
specified above.

| $k$ | Least $R$ | $R_y$ | Nonzero support range (count) | $\max_n\lvert y_n\rvert$ | $C_k$ | Exact $C_k/2^k$ | $b_{\max}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 11 | 20 | 7–20 (5) | 2 | 109 | 109/8 | 0 |
| 4 | 15 | 26 | 6–23 (8) | 2 | 230 | 115/8 | 0 |
| 8 | 26 | 66 | 10–66 (21) | 3 | 967 | 967/256 | 0 |
| 12 | 38 | 74 | 15–69 (36) | 5 | 3167 | 3167/4096 | 1 |
| 16 | 51 | 130 | 18–102 (66) | 9 | 9776 | 611/4096 | 6 |
| 24 | 76 | 146 | 26–146 (108) | 19 | 38364 | 9591/4194304 | 437 |
| 32 | 100 | 258 | 34–258 (156) | 39 | 107670 | 53835/2147483648 | 39890 |
| 48 | 146 | 386 | 50–386 (220) | 123 | 727704 | 90963/35184372088832 | 386798721 |
| 64 | 194 | 386 | 66–386 (284) | 314 | 2433103 | 2433103/18446744073709551616 | 7581571381774 |

As an exposed small example, the selected $k=3$ solution is
$y_7=2$, $y_{10}=y_{11}=y_{14}=-1$, $y_{20}=1$, and zero elsewhere.
Its six unnormalized row products are $(0,0,0,-2,-2,-4)$ and its cost is
$10+2\cdot12+15+16+19+25=109$.

The three support comparisons give the following costs. Every entry is
backed by its own retained inhomogeneous witness; extending the search
interval does not guarantee that this heuristic finds a cheaper vector.

| $k$ | $R=4k+2$ | $R=6k+2$ | $R=8k+2$ |
| --- | --- | --- | --- |
| 3 | 155 | 109 | 109 |
| 4 | 291 | 230 | 298 |
| 8 | 3432 | 1448 | 967 |
| 12 | 15490 | 3167 | 3957 |
| 16 | 36165 | 9886 | 9776 |
| 24 | 224065 | 38364 | 38640 |
| 32 | 557987 | 120384 | 107670 |
| 48 | 3501269 | 856492 | 727704 |
| 64 | 11921743 | 2433103 | 2731713 |

The best retained normalized cost rises from $k=3$ to $k=4$, then falls
at every sampled step through $k=64$. This answers the finite comparison
question only. The search uses three support intervals per order, ending
no later than 514; it does not minimize over those intervals or over every
support through 4096. No bound uniform in $k$ or certified minimum cost
is established. The parent's sufficient asymptotic size
condition, and irrationality itself, remain unresolved.

Full normal and optimized replay each passed 55 named checks, covering
all nine right inverses, all nine predecessor obstructions, and all 36
target/cost witnesses. Each replay took about 0.2 seconds. The positive
and corrupted-input controls passed all 28 expected outcomes in about
one second. These are author execution checks, not independent review.
