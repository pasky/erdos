---
name: research/leads/projective_plane_bounded_blocking/curve_reduction
title: A conditional negative answer from approximate curve structure
desc: A source estimate for lines missing nonlinear curves survives exceptional points. Derangement densities give the exact coefficient needed by a sufficient extraction argument for minimal bounded-cap blocking sets; the structural premise remains unproved.
created: 2026-10-16T20:53:47Z
updated: 2026-10-16T20:53:47Z
---

***

This is the negative branch of the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking sketch]].
It makes a possible full conclusion precise, but its structural premise
is unproved. The implication is author-recorded by Plasma AI, without
independent review, and depends on the source estimate specified below.

## The structural premise

Fix an integer $C\ge1$. Consider the following statement, with the degree
bound uniform in the set and in the prime.

**Approximation premise.** There is an integer $D=D(C)\ge2$ such that,
for every sufficiently large prime $p$ and every
$S\subseteq\operatorname{PG}(2,p)$ meeting each line in at most $C$
points, some nonzero homogeneous polynomial $F$ over $\mathbb F_p$ of
degree at most $D$ satisfies

$$
|S\setminus V(F)|\le 2^{-D-3}p.
$$

A stronger version replaces the displayed bound by $o(p)$ uniformly over
$S$, while keeping $D$ fixed. The latter is the projective formulation of
the general bounded-intersection conjecture in the commentary to Problem
68, printed p. 33, of
[[../library/additive_bases/green_2026_100_open_problems/_index|Green's January 2026 manuscript]].
The affine/projective distinction costs at most $C$ points on the chosen
line at infinity, which is harmless for $o(p)$. This is a conjectural
structural statement, not a theorem of that source. It is stronger than
needed in applying the displayed premise to blocking sets because it
also concerns sets leaving lines empty.

## A sufficient restriction to minimal blocking sets

For the negative argument it suffices to prove the approximation premise
only for inclusion-minimal blocking sets of cap at most $C$. Here minimal
means that deleting any point destroys the blocking property; it does
not assert smallest cardinality among all blocking sets.

Indeed, any cap-$C$ blocking set $S$ contains an inclusion-minimal
blocking subset $B$, obtained by deleting points while every line remains
met. Its line cap is still at most $C$. Each point $P\in B$ has a tangent
line $\ell_P$, meaning $B\cap\ell_P=\{P\}$: if none existed, every line
through $P$ would retain a point after its deletion, contradicting
minimality. Apply the same uniform degree bound and exceptional-point
bound to $B$. The conditional argument below produces a line missing
$B$, contradicting its blocking property. Thus there can have been no
$S$, even though the curve need not approximate $S$ itself.

The sufficient structural problem therefore retains both hypotheses:
every line is met, and every selected point has a tangent. The degree
$D(C)$ and the threshold for $p$ must still be uniform over all such
minimal sets. These extra conditions offer information for a polynomial
argument that the general bounded-cap conjecture does not use. They do
not themselves supply the approximation theorem.

## Source estimate and its exact use

Asgarli, Ghioca and Yip, *Blocking sets from a union of plane curves*,
[[../library/set_systems/asgarli_2025_blocking_sets_union_plane_curves/theorem_3_2|v2, Section 3, Theorem 3.2 and equation (3.1)]],
give the following estimate.
For a reduced union $Y$ of geometrically irreducible curves defined over
$\mathbb F_p$, of degrees $d_i\ge2$, total degree at most $D$, and with
the reflexivity hypothesis of that theorem, the number of lines missing
$Y(\mathbb F_p)$ is at least

$$
\left(\prod_i\frac1{d_i}\right)p^2
\left(1+O_D(p^{-1/2})\right).
$$

Only one conjugacy class, a full cycle on each component, is counted;
there may be additional missing lines. For $p>D$ the components are
reflexive as required in Section 3. The degree-uniform error is essential
because $Y$ is allowed to vary with $p$ and $S$. Since $d\le2^d$ for
each positive integer $d$, the leading coefficient is at least $2^{-D}$.
Thus for all sufficiently large $p$, uniformly in $Y$ of this degree
bound, at least $2^{-D-1}p^2$ lines miss it. If $Y$ is empty, every line
misses it and the same lower bound holds.

Read scope: the v2 HTML and TeX of Section 3, its statements, and the
derivation (3.1)--(3.2) were inspected. Printed pp. 6--8 were read in
extracted PDF text; Theorem 3.2 and (3.1) on p. 7 were also checked on
the page image. Theorem 3.2 is attributed there
to Entin, *Monodromy of hyperplane sections of curves and decomposition
statistics over finite fields*, IMRN 2021(14), 10409--10441, Theorem 1.
The exact Entin v3 monodromy and counting arguments in Sections 2--5
were read in TeX, and Hefez's degree-below-characteristic consequence
was inspected at statement level; the
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil proof]]
records these interfaces and their external dependencies. This is use
of identified source results, not independent verification of them.
The paper's curve theorem does not itself apply to arbitrary point sets.

## End-to-end conditional argument

Assume the approximation premise for the fixed cap $C$, and suppose $S$
is a cap-$C$ blocking set in PG$(2,p)$ for arbitrarily large primes $p$.
Take its polynomial $F$ of degree at most $D=D(C)$. Replace $F$ by its
squarefree part; the zero set does not change. Separate its components
over $\mathbb F_p$ as follows.

1. A line defined over $\mathbb F_p$ contains at most $C$ points of $S$.
   Discarding all such components loses at most $CD$ points of $S$.
2. An irreducible component defined over $\mathbb F_p$ that is not
   geometrically irreducible has at most $D^2$ rational points in total
   over all such discarded components. Indeed, any rational point on it
   lies on each Frobenius conjugate of a geometric component. Two
   distinct conjugates meet in at most the product of their degrees by
   Bézout; summing these bounds is at most the square of the total degree.
   This also handles geometric line components not defined over
   $\mathbb F_p$.
3. The remaining union $Y$ consists of geometrically irreducible
   components of degree at least two, all defined over $\mathbb F_p$,
   with total degree at most $D$. For large $p>D$ it meets the hypotheses
   of the source estimate.

Let $T=S\setminus Y$. The preceding steps give

$$
|T|\le 2^{-D-3}p+CD+D^2.
$$

Each point of $T$ belongs to exactly $p+1$ lines, so at most
$|T|(p+1)$ lines meet $T$. On the other hand, at least
$2^{-D-1}p^2$ lines miss $Y$. For all sufficiently large $p$,

$$
2^{-D-1}p^2>
\bigl(2^{-D-3}p+CD+D^2\bigr)(p+1).
$$

Some line therefore misses both $Y$ and $T$, and hence misses $S$, a
contradiction. For this fixed $C$, no cap-$C$ blocking set exists once
$p$ is sufficiently large. If the approximation premise holds for every
fixed $C$, this proves $c(\operatorname{PG}(2,p))\to\infty$ along the
primes and answers Problem 1159 negatively. These are full projective
planes, and the structural premise is quantified over arbitrary point
sets, so neither of the usual scope restrictions remains hidden in this
conditional implication.

## The coefficient an extraction argument actually needs

The tolerance $2^{-D-3}$ is a convenient sufficient choice, not a
necessary error threshold. The same source theorem permits a larger
coefficient. For $d\ge2$ put

$$
\delta_d=\frac{\#\{\pi\in S_d:\pi\text{ has no fixed point}\}}{d!}
=\sum_{j=0}^d\frac{(-1)^j}{j!},\qquad
\alpha(Y)=\prod_i\delta_{d_i}.
$$

The empty product is $1$. Inclusion-exclusion gives the formula for
$\delta_d$. Sum Theorem 3.2 over every product conjugacy class with no
fixed points. Those classes are disjoint, there are boundedly many at
fixed total degree, and their relative sizes sum to $\alpha(Y)$.
Consequently the number of transverse lines missing $Y$ is

$$
\alpha(Y)p^2\bigl(1+O_D(p^{-1/2})\bigr).
\tag{1}
$$

Only a lower bound on all missing lines is needed; no claim about the
nontransverse lines enters the argument. For empty $Y$, all lines miss
it, and the analogous lower bound holds. In particular, for any fixed
$\varepsilon>0$, the sufficient exceptional-point condition is

$$
|B\setminus Y|\le\bigl(\alpha(Y)-\varepsilon\bigr)p.
\tag{2}
$$

Indeed, the exceptional points meet at most
$(\alpha(Y)-\varepsilon)p(p+1)$ lines, fewer than (1) when $p$ is
sufficiently large. This is a uniform implication when $D$ and
$\varepsilon$ are fixed before $p$. It applies to any blocking set
$B$; minimality is information for proving (2), not a hypothesis needed
by this counting contradiction.

There is a sharper degree-only lower bound too. Let $M(D)$ be the
maximum product of integers at least two whose sum is at most $D$,
allowing the empty product. Thus $M(0)=M(1)=1$ and

$$
M(D)=
\begin{cases}
3^{D/3},&D\equiv0\pmod3,\ D\ge3,\\
4\cdot3^{(D-4)/3},&D\equiv1\pmod3,\ D\ge4,\\
2\cdot3^{(D-2)/3},&D\equiv2\pmod3.
\end{cases}
$$

To verify this formula, an optimal nonempty partition uses its whole
budget: otherwise one part can be increased. Replace each part
$k\ge5$ by $3$ and $k-3$, increasing its product, and replace $4$ by
$2+2$ without changing it. Three parts equal to $2$ are inferior to
two equal to $3$, leaving precisely the displayed cases. Full cycles
are derangements, so $\delta_d\ge1/d$ and therefore

$$
\alpha(Y)\ge\frac1{\prod_i d_i}\ge\frac1{M(D)}.
\tag{3}
$$

In particular the uniform approximation tolerance $1/(4M(D))$ can
replace $2^{-D-3}$ in the structural premise. The discarded line and
non-geometrically-irreducible components still cost only $CD+D^2$
points, which is $o(p)$ at fixed $C,D$. This proves another sufficient
implication; it supplies no approximation theorem.

Equation (2) bounds the lines through each exceptional point by $p+1$.
The [[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil count]]
replaces this by the number of missed lines through that point, about
$\alpha(Y)p$, and so raises the tolerance in (2) from about $\alpha(Y)p$ to
$p-O_{C,D}(\sqrt p)$. It proves this for unions of lines and conics in odd
characteristic and, using tame monodromy and uniform Chebotarev, for
all curves of bounded degree in sufficiently large prime planes.
Both proofs remain author-recorded.

### Repeated extraction with its hypotheses retained

Suppose, provisionally, that for each fixed $C$ there are fixed
$d\ge2$ and $0<\eta\le1$ with the following extraction property.
Starting with any inclusion-minimal cap-$C$ blocking set $B$ in a
sufficiently large prime plane, one can repeatedly choose nonzero
homogeneous polynomials $F_j\in\mathbb F_p[X,Y,Z]$ of degree at most
$d$, each vanishing on at least the fraction $\eta$ of the current residual
$R_{j-1}=B\setminus\bigcup_{i<j}V(F_i)$. The property must remain
valid for all the finitely many steps used below, uniformly in $B,p$.

The cap implies $|B|(p+1)\le C(p^2+p+1)$, hence
$|B|\le(C+o(1))p$. After $t$ extractions,

$$
|R_t|\le(C+o(1))(1-\eta)^t p.
$$

The reduced union has degree at most $td$. Discard its line and
non-geometrically-irreducible components as before, leaving $Y_t$.
Each selected curve contributes component-degree product at most
$M(d)$. Removing repeated components can only increase the lower
bound in (3). Thus

$$
\alpha(Y_t)\ge M(d)^{-t},\qquad
\frac{|B\setminus Y_t|}{p\alpha(Y_t)}
\le C\bigl[M(d)(1-\eta)\bigr]^t+o(1).
\tag{4}
$$

If $M(d)(1-\eta)<1$, choose a fixed $t=t(C)$ making the right side
less than $1/2$, then take $p$ large. Equation (2) contradicts blocking.
This hypothetical extraction theorem for every fixed cap would therefore
settle Problem 1159 negatively. When $d=2$, the sufficient capture
threshold is $\eta>1/2$; when $d=3$, it is $\eta>2/3$.

Known component information can improve this test. If each extraction
uses one geometrically irreducible nonlinear curve of bounded degree,
then $\delta_d\ge1/3$ for all $d\ge2$: after $1/2-1/6$, the
alternating sum defining $\delta_d$ has nonnegative successive pairs.
Consequently $\eta>2/3$ suffices independently of that fixed degree
bound. More generally, let $\beta_j$ be the product of the derangement
densities of the new nonlinear components at step $j$, with repeated
components omitted. The sufficient test is
$C\prod_{j\le t}(1-\eta_j)/\beta_j<1$, with a fixed strict margin,
fixed total degree, and the exceptional contributions included.
These are sufficient tests. Failure of a displayed inequality does not
exclude an extraction argument using sharper data.

There is a separate logical condition. Removing captured points
preserves the cap and a tangent at each retained point, but generally
destroys the blocking property. A theorem stated only for minimal
blocking sets cannot be reapplied to $R_j$. A repeated argument must
keep the original $B$ and prove its extraction statement for the pairs
$(B,R_j)$ that occur, or prove an invariant that still permits the next
step. Alternatively, a one-shot approximation can establish (2)
directly. No extraction property of any of these strengths is proved
here.

Through the pencil count of the
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil page]],
its Theorem B removes both conditions. Any fixed capture fraction
$\eta>0$ suffices, since the exceptional tolerance no longer shrinks with
the degree. The extraction may be required of arbitrary cap-$C$ sets of
at least $(1-\varepsilon)p$ points, which every residual is until the
iteration stops.
A weaker relative form also suffices, with constants uniform through
the required finite number of steps: each residual still meets every
line missing the curves already extracted. If the initial blocker
$B$ is minimal and $A_j$ is its captured portion, the residual is
inclusion-minimal for the larger family of lines avoiding $A_j$,
as proved on the pencil page. An extraction theorem must capture
new residual points, rather than points already in $A_j$.

## The gap and a discriminating test

The missing step is the approximation premise, or its sufficient
restriction to minimal blocking sets, for all fixed $C$, or at least for
all fixed caps in an unbounded set of integers. No argument here
establishes it, even at cap four. A theorem only at cap
four could raise a lower bound but would not answer the absolute-cap
question. The constants and quantifier order cannot be dropped: the
degree must stay bounded as $p$ grows. In the global counting argument
above, the exceptional proportion must also be compared with the
missing-line density. The pencil count gives the larger tolerance
specified below.

Given the source estimate, the restriction of the premise to minimal
blocking sets is equivalent to the nonexistence of cap-$C$ blocking sets
in large prime planes, since it holds vacuously if there are none. Its
coverage and tangent hypotheses are information a proof by contradiction
may use. The logical equivalence neither supplies that proof nor rules
out such an approach. The
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil page]]
states a different sufficient premise: a fixed positive
proportion of every cap-$C$ set of at least $(1-\varepsilon)p$ points,
for some fixed $\varepsilon>0$, lies on a curve of fixed degree. With that
page's pencil count it gives the negative answer. For arcs it follows from
a reported theorem of Voloch; for caps at least three no proof of it is
supplied.

To refute the stronger arbitrary-set premise, one could exhibit an
infinite family $S_p$ with bounded cap such that, for every fixed $D$,
each degree-at-most-$D$ curve misses more than $2^{-D-3}p$ of its points
for infinitely many $p$. Such a family need not refute the
positive-proportion premise, which asks only for a fixed fraction on one
curve. It would refute the sufficient minimal-blocking premise only if
its sets were also inclusion-minimal blocking sets. Even bounded-cap
blocking sets in every prime plane would leave the other finite planes in
Problem 1159 unresolved. A finite interpolation experiment cannot
decide this uniform question: any set of $O_C(p)$ points lies on a curve
of degree $O_C(\sqrt p)$ by linear algebra, whereas the required degree
is independent of $p$.

Without the pencil count, repeated extraction of a fixed positive
proportion onto curves of fixed degree needs the quantitative control
of (4): after $t$ extractions the degree generally grows with $t$,
decreasing the source lower bound for missing lines, and the residual
blocking property cannot be assumed. With the pencil count of the
pencil page any fixed proportion suffices. Naming a curve covering most
of the points does not supply an extraction theorem. No uniform
construction, approximation theorem, or counterexample to it is obtained
here.
