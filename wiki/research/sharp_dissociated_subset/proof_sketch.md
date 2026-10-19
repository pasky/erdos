---
name: research/sharp_dissociated_subset/proof_sketch
title: Toward the floor(log_2 n) dissociated-subset bound
desc: Multiscale averaging proves the sharp bound when nonzero absolute values lie within a factor 4/3, a constant loss at ratio two, and a triple-logarithmic loss in general. The remaining gaps are combining scales and removing the bounded-ratio constant.
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T18:14:21Z
---

# Toward the floor(log_2 n) dissociated-subset bound

***

## Target

For a finite set $X\subset\mathbb R$ let $d(X)$ be the largest size of a
dissociated subset, one whose distinct subsets have distinct sums.
[[problems/number_theory/E0963/_index|Problem 963, whose page records it as open]],
asks whether every nonempty $n$-element real set $A$ has
$d(A)\ge\lfloor\log_2n\rfloor$,
that is, $|A|<2^{d(A)+1}$. Passing to the set $P$ of absolute values of
the nonzero elements gives $d(P)=d(A)$ and $|A|\le2|P|+1$, and the
symmetric set $\{0\}\cup P\cup(-P)$ shows that the target is equivalent to

$$
|P|\le2^{d(P)}-1\qquad\text{for every finite set }P\text{ of positive reals}.
$$

An integer model preserving every ternary relation, positivity, order and
every rational linear relation reduces both forms to positive integers
(section "Proved reductions" of
[[research/erdos_963/proof_sketch|the earlier Problem 963 sketch]], and
Step 1 of
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_proof|the proof of L212]]).
Translating the ambient set is not allowed: it changes relations whose
coefficient sum is nonzero.

## What is established

| Link | Statement | Standing |
| --- | --- | --- |
| L22 | $d(A)\ge\log_2n-\log_2(\log_2n+1)$ | tier 2 |
| graded pivot lemma | a pivot and companions at distinct 2-adic levels under a graded budget are dissociated | author-recorded |
| lattice form | elements $q_zg+\rho_z$ with 2-adically distinct residues of total below $g$ are dissociated | author-recorded |
| realization lemma | every binary tree with leaves at given reals is the residue tree of an integer set at nearly proportional positions | author-recorded |
| L212, ratio two | $\max P\le2\min P$ implies $\lvert P\rvert<3\,2^{d(P)}$ and $d(P)\ge\lfloor\log_2\lvert P\rvert\rfloor-1$ | tier 0 |
| L212, ratio $4/3$ | $\max P\le\tfrac43\min P$ implies $\lvert P\rvert\le2^{d(P)}-1$ | tier 0 |
| odd case of L212 | odd $O$ with $\max O\le2\min O$ has $\lvert O\rvert<3\,2^{d(O)-1}$ | author-recorded, proved in L212 |
| L213 | $d(A)\ge\log_2n-\log_2\log_2\log_2n-O(1)$, explicitly for $n\ge5$ | tier 0, uses L212 |
| L270 | at every fixed ratio $R>1$, a recentered graded certificate can fail to supply the stronger odd extraction | tier 0; certificate obstruction only |

The links are
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22, the binary residue-tree bound]],
[[research/sharp_dissociated_subset/pivot_certificates|the graded pivot lemma, its lattice form, its odd variant, the tree model and their limits]],
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_index|L212, the bounded-ratio bound]],
[[theory/number_theory/L213_triple_log_dissociated_subset/_index|L213, its block-by-block consequence for all real sets]],
and
[[theory/number_theory/L270_recentered_pivot_obstruction/_index|L270, the split-leaf obstruction to the stronger odd certificate]].
Composing author-recorded arguments confers no tier; these three claims are
complete arguments recorded by their author and have not been reviewed.

## The route

**Why a log is lost.** In the binary residue tree a pivot $a$ with
companions $b_j$ at distinct levels $j=v_2(b_j-a)$ admits no relation
whose coefficients sum to zero. A relation with coefficient sum $s\ne0$
must cancel $sa$, and 2-adically this is possible only at the level
$j_0=v_2(s)+v_2(a)$, which lies in a window of about $\log_2d$ levels
above $v_2(a)$. L22 deletes that window. Archimedean size is the other
handle: if the companions lie within total distance $a$ of the pivot, no
multiple $sa$ with $s\ne0$ can be cancelled. The graded pivot lemma
combines the two, requiring for each window level $j$ only that the
companions at levels $\ge j$ have total distance below $2^{j-v_2(a)}a$.

**The averaging step.** Write $A=\min P$, $L=\max P-\min P$, and
$k=d(P)$. If nonzero coefficient sums of relations have magnitude at
least $q$, a pivot's $k$ cheapest companions must cost at least $qa$.
The truncated cost $F(a)=\int_0^L(k-N_a(r))_+\,dr$ is also defined at
pivots with fewer than $k$ levels. The Kraft equality and an integer
deficiency inequality give
$\mathbb EF/L<1+2^k/|P|$. Accounting for deficient pivots gives the
opposite bound $\mathbb EF/L\ge b-(b-1)2^{k-1}/|P|$, where $b=qA/L>1$.
Thus $|P|<(b+1)2^{k-1}/(b-1)$. The always available choice $q=1$ proves
the sharp positive target at ratio $4/3$; $q=2$ gives the odd bound at
ratio two, and summing valuation layers gives $|P|<3\,2^{d(P)}$ there.
This uses the branching of the whole tree at every scale, including the
short paths.

**Arbitrary sets.** L213 applies L212 in every dyadic block of the
absolute values, extends one block's dissociated set by a doubling chain
from alternate occupied blocks far above it, and chooses the block by a
weighted pigeonhole. Its loss of order $\log_2\log_2\log_2n$ comes only
from the gap of about $\log_2\log_2n$ blocks that a doubling chain must
leave above a set of $\log_2n$ elements of comparable size.

## Gaps

**Gap 1: combining scales (constant loss for arbitrary sets).** Prove
$d(A)\ge\log_2|A|-O(1)$ for every finite real set. The case that the
argument of L213 handles worst is a set whose mass is spread over about
$\log_2\log_2n$ consecutive dyadic blocks with comparable counts: there a
block gives about $\log_2(n/\log_2\log_2n)$ elements and nothing yet adds
the missing $\log_2\log_2\log_2n$. Two obstructions are recorded.
A single pivot pays at least $a/2$ for a companion in another block, so
its certificate sees one scale
([[research/sharp_dissociated_subset/pivot_certificates|the spread example there has certificate size 2 and dissociation number 7]]).
A doubling chain above a set $D$ of $\mu$ elements near $a$ cannot start
below $\mu a$. The first obstruction is removed by the
[[research/sharp_dissociated_subset/pivot_certificates|lattice form of the pivot lemma]]:
an element $z$ may enter a certificate with modulus $a$ through its
residue $z-q_za$ for any integer $q_z$, so its cost is its distance to the
nearest multiple of $a$, not to $a$. On the spread example this certifies
five elements where single-pivot certificates reach three. Four ideas
are open:

- *Folding by virtual points.* The lattice lemma holds verbatim for a
  rational modulus $g$ with odd denominator, since only $|Qg|\ge g$ for
  integers $Q\ne0$ and 2-adic valuations of the residues are used. Take
  $g=z_0/q_0$ with $z_0\in P$ and $q_0$ odd, so that $z_0$ has residue
  $0$. An element $z$ entered with an odd multiplier $q$ has residue
  $z-qg=q(z/q-z_0/q_0)$: its level is the 2-adic distance between the
  *virtual points* $z/q$ and $z_0/q_0$, and its cost is $q$ times their
  real distance. A certificate is thus a pivot and companions at distinct
  2-adic distances in the set $V$ of virtual points, under a weighted
  archimedean budget, requiring a weighted extension of L212.
  Heuristically the
  scales then cancel: an element of the dyadic block $2^t$ times above
  the pivot's has about $2^{t-1}$ odd multipliers putting $z/q$ in the
  pivot's window, spaced about $2^{-t}$ of the window apart, while its
  cost weight is about $2^t$; so at every weighted threshold each element
  contributes about as many cheap virtual points as an element of the
  pivot's own block. The missing step is the averaging: a uniform pivot
  of $V$ is usually a virtual point of large weight, whose cheap
  companions lie in correspondingly smaller cells, and a pivot
  distribution weighted toward small multipliers loses the Kraft
  equality. The
  [[research/sharp_dissociated_subset/weighted_folding|weighted-folding note]]
  proves that repeated sources are automatically excluded under a strict
  total residue budget below the modulus. It also refutes a generic
  weighted Kraft packing inequality for arbitrary interval families.
  An averaging proof must use the special arithmetic families $z/q$,
  rather than the Kraft equality alone.
  A modulus whose own residue is nonzero instead reintroduces the pivot
  problem as the Diophantine condition that the distance from
  $s\rho_a/g$ to the nearest integer stay away from zero for
  $1\le|s|\le\mu$, which costs about $\log_2\mu$ levels again.
- *A sufficient condition.* Call it (LC): every finite set $P$ of positive
  integers has a modulus $g$ whose lattice certificate has at least
  $\lfloor\log_2|P|\rfloor+1$ elements. (LC) implies
  $d(P)\ge\log_2(|P|+1)$, the positive form of the target, so it is at
  least as strong as the bound asked by Problem 963 and could fail
  where that bound holds. The weaker form with $\log_2|P|-O(1)$ elements
  would settle Gap 1. The bounded searches recorded in
  [[research/sharp_dissociated_subset/pivot_certificates|the certificate note]]
  found no set violating (LC), and (LC) is exactly tight on the
  13-point set of the problem page; this is an exploratory pattern, not
  a premise.
- *Expensive high levels.* Companions from other blocks may sit at levels
  above the window, where the graded lemma imposes no condition of their
  own. They still enter the window sums. If $F$ new companions each cost
  at most the pivot, the cheap-star extension lemma loses at most
  $\lceil\log_2(F+1)\rceil$ levels. Otherwise the deletion must reflect
  their actual total cost, not just their number.
  The obligation is a pivot whose own block, of $n_k$ elements, supplies
  the window levels cheaply while other blocks supply about
  $\log_2(n/n_k)$ new levels.
- *Several pivots.* Dominant-pivot sets in two blocks interact only through
  $sa+s'a'\approx0$ and through their small balanced combinations; a joint
  certificate would have to control both.

**Gap 2: the last constant at ratio two.** L212 proves the target at
ratio $4/3$. At ratio two it gives $|P|<3\,2^{d(P)}$, while the target
needs $|P|\le2^{d(P)}-1$. Its constant comes from separately bounding
the contributions of deficient pivots and the cost at each scale. The
same proof gives $k+1$ dissociated elements in every positive integer
set of ratio at most two whose residue tree has minimum leaf depth
at least $k$. The proof treats the highest valuation layer by the odd
case and appends representatives from the lower layers. The general
tree has shallow leaves. A sharper count of cheap dominant
pivots cannot close the whole gap:
[[research/sharp_dissociated_subset/pivot_certificates|the certificate note]]
records a set of $32$ integers of ratio below $2$ with no dominant-pivot
certificate of $\lfloor\log_232\rfloor$ companions. It was found in a tree
model, also recorded there, in which certificate questions become
questions about binary trees with leaves on a line. The pivot's own
valuation can enter through the graded lemma, which certifies eight
companions in that set; free centers give another enlargement. Treating
the valuation layers one at a time would need the stronger odd bound
$|O|\le2^{d(O)-1}$, the sufficient condition of the earlier sketch's
odd-slice reduction, and certificates miss it on the
[[research/sharp_dissociated_subset/pivot_certificates|five-point example $\{1,3,5,7,13\}$]],
of dissociation number $4$ with at most two companions per certificate,
and on a nine-element odd set of ratio below $2$, of dissociation number
$8$ with at most three. Searches in the tree model found no set of ratio
at most $2$ with at most $32$ elements that defeats graded certificates
with $\lfloor\log_2n\rfloor$ companions; this is an exploratory pattern,
not a premise. Beyond certificates, relation information such as the full
2-adic expansion of $sa=-\sum_j\varepsilon_j\delta_j$ remains available.
Freely chosen centers give strictly stronger certificates, but the
certificate note's exact 32-point obstruction rules out the sufficient
claim that a free center always reduces a five-companion star's cost to
the diameter. More decisively,
[[theory/number_theory/L270_recentered_pivot_obstruction/_index|L270's split-leaf construction]] defeats the
stronger odd extraction by recentered graded certificates at every fixed
ratio $R>1$. Its explicit 65-element instance has no certificate with
seven companions, although an eight-element dissociated subset is
exhibited. Thus the stronger odd-slice route needs a method beyond one
star in the prescribed tree. The floor-logarithmic certificate statement
for a bounded-ratio set itself remains open.

## Corrected orientation and retired routes

- The odd progressions $O_k=\{1,3,\ldots,2^{k+1}-1\}$ are not extremal:
  $d(O_k)=k+2$ for $k=3,4,5$, checked exactly in
  [the evidence of this folder](evidence/main.py). They do not witness
  sharpness of $\lfloor\log_2n\rfloor$, and inequalities tuned to make
  them tight are not tuned to an extremal case.
- Arguments that cover a dyadic block by windows of ratio $1+2^r/d$ and
  run a residue tree in each window lose about $r$ levels per window and
  need about $d/2^r$ windows. This heuristic accounting gives about
  $d\,2^d$ elements per block for every $r$, the L22 loss. A route of this
  kind must couple the windows, as the multiscale averaging of L212 does.
- A graded certificate with the cheapest companions proves neither the
  stronger odd bound nor the target for sets spread over several scales;
  the two exact examples are in
  [[research/sharp_dissociated_subset/pivot_certificates|the certificate note]].
- Raising the dominant-pivot count of L212 to $\lfloor\log_2n\rfloor$
  companions on every set of ratio at most $2$, and bounding the cheapest
  cost by the diameter instead of the pivot, both fail on exact sets in
  [[research/sharp_dissociated_subset/pivot_certificates|the certificate note]].
  Reopening either needs information beyond the residue tree and the
  positions, such as the valuation of the pivot.
- Allowing a free center does not repair the diameter bound: the exact
  32-point example in the certificate note has minimum centered star
  cost $512668211$ and diameter $512000052$. Its minimizing star is
  nevertheless dissociated. This is a certificate obstruction, not an
  adverse example for the target.
- Recentered graded certificates cannot prove the stronger odd bound
  even at an arbitrarily small fixed aspect ratio above one. The
  split-leaf family of L270 forces too many low and
  high points into every sufficiently large star. Its 65-point integer
  example has an eight-element dissociated subset, so this is a limit
  of the certificate rather than a counterexample to the target.
- An unrestricted weighted-interval version of the Kraft estimate fails
  by an explicit construction with linear growth in the number of scales in the
  [[research/sharp_dissociated_subset/weighted_folding|weighted-folding note]].
  Folding remains open because its intervals have arithmetic constraints
  absent from that construction.

## Next moves

1. Attack Gap 1 through virtual points: find a pivot distribution on
   the virtual-point set $V$ under which the multiscale argument of L212
   survives the multiplier weights, so that some rational modulus has
   cheap residues at about $\log_2N$ distinct 2-adic levels. A positive
   outcome gives $d(A)\ge\log_2|A|-O(1)$, the constant-loss bound for
   all real sets, and a sharp enough one would bear on (LC). Adding
   single elements whose distance to $a\mathbb Z$ exceeds the cost of a
   dominant-pivot set is the special case of the lattice form with one
   residue per element. Shrinking that cost by a factor $K$ loses about
   $\log_2K$ levels, while unstructured residues then admit only about
   $\log_3K$ added elements, so this special case does not close the gap
   by itself.
2. Prove that graded or recentered certificates reach $\lfloor\log_2n\rfloor$
   companions on every set of ratio at most $2$. That would give the
   positive form $|P|\le2^{d(P)}-1$ for such sets, hence the target for
   real sets whose nonzero absolute values lie within a factor two. The
   count must go beyond dominant pivots, and treating valuation layers
   jointly avoids the stronger odd bound, which the split-leaf family
   prevents these certificates from proving. In the tree model of
   $P\cup\{0\}$ the valuation of a pivot is the depth at which it parts
   from the leaf $0$, and every smaller difference level is free; an
   averaging over pivots that credits those free levels is the natural
   first attempt. A first sub-target is the odd-layer statement: every
   finite set $O$ of odd positive integers with $\max O\le2\min O$ has a
   pivot with $\lfloor\log_2|O|\rfloor$ companions satisfying the graded
   lemma. It is unproved; the searches recorded in
   [[research/sharp_dissociated_subset/pivot_certificates|the certificate note]]
   support it with a wide margin. It would give $d(P)\ge\lfloor\log_2n\rfloor$
   for every set of ratio at most $2$, one level above L212. Let the
   nonempty valuation layers $\{x\in P:v_2(x)=t\}$ have sizes
   $\ell_1,\ldots,\ell_r$ from the bottom. A pivot in the $k$-th layer takes
   one free companion from each lower layer, at a level below its own
   valuation, together with its certificate inside its layer, scaled by a
   power of two. Each window level added by the larger count holds
   because every cost is at most the pivot. If every $k$ had
   $k-1+\lfloor\log_2\ell_k\rfloor\le\lfloor\log_2n\rfloor-2$, then
   $\ell_k\le2^{\lfloor\log_2n\rfloor-k}-1$ and the sizes would sum to
   less than $n$. The last unit toward the target must come from a
   companion in a higher layer, which enters at the pivot's own level
   under the budget $a$, or from a larger count inside one layer.
3. Use exact relation data: a relation $sa+\sum_j\varepsilon_j\delta_j=0$
   with $v_2(s)=j_0$ fixes $s$ modulo every power of two from the
   companions' digits. Counting the pairs $(s,\varepsilon)$ compatible
   2-adically before applying the archimedean bound could replace the
   crude budget $\sum_j|\delta_j|$.
4. The cheap-star extension lemma in the certificate note shows that
   $r$ new levels from points at most $2a$ lose only
   $\lceil\log_2(r+1)\rceil$ levels, independently of the original
   star's size. To use it across blocks, find a pivot that simultaneously
   has many cheap levels within its block and new levels below its
   scale. If all the other elements lie in one sibling subtree, they
   supply only one new level; points above the pivot's scale require
   their actual costs. No argument yet controls these two cases jointly.
