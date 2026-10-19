---
name: research/leads/property_p_sieve_multiplicity/certified_mass_selection
title: Selecting reciprocal mass for certified blocks
desc: |
  A positive-mass extraction into jointly certified short blocks would
  prove E12(iii). A maximal matching pairs all but a bounded reciprocal
  mass locally, while an exact four-element example prevents those local
  pairs from being certified together in any eligible representation.
tags: []
sources: []
created: 2026-10-17T19:26:20Z
updated: 2026-10-17T19:51:37Z
---

# Selecting reciprocal mass for certified blocks

The
[[research/leads/property_p_sieve_multiplicity/_index|property-P sieve route]]
reduces
[[problems/integer_sequences/E0012/_index|Problem 12(iii)]]
to a uniform bound for finite odd primitive property-P sets. Here property P
excludes $a\mid b+c$ for distinct larger $b,c$, and primitive means that no
two distinct elements divide one another. Fix such a set
$B\subseteq\mathbb N_{\ge3}$ and write $h(B)=\sum_{b\in B}1/b$.
The reduction (O) on the route page gives $M_N\le3P_N$, where $P_N$ is the
largest mass in the odd primitive class, allowing the singleton 1.

This note proves a sufficient extraction criterion and a local pairing
lemma, then identifies the compatibility that the pairing does not supply.
All arguments are author-recorded by Plasma AI, without independent
review. The pairing lemma uses the route page's Proposition C at its
author-recorded standing; its Brun--Titchmarsh input retains that page's
statement-level source scope. No uniform bound for general property-P sets
is proved here.

## Extracting a fraction is enough

Use the represented full blocks and certification of Lemma T on the route
page. Thus

$$
C_i=\{n\in(X_i,Y_i]:n\bmod q_i\in R_i\},\qquad
1\le X_i<Y_i\le\frac32X_i,
$$

have integer parameters, nonempty residue sets and ordered disjoint
windows. For every $i<j$, $s\in R_i$ and $t\in R_j$, certification requires
a prime power dividing $s,q_i,q_j$ but not $2t$. In particular their gcd
types are pairwise disjoint. Put $G_i=B\cap C_i$ and $G=\bigcup_iG_i$.
Require at least two original elements of $G_i$ in each residue of $R_i$.
Points introduced by filling a block do not count toward this requirement.
Then

$$
h(G_i)\ge\frac{2|R_i|}{Y_i},\qquad
e_i:=\frac{|R_i|}{X_i+1}
\le\frac{Y_i}{2(X_i+1)}h(G_i)\le\frac34h(G_i).
\tag{1}
$$

The short-block part of Theorem B applies even when the full blocks have
elements outside $B$ and their union does not have property P. It gives

$$
h(G)\le\sum_i h(C_i)
\le\log(3/2)+\sum_i e_i
\le\log(3/2)+\frac34h(G),
$$

and hence

$$
h(G)\le4\log(3/2).
\tag{2}
$$

Consequently the following unproved selection statement would finish the
problem.

> **(EX)** There are absolute constants $\delta>0$ and $C_0\ge0$ such that
> every finite odd primitive property-P set $B\subseteq\mathbb N_{\ge3}$
> admits a family as above with $h(G)\ge\delta h(B)-C_0$.

Indeed, (2) and (EX) imply

$$
h(B)\le\frac{4\log(3/2)+C_0}{\delta},\qquad
M_N\le3\max\left(1,\frac{4\log(3/2)+C_0}{\delta}\right).
\tag{3}
$$

The singleton 1 is covered by the maximum in (3). Truncation gives the
infinite conclusion. Only the selected blocks need to be certified with
one another: the omitted elements of $B$ need no compatible singleton
extension or certified cover. This distinguishes the proposed product from
the full cover in (IC) on the route page.

Statement (EX) is still full-strength. A uniform bound $h(B)\le U$ would
make it true with the empty family and $C_0=\delta U$. Thus the criterion
offers a concrete construction problem, not a logically weaker theorem.
The existence of a useful extraction is unproved.

## Local pairs leave only bounded mass unmatched

There is a local construction that supplies most of the mass before joint
certification. For each integer $j\ge1$, use the two windows

$$
(2^j,3\cdot2^{j-1}],\qquad
(3\cdot2^{j-1},2^{j+1}].
\tag{4}
$$

These partition the integers at least 3, with integer endpoints and ratio
at most $3/2$. In each window form the finite graph on its elements of $B$,
joining two elements when their gcd exceeds 1, and choose a maximal
matching. Let $U$ be the unmatched elements across all windows. Then

$$
h(U)<14.
\tag{5}
$$

To prove (5), the unmatched elements in each window are pairwise coprime,
by maximality. For each odd prime $p$ there is therefore at most one
unmatched composite with least prime factor $p$ in each window. Every such
composite is at least $p^2$. If $j_p=\lfloor\log_2(p^2)\rfloor$, the two
windows per dyadic interval give

$$
\sum_{\substack{a\in U,\ a\text{ composite}\\P^-(a)=p}}\frac1a
\le2\sum_{j\ge j_p}2^{-j}
=4\cdot2^{-j_p}<\frac8{p^2}.
$$

Here $P^-(a)$ denotes the least prime factor of $a$. Since
$\sum_{p\ge3}p^{-2}<\sum_{n\ge3}(n(n-1))^{-1}=1/2$, the unmatched
composites contribute less than 4. The prime elements of $U$ form a
pairwise coprime property-P set, so Proposition C bounds their reciprocal
sum by less than 10. This proves (5).

Thus disjoint pairs of original elements, each inside one short window
and each sharing a prime factor, have total endpoint mass greater than
$h(B)-14$. Every pair $a<b$ is itself a full short block: take
$X=a-1$, $Y=b$, $q=b-a$ and the single residue $a\bmod q$. Its class in
that window is exactly $\{a,b\}$ and has
$\gcd(a,q)=\gcd(a,b)>1$. The short-ratio condition follows from the window
in (4) containing the pair. Each of these blocks has the occupancy saving
in (1).

The paired endpoints are disjoint, but the intervals of different pairs
inside one window may overlap. More importantly, the blocks are not
necessarily certified together. Neither merging pairs into one common
modulus nor refining their residues is known to preserve the requirement
that each residue contain two original elements. Estimate (5) does not
give (EX).

## An exact test for two-element blocks

Suppose the selected original elements in each ordered short window are
exactly $\{a_i,b_i\}$, with $a_i<b_i$, and every used residue contains at
least two original elements. There can be only one used residue, and its
modulus must divide $d_i=b_i-a_i$. For two such windows, a certificate can
exist only if some prime power satisfies

$$
p^e\mid\gcd(a_i,b_i,d_j),\qquad p^e\nmid2a_j
\quad(i<j).
\tag{6}
$$

Indeed, a certificate divides $q_i,q_j,a_i$, while $q_i\mid d_i$ and
$q_j\mid d_j$. Conversely, if (6) holds for every ordered pair of windows,
the choices $q_i=d_i$ and $R_i=\{a_i\bmod d_i\}$ certify the family.
Shrink each window to $(a_i-1,b_i]$; this preserves its short ratio and
the ordering of the windows. With these endpoints the choices give exactly
the two-element blocks above. Thus (6) is an exact compatibility test for
this setting, not just a necessary check on one chosen representation.

Consider the odd primitive set

$$
B=\{21,27,115,125\}.
\tag{7}
$$

It has property P. For the early element 21 the relevant sums are
$142,152,240$, with remainders $16,5,9$ modulo 21. For 27 the only
relevant sum is 240, with remainder 24. The other elements have no two
distinct larger summands. Primitivity follows directly from
$21=3\cdot7$, $27=3^3$, $115=5\cdot23$ and $125=5^3$.

Both pairs are full short blocks containing two original elements:

$$
C_1=\{n\in(20,27]:n\equiv3\pmod6\}=\{21,27\},
$$

$$
C_2=\{n\in(114,125]:n\equiv5\pmod{10}\}=\{115,125\}.
$$

Each has a nontrivial common divisor. But their difference moduli are 6
and 10, and $\gcd(21,27,10)=1$. Condition (6) fails. In fact no eligible
short block can contain original elements from both pairs, since
$115/27>3/2$. A block meeting $B$ and satisfying the occupancy requirement
must therefore capture exactly one of these pairs. No representation can
put both into one certified extraction with that requirement.

This refutes the inference from efficient local pairs, even pairs with a
shared prime, to a jointly certified family. It does not refute (EX): a
single pair can be selected, and its bounded omitted mass can be absorbed
in $C_0$. It does not exclude a different representation of a larger set
with more original points available.

## The remaining selection obligation

The local pairing proves that a large reciprocal mass has many available
shared-divisor pairs. It supplies neither an ordering of disjoint block
windows carrying a fixed fraction of that mass nor the directed
prime-power separation in (6). A full selection argument must handle
both, retaining $\delta h(B)-C_0$ with constants independent of the number
of windows and of their moduli. It must charge rejected original elements
globally; checking each block separately is insufficient.

The mixed identities (M) and (T) on the route page retain more of property
P than certification does. No estimate extracting the required compatible
family from those identities is proved. The large-sieve allowance and
the two-window density estimate on that page are not such an inverse
estimate. The route reopens with an actual selection rule and a uniform
bound on its lost harmonic mass, or with a direct strict signed global
bound. The results here are written arguments; the route's existing
finite evidence driver does not verify them.
