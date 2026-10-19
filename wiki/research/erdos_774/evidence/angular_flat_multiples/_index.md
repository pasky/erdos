---
name: research/erdos_774/evidence/angular_flat_multiples
title: Exact checks of the displayed flat cyclotomic multiples
desc: Exact arithmetic certifies D(15) = 8, D(105) = 49 and a flat multiple of the 1155th cyclotomic polynomial of degree 502, with the quoted thresholds and covolume; a separate solver script records the searches that suggest 502 is least.
tags: [E0774, computational, proved, tensor]
sources: []
created: 2026-10-15T11:14:17Z
updated: 2026-10-15T11:14:17Z
---

# Exact checks of the displayed flat cyclotomic multiples

[[research/erdos_774/evidence/_index|..]]

***

## Purpose

The [angular-coloring page](../../routes/angular_colorings.md) bounds the
dissociated coloring number of the odd prime grids by $\lceil N/D(N)\rceil$,
where $D(N)$ is the least degree of a flat multiple of $\Phi_N$, and quotes
values of $D(N)$ together with the thresholds and one lattice covolume used
in its discussion. The algebra on that page and on
[[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123]] is the
durable justification; this probe checks the displayed polynomials and
numbers exactly.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/angular_flat_multiples/main.py
```

The [checker](main.py) uses exact integer arithmetic, the standard library and
the shared root `tools` checker, performs no search and finishes in a few
seconds. It builds $\Phi_{15}$, $\Phi_{105}$ and $\Phi_{1155}$ as Möbius
quotients of the binomials $x^d-1$ and checks their degrees and that each
divides $x^N-1$ but no $x^d-1$ with $d$ a proper divisor. Its named checks
then establish:

- $\Phi_{15}$ is flat, so $D(15)=8$; $(1-x)\Phi_{105}$ is flat of degree 49
  with 26 nonzero coefficients, and $\Phi_{105}$ has height two, attained at
  $x^7$ and $x^{41}$, so $D(105)=49$;
- the multiplier $(1-x^6)S$ displayed on the research page has degree 22 and
  constant term one, $\Phi_{1155}(1-x^6)S$ is flat of degree 502 with 128
  nonzero coefficients, $\Phi_{1155}$ has height three, and $S$ has no
  cyclotomic factor;
- $(1-x^{11})\Phi_{105}(x^{11})$ is a flat multiple of $\Phi_{1155}$ of
  degree 539;
- the exact totient ratios of the odd prime prefixes cross $1/3$ between the
  primes 19 and 23 and $1/4$ between 73 and 79, the odd primes up to 23 have
  $\sum(p-2)=82$, and the ratio for 1155 is $480/1155$;
- the Gram determinant of $\Phi_{1155},x\Phi_{1155},\ldots,x^{22}\Phi_{1155}$
  has half-logarithm $51.39$, and the section bound $2^{23}(503/23)^{23/2}$ has
  logarithm $51.42$.

These give $D(1155)\le502$ and the quoted values; a failed clause exits
nonzero. The lower bound $D(1155)\ge502$ is not checked.

## The solver searches

The [discovery script](produce.py) poses, for given $N$ and degree $D$, the
exact-coefficient feasibility problem of the research page: integer unknowns
$q_0=1,\ldots,q_{D-\varphi(N)}$, bounded by the partial sums of the absolute
coefficients of $1/\Phi_N$, with every coefficient of $\Phi_NQ$ in
$\{-1,0,1\}$. It uses the HiGHS solver in SciPy on one thread, checks every
reported solution by exact multiplication, and appends its verdicts to the
ignored `output/` folder. Its verdicts are observations, not certificates.
For $N=1155$ the solver reported infeasibility at the degrees 488 and 495 to
501, hence at every degree up to 501, and solutions at 502 to 505, 520 and
538; the solution at 502 is the multiplier checked above. For $N=15015$, runs
of 450 seconds at degree 6000 and of 900 seconds at degree 6300 stopped at the
time limit without a solution, so they decide nothing about $D(15015)$.
