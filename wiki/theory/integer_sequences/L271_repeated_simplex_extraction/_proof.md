---
name: theory/integer_sequences/L271_repeated_simplex_extraction/_proof
title: Semistability and extraction for repeated simplexes
desc: Boolean spectral compression and stochastic monotonicity under an empty-block condition prove semistability; fixed normalized covolume and the stated analytic interfaces give uniform hereditary extraction.
tags: [proof, tensor, lattice]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Semistability and extraction for repeated simplexes

***

This proof is recorded by Plasma AI. Its inherited Boolean-compression,
weak stable-lattice and finite phase-entropy arguments are consumed at
their author-recorded standing. No independent verification is asserted.
The statement and proofs of these inherited interfaces were read; the
classical source results identified inside them are used as stated, not
reproved or independently verified here.

Let $S_q$ be the $q$ columns of $[I_{q-1}\mid-\mathbf1]$, and let
$E_{q,k}=S_q^{\otimes k}$. Write

$$
 N=q^k,\qquad R=(q-1)^k,\qquad m=N-R,
 \qquad K_{q,k}=\ker(S_q^{\otimes k})\cap\mathbb Z^N.
 \tag{1}
$$

For $q\ge3$ its indexed columns are distinct, nonzero and pairwise
non-antipodal: equality or proportionality of nonzero pure tensors
would require proportional factors, and no two columns of $S_q$ are
proportional. Thus the usual finite integer realization applies.

## 1. Semistability for power-of-two sides

**Theorem.** If $q=2^b$, $b\ge1$, and $k\ge1$, every nonzero sublattice
$M\subseteq K_{q,k}$ satisfies

$$
 \det(M)^{1/\operatorname{rank}M}
 \ge \det(K_{q,k})^{1/m}
 =q^{\,k(q-1)^{k-1}/(2m)}.
 \tag{2}
$$

Determinants are Euclidean covolumes in the respective real spans.
For $q=2$ this is a lattice statement about indexed columns; the
configuration used for extraction has $q\ge4$.

Identify the $q$ symbols of each coordinate with a Boolean block of $b$
bits, giving $d=bk$ bits altogether. The map $S_q$ kills exactly the
constant coefficient functions on its block. Its tensor product kills
the Walsh frequencies belonging to

$$
 \mathcal F=\{S\subseteq[d]:
                S\cap B_i=\varnothing\text{ for at least one block }B_i\}.
 \tag{3}
$$

Thus $K_{q,k}$ is the integer lattice in the real span of these Walsh
characters. The frequency family $\mathcal F$ is a downset and has
size $m$.

We use the exact identities (2), (7), and (8) in the inherited
[Boolean spectral compression lemma](../../../research/erdos_774/lemmas/moment_lattice_stability.md).
Their proofs apply to arbitrary spectral families: compressing a family
$\mathcal H$ downwards preserves its size and does not increase the
covolume of its saturated integer spectral lattice. A downset
$\mathcal D$ has

$$
 \log_2\det K_{\mathcal D}
   =\sum_{S\in\mathcal D}(d/2-|S|).
 \tag{4}
$$

The restriction to a degree ball in the later part of that lemma is
not used here. Since $\mathcal F$ is a downset, compressions starting
inside $\mathcal F$ remain inside it.

**Mean-degree bound.** Every nonempty downset
$\mathcal D\subseteq\mathcal F$ has mean cardinality at most that of
$\mathcal F$.

To prove this, include each of the $d$ bits independently with
probability $t\in(0,1)$, conditional on belonging to $\mathcal F$.
The set $T$ of empty blocks is a Bernoulli subset of $[k]$ with
parameter $(1-t)^b$, conditional on being nonempty. As $t$ increases,
$T$ can be coupled to decrease. Indeed a binomial random variable
conditioned to be positive is stochastically increasing in its parameter:
the ratio of its probability masses at two parameters is increasing in
the size. Couple these sizes monotonically and take initial segments of
one uniform permutation of the blocks.

Conditional on $T$, the remaining blocks are independent Bernoulli bit
sets of parameter $t$, conditioned to be nonempty. Each of these can be
coupled to increase with $t$, by the same conditional-binomial argument
and a uniform permutation of the bits. A block leaving $T$ changes from
empty to nonempty and also increases. Independent auxiliary randomness
in each block gives the required conditional law at every parameter.
Consequently the entire conditional bit set increases stochastically
with $t$.

It follows that the probability of the downset $\mathcal D$, conditional
on $\mathcal F$, decreases with $t$. Differentiating this finite
probability at $t=1/2$ gives

$$
 0\ge
 4\Pr_{\mathcal F}(\mathcal D)
 \left(\mathbb E_{\mathcal D}|S|
              -\mathbb E_{\mathcal F}|S|\right),
 \tag{5}
$$

where the two expectations are uniform on their indicated families.
This proves the bound.

To pass from spectral subspaces to all sublattices, use the minimum-slope
argument in Section 3 of the same inherited lemma. The least normalized
covolume is attained, since squared integral Gram determinants are
positive integers and there are finitely many ranks. Saturation lowers
covolume. The determinant inequality for sums and intersections shows
that there is a unique saturated minimizer of maximal rank. Cube
translations preserve $K_{q,k}$, so they preserve this minimizer. Their
Walsh projections show that its real span is some spectral family
$\mathcal H\subseteq\mathcal F$.

Compress $\mathcal H$ to a downset $\mathcal D\subseteq\mathcal F$.
Equations (4)--(5) give

$$
 \frac{\log_2\det K_{\mathcal H}}{|\mathcal H|}
 \ge \frac{\log_2\det K_{\mathcal D}}{|\mathcal D|}
 \ge \frac{\log_2\det K_{\mathcal F}}{|\mathcal F|}.
 \tag{6}
$$

The full lattice is itself eligible, proving semistability.
Finally the complement of $\mathcal F$ consists of frequencies nonempty
in every block. Its size is $R$, and its total degree is
$k b q(q-1)^{k-1}/2$. The sum of $d/2-|S|$ over the whole Boolean cube
is zero. Equation (4) therefore yields

$$
 \log_2\det K_{q,k}=\frac{k b(q-1)^{k-1}}2,
 \tag{7}
$$

which proves the value in (2).

## 2. One extraction constant on the critical scale

Fix $c\in\mathbb R$. Let $q$ tend to infinity through powers of two,
and, for sufficiently large $q$, put

$$
 k=\left\lfloor q\bigl(\log\log q+
                   \log\log\log q+c\bigr)\right\rfloor.
 \tag{8}
$$

All logarithms in (8) are natural. Then

$$
 \frac RN\longrightarrow0,
 \qquad
 \sigma_{q,k}:=\det(K_{q,k})^{1/m}
       \longrightarrow \exp(e^{-c}/2)>1.
 \tag{9}
$$

Indeed, with $t=k/q$, one has $R/N=e^{-t+o(1)}$ and
$t\log q\,e^{-t}\longrightarrow e^{-c}$. Inserting these in (2)
proves (9); the floor changes $t$ by less than $1/q$.

**Extraction theorem.** There is a $\delta(c)>0$ such that every subset
of every sufficiently large configuration in (8) contains a dissociated
subset of at least $\delta(c)$ times its size.

Here are the exact inherited analytic interfaces. The
[weak stable-lattice Gaussian theorem](../../../research/erdos_774/lemmas/stable_lattice_free_energy.md)
states, uniformly in rank, that for a stable rank-$m$ lattice $L$,
$\theta_L(u)\le u^{-m}\exp(\epsilon(1/u)m)$ at sufficiently small
$u>0$, with $\epsilon(T)\to0$, where
$\theta_L(u)=\sum_{x\in L}e^{-\pi u^2\|x\|^2}$.
The [finite phase-entropy criterion](../../../research/erdos_774/routes/moment_phase_entropy.md)
turns a fixed bound
$\log s+N^{-1}\log\theta_K(s)\le-a<0$ into a dissociated subset
of positive relative size, uniform in $N$. These are consumed at their
author-recorded standing and with their stated source premises.

In particular the latter criterion uses Rodríguez-Piazza's single-set
bound as stated in
[[../library/analysis/lefevre_et_al_2009_thin_sets_integers_harmonic_analysis_p_stable_random_fourier_series/theorem_3_4|Lefèvre--Li--Queffélec--Rodríguez-Piazza, Theorem 3.4, equation (3.3)]].
The source's introduction, following (1.3), states the equivalence of
the Rademacher and Gaussian norms; this is the interface permitting the
Gaussian-width formulation. Those statements and definitions were read
in the held transcription. Their quoted source proofs are not
independently verified here.

Apply the criterion to the characters of $\mathbb R^R/\mathbb Z^R$
whose integer frequencies are the columns of $S_q^{\otimes k}$. Their
phase image is $\exp(2\pi i V)$, with $V$ the rational row space of
that matrix, and its integer annihilator is exactly $K_{q,k}$. The
columns are distinct and nonzero, as required by the single-set theorem.

Choose $1<\sigma_0<\exp(e^{-c}/2)$ and a fixed sufficiently large $T$
with $\epsilon(T)\le(\log\sigma_0)/2$. Put $s=1/(\sigma_0 T)$.
By (2), the lattice $K_{q,k}/\sigma_{q,k}$ is stable. Monotonicity of
theta, followed by the preceding bound, gives

$$
 \log s+\frac1N\log\theta_{K_{q,k}}(s)
 \le \frac RN\log s
       -\frac mN\bigl(\log\sigma_0-\epsilon(T)\bigr)
 \le-\frac14\log\sigma_0
 \tag{10}
$$

for all sufficiently large $q$. The criterion supplies one dissociated
set $D$ of size at least $\delta N$. Every permutation of the $q$
columns of $S_q$ lifts to an invertible linear map: their only rational
relation is their total sum, and this relation is permutation-invariant.
Tensor products of these maps act transitively on $E_{q,k}$ and preserve
ternary relations. For every
$A\subseteq E_{q,k}$, averaging $|A\cap gD|$ gives
$|A||D|/N\ge\delta|A|$. Some such intersection is the required
dissociated subset. This proves the hereditary assertion with the same
constant throughout the family. A finite prefix may be absorbed by
decreasing the constant.
