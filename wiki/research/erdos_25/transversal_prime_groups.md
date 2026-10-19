---
name: research/erdos_25/transversal_prime_groups
desc: A uniform size obstruction to one high-rank coherent counterexample mechanism.
tags: [sieve, obstructions, partial-results]
sources: []
created: 2026-09-22T00:05:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/transversal_prime_groups

***

## Proved uniform estimate

Let $P_1,\ldots,P_r$ be disjoint finite sets of primes, with
$\sum_{p\in P_j}1/p\le c$ for a fixed $c$. Assign one residue $b_p$
to each prime. For every product $q$ choosing one prime from each group,
give $q$ the residue induced by the $b_p$ via CRT. Let $B$ be the union
of their delayed classes, activated only at $n\ge q$.

There is a function $g_c(r)=O_c(1/r)$ such that, for every positive
integer $N$,
$$
 |B\cap(N,2N]|\le g_c(r)N.
 \tag{1}
$$
The estimate is uniform in the prime groups and all their residue choices.
In particular these coherent high-rank product families cannot have a
fixed positive normalized harmonic deletion while $r\to\infty$,
regardless of the sizes of the quotients $n/q$.

This controls the actual trace for the family underlying the
[divisor-face capacity obstruction](rank_and_moment_obstructions.md).
It shows why feasible abstract face weights need not be realizable as
first-kill harmonic masses.

## Proof

Put $\eta=e^{-2c}$, $C=2/\eta$, and
$z=(2N)^{C/r}$. For each $j$, let $F_j(n)$ indicate avoidance of the
prime classes in $P_j$ with $p\le z$, and set
$$
 p_j=\prod_{\substack{p\in P_j\\p\le z}}(1-1/p),
 \qquad M(n)=\sum_jF_j(n),\qquad m=\sum_jp_j.
$$
Since $\log(1-1/p)\ge-2/p$, we have $p_j\ge\eta$ and $m\ge\eta r$.

Take $r$ sufficiently large in terms of $c$, and let $k$ be the largest
even integer at most $r/(2C)=\eta r/4$. Thus $k\ge2$ and
$z^k\le\sqrt{2N}$. For one group, or the union of any two groups,
Bonferroni's inequalities give a uniform comparison between its
avoidance probability on $(N,2N]$ and its Haar avoidance probability,
with error at most
$$
 \epsilon_r(N)=\frac{(2c)^k}{k!}+\sqrt{\frac2N}.
 \tag{2}
$$
To verify the error directly, compare the even inclusion--exclusion
partial sum through order $k$ and the odd sum through order $k-1$.
Each congruence intersection involved has a squarefree modulus at most
$z^k\le\sqrt{2N}$. There is at most one term for each such modulus,
because each prime has a single fixed residue. The total normalized
counting error is therefore at most $\sqrt{2N}/N$. The Haar gap between
the two partial sums is the degree-$k$ elementary symmetric sum of the
prime reciprocals, at most $(2c)^k/k!$. This proves (2).

Haar independence between disjoint prime groups gives
$\mathbb E_{\rm Haar}F_jF_\ell=p_jp_\ell$ for $j\ne\ell$.
Using (2) for all one- and two-group expectations, with averages over
$I=(N,2N]$, yields
$$
 \mathbb E_I(M-m)^2\le r/4+3r^2\epsilon_r(N).
$$
Consequently
$$
 \Pr_I(M<\eta r/2)
 \le\eta^{-2}\bigl(1/r+12\epsilon_r(N)\bigr).
 \tag{3}
$$

If $n\in B\cap I$, choose an active product $q\le n$ witnessing it.
Every group counted by $M(n)$ must supply a prime greater than $z$ to
this product. If $M(n)\ge\eta r/2$, then
$$
 q>z^{M(n)}\ge z^{\eta r/2}=2N\ge n,
$$
a contradiction. Thus every actual deletion lies in the event in (3).
If $B\cap I$ is nonempty, its witness satisfies $2N\ge q\ge2^r$, so
$\sqrt{2/N}\le2^{1-r/2}$. We may therefore take
$$
 g_c(r)=\eta^{-2}\left(
 1/r+12(2c)^k/k!+12\cdot2^{1-r/2}\right)=O_c(1/r).
$$
For the finitely many smaller $r$, set $g_c(r)=1$. This proves (1).
Summing (1) over dyadic intervals, and using $1/n\le1/N$ on each,
gives the asserted vanishing normalized harmonic bound as $r\to\infty$.

## Removing the bound on group reciprocal sums

For these same complete transversal families, a stronger result follows
from the fundamental lemma of sieve theory. Define
$$
 u_j=\prod_{p\in P_j}(1-1/p),\qquad \mu=\sum_ju_j.
$$
Uniformly over finite disjoint prime groups and their coherent residues,
$$
 \sup_{X\ge1}\frac{|B\cap[1,X]|}{X}\ll\frac1\mu
 \quad\text{as }\mu\to\infty.
 \tag{4}
$$

**External input, checked.** Koukoulopoulos,
[*The Distribution of Prime Numbers*, Theorem 19.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=206),
printed p. 195 (PDF page 206), supplies upper and lower sieve weights
of absolute value at most one, supported on squarefree $d\le D$, with
relative Euler-product error $O(s^{-s/2})$, where $s=\log D/\log z$ is
sufficiently large. For any selected prime set and one forbidden residue
per prime, its dimension hypothesis holds with absolute parameters:
take $\nu(p)=1$, $\kappa=1$, and an absolute $C$ in Axiom 2, as explained
on printed p. 187 (PDF page 198). Both passages were checked in the
author-hosted full text. No supplied source file was altered.

Here is the application, including the interval error. On $(N,2N]$ take
$z=(2N)^{2/\mu}$, $D=\sqrt N$, and define $F_j,p_j,m,M$ as in the
elementary proof. Then $m\ge\mu$. For a single group or two groups
together, each modulus in a sieve-weight sum prescribes one CRT class,
with normalized counting error at most $1/N$. There are at most $D$
such moduli. The pointwise sieve inequalities apply to any vector of
prime hits, by representing that vector by a squarefree integer.
Thus the fundamental lemma gives
$$
 |\mathbb E_I F_j-p_j|\le\epsilon p_j+R,
 \qquad
 |\mathbb E_I F_jF_\ell-p_jp_\ell|
 \le\epsilon p_jp_\ell+R,
$$
where $R=N^{-1/2}$ and $\epsilon\ll s^{-s/2}$, with absolute constants.
For $N\ge2$, $s\ge\mu/8$. If the interval contains a deleted point,
$N\ge2^{r-1}$ and $r\ge\mu$, so all size hypotheses hold when $\mu$
is sufficiently large.

Expansion of the centered second moment now gives
$$
 \mathbb E_I(M-m)^2\le m+4\epsilon m^2+3r^2R.
$$
An active certificate requires $M<\mu/2$, since otherwise its prime
product exceeds $z^{\mu/2}=2N$. This event is contained in
$\{|M-m|>m/2\}$. Its probability is at most
$$
 \frac4\mu+16\epsilon+\frac{12r^2}{\mu^2\sqrt N}
 \ll\frac1\mu.
$$
The last term is exponentially small in $\mu$, using
$N\ge2^{r-1}$ and $r\ge\mu$. Dyadic summation proves (4), and partial
summation gives the same bound for $H_B(X)/H_{\lfloor X\rfloor}$.

In particular a small periodic footprint always forces small deletion
for one complete transversal family. Write
$$
 \beta=\prod_j(1-u_j),\qquad L=\log(1/\beta).
$$
If some $u_j\ge1-1/L$, every deletion lies in that group's delayed prime
union, whose count is at most
$X\sum_{p\in P_j}1/p\le-X\log u_j\le2X/L$ for $L\ge2$.
Otherwise the increasing function $-\log(1-u)/u$ is at most $2\log L$
on the possible range, so $L\le2\mu\log L$. Applying (4) yields
$$
 \sup_{X\ge1}\frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \ll\frac{\log\log(1/\beta)}{\log(1/\beta)}
 \qquad(\beta\downarrow0).
$$
The empty-family case $\beta=0$ is immediate.

## Limitation

The proof uses one consistent prime residue $b_p$ throughout all product
classes. Arbitrary singleton residues modulo the products need not have
this consistency. Nor has a general small-footprint family been reduced
to complete transversal families with controlled total error. These are
specific missing steps, not consequences of this estimate.
