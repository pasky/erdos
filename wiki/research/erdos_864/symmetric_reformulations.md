---
name: research/erdos_864/symmetric_reformulations
desc: Positive-half characterization, modular constructions, and the relation to four-independent sets and Lee packings.
tags: [proved, reductions, constructions]
sources: []
created: 2026-09-23T02:15:22Z
updated: 2026-09-24T22:12:55Z
---


# research/erdos_864/symmetric_reformulations

***

## Positive-half characterization

Let $B\subset(0,L]$ be a finite set. Then $A=B\cup(-B)$ has
unique unordered sums away from zero if and only if

$$
 B\text{ is Sidon},\qquad (B+B)\cap(B-B)=\varnothing. \tag{1}
$$

Indeed the positive sums from $A$ are sums from $B+B$ and positive
differences from $B-B$. Sidon uniqueness makes each of these types
individually unique, and the disjointness prevents cross-type collisions.
The negative sums follow by reflection. Conversely each requirement
follows immediately from uniqueness for $A$.

The second condition in (1) is equivalent to

$$
 (B+B+B)\cap B=\varnothing. \tag{2}
$$

Thus the fully symmetric part of the target would follow from

$$
 |B|\le(\sqrt{2/3}+o(1))\sqrt L
$$

for Sidon, $(3,1)$-sum-free sets $B\subset[1,L]$. This statement
has **not** been proved here. Taking a dense Sidon set in
$(L/3,L]$ attains the proposed constant.

If zero is also to be included in $A$, one must additionally require
$(B+B)\cap B=\varnothing$. Omitting this condition is not legitimate,
although deleting a single central element from an existing example
does not affect its leading size.

## Modular lifting

Call $T\subset G$ symmetric Sidon with center zero if $T=-T$, and
every nontrivial equality of two unordered pair sums has common sum zero.
If $G=\mathbb Z_n$ and $T$ has no nonzero element of order two,
choose its centered representatives in $(-n/2,n/2)$. Modular
nonexceptional sum uniqueness implies integer nonexceptional sum
uniqueness. An exceptional sum is a multiple of $n$, but the integer
pair sums lie in $(-n,n)$, so it can only be zero. The representatives
can be translated into $[n]$.

In particular a cyclic symmetric Sidon family with
$|T|>(2/\sqrt3+\varepsilon)\sqrt n$ would disprove the interval
conjecture. No such family was found.

## The modulus-three construction

Let $D\subset\mathbb Z_v$ be modular Sidon, with $\gcd(v,3)=1$.
In $\mathbb Z_3\times\mathbb Z_v$, put

$$
 T=(\{1\}\times D)\cup(\{-1\}\times(-D)).
$$

The two same-copy sum types and the mixed type have distinct first
coordinates. Nonzero mixed sums are unique because nonzero differences
in $D$ are unique. Thus $T$ is symmetric Sidon. Under CRT it gives
an admissible integer set of size $2|D|$ in $[3v]$. Ordinary modular
Sidon sets of size $(1+o(1))\sqrt v$ reproduce the constant
$2/\sqrt3$.

This construction also cautions against assuming that equality requires points
near the two ends of an interval. For example take a Singer difference set with
$v=q^2+q+1$, $|D|=q+1$, and $q=2^{2r+1}$, so $\gcd(v,3)=1$. The
difference-set identity gives $|\widehat{1_D}(\chi)|=\sqrt q$ at every
nonprincipal character. For every fixed nonzero integer Fourier frequency on
$\mathbb Z_{3v}$, the $\mathbb Z_v$ component is nonprincipal for all
sufficiently large $v$. The normalized Fourier coefficient of $T$ is
therefore $O(q^{-1/2})$. Weyl's criterion gives uniform macroscopic
distribution of the representatives in $[0,3v]$. For the standard Singer
construction, see §3.4 and entry [4] of
[source record](../../../library/additive_bases/obryant_2004_complete_annotated_bibliography_work_related_sidon/_index.md).
Its Sidon property and $(q+1)q=v-1$ show that every nonzero difference occurs
exactly once, which proves the character identity used above. No upper bound in
these notes uses this construction.

## Four-independence and a related conjecture

A subset $B$ of an abelian group is *four-independent* if
$\sum_{b\in B}\lambda_b b=0$ and
$\sum_b|\lambda_b|\le4$ imply that all integer $\lambda_b$ vanish.
For $B$ disjoint from $-B$, the following characterization holds:

$$
 B\text{ is four-independent}\quad\Longleftrightarrow\quad
 \{0\}\cup B\cup(-B)\text{ is symmetric Sidon with center zero}. \tag{3}
$$

For the reverse implication, convert a signed relation of length at most
four to an equality between two pairs, using signs to put each term in
$\pm B$ and padding with zero. A trivial pair equality, or an equality
in which both pairs are opposite pairs, makes all coefficients cancel.
For the forward implication, any forbidden pair equality gives a
nontrivial signed relation of length at most four.

Bajnok–Ruzsa, *The independence number of a subset of an abelian group*,
Integers 3 (2003), A02, Corollary 3.2 and Conjecture 3.3, prove bounds

$$
 (1/\sqrt8-o(1))\sqrt n\le s(\mathbb Z_n,4)
 \le(1/\sqrt2+o(1))\sqrt n
$$

and conjecture $s(\mathbb Z_n,4)\sim\sqrt{n/3}$.
See the
[full primary paper](https://arxiv.org/pdf/1512.03037), pp. 15–16.
This is a related conjecture, **not a theorem proving the target**.

The map $\mathbb Z^{|B|}\to\mathbb Z_n$ taking the standard basis to
the elements of $B$ is injective on the Lee ball of radius two exactly
when $B$ is four-independent. That ball has
$2|B|^2+2|B|+1$ elements. Thus a cyclic lattice packing density
asymptotically greater than $2/3$ would yield a counterexample through
(3) and centered lifting. If the map is not onto, use its image as the
quotient; its order, rather than $n$, is the packing denominator.

Xiao–Zhou, *On the packing density of Lee spheres* (2024), advertise radius-two
lattice packings with density tending to $2/3$, not a larger value. The
[publisher abstract](https://doi.org/10.1007/s10623-024-01410-0) does not
determine the cyclicity of their quotients or the details of their construction.
No result in these notes relies on that construction.

The relation to four-independence is not an equivalence for a symmetric
set without zero. In the positive-half formulation, equations
$x+y=z$ may occur. Their supports are pairwise disjoint: a shared
output violates Sidon uniqueness, a shared input repeats a difference,
and an output used as another input contradicts (2). Nevertheless,
there can be a positive proportion of such disjoint relations, so no
negligible-deletion reduction has been proved.

## A local endpoint-cover construction criterion

The asymmetric endpoint formulation
also permits deletion of individual signs. It gives a sparse construction
with a strict signed-cover saving and a sharp continuum obstruction to
macroscopic versions of that saving.

Let $D\subset[0,v]\cap\mathbb Z$ be ordinary Sidon and let
$0<w<v$ be an integer. Set

$$
 t=(v-w)/2,\qquad B=t+(D\setminus R).
$$

Then $B$ is Sidon, and $B\cap3B=\varnothing$ is equivalent to
requiring that $R$ meet the support of every relation

$$
 d_1+d_2+d_3=d_4-v+w,\qquad d_i\in D. \tag{4}
$$

Repeated inputs are permitted. Every input in such a relation belongs
to $D\cap[0,w]$, and the output belongs to $D\cap[v-w,v]$.
This follows immediately from nonnegativity and $d_4\le v$.

The symmetric set $\pm B$ lies in an interval of span $3v-w$.
Since $t$ is an integer or half-integer, a translation puts it in
an integer interval of length $3v-w+1$. If $|D|\sim\sqrt v$
and $w=\varepsilon v+O(1)$, this construction would beat the target
provided, for a fixed positive margin,

$$
 |R|<
 \left(1-\sqrt{1-\varepsilon/3}\right)\sqrt v.
 \tag{5}
$$

For small fixed $\varepsilon$, the required proportion is
$\varepsilon/6+O(\varepsilon^2)$.

Deleting all of $D\cap[0,w/3]$ is a valid cover: the remaining
three inputs have sum greater than $w$. For an asymptotically
maximal Sidon set in $[0,v]$, uniform distribution makes this cost
$(\varepsilon/3+o(1))\sqrt v$, twice the first-order allowance
in (5). No nongeometric cover meeting (5) was constructed. The
criterion isolates a possible integer-only route; it supplies no
asymptotic improvement by itself.

The [second-order construction](second_order_construction.md) does use
this criterion successfully when $w\asymp v^{3/4}$. Averaging over
$w$ permits deletion of only $O(v^{1/4})$ outputs and proves a
positive $N^{1/4}$ gain over the reflected lower bound along an
unbounded sequence. It does not handle fixed positive $w/v$.

There is also a limitation on replacing the geometric cover
by another macroscopic region. In normalized endpoint coordinates,
let measurable $U,V\subset[0,1]$ be the deleted input and output
regions. Suppose they cover every relation

$$
 x_1+x_2+x_3+y=1,\qquad x_i,y\in[0,1].
$$

The diagonal relations $3x+y=1$ show that

$$
 |U\cap[0,1/3]|+\frac13|V|\ge\frac13,
 \qquad\text{hence}\qquad |U|+|V|\ge\frac13. \tag{6}
$$

The same conclusion holds if coverage is required only almost
everywhere on the three-dimensional relation hypersurface. Otherwise
there is a density point $x$ of the surviving inputs for which
$1-3x$ is a density point of the surviving outputs. Three small
near-full neighborhoods of $x$, together with a near-full
neighborhood of $1-3x$, produce a positive-measure family of
uncovered relations, a contradiction.

Thus, in a continuum model with uniform endpoint densities, arbitrary
macroscopic deletion regions still cost at least
$\varepsilon\sqrt v/3$ when $w=\varepsilon v$.
This is a theorem about the stated continuum cover, **not** an
integer obstruction: passing from arithmetic covers of a sparse Sidon
set to this continuum hypothesis would require the missing
four-variable transfer. A successful fixed-proportion compression
would have to exploit information absent from this macroscopic model.

## A conditional pair-incidence obstruction to compression

There is a weaker sufficient transfer hypothesis than full four-variable
mixing. The following implication is proved, but its hypotheses have
not been established for the proposed Singer endpoint constructions.

Suppose $v\sim q^2$, $w/v\to\varepsilon\in(0,1/2)$, and
the endpoint empirical measures of $D$ are uniform. Form the
hypergraph of relations (4) with three distinct input vertices. For a
cover $R$, write $u(x),z(y)\in[0,1]$ for limiting deleted
densities in coordinates $x=d/w$ at the lower endpoint and
$y=(v-d)/w$ at the upper endpoint. Put $a=\int u$,
$b=\int z$. Let $E$ be the edge count, $I_L,I_U$ the
deleted lower- and upper-vertex incidences, and $J_{LL}$ the count
of pairs of deleted input vertices within edges.

Assume, uniformly over deletion sets,

$$
 E=(\varepsilon^3/36+o(1))q^2,\qquad
 I_L/E=9\int u(x)(1-x)^2\,dx+o(1),
$$


$$
 J_{LL}/E=18\iint u(x)u(y)(1-x-y)_+\,dx\,dy+o(1),
 \qquad I_U/E\le3b+o(1).                                      \tag{7}
$$

Then every cover has $|R|\ge(0.17-o(1))\varepsilon q$.

Indeed, an edge with $k\le3$ deleted input roles and $l\le1$
deleted output roles satisfies, whenever $k+l\ge1$,

$$
 1\le k+l-\tfrac23\binom{k}{2}.
$$

Summing and using (7) gives $1\le\mathcal F(u)+3b+o(1)$, where

$$
 \mathcal F(u)=9\int u(x)(1-x)^2\,dx
       -12\iint u(x)u(y)(1-x-y)_+\,dx\,dy.
$$

For $a\le0.17$, this functional is maximized at
$u=1_{[0,a]}$. To check the rearrangement, its first variation is

$$
 g_u(x)=9(1-x)^2-24\int u(y)(1-x-y)_+\,dy,
 \qquad g_u'(x)\le-18(1-x)+24a.
$$

It decreases on $[0,1-4a/3]$. On $[0,a]$ it is at least
$9(1-a)^2-24a$, whereas on $[1-4a/3,1]$ it is at most
$16a^2$. The former is larger for $a\le0.17$. Moving mass
from outside $[0,a]$ into its holes therefore increases the
functional, at every intermediate density.
Direct integration gives

$$
 \mathcal F(u)\le F(a)=9a-21a^2+15a^3.
$$

Since $F'(a)>3$ on $[0,0.17]$, $a+b\le0.17$ would imply
$\mathcal F(u)+3b\le F(0.17)=0.996795<1$, a contradiction.
Equivalently, apply this argument along any convergent subsequence
of normalized deletion measures. The continuous kernels make the
displayed functionals continuous under that passage.

This conditional deletion cost rules out improvement in (5) whenever
$0<\varepsilon<200/867$, since then
$0.17\varepsilon>1-\sqrt{1-\varepsilon/3}$.
At the first-order allowance $a+b=1/6$, the sharper check is
$F(1/6)=71/72<1$.

For Singer inputs, an unfinished approach to (7) represents the three-input
relation as a symmetric trilinear form on a projective line, and seeks an
auxiliary torus or additive-group law. Character sums could then control
input-pair incidences. A separate uniform fixed-output bound is still required:
except for boundedly many targets, ordered endpoint triple counts would need to
be at most $(\varepsilon^2/2+o(1))q$. The geometric irreducibility and
character noncancellation needed for that assertion remain unproved. No
unconditional Singer obstruction follows here.
