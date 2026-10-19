---
name: research/erdos_25/ordered_coherent_runs
desc: A uniform primitive-annulus bound proves logarithmic endpoint nullity when the residues have sublogarithmically many ordered coherent pieces.
tags: [endpoints, primitive-sets, partial-results]
sources: []
created: 2026-09-22T12:05:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/ordered_coherent_runs

***

This criterion measures how often the residue pattern changes as the
modulus increases, rather than the number of its prime coordinates.
It controls bounded-quotient first kills, not the full delayed union.

## A uniform primitive-annulus lemma

**Lemma.** For every $\varepsilon>0$ there is a constant
$C_\varepsilon$ such that every primitive set $A\subset\mathbb N$
satisfies
$$
 \sum_{a\in A\cap(x,y]}\frac1a
 \le\varepsilon\log(y/x)+C_\varepsilon
 \qquad(1\le x<y).
 \tag{1}
$$
Primitive means that no two distinct members divide one another.
The constants are independent of $A$ and the location of the annulus.

For a finite prime set $\mathcal P$, write
$$
 \rho=\prod_{p\in\mathcal P}(1-1/p),\qquad Z=\rho^{-1}.
$$
The [weighted smooth-antichain bound](colored_towers.md#weighted-antichains-of-smooth-integers)
states that every primitive family of $\mathcal P$-smooth integers
has reciprocal sum at most $\theta_{\mathcal P}Z$, where
$$
 \theta_{\mathcal P}\ll
 \left(1+\sum_{p\in\mathcal P}\frac1{p+1}\right)^{-1/2}.
 \tag{2}
$$
Its product-measure proof is useful here: a geometric valuation splits
as $V_p=B_p+2W_p$, where $B_p$ is Bernoulli with parameter $1/(p+1)$.
Write $B_p=I_pJ_p$, with $I_p$ Bernoulli of parameter $2/(p+1)$
and $J_p$ fair, independently. Conditional on $W,I$, a divisibility
antichain becomes an antichain in a uniform Boolean cube of dimension
$\sum I_p$. Sperner's bound and Chebyshev give (2).

Integers coprime to all primes in $\mathcal P$ form a periodic set of
density $\rho$. Their harmonic sums therefore obey
$$
 H_{\mathrm{rough},\mathcal P}((u,v])
 \le\rho\log(v/u)+C_{\mathcal P}\qquad(0<u<v).
 \tag{3}
$$
For $u\ge1$ this follows by subtracting the two bounded-error
periodic harmonic estimates. For $u<1\le v$, use the initial-interval
estimate and $\log v\le\log(v/u)$; for $v<1$ the sum is empty.

Choose $\mathcal P$ with $\theta_{\mathcal P}\le\varepsilon/2$.
Since the reciprocal sum of all $\mathcal P$-smooth integers is $Z$,
choose $M\ge1$ such that
$$
 T_M:=\sum_{\substack{a>M\\a\ \mathcal P\text{-smooth}}}\frac1a
 \le\varepsilon/(2\rho).
$$
Factor $n=ab$ uniquely with $a$ smooth and $b$ rough. At each fixed
$b$, the selected smooth parts with $ab\in A$ form an antichain.
The part with $a\le M$ has $x/M<b\le y$, so its harmonic contribution
is at most
$$
 \theta_{\mathcal P}Z\,H_{\mathrm{rough},\mathcal P}((x/M,y])
 \le\theta_{\mathcal P}\log(y/x)
       +\theta_{\mathcal P}\log M+\theta_{\mathcal P}ZC_{\mathcal P}.
$$
For $a>M$, discard primitivity and sum (3) on $(x/a,y/a]$.
This contribution is at most
$T_M(\rho\log(y/x)+C_{\mathcal P})$.
The coefficient of $\log(y/x)$ is at most $\varepsilon$; all other
terms depend only on the chosen $\varepsilon$. This proves (1).

## Sublogarithmically many ordered coherent pieces

**Theorem.** Suppose the increasing singleton family is coherent on
each member of a partition into consecutive modulus intervals. Let
$J(X)$ be the number of these intervals containing selected moduli
at most $X$. If
$$
 J(X)=o(\log X),
 \tag{4}
$$
then, for every fixed $K$, the union of first kills with
$1\le(n-a_q)/q\le K$ has logarithmic density zero.

Here coherence within a piece means that its residues are the
projections of one profinite center; different pieces may have arbitrary
different centers. It would suffice to require compatibility just for
divisibility-comparable moduli within a piece.

Let $D_K$ be the moduli with a first kill in this quotient range.
Within each piece $D_K$ is primitive. Indeed, if $p<q$ both occur,
$p\mid q$, and their classes are compatible, then the entire $q$-class
is contained in the $p$-class. Every active point for $q$ is already
active for $p$, contradicting a first kill at $q$.

Partition $(1,X]$ at the piece boundaries and apply (1) to the
primitive moduli in each piece. The logarithmic interval lengths
telescope, giving
$$
 \sum_{\substack{q\le X\\q\in D_K}}\frac1q
 \le\varepsilon\log X+C_\varepsilon J(X)+O(1).
$$
The initial modulus $1$, if present, is harmless. Divide by $\log X$,
use (4), and then let $\varepsilon\downarrow0$.
Finally a witnessing modulus contributes at most
$H_{\lfloor K\rfloor}/q$ to the harmonic sum of its bounded-quotient
hits. Overcounting can only increase the upper bound. This proves the
theorem with the original activation thresholds.

In particular, it applies whenever the canonical residues are
nondecreasing along the modulus sequence and
$$
 a_q=o(\log q).
 \tag{5}
$$
There are at most $a_q+1$ constant-residue runs before such a modulus,
and each run is coherent. This includes the fixed profile
$a_q=\lfloor\log\log q\rfloor$.

The earlier [finite-component estimate](colored_towers.md#a-bounded-number-of-coherent-components-cannot-supply-dense-early-first-kills)
allows arbitrary interlacing but loses a factor equal to the number of
components. The ordered-run theorem permits many more components by
using their disjoint logarithmic intervals. It gives no assertion when
the number of ordered pieces is comparable to $\log X$, nor for
arbitrary monotone sublinear residues. The
[fixed flat-profile construction](curved_residue_profiles.md#a-fixed-flat-profile-can-have-large-natural-endpoint-spikes)
also shows that its logarithmic conclusion cannot be strengthened to
natural nullity even in example (5).
