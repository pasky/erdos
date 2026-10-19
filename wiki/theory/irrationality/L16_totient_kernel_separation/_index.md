---
name: theory/irrationality/L16_totient_kernel_separation
title: Nonzero summable totient kernels do not vanish on a progression
desc: |
  Every nonzero real absolutely summable kernel of shifted phi(n)/n has
  positive absolute limsup on each fixed arithmetic progression; a fresh
  prime gives an explicit pair of separating refinements.
tags: []
sources:
- problems/irrationality/E0249
id: L16
statement: |
  Let phi be Euler's totient with phi(1)=1 and rho(n)=phi(n)/n for n>=1.
  Let (c_s)_{s>=1} be a real sequence with sum_s |c_s| finite and at least
  one nonzero entry. For integers N>=1 put F(N)=sum_s c_s*rho(N+s).
  For every integer Q>=1 and a in Z,
  limsup_{N->infinity, N>0, N congruent a mod Q} |F(N)| > 0.
  More precisely define
  kappa_Q(r)=zeta(2)^(-1)*product_{p|Q}(1-p^(-2))^(-1)
             *product_{p|gcd(Q,r)}(1-p^(-1)),
  where both products are over primes and zeta(2)=sum_{n>=1} n^(-2).
  Put d_s=c_s*kappa_Q(a+s). For every s_*>=1 with d_{s_*} nonzero,
  every integer K>=s_* with sum_{s>K}|d_s|<|d_{s_*}|/4, and every
  prime ell>K not dividing Q, choose a_0 and a_1 with
  a_i congruent a mod Q, a_0 congruent 0 mod ell, and
  a_1 congruent -s_* mod ell. The Cesaro means of F on these two
  progressions modulo Q*ell exist and differ. At least one has absolute
  value greater than |d_{s_*}|/(4*ell*(1-ell^(-2))), and that progression
  contains infinitely many positive N with
  |F(N)|>|d_{s_*}|/(8*ell*(1-ell^(-2))).
status: proved
tier: 0
depends_on: []
created: 2026-09-17T06:05:14Z
updated: 2026-09-17T06:05:14Z
---

# Nonzero summable totient kernels do not vanish on a progression

[[theory/irrationality/_index|..]]

[[theory/irrationality/L16_totient_kernel_separation/_proof|_proof]]: Divisor counting gives exact progression means; two fresh-prime
refinements separate an isolated nonzero coefficient from the l1 tail.

***

## Statement

Let $\varphi$ be Euler's totient, with $\varphi(1)=1$, and write
$\rho(n)=\varphi(n)/n$ for $n\ge1$. For a real sequence
$(c_s)_{s\ge1}$ with $0<\sum_s|c_s|<\infty$, set

$$
F(N)=\sum_{s\ge1}c_s\rho(N+s),\qquad N\ge1.
$$

For every integer $Q\ge1$ and $a\in\mathbb Z$,

$$
\limsup_{\substack{N\to\infty\\N>0,\ N\equiv a\ (Q)}}|F(N)|>0.
$$

The series is absolutely and uniformly convergent in $N$ since
$0<\rho\le1$. The following explicit refinement statement is part of
the claim. Define, for integer $r$,

$$
\kappa_Q(r)=\frac1{\zeta(2)}
 \prod_{p\mid Q}(1-p^{-2})^{-1}
 \prod_{p\mid\gcd(Q,r)}(1-p^{-1}),\qquad
d_s=c_s\kappa_Q(a+s),
$$

where products are over primes and $\zeta(2)=\sum_{n\ge1}n^{-2}$.
Take any $s_*\ge1$ with $d_{s_*}\ne0$, any integer $K\ge s_*$ with
$\sum_{s>K}|d_s|<|d_{s_*}|/4$, and any prime $\ell>K$ not dividing
$Q$. Let $a_0,a_1$ satisfy

$$
a_0\equiv a_1\equiv a\pmod Q,\qquad
a_0\equiv0\pmod\ell,\qquad a_1\equiv-s_*\pmod\ell.
$$

The Cesàro means of $F$ along the two progressions modulo $Q\ell$
exist and differ. At least one has magnitude greater than

$$
\eta=\frac{|d_{s_*}|}{4\ell(1-\ell^{-2})}>0,
$$

and that progression contains infinitely many positive $N$ with
$|F(N)|>\eta/2$. Means omit any finitely many nonpositive indices.
The choices exist because $\kappa_Q(r)>0$, $\sum_s|d_s|<\infty$,
and there are arbitrarily large primes outside the finite set dividing
$Q$. The [proof](_proof.md) establishes those facts as well as the claim.

## Scope and application

The kernel and the original progression are fixed before choosing the
anchor, cutoff, refining prime and limit. No lower bound uniform over
all nonzero kernels or growing moduli is asserted. The claim concerns
every fixed subprogression as well, but it does not prohibit vanishing
on a specially selected subsequence.

The [[research/leads/totient_binary_series/progression_means|research applications]]
give a finite-window error bound and apply this claim to fixed dilation
grids. The [[research/leads/totient_binary_series/_index|combined sketch]]
explains its proposed use for [[problems/irrationality/E0249/_index|Problem 249]].
Rationality of $\sum_{n\ge1}\varphi(n)/2^n$ has not been shown to force a
nonzero kernel of this kind to tend to zero. The theorem therefore does
not prove or disprove that target.

## Current standing and verification

The complete proof is author-recorded at tier 0. It has no identified
gap, independent whole-claim acceptance, formal verification, or novelty
claim. Internal research challenge supplied no independent acceptance.
No native L-claim is consumed. The proof uses the elementary totient
divisor identity, congruence counting, absolutely convergent series and
Euler products, the Chinese remainder theorem, and infinitude of primes.
It uses neither Dirichlet's theorem on primes in progressions nor an
uninspected source theorem.

The entire mathematical subject is this statement and its
[self-contained proof](_proof.md); no program or computational input is
required. The finite evidence and subsequent tail applications in the
research home are separate results and do not certify this claim.
