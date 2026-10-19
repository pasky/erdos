---
name: research/erdos_25/compression_and_blocks
desc: A finite Haar-measure obstruction and the remaining counterexample mechanism.
tags: [compression, counterexamples]
sources: []
created: 2026-09-21T22:37:44Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/compression_and_blocks

***

## Finite union compression: proved

For any finite list of moduli $q_i$ and residues $a_i$, let $U$ be the union
of the full classes $a_i\pmod{q_i}$ and $M$ the union of $0\pmod{q_i}$.
Then
$$
d(U)\ge d(M).
$$
Here densities are periodic densities, not densities of delayed infinite
unions. Distinctness is unnecessary for this finite comparison.

**Proof.** Let $L=\operatorname{lcm}(q_i)$ and use CRT to decompose
$\mathbb Z/L\mathbb Z$ as the product of its prime-power coordinates.
Fix one prime $p$ and every coordinate other than its $p$-coordinate.
Each class whose other coordinates are compatible contributes one $p$-adic
ball of relative measure $p^{-v_p(q_i)}$. The union of these balls has
measure at least their largest measure. Replace every ball's center by
zero, for all classes simultaneously, leaving the other coordinates
unchanged. The resulting balls in this fiber are nested, so their union
has precisely the largest measure. Thus the replacement does not increase
any fiber measure, hence does not increase total measure. Iterate over all
prime coordinates to obtain the zero classes. $\square$

The introduction of the
[Filaseta–Ford–Konyagin–Pomerance–Yu source](../../../library/integer_sequences/filaseta_2007_sieving_large_integers_covering_systems_congruences/_index.md)
attributes this comparison to Rogers (paragraph defining $\delta^+(S)$).
The proof above was independently reconstructed; the source passage was checked.

## Why the supplied multi-residue construction is not a solution

The [Wang source](../../../library/integer_sequences/wang_2026_proposed_solution_erdos_problem_486/_index.md),
Lemmas 3.1–3.4 and Section 4, was checked. Its block at $Q=2^j$ assigns
$\gg Q$ endpoints to at most $2^k$ distinct moduli, where $k=O(\sqrt j)$.
Endpoints with the same label subset reuse one modulus but use different
residues; the endpoint interval is shorter than that modulus.
Keeping one residue per modulus therefore leaves at most $2^k$ endpoints
and local harmonic mass $O(2^k/Q)=o(1)$, not the fixed positive amount
needed for its logarithmic-density oscillation.

A possible counterexample mechanism remains conditional: construct long
epochs of singleton classes that remove a fixed proportion of logarithmic
mass while adding a summably small amount of eventual periodic measure.
Finite periodic recovery and the activation threshold then allow epochs to
be separated without changing earlier recovery averages. The missing
singleton block/epoch construction is not supplied by Wang's theorem.

## Uniform bound for bounded-quotient deletion: proved

Let $D$ be a finite set of distinct moduli, let $U=\bigcup_{q\in D}[a_q]_q$
be their full periodic union, and normalize $0\le a_q<q$. Write
$$
Z_X=\prod_{p\le X}(1-1/p)^{-1}.
$$
For $K\ge1$, let $T_K(X)$ consist of those $n\le X$ that are deleted by
some class with $q\le n\le Kq$. Then
$$
\sum_{n\in T_K(X)}\frac1n
 \le H_{\lfloor K\rfloor}\sum_{\substack{q\in D\\q\le X}}\frac1q
 \le H_{\lfloor K\rfloor} Z_X\,d(U).
\tag{1}
$$
The first inequality sums $1/(a_q+tq)\le1/(tq)$ over the possible
integers $1\le t\le K$ and then over the distinct moduli.

For the second, give each $X$-smooth integer $m$ mass $1/(Z_Xm)$.
Equivalently, its valuations at primes $p\le X$ are independent with
$\Pr(v_p(m)=e)=(1-1/p)p^{-e}$.
For $D_X=D\cap[1,X]$, the probability that some $q\in D_X$ divides $m$
is exactly $d(M(D_X))$: the geometric valuation tails are $p^{-e}$,
identical to Haar valuations. Every $q\in D_X$ is itself $X$-smooth and
belongs to $M(D_X)$, so
$$
\sum_{q\in D_X}\frac1q\le Z_X d(M(D_X))\le Z_Xd(U),
$$
where the last inequality uses finite compression and inclusion.
Distinctness matters in the first sum: multiple residues at one modulus
cannot be counted repeatedly as distinct atoms of the smooth distribution.

The classical bound $Z_X\ll\log(2X)$ therefore makes (1) a uniform
weak-type estimate with constant $O(H_{\lfloor K\rfloor})$.
The smooth-number identity and this Euler-product bound were checked in the
[Davenport–Erdős 1951 source](../../../library/divisors/davenport_1951_sequences_positive_integers/_index.md),
equations (5)–(7) and the paragraph before (12). They are only being used
for zero-class multiples, where their hypotheses apply.

Consequently no sequence of finite singleton epochs with periodic footprints
tending to zero can delete a fixed positive normalized logarithmic mass
using a uniformly bounded ratio $n/q$. This rules out the direct singleton
analog of Wang's epochs, not merely one construction of their dyadic blocks.
It leaves deletion with unbounded quotient $n/q$ and conditioned-tail
constructions unresolved.

## Summable footprints and selected endpoints: proved

Suppose finite blocks $D_j$ have pairwise disjoint modulus sets and full
periodic unions $U_j$ with $\sum_jd(U_j)<\infty$. Select at most one
endpoint $m_q\ge q$ per modulus. The union of all selected endpoints has
logarithmic density zero. Indeed, endpoints from finitely many blocks form
a finite set. For the tail $j\ge J$ and any cutoff $X$, apply finite
compression to its moduli $q\le X$ and the union bound to obtain
$$
\sum_{\substack{m_q\le X\\q\in\bigcup_{j\ge J}D_j}}\frac1{m_q}
\le\sum_{\substack{q\le X\\q\in\bigcup_{j\ge J}D_j}}\frac1q
\le Z_X\sum_{j\ge J}d(U_j).
$$
Taking an upper logarithmic density and then $J\to\infty$ proves the claim.
The same proof permits any fixed finite number of selected endpoints per
modulus. Endpoint coincidences only reduce the harmonic sum.

## Quantitative dyadic obstruction: proved

If $D\subset[Q,2Q)$ and $|D|\ge cQ$, then, for arbitrary singleton residues,
$$
d(U)\ge \frac{c^2}{16(1+\log(2Q))}.
$$
To see this, let $Y=\sum_{q\in D}\mathbf1_{[a_q]_q}$ on the common finite
period. Then $\mathbb EY\ge |D|/(2Q)$ and
$$
\mathbb EY^2\le\frac1{Q^2}\sum_{q,r\le2Q}\gcd(q,r)
\le4\sum_{d\le2Q}\frac{\varphi(d)}{d^2}
\le4(1+\log(2Q)).
$$
The middle inequality follows by writing
$\gcd(q,r)=\sum_{d\mid q,\ d\mid r}\varphi(d)$.
Cauchy–Schwarz gives the claim. Thus such blocks at every dyadic scale
$Q=2^j$ cannot have summable individual footprints. This is weaker than
(1) for entire logarithmic epochs, but has a direct elementary proof.

## Sharpening the harmonic constant

The exact multiples inequality (2) in
[basic reductions](basic_reductions.md#an-exact-finite-harmonic-inequality-for-multiples-proved)
improves every occurrence of $Z_X$ in the bounds above to
$H_{\lfloor X\rfloor}$. Indeed,
$$
\sum_{q\in D_X}\frac1q
\le H_{M(D_X)}(X)
\le d(M(D_X))H_{\lfloor X\rfloor}
\le d(U)H_{\lfloor X\rfloor}.
$$
Thus the limiting constant in (1) is at most $H_{\lfloor K\rfloor}$,
with no Mertens theorem needed. The earlier smooth-product bounds remain
valid but are weaker.

## Nearby-multiple injections need not exist

Section 6.3 of the [[research/erdos_25/independent/profinite_shifts_and_long_windows|third independent record]]
correctly rules out a pointwise way of applying the multiples inequality.
There is no absolute $C$ such that every delayed singleton union admits
an injection taking each deleted integer $n$ to a multiple of a witnessing
modulus at most $Cn$.

Indeed, fix integers $K\ge2$ and $q\ge K$, and use the distinct moduli
$kq$ with residues $k-1$, for $1\le k\le K$. Their full cylinders lie
in distinct residues modulo $q$, so their footprint is exactly $H_K/q$.
At $X=Kq$ the active union satisfies
$$
 |B\cap[1,X]|
 =\sum_{k=1}^K\left\lfloor\frac{Kq-k+1}{kq}\right\rfloor
 \ge KH_K-2K.
$$
Every target multiple belongs to $q\mathbb N$, which has only
$\lfloor CK\rfloor$ points below $CX$. Choosing $K$ sufficiently
large contradicts even an injection into this larger target set, without
requiring it to respect the particular witness. The original footprint
is $H_K/q$, not the compressed footprint $1/q$; ignoring the distinct
residue fibers loses exactly the information this attempt needed.

## Rough moduli in a fixed power range have small reciprocal cost

The stronger support estimate in Section 6.4 of the same input is also
valid. Fix $u\ge1$ and $y\ge2$. If $D$ consists of distinct integers
$q\le y^u$ with no prime factor at most $y$, and $U$ is any singleton
residue assignment on $D$, then
$$
 \sum_{q\in D}\frac1q\le C_u\,d(U).
 \tag{R}
$$
The constant depends only on $u$. Modulus $1$, if present, causes no
exception to the argument.

Here are the missing uniform details. The
[elementary prime estimates](coprime_entropy.md#elementary-prime-estimates)
give $\sum_{y<p\le y^u}1/p=O_u(1)$. Every $y$-rough integer at most
$y^u$ has at most $\lceil u\rceil$ prime factors counted with
multiplicity. Summing over ordered prime tuples therefore proves
$$
 R_u(y):=\sum_{\substack{n\le y^u\\P^-(n)>y}}\frac1n=O_u(1),
$$
where the sum includes $1$. For a fixed $q\in D$, expanding the gcd
and then writing $r=ds$ yields
$$
 \sum_{r\in D}\frac{(q,r)}r
 \le\sum_{d\mid q}\frac{\varphi(d)}d R_u(y)
 \le 2^{\lceil u\rceil}R_u(y)=O_u(1).
$$
If $Z=\sum_{q\in D}\mathbf1_{[a_q]_q}$ and
$S=\mathbb EZ=\sum_{q\in D}1/q$, compatibility and CRT give
$\mathbb EZ^2\le C_uS$. Cauchy--Schwarz gives
$S^2\le d(U)\mathbb EZ^2$, proving (R).

The fixed roughness range is essential: bounded prime rank alone does
not bound reciprocal support cost, as all prime moduli demonstrate.
The counting and harmonic consequences of (R) are already subsumed by
the [bounded-rank finite theorem](bounded_prime_rank.md). Neither
result controls incremental footprints inside an earlier survivor set.

## Infinite multiplier simulation preserves measure, not the anomaly

There is an exact eventual-measure simulation of a countable multi-residue
system by globally distinct singleton moduli. Normalize every original
pair as $(q,a)$ with $0\le a<q$. Partition primes into disjoint sets
$P_{q,a}$, each with divergent reciprocal sum, and discard the finitely
many primes $p\le q$ from its assigned set. Such a partition can be made
by assigning successive finite prime batches of reciprocal sum at least
one to each index infinitely often. Replace $(q,a)$ by
$$
a\pmod{qp}\qquad(p\in P_{q,a}).
$$
All new moduli are distinct: $qp$ has unique largest prime factor $p>q$,
and disjoint prime assignments distinguish repeated original moduli.
Writing an original hit as $n=a+qk$, the lifted delayed union removes it
exactly when $k$ has a prime divisor in $P_{q,a}$. Such a divisor satisfies
$qp\le qk\le n$, so activation is respected.

For each fixed original class the omitted quotient set has natural density
zero, by the finite upper bound $\prod_{p\in F}(1-1/p)$ as
$F\uparrow P_{q,a}$. The same conditional Haar calculation proves that
the completed periodic unions agree up to a null set. Thus a finite
original family and its infinite lift differ on a natural-density-zero
set, and the full countable Haar unions also have equal measures.

This does **not** transfer logarithmic-density failure for arbitrary
multi-residue systems: a countable union of the omitted
natural-density-zero sets is uncontrolled. Every lifted modulus exceeds
$q^2$, so the lift misses every original hit below $q^2$. For Wang's
particular construction, the stronger result below proves that its
infinite prime lift actually has natural density.

## Arbitrary quotient ranges and a logarithmic-moment constraint

The bounded-quotient obstruction extends to any set of quotient indices.
For a finite singleton family with periodic footprint $\beta$, and
$T\subseteq\mathbb N$, let $B_T$ be the union of the hits $a_q+tq$
with $t\in T$. Distinctness and the previously proved compression bound give
$$
 H_{B_T}(X)
 \le\sum_{q\le X}\frac1q
       \sum_{\substack{t\in T\\t\le X}}\frac1t
 \le\beta H_{\lfloor X\rfloor}
       \sum_{\substack{t\in T\\t\le X}}\frac1t.
 \tag{3}
$$
In particular a multiplicative quotient window $T=[R,KR]\cap\mathbb N$
has harmonic contribution at most
$$
 \beta\left(\log K+1/\lceil R\rceil\right)H_{\lfloor X\rfloor}
 \qquad(R\ge1,\ K\ge1).
$$
Making the quotients large without making their logarithmic range broad
therefore does not evade the obstruction.

More quantitatively, select any one witnessing quotient $t(n)$ for every
deleted $n\le X$, and write $\alpha=H_B(X)/H_{\lfloor X\rfloor}$.
For $\beta>0$, (3) implies
$$
 \frac1{H_{\lfloor X\rfloor}}
 \sum_{\substack{n\le X\\n\in B}}\frac{\log t(n)}n
 \ge\frac{(\alpha-\beta)_+^2}{2\beta}.
 \tag{4}
$$
Indeed the normalized mass with $\log t(n)\le y$ is at most
$\beta H_{\lfloor e^y\rfloor}\le\beta(1+y)$.
Integrating the lower bound
$(\alpha-\beta(1+y))_+$ for the complementary mass proves (4).

This is a necessary condition on a small-full-footprint counterexample
epoch, not a sufficient condition and not a bound for conditioned tails.

## Every divisor-refinement of a Wang block is uniformly small

The following proved bound handles arbitrary composite multipliers and
unbounded quotient ranges, rather than only selected early endpoints.

**Refinement lemma.** Let $U$ be a periodic union of residue classes using
the finite set of base moduli $q_1,\ldots,q_M$. Put
$$
 \beta=d(U),\quad q_0=\min_jq_j,\quad
 L=\operatorname{lcm}(q_1,\ldots,q_M),\quad W=\sum_j1/q_j.
$$
Let $B$ be any finite or infinite delayed singleton union with globally
distinct moduli $r$, where each $r$ is divisible by some $q_j$ and each
full refined cylinder is contained in $U$. Then
$$
 \sup_{X\ge1}\frac{|B\cap[1,X]|}{X}
 \le\max\left\{2\beta,\ W\left(1+\log\frac L{q_0}\right)\right\}.
 \tag{5}
$$
The same bound holds for $H_B(X)/H_{\lfloor X\rfloor}$.

**Proof.** Activation and distinctness give
$$
 \frac{|B\cap[1,X]|}{X}
 \le\sum_{\substack{r\le X\\r\text{ used}}}\frac1r
 \le\sum_{j=1}^M\frac1{q_j}H_{\lfloor X/q_j\rfloor}.
$$
For $q_0\le X\le L$, this is at most the second quantity in (5);
below $q_0$ there are no hits. For $X\ge L$, the inclusion $B\subseteq U$
and the fact that a partial period contains at most all $\beta L$
occupied residues give
$$
 |B\cap[1,X]|\le\beta X+\beta L\le2\beta X.
$$
Partial summation transfers this uniform counting bound to harmonic
weights. This proves (5). $\square$

For a Wang block, write $Q=2^j$, $k=2\lfloor\sqrt j/8\rfloor$, and let
$M\le2^k$ be its number of used base moduli. Lemmas 3.1 and 3.4 of the
[full source](../../../library/integer_sequences/wang_2026_proposed_solution_erdos_problem_486/_index.md)
give
$$
 19Q/20\le q_i\le21Q/20,\qquad |E|\ge3Q/8,\qquad
 \beta\le\eta_j=e^{-k/100}.
$$
The passages defining $q_m=q_{K(m)}$, the diameter assertion in Lemma 3.1,
and Lemma 3.4 were checked in the full source for this application.
Endpoints attached to a common modulus are different residues, since
their interval has diameter smaller than that modulus. Pigeonholing gives
$$
 \beta\ge\frac{|E|}{M(21Q/20)}\ge\frac5{14M}.
$$
On the other hand,
$$
 W(1+\log(L/q_0))
 \le R_j:=\frac{20M}{19Q}\left(1+M\log\frac{21Q}{20}\right),
$$
and therefore
$$
 \frac{R_j}{\beta}
 \le\frac{56M^2}{19Q}\left(1+M\log\frac{21Q}{20}\right)
 =O(M^3\log Q/Q)=o(1).
$$
Here $M\le2^k$, $k\le\sqrt j/4$, and $Q=2^j$. Thus for every
sufficiently large Wang block, every singleton divisor-refinement obeys
$$
 |B_j\cap[1,X]|\le2\beta_jX,\qquad
 H_{B_j}(X)\le2\beta_jH_{\lfloor X\rfloor}
 \quad\text{for every }X.
 \tag{6}
$$
This rules out repairing one of these blocks by arbitrary long-quotient
divisor refinements. It does not assume the refined moduli are prime
extensions, nor any upper bound on their sizes.

### Natural density of the full fresh-prime lift

Apply the disjoint-prime lift described above to every original
congruence pair in Wang's system. Its moduli are globally distinct.
For a fixed original pair $(q,a)$, the omitted positive quotient integers
avoid every prime in $P_{q,a}$ and have natural density zero, by
$\sum_{p\in P_{q,a}}1/p=\infty$ and finite CRT products. Thus the lift
of any finite number of original blocks differs from their delayed
original union by a natural-density-zero set. In particular its natural
density equals that finite union's Haar measure.

By (6), the lifted union of all blocks beyond $J$ has, uniformly in $X$,
at most $2X\sum_{j>J}\beta_j$ hits below $X$. This tends to zero after
division by $X$ and then $J\to\infty$, since
$\sum_j\beta_j\le\sum_j\eta_j<\infty$. Finite-block approximation now
proves
$$
 d(B_{\rm lift})=\mu\left(\bigcup_jU_j\right).
$$
So this infinite singleton lift has **natural density**, and hence
logarithmic density. It cannot be a counterexample to Problem 25.
Arbitrary other refinements of a fixed finite number of source blocks
need not be settled by this argument; (6) controls their remote-block
tails, not every possible system inside one parent cylinder.

## Refinement trees with summable parent mass

There is a further natural-density criterion for recursive covering
constructions. A node of a rooted tree is a cylinder
$C_v=[a_v]_{Q_v}$. Expanding it installs finitely many classes contained
in $C_v$, with moduli divisible by $Q_v$, and partitions the remaining
part of $C_v$ into finitely many child cylinders. Write $D_v$ for the
part removed by this expansion. Ancestor expansions precede descendant
expansions in this description; the installed congruences themselves
are still activated by their numerical moduli.

**Proposition.** If
$\sum_{v\text{ expanded}}\mu(C_v)<\infty$, the full delayed union has
natural density equal to its Haar union measure. In particular this
holds if there is a fixed $\eta>0$ such that
$\mu(D_v)\ge\eta\mu(C_v)$ at every expanded node.

**Proof.** Every activated deletion made at node $v$ occurs in $C_v$
at an integer at least $Q_v$. Its count below $X$ is therefore at most
$X/Q_v$. The union of the deletions made outside any finite collection
of expanded nodes has count at most
$$
 X\sum_{v\text{ omitted}}\frac1{Q_v}.
$$
Finite approximation proves the first assertion. For the second,
the $D_v$ are pairwise disjoint, including for ancestor--descendant
pairs, because descendants lie in their ancestors' surviving regions.
Hence
$$
 \sum_v\mu(C_v)\le\eta^{-1}\sum_v\mu(D_v)\le\eta^{-1}.
$$
This proves the proposition. No multiplicity restriction is needed for
this criterion; it applies in particular when the installed moduli
are globally distinct. $\square$

The fixed-efficiency survivor-tree construction in the proof of Theorem 10.2
(Section 10, printed pp. 410–413) of the
[Balister et al. source](../../../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/_index.md)
falls within this criterion: its local surviving fraction is at most
$e^{2-t}<1$. That construction and its final reciprocal-cost calculation
were checked in the full source. Its direct infinite iteration therefore
cannot furnish the requested counterexample.

If the local efficiencies $\eta_v=\mu(D_v)/\mu(C_v)$ vary, the proof
still applies whenever $\sum_v\mu(D_v)/\eta_v<\infty$.
It supplies no bound when the parent masses are nonsummable and the
efficiencies tend to zero. In particular it does not rule out an
arbitrary conditioned-tail construction.

### Bounded-quotient nullity without an efficiency hypothesis

For bounded-quotient hits there is a stronger conclusion, even when the
parent masses are nonsummable and the local efficiencies tend to zero.
Assume that all installed moduli are globally distinct and that each
modulus carries one residue class. For an expanded node $v$, let
$\mathcal F_v$ be its finite family of installed full cylinders and set
$$
 D_v=\bigcup_{C\in\mathcal F_v}C.
$$
Thus $D_v$ is the full periodic union installed at that node, not merely
its activated part or a first-kill subset.

**Proposition.** For every fixed real $K\ge1$, the set
$$
 T_K=\{n\ge1:\text{some installed }[a]_q\text{ satisfies }
                    n\equiv a\pmod q,\ q\le n\le Kq\}
$$
has logarithmic density zero. In particular this holds for all first-kill
endpoints with a uniformly bounded ratio $n/q$.

**Proof.** The sets $D_v$ are pairwise disjoint. If $w$ properly descends
from $v$, then $C_w$ lies in a surviving child region of $v$, and
therefore avoids every class installed at $v$. For incomparable nodes
$v,w$, the cylinders $C_v,C_w$ lie in disjoint child cylinders at their
first branching ancestor. Consequently
$$
 \sum_v\mu(D_v)\le\mu(C_{\rm root})\le1.
$$
Enumerate the expanded nodes as $v_1,v_2,\ldots$, and put
$\tau_J=\sum_{j>J}\mu(D_{v_j})$. Then $\tau_J\to0$.

Let $T_{K,J}$ consist of the hits defining $T_K$ whose witnessing class
was installed at a node $v_j$ with $j>J$. For a cutoff $X$, only moduli
$q\le X$ can witness such hits. There are finitely many of them, by
global distinctness. The bounded-quotient estimate proved above,
together with the sharpened harmonic compression bound, gives
$$
 \sum_{\substack{n\le X\\n\in T_{K,J}}}\frac1n
 \le H_{\lfloor K\rfloor}
       \sum_{\substack{q\le X\\q\text{ installed beyond }J}}\frac1q
 \le H_{\lfloor K\rfloor}H_{\lfloor X\rfloor}\tau_J.
$$
Indeed, the full union of these finitely many classes is contained in
$\bigcup_{j>J}D_{v_j}$, of Haar measure $\tau_J$. The classes from the
first $J$ nodes contribute only finitely many hits with $q\le n\le Kq$,
because each of these nodes installs finitely many classes. Dividing by
$\log X$, letting $X\to\infty$, and then letting $J\to\infty$ proves
the proposition. $\square$

The proof counts all bounded-quotient hits, not only first kills. Every
counted hit satisfies the actual activation condition $n\ge q$;
reordering the installed classes by numerical modulus does not change
this inclusion. Thus the conclusion does not require the construction's
ancestor order to agree with numerical modulus order.

This excludes an endpoint-only counterexample from any such refinement
tree, including one with collapsing efficiencies. It does not establish
logarithmic density for the entire delayed union: deletions with
unbounded quotient ranges remain unresolved when the summable-parent
criterion is unavailable.
