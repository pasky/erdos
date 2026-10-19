---
name: research/erdos_774/routes/tensor_holes
title: Root signed-span coverage and its reset
desc: A proved root-coverage recurrence amplifies separation thresholds below a critical level, but an explicit arbitrarily large chromatic jump resets coverage maximally.
tags: [E0774, proved, tensor, obstruction]
sources: []
created: 2026-09-18T00:24:00Z
updated: 2026-09-18T00:24:00Z
---


# Root signed-span coverage and its reset

***

## Standing

This is a proved refinement of
[the tensor coloring criterion](tensor_coloring.md). It does not yet iterate to
unbounded coloring. The exact reset example below explains the missing induction
hypothesis.

## A necessary separation parameter

Let $B$ have $N$ nonzero elements and admit a proper $q$-coloring.
For $C\subseteq B$ put $R(C)=B\setminus\Sigma(C)$, and define

$$
R_q(B)=\max_f\sum_{c=1}^q|R(f^{-1}(c))|,
\qquad \alpha_q(B)=\frac{R_q(B)}{qN}. \tag{1}
$$

The maximum ranges over all proper $q$-colorings. Every root belongs to
the signed span of its own color, so $0\leq\alpha_q\leq(q-1)/q$.
Any family witnessing $\tau_q(B)$ must omit each root from each color's
signed span in at least one layer. Counting these $qN$ requirements gives

$$
\tau_q(B)\geq\lceil1/\alpha_q(B)\rceil \quad(\alpha_q(B)>0).
\tag{2}
$$

If $\alpha_q(B)=0$, every root is universal and $\tau_q(B)=\infty$.
Positive $\alpha_q$ does not imply that $\tau_q$ is finite.

## Nonjump recurrence — proved

Suppose $Y=B\otimes S_m$ admits a proper $q$-coloring, where
$m\geq3$. Then

$$
m\alpha_q(B)\geq1,\qquad
\alpha_q(Y)\leq
\min\left\{\alpha_q(B),\ 2\alpha_q(B)-\frac2m\right\}. \tag{3}
$$

To prove this, fix a proper coloring of $Y$, and denote its color $c$
by $D_c$, with base layers $C_{j,c}$. For a root $b\in B$, exact
membership is

$$
b\otimes s_j\in\Sigma(D_c)
\iff \exists u\in\bigcap_{i\ne j}\Sigma(C_{i,c})
          \text{ with }u+b\in\Sigma(C_{j,c}). \tag{4}
$$

Indeed, a representation of the left side has common layer sum $u$ off
layer $j$, and sum $u+b$ at that layer, by the unique rational
relation among the simplex directions.

Let $k_c(b)$ be the number of layers whose color-$c$ span omits $b$.
Properness and the layer criterion force $k_c(b)\geq1$. A root over
$b$ can be absent from $\Sigma(D_c)$ only at one of these omitted
layers, since otherwise use $u=0$ in (4). If $k_c(b)=1$, it is
not absent even there: use $u=-b$ in (4). Thus

$$
\sum_c|Y\setminus\Sigma(D_c)|
\leq\sum_{b,c}k_c(b)1_{k_c(b)\geq2}.
$$

Put $K=\sum_{b,c}k_c(b)$ and $M=qN$. Each layer is a proper base
coloring, so $M\leq K\leq mR_q(B)$. Since every $k_c(b)\geq1$,

$$
\sum_{b,c}k_c(b)1_{k_c(b)\geq2}
\leq\min\{K,2(K-M)\}.
$$

Divide by $qmN$ and maximize over the coloring of $Y$ to get (3).

In particular, if $0<\alpha=\alpha_q(B)\leq1/2$ and
$m=\lfloor1/\alpha\rfloor+1$, a nonjump yields

$$
\alpha_q(Y)\leq\frac{2\alpha^2}{1+\alpha}. \tag{5}
$$

If $1/2<\alpha<2/3$, repeated nonjump factors $S_3$ first lower it
below $1/2$, since the gap below $2/3$ at least doubles at each step.
These are genuine amplification statements. No assertion here bounds their
total analytic loss through arbitrarily many chromatic levels.

### Quantitative cheap amplification below a small threshold

Suppose a tensor base has $\chi(B)=q$, $\alpha_q(B)\leq a\leq1/4$,
and rounding parameter $Q_0$. As long as the color number does not jump,
set $a_0=a$, $m_n=\lfloor1/a_n\rfloor+1$, and
$a_{n+1}=2a_n-2/m_n$. If $a_n=0$, every further simplex forces a
jump, and arbitrarily large arity makes its analytic cost arbitrarily small.
Otherwise (3) gives $\alpha_q\leq a_n$ at each stage, and
$a_{n+1}\leq2a_n^2\leq a_n/2$.

The logarithmic growth of $Q$ is at most

$$
\sum_n\frac{\log m_n}{m_n}
\leq\sum_n a_n\log(2/a_n)
\leq2a\log(4/a)\leq\log4.
$$

Thus $Q\leq4Q_0$ and the total nonjump extension loss is at most
$2Q_0\sum_na_n^2\leq(8/3)Q_0a^2$. After a sufficiently long prefix,
$p=\lfloor1/(2a_n)\rfloor\geq q+1$ is below $\tau_q$, so it forces
a jump with additional loss tending to zero as the prefix length grows.

This proves a quantitatively cheap jump **given** a small input coverage
bound. It supplies no restart bound after the jump; (6) below disproves a
general restart bound even below $2/3$.

## An exact maximal reset after a jump

Let $B=S_3\otimes S_4$. Then

$$
\chi(B)=2,\quad\tau_2(B)=\infty,
\qquad
\chi(B\otimes S_m)=3,
\quad\alpha_3(B\otimes S_m)=2/3\quad(m\geq12). \tag{6}
$$

Identify $B$ with the edges of $K_{3,4}$. The elementary cographic criterion
proved for $K_{3,5}$ in
[the layer evidence](../evidence/tensor_layers/_index.md) applies with the same
proof: a set is dissociated exactly when its complement graph is connected; a
root outside it is in its signed span exactly when that edge is a bridge of the
complement.

The following two edge-disjoint spanning paths partition $K_{3,4}$:

$$
R_1-L_1-R_2-L_2-R_3-L_3-R_4,
\qquad
R_3-L_1-R_4-L_2-R_1-L_3-R_2.
$$

Their complements are spanning trees, giving a proper two-coloring. Every
dissociated set has size at most six. Thus in every proper two-coloring both
classes have size six, both complements are trees, and both classes signed-span
every root. This proves the first two assertions in (6); the chromatic jump
then follows from the layer criterion and the three-palette upper bound.

Here is a fully rational certificate for the last assertion. Color the four
columns of the $3$-by-$4$ edge array by the permutations

$$
(123),\quad(231),\quad(312),\quad(123).
\tag{7}
$$

Call the classes $C_0,C_1,C_2$. Each class has four edges. Its complement
is connected and bridgeless: suppressing the four degree-two right vertices
gives a triangle on the left vertices with edge multiplicities $(2,1,1)$.
Consequently each class is independent and
$\Sigma(C_i)\cap B=C_i$.

Order the six tensor coordinates as $(11,12,13,21,22,23)$. Directly from
the classes in (7), their rational spans have common intersection

$$
U=\{(0,a,b,0,a-b,a):a,b\in\mathbb Q\}. \tag{8}
$$

For verification, defining equations for their spans respectively are

$$
\begin{array}{ll}
C_0:&x_{21}=0,\quad -x_{12}+x_{13}+x_{22}=0,\\
C_1:&x_{11}=0,\quad -x_{13}-x_{22}+x_{23}=0,\\
C_2:&x_{21}-x_{11}=0,\quad x_{23}-x_{12}=0.
\end{array}
$$

Swap right columns 3 and 4, with induced ambient map $T$. On each row
triple it sends $(x_1,x_2,x_3)$ to
$(x_1-x_3,x_2-x_3,-x_3)$, so

$$
T(U)=\{(-b,a-b,-b,-a,-b,-a):a,b\in\mathbb Q\},
\qquad U\cap T(U)=\{0\}. \tag{9}
$$

For the last equality, coordinates $11$ and $21$ force both parameters
of the vector in $T(U)$ to vanish.

Use six layer types: the three cyclic color relabelings of (7), and the
three relabelings of its $T$-image. For $m\geq12$, use every type
at least twice, filling any extra layers by repetitions. For each color, the
intersection of its layer rational spans remains zero even after deletion
of any one layer, by (8)–(9). The layers give a proper three-coloring.
In (4), the only possible $u$ is zero; hence a tensor root belongs to a
color's signed span exactly when it actually has that color. It is omitted
by exactly the other two colors, proving $\alpha_3=2/3$, its absolute
maximum.

The same witness gives the maximal value for **any nonnegative weights on
the tensor roots**. Thus simply weighting root omissions cannot prevent this
reset. This does not exclude other witness sets or a stronger invariant.

## The same seed also loses anchors at boundary arity three

For $Y=S_3\otimes S_4\otimes S_3$, an additional exact certificate
proves $\chi(Y)=3$ and

$$
\tau_3(L(Y))\leq36 \tag{10}
$$

for every linear scalar encoding $L$ preserving all ternary relations
exactly. In particular no universal three-color anchor survives.

Run `uv run --no-sync python
wiki/research/erdos_774/evidence/tensor_boundary/main.py` from the repository
root. The
[standalone standard-library checker](../evidence/tensor_boundary/main.py) has
fixed finite input: nine four-point base layers with exactly $3^4=81$ ternary
sums each, and twelve specified automorphisms. It verifies the colorwise
intersection sizes $(81,7,1),(81,7,1),(81,17,1)$, so the displayed tensor
coloring is proper. Each color has twelve points.

Its third class lies in a rational hyperplane. The twelve automorphic
copies have hyperplane normals of rank twelve, and each copied coloring
has a class disjoint from a class of the original coloring. All classes
therefore lie in one connected disjoint-class graph. A scalar common to
all their signed spans has a common vector lift, by the exactness argument
in [the Grow boundary certificate](../evidence/boundary_anchor/_index.md). The
full-rank normals force this vector to be zero. Taking all three cyclic
color relabelings of each copied coloring makes these twelve partitions
into a 36-layer witness for (10). The
[certificate page](../evidence/tensor_boundary/_index.md) records what the
checker verifies and how the certificate was found.
