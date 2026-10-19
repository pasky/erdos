---
name: research/erdos_25/branch_separated_centers
desc: Logarithmic density for primewise bounded collisions of integer centers, including arbitrary residues close to either end relative to the least prime factor.
tags: [density, negative-dependence, small-residues, partial-results]
sources: []
created: 2026-09-22T09:25:34Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/branch_separated_centers

***

## Theorem: proved

Partition a family of globally distinct moduli into blocks $D_b$, indexed by
distinct integers $b\in\mathbb Z$, using the residue $b\pmod q$
throughout $D_b$, and suppose
$$
 |b|<\min D_b.
 \tag{1}
$$
Assume there is a fixed integer $R\ge1$ such that, for every prime
$p$ and every residue $u\pmod p$, at most $R$ centers $b$
satisfy both
$$
 b\equiv u\pmod p,
 \qquad p\mid q\text{ for some }q\in D_b.
 \tag{2}
$$
Then the delayed union, with the original activation $n\ge q$,
has logarithmic density equal to its full Haar union measure.
It has finite-periodic approximation in upper logarithmic density.

Write $H_B(X)=\sum_{n\le X,\ n\in B}1/n$, and let $H_N$ be the
ordinary harmonic sum. For a finite such system of Haar union measure
$\beta<1$, and every $X\ge1$,
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le\min\{1,R\log(1/(1-\beta))\}.
 \tag{3}
$$
This is a different extension of the
[bounded-prime-overlap block theorem](bounded_prime_overlap_blocks.md):
arbitrarily many blocks may use a prime, provided their centers have
bounded multiplicity in each first-digit branch.

**Corollary.** For every fixed $C>0$, the delayed union for arbitrary
normalized residues $0\le a_q<q$ has logarithmic density if
$$
 \min(a_q,q-a_q)<C P^-(q)\qquad(q>1).
 \tag{4}
$$
There is no coherence assumption. In particular the one-sided
condition $a_q<C P^-(q)$ suffices. Modulus one is trivial and can be
handled separately.

Choose the representative $b_q\equiv a_q\pmod q$ of smallest absolute
value, breaking a possible tie consistently. Then $|b_q|<q$, and
(4) gives $|b_q|<Cp$ whenever $p\mid q$. In the open interval
$(-Cp,Cp)$, a fixed residue modulo $p$ has at most
$\lceil2C\rceil$ integer representatives. Thus (2) holds with that
$R$. For the one-sided condition use $b_q=a_q\ge0$ and
$R=\lceil C\rceil$.

## A one-coordinate inequality

Let $x_p$ have Haar law on $\mathbb Z_p$. Suppose finitely many
nonnegative functions $f_b(x_p)$ have the following property: for
each $b$, there is a constant $c_b\ge0$ such that
$$
 f_b=c_b\text{ outside }[b]_p,\qquad 0\le f_b\le c_b\text{ everywhere}.
 \tag{5}
$$
Suppose each branch modulo $p$ has at most $R$ assigned functions.
Then
$$
 \mathbb E_p\prod_b f_b
 \le\prod_b(\mathbb E_p f_b^R)^{1/R}.
 \tag{6}
$$

To prove this, group the functions by their branch $u$, and write
$h_u=\prod_{b\equiv u(p)}f_b$, $C_u=\prod_{b\equiv u(p)}c_b$.
If a baseline is zero both sides are zero. Otherwise put
$t_u=\mathbb E_p(C_u-h_u)/C_u$. The depressions from the baselines
have disjoint supports, so
$$
 \mathbb E_p\prod_u h_u
 =\prod_u C_u\left(1-\sum_u t_u\right)
 \le\prod_u C_u\prod_u(1-t_u)
 =\prod_u\mathbb E_p h_u.
$$
Apply Hölder within each group of at most $R$ factors, padding with
constant-one factors when needed, to get (6). This argument allows
arbitrary variation within each branch; it does not assume that
different centers in the same branch have nested deeper balls.

For a product of prime-coordinate spaces, (6) can be iterated. If a
factor satisfies (5) at every coordinate on which it depends, replacing
it by $(\mathbb E_p f_b^R)^{1/R}$ preserves (5) at all other
coordinates: their pointwise baseline upper bounds survive integration
and taking positive roots. The $R$-norm operations commute across
independent coordinates. Thus
$$
 \mathbb E\prod_b f_b
 \le\prod_b(\mathbb E f_b^R)^{1/R}.
 \tag{7}
$$
Factors independent of a coordinate can be taken outside its integral.

## Apply the inequality to block survivors

For a finite subsystem put
$$
 U_b=\bigcup_{q\in D_b}[b]_q,\qquad \beta_b=\mu(U_b),\qquad
 f_b=\mathbf1_{G\setminus U_b},
$$
where $G=\widehat{\mathbb Z}$. With all other coordinates fixed,
$f_b$ is constant outside $[b]_p$, and cannot increase on that
branch. Classes in $D_b$ not divisible by $p$ may make it zero
everywhere; this is the zero-baseline case already included.
Condition (2) therefore permits (7), giving
$$
 1-\beta=\mu\Bigl(\bigcap_b U_b^c\Bigr)
 \le\prod_b(1-\beta_b)^{1/R}.
 \tag{8}
$$
For countable systems, exhaust finitely many classes in finitely many
blocks and pass to the limit. If the full survivor measure
$\delta=1-\beta$ is positive, (8) implies
$$
 \sum_b\beta_b
 \le\sum_b-\log(1-\beta_b)
 \le R\log(1/\delta)<\infty.
 \tag{9}
$$

## Exact harmonic control of a signed-center block

For every block satisfying (1), with delayed union $B_b$,
$$
 H_{B_b}(X)\le\beta_b H_{\lfloor X\rfloor}.
 \tag{10}
$$
For $b\ge0$, the block is exactly $b+M(D_b)$: every generator
exceeds $b$, and its active points are $b+tq$, $t\ge1$.
Subtracting $b$ does not increase the cutoff or decrease a harmonic
weight, so (10) follows from the
[exact multiples inequality](basic_reductions.md#an-exact-finite-harmonic-inequality-for-multiples-proved).

For $b=-c<0$, let $P_b$ be the primitive core of $D_b$.
Since $c<\min D_b$, the exact identity is
$$
 B_b=(M(D_b)\setminus P_b)-c.
 \tag{11}
$$
Indeed, a point $m=n+c$ divisible by a generator $q$ is active
unless $m=q$ and there is no proper generator divisor of $m$.
These exceptional points are exactly $P_b$; any proper generator
divisor is at most $m/2$, and $m-q\ge q>c$ makes its deletion
active at $n=m-c$.

Each point of $M(D_b)\cap(X,X+c]$ has a primitive divisor in
$P_b\cap[1,X+c]$. Different points cannot choose the same divisor:
every primitive divisor is greater than $c$, whereas the points
differ by less than $c$. Hence
$$
 |B_b\cap[1,X]|
 =|M(D_b)\cap[1,X+c]|-|P_b\cap[1,X+c]|
 \le |M(D_b)\cap[1,X]|.
$$
Partial summation and the exact multiples inequality again give (10).
For integer cutoffs this argument is literal; real cutoffs follow by
taking integer parts.

Each fixed signed-center block has finite-periodic logarithmic
approximation. For nonnegative centers this is the multiples theorem
and fixed translation. For negative centers, primitive sets are
logarithmically null, so (11) gives the same conclusion. More explicitly,
if $F\subset D_b$ is finite, then
$$
 B_b(D_b)\setminus B_b(F)
 \subseteq ((M(D_b)\setminus M(F))-c)\cup(P(F)-c),
$$
whose second term is finite. Finite approximation for multiples
therefore transfers to the delayed block.

## Finish the density theorem

For $\delta>0$, (9)--(10) show that all blocks outside any finite
selection have normalized harmonic mass at most the omitted sum of
their $\beta_b$. This tends to zero as the selection grows.
Approximate each of the finitely many retained blocks by finitely
many of its congruences. Finite unions preserve upper logarithmic
approximation, proving the theorem. Any such finite selection is
contained in an original finite initial segment of increasing moduli.

If $\delta=0$, finite delayed prefixes already imply natural
survivor density zero. For a finite family, summing (10) and using
(9) proves (3). One can also write the constant-factor consequence
$$
 H_B(X)\le\frac{\beta}{1-e^{-1/R}}H_{\lfloor X\rfloor}.
$$
This follows by splitting at $\beta=1-e^{-1/R}$ and using
monotonicity of $-\log(1-\beta)/\beta$.

The theorem makes no assertion of natural density when
$0<\delta<1$, and it does not control arbitrary moving residues
with unbounded primewise collision multiplicities.

## A sharper prime-power overlap criterion

Condition (2) can be weakened. For every block $b$ using a prime
$p$, put
$$
 e_{p,b}=\min\{v_p(q):q\in D_b,\ p\mid q\},
 \qquad V_{p,b}=[b]_{p^{e_{p,b}}}\subseteq\mathbb Z_p.
$$
It suffices that the balls $V_{p,b}$, counted once for each block,
have pointwise overlap at most $R$ for every prime $p$. The
theorem and its finite bound (3) then remain valid with this $R$.
Condition (2) implies this criterion, because
$V_{p,b}\subseteq[b]_p$.

To verify the extension, fix the other coordinates. The block survivor
factor is constant outside $V_{p,b}$, and is at most this baseline
everywhere. A finite family of $p$-adic balls with overlap at most
$R$ can be colored using $R$ colors so that balls of the same
color are disjoint. Indeed, order the balls from larger to smaller,
allowing repeated balls; all previously colored balls meeting a new
ball contain it. At most $R-1$ such balls exist, so greedy coloring
works.

Let $G_j$ be the product of the factors in color $j$, padding
with empty products if necessary. Hölder and the disjoint-support
inequality used above give
$$
 \mathbb E_p\prod_b f_b
 \le\prod_{j=1}^R(\mathbb E_p G_j^R)^{1/R}
 \le\prod_b(\mathbb E_p f_b^R)^{1/R}.
$$
The second inequality applies to the factors $f_b^R$ within each
color. Integration and positive roots preserve the baseline and the
suppression property outside each remaining prime's prescribed ball.
Thus the coordinate induction proving (7), and all subsequent steps,
apply unchanged. Infinite blocks follow by finite truncation: the balls
needed for a truncation are contained in the displayed $V_{p,b}$.
