---
name: research/erdos_940/cubic_trace_counterexample
title: Many representations with large ratios in all three traces
desc: A sparse conic construction defeats unrestricted deterministic all-three-traces pigeonholing, but not a statistical multiplicity estimate.
tags: []
sources: []
created: 2026-09-23T00:00:00Z
updated: 2026-09-23T00:00:00Z
---


# Many representations with large ratios in all three traces

***

## Scope

For every fixed $K\ge2$, there are arbitrarily large $N$ and
$K$ distinct positive representations

$$
x_j^3+y_j^3+z_j^3=N^3,\qquad
(x_j,y_j,z_j)\in[N/3,N]^3,
$$

such that, for each of the three chosen traces $x+y,x+z,y+z$,
every reduced ratio between two representations has height
$\asymp_K N$. Constants may depend on the fixed construction.

This rules out forcing a small ratio in at least one of the
three traces merely from a large fixed number of interior
representations. **No primitivity assertion is made.** The
constructed family is sparse and has cube targets; it does
not rule out a typical-fiber estimate after deleting negligible
input families.

## A conic on the equal-sums surface

In the plane $x+y=3(w-z)$, put $d=x-y$. The equation
$x^3+y^3+z^3=w^3$ contains the residual conic

$$
(23z-29w)^2+23(3d)^2=312w^2.                         \tag{1}
$$

Indeed, substituting $x=(3(w-z)+d)/2$ and
$y=(3(w-z)-d)/2$ reduces the cubic equation to

$$
(w-z)\bigl(23w^2-58wz+23z^2+9d^2\bigr)=0.
$$

The quadratic factor is equivalent to (1).

Let $\rho=\sqrt{-23}$ and $\alpha_0=-105-3\rho$,
whose norm is $11232=312\cdot6^2$. Choose $L$ with
$2^{L-1}\ge K$, and choose $K$ distinct sign vectors
$\epsilon\in\{\pm1\}^L$ whose last coordinate is $+1$.
Fix even integers $c_1,\ldots,c_L$, to be selected below, and
take positive even integers $M$. Define

$$
G(M)=\prod_{i=1}^L((M+c_i)^2+23),\qquad w=6G(M),
$$


$$
t_\epsilon+e_\epsilon\rho
=\alpha_0\prod_{i=1}^L(M+c_i+\epsilon_i\rho)^2,
$$

and

$$
z_\epsilon=\frac{t_\epsilon+29w}{23},\qquad
d_\epsilon=e_\epsilon/3,\qquad
x_\epsilon=\frac{3(w-z_\epsilon)+d_\epsilon}{2},\qquad
y_\epsilon=\frac{3(w-z_\epsilon)-d_\epsilon}{2}.
$$


These coordinates are integral. The coefficient $e_\epsilon$
is divisible by three. Modulo $23$, one has
$t_\epsilon\equiv-105G$ and $29w=174G$, so the formula for
$z_\epsilon$ is integral. Since $M+c_i$ is even,
$t_\epsilon,e_\epsilon,z_\epsilon,d_\epsilon$ are odd and
$w$ is even, which verifies the divisions by two.
Taking norms gives (1), hence

$$
x_\epsilon^3+y_\epsilon^3+z_\epsilon^3=w^3.
$$

As $M\to\infty$ with the $c_i$ fixed,

$$
(x_\epsilon,y_\epsilon,z_\epsilon)/w
\longrightarrow(2/3,5/6,1/2).
$$

Thus all the points eventually lie in the claimed interior box.

## Choosing constants so that the trace gcds are bounded

Before specializing $X_i=M+c_i$, put

$$
U_\epsilon=\prod_i(X_i+\epsilon_i\rho),\qquad
V_\epsilon=\prod_i(X_i-\epsilon_i\rho).
$$

Each of the three trace formulas is a binary quadratic
expression

$$
A U_\epsilon^2+B U_\epsilon V_\epsilon+C V_\epsilon^2,
\qquad A C\ne0.
$$

This follows directly from its nonzero real-linear dependence
on $t_\epsilon,e_\epsilon$, together with
$w=6U_\epsilon V_\epsilon$.
Over an algebraic closure it therefore factors into expressions
$U_\epsilon-\lambda V_\epsilon$, with $\lambda\ne0$.

On the open set $X_i\ne\pm\rho$, use the coordinates
$u_i=(X_i+\rho)/(X_i-\rho)$. Each such factor becomes, up to
a unit, a Laurent binomial

$$
\prod_i u_i^{\epsilon_i}-\lambda.
$$

It is irreducible because the exponent vector is primitive.
Binomials from two selected sign vectors are not associates:
their exponent vectors are neither equal nor opposite. Also
no trace polynomial has a factor $X_i-\rho$ or $X_i+\rho$,
because $A C\ne0$. Consequently two trace polynomials for
the same chosen trace and different sign vectors are coprime.

Their common-zero locus in affine $L$-space therefore has
codimension at least two. A generic line parallel to
$(1,\ldots,1)$ misses it: the exceptional translations lie
in the image of this locus times an affine line, of dimension
at most $L-1$. There are only finitely many pairs and traces.
Thus fixed even integral $c_i$ can be chosen outside all
exceptional algebraic sets. For that choice the corresponding
one-variable trace polynomials in $M$ are pairwise coprime.

After clearing their fixed denominators, Bezout identities for
these polynomials show that the gcds of their integer values
are bounded independently of $M$. Each trace has size
$\asymp w$, so all the reduced trace-ratio heights are
$\asymp w$. In particular the represented triples are distinct
for all sufficiently large $M$. Set $N=w$ to finish the proof.

## What remains possible

The
[fixed-ratio collision bound](cubic_collision_ranges.md#binary-trace-ratios-uniformly-in-the-prescribed-ratio)
does not acquire a deterministic rich-fiber consequence by simply using all
three traces. This construction shows why. But it produces only
$O_K(T^{1/(2L)})$ inputs of root height at most $T$, since $w\asymp M^{2L}$. It
is therefore a zero-mass input family. It neither establishes unbounded typical
multiplicity nor prevents a statistical estimate which first excludes sparse
exceptional families.
