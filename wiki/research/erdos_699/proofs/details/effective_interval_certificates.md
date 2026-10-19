---
name: research/erdos_699/proofs/details/effective_interval_certificates
title: "Erdős 699: complete interval certificates at further small indices"
desc: "Complete interval proofs exclude every i>=26 and the isolated indices 17 and 23, using numerical prime-pair bounds both in the tail and inside the interval proof."
created: 2026-09-22T02:28:29Z
updated: 2026-09-22T02:28:29Z
---

# Erdős 699: complete interval certificates at further small indices

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Numerical small-index bounds]] ·
[[research/erdos_699/proofs/details/cutoff_and_cubic|Earlier interval certificates]]

***

Under the original threshold $p\ge i$, **there are no bad triples at
$i=17,23$ or at any $i\ge26$**. The new certificates exclude the ten indices
$17,23,26,27,28,30,31,32,33,34$; the earlier certificate already excluded
$29$ and every $i\ge35$.

The new ingredients are a numerical tail bound and the use of its
prime-pair inequalities inside intervals. The finite interval argument
retains the valuation bounds and outward-rounded comparisons in the
earlier $i\ge35$ certificate. It covers entire integer intervals, without
iterating through their individual rows.

## Numerical tail

Write $S=\{p:p<i\}$, $s=|S|$, and let $U_i(n)$ be the $S$-part of
$\binom ni$. The prime-pair result in the linked small-index note gives,
for all indices used below and all $n\ge1\,771\,595$,

$$
U_i(n)\le \frac{2^{913/1000}}{[i]_S}\,n^{s-913/1000},
\qquad
[i]_S=\begin{cases}i,&i\text{ composite},\\1,&i\text{ prime}.
\end{cases}
\tag{1}
$$

The lower bounds forced by a bad triple are the previously established
fat-point and symmetric discriminant bounds. Their constants are evaluated
at the first row not already excluded by the terminal-prime argument.
Comparison with (1), using directed rounding throughout, gives the
conservative caps in the table. The interval computation includes the cap;
every larger row is excluded by (1).

| $i$ | First remaining row | Inclusive cap | Certified intervals | Least logarithmic margin, rounded down |
| --- | ---: | ---: | ---: | ---: |
| $17$ | $523$ | $10^{48}$ | $110\,596$ | $0.000007174$ |
| $23$ | $1327$ | $10^{76}$ | $140\,571$ | $0.00002213$ |
| $26$ | $1327$ | $10^{86}$ | $100\,819$ | $0.00004804$ |
| $27$ | $1327$ | $10^{40}$ | $373\,615$ | $0.0001093$ |
| $28$ | $1327$ | $10^{27}$ | $31\,894$ | $0.0001968$ |
| $30$ | $1327$ | $10^{47}$ | $666\,271$ | $0.000001617$ |
| $31$ | $1327$ | $10^{34}$ | $78\,047$ | $0.00004098$ |
| $32$ | $1327$ | $10^{118}$ | $161\,338$ | $0.00006757$ |
| $33$ | $1327$ | $10^{54}$ | $37\,338$ | $0.0001239$ |
| $34$ | $9551$ | $10^{36}$ | $69\,948$ | $0.0004670$ |

These caps need not be the smallest available caps: preserving one choice
makes the complete interval partition and its hash reproducible.

## Interval proof

For every $p<i$,

$$
v_p\binom ni=
\sum_{a\ge1}
\mathbf 1_{\{n\bmod p^a<i\bmod p^a\}}.
\tag{2}
$$

For an interval $[L,R]$, a term of (2) can occur only if either its residue
condition already holds at $L$, or $[L,R]$ crosses a multiple of $p^a$.
Summing these possible contributions gives a rigorous upper bound for
$\log U_i(n)$ throughout the interval. The lower bounds increase with $n$,
so their value at $L$ is a valid lower bound throughout the same interval.
Whenever the lower bound exceeds the upper bound by a positive
outward-rounded margin, every row of the interval is excluded. Otherwise
the interval is bisected.

For each of the ten indices the process terminates with every interval
certified. The JSON retains the number of visited and accepted intervals,
the smallest certified margin, and a SHA-256 hash of the ordered interval
partition. An unexcluded singleton or an exhausted node budget would be
reported as an incomplete proof and would not support the conclusion.

The five indices $27,28,30,31,34$ need only (2) within each interval. The
other five also use the following local prime-pair bound.

## Prime-pair bounds inside an interval

For each $p<i$, choose $r_p\in\{0,\ldots,i-1\}$ maximizing
$v_p(n-r_p)$, and put

$$
P_p=p^{v_p(n-r_p)},\qquad u_p=(n-r_p)/P_p.
$$

The maximal-position inequality gives

$$
p^{v_p\binom ni}\le P_p/p^{v_p(i)}.\tag{3}
$$

Suppose $L\ge1\,771\,595$. For every edge $pq$ in the explicit
Bennett--Filaseta--Trifonov table, the argument in the small-index note
gives

$$
\max(u_p,u_q)\ge(L-i+1)^{\lambda_{pq}}.\tag{4}
$$

Assign each edge to an endpoint witnessing (4). At each of the six
vertices $p\in\{2,3,5,7,11,13\}$, take the largest weight of its assigned
edges, or zero if no edge is assigned. This produces an exponent vector
$v=(v_p)$ for which $u_p\ge(L-i+1)^{v_p}$. There are $2^{14}$ endpoint
assignments, giving 673 distinct vectors. Removing each vector
componentwise dominated from below by another leaves **31 vectors**.
Every possible collection of actual cofactors satisfies the inequalities
of at least one of these 31 vectors.

Let $E_p$ be the interval valuation upper bound from (2). For a particular
vector $v$, (3) and $n-r_p\le R$ give

$$
\log p^{v_p\binom ni}
\le
\min\left\{
E_p\log p,\quad
\log R-v_p\log(L-i+1)-v_p(i)\log p
\right\}.
\tag{5}
$$

Here the coordinate $v_p$ of the assignment vector and the valuation
$v_p(i)$ are distinct quantities. To avoid choosing which assignment the
unknown row satisfies, sum (5) over the six vertices and take the
**maximum** over the 31 vectors. Add the ordinary bounds $E_p\log p$ for
the remaining primes $p<i$. This is a uniform upper bound for
$\log U_i(n)$ throughout $[L,R]$.

This refinement is used only at or above the numerical source threshold;
smaller intervals use (2) alone. In the implementation, every subtracted
quantity is first rounded down. Each upper bound, sum, and maximum is
then rounded up, before comparison with the lower bound rounded down.

The complete certificates, comprising 1,770,437 accepted intervals, are
retained in the
[effective-interval record](../../computations/erdos_699_effective_intervals.json).
Reproduce them from the repository root with:

```sh
python wiki/research/erdos_699/computations/erdos_699_effective_intervals.py \
  --indices 34 31 30 28 27 --max-nodes 1500000
python wiki/research/erdos_699/computations/erdos_699_effective_intervals.py \
  --indices 33 32 26 23 17 --local-pairs --max-nodes 500000
```

Without `--local-pairs`, the entry point only replaces the numerical tail
bound in `erdos_699_i_ge_35.py`; its interval valuation and margin calculations
are unchanged. The option adds (5) when the ordinary upper bound does not
suffice. No floating-point comparison certifies an interval: floating point
only decides whether to attempt the final directed-rounding check.
