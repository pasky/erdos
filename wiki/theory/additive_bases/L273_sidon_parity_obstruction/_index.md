---
name: theory/additive_bases/L273_sidon_parity_obstruction
title: "A parity obstruction to zeroing Sidon moments"
desc: "An alternating quadratic has negative square expectation after zeroing forbidden moments of block/uniform mixtures, with or without degreewise renormalization, once the excess above sqrt(N) exceeds an absolute constant in the stated even-block family."
id: L273
statement: |
  There are absolute constants s_0 and C>0 such that the following holds.
  Let s>=s_0 be an integer, let W be an even integer with s^3/2<=W<=s^3,
  and put N=sW and k=s^2. On {0,...,N-1}, let mu independently choose a
  uniform s-subset of each of s consecutive W-point blocks, either without
  rotation or followed by an independent uniform cyclic rotation. Let nu
  be uniform on all k-subsets, and let rho=(1-alpha)mu+alpha nu for any
  real alpha in [0,1]. Write p(T)=Pr_rho(T is contained in the random set).
  Strong Sidon means that equality of two sums, including repeated summands,
  implies equality of their unordered pairs. Define L_0 on Boolean-reduced
  monomials of degree at most four by L_0(z_T)=p(T) for |T|<=2 and for
  strong Sidon T, and L_0(z_T)=0 otherwise. Define L_1 by the same rule,
  except that every surviving degree-t moment is multiplied by
  a_t=binom(k,t)/sum_{|T|=t, T strong Sidon}p(T), t=3,4.
  These denominators are positive. Put
  A=sum_{d=1}^{N-1}(-1)^d sum_{x=0}^{N-1-d}z_x z_{x+d}.
  For either L=L_0 or L=L_1,
  L((A-L(A))^2) <= -(k^2/(2N))(k^2-N)+C s^2.
  Consequently, for every fixed beta in (0,1], any such even W_s satisfying
  W_s=s^3-beta s^2+O(s), and any sequence alpha_s in [0,1], the limsup
  of s^(-3)L((A-L(A))^2) is at most -beta/2.
status: proved
tier: 0
depends_on: []
created: 2026-10-16T00:12:37Z
updated: 2026-10-16T00:12:37Z
---

# A parity obstruction to zeroing Sidon moments

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L273_sidon_parity_obstruction/_proof|_proof]]: The alternating-count identity, elementary balanced-sample moments, a common-block incidence bound, cancellation over progression extensions, and control of uniform degreewise renormalization.

[[theory/additive_bases/L273_sidon_parity_obstruction/evidence/_index|evidence/]]: Exhaustive rational moment checks for the parity identity at N=8,16,54, both block rotation conventions and three mixture weights, with an independent direct sample-space calculation at N=8.

***

This is Plasma AI's complete author-recorded argument, without independent
review or formal verification. It concerns two specified moment functionals.
It leaves the upper and lower error estimates in
[[problems/additive_bases/E0030/_index|Problem 30]] unresolved.

The [proof](_proof.md) uses the identity $2A=B^2-Z$, where $B$ is parity
imbalance and $Z$ is cardinality. Every four-distinct sum collision has even
element sum. Erasing these moments therefore removes a large contribution
from the square of $A$. Elementary sampling moments and incidence counts
control the remaining terms, uniformly over the mixture parameter.

The block sampling model is also used in
[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216's linear-capacity barrier]],
and the degreewise renormalization is the rule tested in
[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217's quartic obstruction]].
All definitions and the argument needed here are given locally. The evenness
of $W$ is essential to this proof. The mixture need not satisfy any capacity
inequality. In the stated family, the bound is negative once
$k-\sqrt N$ exceeds an absolute constant; it supplies no bound on the
cardinality of an actual Sidon set.

The [evidence entry point](evidence/main.py) exhausts the inclusion moments
of degrees two through four at $(s,W)=(2,4),(2,8),(3,18)$, for both block
rotation conventions and the mixture weights $0,1/2,1$. Exact rational
arithmetic checks the parity identity, the centered-square calculation and
the renormalization denominators. A separate enumeration of the whole
sample space at $(s,W)=(2,4)$ checks the calculation directly. These finite
controls do not prove the asymptotic theorem. Run from the repository root:

```sh
uv run --no-sync python wiki/theory/additive_bases/L273_sidon_parity_obstruction/evidence/main.py
```

The proof has no unresolved mathematical step. The
[[research/sidon_extremal_error/parity_obstruction|research account records the necessary parity budget and the unresolved linear compatibility of local repairs]],
and the
[[research/sidon_extremal_error/proof_sketch|proof sketch separates those gaps from the extremal target]].
