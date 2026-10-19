---
name: theory/irrationality/L218_sparse_perturbation_any_value
title: Sparse small changes of the totient give the binary series any value
desc: |
  Changing Euler's totient only on a set with gaps at most g, by multiples of
  2^s and by at most the square root except at the first change, makes
  sum psi(n)/2^n equal any real number when s+g is at most half of log2 n.
tags: []
sources:
- problems/irrationality/E0249
id: L218
statement: |
  Let phi be Euler's totient with phi(1)=1. Let g and s be nondecreasing
  functions from the positive integers to the nonnegative integers, and let
  n_0>=1 be an integer with s(n)+g(n)<=(1/2)*log_2(n) for every n>=n_0.
  Let e_1<e_2<... be an infinite sequence of integers with e_1>=n_0 and
  e_(k+1)-e_k<=g(e_k) for every k>=1. Then for every real number r there
  are integers delta_1, delta_2, ... such that, putting psi(n)=phi(n) when
  n is not one of the e_k and psi(e_k)=phi(e_k)+delta_k, one has
  (i) delta_k is divisible by 2^(s(e_k)) for every k>=1;
  (ii) |delta_k|<=e_k^(1/2) for every k>=2; and
  (iii) the series sum_{n>=1} psi(n)*2^(-n) converges absolutely and its
  sum equals r.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

# Sparse small changes of the totient give the binary series any value

[[theory/irrationality/_index|..]]

[[theory/irrationality/L218_sparse_perturbation_any_value/_proof|_proof]]: Greedy rounding at each changed place keeps the remaining error below
2^(s-e-1), so the next change is at most 2^(s+g), which is at most e^(1/2).

***

## Statement

Let $\varphi$ be Euler's totient, with $\varphi(1)=1$. Let $g,s$ be
nondecreasing functions from the positive integers to the nonnegative
integers and $n_0\ge1$ an integer such that

$$
s(n)+g(n)\le\tfrac12\log_2n\qquad(n\ge n_0).
$$

Let $e_1<e_2<\cdots$ be integers with $e_1\ge n_0$ and
$e_{k+1}-e_k\le g(e_k)$ for every $k\ge1$. Then for every real number $r$
there are integers $\delta_1,\delta_2,\ldots$ such that, with
$\psi(n)=\varphi(n)$ for $n\notin\{e_k\}$ and
$\psi(e_k)=\varphi(e_k)+\delta_k$,

1. $2^{s(e_k)}\mid\delta_k$ for every $k\ge1$;
2. $|\delta_k|\le e_k^{1/2}$ for every $k\ge2$;
3. $\sum_{n\ge1}\psi(n)2^{-n}$ converges absolutely and equals $r$.

Only the first change $\delta_1$ may be large. The [proof](_proof.md) is a
greedy rounding.

## Significance

[[problems/irrationality/E0249/_index|Problem 249]] asks whether
$\sum_{n\ge1}\varphi(n)2^{-n}$ is irrational. With
$s(n)=g(n)=\lfloor\frac14\log_2n\rfloor$ for large $n$ and gaps exactly
$g(e_k)$, the sequence $\psi$ agrees with $\varphi$ modulo
$2^{\lfloor\log_2n/4\rfloor}$ at every $n$, differs from it by at most
$n^{1/2}$ except at the single place $e_1$, and differs from it only on a
set that windows of $o(\log N)$
consecutive integers near $N$ meet for a vanishing proportion of $N$. Since
$r$ may be any rational number, no property shared by $\varphi$ and all such
$\psi$ can decide the problem. The
[[research/totient_binary_new_attack/perturbation_barrier|perturbation
barrier page]] derives these window statements and explains what they
exclude and what they leave open, in particular arguments that use exact
multiplicative identities of $\varphi$; the
[[research/totient_binary_new_attack/proof_sketch|proof sketch of the fresh
attack]] records the limitation on arguments using only these shared data.
The claim does not prove or disprove the irrationality of the totient
series.

## Current standing and verification

The complete proof is author-recorded at tier 0, with no independent
acceptance, formal verification, or novelty claim. No native L-claim is
consumed. The proof uses only $0<\varphi(n)\le n$, rounding to the nearest
integer, and absolute convergence. Check 6 of the
[research evidence](../../../research/totient_binary_new_attack/evidence/main.py)
runs the construction on a finite prefix for four rational targets and
verifies the residue, size and error bounds of the proof at every step
there, with a control that must fail; that finite exercise does not certify
the claim, which rests on the proof.
