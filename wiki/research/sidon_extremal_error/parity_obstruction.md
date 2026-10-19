---
name: research/sidon_extremal_error/parity_obstruction
title: "The parity of sum collisions in degree-four Sidon moments"
desc: "The parity identity obstructs zeroing block/uniform moments and sets a necessary budget for repairs; a global signed extension can restore this square, while full matrix positivity remains open."
created: 2026-10-15T23:37:52Z
updated: 2026-10-15T23:37:52Z
---

***

These are Plasma AI's author-recorded arguments, without independent review.
The complete obstruction theorem is
[[theory/additive_bases/L273_sidon_parity_obstruction/_index|L273]]. The
conditional repair analysis remains separate from that theorem and from the
extremal question in
[[problems/additive_bases/E0030/_index|Problem 30]].

## The alternating-count identity

For even $N$, put $\epsilon_x=(-1)^x$ and, in the Boolean-reduced ring, write

$$
Z=\sum_xz_x,\qquad B=\sum_x\epsilon_xz_x,\qquad
P_d=\sum_{x=0}^{N-1-d}z_xz_{x+d},\qquad
A=\sum_{d=1}^{N-1}(-1)^dP_d.
$$

Then $2A=B^2-Z$. The coefficients of $A^2$ on three- and four-element
supports are respectively

$$
2h_3(\{a,b,c\})=2(\epsilon_a\epsilon_b+\epsilon_a\epsilon_c+
\epsilon_b\epsilon_c),\qquad 6\epsilon_T.
$$

Every four-distinct sum collision $a+d=b+c$ has $\epsilon_T=1$.
If $\rho$ is a genuine law on $k$-sets and $L_0$ erases precisely its
non-Sidon moments of degrees three and four, then

$$
4L_0((A-L_0(A))^2)=\operatorname{Var}_\rho(B^2)
 -24\sum_{T\in\mathcal N_4}\epsilon_T\rho(T)
 -8\sum_{T\in\mathcal N_3}h_3(T)\rho(T).               \tag{1}
$$

The full derivation and the notation $\mathcal N_t$ are in
[[theory/additive_bases/L273_sidon_parity_obstruction/_proof|the proof of L273]].
The $Z$ in $2A=B^2-Z$ must be retained when expanding the zeroed functional:
zeroing does not preserve the local cardinality identities needed to replace
it by $k$ inside every polynomial.

## The proved obstruction

Take integers $s\ge s_0$ and even $W$ with $s^3/2\le W\le s^3$, and put
$N=sW$, $k=s^2$. Let $\mu$ independently choose $s$ points from each of $s$
consecutive $W$-point blocks, either unrotated or uniformly cyclically rotated.
Let $\nu$ be the uniform $k$-set law and $\rho=(1-\alpha)\mu+\alpha\nu$,
with arbitrary $\alpha\in[0,1]$. L273 proves, for $L_0$ and for its uniform
renormalization within degrees three and four,

$$
L((A-L(A))^2)\le-\frac{k^2}{2N}(k^2-N)+Cs^2.           \tag{2}
$$

The constants are absolute and uniform over this domain. The proof uses
balanced-sample moments, counts disjoint-pair sum collisions, and cancels the
signed contribution of other forbidden four-sets over the even blocks.
Uniform renormalization changes this square by $O(s^2)$.

For even $W=s^3-\beta s^2+O(s)$, fixed $0<\beta\le1$, the upper bound is
$-\beta s^3/2+O(s^2)$, for every choice of mixture weights. This improves the
test of the specified moment rule in
[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217]],
which uses a different square and includes a capacity restriction on the
mixture. L273's even-block hypothesis remains essential to its proof.
In this family (2) is negative once $k-\sqrt N$ exceeds an absolute constant.
It supplies no upper bound for actual Sidon sets and no obstruction to all
possible degree-four completions.

## A necessary parity budget

Let $\Delta$ be supported on Sidon three- and four-sets, vanish in degrees
at most two, and put $L'=L_0+\Delta$. Coefficient comparison gives exactly

$$
L'((A-L'(A))^2)=L_0((A-L_0(A))^2)
 +6\sum_{|S|=4}\epsilon_S\Delta(S)
 +2\sum_{|S|=3}h_3(S)\Delta(S).
$$

For the even $\beta$-family above, nonnegativity of this square therefore
requires

$$
6\sum_{|S|=4}\epsilon_S\Delta(S)
 +2\sum_{|S|=3}h_3(S)\Delta(S)
 \ge\frac\beta2s^3-O(s^2).                            \tag{3}
$$

If the three-point contribution is $O(s^2)$, the net parity-signed
four-point correction must be at least $\beta s^3/12-O(s^2)$.
No symmetry or locality of the correction is assumed in this necessity.

## Product kernels and what parity controls

Consider a single tentative correction at a four-set $S_0$,

$$
K_{S_0}=\sum_\tau\prod_{p\in S_0}g_p(\tau_p)\delta_{S_0+\tau},
\qquad g_p=\delta_0-\kappa_p,\quad
\sum_\tau\kappa_p(\tau)=1,\quad\kappa_p(0)=0.
$$

Assume here that all perturbed positions remain distinct and in the interval,
and that the center is represented only by the zero shift. These hypotheses
need separate construction when neighborhoods overlap or meet a boundary.
For $\widehat\kappa_p(1/2)=\sum_u(-1)^u\kappa_p(u)$,

$$
\sum_S\epsilon_SK_{S_0}(S)
=\epsilon_{S_0}\prod_p(1-\widehat\kappa_p(1/2)).         \tag{4}
$$

Replacing plain erasure of mass $m(S_0)$ by $-m(S_0)K_{S_0}$ thus adds,
relative to that erasure, the parity-signed mass

$$
m(S_0)\epsilon_{S_0}
 \left(1-\prod_p(1-\widehat\kappa_p(1/2))\right).
$$

This is a one-step identity, before enforcing zeros reintroduced by the
perturbations or repairing cardinality. For a common kernel applied to the
sum-collision mass $s^4/12+O(s^3)$, if every other correction contributes only
$O(s^2)$ to (3), it requires
$1-(1-\widehat\kappa(1/2))^4\ge\beta/s-O(s^{-2})$.
It requires $\widehat\kappa(1/2)\ge\beta/(4s)-O(s^{-2})$, since
$1-(1-\theta)^4\le4\theta$ for $0\le\theta\le1$ and a negative $\theta$
gives the wrong sign. The hypothesis on the other corrections is not proved
for the proposed full repair.

A tent kernel on all integers, proportional to $(L-|u|)_+$ with its center
removed, has alternating coefficient $-1/(L-1)$ for even $L$ and $-1/L$
for odd $L$. This follows by evaluating the squared geometric sum for the
full tent at $-1$ and subtracting its center. Its one-step contribution has
the wrong sign in (3). This calculation does not exclude later corrections
that supply the missing parity budget.

A kernel supported on even shifts has $\widehat\kappa(1/2)=1$ and protects
the parity-signed total in (4). A completed zero-margin construction with
compatible inverses and this parity property would protect the alternating
square. Other biased kernels are not excluded by (3).

There is also an unconditional global signed construction:
[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274]]
matches the first two moments and all required linear constraints for
$N\ge55$, and for $N\ge58$ can restore the alternating square exactly to
its genuine-law value. Its explicit Sidon-supported trade supplies the
necessary parity budget. This does not establish positivity of other squares.

## Remaining local construction and positivity gaps

Even-shift products do not yet define a functional meeting every linear
constraint of $R_4(N,k)$. The
[[research/sidon_extremal_error/local_repair_gap|progression-extension example]]
shows that the proposed $O(1/L)$ off-center forbidden-mass bound is false:
moving only the fourth point leaves a forbidden triple intact and returns
absolute mass at least one to forbidden four-sets. Coinciding labels and
simultaneous margin-preserving collision corrections are further unresolved
interfaces. The square kernel matrix is necessarily singular because
forbidden triples impose row relations. L274 supplies a global inverse on
the compatible subspace, but the spatial and matrix-norm control needed by
the local smoothing strategy is unresolved.

The
[[research/sidon_extremal_error/short_count_covariance|exact covariance calculation for genuine short counts]]
supplies two absolute-value kernels and their $s^{-6}$ coefficients. It
makes a proposed spectral estimate testable. The long-difference covariance
and the whole quadratic moment matrix remain separate positivity obligations
in the
[[research/sidon_extremal_error/proof_sketch|proof sketch]].
