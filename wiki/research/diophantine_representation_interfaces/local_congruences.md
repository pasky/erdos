---
name: research/diophantine_representation_interfaces/local_congruences
title: "Congruence coverage and lifting obstructions"
desc: "Interval packing, fixed prime multipliers, moving prime cutoffs and local powerful-number solvability have distinct global limitations."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E0445/_index|E0445]],
[[problems/diophantine_problems/E0479/_index|E0479]],
[[problems/diophantine_problems/E0676/_index|E0676]],
[[problems/diophantine_problems/E1107/_index|E1107]].

## E0445: interval packing does not improve this theorem's exponent

The target is every translate (n,n+p^c), for all sufficiently large primes p,
for each c>1/2; a,b need not differ. Browning--Haynes Theorem 1 guarantees an
inverse pair in one of J interval pairs of lengths H,K, with disjoint first
intervals, when JH^2K^2>=C p^3 log^4 p.

To force the pair inside one prescribed nonwrapping interval I of length L, put
all first and second intervals inside I. Then JH<=L and K<=L, so

$$
JH^2K^2\le L^4/J\le L^4.
$$

The criterion can therefore only be invoked if L^4>=Cp^3 log^4 p. Its best
packing is J=1; subdividing loses. For L=p^c this is still c>3/4, with the
logarithm excluding the endpoint. Intervals outside I prove existence elsewhere.
Splitting a wrapping interval modulo p only changes constant factors. This
obstructs this particular internal-packing use, not the target or all
Kloosterman methods. Next test: uniform control for one specified interval or
new use of the same-interval condition. Stop if the gain is only choosing one
successful interval among many.

## E0479: fixed-prime-multiplier lifting fails for generic k

The target is infinitely many positive n for every fixed integer k!=1, including
negative k and zero. Suppose n=mp with m fixed and p prime. Fermat gives
2^(mp)=(2^m)^p congruent to 2^m modulo p, also for p=2. Thus a solution forces
p|(2^m-k). If 2^m!=k, only finitely many p can work. This holds even when m was
already a solution and p is confined to a progression.

For k=2^m the obstruction vanishes. The held Tang theorem and the page's
order/Dirichlet argument choose p in a reduced class making m divide the
difference too, excluding primes dividing m. This is the known power-of-two
family, not a lifting mechanism for k=3. The known k=0,-1,-2 mechanisms are not
refuted by the fixed-m statement.

Next test: a growing-seed mechanism producing a new prime with all needed order
conditions. Stop at multiplication of one fixed seed by arbitrary primes.

## E0676: finite prime sieves leave an exact moving-cutoff gap

For a given n the condition is exactly that some prime p<=sqrt(n) satisfies n
mod p^2<p. The cutoff follows from a>=1. A complete finite test of one n must
therefore check all those primes; an eventual assertion has no supplied finite
reduction.

For a finite prime set S, let M=product_(p in S)p^2. All sufficiently large n
congruent to -1 modulo M avoid S, since p^2-1>=p. Thus no fixed finite set of
primes covers all large integers. These n can still be represented by other
primes: this is not a counterexample family to E0676.

Conversely the density avoiding all primes p<=y is exactly
product_(p<=y)(1-1/p), by CRT: precisely p of each p^2 residue classes succeed.
The finitely many n<p^2 do not affect density. The full exceptional set is
contained, up to finitely many terms, in each such avoidance set. Euler's
divergence of sum_p 1/p makes the products tend to zero. This proves density
zero for exceptions, not finiteness; no stronger sieve bound is used.

Next test: control y<p<=sqrt(n) along an explicit growing CRT family, or obtain
an eventual coverage bound. Stop if y stays fixed while n grows, or only
density/finite examples are supplied.

## E1107: no fixed congruence obstruction exists

The target is all sufficiently large integers as sums of at most r+1 positive
r-powerful numbers for every fixed r>=2; 1 is allowed and no coprimality is
required. The Problem 939 transfer was already excluded because it makes the
total powerful too; that obstruction is not new here.

For every modulus M>=1, every residue is a sum of at most three residues
containing positive r-powerful integers. For M=1 this is immediate. If M is odd,
each residue is a sum of two units: at each prime divisor choose a nonzero first
residue different from the target, and choose the second as the difference
modulo the full prime power; combine by CRT. If M is even, an even target is a
sum of two units by the same choices at odd primes and 1,target-1 at the power
of 2. An odd target is a sum of three units: use 1,1,target-2 at the power of 2,
and 1 plus a two-unit decomposition of target-1 at odd prime powers. CRT
combines these choices.

Choose e>=r with e congruent to 1 modulo phi(M). For a positive unit
representative u, Euler gives u^e congruent to u modulo M. Every u^e is
r-powerful, since nonzero valuations are multiples of e. The sum therefore has
the desired residue, and 3<=r+1. No fixed-modulus test can disprove the target.
There is no size control relative to the integer being represented, so this is
not a local-to-global theorem.

No novelty is claimed for this local observation. The missing step is a global
argument with the exact summand count and size control. Congruence coverage or a
finite represented suffix does not supply that step.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/diophantine_problems/browning_2013_incomplete_kloosterman_sums/_index|Browning
  and Haynes (2013): Incomplete Kloosterman sums]]: Many-interval corollary and
  constant/packing qualification (account reading). Theorem 1 and J=1 criterion;
  proof pointer only (statement reading).
- [[../library/number_theory/tang_2025_erdos_479_congruences/_index|Tang (2025):
  A note on Erdős Problem 479]]: Theorem 3.1 and order/Dirichlet proof pointer,
  pp.4-5 (account reading).
