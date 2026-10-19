---
name: research/leads/projective_plane_bounded_blocking/pencil_threshold
title: Points off a curve that block its missed lines number almost p
desc: A pencil count shows that a bounded-cap blocking set has at least p minus O(sqrt(p)) points off any curve of fixed degree in sufficiently large prime planes. The author-recorded proof uses tame monodromy and uniform Chebotarev; the positive-proportion extraction premise needed for a negative answer remains unproved.
created: 2026-10-17T01:51:23Z
updated: 2026-10-17T01:51:23Z
---

***

This page sharpens the exceptional-point threshold of the
[[research/leads/projective_plane_bounded_blocking/curve_reduction|conditional curve reduction]],
which belongs to the negative branch of the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking sketch]].
That reduction lets a blocking set have at most about $\alpha(Y)p$ points
off a curve $Y$, where $\alpha(Y)$ is the density of lines missing $Y$.
Counting the missed lines through each outside point raises the threshold
to about $p$, independently of $\alpha(Y)$. For unions of conics in odd
characteristic the count is proved below by quadratic character sums.
For curves of bounded degree in large prime planes it follows from
the monodromy of the projection from a point, with the source interfaces
and the restriction argument given below. The negative answer then needs a premise that a
fixed proportion of every bounded-cap set of linear size lies on a curve
of fixed degree. The arguments are author-recorded by Plasma AI, without
independent review. Nothing here proves either answer to Problem 1159.

## Setting

Let $q$ be a prime power and $Y\subset\operatorname{PG}(2,q)$ a curve
defined over $\mathbb F_q$. Write $Y(\mathbb F_q)$ for its rational points,
$L_Y$ for the set of lines containing none of them, and, for a rational
point $P\notin Y$,

$$
N_P=\#\{\ell\in L_Y:P\in\ell\}.
$$

Every line of $L_Y$ has $q+1$ points, none on $Y$, so

$$
\sum_{P\notin Y}N_P=(q+1)\,|L_Y|.
\tag{1}
$$

**Counting principle.** Let $B$ meet every line, and put
$T=B\setminus Y(\mathbb F_q)$. Each line of $L_Y$ misses $Y$ and meets
$B$, so it contains a point of $T$. Hence

$$
|L_Y|\le\sum_{P\in T}N_P.
\tag{2}
$$

The old threshold bounds every $N_P$ by $q+1$. If instead $N_P$ is close
to its average $|L_Y|(q+1)/(q^2+O(q))$ for all but boundedly many $P$,
then (2) forces $|T|$ to be at least about $q$.

The threshold $q$ cannot be raised for arbitrary blocking sets. For $q$
odd, a conic together with an external line blocks every line, and only
the $q+1$ points of that line lie off the conic. Raising it would need
the line cap, which the conic proposition below does not use.

## Unions of conics in odd characteristic

**Proposition.** Let $q$ be odd and let $Y$ be the union of $m\ge1$
distinct nondegenerate conics $Q_1,\dots,Q_m$ defined over $\mathbb F_q$.
There is a set $E_m$ of at most $\binom{2m(m-1)}2$ points such that every
rational point $P\notin Y\cup E_m$ satisfies

$$
\left|N_P-\frac{q+1}{2^m}\right|\le m\sqrt q+2m+1.
\tag{3}
$$

Consequently, if $B$ meets every line of PG$(2,q)$,
$T=B\setminus Y(\mathbb F_q)$, and $(q+1)/2^m>m\sqrt q+2m+1$, then

$$
|T|\left(\frac{q+1}{2^m}+m\sqrt q+2m+1\right)
\ge\frac{q^2+q+1-m(q+1)-|E_m|}{q+1}
\left(\frac{q+1}{2^m}-m\sqrt q-2m-1\right)-|E_m|(q+1),
\tag{4}
$$

so $|B\setminus Y(\mathbb F_q)|\ge q-2^{m+1}m\sqrt q-O_m(1)$.

*Proof.* Let $Q_i(v)=v^{\mathsf T}A_iv$ with symmetric $A_i$ and
$B_i(u,v)=u^{\mathsf T}A_iv$. Fix a rational $P\notin Y$ and a line
$\ell_1\not\ni P$; the lines through $P$ are the lines $PR$ with
$R\in\ell_1$. Parametrize $R=R(\lambda)$ by $\lambda\in\mathbb P^1(\mathbb F_q)$.
The points $sP+tR$ of $PR$ lie on $Q_i$ exactly when

$$
Q_i(P)s^2+2B_i(P,R)st+Q_i(R)t^2=0 .
$$

Since $Q_i(P)\ne0$, this binary quadratic form is nonzero. As $q$ is odd,
its rational zeros number $0$, $1$ or $2$ according as

$$
\Delta_i(R)=B_i(P,R)^2-Q_i(P)Q_i(R)
$$

is a nonsquare, zero, or a nonzero square. Replacing $R$ by $R+cP$ leaves
$\Delta_i$ unchanged and replacing $R$ by $\mu R$ multiplies it by $\mu^2$,
so its quadratic character $\chi(\Delta_i)$ depends only on the line.
Along $\ell_1$, $\Delta_i$ is a binary quadratic form in $\lambda$. Its
zeros are the tangent lines from $P$ to $Q_i$. There are exactly two of
them over $\overline{\mathbb F}_q$, because $P$ is off the conic and the
characteristic is odd, so $\Delta_i$ has two distinct roots.

A line through $P$ misses $Y(\mathbb F_q)$ exactly when
$\chi(\Delta_i)=-1$ for every $i$. When no $\Delta_i$ vanishes, the
product $\prod_i\frac12(1-\chi(\Delta_i))$ is that indicator. At the at
most $2m$ tangent parameters it lies in $[0,1]$ while the line meets $Y$
at its rational point of tangency. Expanding the product,

$$
N_P=\frac1{2^m}\sum_{I\subseteq\{1,\dots,m\}}(-1)^{|I|}S_I-\theta,
\qquad
S_I=\sum_{\lambda\in\mathbb P^1(\mathbb F_q)}
\chi\Bigl(\prod_{i\in I}\Delta_i(\lambda)\Bigr),
\qquad0\le\theta\le2m,
$$

with $S_\emptyset=q+1$. Each $f_I=\prod_{i\in I}\Delta_i$ is a binary form
of even degree $2|I|$, so its character is defined on $\mathbb P^1$. If
$f_I$ is not a constant multiple of a square, its affine restriction is
not either: a form of even degree has an even number of roots of odd
multiplicity. Weil's bound in the form of Lidl and Niederreiter,
*Finite Fields*, Theorem 5.41, used at statement level and not re-read
here, then gives
$|S_I|\le(2|I|-1)\sqrt q+1$, the $1$ accounting for the parameter at
infinity. Summing over nonempty $I$,

$$
\frac1{2^m}\sum_{I\ne\emptyset}\bigl((2|I|-1)\sqrt q+1\bigr)
=\Bigl(m-1+2^{-m}\Bigr)\sqrt q+1-2^{-m}\le m\sqrt q+1,
$$

which with $\theta\le2m$ gives (3), unless some $f_I$ with $I\ne\emptyset$
is a constant multiple of a square.

Suppose $f_I=c\,g^2$. Then every root of $f_I$ has even multiplicity. For
$|I|=1$ this is impossible, the two roots being distinct. For $|I|\ge2$,
choose $i\in I$: each of the two tangent lines from $P$ to $Q_i$ is also
tangent to some $Q_j$ with $j\in I$, $j\ne i$. Let $\mathcal T$ be the set
of lines over $\overline{\mathbb F}_q$ tangent to at least two of the
conics. In odd characteristic a nondegenerate conic is recovered from its
dual conic, so distinct conics have distinct dual conics, which meet in at
most four points. Hence $|\mathcal T|\le4\binom m2=2m(m-1)$. The two
tangents from $P$ to $Q_i$ are distinct lines of $\mathcal T$ through $P$,
so $P$ belongs to the set $E_m$ of intersection points of two distinct
lines of $\mathcal T$, which has at most $\binom{2m(m-1)}2$ elements. This
proves (3).

For (4), there are at least $q^2+q+1-m(q+1)$ rational points off $Y$, and
$N_P\ge0$ at the points of $E_m$. The lower bound in (3) is positive by
hypothesis, so (1) and (3) give

$$
|L_Y|\ge\frac{q^2+q+1-m(q+1)-|E_m|}{q+1}
\Bigl(\frac{q+1}{2^m}-m\sqrt q-2m-1\Bigr).
$$

Points of $T\cap E_m$ lie on at most $q+1$ lines, and the other points of
$T$ satisfy (3). Inserting both bounds in (2) gives (4). For fixed $m$,
dividing (4) by $(q+1)/2^m+O(\sqrt q)$ gives the stated asymptotic form.
$\square$

For a single conic, (3) holds with no exceptions. More precisely an
internal point lies on $(q+1)/2$ external lines and an external point on
$(q-1)/2$. So a point set blocking the $q(q-1)/2$ external lines has at
least $q(q-1)/(q+1)>q-2$ points, hence at least $q-1$. The old threshold
gave only about $q/2$. The exceptional set is genuinely needed when
$m\ge2$. In characteristic different from two and three, the two conics
$x^2+y^2=z^2$ and $x^2+y^2=4z^2$ have the same pair of
tangent lines from the origin, and through the origin about $q/2$ lines,
rather than $q/4$, miss both. The
[evidence entry point](evidence/main.py) checks (3), the exceptional count
and this example in small prime planes.

**Corollary.** Let $q$ be odd, $C$ and $D$ fixed, and $B$ a set meeting
every line of PG$(2,q)$ in $1$ to $C$ points. Let $F$ be a nonzero homogeneous form over $\mathbb F_q$ of
degree at most $D$ whose geometrically irreducible nonlinear components
defined over $\mathbb F_q$ are all conics. Then

$$
|B\setminus V(F)|\ge q-O_{C,D}(\sqrt q).
$$

Indeed, the line components contain at most $CD$ points of $B$ and the
other non-conic components at most $D^2$ rational points in total, as in
the [[research/leads/projective_plane_bounded_blocking/curve_reduction|curve reduction]].
Apply the proposition to the union of the conic components if it is
nonempty; otherwise $|B|\ge q+1$ gives the conclusion directly. In
particular, at cap $C$ a bounded union of lines and conics contains at
most $|B|-q+O(\sqrt q)$ points of $B$. Since a cap-$C$ blocking set has at
most about $Cq$ points, this bounds the portion of $B$ that such curves
can carry. It does not by itself contradict blocking, because nothing
forces $B$ to lie mostly on conics.

Odd characteristic is essential. In PG$(2,2^h)$ with $h\ge2$ the three
conics of the
[[research/leads/projective_plane_bounded_blocking/parity_construction|parity construction]]
meet every line in one to six points and leave no point outside their
union. There every tangent of a conic passes through its nucleus, so the
discriminant argument above has no analogue.

## The pencil count for curves of bounded degree

For general $Y$ the same count needs the distribution of rational points
in the fibres of the projection from $P$. Exceptional points cannot be
avoided, but for sets with a line cap it suffices that they lie on
boundedly many lines.

**Proposition 2.** Fix $D\ge2$. There are constants $L(D)$ and $c(D)$
with the following property. Let $p>D!$ be prime and let $Y$ be a
nonempty reduced union of geometrically irreducible curves defined over
$\mathbb F_p$, of degrees $d_i\ge2$ and total degree at most $D$. Outside
a union of at most $L(D)$ lines, every rational point $P\notin Y$
satisfies

$$
\bigl|N_P-\alpha(Y)p\bigr|\le c(D)\sqrt p,
\qquad
\alpha(Y)=\prod_i\delta_{d_i}.
\tag{5}
$$

Here $\delta_d$ is the proportion of fixed-point-free permutations in
$S_d$, as in the
[[research/leads/projective_plane_bounded_blocking/curve_reduction|curve reduction]].
One may take $L(D)=4D^4$. The constants are uniform over the coefficients
and components of $Y$.

*Proof.* Work first over $k=\overline{\mathbb F}_p$. Let $\Sigma$ be the
singular points of the whole reduced curve $Y$, including intersections
of different components. In the dual plane put

$$
\Delta=Y^\vee\ \cup\ \bigcup_{S\in\Sigma}S^*,
\qquad U=(\mathbb P^2)^*\setminus\Delta,
$$

where $S^*$ parametrizes lines through $S$ and $\Delta$ has its reduced
structure. Thus $U$ is exactly the set of lines meeting $Y$ in
$\deg Y$ distinct geometric points. The incidence morphism
$X=\{(Q,\ell):\ell\in U,\ Q\in Y\cap\ell\}\to U$ is finite étale.

The degree assumption makes each component reflexive. The precise
external input is the degree-below-characteristic consequence of Hefez's
generic-contact discussion, specified under the source interfaces below.
In odd characteristic reflexivity gives simple generic tangency.
Distinct reflexive components have distinct dual curves, by biduality.
A generic tangent to one component therefore has contact exactly two
there and meets every other component transversally, away from all
singular points. The whole union is quasireflexive in Entin's sense.
His Theorem 2 gives geometric monodromy

$$
G=\prod_i S_{d_i}.
$$

In the plane case its mechanism can be seen directly. For each component,
the off-diagonal fibre square of the incidence morphism is birational
to $Y_i\times Y_i$: two distinct points determine their line. This gives
double transitivity on that component's fibre. A simple tangent on
$Y_i$ gives an inertia element which transposes two sheets of that
component and fixes the sheets of every other component. Conjugating
this element using double transitivity gives every transposition
supported on the $i$th factor. Doing this for each $i$ gives the product,
without inferring joint independence merely from pairwise independence.

We next specify the exceptional lines. A generic polar of a reduced
degree-at-most-$D$ plane curve has no component in common with it, so
Bézout bounds $|\Sigma|$ by $D(D-1)$. The same polar argument bounds
$\deg Y_i^\vee$ by $d_i(d_i-1)$. Consequently

$$
b:=\deg\Delta\le 2D(D-1).
$$

The reduced plane curve $\Delta$ has at most $b(b-1)$ singular geometric
points, again by a generic polar. Let $E$ be the union, in the original
plane, of the lines dual to those points. It has at most $4D^4$
components.

Fix $P\notin Y\cup E$. Its pencil $P^*$ misses
$\operatorname{Sing}\Delta$. It is not a component $S^*$ of $\Delta$,
because that would say $P=S\in Y$. None of the dual curves $Y_i^\vee$
is a line, by reflexivity and $d_i\ge2$. At a smooth point $\ell$ of
$Y_i^\vee$, biduality identifies its tangent with $Q^*$ for some
$Q\in Y_i$. Thus $P^*$ can be tangent to this dual curve only if $P=Q$,
also excluded. Its intersections with the line components $S^*$ are
transverse. We have proved that $P^*$ meets $\Delta$ only transversally
at smooth points.

Let $\pi:\Omega\to(\mathbb P^2)^*$ be the normalization in the function
field of the connected geometric Galois closure over $U$. The surface
$\Omega$ is normal, integral and projective, and $\pi$ is finite. Write
$Z=\pi^{-1}(P^*)$ as a scheme. It is an effective ample Cartier divisor:
it is the pullback of a line under a finite surjection.

Here is the needed connectedness argument. A normal surface is
Cohen--Macaulay and has a dualizing sheaf $\omega_\Omega$. Serre duality
and Serre vanishing give, for sufficiently large $n$,

$$
H^1(\Omega,\mathcal O_\Omega(-nZ))
\cong H^1(\Omega,\omega_\Omega(nZ))^\vee=0.
$$

In the exact sequence for the effective divisor $nZ$, the restriction
of global functions therefore gives
$H^0(nZ,\mathcal O_{nZ})=k$: global functions on the integral projective
surface are constant, and a constant vanishing on $nZ$ is zero.
A disconnected $Z$ would give a nontrivial idempotent on $nZ$.
Thus $Z$ is connected.

It is also smooth. Over $U$, $\pi$ is étale, so this is immediate there.
Its Galois group has order $\prod_i d_i!\le D!<p$, making the cover tame
at every component of $\Delta$. Near a smooth point of $\Delta$,
Abhyankar's lemma expresses the normalization, étale locally, as a
disjoint union of covers obtained by adjoining $z$ with $z^e=t$, where
$t=0$ defines $\Delta$ and $p\nmid e$. Since $P^*$ is transverse, choose
a second local parameter $s$ with $P^*=(s=0)$. The restriction is
locally $z^e=t$ over this smooth line, hence has regular local parameter
$z$. This proves smoothness everywhere on $Z$.

A connected smooth curve is irreducible. Removing the finitely many
points above $\Delta$ leaves a connected Galois cover of
$P^*\cap U$ of degree $|G|$. Therefore the restricted incidence cover
has geometric monodromy $G$. The arithmetic group preserves each
$Y_i$, since every component is defined over $\mathbb F_p$, and so is
a subgroup of $\prod_iS_{d_i}$. It contains the geometric group, already
equal to that product. The two groups coincide.

Finally apply Entin's Theorem 3 to the incidence cover restricted to
$P^*\cap U$. Its base is a geometrically irreducible open subset of
$\mathbb P^1$. Its morphism complexity is bounded in terms of $D$:
the equations for $Y$, incidence, membership in $P^*$ and exclusion
of $\Delta$ have bounded degree in fixed-dimensional projective
products. The arithmetic-to-geometric quotient is trivial, so the
theorem's constant-field factor is one. Summing its estimate over the
conjugacy classes having no fixed point on any component gives

$$
\#\{\ell\in(P^*\cap U)(\mathbb F_p):
           \ell\cap Y(\mathbb F_p)=\varnothing\}
=\alpha(Y)p+O_D(\sqrt p).
$$

There are at most $b$ omitted pencil parameters. Adding any of them
which also miss the rational points changes the count by $O_D(1)$,
proving (5).

The exceptional lines were defined over $k$. A non-rational geometric
line contains at most one $\mathbb F_p$-point; choose any rational line
through that point if it exists. This replaces $E$ by at most the same
number of rational lines covering all its rational points, as required.
$\square$

The restriction proof includes singular curves. A projection of a branch
of multiplicity at least three can have ramification index at least
three for every centre; avoiding flex tangents does not make all its
inertia transpositions. The proof uses transpositions to determine the
monodromy of the whole family and uses tame local models, allowing
higher ramification indices, to restrict that family to the pencil.

### Source interfaces and reading depth

These are external premises of the author-recorded proof, not claims of
independent verification.

- Hefez, *Non-reflexive curves*, Compositio Math. 69 (1989), Section 2,
  equation (2.1) and the consequence at the top of printed p. 5
  ([article](https://www.numdam.org/item/CM_1989__69_1_3_0/)):
  a nonlinear irreducible curve of degree less than the characteristic
  is reflexive. The consequence and its generic-contact context were
  inspected at statement level. The original generic-contact proof,
  attributed there to Hefez and Kleiman, and the Segre--Wallace
  separability criterion were not reconstructed.
- Entin, *Monodromy of hyperplane sections of curves and decomposition
  statistics over finite fields*,
  [arXiv:1805.05454v3](https://arxiv.org/abs/1805.05454v3):
  Proposition 2.1 identifies reflexivity with quasireflexivity in odd
  characteristic; Theorem 2 gives the full product monodromy for a
  quasireflexive union; Theorem 3 counts Frobenius classes in finite
  étale covers with error uniform in morphism complexity.
  Sections 2--5, including the monodromy and twisting proofs, were
  read in the v3 TeX. The cited general contact, monodromy-action,
  descent and Lang--Weil theorems remain external inputs. No comparison
  with the journal edition was made.
- The Stacks Project,
  [Lemma 58.31.5, tag 0EYG](https://stacks.math.columbia.edu/tag/0EYG):
  a finite étale cover tame in codimension one along a regular
  effective Cartier divisor is étale locally a disjoint union of the
  standard root covers. Its statement and proof were read. It is used
  only near the smooth points of $\Delta$, where the base is a regular
  surface and the branch divisor is regular.
- The Stacks Project,
  [Lemmas 30.17.1--2, tag 01XO](https://stacks.math.columbia.edu/tag/01XO),
  supply Serre vanishing and preservation of ampleness by a finite
  surjective pullback. Their statements and proofs were read.
  [Lemma 48.27.5 and Remark 48.27.6, tag 0FVU](https://stacks.math.columbia.edu/tag/0FVU),
  supply Serre duality on a proper Cohen--Macaulay scheme. Their
  statements and displayed derivations were read; the underlying
  duality theory was not reconstructed. Here the scheme is the
  normal projective surface $\Omega$, the sheaf being dualized is
  the invertible sheaf $\mathcal O_\Omega(-nZ)$, and its dimension is two.

For completeness, summing (5) through (1) gives the global lower bound

$$
|L_Y|\ge\alpha(Y)p^2-O_D(p^{3/2}).
\tag{6}
$$

Indeed, at most $D(p+1)$ rational points lie on $Y$, by counting their
incidences with all lines, none of which is a component of $Y$.
At most $L(D)(p+1)$ lie on the exceptional lines. Thus
$p^2-O_D(p)$ points contribute at least $\alpha(Y)p-c(D)\sqrt p$ each
to (1), which proves (6) for large $p$. This also recovers the lower
bound needed from the global source estimate.

For conics the first proposition gives the stronger conclusion, with
finitely many exceptional points and explicit constants, in every odd
characteristic, by an elementary argument. For cubics the
[evidence entry point](evidence/main.py) computes every $N_P$ at $p=211$
for a Fermat, a nodal, a cuspidal and a smooth cubic. All but $3$, $3$, $1$
and $0$ points off the curve satisfy $|N_P-p/3|\le2\sqrt p$. The
exceptions of the Fermat cubic are the three coordinate points, from which
the projection is a cyclic cover. They lie on its flex tangents, such as
$x+\omega y=0$ through $(0:0:1)$ with $\omega^2+\omega+1=0$, which are
rational because $211\equiv1\pmod3$, as Proposition 2 permits. For a cubic
with a conic and for two cubics, the same bound with $\alpha=1/6$ and
$1/9$ fails at only $2$ and $0$ points. These main terms are the products
of the component densities; the empirical constant $2$ and the exact
exception counts are finite observations, not consequences of Proposition 2.
The two-cubic example has total degree six and $211<6!$, outside that
proposition's convenient sufficient characteristic range. None of these
examples verifies the uniform estimate.

## The sharpened reduction

**Theorem A.** Fix positive integers $C,D$. For all sufficiently large primes $p$,
every set $B\subseteq\operatorname{PG}(2,p)$ meeting each line in $1$ to
$C$ points, and every nonzero homogeneous form
$F\in\mathbb F_p[X,Y,Z]$ of degree at most $D$, satisfy

$$
|B\setminus V(F)|\ge p-O_{C,D}(\sqrt p).
$$

*Proof.* Discard the line components of $F$ and its
components that are not geometrically irreducible, at a cost of at most
$CD+D^2$ points of $B$, as in the curve reduction. Let $Y$ be the
remaining union and $T=B\setminus Y(\mathbb F_p)$. If $Y$ is empty,
$|T|=|B|\ge p+1$. Otherwise Proposition 2 summed through (1), or the
source estimate of the curve reduction, together with the bound
$\alpha(Y)\ge1/M(D)$ of that page, gives
$|L_Y|\ge\alpha(Y)p^2(1-O_D(p^{-1/2}))$. At most $CL(D)$ points of $T$ lie
on the exceptional lines of Proposition 2, and each lies on at most $p+1$
lines. So (2) gives

$$
\alpha(Y)p^2\bigl(1-O_D(p^{-1/2})\bigr)
\le|T|\bigl(\alpha(Y)p+c(D)\sqrt p\bigr)+CL(D)(p+1).
$$

Dividing by $\alpha(Y)p$, which is at least $p/M(D)$, gives
$|T|\ge p-O_{C,D}(\sqrt p)$. Adding back the discarded components costs
$O_{C,D}(1)$. $\square$

For unions of lines and conics the corollary above proves Theorem A by
the elementary argument, in every odd order.

**Theorem B.** Fix a cap $C$ and assume the following.

**Positive-proportion extraction $\mathrm{WE}_C$.** There are
$\varepsilon\in(0,1)$, an integer $d\ge1$ and $0<\eta\le1$ such that, for all
sufficiently large primes $p$, every $S\subseteq\operatorname{PG}(2,p)$
meeting each line in at most $C$ points and having
$|S|\ge(1-\varepsilon)p$ has at least $\eta|S|$ points on some curve defined over $\mathbb F_p$ of
degree at most $d$.

Then no set in PG$(2,p)$ meets every line in $1$ to
$C$ points once $p$ is large. If $\mathrm{WE}_C$ holds for every $C$, then
$c(\operatorname{PG}(2,p))\to\infty$ along the primes, and Problem 1159
has a negative answer.

*Proof.* Let $B$ be such a set and $R_0=B$. While
$|R_j|\ge(1-\varepsilon)p$, apply $\mathrm{WE}_C$ to $R_j$, which still
meets each line in at most $C$ points, to obtain $F_{j+1}$, and put
$R_{j+1}=R_j\setminus V(F_{j+1})$. Then $|R_j|\le(1-\eta)^j|B|$ and
$|B|\le(C+1)p$, by counting incidences, so the process stops after at
most $t=\lceil\log((C+1)/(1-\varepsilon))/\eta\rceil$ steps, a number
independent of $p$. If it stops at step $j\le t$, the product
$F=F_1\cdots F_j$ has degree at most $td$, and
$|B\setminus V(F)|=|R_j|<(1-\varepsilon)p$. This contradicts
Theorem A at degree $td$ once $p$ is large. $\square$

Compared with the repeated-extraction test of the curve reduction, the
contraction condition $M(d)(1-\eta)<1$ disappears: any fixed $\eta>0$
suffices, because the threshold for exceptional points no longer
decreases as the total degree grows. The residual hypothesis also
disappears. Each residual keeps the cap and its size stays at least
$(1-\varepsilon)p$ until the iteration stops, and $\mathrm{WE}_C$ is asked
of arbitrary bounded-cap sets, not of blocking sets.

### A relative invariant with tangents

A weaker extraction premise suffices. In the preceding proof each
residual $R_j$ meets every line missing
$Y_j=V(F_1\cdots F_j)$, because $B$ meets every line. To use that weaker
premise, the quantifiers must still be uniform: choose
$\varepsilon,d,\eta$ first and then
$t=\lceil\log((C+1)/(1-\varepsilon))/\eta\rceil$. Require the extraction
statement for each $0\le j<t$, every degree-at-most-$jd$ curve $Y_j$ (with $Y_0=\varnothing$),
and every cap-$C$ set $R_j$ of size at least $(1-\varepsilon)p$
blocking the lines missing $Y_j$, with one threshold for $p$.
Allowing $d$ or $\eta$ to deteriorate with $j$ without a termination
bound does not establish this premise.

There is a stronger valid invariant which retains minimality and
tangents, provided the covered **points**, not just their containing
curve, stay in the state. Initially delete to an inclusion-minimal
blocking set $B$, and keep this same $B$ throughout. Put

$$
A_j=B\cap Y_j,\qquad R_j=B\setminus Y_j,\qquad
\mathcal L(A_j)=\{\ell:\ell\cap A_j=\varnothing\}.
$$

Then $R_j$ is an inclusion-minimal blocking set for the line family
$\mathcal L(A_j)$. It blocks that family because $A_j\cup R_j=B$.
For each $P\in R_j$, a tangent to the original minimal $B$ avoids $A_j$
and meets $R_j$ only at $P$, proving relative minimality. The line cap
holds for the union $A_j\cup R_j$, as well as for the residual.

Thus one can replace $\mathrm{WE}_C$ by an extraction theorem for these
triples $(Y_j,A_j,R_j)$, with the same uniform constants through
$j<t$. The required curve must capture a fraction of $R_j$, not merely
a fraction of $A_j\cup R_j$. An extraction theorem stated only for
minimal blocking sets does not imply this: its captured points could
all belong to $A_j$.

The family $\mathcal L(A_j)$ includes the lines which meet $Y_j$ only
outside $B$. Deleting points merely because the lines missing the
whole curve remain blocked can uncover such a line. Likewise a tangent
to $B$ at a residual point need not miss the whole curve. The two
relative line families cannot be interchanged.

## Standing

The first proposition and its corollary are author-recorded proofs
resting on Weil's bound. Proposition 2 and Theorem A are
author-recorded proofs with the external interfaces and reading depth
specified above. Theorem B proves a conditional implication from
$\mathrm{WE}_C$. None has independent review, and no result here
settles Problem 1159.

$\mathrm{WE}_C$ is the remaining structural premise. Nothing here
proves it for any $C\ge3$, and no counterexample to it is supplied.
It concerns arbitrary bounded-cap sets, so it is not vacuous: a conic
and unions of boundedly many nonlinear curves give examples of sets
to which it applies for suitable caps. The heuristic that bounded
line intersections require structure does not show that the structure
is algebraic.

Given the source estimate, restricting the curve reduction's
approximation premise to inclusion-minimal cap-$C$ blocking sets is
logically equivalent to their nonexistence in large prime planes.
The forward direction is the counting contradiction; the reverse
direction is vacuity. This equivalence does not rule out a useful
proof by contradiction exploiting the covering and tangent
hypotheses. It identifies what that restricted approximation theorem
would have to establish, without supplying it.

Because Theorem A leaves about $p$ points off every curve, extraction is
needed only for sets of at least $(1-\varepsilon)p$ points, with any fixed
$\varepsilon>0$. For arcs this case is known. Ball and Lavrauw, *Arcs in
finite projective spaces*
([arXiv:1908.10772v2](https://arxiv.org/abs/1908.10772v2)), Theorem 52,
state that in PG$(2,p)$ with $p$ prime an arc of more than
$\frac{44}{45}p+\frac89$ points lies on a conic, attributing it to Voloch,
J. Geom. 38 (1990), 198–200. Only the statement in the survey's extracted
text was read; the original was not. So $\mathrm{WE}_2$ holds with
$\varepsilon<1/45$, $d=2$ and $\eta=1$, but cap-two blocking sets are
already excluded by L27. For $C\ge3$ no comparable theorem is known to
us. Segre's method behind such results uses the few tangent lines of a
nearly maximal arc; a set of about $p$ points with cap $C\ge3$ can have a
positive proportion of lines of every load through each of its points,
and no proof of $\mathrm{WE}_C$ is supplied here. Random sets of linear size have line
intersections growing with $p$, so they supply no test cases.

## Next discriminating test

The decisive input is $\mathrm{WE}_C$, or the uniform relative
blocking version above, for every fixed $C$ (an unbounded sequence of
caps would also suffice). Together with Theorem A it would give a
negative answer to Problem 1159. A result only for small caps would
raise lower bounds without answering the problem.

A direct attack can instead exploit the product of the dual covering
lines; the
[[research/leads/projective_plane_bounded_blocking/covering_polynomial|covering-polynomial account]]
retains its exact identities and the point where the freeness route
fails to produce a fixed-degree extraction. No implication from those
identities to $\mathrm{WE}_C$ is known here.
