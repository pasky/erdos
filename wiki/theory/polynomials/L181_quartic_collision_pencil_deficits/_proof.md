---
name: theory/polynomials/L181_quartic_collision_pencil_deficits/_proof
title: From the certified pencils to the strict quartic deficits
desc: |
  The two fixed quartics have two real critical values. Conjugation reduces
  each pencil to a compact angle interval, on which the retained program
  certifies the signed integral. Scaling the inverse images gives the
  claimed length inequality.
created: 2026-10-15T20:30:28Z
updated: 2026-10-15T20:30:28Z
---

***

We give the mathematical bridge for the
[[theory/polynomials/L181_quartic_collision_pencil_deficits/_index|claim]].
All computational steps below are author evidence, without an independent
audit of the engine.

## The two pencils and their coverage

For $F_D=z^4-\tfrac32z^2-z$,
$F_D'=4(z-1)(z+\tfrac12)^2$. Its critical values are $-\tfrac32$ at
$1$ and $\tfrac3{16}$ at the double critical point $-\tfrac12$.
For $F_E=z^4-2z^2$, $F_E'=4z(z-1)(z+1)$. Its critical values are
$-1$ at $1,-1$ and $0$ at $0$. Denote the two ordered values of either
quartic by $f_A<f_B$, and put $d=f_B-f_A$.

Every circle through these values has center on their perpendicular
bisector. After conjugation, which preserves the integral because the
quartics have real coefficients, it is represented by

$$
R=\frac{d}{2\sin\beta},\qquad
C=\frac{f_A+f_B}{2}+iR\cos\beta,
\qquad 0<\beta\le\pi/2.
$$

The value $\beta=0$ represents the real line. Thus the compact interval
$[0,\pi/2]$ covers the entire pencil, including its line limit.
The flattening parametrization used by the program is

$$
\sigma(x)=f_A+\frac{e^{-i\beta}x}{1-i\kappa x/2},\qquad
\kappa=\frac{2\sin\beta}{d}.
$$

It has the displayed circle as its image when $\beta>0$ and is the
real line when $\beta=0$.

## The certified integral

The
[[research/erdos_114/quartic_evidence/_index|evidence account]] and the
docstring and formulas of
`wiki/research/erdos_114/quartic_evidence/evidence/main.py`
specify the finite computation. The mathematical bounds it applies are
the Crofton window estimate, certified inverse-root discs, the singular
weight identity and the far-field factorization proved in the
[[research/erdos_114/quartic_critical_values|research sketch]],
under "Uniform estimates through the degenerations".

For the flatter circles it subtracts the reference density pointwise;
for the other circles it bounds the nonnegative density integral and
subtracts the exact reference integral. Every accepted bound is uniform
both in its angle box and in its integration piece. All roots used in
those bounds are included in four pairwise disjoint discs certified by
Rouché's theorem. Singular windows use full preimage length bounds.
The signed pieces share exact endpoints, and the signed tail is bounded
as an integral, so no overlap of an unknown sign is discarded.

The full check accepts only if the angle boxes tile the specified
interval and every upper bound is strictly below $-1$. Its last edge
is checked to exceed $\pi/2$. The retained computation gives 142
accepted boxes for $F_D$ and 126 for $F_E$, with largest upper bounds
less than $-1.021$ and $-1.077$, respectively. These quoted decimal
bounds are rounded outward from the enclosures printed by the program.
It follows that the integral is below $-1$ at every parameter in the
two pencils.

Local inverse singularities have exponent at most $2/3$ on these
pencils, and the reference exponent is $3/4$, so the finite singularities
are integrable. The retained far-field estimate makes the signed
difference absolutely integrable at the line's infinity as well.

Run the complete evidence from the repository root with

```sh
uv run --no-sync python wiki/research/erdos_114/quartic_evidence/evidence/main.py
```

The full check uses 80-bit Arb and Acb balls and takes about forty-five
minutes of one thread per pencil. The options `--only double` and
`--only equal` partition it into its two required checks. The `--quick`
option covers only selected boxes and cannot establish this claim.
The approximate line values used in the controls test the implementation;
the proof of the bounds comes from the certified enclosures themselves.

## Passage to polynomial length

Let $\Gamma$ be a circle with center $C$ and radius $R$, and set
$p(z)=R^{-1}F(R^{1/4}z)-C/R$. Inverse-branch integration gives

$$
\ell(p)=R^{-1/4}\int_\Gamma G_F(\sigma)\,|d\sigma|.
$$

The inverse-derivative density of $w^4+f_A$ is
$|\sigma-f_A|^{-3/4}$. Because $f_A$ lies on $\Gamma$, its preimage
is, after rotation and the scale $R^{1/4}$, the lemniscate of $z^4-1$.
Consequently its length is $R^{1/4}\ell(z^4-1)$. Subtracting these two
identities yields

$$
\ell(p)-\ell(z^4-1)
=R^{-1/4}\widetilde I(F,\Gamma)<-R^{-1/4}.
$$

This proves the length consequence. The argument covers the two
collision pencils only and makes no assertion about all quartics.
