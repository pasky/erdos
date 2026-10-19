---
name: research/erdos_699/proofs/details/index_9_baseline
title: "Erdős 699: exact polynomial coverage of all index-9 position assignments"
desc: "Seventy modular interpolation certificates cover 104059 of 104976 labelled position/witness cases; the retained 917 residual cases include every collision not yet covered."
created: 2026-09-22T08:30:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: exact polynomial coverage of all index-9 position assignments

***

**Complete follow-up.** The [index-nine proof](index_9_effective.md) closes all
917 residual root cases below and makes the entire index effective.

The [certificate catalog](../../computations/erdos_699_index_9_baseline.json)
and [checker](../../computations/erdos_699_index_9_baseline.py) cover all
$9^4$ labeled assignments of the maximal positions of primes $2,3,5,7$,
including coinciding positions. For each assignment, they check all sixteen
minimal cofactor vectors supplied by the retained prime-pair estimates.

Of the resulting **104,976 cases**, **104,059** have a positive integer
polynomial certificate. The remaining **917** labeled cases are recorded
explicitly. Twelve have coinciding positions. These are finite
configurations of cofactor exponents and positions, not a finite list of
possible bad triples, and this calculation alone does not prove an
effective bound at index 9.

## The exact gain

Put $H=n-8$, and choose $r_p\in\{0,\ldots,8\}$ maximizing
$v_p(n-r_p)$ for each $p\in\{2,3,5,7\}$. Write

$$
n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)}.
$$

The source graph combines the original symmetric BFT bounds with the
retained [asymmetric pair table](../../computations/erdos_699_bft_asymmetric_pair_table.json).
Its disjunctions imply, beyond an effectively computable common threshold,
that one of the sixteen recorded vectors $v$ satisfies
$u_p\ge H^{v_p/10000}$ for every prime. The checker reconstructs these
vectors from the canonical source tables; it does not read discovery
outputs.

For each row $t$, set

$$
\alpha_t=\begin{cases}
1,&\text{no selected prime has position }t,\\
v_p/10000,&\text{only prime }p\text{ has position }t,\\
0,&\text{at least two selected primes have position }t.
\end{cases}
$$

The last case retains the bound
$\prod_{p:r_p=t}P_p\le n-t$ for the whole prime group.
For nonnegative integer line exponents $h_a$ and row multiplicities $m_t$,
a certificate of interpolation degree $d$ has total degree

$$
D=2\sum_a h_a+\max\{0,d+1\}.
$$

Its exact gain is

$$
\boxed{\sum_{t=0}^8\alpha_tm_t-D.} \tag{1}
$$

The checker requires (1) to be strictly positive, with all comparisons
performed at denominator 10000. The least first-use gain among the
covered cases is $3/10000$. Prime labels are preserved throughout;
there is no inference from sorted cofactor vectors to particular prime
assignments.

## Polynomial construction and ranks

Each record requires residual multiplicity

$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}
$$

at every nonnegative integer point $x+y\le8$. Its symmetric jet matrix
on polynomials of degree at most $d$ has full row rank modulo 251.
All seventy records were checked by exact modular rank calculations.
There are 95,014 jet rows in total; the largest matrix has 9,016 rows and
9,025 columns. Two records need no residual interpolation: their
coordinate-line products already supply all multiplicities, and they
use the convention $d=-1$.

The [surjective interpolation lemma](../../methods/details/jet_nonvanishing.md)
therefore produces a finite family of integer polynomials of total degree
at most $D$, all with the prescribed row multiplicities, and with at
least one nonzero evaluation at each admissible $(j,n-j)$. The common
coordinate-line factor is nonzero because both coordinates exceed 9.

The weighted divisibility argument then gives, for a suitable effectively
computable constant $C$,

$$
n^{\sum_t\alpha_tm_t-D}\le C
$$

once the source estimates apply. The conversion from $H=n-8$ to $n$
only changes this constant. Strict positivity of (1) gives an effective
stopping bound for every covered case. No numerical value for those
bounds is needed in this component of the argument.

## The twelve collision cases

Every remaining collision has $r_2=r_5$, with the three positions
$r_2,r_3,r_7$ forming a permutation of $0,1,2$. There are two witness
vectors, in prime order $2,3,5,7$:

$$
(3296,505,3931,0)/10000,
\qquad(3296,502,3931,505)/10000.
$$

A collision also supplies additional cofactor information. If $k$ primes
share a position $r$ and $e_p=\log u_p/\log H$, then

$$
\prod_{p:r_p=r}u_p
=\frac{(n-r)^k}{\prod_{p:r_p=r}P_p}
\ge(n-r)^{k-1}\ge H^{k-1},
\qquad
\boxed{\sum_{p:r_p=r}e_p\ge k-1.} \tag{2}
$$

In particular these twelve cases satisfy $e_2+e_5\ge1$. A subsequent
cofactor analysis may use (2); the polynomial coverage count above does
not assume it.

## Reproduction

The full checker recomputes all seventy modular ranks. The arithmetic
mode checks the integer multiplicities and jet counts, source vectors,
all 104,976 cases, the exact residual list, and the coverage hash, without
repeating ranks (with the pinned dependencies named below installed in
the repository's `.venv/`):

```sh
.venv/bin/python \
  wiki/research/erdos_699/computations/erdos_699_index_9_baseline.py \
  --arithmetic-only
```

Omit the final option to repeat the rank calculations. NumPy and
`python-flint` versions are recorded in the existing
[requirements file](../../evidence/assets/erdos_699_interpolation_requirements.txt).
