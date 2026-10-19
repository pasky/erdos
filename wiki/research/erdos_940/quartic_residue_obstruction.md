---
name: research/erdos_940/quartic_residue_obstruction
title: An exact obstruction to the restricted quartic residue objective
desc: A finite certificate rules out one 32-prescription upper-bound objective, not the successful quartic proof.
tags: []
sources: []
created: 2026-09-22T16:39:33Z
updated: 2026-10-14T00:26:52Z
---


# An exact obstruction to the restricted quartic residue objective

***

## Status and scope

Section 8 of the
[independent record](independent/canonical_decomposition_and_quartic_zero_target.md)
claimed a finite obstruction to one quartic construction. Its referenced script
was not supplied. The calculation is reconstructed in the
[preserved exact certificate](evidence/util/quartic_residue_obstruction.py), and
its formulas and rounding are checked. It proves that the specific objective
below exceeds $27/25=1.08$ for every choice of nonnegative budgets. This is
**not** an
obstruction to the [quartic complement argument](quartic_complement.md).

## The restricted objective

Fix target $15\pmod{16}$. A canonical coefficient $d=2^eu$ has type
$s=(E,v)$, where $e\in\{0,5,6,7\}$, $E=e\pmod4$, and $v=u\pmod{16}$ is
odd. There are $32$ types. Write

$$
Z_v=\sum_{\substack{u\text{ odd canonical}\\u\equiv v\ (16)}}u^{-1/4},
\qquad a_E=2^{-e/4},\qquad V=\Gamma(5/4)^4.
$$

The $32$ character prescriptions are indexed by a character $\psi$ of
$(\mathbb Z/16\mathbb Z)^\times$ and $t\in\{0,1,2,3\}$, with
$\chi(\ell)=\psi(\ell\bmod16)$ at odd coefficient primes and $\chi(2)=i^t$.
The associated sign is

$$
\epsilon=\chi(-1)=\chi(2)^2=(-1)^t,
$$

not necessarily $\psi(15)$: the prescription concerns positive odd primes.
For a multiset of four types, put $z_j=i^{tE_j}\psi(v_j)$ and $D=\prod_jz_j$.
The finite part of its zero-target trace is

$$
B=D^2\left[1+\epsilon\left(\left|\sum_jz_j\right|^2-4\right)\right]
  +D\sum_{j<k}z_j^2z_k^2.
$$

The remaining Jacobi term has absolute value at most $2$, by the checked
[Gauss-sum expansion](quartic_euler_majorant.md).

Among the $k$ odd coefficients, let $P$ be the fraction of their $2^k$
subsets whose residues sum to $15\pmod{16}$. All even coefficients vanish
modulo $16$, while an odd-coefficient term contributes either $0$ or its
coefficient residue with equal probability. Thus $\rho_{16}=16P$.
If $m_s$ is the multiplicity of type $s$, its relative unordered
representation weight is

$$
w=16VP\frac{\prod_s(a_EZ_v)^{m_s}}{\prod_s m_s!}.
$$

Indeed, type permutations give $4!/\prod_s m_s!$, followed by the usual
division by $4!$; representations with repeated actual summands are $o(X)$.

The proposed safe upper-bound objective is

$$
\mathcal F(\boldsymbol\lambda)
=\sum_{\text{type multisets}}w
\exp\left(\sum_g\lambda_g(B_g+2)\right),
\qquad\lambda_g\ge0.
$$


## The finite certificate

The certificate enumerates exactly $\binom{35}{4}=52360$ multisets and all
$32$ prescriptions. Exactly $364$ multisets have $P>0$ and $B_g+2\ge0$ for
every prescription. Their contributions cannot decrease as any budget grows.

Their weights are bounded below using only odd canonical coefficients
supported on the $53$ odd primes at most $251$. The cube
$[0,1/\sqrt2]^4$ lies in the positive quartic unit ball, so $V\ge1/4$.
All local weights $p^{-e/4}$ and all residue convolutions are rounded
**down** to multiples of $10^{-12}$, using integer fourth-root comparisons.
Nonnegative coefficients preserve the direction of every bound. The final
sum uses exact rational arithmetic and equals

$$
\frac{67826836205251839956626671887649519872177425279}
{62500000000000000000000000000000000000000000000}
>\frac{27}{25}.
$$

This is a newly reconstructed lower bound; no reliance is placed on the
unavailable original script or on floating-point optimization.

Hence $\mathcal F(\boldsymbol\lambda)>27/25$ for all nonnegative budgets. The
result does not cover other residue targets, other character prescriptions,
sharper use of Jacobi phases, additional small-prime restrictions, or
distinct-value estimates. In particular, the successful proof first eliminates
exceptional tuples using $8\pmod{16}$ and valuation-one targets, then uses a
different multiquadratic Frobenius distribution. See the
[comparison of the two methods](quartic_finite_families.md).
