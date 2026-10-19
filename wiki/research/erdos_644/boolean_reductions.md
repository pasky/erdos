---
name: research/erdos_644/boolean_reductions
desc: Reliability and threshold-minor obstructions, exact promise relations and substitution, and the limitation of qualitative AND-solvable template classification.
tags: [proved, reductions, method-obstruction]
sources: []
created: 2026-09-22T22:54:42Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/boolean_reductions

***

Associate to a finite hypergraph $\mathcal H$ the monotone Boolean function
$f(R)=1$ exactly when $R$ contains an edge. Its positive minterms are the
inclusion-minimal edges. A set of variables fixed to zero forces $f=0$ exactly
when it is a transversal. These observations give reformulations, not either
requested asymptotic conclusion.

## Reliability can vanish at the Fano bias

Write $\mu_p(f)$ for the probability that an independently sampled Bernoulli-$p$
vertex set contains an edge. Assign each vertex independently and uniformly one
of the seven Fano caps. Each row union has the Bernoulli-$4/7$ distribution. If
$\mathcal H$ has $P_7$, these seven unions cannot all contain edges, since
choosing one edge inside each would produce a bad tuple. Consequently

$$
\mu_{4/7}(f)\le6/7.
$$

There is no positive lower bound at this bias from near-three-quarter
extremality, even with all Shapley values tending to zero.

Indeed, let $4\mid k$, put $n=7k/4-1$ and $s=\lceil k^{3/4}\rceil$. For every
core $k$-set $A\subseteq[n]$, append its own disjoint set $P_A$ of $s$ private
vertices. The resulting family has uniformity $K=k+s$ and retains $P_7$ from the
complete core family. Private padding preserves its transversal number: replace
each chosen private point by any core point of its unique edge to obtain a core
transversal of no greater size. Thus

$$
\tau=3k/4,\qquad \tau/K\longrightarrow3/4.
$$


Let $M$ count retained core vertices at bias $4/7$, and put
$a=\lceil k^{2/3}\rceil$. Then $M$ is binomial of mean $k-4/7$, and the
elementary binomial tail bound gives

$$
\Pr(M>k+a)\le\exp(-\Omega(k^{1/3})).
$$

Otherwise there are at most $\binom{k+a}{k}$ possible core witnesses, each
requiring all $s$ of its private vertices. Hence

$$
\mu_{4/7}(f)
\le\exp(-\Omega(k^{1/3}))+
\binom{k+a}{k}(4/7)^s=o(1),
$$

since $\log\binom{k+a}{k}=O(k^{2/3}\log k)=o(s)$.

The Shapley value of a variable is its probability of being the pivotal variable
in a uniformly random ordering. These values sum to one. The construction's
automorphisms have two vertex orbits, of sizes $n$ and $s\binom nk$, and Shapley
values are constant on each orbit. Their maximum is consequently at most
$1/n=o(1)$.

This excludes a positive critical-bias reliability estimate based only on
near-extremality and small Shapley values. It does not exclude an estimate
assuming a fixed positive excess $\tau>(3/4+\varepsilon)K$, or a reduction that
first removes private padding.

## Minors and fixed variables

Identifying vertices preserves $P_7$: the images of a local pair still cover the
image edges. But it need not preserve the ratio of transversal number to rank.
If all identification fibers have size at most $b$, lifting a cover only gives

$$
\tau(\mathcal H_{\rm image})\ge\tau(\mathcal H)/b,
$$

while individual edge sizes need not decrease by a factor $b$. Thus a theorem
producing symmetric threshold minors needs additional quantitative control
before it can prove the desired coefficient.

Fixing variables to zero deletes all edges meeting those variables, so it
preserves the local property. Fixing variables to one has no such general
preservation statement. For any monotone Boolean function $f(x)$,

$$
g(u,x)=u\wedge f(x)
$$

has a one-point transversal and hence $P_7$, while $g|_{u=1}=f$. Therefore
allowing arbitrary one-restrictions recovers every monotone Boolean function and
discards the local condition entirely.

The class also contains arbitrarily large overlapping double-AND functions. For
nonempty disjoint blocks $X,Y,Z$, put

$$
a=\Bigl(\bigwedge Y\Bigr)\wedge
\left(\Bigl(\bigwedge X\Bigr)\vee\Bigl(\bigwedge Z\Bigr)\right).
$$

All minterms share every variable of $Y$, so $\tau(a)=1$, regardless of the
block sizes. Thus a structural theorem requiring exclusion of all sufficiently
large such functions cannot apply to the whole $P_7$ class.

Restricting first to self-dual monotone functions does not remove this example
from the zero-restriction closure. Let $a^*(x)=1-a(\bar x)$. The common minterm
variable gives $a\le a^*$, so

$$
h(u,x)=\begin{cases}a(x),&u=0,\\a^*(x),&u=1\end{cases}
$$

is monotone and self-dual. For $y\in Y$, the set $\{u,y\}$ is a transversal,
hence $h$ has $P_7$, while setting $u=0$ recovers $a$.

These examples rule out the specified unrestricted uses of Boolean restrictions
and forbidden-minor hypotheses. They do not exclude every quantitative
Boolean-function approach to the ratio problem. The new
[Boolean factor reduction](boolean_factor_reduction.md) gives a controlled
exception to the prohibition on one-restrictions: independent factors with three
disjoint minterms may be removed. It also normalizes a hypothetical fixed-excess
counterexample to be conjunction-prime and low-Shapley at $o(k)$ transversal
cost.

## Small-rank guards can push the critical bias to one

The earlier private-padding example establishes vanishing reliability **at**
$p=4/7$; it must not be described as having critical bias tending to one. The
following different construction does establish that stronger obstruction.

Let $s-1$ run through primes. Let $\mathcal A$ be the complete $4s^2$-uniform
family on $7s^2-1$ points. It has $P_7$ and transversal number $3s^2$: seven
rows have total incidence $28s^2>4(7s^2-1)$, so some point meets at least five
rows, and any remaining two rows intersect.

Let $\mathcal G$ be the disjoint union of $m=3s$ projective-plane line families
of order $s-1$. In each plane there are $N=s^2-s+1$ points and lines, each line
has $s$ points, and each point lies on $s$ lines. Any line covers all lines,
while fewer than $s$ points cover at most $(s-1)s=N-1$ lines. Thus

$$
\operatorname{rank}(\mathcal G)=s,\qquad
\tau(\mathcal G)=ms=3s^2,\qquad
|E(\mathcal G)|=M=3s(s^2-s+1).
$$

These planes exist explicitly as the one- and two-dimensional subspaces of the
three-dimensional vector space over the field with $s-1$ elements.

On disjoint variables take $\mathcal F=\mathcal A\otimes\mathcal G$. The product
identities in [Boolean factor reduction](boolean_factor_reduction.md) give

$$
K=4s^2+s,\qquad \tau(\mathcal F)=3s^2,\qquad P_7,
\qquad \frac{\tau(\mathcal F)}K\longrightarrow\frac34.
$$

For every fixed $p<1$,

$$
\mu_p(f_{\mathcal F})\le\mu_p(f_{\mathcal G})\le Mp^s\longrightarrow0.
$$

Consequently the bias at which the reliability equals one half tends to one.
Automorphisms act transitively on the $7s^2-1$ core vertices and also on the
$mN$ guard vertices. Shapley values are constant within each of these sets and
sum to one, so their maximum tends to zero.

This disproves any threshold-location conclusion based only on
near-three-quarter extremality and vanishing maximum Shapley value. The
displayed product is removed by the factor theorem because $\mathcal G$ has
three disjoint edges. However, [Prime guard families](prime_guard_families.md)
now gives the same near-boundary obstruction even under conjunction-primality,
by deleting one product edge. It also proves a conditional guard transformation
for hypothetical fixed-positive-excess sequences and a safe projection criterion
for identifiable sparse partial products. No fixed-positive-excess
counterexample is constructed.

### Linear-size threshold minors are not automatic either

The same example bounds the size of symmetric threshold minors obtainable using
identifications and zero-restrictions. Every such minor still has the form
$a'\wedge g'$ (the variable sets may now overlap), where the minterm family of
$g'$ is contained in a union of at most $m$ intersecting families with at most
$M$ edges in total.

Here is the counting fact needed. Suppose such a family $\mathcal B$ on $q$
points has an edge in every $\ell$-set. Fix an integer $L\ge1$. From each
component having an edge of size at most $L$, choose one such edge. Their union
$S$, of size at most $mL$, meets every edge of those components. Every edge
disjoint from $S$ therefore has size at least $L+1$.

If $q-|S|\ge\ell$, a random $\ell$-subset of the complement of $S$ contains an
edge with probability at most

$$
M\left(\frac{\ell}{q-|S|}\right)^{L+1}.
$$

This probability must be one. If $q-|S|<\ell$, the following conclusion is
immediate instead. In both cases,

$$
q-\ell\le mL+\bigl(M^{1/(L+1)}-1\bigr)\ell.
\tag{1}
$$


If the original minor is the symmetric threshold $\ell$-of-$q$, every $\ell$-set
wins $g'$, so (1) applies. Put $L=\lceil\log M/\log(5/4)\rceil$. If its
transversal-to-rank ratio satisfies

$$
\frac{q-\ell+1}{\ell}>\frac34,
$$

then (1) yields

$$
\ell<2mL+2=O(s\log s)=O(\sqrt K\log K).
$$

Thus even near extremality one cannot demand an $\Omega(K)$-rank threshold minor
by these operations. This does not rule out a size-divergent minor or one
extracted under a fixed-positive-excess hypothesis.

## Finite promise relations and the exact substitution restriction

For fixed $r\ge3$, let $\mathscr S_r$ consist of the downward-closed families
$S\subseteq2^{[r]}$ in which no two members have union $[r]$. A monotone
function has $P_r$ exactly when, on any binary matrix whose columns lie in such
an $S$, its coordinatewise output is not $1^r$. For if all rows win, choose a
minterm inside each row; their spectra remain in $S$ by downward closure. The
converse uses the spectra of a bad tuple itself.

This describes a finite family of promise relations and is preserved by
identification of variables. It is not an assertion that the functions are
closed under composition.

There is an exact elementary distinction. An idempotent monotone function $g$
preserves every strong relation $S\in\mathscr S_r$ (its output itself belongs to
$S$) if and only if every at-most-$(r-1)$ winning minterms intersect.

For necessity, put $r-1$ winning rows with empty intersection above a zero final
row, repeating rows if necessary, and let $S$ be the downward closure of the
columns. No column contains all the first $r-1$ positions, whereas the output
does. For sufficiency, if fewer than $r$ rows win, their common input coordinate
contains the output support, so downward closure puts the output in $S$. If all
$r$ win, one input column covers the first $r-1$ rows and a second covers the
last, contradicting the definition of $S$. The zero output is already in $S$.

Equivalently, substituting the same inner family into every point of **every**
$P_r$ outer family preserves $P_r$ exactly when the inner family is $(r-1)$-wise
intersecting. For necessity use the outer family of two disjoint singletons,
taking the nonintersecting inner tuple on one side and one edge on the other.
For sufficiency, if neither outer covering point alone covers the selected rows,
assign rows to the two points with both parts nonempty; each part has at most
$r-1$ rows. If one outer point covers all rows, its inner copy alone supplies a
two-cover: intersect the first at most $r-1$ inner edges and separately cover
the last edge if necessary.

An inner family of rank $a$ satisfying this condition has

$$
\tau\le\left\lceil\frac a{r-2}\right\rceil:
$$

partition one edge into $r-2$ balanced parts and choose avoiding edges if the
bound fails. Thus for $r\ge4$ this universal substitution mechanism loses a
fixed factor asymptotically. It cannot supply the desired ratio-preserving
amplifier.

Section 6.1 of
[second independent record](independent/fractional_reductions_and_good_triples.md)
uses the stronger sufficient assumption of $r$-wise intersection. That argument
is correct, but the exact universal condition above improves its asymptotic loss
factor from $r-1$ to $r-2$ (from six to five for $r=7$). Neither condition is
asserted necessary for substitution into a particular restricted outer family.

There is also a small explicit failure of composition. Ternary majority has
$P_r$ for every $r$, since its three minterms have a global two-cover. Composing
it with three disjoint copies of itself gives the family choosing two of three
blocks $\{0,1,2\}$, $\{3,4,5\}$, $\{6,7,8\}$ and two points from each chosen
block. The following six admitted edges have no two-cover:

$$
\{0,2,4,5\},\ \{1,2,3,5\},\ \{0,1,6,7\},\
\{1,2,7,8\},\ \{3,4,6,8\},\ \{3,5,7,8\}.
$$

Every point has degree at most three. The degree-three spectra are

$$
234,\quad124,\quad256,\quad126,\quad346,\quad456;
$$

none is the complement of another, so two degree-three points do not cover all
six rows either. This is a finite certificate against iterated-majority
composition as a $P_7$-preserving amplifier; no claim about an optimal witness
size is needed.

No finite-template compactness or well-quasi-order argument proving convergence
was established. A proposed near-extremal antichain proof was not retained: it
incorrectly treated a universal graph vertex as a one-point vertex cover. No
claimed obstruction to a stronger critical-family preorder rests on that
argument.

## Why qualitative promise-template classification is insufficient

The finite promise formulation above does not, by itself, turn the problem
into a useful tractability dichotomy. For every $r$, its strong relations are
already preserved by coordinatewise AND of every positive arity.

Indeed, if $x^{(1)},\ldots,x^{(n)}\in S$ and $S$ is downward closed, their
coordinatewise AND lies below $x^{(1)}$ and hence belongs to $S$. Thus AND
strongly preserves every $S\in\mathscr S_r$. Such an $S$ excludes $1^r$, so
this also gives the required weak preservation. AND preserves the Boolean
order relation and the unary constants as well, if these are added to impose
monotonicity and idempotence.

There is a direct algorithmic check, requiring no classification theorem.
Consider constraints using these strong relations, unary constants, and order
implications. Propagate all forced ones along the implications. If a forced
zero is reached, there is no solution. Otherwise set precisely these forced
variables to one and all others to zero. This is the least assignment satisfying
the constants and implications. Any strong satisfying assignment dominates it,
so downward closure implies that the least assignment satisfies all strong
constraints whenever any strong solution exists. Checking it therefore decides
the strong constraint problem. Repeated variables in constraints do not affect
this argument.

Consequently, qualitative solvability holds for all $r$ and supplies no
$r$-dependent transversal-to-rank estimate. The particular AND function on
$n$ variables has one minterm of size $n$ and transversal number one, so its
presence says nothing about the large-transversal functions also in the same
class. This rules out an inference from qualitative tractability alone, not
every possible quantitative use of the promise relations.

The proposed use of [simultaneous criticality](incidence_minimal_families.md)
does not fix this automatically. Its normalization at transversal number
$t>1$ is not preserved under arbitrary minors: identifying all ground points
produces the singleton family of transversal number one. No rank-sensitive
threshold-minor theorem, or reliability bound at the Fano bias, was proved for
the normalized fixed-positive-excess families. Such a quantitative result
remains a missing step, not a consequence of AND preservation or of the
qualitative template formulation.

## Anchored residual families: a corrected intersection constraint

Let $\mathcal H$ have $P_7$, fix $A\in\mathcal H$, and, for $B\subseteq A$, put

$$
\mathcal F_B=\{E\in\mathcal H:E\cap A\subseteq B\}.
$$

Here three-wise intersection means that every nonempty subfamily of at most
three members has nonempty intersection.

**Lemma.** If $B,C\subseteq A$ are disjoint, $\mathcal F_B$ and $\mathcal F_C$
cannot both fail three-wise intersection.

**Proof.** Otherwise choose at most three rows from each family whose respective
intersections are empty. Adjoin $A$ and apply $P_7$. A two-point transversal
must have a point $x\in A$. If $x\in B$, it misses every selected $\mathcal F_C$
row; if $x\notin B$, it misses every selected $\mathcal F_B$ row. In either case
the other point would have to belong to an empty intersection, a contradiction.
$\square$

Writing $t=\tau(\mathcal H)$, one also has

$$
\tau(\mathcal F_B)\ge t-|A\setminus B|.
\tag{2}
$$

Indeed, a transversal of $\mathcal F_B$, together with $A\setminus B$, covers
$\mathcal H$. For a partition $A=B_1\cup\cdots\cup B_4$, at most one of the four
full-edge families $\mathcal F_{B_i}$ can fail three-wise intersection. If
$|A|=k$, the parts are balanced, and $t>(3/4+\varepsilon)k$, equation (2) gives

$$
\tau(\mathcal F_{B_i})>\varepsilon k-1
\qquad(i\in[4]).
$$

This does not give a contradiction: a three-wise-intersecting rank-$k$ family
can have transversal number as large as order $k$, and the elementary bound
$\lceil k/2\rceil$ does not control these positive-excess residual demands
sufficiently.

**The outside-trace version is false and is withdrawn.** The lemma does not
assert three-wise intersection of $\{E\setminus A:E\in\mathcal F_B\}$. For a
$k$-set $A$ containing distinct points $b,c$, with $k\ge2$, take three rows
$\{b\}\cup P_i$ and three rows $\{c\}\cup Q_i$, where the six private
$(k-1)$-sets are pairwise disjoint and disjoint from $A$. Together with $A$,
these rows have the global two-cover $\{b,c\}$ and hence $P_7$. Nevertheless,
for $B=\{b\}$ and $C=\{c\}$, both outside-trace triples have empty intersection.
The failed argument overlooked a two-cover using two points of $A$, one for each
group. Equation (2) remains valid, but no outside-intersection conclusion or
rank-sensitive approximate-factor extraction follows from this lemma.
