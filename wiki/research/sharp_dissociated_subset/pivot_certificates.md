---
name: research/sharp_dissociated_subset/pivot_certificates
title: Graded pivot certificates
desc: Graded and recentered pivot lemmas, a lattice form, and exact limits of their certificates. A split-leaf family obstructs the stronger odd extraction at every fixed aspect ratio above one.
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T18:14:21Z
---

# Graded pivot certificates

***

This note records the dissociation certificate behind
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_index|L212]]
in its most general form, and exact examples of what a certificate of
this kind cannot prove. Everything here is by Plasma AI and
author-recorded; nothing has independent review. The
[[research/sharp_dissociated_subset/proof_sketch|proof sketch]] uses it.

## The graded pivot lemma

For a nonzero integer $z$ let $v_2(z)$ be the exponent of $2$ in $z$.

**Lemma.** Let $a$ be a nonzero integer with $u=v_2(a)$, and let $b_j$
($j\in J$) be integers with $v_2(b_j-a)=j$, the levels $j$ pairwise
distinct. Put $N=|J|+1$. Suppose that for every $j\in J$ with $j\ge u$ and
$2^{j-u}\le N$,

$$
\sum_{i\in J,\ i\ge j}|b_i-a|\ <\ 2^{j-u}|a|.
$$

Then $\{a\}\cup\{b_j:j\in J\}$ is dissociated.

*Proof.* The elements are distinct, because the differences $b_j-a$ are
nonzero with distinct valuations. Put $\delta_j=b_j-a$ and consider a
ternary relation $\varepsilon_0a+\sum_j\varepsilon_jb_j=0$, that is,
$sa+\sum_j\varepsilon_j\delta_j=0$ with $s=\varepsilon_0+\sum_j\varepsilon_j$.
If every $\varepsilon_j$ vanishes, then $\varepsilon_0a=0$ and the
relation is trivial. Otherwise let $j_0$ be the least $j$ with
$\varepsilon_j\ne0$. The term $\varepsilon_{j_0}\delta_{j_0}$ is the only
$\delta$-term of valuation $j_0$ and the others have larger valuation, so
$s=0$ is impossible; and in a vanishing sum the least valuation of a
nonzero term is attained at least twice, so $v_2(s)+u=j_0$. Hence
$j_0\ge u$ and $2^{j_0-u}\le|s|\le N$, the hypothesis applies at $j_0$,
and

$$
2^{j_0-u}|a|\le|sa|=\Bigl|\sum_{j\ge j_0}\varepsilon_j\delta_j\Bigr|
\le\sum_{i\in J,\ i\ge j_0}|\delta_i|<2^{j_0-u}|a|,
$$

a contradiction. $\square$

The hypothesis imposes a separate budget only at levels
$u\le j\le u+\log_2N$. Higher levels still contribute to the tail sums
in these budgets; levels below $u$ do not.

## Special cases

- **Pure 2-adic deletion.** If no level of $J$ lies in the window, the
  hypothesis is empty. This is the binary residue-tree argument of
  [[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22]],
  which deletes the window $[u,u+\lfloor\log_2(d+1)\rfloor]$ and so loses
  $\log_2(d+1)$ levels.
- **Dominant pivot.** If $a>0$ and $\sum_{j}|b_j-a|<a$, every window
  condition holds. This is the $q=1$ case of Lemma A in
  [[theory/number_theory/L212_bounded_ratio_dissociated_subset/_proof|the proof of L212]],
  which loses no level but needs all companions within total distance $a$.
- **Odd elements.** If $a$ and every $b_j$ are odd, then $u=0$, every
  level is at least $1$, and $\sum_j|b_j-a|<2a$ suffices. The averaging of
  L212 with this doubled budget gives $|O|<3\,2^{d(O)-1}$, and hence
  $d(O)\ge\lfloor\log_2|O|\rfloor$, for a finite set $O$ of odd positive
  integers with $\max O\le2\min O$. This is proved in Step 4 of L212.

## Adding companions to a cheap star

Suppose a positive integer pivot $a$, with $u=v_2(a)$, has a set $J$ of
companions at distinct difference levels and total cost below $a$. Add
$r$ further companions at new distinct levels, all in $(0,2a]$. Put
$h=\lceil\log_2(r+1)\rceil$, and delete the companions whose levels lie
in $\{u,\ldots,u+h-1\}$. The survivors, with $a$, are dissociated and
number at least

$$
|J|+r+1-\lceil\log_2(r+1)\rceil.
$$

Indeed, each new companion costs at most $a$, so the total cost is below
$(r+1)a\le2^ha$. A surviving level below $u$ cannot be the least level
of a relation, while every surviving level $j\ge u$ has
$2^{j-u}a\ge2^ha$. The graded lemma applies at every required level.
For $r=0$ the deletion set is empty.

This loses a logarithm of the number of added companions, independent
of the size of the original cheap star. It does not guarantee new
levels: many elements outside the original block can all have the same
difference level from the pivot. Points above $2a$ also require their
actual costs to be accounted for. These are the two missing interfaces
in a proposed combination of blocks in the
[[research/sharp_dissociated_subset/proof_sketch|proof sketch]].

## Freely chosen centers

The point used for the archimedean estimate need not be the pivot of the
residue tree. This strictly enlarges the certificate family.

**Center lemma.** Let $D$ be an affinely dissociated set of positive
integers: a ternary relation whose coefficients sum to zero is trivial.
Suppose every ternary relation on $D$ has coefficient sum divisible by
an integer $q\ge1$. If some real $c>0$ satisfies

$$
\sum_{x\in D}|x-c|<qc,
\tag{C}
$$

then $D$ is dissociated. In particular $q=1$ is always available, and
$q=2$ is available when every element of $D$ is odd.

*Proof.* If a nontrivial relation has coefficient sum $s=0$, affine
dissociation excludes it. Otherwise $|s|\ge q$, and rewriting the
relation around $c$ gives

$$
qc\le |s|c=\left|\sum_{x\in D}\varepsilon_x(x-c)\right|
\le\sum_{x\in D}|x-c|<qc,
$$

a contradiction. For odd integers, reduction modulo two makes $s$ even.
More generally, a unit class modulo $q$ gives the divisibility assumption.
$\square$

A pivot and companions at distinct difference valuations are affinely
dissociated by the least-valuation argument. They can therefore use (C)
with any center, whether or not the center is the pivot or an element of
the ambient set. The choice can also vary with the level.

**A support threshold.** Suppose $P$ is a finite nonempty positive set,
$\max P\le R\min P$
with $R>1$, and every ternary relation on $P$ has coefficient sum zero
or absolute value at least an integer $q\ge1$. Put

$$
T=q+2\left\lfloor\frac q{R-1}\right\rfloor+1.
$$

Every affinely dissociated subset of $P$ with at most $T$ elements is
dissociated. Consequently, for $n=|P|\ge1$,

$$
d(P)\ge\min\bigl(\lceil\log_2n\rceil+1,T\bigr).
\tag{S}
$$

To prove the first assertion, orient an unbalanced relation so that its
numbers $p,t$ of positive and negative coefficients satisfy $p-t\ge q$.
Positivity gives $t\ge1$ and $p\ge2$. Since the elements are distinct,
the sum of the $p$ positive terms is strictly greater than $p\min P$,
whereas the negative terms sum to at most $tR\min P$. Equality of the
two sums therefore requires $q<t(R-1)$. Thus
$t\ge\lfloor q/(R-1)\rfloor+1$, and its support has at least
$p+t\ge q+2\lfloor q/(R-1)\rfloor+2=T+1$ elements. Smaller relations
must be balanced, and affine dissociation excludes them.

For (S), use the integer model and Kraft equality in
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_proof|L212]].
Some leaf has at least $\lceil\log_2n\rceil$ distinct difference levels;
the leaf and one representative from each level are affinely
dissociated. Take as many of these elements as the minimum in (S).
The integer model preserves balanced ternary relations, so this argument
also gives an affinely dissociated subset of the original real set.

In particular $R=2,q=1$ gives $T=4$, while $R=2,q=2$ gives $T=7$.
For odd positive sets of ratio at most two, (S) yields
$d(P)\ge\lceil\log_2n\rceil+1$ for $n\le64$; it also implies
$|P|\le2^{d(P)-1}$ whenever $d(P)\le6$. These are consequences of a
support bound, not finite searches. Tests on small odd sets do not
address the difficulty of unbalanced relations with larger support.

**Recentered graded lemma.** Let $a,b_j$ be positive integers with the
distinct difference levels of the graded pivot lemma, and put
$u=v_2(a)$ and $N=|J|+1$. For each $j\in J$ with $j\ge u$ and
$2^{j-u}\le N$, set
$D_j=\{a\}\cup\{b_i:i\in J,\ i\ge j\}$. Suppose some $c_j>0$ satisfies

$$
\sum_{x\in D_j}|x-c_j|<2^{j-u}c_j.
\tag{RC}
$$

Then $\{a\}\cup\{b_j:j\in J\}$ is dissociated.

*Proof.* In a nontrivial relation, let $j_0$ be the smallest used companion
level. As in the graded lemma, its coefficient sum satisfies
$v_2(s)+u=j_0$, so $j_0\ge u$ and
$2^{j_0-u}\le |s|\le N$. All used elements lie in $D_{j_0}$.
Rewriting around $c_{j_0}$ contradicts (RC), just as in the center lemma.
$\square$

The old graded lemma takes $c_j=a$. For a fixed set $D_j$, it is enough
to test centers among its elements: the function
$c\mapsto\sum_{x\in D_j}|x-c|-2^{j-u}c$ is piecewise linear with
breakpoints in $D_j$. If $2^{j-u}<|D_j|$, its minimum occurs at a
breakpoint or a whole interval between two; if $2^{j-u}\ge|D_j|$, its
value at $\max D_j$ is already negative.

The fixed examples below obstruct only their stated certificate models.
The [entry point](evidence/main.py) checks three separating witnesses.
For the bounded odd set $O'$ below, take pivot $1000471$, companions
$1001479,1990915,1990927,1991173$ and center $1990915$. Their difference
levels are $4,2,3,1$, respectively, and their total distance from the
center is $1980150<1990915$. Thus even (C) with $q=1$ certifies five
elements, whereas the original graded certificate reaches only four.
Likewise the retained six-element centered certificate in $B$ has total
cost $939845343<2000045707$, and a four-element centered certificate in
the diameter example has cost $764041<1000000$.

Allowing a free center does not give a universal diameter bound. The
32-element set $C$ retained in the entry point as
`_RECENTERED_DIAMETER` has diameter $512000052$, whereas

$$
\min_{a,J,c}\left(|a-c|+\sum_{j\in J}|b_j-c|\right)=512668211.
$$

The minimum ranges over every pivot $a\in C$, every five companions at
distinct difference valuations, and every real center $c$. To check this
coverage, a minimizing center for any fixed six-point selection can be
chosen among its medians, hence among $C$. For a fixed pivot and center,
take the nearest representative of each level and then the five cheapest
levels. The entry point checks these finitely many minima in exact
integer arithmetic.

This refutes the proposed statement that every binary tree with
$n\ge2^k$ leaves on an interval of length $L$ has a $k$-companion star
whose total distance from a free center is at most $L$. It does not
refute (C), the recentered graded lemma, or the sharp dissociation bound.
Indeed the retained minimizing star in $C$ has center $1024000059$,
larger than its cost, and is dissociated. A diameter argument would need
more than the prescribed residue tree, for example other affinely
dissociated selections or an adapted choice of binary characters.

## An obstruction to the stronger odd extraction

The precise result and a self-contained proof are
[[theory/number_theory/L270_recentered_pivot_obstruction/_index|L270, the split-leaf obstruction at every fixed ratio above one]],
at tier 0. The construction below explains its role in this route.

Free centers do not make single-pivot certificates sufficient for the
stronger odd bound $|O|\le2^{d(O)-1}$. In fact, for every $R>1$ there
is a positive odd integer set $O$ with $\max O<R\min O$ and an integer
$k$ such that

$$
|O|=2^{k-1}+1,
$$

but no recentered graded certificate has $k$ companions. The stronger
odd bound would require $k+1$ dissociated elements. The certificate
obstruction does not assert that this dissociated subset is absent.

Here is a construction. Choose $1<R_0<R$ and positive integers $h,l$
with

$$
h(R_0-1)>2,\qquad l(R_0-1)>2R_0,
$$

and put $k=h+l-1$. Begin with a perfect binary tree of height $k-1$
and replace one leaf by two children. Only those two children have
depth $k$; every other leaf has depth $k-1$. A star with $k$
companions must therefore use one of the two deepest leaves as pivot
and one representative of every sibling subtree along its path.

Place the two deepest leaves near $1$. Of their $k-1$ other sibling
subtrees, place all leaves of $h$ subtrees near $R_0$ and those of the
remaining $l-2$ subtrees near $1$. Every possible $(k+1)$-element star
then has $h$ high points and $l$ low points. At the limiting locations
$1,R_0$, its centered budget defect is

$$
F(c)=l|1-c|+h|R_0-c|-2c.
$$

It is positive for every $c>0$: on $[1,R_0]$ it is linear and has
positive endpoint values by the two displayed inequalities; below $1$
it decreases toward its positive value at $1$, and above $R_0$ it
increases. Move the leaves to distinct nearby positions. The positive
minimum persists, since there are finitely many selections and a
minimizer is among their elements. Apply the realization lemma below
and then replace each integer $x$ by $2x+1$. With a sufficiently fine
realization the resulting set is odd, still has ratio below $R$, and
has the same strict centered obstruction. Its difference levels are
the tree depths plus one. At level $j=1$, the recentered graded lemma
requires $F(c)<0$ for the entire star, which is impossible. This proves
the stated obstruction for every fixed ratio $R>1$.

A small explicit instance has $k=7$, $|O|=65$, and ratio below two.
For $0\le c\le64$ put

$$
x_c=2048+2c+1+1792\,\boldsymbol 1_{8\nmid c},\qquad
O=\{x_c:0\le c\le64\}.
\tag{O}
$$

All elements are odd. Because $1792$ is divisible by $256$,
$v_2(x_c-x_{c'})=1+v_2(c-c')$ for $c\ne c'$. Only $c=0,64$ have
seven difference levels; all other pivots have six. Every seven-level
star has three high elements, between $3843$ and $3967$, and five low
elements, between $2049$ and $2177$. For any such eight-element set,
the minimum of $\sum_x|x-c|-2c$ is the sum of its three largest
elements minus the sum of its five smallest. It is therefore at least
$3\cdot3843-5\cdot2177=644>0$. The entry point minimizes over every
pivot and center in exact arithmetic and finds the sharper minimum
$892$.

Nevertheless

$$
\{2049,3843,3845,3847,3851,3859,3875,3907\}
\tag{D}
$$

is dissociated. The seven high elements have the form $3841+2c$ with
$c\in\{1,2,3,5,9,17,33\}$. This code set is affinely dissociated,
using pivot $1$ and differences $1,2,4,8,16,32$. In a relation on (D),
write $s$ for the sum of coefficients on the seven high elements and
$\varepsilon$ for the coefficient on $2049$. The remaining code term
has absolute value at most $2(1+2+3+5+9+17+33)=140$. If
$\varepsilon\ne0$, then $|3841s+2049\varepsilon|\ge1792$; if
$\varepsilon=0$ and $s\ne0$, it is at least $3841$. Thus both vanish,
and affine dissociation of the code set finishes the proof. The entry
point also checks the $256$ subset sums directly.

The original sharp positive target for (O) asks for only seven
elements, which its certificates can supply. The obstruction concerns
the additional element needed by the stronger odd-slice route. It
leaves open a floor-logarithmic certificate theorem at bounded ratio.

## The lattice form

The pivot can be replaced by a modulus, and companions can then come from
any scale.

**Lemma.** Let $g$ be a positive integer and $Z$ a finite set of positive
integers, and write each $z\in Z$ as $z=q_zg+\rho_z$ with an integer $q_z$.
Suppose that the nonzero $\rho_z$ have pairwise distinct 2-adic
valuations, that at most one $\rho_z$ is zero, and that
$\sum_{z\in Z}|\rho_z|<g$. Then $Z$ is dissociated.

*Proof.* A ternary relation $\sum_z\varepsilon_zz=0$ reads
$Qg+\sum_z\varepsilon_z\rho_z=0$ with $Q=\sum_z\varepsilon_zq_z\in\mathbb Z$.
If $Q\ne0$ then $|Qg|\ge g>\sum_z|\rho_z|$, which is impossible. If $Q=0$
then $\sum_z\varepsilon_z\rho_z=0$, so the coefficient of every nonzero
$\rho_z$ vanishes by the least-valuation argument, and the remaining
relation $\varepsilon_{z_0}z_0=0$ on the element with zero residue forces
$\varepsilon_{z_0}=0$. $\square$

The one-zero-residue condition can be replaced by the assumption that
the selected zero-residue elements form a dissociated set. The same
proof eliminates every nonzero residue and leaves a relation on that
set. Thus a known dissociated block of multiples of $g$ can replace a
single anchor, without changing the strict budget for the other
residues. This does not itself supply such a block or new cheap levels.

With $g=a\in Z$, $q_a=1$ and $q_z=1$ for every companion this is the
dominant pivot. With $g$ larger than $\sum Z$ and every $q_z=0$ it is the
choice of one element from each 2-adic valuation layer, as for the
representatives in the odd-slice reduction. In between, an element far
above or below $g$ costs only its distance to the nearest multiple of $g$.
On the spread set
$X=\{3,14,17,24,41,43,58,107,289\}$ of the next section, the modulus
$g=107$ with residues $3,14,24$ and $289-3\cdot107=-32$, of valuations
$0,1,3,5$ and total $73<107$, gives the dissociated set
$\{3,14,24,107,289\}$ of size five, whereas every graded pivot certificate
in $X$ has at most three elements.

**Graded form.** Let the modulus $g$ be odd and the residues centered,
$|\rho_z|\le g/2$, with the nonzero ones at pairwise distinct levels and
at most one zero. If for every level $j$ of a nonzero residue with
$2^j\le|Z|/2$ the residues at levels $\ge j$ have total below $2^jg$,
then $Z$ is dissociated. Indeed, in a relation $Qg+\sum_z\varepsilon_z\rho_z=0$
with some nonzero residue used, let $j_0$ be its least level; the residue
sum has valuation $j_0$, so $Q\ne0$, $v_2(Q)=j_0$ and $|Q|\ge2^{j_0}$,
while $|Q|g\le\sum_z|\rho_z|\le|Z|g/2$ gives $2^{j_0}\le|Z|/2$; the
hypothesis at $j_0$ then contradicts
$|Q|g=|\sum_{i\ge j_0}\varepsilon_i\rho_i|$.
If no nonzero residue is used, $Qg=0$ forces the remaining coefficient to
vanish. So with centered residues only the levels below
$\log_2(|Z|/2)$ need a budget; above them any residue of size at most
$g/2$ is free, although it still enters the totals of the lower levels.

A **certificate** for a finite set $X$ of integers is a pivot $a\in X$ and
companions in $X$ satisfying the graded pivot lemma; its size is the
number of companions. The certificate can always use, for each level, the
companion nearest to $a$, because the hypothesis only gets easier when a
cost decreases.

## What single-pivot certificates cannot prove

The [entry point](evidence/main.py) checks the following finite facts
exactly, enumerating every pivot, every set of levels and every choice of
companions.

**The stronger odd bound.** The old research's sufficient condition
$|O|\le2^{d(O)-1}$ for odd $O$
([[research/erdos_963/proof_sketch|the odd-slice reduction of the Problem 963 sketch]])
needs $d(O)\ge\log_2|O|+1$. For $O=\{1,3,5,7,13\}$ we have $d(O)=4$, with
witness $\{1,3,5,13\}$, which meets that requirement, but the largest
certificate has only $2$ companions, so certificates prove only
$d(O)\ge3$. The dependent set $\{13;7,1,5\}$, with $1+5+7=13$, has costs
$6,12,8$ at levels $1,2,3$, so its budget sum $26$ equals $2\cdot13$:
the strict inequality of the lemma cannot be relaxed.

**Sets spread over several scales.** For
$X=\{3,14,17,24,41,43,58,107,289\}$ the largest certificate again has only
$2$ companions, while $d(X)=7$, with witness
$\{3,14,24,43,58,107,289\}$. In a certificate a pivot pays more than
$a/2$ for each companion outside $(a/2,3a/2)$, so on a set spread over several
dyadic scales a single certificate sees essentially one scale. Here the
certificate $\{14;3,24\}$ followed by the doubling chain $43,107,289$
already gives six elements; adding single elements from other scales is
how [[theory/number_theory/L213_triple_log_dissociated_subset/_index|L213]]
proceeds.

**Odd progressions are not extremal.** The progressions
$O_k=\{1,3,\ldots,2^{k+1}-1\}$ have $d(O_k)=2,3,5,6,7$ for $k=1,\ldots,5$.
From $k=3$ on, $|O_k|=2^k=2^{d(O_k)-2}$, a factor two below the stronger
odd bound, and the symmetric set $\{0\}\cup O_k\cup(-O_k)$, of size
$2^{k+1}+1$, has dissociation number $k+2>\lfloor\log_2(2^{k+1}+1)\rfloor$.
These sets therefore do not show the asked bound to be sharp; the 13-point
example recorded on
[[problems/number_theory/E0963/_index|the Problem 963 page]] remains the
relevant small comparison.

## The tree model

A dominant-pivot certificate in a finite set $P$ of positive integers
depends only on the binary residue tree of $P$, in which two elements part
at the level $v_2(x-y)$, and on the positions of the elements on the line.
For $a\in P$ let $\sigma_1(a),\ldots,\sigma_{m(a)}(a)$ be the sets of
elements of the subtrees that branch off the path from the root to $a$,
one for each level of $a$, and let $c_i(a)$ be the distance from $a$ to
the nearest element of $\sigma_i(a)$. Then $P$ has a dominant-pivot
certificate with $\mu$ companions exactly when some $a$ has $m(a)\ge\mu$
and its $\mu$ smallest costs $c_i(a)$ sum to less than $a$. Every tree,
with every placement of its leaves, occurs up to scaling and an
arbitrarily small error.

**Realization lemma.** Let $T$ be a full binary tree whose leaves
$\lambda$ carry distinct positive reals $\xi(\lambda)$. For every
$\varepsilon>0$ there are a scale $s>0$ and distinct positive integers
$x(\lambda)$ such that $v_2(x(\lambda)-x(\lambda'))$ is the depth in $T$ of
the lowest common ancestor of $\lambda$ and $\lambda'$, the root having
depth $0$, and $|x(\lambda)/s-\xi(\lambda)|<\varepsilon$ for every leaf.

*Proof.* Give each leaf the code $c(\lambda)=\sum_kb_k(\lambda)2^k$, where
$b_k(\lambda)\in\{0,1\}$ records which child the path to $\lambda$ enters
at depth $k$. Two leaves whose paths part at depth $k$ have codes that
agree below bit $k$ and differ in bit $k$, so their difference has
valuation $k$. Choose $H$ with $2^H$ above every code and an integer
$R\ge1$, and put
$x(\lambda)=c(\lambda)+2^H\lfloor R\xi(\lambda)+\tfrac12\rfloor$ and
$s=2^HR$. The second term has valuation at least $H$, so the
differences keep the valuations of the codes, the $x(\lambda)$ are
distinct, and $|x(\lambda)/s-\xi(\lambda)|\le3/(2R)$, which is below
$\varepsilon$ for large $R$. $\square$

Hence a configuration $(T,\xi)$ in which every pivot misses its budget by
a fixed margin yields an integer set in which every pivot misses it, and
questions about dominant-pivot certificates are questions about binary
trees with leaves on a line. For the graded lemma the valuation $v_2(a)$
of the pivot also enters. It is the level at which $a$ parts from $0$, so
graded certificates are read off the residue tree of $P\cup\{0\}$, with
$0$ placed at the origin, and the lemma realizes that tree as well. Give
every edge toward the leaf $0$ the bit zero; the formula then places that
leaf exactly at zero. Along
a path the level grows by at least one at each branching, so $j-v_2(a)$ is
at least the corresponding difference of depths. Realizations whose levels
equal the depths therefore have the smallest budgets $2^{j-v_2(a)}a$ and
the most window levels, and they are the hardest case for graded
certificates.

The three sets below were found by simulated annealing over trees and
placements and then realized by the lemma; the
[entry point](evidence/main.py) checks them directly in exact arithmetic.

**Dominant pivots on bounded-ratio sets.** The 32-element set $B$ of the
entry point has $\max B<2\min B$ and contains a dissociated subset of size
$6=\lfloor\log_232\rfloor+1$, as the asked bound requires, but its largest
dominant-pivot certificate has $4$ companions. Its fifteen largest elements
lie within $1.4\cdot10^4$ of each other near $2\cdot10^9$ and have only
four levels each, so none of them can carry five companions; each of the
other seventeen elements reaches four of its levels only through those
fifteen. So no count of cheap pivots, however sharp, lifts the proof of
L212 to $\lfloor\log_2n\rfloor$ companions on every set of ratio at most
two. The graded lemma is not limited in the same way: in $B$ the odd pivot
$1596136281$ has eight companions, at levels $1,\ldots,8$, within the
budget $2a$ that its valuation allows.

**The stronger odd bound at bounded ratio.** The 9-element set $O'$ of
odd integers in the entry point has $\max O'<2\min O'$ and $d(O')=8$, but
its largest graded certificate has $3$ companions. A certificate for the
stronger odd bound $|O'|\le2^{d(O')-1}$ would need $4$, since $9>2^3$.
Only the two smallest elements have four levels; they part from each other
at level $4$ and from the seven larger elements, which lie near
$2\min O'$, at levels $1,2,3$. A certificate with four companions
therefore costs about $3\min O'$, against the budget $2a$ of an odd pivot
at level $1$. The odd-slice reduction of the earlier sketch cannot be
completed by single-pivot certificates even for odd sets of ratio at most
two, although such sets are far from extremal for the bound itself.

**Cost against the diameter.** A translation-invariant strengthening of
the cost estimate of L212, that some pivot has $\lfloor\log_2|P|\rfloor$
companions at distinct levels of total cost at most $\max P-\min P$, is
false: in the 8-element set of the entry point every pivot with at least
three levels pays more than the diameter for its three cheapest levels.
An argument reaching $\lfloor\log_2n\rfloor$ companions must use budgets
above the diameter, such as the pivot itself.

## Exploratory observations

The following patterns were found by bounded random, hill-climbing and
annealing searches over sets of at most a few thousand elements, or over
trees with at most a few dozen leaves, computing only certificates. They
are discoveries from those searches, not predictions, and they support no
universal statement; the search code is not retained.

- On random sets in an interval $[A,2A]$, the dominant-pivot certificate
  found at least $\lfloor\log_2n\rfloor$ companions, two more than the
  proof of L212 guarantees; the set $B$ above shows that this fails in
  general.
- In the tree model of $P\cup\{0\}$ with levels equal to depths and $P$
  placed in $[D,2D]$, annealing with $|P|\le32$ found no configuration in
  which every graded certificate with $\lfloor\log_2|P|\rfloor$ companions
  exceeds its budget. At the hardest configuration found, some such
  certificate used at most about $0.71$ of its budget at every window
  level. If graded certificates reached $\lfloor\log_2n\rfloor$ companions
  on every set of ratio at most two, the asked bound $|P|\le2^{d(P)}-1$
  would follow for such sets, and with it the bound of Problem 963 for
  real sets whose nonzero absolute values lie within a factor two.
- For odd sets the same model has every level at least $1$ and the
  budget $2^ja$ at level $j$. There, certificates with
  $\lfloor\log_2|O|\rfloor$ companions were never close to failing: with
  $|O|\le16$, even the average over the pivots with enough levels of the
  best certificate's largest budget ratio stayed below about $0.45$.
  Certificates with $\lceil\log_2|O|\rceil$ companions fail, as the set
  $O'$ above shows. In the dominant-pivot model, by contrast, such
  averages exceed the budget, so an averaging proof is plausible only
  once the valuation enters.
- On sets of odd integers, including clustered, Bohr-type and
  difference-avoiding families, the graded certificate found at least
  $\lceil\log_2n\rceil-1$ companions, and the searches reached that value
  only on sets such as $O_k\cup\{x\}$.
- On sets spread over up to five dyadic scales, including runs of
  consecutive odd numbers at several scales, the best lattice
  certificate over the moduli tried (the elements, their quotients by
  small integers, and random integers) had at least
  $\lfloor\log_2n\rfloor+1$ elements, and every certified set was
  confirmed dissociated directly. On the 13-point set
  $\{1,\ldots,10,12,13,15\}$ of dissociation number $4$ the modulus $8$
  certifies $\{1,2,4,8\}$: residues $1,2,4$ of total $7<8$ and the
  multiple $8$, so $\lfloor\log_2 13\rfloor+1=4$ elements, with no room
  to spare.
