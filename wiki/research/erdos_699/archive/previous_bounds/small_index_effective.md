---
name: research/erdos_699/archive/previous_bounds/small_index_effective
title: "Erdős 699: cutoff 26 and further effective bounds"
desc: "The earlier prime-pair and interval proof of cutoff 26, retained as an input to the current cutoff 21 and complete small-index exclusions."
created: 2026-09-22T02:17:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: cutoff 26 and further effective bounds

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|Earlier effectivity reduction]]

**Current result.** The [cutoff-nine proof](../../proofs/details/cutoff_9.md)
excludes seven and every $i\ge9$. The four indices still lacking effective
bounds are $4,5,6,8$. The derivation below records the preceding
cutoff-26 stage.

**There are no bad triples with $i\ge26$, or with $i=17,23$.** This
improves the previous cutoff $i\ge35$ and the extra case $i=29$.
The new exclusions are computer-assisted: explicit analytic bounds close
the infinite tail, and rigorously rounded interval certificates exclude
the entire remaining range. The original threshold is $p\ge i$ throughout.

**Follow-up.** The [further effective bounds](further_effective_bounds.md)
make $i=21$ effective and give fully numerical stopping bounds at
$i=11,16,19,21,22,24,25$. In particular, $i=19,24$ have $n<10^{976}$,
and $i=22,25$ have $n<10^{957}$. The derivation below records the preceding
stage, with source thresholds unevaluated; that note replaces them by explicit
alternatives.

The prime-pair estimates first make eleven previously ineffective indices effective:

$$
16,17,19,22,23,25,26,27,30,32,33.
$$

Seven of them have fully numerical row bounds. The same method makes the
previously uninstantiated bounds at $28,31,34$ numerical. Completed
interval calculations exclude all ten numerically bounded indices:
$17,23,26,27,28,30,31,32,33,34$.
The [adapted argument at index eleven](../../proofs/details/index_11_effective.md)
and [two further prime-pair estimates at index 24](effective_index_24.md)
give two more effective indices. Thus **thirteen previously ineffective
indices are effective**, with ten additional complete exclusions
when the previously effective cases are included. At this stage,
$11,16,19,22,24,25$ had computable last rows with unevaluated source
constants. The follow-up evaluates numerical alternatives for all six and
adds index $21$. At that stage the indices still lacking effective last rows were

$$
\boxed{\{4,5,6,7,8,9,10,12,13,14,15,18,20\}.}
$$

The new input is Bennett, Filaseta and Trifonov (BFT), *On the
factorization of consecutive integers*, Theorem 2.1 and Corollary 2.3.
Their bounds apply to prime powers in integers separated by any prescribed
bounded gap. Applying them simultaneously to six small primes saves
$0.913$ in an explicitly bounded range, or $1.012$ beyond an effectively
computable threshold. The simultaneous **maximum** inequalities are
stronger than the estimates obtained by pairing the primes disjointly.

These deductions are repository work; their novelty has not been assessed.
The theorem numbering below refers to the author preprint dated
26 February 2007, associated with the
published 2009 article.

## 1. Small-prime powers and their cofactors

Let $S_i=\{p:p<i\}$, $s_i=|S_i|$, and write
$\binom ni=U_i(n)V_i(n)$, with $U_i$ supported on $S_i$.
For each $p<i$, choose $r_p\in\{0,\ldots,i-1\}$ maximizing
$v_p(n-r_p)$, and put

$$
P_p=p^{v_p(n-r_p)},\qquad u_p=(n-r_p)/P_p.
$$

The earlier maximal-position argument gives

$$U_i(n)\le\frac{1}{[i]_{S_i}}\prod_{p<i}P_p,\qquad
[i]_{S_i}=\begin{cases}i,&i\text{ composite},\\1,&i\text{ prime}.
\end{cases}\tag{1}$$

Indeed, for $t\ne r_p$, the maximality and the ultrametric inequality give
$v_p(n-t)\le v_p(t-r_p)$. The total contribution of the other factors
is therefore at most $v_p((i-1)!)$. Multiply over $p<i$ and divide by
the small-prime part of $i!$ to obtain (1).

For any two small primes,

$$
|P_pu_p-P_qu_q|=|r_q-r_p|\le i-1.\tag{2}
$$

This is exactly the bounded-gap condition in BFT. No coprimality of the
cofactors, distinctness of the positions, or nonzero difference in (2)
is required by their statements.

## 2. The two prime-pair tables

BFT give the following exponents:

| $p,q$ | Theorem 2.1: explicit $a_{pq}$ | Corollary 2.3: effective $b_{pq}$ |
| --- | ---: | ---: |
| $2,3$ | $.285$ | $.2921$ |
| $2,5$ | $.258$ | $.2679$ |
| $2,7$ | $.259$ | $.2757$ |
| $2,11$ | $.059$ | $.0698$ |
| $2,13$ | $.054$ | $.0798$ |
| $3,5$ | $.216$ | $.2238$ |
| $3,7$ | $.038$ | $.0505$ |
| $3,11$ | $.329$ | $.3453$ |
| $3,13$ | $.231$ | $.2372$ |
| $5,7$ | $.227$ | $.2667$ |
| $5,11$ | $.199$ | $.2091$ |
| $5,13$ | $.163$ | $.1838$ |
| $7,13$ | $.098$ | $.1243$ |
| $11,13$ | $.037$ | $.0729$ |

Theorem 2.1 applies when the difference in (2) is at most $100$.
Outside a displayed finite list and the range $P_pu_p\le1000$, it gives

$$
\max(u_p,u_q)>\min(n-r_p,n-r_q)^{a_{pq}}.
$$

The largest coordinate in that list is $1\,771\,561$.
Consequently **every** pair in the explicit column applies whenever

$$
i\le34,\qquad n\ge N_0:=1\,771\,595.\tag{3}
$$

For the other column, Corollary 2.3 supplies an effectively computable
$x_0(D)$, uniform over its fourteen pairs, such that

$$
\max(u_p,u_q)>(n-r_p)^{b_{pq}}\tag{4}
$$

when $n-r_p\ge x_0(D)$ and $|r_p-r_q|\le D$.
Unlike (3), this threshold is not numerically evaluated in the corollary.
We use it only to claim a computable bound unless a separate numerical
calculation is supplied.

## 3. Combining all the maximum inequalities

Set $h=n-i+1>1$ and $z_p=\log(u_p)/\log h\ge0$.
Each applicable pair gives

$$\max(z_p,z_q)\ge a_{pq}\quad\text{or}\quad
\max(z_p,z_q)\ge b_{pq}.\tag{5}$$

For the six primes $2,3,5,7,11,13$, the exact minimum of
$\sum z_p$ under these constraints is respectively

$$\boxed{\gamma_{\rm explicit}=913/1000,\qquad
\gamma_{\rm effective}=253/250.}\tag{6}$$

One way to verify (6) is to choose an endpoint of each of the fourteen
edges witnessing its maximum constraint. At a vertex, the least permitted
value is the maximum of the weights assigned to it, or zero if none is
assigned. Checking the $2^{14}$ choices is therefore an exact finite proof
of the minimum. The [checker](../../computations/erdos_699_prime_pair_savings.py)
uses integer weights, and its
[recorded certificate](../../computations/erdos_699_prime_pair_savings.json)
includes the minimizers. In the order $2,3,5,7,11,13$, they are

$$(.259,.329,.227,0,0,.098),\qquad
(.2757,.3453,.2667,0,0,.1243).$$

For clarity, a short proof of the second minimum follows. A triangle whose
three edge weights are $a\le b\le c$ has minimum vertex sum $a+c$:
the vertex meeting the largest edge has weight at least $c$, and the edge
between the other two vertices has weight at least $a$; equality is attained
by putting $c$ at the intersection of the two larger edges and $a$ at one
remaining vertex.

If $z_{11}\ge.3453$, the triangle on $3,5,13$ and the edge $2,7$ give
$\sum z_p\ge.3453+.421+.2757=1.042$.
Otherwise $z_3\ge.3453$. If $z_{13}\ge.1243$, the triangle on $2,5,7$
gives $\sum z_p\ge.3453+.1243+.5424=1.012$.
If $z_{13}<.1243$, then $z_7\ge.1243$ and $z_5\ge.1838$.
If $z_7<.2757$, then $z_2\ge.2757$, and the edge $5,7$ completes a
sum of at least $1.012$.
If $z_7\ge.2757$ and $z_5<.2679$, then $z_2\ge.2679$, giving a
sum at least $1.0727$.
Finally, if $z_7\ge.2757$ and $z_5\ge.2679$, the triangle on
$2,11,13$ gives a further $.1496$, for a total at least $1.0385$.
This proves the lower bound, and the displayed vector attains it.
The same cases with the explicit weights prove $.913$.

For $i\ge14$, all six primes are in $S_i$. Equation (6) implies
$\prod_{p<i}u_p\ge h^\gamma$, since the other cofactors are positive
integers. Hence

$$U_i(n)\le\frac{n^{s_i}}{[i]_{S_i}(n-i+1)^\gamma}
\le\frac{2^\gamma}{[i]_{S_i}}n^{s_i-\gamma}\tag{7}$$

whenever $n\ge2(i-1)$ and the relevant source threshold holds.

## 4. Fully numerical last rows

For $i\ge5$, put

$$k=\lfloor2i/3\rfloor,\quad m=3k-i+1,\quad
A=k(k+1)/2,\quad \rho_i=3A/m.$$

The retained fat-point certificate gives
$V_i(n)^m<n^{3A}/4^A$.
For $n\ge N_0$, define

$$g_i=1-\frac{i(i-1)}{2N_0}>0,\qquad
M_i=\frac{i!}{[i]_{S_i}g_i4^{A/m}}.$$

The elementary product bound gives
$\binom ni\ge g_i n^i/i!$.
Combining it with (7), badness forces

$$n^{\eta_i}<2^\gamma M_i,\qquad
\eta_i=i-\rho_i-s_i+\gamma.\tag{8}$$

For $\gamma=.913$, (8) gives the following certified bounds, each of
which exceeds $N_0$ and therefore also covers all smaller rows:

| $i$ | Necessary condition for badness |
| --- | --- |
| $17$ | $n<10^{47}$ |
| $23$ | $n<10^{75}$ |
| $26$ | $n<10^{85}$ |
| $27$ | $n<10^{40}$ |
| $28$ | $n<10^{27}$ |
| $30$ | $n<10^{46}$ |
| $31$ | $n<10^{33}$ |
| $32$ | $n<10^{117}$ |
| $33$ | $n<10^{53}$ |
| $34$ | $n<10^{36}$ |

The [numerical checker](../../computations/erdos_699_small_index_bounds.py)
certifies the positive logarithmic margins in (8) with outward rounding;
its [output](../../computations/erdos_699_small_index_bounds.json)
records the exact rational exponents. No unspecified constants occur in
these bounds. This computation evaluates ten inequalities, not rows.

## 5. Further effective indices

Use instead $\gamma=1.012$ in (7). The same comparison has

$$
\eta_i=3/250>0\qquad(i=16,19,22,25).
$$

For an explicit form of the resulting computable bound, let
$X=x_0(33)$ be the threshold from BFT Corollary 2.3.
For $n\ge\max\{X+33,i(i-1)\}$ we may replace $g_i$ by $1/2$, giving

$$n<\max\left\{X+33,\ i(i-1),\
\left(\frac{2^{1+253/250}i!}
{[i]_{S_i}4^{A/m}}\right)^{250/3}\right\}.\tag{9}$$

Thus these four indices become effective without evaluating $X$.
The checker also verifies the index classification with exact rational
arithmetic. The [index-eleven argument](../../proofs/details/index_11_effective.md)
uses the smaller four-prime table with a position-dependent polynomial;
it is not a consequence of the unweighted sum in (7).

At $i=24$, two certified applications of BFT Theorem 2.2 add the pairs
$(17,19)$ and $(11,23)$ with exponents $.21$ and $.145$.
Their combined saving is $1.3237$, slightly larger than the required
$1.32$. The [full derivation](effective_index_24.md)
gives $n<\max\{X_{24}+23,10^{10000}\}$, where $X_{24}$ is the maximum
of the finitely many effective source thresholds used there. As at
$i=11,16,19,22,25$, this is a computable bound whose source thresholds
were left unevaluated at this stage. The
[follow-up](further_effective_bounds.md) supplies numerical
alternatives and smaller algebraic terms for all six cases.

## 6. Complete exclusions by interval certificates

The bounds in Section 4 close the upper end of a finite interval. At the
lower end, the terminal-prime argument and the retained prime-gap records
supply $P_i$. The existing interval method from the
[cutoff note](../../proofs/details/cutoff_and_cubic.md), Section 3, applies
unchanged on $[P_i,B_i]$: each leaf bounds every small-prime valuation on
an entire integer interval and compares it to the increasing fat-point
and discriminant lower bounds.

The [new interval driver](../../computations/erdos_699_effective_intervals.py)
uses the numerical BFT bound to supply its cap. At $27,28,30,31,34$, the
existing interval upper bound suffices. For the other five indices we also
apply the prime-pair constraints inside each interval.

For an interval $[a,b]$ with $a\ge N_0$, the single-prime version of (1)
and an applicable cofactor vector $w$ give

$$p^{v_p(\binom ni)}\le
\min\left\{p^{E_p(a,b)},
\frac{b}{p^{v_p(i)}(a-i+1)^{w_p}}\right\}.$$

Here $w_p$ is the cofactor-vector coordinate and $v_p(i)$ is the usual
prime valuation.
Every row admits one of 31 componentwise minimal vectors from the
explicit table. Take the logarithm of this upper bound, sum over primes,
then take the **maximum** over the 31 vectors. This gives a uniform upper
bound for the entire interval, because the applicable vector can vary
with the row. The [full interval proof](../../proofs/details/effective_interval_certificates.md)
spells out the inequality, coverage argument, and rounding directions.

The [completed output](../../computations/erdos_699_effective_intervals.json)
records ten complete partitions, with **1,770,437 certified leaf
intervals**. The smallest certified logarithmic margin exceeds
$0.0000016177$. Each record includes the cap, leaf count, minimum margin,
and partition hash. Some caps are slightly larger than those in Section 4
because the driver fixes its constants at the terminal-prime lower bound.

This excludes all ten numerically bounded indices. Together with the
earlier case $29$ and tail $i\ge35$, it proves the cutoff $i\ge26$
and the extra cases $17,23$. The prime-gap records and the earlier tail
theorem remain inputs. These new certificates have not been formalized
in Lean.

## Sources and reproduction

Bennett, Filaseta and Trifonov, *On the factorization of consecutive
integers*, J. Reine Angew. Math. 629 (2009), 171–200,
[DOI](https://doi.org/10.1515/CRELLE.2009.030).
Theorem 2.1 gives the numerical table and complete exception list;
Corollary 2.3 gives the larger effective exponents.

```sh
python3 wiki/research/erdos_699/computations/erdos_699_prime_pair_savings.py
python3 wiki/research/erdos_699/computations/erdos_699_small_index_bounds.py
python3 wiki/research/erdos_699/computations/erdos_699_effective_intervals.py --indices 27 28 30 31 34 --max-nodes 1500000
python3 wiki/research/erdos_699/computations/erdos_699_effective_intervals.py --indices 17 23 26 32 33 --local-pairs --max-nodes 500000
```
