---
name: research/erdos_132/weighted_circle_energy
title: Weighted chord energy and a seven-eighths circle threshold
desc: |
  Weighting chord coincidences improves the circular concentration threshold
  to q to the seven-eighths power and the inactivity tradeoff to n to the one-twenty-fourth.
sources: []
research_state: closed
created: 2026-09-23T06:20:00Z
updated: 2026-09-24T22:12:56Z
---


# Weighted chord energy and a seven-eighths circle threshold

***

Write $n=|A|$, $q=q(A)$, and $Q=q+1$. All distance multiplicities are unordered.
The following strengthens [quantitative_circle](quantitative_circle.md):

**Theorem.** There is an absolute $C$ such that a circle containing


$$
m\ge C Q^{7/8}
$$


points of $A$ forces $R(A)\ge m/4$.

This is not an unrestricted rarity theorem: a bounded-rarity sequence
has not been shown to have a circle meeting this threshold.

## Weighted energy between concentric circles

Suppose $A\setminus\{o\}$ lies on $k$ circles centered at $o$,
with distinct positive radii $R_i$ and angular sets $B_i$ of sizes


$$
n_i=|B_i|,\qquad \sum_i n_i\le n.
$$


Let the first circle be an anchor, $B=B_1$, $m=|B|$, $R=R_1$.
For each positive distance $r$, let $a_r$ count its unordered pairs
on the anchor and let $e_r=m_A(r)-a_r$.

For $(i,j)\ne(1,1)$, equal squared distances between an ordered anchor
pair $(x,y)\in B^2$ and an ordered pair $(u,v)\in B_i\times B_j$
satisfy


$$
\cos(v-u)=\frac{R^2}{R_iR_j}\cos(y-x)
 +\frac{R_i^2+R_j^2-2R^2}{2R_iR_j}.
$$


The parameters are not the degenerate pair $(1,0)$: equality would
force both $R_iR_j=R^2$ and $R_i^2+R_j^2=2R^2$, hence $i=j=1$.
Apply the uniform translated-cosine incidence lemma in
[circle_incidence](circle_incidence.md), with point set $B\times B_i$
and curves indexed by $B\times B_j$. Its coincidence multiplicity
is at most two, including the antipodal case. The number $E_{ij}$
of these ordered coincidences is at most


$$
E_{ij}\ll m^{4/3}(n_i n_j)^{2/3}+m(n_i+n_j).
\tag{1}
$$


Allowing zero-length pairs in this upper bound is harmless. Every
positive unordered coincidence not involving $o$ is counted four
times when ordered anchor pairs and all ordered radius-pair types are
used. Pairs involving $o$ contribute at most $mn$, since $a_r\le m$.
Hölder gives $\sum_i n_i^{2/3}\le k^{1/3}n^{2/3}$, so


$$
E:=\sum_{r>0}a_r e_r
\ll m^{4/3}k^{2/3}n^{4/3}+mkn+mn.
\tag{2}
$$


Every rich $r$ has $e_r\ge n+1-m$. At most $R(A)$ anchor
lengths are rare, and each has $a_r\le m$. Therefore


$$
E\ge(n+1-m)\left(\binom m2-mR(A)\right).
\tag{3}
$$


If $m\le n/2$, division of (2)--(3) yields


$$
R(A)\ge\frac{m-1}{2}
-C_0\left(m^{1/3}k^{2/3}n^{1/3}+k+1\right).
\tag{4}
$$


Unlike the earlier proof, this does not discard an anchor length after
one outside occurrence. Its anchor multiplicity weights the cost of
making that length rich. No Plünnecke or angular covering step is used
in (1)--(4).

## Obtaining the radius bound

Replace the given anchor by a largest circle, of size $m$; this can
only strengthen the desired conclusion. Put $H=2Q/m$. The pinned
spectra in [circle_incidence](circle_incidence.md) each have size at
least $m/2$. For points at different positive radii about the anchor
center, the intersection of two such spectra has size at most


$$
C_1(H^{4/3}m^{2/3}+H^2).
$$


Indeed $|B-B|/m\le H$, and this is precisely that note's
small-difference-set cosine-overlap lemma. If $L=\lceil2H\rceil$
distinct radii occurred, the elementary union lower bound would give


$$
Q\ge Lm/2-O(H^{10/3}m^{2/3}+H^4)>Q
$$


when $m\ge C_2H^7$, for a sufficiently large absolute constant.
Consequently $k\ll H\ll Q/m$. The size condition is equivalent,
up to the constant, to $m\ge C_3Q^{7/8}$.

Maximality of the anchor now gives $n_i\le m$, and thus


$$
n\le km+1\ll Q.
$$


If $m\le n/2$, (4) becomes


$$
R(A)\ge\frac{m-1}{2}
-C_4\left(\frac{Q}{m^{1/3}}+\frac Qm+1\right).
\tag{5}
$$


For $m\ge C Q^{7/8}$, the error is at most $m/4-1/2$, after
increasing the absolute constant and absorbing small orders. If
$m>n/2$, the existing positive-fraction circle theorem with fraction
$1/2$ gives $R(A)\ge(m-1)/2-O(n^{2/3})\ge m/4$ for large orders;
small orders are again excluded by increasing $C$. This proves the theorem.

## Consequences

For each fixed $K$, an unbounded sequence with $R(A)\le K$ has


$$
\max_{\gamma\text{ circle}}|A\cap\gamma|=O_K(n^{7/8}).
\tag{6}
$$


The diameter-inactivity tradeoff likewise improves to


$$
R(A)+t(A)+1\ge c n^{1/24},
\tag{7}
$$


where $t(A)$ counts diameter-inactive points. In the proof in
[quantitative_circle](quantitative_circle.md), put $s=R+t+1$.
Under $s\le c n^{1/24}$, its checked rank inverse supplies a circle
of size at least $n/(155520s^3)\ge C(q+1)^{7/8}$, for sufficiently
small $c$. The new theorem then gives
$R\ge n/(622080s^3)>s$, a contradiction. The other size hypotheses
of that inverse hold under the same assumption; small $n$ are absorbed
by decreasing $c$.

The author checked the ordered/unordered factors, center contribution,
cosine degeneracy, largest-circle choice, and exponents; the argument
is author-recorded. The incidence input and its elementary proof are in the
linked circle note. Neither unrestricted question is answered.

## Why ordinary spectrum second moments do not improve the threshold

A subsequent attempt to improve the occupied-radius step did not
improve the unrestricted $7/8$ exponent. Put $H\asymp Q/m$.
The available pairwise pinned-spectrum overlap estimate is

$$T\ll H^{4/3}m^{2/3}.$$

Both the union bound and the usual second-moment inequality need
$T$ to be small compared with $m/H$ in order to force only $O(H)$
occupied radii. This gives exactly $m\gg H^7$ again.

There is an abstract set-system obstruction to improving that step
using only the cardinalities and pairwise overlaps. Take a projective
plane of prime-power order $h$, and replace every point by $\lambda$
clones. Its line sets have

$$k=h^2+h+1,\quad |S_i|=(h+1)\lambda,\quad
\left|\bigcup_iS_i\right|=(h^2+h+1)\lambda,\quad
|S_i\cap S_j|=\lambda\quad(i\ne j).$$

With $\lambda=h^6$, their set size is $m\asymp h^7$, their union
size is $Q\asymp h^8$, and the intersections have order
$H^{4/3}m^{2/3}\asymp h^6$. Yet $k\asymp H^2$, not $O(H)$.
This is not a Euclidean realization or a counterexample to rarity.
It rules out deriving a better power threshold from those abstract
overlap bounds alone. Controlling the actual geometry of the spectra,
especially those on sparsely occupied radii, remains a provisional
direction rather than an established improvement.
