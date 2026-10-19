---
name: research/erdos_25/product_capacity_obstruction
desc: Divisor-face capacities fail even for distinct primitive moduli with at most three distinct prime factors.
tags: [obstructions, prime-rank, carleson-measures]
sources: []
created: 2026-09-22T03:23:08Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/product_capacity_obstruction

***

A proposed extension of the bounded-$\Omega$ argument was to exploit
the tree structure of prime-power residue classes, hoping for a bound
depending only on the number $\omega(q)$ of distinct prime factors.
The obstruction below defeats any such argument based **only on all
individual divisor-face capacities**, even when $\omega(q)\le3$ and
the moduli are distinct and primitive.

The weights constructed here are not known to be realizable as actual
first-kill harmonic masses. This is not a counterexample to Problem 25,
or to its bounded-$\omega$ version for arbitrary residues. The later
[squarefull-kernel theorem](squarefull_kernel_truncation.md) proves
natural density for that bounded-$\omega$ singleton version. Its
arithmetic kernel truncation and activation estimates go beyond the
face capacities used here.

## External finite rectangle input

We use the following finite form of Carleson's rectangle counterexample.
For every integer $N$ there is a finite family $\mathcal R_N$ of dyadic
rectangles in $[0,1)^2$ such that
$$
 \sum_{R\in\mathcal R_N}|R|=1,\qquad
 \left|\bigcup_{R\in\mathcal R_N}R\right|\le C_1/N,
 \tag{1}
$$
and, for every dyadic rectangle $F$,
$$
 \sum_{\substack{R\in\mathcal R_N\\R\subseteq F}}|R|
 \le C_2|F|.
 \tag{2}
$$
The constants are absolute. This statement and its finite construction
were checked on pages 1, 3, and 4 of
[Blasco--Pott, *Carleson's counterexample and a scale of Lorentz-BMO
spaces on the bitorus*](https://www.uv.es/oblasco/Investigacion/CHA/SandraMRL.pdf).
The transfer to congruences and the distinct-modulus refinement below
are separate arguments.

## Transfer to two different prime coordinates

For each second-coordinate dyadic interval $J$, choose a triadic interval
$J'\subseteq J$ with $|J'|>|J|/6$. To do so, choose a triadic grid
length $t$ satisfying $|J|/6<t\le|J|/2$; an interval of length at least
$2t$ contains a full grid interval of length $t$.

Replace $R=I\times J$ by $R'=I\times J'$ and give it weight
$$
 c_R=\frac{|R'|}{24C_2}.
$$
Then
$$
 \sum_Rc_R\ge\frac1{144C_2},\qquad
 \left|\bigcup_RR'\right|\le C_1/N.
 \tag{3}
$$
The modified rectangles satisfy the exact packing bound
$$
 \sum_{R'\subseteq I_0\times K}c_R\le|I_0\times K|
 \tag{4}
$$
for every dyadic $I_0$ and triadic $K$.

For verification, put $\ell=|K|$. If $R'\subseteq I_0\times K$, then
$I\subseteq I_0$, $J$ meets $K$, and $|J|<6\ell$. Choose a dyadic
grid length $h$ with $6\ell\le h<12\ell$, using $h=1$ if this
choice exceeds the ambient interval. Every such $J$ is contained in
an $h$-grid interval meeting $K$. Since $h\ge\ell$, there are at most
two such intervals, with total length at most $24\ell$. Applying (2)
to $I_0$ times those intervals bounds the sum of the original areas by
$24C_2|I_0\times K|$. Modified areas are no larger, proving (4).

The digit maps identify dyadic intervals with $2$-adic balls and triadic
intervals with $3$-adic balls, preserving measure and containment.
CRT therefore identifies the modified rectangles with full cylinders
$C_i=[a_i]_{q_i}$, $q_i=2^{u_i}3^{v_i}$. Combine any duplicate cylinders
by adding their weights. Equation (4) becomes every divisor-face bound
$$
 \sum_{\substack{i:d\mid q_i\\a_i\equiv b\pmod d}}c_i\le1/d.
 \tag{5}
$$
Faces containing other primes have no descendants. This already gives
an obstruction with $\omega(q_i)\le2$, but possibly repeated moduli.

## Distinct primitive moduli with at most three prime factors

For each base cylinder $C_i$, choose a finite pool $P_i$ of primes
greater than $3$, all pools disjoint, such that
$$
 1\le\sum_{p\in P_i}1/p\le2.
$$
Divergence of the prime reciprocal sum permits this. Replace the base
cylinder by
$$
 D_{i,p}=C_i\cap[0]_p,\qquad
 w_{i,p}=c_i/(2p)\quad(p\in P_i).
$$
The modulus is $q_ip$. Each tag prime occurs in exactly one modulus,
so all moduli are distinct and no one divides another. Also
$$
 \omega(q_ip)\le3,\qquad
 \mu\left(\bigcup_{i,p}D_{i,p}\right)\le C_1/N,
 \qquad \sum_{i,p}w_{i,p}\ge\frac1{288C_2}.
 \tag{6}
$$

All face capacities remain true. A face without a tag receives at most
the old total weight, since $\sum_{p\in P_i}1/(2p)\le1$.
A face with a tag prime has at most one descendant. Equation (5) for
the base cylinder itself gives $c_i\le1/q_i$, so its descendant weight
is at most $1/(2q_ip)\le1/d$ for every relevant divisor $d\mid q_ip$.
A face with two tags has no descendants.

## The exact harmonic cutoffs do not fix the obstruction

Let $Q$ be the largest tagged modulus, put $X=Q^3$, and halve all the
weights in (6). Every relevant divisor $d$ is at most $Q$, and
$$
 \frac{H_{\lfloor X/d\rfloor}}{H_X}
 \ge\frac{\log(X/d)}{1+\log X}
 \ge\frac{2\log Q}{1+3\log Q}>\frac12
 \qquad(Q\ge3).
$$
The new weights consequently satisfy
$$
 \sum_{\substack{i:d\mid q_i\\a_i\equiv b\pmod d}}w_i
 \le\frac{H_{\lfloor X/d\rfloor}}{dH_X},
$$
yet have total mass at least $1/(576C_2)$ and full union measure tending
to zero. Thus even the precise harmonic face constraints, together with
distinctness, primitivity, and $\omega(q)\le3$, cannot imply a uniform
small-footprint bound on the abstract total mass.

The previous [unbounded-rank face obstruction](rank_and_moment_obstructions.md#all-individual-divisor-face-capacities-still-miss-the-difficulty)
is therefore not merely a consequence of increasing the number of prime
coordinates. Large exponents already permit a fixed-rank obstruction.
Additional information specific to actual first-kill masses is necessary.

## Comparable two-prime base moduli cannot be repaired by refinement

There is a direct arithmetic obstruction to one attempted realization
of these abstract weights. Fix $C\ge1$. Let $U$ be any finite
periodic union, allowing multiple residues, all of whose base moduli
are of the form $2^u3^v$ and lie in $[Q,CQ]$. Put
$\beta=\mu(U)$. Suppose $B$ is a delayed singleton system with
globally distinct moduli, each divisible by a base modulus and with
each full cylinder contained in $U$. Then, uniformly in $X$,
$$
 \frac{|B\cap[1,X]|}{X},\quad
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le\max\left\{2\beta,\,
             O_C\left(\frac{(\log(2Q))^2}{Q}\right)\right\}.
 \tag{7}
$$

Indeed, there are $O_C(\log(2Q))$ distinct base moduli: for each
$u$, the allowed $v$'s occupy an interval of bounded length.
Their lcm is at most $(CQ)^2$, and their reciprocal sum is
$O_C(\log(2Q)/Q)$. Insert these facts into the established
[arbitrary divisor-refinement bound](compression_and_blocks.md#every-divisor-refinement-of-a-wang-block-is-uniformly-small),
equation (5). The number of base residues does not enter that lemma.
This proves (7).

In particular, if such a base family has $\beta\to0$ and
$Q\to\infty$, no choice of singleton divisor refinements can
realize a fixed positive harmonic mass, even with arbitrary composite
tags or repeated use of a tag prime on different base moduli.
The hypotheses include the comparable-modulus situation obtained
when a two-coordinate rectangle construction has common area before
the bounded-factor dyadic-to-triadic replacement. No assertion that
every rectangle obstruction admits that normalization is needed here.
