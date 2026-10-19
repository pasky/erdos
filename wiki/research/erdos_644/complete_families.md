---
name: research/erdos_644/complete_families
desc: A finite linear-program characterization of the asymptotic coefficient within complete uniform hypergraphs; not a solution for arbitrary families.
tags: [proved, lower-bounds]
sources: [fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2, erdos_1997_some_recent_problems_results_graph_theory]
created: 2026-09-22T20:23:03Z
updated: 2026-10-14T07:06:52Z
---


# research/erdos_644/complete_families

***

This page establishes the limit for the **complete-hypergraph subclass**. It
does not establish the limit asked for in Problem 644.

## A finite parameter

For fixed $r\ge3$, define

$$
\lambda_r=\min_{\mathcal F,w}\max_{i\in[r]}\sum_{F\ni i}w_F,
$$

where $\mathcal F\subseteq2^{[r]}\setminus\{\varnothing\}$ is pairwise
intersecting, $w_F\ge0$, and $\sum_Fw_F=1$. There are finitely many possible
supports, and each optimization is a rational linear program. Thus the minimum
is attained and rational. Also $0<\lambda_r<1$: the upper inequality follows by
taking all $(r-1)$-subsets with equal weights.

Let $g(k,r)$ be the largest transversal number among complete $k$-uniform
hypergraphs having the local two-point property. Then

$$
g(k,r)=\frac{\lambda_r}{1-\lambda_r}k+O_r(1).
\tag{1}
$$


### Lower bound

Suppose $A_1,\ldots,A_r$ are $k$-subsets of an $n$-point set and have no
two-point transversal. For each point $x$, set

$$
F_x=\{i:x\notin A_i\}.
$$

These traces are nonempty and pairwise intersecting, since
$F_x\cap F_y=\varnothing$ would say that $x,y$ cover every $A_i$. Give each
trace its multiplicity divided by $n$. Every coordinate has load $(n-k)/n$, so

$$
\frac{n-k}{n}\ge\lambda_r.
$$

Consequently the complete $k$-uniform family has the local property whenever
$n<k/(1-\lambda_r)$. Its transversal number is $n-k+1$, proving the lower bound
in (1).

### Matching upper bound within the complete subclass

Start with an optimal rational distribution on intersecting nonempty sets and
write its coordinate loads as $p_i\le\lambda_r$. Enlarge sampled sets by
inserting each missing coordinate $i$ with probability

$$
\frac{\lambda_r-p_i}{1-p_i}.
$$

These probabilities are rational. Enlargement preserves pairwise intersection,
and the new distribution has every coordinate load exactly $\lambda_r$. Clearing
denominators gives an integer $n_0$ and a bad family $A_1,\ldots,A_r$ of equal
size

$$
k_0=(1-\lambda_r)n_0
$$

on $n_0$ points.

Replace each point by $q$ identical copies to obtain a bad family of uniformity
$qk_0$ on $qn_0$ points. For arbitrary sufficiently large $k$, put
$q=\lfloor k/k_0\rfloor$, and add $k-qk_0$ private points to each edge. The
resulting family is still bad: a private point in a purported two-cover can be
replaced by any original point of its unique edge. Its ground-set size is

$$
qn_0+r(k-qk_0)=\frac{k}{1-\lambda_r}+O_r(1).
$$

Therefore the complete family on this many points fails the local property.
Repeated edges, if any, can be removed; a bad subfamily of fewer than $r$
distinct edges can be extended to $r$ edges inside a sufficiently large complete
family. This proves (1).

## The seven-edge value

For an intersecting support family on seven coordinates, if a support member has
size at most two then the sum of the loads on its coordinates is at least one.
Hence the maximum load is at least $1/2$. Otherwise every support member has
size at least three, and averaging gives maximum load at least $3/7$. Uniform
weights on the seven lines of the Fano plane attain $3/7$. Thus

$$
\lambda_7=3/7.
$$

In particular, the complete $k$-uniform hypergraph on

$$
n=\lceil7k/4\rceil-1
$$

points gives the all-uniformities bound

$$
f(k,7)\ge\lceil3k/4\rceil.
$$


There is also a direct proof. Since $n<7k/4$, seven $k$-sets have total degree
greater than $4n$, so some point belongs to at least five of them. Since $n<2k$,
the at most two remaining sets intersect. These two points cover the seven sets.

The supplied 1999 paper, Section 2, gives this complete construction for $k$
divisible by four and explains the Fano obstruction at $n=7k/4$. Its parity
construction improves the transversal number by one on a subsequence; this does
not change (1).

## Equivalent fractional formulations

Section 4 of
[the independent record](independent/fractional_reductions_and_good_triples.md)
uses

$$
M_r=\max\{\nu^*(\mathcal F):
\mathcal F\subseteq2^{[r]}\setminus\{\varnothing\}
\text{ is intersecting}\}.
$$

This is exactly $1/\lambda_r$, not a different threshold. For a fixed support,
dividing a probability distribution by its maximum coordinate load gives a
feasible fractional matching. Conversely, normalizing a fractional matching of
total weight $M$ gives maximum coordinate load at most $1/M$. Optimizing both
statements proves the identity. Thus (1) strengthens the independent coefficient
statement to

$$
g(k,r)=\frac{k}{M_r-1}+O_r(1).
$$


The same parameter gives the sharp sufficient fractional condition

$$
\tau^*(\mathcal H)<\rho_r:=\frac1{1-\lambda_r}
=\frac{M_r}{M_r-1}
\quad\Longrightarrow\quad P_r
\tag{F}
$$

for any finite family of nonempty edges, without a uniformity assumption. This
is the weighted obstruction already proved in
[Convex-profile amplification](convex_profile_amplification.md#the-complete-family-threshold-as-a-weighted-obstruction).
Indeed, a bad list of $r$ rows, repeating rows if necessary, maps normalized
fractional-cover weights of total $z$ to intersecting complement spectra with
coordinate loads at most $1-1/z$. Hence $\lambda_r\le1-1/z$, or $z\ge\rho_r$.

The strict threshold is attained by a bad uniform family. Clear denominators in
the balanced rational distribution constructed above, obtaining $N$ points and
rows of size $K=N(1-\lambda_r)>0$. Constant point weights $1/K$ give fractional
transversal number at most $\rho_r$, while the preceding obstruction gives the
reverse inequality. Repeated rows may be discarded without changing either the
fractional constraints or the failure of a two-cover. For $r=7$, the seven Fano
caps give $\rho_7=7/4$, checking the independent record's §3.2 including
strictness. This sufficient condition is not a characterization of $P_r$; parity
families already have $P_7$ with fractional transversal number greater than
$7/4$.

### The independent row-normalized linear programs

Section 4 of
[third independent record](independent/complete_family_limit_and_seven_edge_obstruction.md)
uses $g_r(k)$ for the **minimum union size of a bad tuple**, not the maximum
complete-family transversal number $g(k,r)$ used here. Using the at-most-$r$
convention, exactly,

$$
g_r(k)=g(k,r)+k.
$$

Its LP constant is therefore

$$
d_r=\rho_r=\frac1{1-\lambda_r},\qquad d_7=\frac74,
$$

and its $g_r(k)=d_rk+O_r(1)$ is the same restricted limit theorem.

The proposed direct rounding proof is valid. For an admissible support
$\mathcal Q\subseteq2^{[m]}\setminus\{\varnothing\}$, $m\le r$, with
$S\cup T\ne[m]$ for every $S,T\in\mathcal Q$, round an optimal solution
of $\sum_{S\ni i}w_S=1$ down to $\lfloor kw_S\rfloor$ points of each
spectrum. Each row needs only $O_r(1)$ private points to reach size $k$.
No support can be $[m]\setminus\{i\}$, because the row equation for $i$
supplies another positive-weight support containing $i$. Thus adding
singleton spectra cannot create a two-cover. Removing repeated rows does
not change the transversal number. Conversely, dividing the multiplicities
of any bad tuple by $k$ gives a feasible LP solution.

This verifies the alternative formulation, not a reduction of arbitrary
families to complete families. A finite list of local spectrum supports
still does not yield an unrestricted amplification or convergence theorem.

## An upper bound in terms of the ground-set size

The same bad tuple gives a useful separate statement. Use the at-most-$r$
version of the local property here (equivalent to the stated version for
families with at least (r) edges). Every such family on $n$ points has

$$
\tau(\mathcal H)\le\lambda_r n+O_r(1),
$$

regardless of its uniformity. Indeed, set $q=\lfloor n/n_0\rfloor$, replace
every point of the threshold tuple constructed above by $q$ copies, and leave
the other points unused. The resulting bad $r$-tuple consists of $qk_0$-subsets
$R_i\subseteq[n]$. If $\tau(\mathcal H)>n-qk_0$, every $R_i$ contains an edge of
$\mathcal H$, yielding a bad subfamily. Thus
$\tau\le n-qk_0=\lambda_r n+O_r(1)$. Small values with $q=0$ are absorbed in the
constant.

For $r=7$, the rounding can be sharpened as follows. Write $n=7q+s$,
$0\le s\le6$. Then

$$
\tau(\mathcal H)\le3q+w(s),\qquad
(w(0),\ldots,w(6))=(0,1,2,2,2,3,3).
\tag{2}
$$

This refinement, proposed in §5 of
[first independent record](independent/fano_ground_set_and_coding_constructions.md),
has the following direct proof. Partition the ground set into seven classes, $s$
of size $q+1$ and the rest of size $q$, indexed by Fano points. For $s=3$ place
the larger classes on a noncollinear triple; for $s=4$ place them on a cap. For
the other values any placement works. Every line then contains at most $w(s)$
larger classes.

The seven unions $U_L$ of classes on a line have size at most $3q+w(s)$ and
collectively contain every pair of ground points, including pairs within one
class. If the transversal number exceeded this bound, an edge could be chosen
disjoint from each $U_L$. No pair would cover these at-most-seven edges, a
contradiction. A singleton cover is excluded as well, since each point lies in
some $U_L$. For the exactly-seven convention without a lower bound on the number
of edges, replace the right side of (2) by its maximum with six.

In particular, the conjectured $3k/4+o(k)$ upper bound holds when the entire
ground set has size at most $7k/4+o(k)$. No reduction to that size has been
proved for arbitrary families.

## Exact-rounding caution for the supplied survey

The 1997 survey, §16 (p. 85;
[library card](../../../library/ramsey_theory/erdos_1997_some_recent_problems_results_graph_theory/_index.md)),
prints $f(k,4)=[3k/2]$ and $f(k,5)=[5k/4]$ with square brackets, which the
card reads as ceilings and erdosproblems.com as the floors $\lfloor3k/2\rfloor$
and $\lfloor5k/4\rfloor$, as repeated in the independent inputs, including §2.3
of
[second independent record](independent/fractional_reductions_and_good_triples.md).
Both floor readings are inconsistent with elementary complete-family examples.
Calling them reported background does not validate the exact formulas. This is
distinct from the vacuous-small-family convention.

For $r=4$, the complete $k$-uniform family on $\lceil5k/2\rceil-1$ points has
$P_4$ and transversal number $\lceil3k/2\rceil$. To prove the local property, a
bad four-tuple would have point degrees at most two. Its edge-intersection graph
has matching number at most one, since two intersecting pairs of rows would give
a two-cover. Such a graph is contained in a star or a triangle. The star case
requires three disjoint $k$-sets. The triangle case requires one $k$-set
disjoint from three rows whose union has size at least $\lceil3k/2\rceil$, by
the degree bound. Both cases require at least $\lceil5k/2\rceil$ points. In
particular, all triples on seven points have $P_4$ and transversal number five,
not the quoted floor value four.

For $r=5$, take all triples on six points. This twenty-edge family has
transversal number four. If five edges lacked a two-cover, their five
complementary triples would cover all $15$ pairs. They supply exactly
$5\binom32=15$ pair occurrences, so every pair would occur exactly once. At a
fixed vertex the five incident pairs would then give $2d(v)=5$, where $d(v)$
counts complementary triples through that vertex, an impossibility. Hence the
family has $P_5$, although $\lfloor5\cdot3/4\rfloor=3$.

These checks do not establish corrected exact formulas for general $k$. No
argument here uses the disputed rounding, and the reported asymptotic
coefficients are not challenged by these bounded discrepancies.

## What is not established

Nothing here bounds arbitrary families by the complete-family coefficient. In
particular, rationality of $\lambda_r$ does not prove existence or rationality
of the coefficient asked for in the problem. The missing general upper bound
would be much stronger than (1).
