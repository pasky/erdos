---
name: research/erdos_774/lemmas/canonical_circuit_cover_colors
title: Canonical cyclic lifts of one circuit have two actual colors
desc: For a primitive nonternary rational circuit, sufficiently large degree-2P canonical interval lifts are fully dissociated-two-colorable by sheet parity; mixed-circuit and arbitrary-cover amplification remain open.
tags: [E0774, covers, coloring, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:10:00Z
updated: 2026-10-13T05:28:09Z
---


# Canonical cyclic lifts of one circuit have two actual colors

***

The [canonical cyclic lift](cover_projection_and_templates.md) flattens
any integer relation. Unlike the earlier designated-template splitting
bound, the theorem below colors **all ternary relations** of specified
covers of a single rational circuit. It does not bound arbitrary covers
or simultaneous constructions using several interacting circuits.

## 1. The canonical polynomial matrix

Let $A\in\{0,1\}^{X\times V}$ have distinct nonzero columns forming a
rational circuit. Put $n=|V|$ and choose its primitive relation

$$
\ker_{\mathbb Q}A=\mathbb Q a,\qquad
a\in\mathbb Z^V,\quad \gcd_v|a_v|=1.
$$

All $a_v\ne0$. Write $L_v=|a_v|$ and

$$
p_x=\sum_{a_v>0}A_{xv}a_v
    =\sum_{a_v<0}A_{xv}|a_v|.
$$

For each row, tile $[0,p_x)$ separately by its positive and negative
incident lengths, in any fixed orders. Let $g_{xv}\geq0$ be the tile
start and $G=\max_{A_{xv}=1}g_{xv}$. Set

$$
A(z)_{xv}=A_{xv}z^{g_{xv}},\qquad
h_v(z)=\operatorname{sgn}(a_v)S_{L_v}(z),\qquad
S_L(z)=1+\cdots+z^{L-1}.
$$

The two tilings of every row give the exact identity

$$
A(z)h(z)=0\quad\hbox{over }\mathbb Z[z].           \tag{1}
$$

For any degree $m>\max_xp_x$, use incidence shifts $b\mapsto b+g_{xv}$
modulo $m$. The coefficients of $h$, assigned to sheets, form a
nonzero ternary relation in the resulting cover. All used sheets are
distinct within a type because $L_v\leq\max_xp_x<m$.

## 2. Full dissociation of the two parity classes

**Theorem.** Suppose $\max_vL_v\geq2$. For every odd prime $P$ with

$$
P-1>nG,\qquad 2P>\max_xp_x,                       \tag{2}
$$

the degree-$2P$ canonical cover is properly dissociated-colored by
$c(v,b)=b\bmod2$. In particular its actual coloring number is exactly two.

**Proof.** Since $A(1)=A$ has rank $n-1$, while (1) supplies a kernel,

$$
\ker_{\mathbb Q(z)}A(z)=\mathbb Q(z)h(z).
$$

The vectors $h(z)$ and $h(-z)$ are not proportional. To verify this,

$$
\frac{S_L(-z)}{S_L(z)}
=\frac{1-z}{1+z}
 \begin{cases}
 1,&L\ \text{even},\\
 (1+z^L)/(1-z^L),&L\ \text{odd}.
 \end{cases}                                    \tag{3}
$$

An even and odd length have unequal ratios. Two distinct odd lengths
also have unequal ratios (compare their first nonconstant terms after
canceling the common factor). Thus proportionality requires either all
lengths even, or all the same odd length. Primitivity excludes the first
case and reduces the second to $L_v=1$ for all $v$, contrary to the
hypothesis.

Therefore the stacked matrix

$$
M(z)=\begin{bmatrix}A(z)\\ A(-z)\end{bmatrix}
$$

has full column rank over $\mathbb Q(z)$. Choose a nonzero $n$-row
minor $D(z)$. Its polynomial degree is at most $nG$.

Suppose $f_v(b)\in\{0,\pm1\}$ is a relation supported on sheet parity
$\varepsilon$, and put $F_v(z)=\sum_{b=0}^{2P-1}f_v(b)z^b$.
At every $2P$-th root of unity,

$$
A(z)F(z)=0,\qquad F(-z)=(-1)^\varepsilon F(z).
$$

Applying the first identity at $-z$ also gives $M(z)F(z)=0$.
Every $2P$-th root other than $1,-1$ has order $P$ or $2P$ and
degree $P-1$ over $\mathbb Q$. For completeness, irreducibility of
$1+z+\cdots+z^{P-1}$ follows by substituting $z+1$ and applying
Eisenstein at $P$; the order-$2P$ case is obtained by $z\mapsto-z$.
Equation (2) thus ensures $D(z)\ne0$ at all these roots. Consequently
$F(z)=0$ there.

Write $F_v(z)=z^\varepsilon Q_v(z^2)$, where $\deg Q_v<P$.
It vanishes whenever $z^2$ is a nontrivial $P$-th root. Fourier
inversion on $\mathbb Z/P\mathbb Z$ shows that its coefficient sequence
is constant:

$$
f_v(\varepsilon+2j)=\lambda_v\in\{0,\pm1\}
           \quad(0\leq j<P).                    \tag{4}
$$

Sum the covering relation over all sheets. It gives $A\lambda=0$,
so $\lambda=q a$ for rational $q$. Since $a$ is primitive and
$\lambda$ integral, Bezout's identity gives $q\in\mathbb Z$.
The bounds $|\lambda_v|\leq1$ and $\max|a_v|\geq2$ force $q=0$.
Thus (4) vanishes and each parity class is fully dissociated.
The nonzero canonical relation from Section 1 proves that one color
does not suffice. $\square$

## 3. Fixed voltages preserve type independence at large prime degree

Here is a separate useful stabilization fact. Fix any nonnegative
integer translation voltages on any finite binary base, and a rationally
independent set $U$ of its column types. Some $|U|$-row minor of
$A(z)_U$ is nonzero at $z=1$, and has degree at most $|U|G$.
For a prime cover degree $Q$ with $Q-1>|U|G$, that minor is nonzero
at every $Q$-th root. Fourier decomposition of the cyclic cover then
shows that **all copies of the types in $U$** are rationally independent.

For a rational circuit, partition its types into any two nonempty proper
sets and apply this fact to each. For its canonical voltages, when

$$
Q-1>nG,\qquad Q>\max_xp_x,
$$

the degree-$Q$ cover has
$\chi_1=\chi_{\mathbb Q}=2$, including when the base circuit is already
ternary. The upper bound is a type coloring; the canonical relation gives
the lower bound. This is a theorem for **fixed voltages and growing prime
degree**, not for all covers of those degrees.

## 4. Adaptive cuts also exist, but do not defeat these colorings

Multiplying (1) by $(z-1)Y(z)$, for any binary sheet function $y$,
gives the ternary relation

$$
f_v(b)=\operatorname{sgn}(a_v)
                  (y(b-L_v)-y(b)).              \tag{5}
$$

These are cuts of the circulant multigraph with a type-$v$ edge
between $b-L_v$ and $b$, labeled by the covered column $(v,b)$.
This graph is connected because $\gcd_vL_v=1$. A coloring avoids all
nonzero relations (5) exactly when deleting the edges of each individual
color leaves a connected graph: a constant-on-components indicator gives
the reverse implication.

Thus the interval template is only one member of a genuinely adaptive
family. Nevertheless Section 2 colors **every** ternary relation, including
all these cuts, in the stated nonflat-circuit covers. A successful cover
amplifier must go beyond independently chosen canonical one-circuit lifts,
for example by coupling different relation spaces. No such arbitrary-color
coupling theorem is established here.

The polynomial identities, Fourier argument, primitive coefficient step,
and quantifier restrictions are author-recorded, checked against the
supplied proof. No computation or new external paper theorem is used; the
review is internal.
