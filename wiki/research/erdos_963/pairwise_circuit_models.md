---
name: research/erdos_963/pairwise_circuit_models
title: 'Pairwise circuit data and the ternary projective model'
desc: With free signs and order the realization cone only forbids implied relations of support at most two; sign-free pairwise circuit data stops at (3^d-1)/2, attained by the ternary projective model; positive orientation excludes that model and gives the target for d at most 3. The target remains unresolved.
tags: []
sources: []
created: 2026-10-15T11:06:18Z
updated: 2026-10-15T11:06:18Z
---

# Pairwise circuit data and the ternary projective model

***

This note asks whether the ordered-realization criterion of
[[research/erdos_963/collision_trade_method|the collision-trade note]], applied
to overlapping circuits, can make the short and long circuits forced in a
hypothetical counterexample incompatible. Through pairs of circuits whose
orientations are free it cannot: all such data, including every restriction on
mixed-sign overlaps, is satisfied by a model with $(3^d-1)/2$ points that
contains circuits of every size. A common increasing positive realization
requires one choice of element signs making every circuit two-sided, and the
model already fails this necessary condition. Orientation of single relations
in a common order,
with unique completion, already gives the target for $d\le3$; whether the
ordered pairwise conditions imply it for larger $d$ is open. The arguments
below are Plasma AI's author-recorded deductions; none proves or refutes the
target. The sign-free countermodel is not a model of the global cone condition.

Notation follows the collision-trade note. $P=\{p_1<\cdots<p_n\}$ is a set of
positive reals, $d=d(P)$ is the maximum cardinality of a dissociated subset,
$L$ is the real span of the ternary relations of $P$, and
$\tau(u)_j=\sum_{i\ge j}u_i$. A **circuit** is an inclusion-minimal support of
a nonzero ternary relation; its relation $u_C\in\{\pm1\}^C$ is unique up to
sign. Every ternary vector of $L$ is a relation, since $L\subseteq p^\perp$.

## The realization cone with free signs and order

**Proposition 1.** Let $L\subseteq\mathbb R^n$ be spanned by integer vectors.
The following are equivalent.

1. For some permutation $\pi$ of the coordinates and some signs
   $\sigma\in\{\pm1\}^n$, the subspace $\pi\sigma L$ satisfies the criterion
   $\tau(\pi\sigma L)\cap\mathbb R^n_{\ge0}=\{0\}$.
2. $L$ contains no nonzero ternary vector whose support has at most two
   elements.

When the second condition holds, there are signs $\sigma$ and distinct positive
integers $|a_1|,\ldots,|a_n|$ whose ternary relations are exactly the vectors
$\sigma t$ with $t$ a nonzero ternary vector of $L$. In particular the
dependent subsets of that positive set are exactly the subsets of $[n]$ that
support a nonzero ternary vector of $L$.

*Proof.* If increasing positive reals annihilate $\pi\sigma L$, undoing $\pi$
and $\sigma$ gives a vector $a\perp L$ whose coordinates are nonzero and have
distinct absolute values. A ternary vector $\pm e_i$ in $L$ would force
$a_i=0$, and $\pm e_i\pm e_j$ would force $|a_i|=|a_j|$.

Conversely, $L^\perp$ is a rational subspace and $(L^\perp)^\perp=L$. Under
the second condition the subspaces $L^\perp\cap\{x_i=0\}$ and
$L^\perp\cap\{x_i=\pm x_j\}$ are proper, as is $L^\perp\cap r^\perp$ for every
ternary $r\notin L$. Choose a rational point $a\in L^\perp$ outside their
finite union and clear denominators. Put $\sigma_i=\operatorname{sign}a_i$.
The integers $|a_i|$ are positive and distinct. A ternary $t$ is a relation of
$(|a_i|)$ exactly when $\sigma t\perp a$, that is, when $\sigma t\in L$. Sorting
the $|a_i|$ gives $\pi$, and the criterion holds by its necessity half,
summation by parts. $\square$

Thus, once signs and order are free, the cone criterion says only that the
relation space implies no relation of the form $e_i$ or $e_i\pm e_j$. This is
the column condition of [[research/erdos_963/corank_one|the corank-one note]]
(distinct nonzero columns with no antipodal pair) in dual form. Thus the
sign-free realization question is exactly whether the full real span contains
one of these forbidden vectors. For prescribed signs and order, merely making
every circuit two-sided is necessary but not sufficient: the cone condition
still applies to all real linear combinations. The sections below keep these
distinct requirements separate.

## Two-circuit spans

**Proposition 2.** Let $u$ and $v$ be the relations of distinct circuits $C$
and $D$, and put $I=C\cap D$. Fix an orientation of $v$ and put

$$
I_+=\{i\in I:u_i=v_i\},\qquad I_-=\{i\in I:u_i=-v_i\}.
$$

The nonzero ternary vectors of $\operatorname{span}(u,v)$ are exactly:

- $\pm u$, $\pm v$ and $\pm u\pm v$ when $I$ is empty;
- $\pm u$, $\pm v$ and $\pm(u-v)$ when $I$ is nonempty and $I_-$ is empty, a
  **compatible** pair (the case of empty $I_+$ is the same after reversing
  $v$);
- $\pm u$ and $\pm v$ only, when $I_+$ and $I_-$ are both nonempty, a
  **mixed** pair.

*Proof.* Neither circuit contains the other, so $C\setminus D$ and
$D\setminus C$ are nonempty. On them $\alpha u+\beta v$ equals $\alpha u$ and
$\beta v$, so a ternary combination has $\alpha,\beta\in\{-1,0,1\}$. On $I_+$
and $I_-$ it equals $(\alpha+\beta)u$ and $(\alpha-\beta)u$, which must also be
ternary when those sets are nonempty. Enumerating the eight nonzero pairs
$(\alpha,\beta)$ gives the list. $\square$

By Proposition 1 applied to $\operatorname{span}(u,v)$, two circuits restrict
each other only when a listed vector has support at most two. The circuits have
at least three points, and $C\cup D$ has at least six when they are disjoint.
For a compatible pair, $|C\triangle D|=|C\setminus D|+|D\setminus C|\ge2$, with
equality exactly when $C=T\cup\{x\}$ and $D=T\cup\{y\}$ and the relations agree
on $T$ up to sign: a **compatible exchange pair**. Every other pair is realized
by positive integers having exactly the relations of its span. Consequently:

1. Circuits of different sizes never restrict each other pairwise. In
   particular a short circuit and a long circuit do not, whatever their
   overlap and relative signs.
2. A mixed overlap of any size imposes no pairwise restriction.
3. The only pairwise restriction is unique completion: for an $(s-1)$-set $T$
   and a sign pattern on $T$, at most one point completes a circuit. This is
   precisely the input of the circuit-covering inequality (2) of the
   collision-trade note. A compatible pair also forces a relation on
   $C\triangle D$, so that set contains a circuit. This closure is a further
   constraint on the whole family, but the model below satisfies it too.

## The ternary projective model

Let $X$ be a set of representatives of the $(3^d-1)/2$ classes $\{\pm x\}$ of
nonzero vectors of $\mathbb F_3^d$. Over $\mathbb F_3$ the coefficients
$-1,0,1$ are all the coefficients, so the ternary relations on $X$ are its
linear relations, and its circuits are those of the projective geometry
$\mathrm{PG}(d-1,3)$, each with its coefficient vector.

**Theorem 3.**

1. Every $(d+1)$-subset of $X$ supports a circuit, and a basis supports none.
2. Each circuit has one relation up to sign; no two circuits form a compatible
   exchange pair; and for every compatible pair the set $C\triangle D$ contains
   a circuit.
3. For every $s$ with $3\le s\le d+1$ there is a circuit with $s$ points.
4. $|X|=(3^d-1)/2$, which is at least $2^d$ for every $d\ge2$.

Conversely, let a family of signed sets with at least three points each be
given on $[n]$, with no two members forming a compatible exchange pair, such
that every $(d+1)$-subset contains a member and some $d$-subset contains none.
Then $n\le(3^d-1)/2$.

*Proof.* For the first item, a subset is dependent over $\mathbb F_3$ exactly
when it supports a nonzero ternary relation. Two relations on one circuit that
are not proportional have a combination vanishing at a point of the circuit,
leaving a relation on a proper subset; the only scalars are $\pm1$. If
$C=T\cup\{x\}$ and $D=T\cup\{y\}$ have relations agreeing on $T$, then
$u_xx=-\sum_{t\in T}u_tt=v_yy$, so $x=\pm y$, which is impossible for distinct
representatives. For a compatible pair, $u-v$ is an integer vector with entries
in $\{-1,0,1\}$ that vanishes on $C\cap D$; it is a nonzero relation, so its
support contains a circuit. For the third item take
$e_1,\ldots,e_{s-1},e_1+\cdots+e_{s-1}$: they are dependent, and every $s-1$ of
them are independent.

For the converse, let $D$ be a $d$-subset containing no member. For each
$x\notin D$, the set $D\cup\{x\}$ contains a member $C_x$, which must contain
$x$. Normalize its relation to have coefficient $1$ at $x$ and let
$\varepsilon_x\in\{-1,0,1\}^D$ be minus its restriction to $D$; its support has
at least two points. If $\varepsilon_x=\pm\varepsilon_y$ for $x\ne y$, then
$C_x$ and $C_y$ are a compatible exchange pair. Hence $x\mapsto\pm\varepsilon_x$
is injective into the classes of ternary vectors on $D$ with support at least
two, and

$$
n-d\le\frac{3^d-1}2-d. \qquad\square
$$

So $(3^d-1)/2$ is the exact maximum permitted by pairwise circuit data when
orientations are free, and it is the trivial ternary bound. The model satisfies
the circuit-covering inequality (2) because that inequality uses only such
data. For $d\ge9$ it has both a circuit of at most six points and circuits with
more than $\theta(d+1)$ points, and it has $n\ge2^d$. An overlap restriction
derived from pairs of circuits with free orientation, including every
restriction on mixed overlaps, holds in this model, so it cannot make the
forced short and long circuits incompatible.

For $d=2$ the model is four signed triples on four points. With
$x_1=(1,0)$, $x_2=(0,1)$, $x_3=(1,1)$ and $x_4=(1,2)$, three of its relations
are

$$
u_1=e_1+e_2-e_3,\qquad u_2=e_1-e_2-e_4,\qquad u_3=e_1+e_3+e_4,
$$

and every two of its four triples meet in a mixed pair of points. Over the
reals, $u_1+u_2+u_3=3e_1$, so these three circuits imply $p_1=0$.

## Where characteristic zero enters

As sign-free data, the model differs from a real set only through combinations
of at least three circuits. Two such combinations are the following.

**Lemma 4 (mixed overlaps).** For a mixed pair, put
$t_\pm=u|_{C\setminus D}\pm v|_{D\setminus C}$. Then

$$
u\pm v=2u|_{I_\pm}+t_\pm .
$$

For a real set, no ternary vector $t_\pm+c\,u|_{I_\pm}$ with
$c\in\{-1,0,1\}$ is a relation. In the projective model $t_\pm-u|_{I_\pm}$
is always a relation.

*Proof.* The vector $u|_{I_\pm}$ is a nonzero ternary vector on a proper subset
of the circuit $C$, so it is not in $L$. Since
$t_\pm+c\,u|_{I_\pm}=(u\pm v)+(c-2)u|_{I_\pm}$, it lies in $L$ only for
$c=2$. Modulo three, $2\equiv-1$. $\square$

Thus replacing the coefficient two by minus one gives a ternary relation over
$\mathbb F_3$, whose support contains a circuit, but never a relation over
the reals. Minimality of the whole new support is not asserted. The relations
$u$, $v$ and $w=t_+-u|_{I_+}$ satisfy
$u+v-w=3u|_{I_+}$; the four triples above are an instance.

**Lemma 5 (completion paths).** Fix a set $U$ and a sign vector $\sigma$ on
$U$ up to sign. Join $x$ and $y$ outside $U$ when $U\cup\{x,y\}$ is a circuit
whose relation, normalized to restrict to $\sigma$ on $U$, is
$\sigma+ae_x+be_y$. For a real set this graph is a disjoint union of paths.

*Proof.* Unique completion allows at most one edge at $x$ for each sign $a$,
and two edges at $x$ carry opposite signs there. Along a cycle
$x_1,\ldots,x_k$ with relations $u_i=\sigma+a_ie_{x_i}+b_ie_{x_{i+1}}$ this
gives $b_{i-1}=-a_i$, so $\sum_iu_i=k\sigma\in L$. But $\sigma$ is a nonzero
ternary vector on a proper subset of a circuit. $\square$

In positive terms every edge joins a pair with $x+y=G$ or $|x-y|=G$, where
$G=|\sigma\cdot p_U|$. Along a path the signed values $a_ip_{x_i}$ change by
$\sigma\cdot p_U$ at each step, so a path consists of the absolute values of
consecutive terms of an arithmetic progression. In the projective model the
progressions have period three and the graphs contain triangles.

Count each circuit of size $s$ once for each of its $\binom s2$ pairs, over the
$2^{s-3}\binom n{s-2}$ choices of $U$ and $\pm\sigma$, with at most $n-s+1$
edges in a forest on $n-s+2$ vertices. Following the derivation of (2) then
gives

$$
\sum_{s=3}^{R}\frac{2^{s-2}\binom{d+1}{s}}{n-s+2}\ge1,
$$

improving the denominator $n-s+1$ of (2). At $d=2$ this gives $n\le3$, which
is sharp, whereas (2) allows the four-point model. At $d=3$ it gives
$n\le13$ instead of $14$; the true maximum is six. Beyond small $d$ the gain is
a factor $(n-s+1)/(n-s+2)$. It is another separate support count and does not
separate the forced short and long circuits.

## What positive orientation adds

In a positive real set, each circuit relation has both sides nonempty. For a
family of signed sets, call a choice of element signs a **positive
orientation** if it makes every relation two-sided.

**Proposition 6.** For $d\ge2$ the projective model has no positive
orientation.

*Proof.* Changing element signs replaces $X$ by another set $R$ of
representatives. Suppose every circuit relation on $R$ is two-sided. For
distinct $x,y\in R$, the vector $x+y$ is nonzero and not $\pm x$ or $\pm y$;
let $r=\pm(x+y)$ be its representative. The triple $\{x,y,r\}$ is a circuit
with relation $x+y\mp r=0$, one-sided when $r=-(x+y)$. Hence $x+y\in R$. Take
distinct $x,y\in R$. Then $a=x+y\in R$, so $a+y=x-y$ and $a+x=y-x$ also lie in
$R$. These are opposite nonzero vectors, a contradiction. $\square$

The ordered form of pairwise realizability is therefore strictly stronger.
Its data are a linear order of $[n]$ and a positive relation for each member of
the family. Its conditions are that every two members are annihilated by one
increasing positive vector, and that the support of the eliminated relation of
a compatible pair contains a member. For a single relation $u$ the first
condition says that $\tau(u)$ takes both signs; for a three-point circuit it
says that the largest element is the sum of the other two. For a pair it says
that the points $(\tau(u)_j,\tau(v)_j)$, $1\le j\le n$, positively span
$\mathbb R^2$.

Orientation of single relations already gives a bound well below the
projective model. Put

$$
f(k)=2^{k-1}-\binom k{\lfloor k/2\rfloor}
+[k\text{ even}]\,\frac{1}{k/2+1}\binom k{k/2}.
$$

**Proposition 7 (greedy set from the top).** Fix a linear order of $[n]$ and a
family of members with at least three points each, each with a relation whose
tail profile takes both signs. Suppose that no two members form a compatible
exchange pair and that every $(d+1)$-subset contains a member. Then

$$
n\le d+\sum_{k=2}^{d}\binom dk f(k).
$$

*Proof.* Scan $[n]$ downward from the largest position, keeping a set $G$ that
contains no member and adding each position whose addition keeps it so. Then
$|G|\le d$. A rejected position $x$ completes a member $C_x$ whose other points
lie in $G$ above $x$, so $x$ is the least point of $C_x$. Put
$S=C_x\setminus\{x\}$ and $k=|S|\ge2$, and read the signs of the relation on
$S$ from the top down as a walk, normalized to start with $+1$. Apart from
zeros above $S$, the tail profile takes the partial sums $t_k=1,\ldots,t_1$ of
this walk above $x$, and the value $t_1\pm1$ at and below $x$. If the walk
stays nonnegative and ends at $t_1\ge1$, every value is nonnegative and the
relation is not satisfiable. Of the $2^{k-1}$ walks,
$\binom k{\lfloor k/2\rfloor}$ stay nonnegative, and those among them that
end at zero, a Catalan number when $k$
is even, remain satisfiable with the sign $-1$ at $x$. So $f(k)$ classes are
available on each $k$-subset of $G$. Unique completion makes $x\mapsto(S,\pm$
signs$)$ injective, and the right side increases with $|G|$. $\square$

The bound equals $3$ and $7=2^d-1$ for $d=2,3$, where sign-free pairwise data
allow $4$ and $13$ and real sets reach $3$ and $6$. Thus positive orientation
of single relations, with unique completion, proves the target for $d\le3$. For
$d=4,5$ the bound is $18$ and $51$, against the targets $15$ and $31$ and the
proof sketch's bounds $14$ and $42$. Asymptotically it is
$\tfrac12 3^d(1-\Theta(d^{-1/2}))$: the walk restriction removes only a
polynomial fraction of the ternary classes, so this count cannot reach $2^d$.
This is a limitation of the displayed count. It does not construct a family
attaining it, or prove that the single-relation ordered assumptions themselves
fail to imply the target. The unused requirement that all $(d+1)$-subsets,
including those with several rejected points, contain a member could impose
further restrictions.

Two further facts are proved.

1. **One-sided circuits.** The bound $n\le2^d-1$ for one-sided circuits in the
   collision-trade note holds under the ordered conditions, with $D$ chosen
   to minimize the sum of the positions of its elements. Its proof uses only
   single relations (a root is the largest element of its circuit), unique
   completion, and the closure
   that places a circuit inside the elimination support of a compatible pair.
2. **Order constrains pairs.** Proposition 2 permits pairs that the order
   excludes. With positions $1<\cdots<6$, the relations $p_3=p_1+p_2$ and
   $p_4+p_6=p_1+p_2+p_5$ are each satisfiable and agree on $\{1,2\}$, with a
   symmetric difference of four points. Under the first,
   $p_4+p_6-p_1-p_2-p_5=(p_4-p_3)+(p_6-p_5)>0$, so no increasing positive
   vector satisfies both.

For a three-point circuit the pair condition can be stated exactly. This is
the quantitative overlap restriction that the cone imposes between a short
circuit and any other circuit.

**Proposition 8.** Let $u$ be the relation $p_c=p_a+p_b$ with $a<b<c$, and let
$v$ be the relation of another member, satisfiable on its own. No increasing
positive vector satisfies both if and only if, for $\epsilon=1$ or
$\epsilon=-1$, the profile $w=\epsilon\tau(v)$ is nonnegative on $(a,b]$ and
on $(c,n]$, and

$$
\min_{j\le a}w_j+\min_{b<j\le c}w_j\ge0.
$$

*Proof.* The profile $\tau(u)$ equals $-1$ on $[1,a]$, $0$ on $(a,b]$, $1$ on
$(b,c]$ and $0$ above $c$. Infeasibility means
$\alpha\tau(u)+\beta\tau(v)\ge0$ for some $(\alpha,\beta)\ne0$, the
combination being nonzero because $u,v$ are independent and $\tau$ is
injective. Here $\beta\ne0$, since
$\tau(u)$ takes both signs. Dividing by $|\beta|$ and putting
$\epsilon=\operatorname{sign}\beta$ and $\lambda=\alpha/|\beta|$, the
condition reads $w\ge0$ on $(a,b]$ and above $c$, $w\ge\lambda$ on $[1,a]$,
and $w\ge-\lambda$ on $(b,c]$. A suitable $\lambda$ exists exactly when the
displayed inequality holds. $\square$

Above $c$ the restriction uses only the signs of the profile of $v$. If it takes
both signs above $c$, or both signs on $(a,b]$, the two relations are jointly
realizable in the given order whatever their overlap. A long circuit whose
profile changes sign above the largest element of a three-point circuit is
therefore never excluded by it. Proposition 8 adds an orientation-dependent
restriction to Proposition 2, but no contradiction between the forced short
and long circuits follows from it.

Whether the ordered pairwise conditions, with the covering property, imply
$n\le2^d-1$ for $d\ge4$, or even $n\le\kappa^d$ for some $\kappa<3$, is open.
A family satisfying them with $n\ge2^d$ would show that the ordered overlap
restriction also fails. The projective model supplies no such family, and
Proposition 7 is not evidence that one exists.

## The pair condition for every short support

The cone test has an exact quantitative form for a pair of arbitrary circuit
sizes, including all the short supports of sizes three through six forced by
the high-girth argument. Put $a=\tau(u)$ and $b=\tau(v)$, where $u,v$ are
independent and each profile takes both signs. Write $J_+$, $J_-$ and $J_0$
for the coordinates where $a$ is positive, negative and zero. For
$\epsilon\in\{1,-1\}$ define

$$
\lambda_\epsilon^-
 =\max_{j\in J_+}\frac{-\epsilon b_j}{a_j},\qquad
\lambda_\epsilon^+
 =\min_{j\in J_-}\frac{-\epsilon b_j}{a_j}.
\tag{5}
$$

**Proposition 9.** No increasing positive vector annihilates both relations
if and only if, for at least one choice of $\epsilon$,

$$
\epsilon b_j\ge0\quad(j\in J_0),\qquad
\lambda_\epsilon^-\le\lambda_\epsilon^+.
\tag{6}
$$

*Proof.* By the cone criterion, infeasibility is equivalent to a nonzero
combination $\alpha a+\beta b\ge0$. Since $a$ takes both signs, $\beta\ne0$.
Divide by $|\beta|$ and put $\lambda=\alpha/|\beta|$ and
$\epsilon=\operatorname{sign}\beta$. The inequalities on $J_+$ say
$\lambda\ge\lambda_\epsilon^-$, those on $J_-$ say
$\lambda\le\lambda_\epsilon^+$, and those on $J_0$ are exactly (6).
Independence ensures that the resulting combination is nonzero. $\square$

Thus every pair of actual circuits must violate (6) for both signs. This
uses the relative positions and signs of the two circuits; their cardinalities
and intersection size do not determine it. If $b$ takes both signs on $J_0$,
both choices of $\epsilon$ already fail. In particular, oscillation of the
long relation's profile above the short circuit defeats this exclusion test.
Proposition 8 is the case $a=-1,0,1,0$ on its four successive intervals.

No estimate has been obtained that combines these allowed profile patterns
with covering every $(d+1)$-set to contradict $n\ge2^d$. The numerical
inequality retained from the ordered argument is exactly Proposition 7:
it gives $n\le18$ at $d=4$, where the needed bound is $15$, and has base
three asymptotically. The completion-path inequality is a separate support
count, so it does not fill this gap. Passing the realization test for all pairs
still leaves the full cone condition on combinations of three or more relations
to be checked.

## Retained examples

The 25-point $K_{4,4}$ construction in
[[research/erdos_963/forest_obstruction|the forest note]] contains both the
four-point circuit

$$
50025+19995=50010+20010
$$

and a seventeen-point circuit on $D\cup\{50025\}$. The latter is

$$
50025=2001\bigl(15+54+66+90+114+174+246-734\bigr),
$$

where multiplication by $2001$ means using both copies of the eight-element
block $A$, once in $A$ and once in $2000A$. The forest note proves that $D$
is dissociated and this ternary representation is unique, so its full
seventeen-element support is minimal. The four-point relation is minimal
because its distinct positive entries have no additive triple. These circuits
meet at $50025$ and are jointly realized by the displayed positive integers;
no cone certificate from them is possible. Here $d=16$ and $n=25$, far below
the counterexample threshold. The coexistence therefore defeats an absolute
ban on interacting short and long circuits, without testing the required
exponential cardinality hypothesis.

In the seven-point set of
[[research/erdos_963/matching_obstruction|the matching note]] every circuit
has six points, each omitting one point, so every two circuits are an exchange
pair sharing five points, and Proposition 2 forces every pair to be mixed.
For example, the relations omitting $3$ and $15$,

$$
15+35+55=31+33+41,\qquad 3+41+55=31+33+35,
$$

agree on $31,33,55$ and disagree on $35,41$. That set has only circuits of size
$d+1$, so it exhibits no coexistence of short and long circuits.

In the sharp six-point example $\{1,3,4,5,7,8\}$, take
$u:p_6=p_1+p_5$ and $v:p_1+p_5=p_2+p_4$. Their profiles are
$(-1,0,0,0,0,1)$ and $(0,-1,0,0,1,0)$, respectively. The second takes both
signs where the first is zero, so (6) fails for both signs. Compatible
elimination gives the existing circuit $p_6=p_2+p_4$. Conversely, the
six-position infeasible example above has profiles $(-1,0,1,0,0,0)$ and
$(-1,0,1,1,0,1)$: for $\epsilon=1$ both endpoints in (5) equal $-1$, and
the second profile is nonnegative on $J_0$. Formula (6) excludes it.

For small $d$ the three relevant maxima compare as follows. At $d=2$ real sets
reach $3$, sign-free pairwise data allow $4$, and the ordered conditions allow
$3$. At $d=3$ the values are $6$, $13$ and at most $7$. At $d=4$ the real
maximum is at most $14$, sign-free pairwise data allow $40$, and the ordered
conditions allow at most $18$.

## Remaining gap

The interaction between the two forced circuit sizes cannot come from pairs of
circuits with free orientation; Theorem 3 rules this out at every $d$.
A successful inequality must use information beyond the sign-free pairwise
conditions. Examples of such information are the fixed order and signs in
(6), and combinations of at least three circuits, such as the characteristic
three obstruction in Lemma 4. Other arguments may
use the integer realization directly, as the high-girth bound and the binary
residue tree of [[research/erdos_963/proof_sketch|the proof sketch]] do. The
projective model has no integer realization. The ordered conditions settle
$d\le3$ through single relations. The remaining question is whether covering,
compatible closure and the common-order restrictions imply the all-$d$ bound.
The first undecided value for this weakened system is $d=4$, where
Proposition 7 gives $18$; the actual real-set case already has the stronger
bound $14$. No ordered countermodel or coupled covering estimate is supplied.
The target is unresolved.
