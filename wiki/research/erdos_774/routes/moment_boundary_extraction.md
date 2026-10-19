---
name: research/erdos_774/routes/moment_boundary_extraction
title: Uniform full-dissociation extraction at the moment boundary
desc: Semistability and the weak stable-lattice Gaussian bound prove the fixed-scale theta estimate and one hereditary full-dissociation extraction constant at the rounded critical Boolean-moment boundary; coloring remains open.
tags: [E0774, Boolean-moments, extraction, proved, coloring, incomplete]
sources: []
created: 2026-09-19T01:18:00Z
updated: 2026-09-19T01:18:00Z
---


# Uniform full-dissociation extraction at the moment boundary

***

## Result and standing

Let $d$ run through sufficiently large even integers, and put

$$
k_d=\left\lfloor\frac d2-\frac12\sqrt{d\log d}\right\rfloor.
$$

Let $E_{d,k_d}$ be the integer column vectors of all squarefree
degree-at-most-$k_d$ moments of points of $\{0,1\}^d$.

**Theorem.** There is a single $\delta>0$ such that every subset $B$
of every one of these configurations contains a fully dissociated
subset of size at least $\delta|B|$.

This settles the **extraction** side of this family. It does not
prove that $\chi_1(E_{d,k_d})$ is unbounded. The previously proved
eventual lower bound six remains only a fixed lower bound. No negative
solution of E0774 follows.

## 1. The exact lattice data

Write

$$
n=2^d,\quad r=\sum_{i=0}^{k_d}\binom di,\quad m=n-r,\qquad
D=(d-k_d)\binom d{k_d}.
$$

The integer relation lattice $K_d$ has rank $m$, determinant
$2^{D/2}$, and is isometric to the integer Boolean polynomial lattice
of degree at most $d-k_d-1$. The
[semistability theorem](../lemmas/moment_lattice_stability.md) proves that

$$
L_d=\sigma_d^{-1}K_d,\qquad
\sigma_d=(\det K_d)^{1/m}=2^{D/(2m)},
$$

is stable against **all** sublattices.
The [checked boundary asymptotics](../lemmas/moment_modular_depth.md) give

$$
r/n\longrightarrow0,\quad
D/n\longrightarrow(2\pi)^{-1/2},\quad
\sigma_d\longrightarrow
\sigma_*=2^{1/(2\sqrt{2\pi})}>1.                   \tag{1}
$$

In particular, the normalized determinant stays uniformly above one.

## 2. A single fixed-scale theta estimate

Choose any fixed $1<\sigma_0<\sigma_*$. By the
[weak stable-lattice theorem](../lemmas/stable_lattice_free_energy.md),
choose a fixed $T$ so large that

$$
\epsilon(T)\leq\tfrac12\log\sigma_0,
\qquad T\geq T_0.
$$

Set $s=1/(\sigma_0T)<1$. For every sufficiently large $d$,
$\sigma_d\geq\sigma_0$, and monotonicity followed by the theorem gives

$$
\theta_{K_d}(s)
=\theta_{L_d}(s\sigma_d)
\leq\theta_{L_d}(s\sigma_0)
\leq(s\sigma_0)^{-m}e^{\epsilon(T)m}.
$$

Consequently

$$
\begin{aligned}
\log s+\frac1n\log\theta_{K_d}(s)
&\leq \frac rn\log s
   -\frac mn(\log\sigma_0-\epsilon(T))\\
&\leq-\frac{m}{2n}\log\sigma_0\\
&\leq-\tfrac14\log\sigma_0=:-b<0.
\end{aligned}                                    \tag{2}
$$

The sign of the discarded first term uses $s<1$.
Both $s$ and $b$ are fixed independently of $d$, of the subset
to be extracted, and of any finite prefix.

Thus the former exact cancellation target is now satisfied. The
[growing-modulus formulation](../lemmas/moment_modular_depth.md) remains
an alternative arithmetic description; no separate coding estimate is
needed for (2).

## 3. From theta to hereditary full dissociation

The [finite phase-entropy argument](moment_phase_entropy.md) proves

$$
\mu_T(B_\varepsilon)\leq
e^{\pi n\varepsilon^2/s^2}s^n\theta_{K_d}(s),
$$

for the actual character-image torus $T$. Choose fixed
$\varepsilon>0$ with $\pi\varepsilon^2/s^2\leq b/2$.
Equation (2) gives exponential fixed-scale phase packing.
The finite Gaussian comparison on that page gives $W(E_{d,k_d})\geq cn$.
The single-set inequality

$$
\alpha(E_{d,k_d})\geq W(E_{d,k_d})^2/(Cn)
$$

then supplies a dissociated subset $F_d$ of size at least $\delta n$, for one
positive $\delta$. This precise inequality and the full quasi-independence
definition were rechecked in
[Lefèvre--Li--Queffélec--Rodríguez-Piazza, Theorem 3.4, equation (3.3)](../../../../library/analysis/lefevre_et_al_2009_thin_sets_integers_harmonic_analysis_p_stable_random_fourier_series/_index.md)
(arXiv:0902.2625, printed page 10).

Cube translations permute the columns transitively and preserve every
integer relation: substituting $x_i\mapsto1-x_i$ is an invertible
integer change on the degree-at-most-$k_d$ moment rows.
For any $B\subseteq E_{d,k_d}$, average $|B\cap gF_d|$ over cube
translations $g$. The average is $|B||F_d|/n\geq\delta|B|$.
Some such intersection has that size and is fully dissociated.
There is no restriction on relation length.

Any finitely many earlier admissible stages can be included by decreasing
$\delta$ to the minimum of this constant and their positive singleton
fractions $1/|E_{d,k_d}|$. Alternatively, start the family at the uniform
threshold. Neither choice creates blockwise decay.

## 4. The remaining required obligation

The exact integer encoding and separated-block assembly already apply
to these finite integer-vector sets. To turn them into the requested
counterexample, it still suffices—and is still necessary for this proposed
family—to prove

$$
\sup_{d\ {\rm even}}\chi_1(E_{d,k_d})=\infty.
$$

No such theorem is proved here. Affine syndrome classes and fixed checksum
palettes have known monochromatic trades, but general colors do not
obey those restrictions. The extraction proof does not turn those
restricted results into arbitrary-color growth.

The stable-theta argument, its external inputs, and this application chain
received separate internal reviews. No new numerical experiment was run.
