---
name: research/erdos_1145/monotone_path_shells
desc: Flexible path shells give balanced cofinite complements and uniform bounds for every block pair, but only a logarithmic bound for the full unions.
tags: [proved, construction, unresolved]
sources: []
created: 2026-09-23T02:57:47Z
updated: 2026-10-16T06:44:50Z
---


# research/erdos_1145/monotone_path_shells

***

This construction retains exponentially many choices at each scale while
proving balance and coverage. It does **not** give a uniform representation
bound. The exact remaining condition concerns simultaneous interactions
with all earlier blocks, rather than any one pair of blocks.

## A flexible finite cover

For an integer $q\ge7$, choose $h_q(0)=0$ with increments in
$\{1,2\}$ through index $4q$. Put $D=\{0,1,2,3\}$ and
$$
 A_q=\{q^2+qx+h_q(x):0\le x\le4q\}+D,
 \quad
 B_q=\{q^2+qy-h_q(y):0\le y\le4q\}+D.
\tag{1}
$$
Both cardinalities are $4(4q+1)$. Their corresponding ranks differ
by at most $16q$, and
$$
 r_{A_q,B_q}\le272,
 \qquad [3q^2-q,9q^2+q]\cap\mathbb Z\subseteq A_q+B_q.
\tag{2}
$$

Indeed, consecutive bare points have gaps at least $q-2>3$, so the
four-point clusters are disjoint and their ordering agrees on both sides.
The rank discrepancy is $2h_q(x)\le16q$. A bare sum is
$2q^2+qs+h_q(x)-h_q(s-x)$. Its correction lies in $[-8q,8q]$,
so a fixed target permits at most seventeen integer values of $s$.
For each $s$, the correction increases strictly with $x$, in
steps between two and four. Hence there is at most one representation
for that $s$; the sixteen shift pairs give the bound in (2).

For $q\le s\le7q$, the admissible $x$-interval has length at
least $q$. The correction has symmetric endpoints $-\Delta_s$
and $\Delta_s$, with $\Delta_s\ge q$. Adding
$D+D=[0,6]$ fills every gap between its successive values. Thus
the entire interval $[2q^2+qs-q,2q^2+qs+q]$ is covered. These
intervals overlap for consecutive $s$, proving (2).

## A schedule with controlled pairwise interactions

Use the increasing sequence
$$
 \mathcal Q=\{2^k,3\cdot2^{k-1}:k\ge4\}.
$$
Its successive ratios are $3/2$ and $4/3$, and for $p<Q$
in this sequence, $p/\gcd(p,Q)\le3$.

For **arbitrary** increment words in (1), every mixed block pair has
an absolute representation bound. To prove this for a fixed shift pair
in $A_Q+B_p$, compare two representations. Their large-block indices
differ by at most $4p^2/Q$, since a small bare block has span at
most $4p^2$. Consequently the correction
$h_Q(x)-h_p(y)$ ranges over an interval of length at most $16p$.
The base quantity $Qx+py$ is a multiple of
$g=\gcd(p,Q)$, so at most $16p/g+1\le49$ such base values
are possible. Along each line $Qx+py=\text{constant}$, the correction
is strictly monotone. There is at most one solution on each line.

For $A_p+B_Q$, the same comparison uses large-block gaps at least
$Q-2$. The large index range is at most
$(4p^2+8p)/(Q-2)\le8p^2/Q$, giving correction range at most
$24p$. Thus at most $24p/g+1\le73$ base values occur, again
with one solution on each line. Restoring the sixteen shift pairs gives
a uniform bound of $1168$ for both orientations.

## Balance of the full unions

To control deduplication within a component, further require each
increment word to contain neither $111$ nor $22$. Every window
of length $t$ then satisfies
$$
 \tfrac43t-1\le h_q(i+t)-h_q(i)\le\tfrac32t+\tfrac12.
\tag{3}
$$
There are still exponentially many choices: arbitrary concatenations
of the two length-five words $12112$ and $11212$, followed by
an alternating final segment if necessary, are admissible.

That particular entropy source is
excluded: it fixes
$h_q(5t)=7t$, and the resulting progression cores already force
representation peaks of every fixed height on a set of positive lower
density. Sparse deletions and uniformly bounded perturbations do not
remove that obstruction. The broader no-$111$, no-$22$ family
is not excluded by that proof.

An equal-index obstruction rules
out taking the paths from one common infinite initial word, however
nonperiodic, and more generally from finitely many uniformly approximated
prefix germs. This argument is independent of the progression anchors
above. Opposite scale-dependent translations can remove that exact
resonance, but no full packing bound is known for them either.
The arbitrary-offset affine obstruction
excludes $h_q(t)=t$ even with arbitrary opposite translations
$o(q^2)$; genuinely nonlinear translated paths are not covered.

Put $A=\bigcup_{q\in\mathcal Q}A_q$ and
$B=\bigcup_{q\in\mathcal Q}B_q$. Same-side intersections of
distinct blocks have bounded cardinality. Here are the details needed
to justify that claim. All blocks lie in $[q^2,6q^2]$, so only
$Q/p\le\sqrt6$ need be considered. Fixing the two cluster shifts,
an equality between $A_Q$ and $A_p$ has base quantity
$Qx-py$ in an interval of length $8(Q+p)+6$. This interval
contains only an absolute number of multiples of $g$, since
$p/g\le3$ and $Q/p\le\sqrt6$.

On one base line, the solutions have steps
$(x,y)\mapsto(x+p/g,y+Q/g)$. For two line parameters separated
by $u\ge1$, (3) gives
$$
 \Delta\bigl(h_Q(x)-h_p(y)\bigr)
 \le-\frac5{18}\frac pg\,u+\frac32,
$$
using $Q/p\ge4/3$. In particular, a fixed correction can occur
at at most six line parameters. The corresponding argument for the
two $B$-blocks reverses the sign. Summing over the finitely many
base lines and cluster shifts proves the claimed intersection bound.

Each block overlaps numerically with only an absolute number of other
blocks. Hence replacing the sum of block counting functions by the
union counting function costs only $O(\log x)$. For one block,
the rank discrepancy bound $16q$, together with bare gaps at least
$q-2$, gives $A_q(x)-B_q(x)=O(1)$ uniformly in the cutoff.
Consequently
$$
 A(x)-B(x)=O(\log x),\qquad A(x),B(x)=\Theta(\sqrt x).
\tag{4}
$$
The upper growth bound follows by summing $O(q)$ over the geometric
scales. For the lower bound one complete block of scale comparable
to $\sqrt x$ suffices.

Both unions have gaps $O(\sqrt x)$ near $x$. Choose the largest
$q\in\mathcal Q$ with $q^2\le x$. Then
$x<(3q/2)^2$, whereas each bare block extends beyond
$5q^2-8q\ge(9/2)q^2$. Its consecutive gaps are at most $q+2$.
Combining this gap bound with (4) yields matched-rank displacement
$O(\sqrt x\log x)=o(x)$, and hence $a_n/b_n\to1$.

## Coverage and the unresolved uniform bound

The bands in (2) overlap on this scale schedule, proving that $A+B$
is cofinite. A representation of $n$ whose maximal block scale is
$Q$ has $Q^2\le n\le12Q^2$. There are only an absolute
number of such maximal scales. Summing the fixed block-pair bounds
over the $O(\log n)$ smaller scales proves only
$$
 1\le r_{A,B}(n)=O(\log n)\quad(n\text{ sufficiently large}).
$$
This estimate is **not** uniform and does not answer Problem 1145.

The [exact-resonance construction](prefix_resonance.md), proved as
[[theory/additive_bases/L126_path_shell_resonance/_index|L126 at tier 0]],
shows that this logarithmic order is attained by an admissible infinite
family. For any prescribed path at a dyadic $Q$, admissible smaller paths
can give $\gg\log Q$ distinct representations of
$3Q^2+h_Q(2Q)$, with exact carries. This disproves a uniform bound derived
solely from the local path restrictions. It does not exclude a globally
coordinated choice satisfying (5).

Locally sparse paired pruning preserves coverage
after enlarging the clusters, but no bounded-capacity choice of such
masks has been proved. Independent constrained paths, including
independent uniform central bridges, have unbounded representations
even after arbitrary $o(\sqrt x)$ deletions. Consequently any
successful alteration in that setting must delete a nonvanishing
proportion or use a globally coupled choice of paths.

Let $P^A_{<Q}=\bigcup_{q<Q}A_q$, and similarly for $B$.
The exact additional condition that would complete this construction is
$$
 \sup_{Q,n}\left(
 r_{A_Q,P^B_{<Q}}(n)+r_{P^A_{<Q},B_Q}(n)\right)<\infty.
\tag{5}
$$
The same maximal-scale argument shows why (5), together with (2),
would suffice. Earlier blocks with $6q^2\le Q$ collectively cost
at most eight representations in either orientation: all their points
lie in $[0,Q]$, and an interval of length $Q$ meets at most two
four-point clusters of the large block. The unresolved range is
$\sqrt{Q/6}<q<Q$, containing an unbounded number of scales.

An exact carry formulation may help retain the issue. For dyadic
$Q=2^k$, $q=2^j$, $j\ge k/2$, set $m=Q/q$.
In $A_Q+B_q$, write $y=mt+s$, $0\le s<m$, and
$n-Q^2-q^2=QV+R$, $0\le R<Q$. Then a representation is
equivalent to
$$
 x=V-t-c,\qquad
 R=qs+h_Q(V-t-c)-h_q(mt+s)+d+e-cQ,
\tag{6}
$$
with the original index ranges, $d,e\in D$, and an absolutely
bounded integer $c$. What is missing is a choice of the paths
that makes these tests, over all smaller scales, overlap only a bounded
number of times. No such coding, existence theorem, or invariant has
been established. Separate pairwise bounds and random-looking tests do
not prove (5).

## Limitation of an exact-grid scale-gap proposal

One proposed way to separate smaller scales was to force every
correction branch onto an exact arithmetic grid, with stride
$3m/2$ for scale ratio $m$. For fixed $V,s,c$ in (6), put
$G_t=h_Q(V-t-c)-h_q(mt+s)$. Requiring
$G_t-G_{t+1}=3m/2$ forces
$$
 \frac{3m}{2}-\bigl(h_q(m(t+1)+s)-h_q(mt+s)\bigr)
 =h_Q(V-t-c)-h_Q(V-t-c-1)\in\{1,2\}.
$$
Imposing these deficits on all aligned blocks at all relevant dyadic
scales is inconsistent.

Precisely, let $m$ be even. If four consecutive aligned blocks
satisfy
$$
 \frac{3m}{2}-\bigl(h(i+(j+1)m)-h(i+jm)\bigr)
 \in\{1,2\}\qquad(0\le j<4),
$$
their sum gives
$$
 6m-\bigl(h(i+4m)-h(i)\bigr)\ge4.
$$
The union therefore cannot also have its deficit in $\{1,2\}$.
This rules out only imposing those exact-grid deficits simultaneously
at all scales, not general nonlinear paths or branch-dependent routing.
The scale-gap tag formulation
retains a possible bounded-overlap objective, but has no proved integer
realization.
