---
name: problems/integer_sequences/E0472
title: Problem 472
desc: |
  Asks whether some finite starting sequence of primes $q_1<\cdots<q_m$ makes
  infinite the sequence in which each next term $q_{n+1}$ is the least prime of
  the form $q_n+q_i-1$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 472

[[problems/integer_sequences/_index|..]]

***

**Statement.** Given some initial finite sequence of primes $q_1<\cdots<q_m$
extend it so that $q_{n+1}$ is the smallest prime of the form $q_n+q_i-1$ for
$n\geq m$. Is there an initial starting sequence so that the resulting sequence
is infinite?

**Status.** Open.

**Source.** [erdosproblems.com/472](https://www.erdosproblems.com/472), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #472,
https://www.erdosproblems.com/472.

**Formalization.** None recorded.

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

With $r_i=q_i-1$, the recurrence candidate $q_{n+1}=q_n+q_i-1$, $i\le n$,
becomes $r_{n+1}=r_n+r_i$. The gcd of the prefix of $r_i$'s is invariant, and a
new term is at most $2q_n-1$. Neither fact guarantees a prime among the
candidates.

If selected offsets were bounded by $D$, successive prime gaps would be at most
$D$. Choose $T>D+1$ with $T!$ past the seed. All of $T!+2,\ldots,T!+T$ are
composite. An increasing unbounded prime sequence must cross this block with a
jump greater than $D$, a contradiction. Every infinite extension therefore uses
unbounded offsets and unbounded historical indices.

Dirichlet's theorem gives no prime in the prescribed finite set of offsets;
Bertrand's interval theorem does not either. No computation or infinite
extension proof was supplied.

The unresolved obligation is to guarantee primality among an expanding
historical set of offsets, uniformly at every stage. A useful test is to check
any proposed finite-state reduction for whether it secretly bounds increments;
if so, the factorial obstruction refutes it. Stop at numerical survival of a
seed, bounded-offset models, or a prime-in-interval theorem without an
allowed-offset bridge.
