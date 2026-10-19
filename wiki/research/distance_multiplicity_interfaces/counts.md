---
name: research/distance_multiplicity_interfaces/counts
title: "Distance counts, multiplicities and pinned occupancy"
desc: "Exact counting identities separate raw energy, rare lengths, circle occupancy and pinned-distance quantifiers from the remaining geometric gaps."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/distance_problems/E0089/_index|E0089]],
[[problems/distance_problems/E0098/_index|E0098]],
[[problems/distance_problems/E0132/_index|E0132]],
[[problems/distance_problems/E0100/_index|E0100]],
[[problems/distance_problems/E0604/_index|E0604]],
[[problems/distance_problems/E0654/_index|E0654]],
[[problems/distance_problems/E0657/_index|E0657]],
[[problems/distance_problems/E0661/_index|E0661]].

## Distinct counts, multiplicities and pinned counts

## E0089: the energy route has a precise obstruction

For an arbitrary planar set,
$$
 M^2=\left(\sum_r m_r\right)^2\le D\sum_r m_r^2.
$$
Guth--Katz's ordered quadruples count each pair of unordered pairs in four
orientations, so its quantity $|Q|$ is exactly $4E$, where $E=\sum_r m_r^2$.
Their $E=O(n^3\log n)$ gives $D\gg n/\log n$. A uniform $E=O(n^3\sqrt{\log n})$
would give the desired $D\gg n/\sqrt{\log n}$, but the square-grid appendix
proves $E=\Omega(n^3\log n)$. Thus that particular sufficient energy estimate is
false. The conjecture itself is not contradicted: the Cauchy inequality can lose
information about uneven multiplicities.

Inspected: Guth--Katz's primary transcription, Theorem 1.1, Section 2 definition
and counting lemma, and the square-grid proof in Section 5; the appendix opening
was also checked against PDF page 32. The entire incidence proof was not
rechecked. The next question is whether a truncation or weighting can remove the
grid's excess energy while still recovering enough of $M$. Stop an approach that
requires the false uniform raw-energy improvement.

## E0098 and E0654: occupancy identifies the missing gain

If no four points are cocircular, a circle about any pin contains at most three
other points. Consequently every distance graph has degree at most three,
$m_r\le3n/2$, and
$$
 D\ge \left\lceil\frac{n-1}{3}\right\rceil.
$$
This alone gives no superlinear conclusion for E0098. A uniform $m_r=o(n)$ is
actually false under both general-position exclusions: take $n/2$ unit segments,
choosing their rotations and translations successively outside the finitely many
collinearity and cocircularity conditions. These conditions are proper algebraic
conditions; translations can be chosen in arbitrary distant open regions. All
prescribed segments remain unit segments. A unit class of at least $n/2$ pairs
survives. This is not a counterexample to E0098, since other distances can be
numerous. The inspected proof of Sheffer's Lemma 3.1 uses the no-three-collinear
condition to limit isosceles apices on perpendicular bisectors; it too produces
a linear-order estimate. A route must improve the average multiplicity, not just
invoke either elementary occupancy limit.

For E0654, collinear triples are permitted. Let $r_j(x)$ be the number of
circles about $x$ containing exactly $j$ other points, $j=1,2,3$. Then
$$
 n-1=r_1+2r_2+3r_3,\qquad d(x)=r_1+r_2+r_3,
 \qquad 3d(x)-(n-1)=2r_1+r_2.
$$
Thus $d(x)>(1/3+c)n$ is equivalent to $2r_1(x)+r_2(x)>3cn+1$. The next
discriminating statement is a linear deficit from full triple occupancy at one
pin. A result assuming no three collinear is not a specialization to E0654. The
pending two-line negative claim was read only through the problem account and
supplies no newly checked proof here.

## E0132: a counting interface for the existing owner

Let $R$ count lengths whose unordered multiplicity lies in $\{1,\ldots,n\}$.
Every other realized length has at least $n+1$ pairs, so
$$
 M\ge R+(D-R)(n+1),\qquad
 R\ge\left\lceil\frac{(n+1)D-M}{n}\right\rceil.
$$
In particular $D>n/2$ forces $R\ge2$. Even the full conjectural E0089 bound is
below this threshold for large $n$.

There is a useful scalar countermodel to an argument using only these totals and
the known order of energy. Put $D=\lfloor n/\log n\rfloor$, give one class
multiplicity one, and divide $M-1$ as equally as possible among the remaining
$D-1$ classes. For sufficiently large $n$, every one of those multiplicities
exceeds $n$, while $E=\Theta(n^3\log n)$ and $R=1$. This is only an integer
multiplicity profile, with no planar realization claimed. It proves that the
displayed scalar information is insufficient, not that the conjecture fails.

This scalar obstruction is relevant to [[research/erdos_132/_index|the existing
rare-distance arguments]]. It is not a planar construction, and supplies no new
sustained geometric route.

## E0100, E0604 and E0657: different missing hypotheses

In E0100 all lengths are at least one, but repetitions are allowed. If the $D$
distinct values are separated by at least one and sorted as $r_1<\cdots<r_D$,
then $r_j\ge j$, hence $\operatorname{diam}P\ge D$. Guth--Katz gives only $\gg
n/\log n$; even E0089 would leave $\sqrt{\log n}$. Equally spaced collinear
points have diameter $n-1$, so linear order is plausible. Treating all $M$ pairs
as different lengths would change the question to E0670. The next test must use
separation between values, not merely their number.

For E0604, the held accepted weak assertion quantifies over every fixed
$\varepsilon>0$. It gives no uniform threshold allowing $\varepsilon$ to shrink
with $n$. The scalar function
$$
 g(n)=n\exp(-\sqrt{\log n})
$$
eventually exceeds $n^{1-\varepsilon}$ for each fixed positive $\varepsilon$,
but $g(n)/(n/\sqrt{\log n})\to0$. Thus the weak quantified conclusion does not
imply the requested logarithmic bound, even if one assigns it to every pin. This
is a quantifier countermodel, not a point set. Including zero changes the pinned
count by only one. The weak result is used only at the standing and quantified
scope recorded on the problem page.

E0657 forbids an isosceles triple, including an equally spaced collinear triple.
Each distance class is therefore a matching, so
$$
 D\ge\frac{\binom n2}{\lfloor n/2\rfloor}
 =\begin{cases}n-1&n\text{ even},\\n&n\text{ odd}.\end{cases}
$$
For even $n$, an abstract edge coloring of $K_n$ attains $n-1$: on vertices
$\mathbb Z_{n-1}\cup\{\infty\}$, the factor indexed by $a$ consists of
$\{\infty,a\}$ and $\{a+j,a-j\}$, $1\le j\le(n-2)/2$. These are perfect
matchings partitioning the edges. They are not asserted to be planar distance
classes. The geometric realization constraint must do further work. The
inspected Fox--Pach--Suk Theorem 1 instead assumes $p\ge6$ and at least $\binom
p2-p+6$ lengths in every $p$-set. Its hypothesis is not established by the
matching count above: applying the theorem requires a separate proof of its
$p$-point hypothesis. Arithmetic-box or progression-free arguments require extra
coordinate hypotheses as well.

## E0661: the balanced bipartite gap survives

Here $|P|=|Q|=n$, and the incidence total is $n^2$ on $P\times Q$. Mathialagan's
Theorem 3 specializes to $D(P,Q)\gg n/\log n$; Theorem 4's logarithm-free regime
$m\le n^{1/3}$ does not include the balanced case. A partition of a $2n$-point
lattice example gives only $O(n/\sqrt{\log n})$, whereas the question asks for
little-o. These upper and lower bounds leave room in the requested direction. If
the sets overlap, zero contributes at most one distinct value. Nothing about
that convention closes the gap. Only the primary statements and their hypotheses
were inspected, not the full incidence proof. A candidate construction must beat
the lattice constant asymptotically, rather than merely reproduce its order.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/distance_problems/fox_2016_more_distinct_distances_local_conditions/_index|fox
  2016 more distinct distances local conditions]]: Section 1, D(n,3,3)
  discussion and Theorem 1 (statement reading).
- [[../library/distance_problems/guth_2015_erdos_distinct_distance_problem_plane/_index|On
  the Erdős distinct distance problem in the plane]]: Section 2 Lemma 2.1
  counting proof; Section 5 square-grid proof, Lemma 5.1 and Proposition 5.2
  (proof reading). Section 2 definition (2.1) and Proposition 2.2 statement
  (statement reading). Theorem 1.1; Section 2 distance convention (statement
  reading).
- [[../library/distance_problems/mathialagan_2021_bipartite_distinct_distances_plane/_index|mathialagan
  2021 bipartite distinct distances plane]]: Section 1 definitions; Theorems 3
  and 4; Table 1; Question 5 (statement reading).
- [[../library/distance_problems/sheffer_2014_distinct_distances_open_problems_current_bounds/_index|sheffer
  2014 distinct distances open problems current bounds]]: Section 3, Lemma 3.1
  proof (proof reading). Section 3, Problem 8 discussion (account reading).
