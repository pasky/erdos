---
name: research/erdos_644/exterior_transversal_model
desc: Exact exterior and ordinary split-form models preserving transversal data, with dimension reductions and limitations of localization and set-pair certificates.
tags: [proved, reductions, limitations]
sources: [tuza_1985_critical_hypergraphs_intersecting_set_pair_systems]
created: 2026-09-22T22:08:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/exterior_transversal_model

***

The results below are elementary reformulations and dimension reductions. They
do not improve the unrestricted bound for Problem 644. Throughout, the
hypergraph is finite, its edges are nonempty, and a cover may have at most the
indicated number of points. The final section gives a separate
ordinary-polynomial-ring model preserving every subfamily's transversal number
as an ideal height.

## Coordinate subspaces retain the exact transversal number

Let $\mathcal H$ be a hypergraph on a finite set $X$, and let
$V=\mathbb F^X$, with coordinate basis $(e_x)_{x\in X}$. Associate to each
edge $A$ the subspace

$$
W_A=\operatorname{span}\{e_x:x\in A\}.
$$

For a family $\mathcal L$ of nonzero linear subspaces, define

$$
\lambda(\mathcal L)=\min\{\dim U:U\cap L\ne\{0\}\text{ for every }L\in\mathcal L\}.
$$

Then

$$
\lambda(\{W_A:A\in\mathcal H\})=\tau(\mathcal H).
\tag{1}
$$


The inequality $\lambda\le\tau$ follows by spanning the coordinate vectors of
a cover. Conversely, let $U$ be an $s$-dimensional linear transversal. There
is a set $T\subseteq X$ of size $s$ such that the coordinate projection

$$
\pi_T:U\longrightarrow\mathbb F^T
$$

is injective: choose a nonsingular $s$-column minor of a matrix whose rows
form a basis of $U$. For every edge $A$, choose $0\ne u\in U\cap W_A$.
Since $\pi_T(u)\ne0$, some coordinate in $A\cap T$ is nonzero. Thus $T$
covers $\mathcal H$, proving (1).

In particular, the original $P_7$ property is exactly the assertion that every
at-most-seven of these coordinate subspaces admit a linear transversal of
dimension at most two. This equality uses the common coordinate representation;
it is not an assertion about arbitrary subspace arrangements and arbitrary
designated point sets.

## An exact exterior-ideal formulation

Write $E=\Lambda V$, and use $e_T$ for the exterior monomial associated with
a subset $T\subseteq X$, with a fixed ordering of $X$. Define the ideal

$$
I_A=W_A\wedge E.
$$

Its degree-$s$ part has basis

$$
\{e_T:|T|=s,\ T\cap A\ne\varnothing\}.
$$

Consequently, for

$$
J(\mathcal H)=\bigcap_{A\in\mathcal H}I_A,
$$

one has

$$
J(\mathcal H)_s
=\operatorname{span}\{e_T:|T|=s,\ T\text{ covers }\mathcal H\}.
\tag{2}
$$

In particular,

$$
\min\{s:J(\mathcal H)_s\ne0\}=\tau(\mathcal H).
\tag{3}
$$

Also $I_A=\operatorname{Ann}_E(e_A)$. Indeed, multiplication by $e_A$ kills
precisely the monomials meeting $A$; distinct monomials disjoint from $A$
have distinct nonzero products, up to signs.

Thus $P_7$ is equivalent to nonvanishing in degree two of the intersection of
every at-most-seven of the ideals $I_A$, provided $|X|\ge2$. The trivial
one-point case can instead be expressed using nonvanishing in some degree at
most two. A proof of the desired bound could therefore construct a nonzero
element of $J(\mathcal H)$ in the desired degree. It need not construct a
decomposable element: by (2), any nonzero homogeneous element already has a
cover among its nonzero monomials.

This last conclusion is specific to coordinate ideals. For an arbitrary subspace
$L\subseteq V$, a nonzero decomposable element of $\Lambda^sV$ belongs to
$L\wedge E$ exactly when its associated $s$-plane meets $L$ nontrivially.
Nonzero elements of an intersection of such ideals need not be decomposable.

Here is a finite illustration over a field of characteristic different from two.
In a four-dimensional space with basis $e_1,e_2,f_1,f_2$, take

$$
\begin{aligned}
L_1&=\langle e_1,e_2\rangle,&L_2&=\langle f_1,f_2\rangle,\\
L_3&=\langle e_1,f_2\rangle,&L_4&=\langle e_2,f_1\rangle,\\
L_5&=\langle e_1+e_2,f_1-f_2\rangle.
\end{aligned}
$$

The degree-two intersection of the first four ideals is
$\langle e_1\wedge f_1,e_2\wedge f_2\rangle$. Modulo $L_5$, one has
$e_2=-e_1$ and $f_2=f_1$, so the intersection of all five ideals in degree
two is exactly

$$
\langle\Omega\rangle,
\qquad
\Omega=e_1\wedge f_1+e_2\wedge f_2.
$$

But $\Omega\wedge\Omega\ne0$, so this space contains no nonzero decomposable
bivector. Thus these five planes have a common nonzero degree-two exterior
annihilator but no two-dimensional linear transversal. Their linear transversal
number is three, since every three-dimensional subspace meets every
two-dimensional subspace in a four-dimensional space.

## A dimension reduction that preserves the transversal number

Suppose $\mathcal H$ has rank at most $k$ and $\tau(\mathcal H)=t$. Over
an infinite field, it admits a representation by subspaces of dimension at most
$k$ in an ambient space of dimension

$$
D=kt
\tag{4}
$$

whose linear transversal number is exactly $t$. Moreover, every original
two-point cover still gives a cover by the corresponding two designated vector
lines. Thus the full local $P_7$ property is retained.

Choose vectors $(v_x)_{x\in X}$ in $\mathbb F^D$ such that every
at-most-$D$ of them are linearly independent. Distinct parameters on the
moment curve give such a choice. Let

$$
\phi:\mathbb F^X\longrightarrow\mathbb F^D,
\qquad \phi(e_x)=v_x,
\qquad L_A=\phi(W_A).
$$

The map is injective on every coordinate subspace supported on at most $D$
points. In particular, $\dim L_A=|A|$.

Spanning the vectors of a minimum cover gives $\lambda(\{L_A\})\le t$.
Suppose, for a contradiction, that a subspace $U$ of dimension at most $t-1$
meets every $L_A$. For each edge choose $0\ne u_A\in U\cap L_A$, and lift it
uniquely to $z_A\in W_A$.

The span of all the lifts has dimension at most $t-1$. Otherwise, choose $t$
independent lifts. They are supported on the union of $t$ edges, which has
size at most $kt=D$. The map $\phi$ is injective on that coordinate
subspace, so their images are independent, contradicting $\dim U\le t-1$. The
span of the lifts is therefore a linear transversal of the original coordinate
spaces of dimension at most $t-1$. Equation (1) gives a cover of
$\mathcal H$ of that size, a contradiction.

If $\{x,y\}$ covers an original subfamily, each corresponding $L_A$ contains
$v_x$ or $v_y$, so the local assertion is immediate. This representation is
a quadratic-dimensional **linear-subspace** reduction when $t=O(k)$; it is not
a quadratic-vertex hypergraph kernel. Nor does the proof assert that
nondecomposable exterior annihilators retain their minimum degree after the
projection.

The much smaller dimension $k+t-1$ does not in general preserve linear
transversal number. Take two disjoint $k$-sets, where $k\ge2$, so that
$t=2$. After mapping their points in general position into dimension $k+1$,
their two $k$-dimensional spans intersect in dimension at least $k-1$. The
projected family has linear transversal number one, although the original family
has transversal number two and satisfies $P_7$.

## Set-pair biorthogonality alone loses the minimum-cover condition

The exterior identities obtained from critical set pairs do not by themselves
encode the transversal number. Fix $k\ge2$, let $C$ have size $k-1$, and
choose distinct points $v_1,\ldots,v_s$ outside $C$. Put

$$
A_i=C\cup\{v_i\},
\qquad T_i=\{v_j:j\ne i\}.
$$

Then

$$
|A_i|=k,
\quad |T_i|=s-1,
\quad A_i\cap T_i=\varnothing,
\quad A_i\cap T_j\ne\varnothing\quad(i\ne j).
$$

Each $T_i$ is even an inclusion-minimal cover of the family with $A_i$
deleted: its point $v_j$ is needed to hit $A_j$. Nevertheless, all the
$A_i$ share $C$, so their actual transversal number is one and their local
two-cover property is automatic.

In the coordinate space of dimension $k+s-1$, let $x_i=e_{A_i}$ and
$y_i=e_{T_i}$. They satisfy

$$
x_i\wedge y_j=0\quad(i\ne j),
\qquad x_i\wedge y_i\ne0.
$$

Thus the usual decomposable set-pair biorthogonality and the local two-factor
covering property hold with an arbitrarily large formal parameter $s$. Any
argument that uses only these identities cannot bound $s$ by a constant
multiple of $k$. To use the true parameter $t=\tau(\mathcal H)$, it must
additionally retain the absence of smaller covers, for example through (1) or
(3). This is a limitation of the reduced algebraic data, not a counterexample to
the original problem.

## Tuza's completion can destroy the local property

Section 6.7 of
[first independent record](independent/fano_ground_set_and_coding_constructions.md)
leaves preservation by Tuza's Construction 15 unproved. In fact it fails
explicitly, even when the completion stays uniform. The definition below was
checked in the
[paper, §4.1](../../../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/_index.md).

For an $(a,b)$ set-pair system $(A_i,B_i)$, put $V=\bigcup_i(A_i\cup B_i)$ and
$\mathcal H'=\{A_i\}$. Construction 15 adjoins $V\setminus T$ for every
$b$-element transversal $T$ of $\mathcal H'$.

Specialize the preceding example to $k=2$, $C=\{c\}$, and $s\ge7$:

$$
A_i=\{c,v_i\},\qquad B_i=\{v_j:j\ne i\}.
$$

This is a $(2,s-1)$ set-pair system, and $\mathcal H'$ has a one-point cover. A
size-$(s-1)$ set covers all the $A_i$ exactly when it contains $c$: without $c$
it would have to contain all $s$ leaves. Its complement is therefore an
arbitrary pair of leaves. The completion is exactly the complete graph
$K_{s+1}$, with transversal number $s$. The six edges of a leaf $K_4$ have
transversal number three; extending them to seven edges proves failure of $P_7$.
Thus completion can convert a formally large certificate parameter into a large
actual transversal number only at the cost, in this example, of losing the
required local property.

The separate set-pair composition in §2.1 also does not add transversal
parameters. Its first-coordinate family consists of $A'_i\cup A''_{ij}$, where
the $A'_i$ are all $a'$-subsets of a fixed $(a'+b')$-set and the inner families
have disjoint private grounds for different $i$. For $a'>0$, its transversal
number is **exactly** $b'+1$. Any $b'+1$ outer points cover it. Conversely,
replace each selected inner point in copy $i$ by any point of $A'_i$; this
preserves coverage without increasing size. The resulting outer cover meets
every $a'$-subset and thus has at least $b'+1$ points. This strengthens the
independent note's upper bound and shows directly why the summed set-pair
parameters do not give transversal amplification.

## Ordinary split forms preserve all local heights

Let $\mathcal H$ be finite and nonempty with $\tau(\mathcal H)=t$. Over an
infinite field choose linear forms $L_v$ in

$$
R=\mathbb F[z_1,\ldots,z_t]
$$

such that every at-most-$t$ of them are linearly independent; a Vandermonde
construction suffices. Put $f_E=\prod_{v\in E}L_v$. Then, simultaneously for
every subfamily $\mathcal F\subseteq\mathcal H$,

$$
\operatorname{ht}(f_E:E\in\mathcal F)=\tau(\mathcal F).
\tag{P1}
$$


Indeed, if a prime ideal $Q$ contains all these products, primality makes

$$
T_Q=\{v:L_v\in Q\}
$$

a transversal of $\mathcal F$. General position implies

$$
\operatorname{ht}Q\ge\min\{|T_Q|,t\}\ge\tau(\mathcal F),
$$

where $\tau(\mathcal F)\le t$ was used. Conversely, the linear ideal generated
by the forms of a minimum transversal has height $\tau(\mathcal F)$ and contains
every product. This proves (P1), including the empty subfamily.

For a $k$-uniform $P_7$ family, the full ideal is homogeneous and
maximal-ideal-primary in $t$ variables, generated by split degree-$k$ forms,
while every at-most-seven distinguished generators generate an ideal of height
at most two. This is an exact reformulation. It has not yielded an inequality
between $t$ and $k$.

### Criticality gives interpolation

Assume $\mathcal H$ is transversal-critical. For each edge $E$, choose a
$(t-1)$-cover $T_E$ of all other edges disjoint from $E$. The forms of $T_E$ cut
out a projective point $p_E\in\mathbb P^{t-1}$. General position gives

$$
f_E(p_E)\ne0,\qquad f_F(p_E)=0\quad(F\ne E).
$$

Thus the $f_E$ are linearly independent Lagrange interpolation polynomials,
recovering

$$
|\mathcal H|\le\dim R_k=\binom{k+t-1}{k}
$$

in the uniform case.

For the complete $k$-uniform family on $k+t-1$ points, equality holds. Its
compressed ideal is therefore exactly $(z_1,\ldots,z_t)^k$. The local condition
resides in the distinguished split generators, not merely in the resulting ideal
or its Hilbert function.

### Why localization does not preserve the hypothesis

In the original squarefree monomial ideal $I=(x_E:E\in\mathcal H)$, let $T$ be a
minimum transversal and $P_T=(x_v:v\in T)$. Minimality supplies an edge $E_v$
with $E_v\cap T=\{v\}$ for every $v\in T$. After localization at $P_T$, its
monomial is a unit times $x_v$. Hence

$$
I_{P_T}=P_TS_{P_T}.
$$

Any $q$ of these witness generators have localized height $q$, even when $q\le7$
and their global subideal has height at most two.

Thus localizing at a minimum-transversal prime removes the low-height components
responsible for $P_7$. An order-ideal or regular-sequence argument there cannot
silently reuse the original local-height hypothesis. The map from the original
coordinate ring to the split-form model is likewise a parameter reduction, not a
proved regular-sequence reduction; preservation of graded resolutions is not
asserted.

## Further geometric tests

These tests were explored as an alternative to the combinatorial selection
arguments. They are exact reformulations or limitations, not an improvement of
the unrestricted transversal bound.

### An exact planar piercing model

Choose distinct real numbers $a_v$ and let

$$
\ell_v:\quad y=2a_vx-a_v^2.
$$

No two lines are parallel, and no three concur: the intersection of
$\ell_u,\ell_v$ has coordinates $((a_u+a_v)/2,a_ua_v)$, and it lies on $\ell_w$
exactly when $(a_w-a_u)(a_w-a_v)=0$.

Associate to an edge $E$ the connected union $C_E=\bigcup_{v\in E}\ell_v$. For
every nonempty subfamily $\mathcal F$, its planar point-piercing number
satisfies

$$
\pi(\{C_E:E\in\mathcal F\})=\left\lceil\frac{\tau(\mathcal F)}2\right\rceil.
$$

Indeed, one planar point lies on at most two designated lines, so $s$ piercing
points give an original transversal of size at most $2s$. Conversely, pair the
vertices of a minimum transversal and use their line intersections, with an
arbitrary point on an unpaired line if needed.

Thus $P_7$ is exactly seven-wise nonempty intersection for these unions of $k$
lines, and the target becomes a piercing bound $(3/8+o(1))k$. This preserves the
full global parameter up to rounding, unlike restriction of ideal height to
three variables. Connectivity by itself supplies no improvement: the
complete-family examples already require linearly many piercing points.

### Projective base schemes are reduced

In the generic split-form model above, put $I_{\mathcal F}=(f_E:E\in\mathcal F)$
and $\mathfrak m=(z_1,\ldots,z_t)$. Then

$$
I_{\mathcal F}^{\mathrm{sat}}=
\bigcap_{\substack{T\text{ inclusion-minimal transversal of }\mathcal F\\|T|<t}}
(L_v:v\in T),
\tag{P2}
$$

where an empty intersection denotes $R$. In particular the saturation is
radical.

To prove this, take a prime $P\ne\mathfrak m$. Fewer than $t$ factor forms lie
in $P$, because any $t$ generate $\mathfrak m$. Those forms are independent and
can be extended to coordinates. Each $f_E$ becomes a unit times a squarefree
monomial in them. Thus $(I_{\mathcal F})_P$ is radical. Its minimal primes away
from $\mathfrak m$ are exactly the linear ideals of the inclusion-minimal
transversals of size less than $t$, proving (P2).

Every codimension-two component therefore has multiplicity one. Directly, a
minimal two-cover $\{x,y\}$ has a witness edge containing $x$ but not $y$, and
one containing $y$ but not $x$. At $(L_x,L_y)$ these generators give the full
localized linear ideal. Consequently multiplicity at these components adds no
weights beyond the existing pair-cover graph. This does not rule out information
from higher-codimension intersections or the finite-length saturation defect.

### Full-ideal multiplicity is universal

If a homogeneous $\mathfrak m$-primary ideal $I$ in $t$ variables is generated
entirely in degree $k$, then its Hilbert--Samuel multiplicity is

$$
e(I)=k^t.
\tag{P3}
$$

This holds without splitting or a local transversal condition. Choose $D\ge k$
with $\mathfrak m^D\subseteq I$. Equigeneration gives $R_d=I_kR_{d-k}$ for
$d\ge D$. Iterating yields

$$
\mathfrak m^{kq+D-k}\subseteq I^q\subseteq\mathfrak m^{kq}.
$$

The lengths of the bounding quotients have the same leading coefficient $k^t/t!$
as polynomials in $q$, proving (P3).

Thus this multiplicity also cannot distinguish candidate extremal families. The
colength $\dim R/I$ is a different invariant and is not determined here. Nor do
the generic factor points supply a Sylvester--Gallai configuration: in dimension
at least three they may have no three collinear, while a local two-cover merely
records the span of its two factors. No useful additional geometric incidence
was established.
