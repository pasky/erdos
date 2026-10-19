---
name: research/diophantine_representation_interfaces/factorial_residues
title: "Factorial reflections and prime cofactors"
desc: "Reflection supplies bounded families at one prime, while first-hit distributions and prime cofactor support need separate information."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E1056/_index|E1056]],
[[problems/diophantine_problems/E1065/_index|E1065]],
[[problems/diophantine_problems/E1072/_index|E1072]].

## E1056: factorial reflection has bounded orbits

The target is one prime for each k and k adjacent nonempty intervals of product
1. Their union avoids multiples of p and translates into a single residue block.
Equal nonzero factorial residues at indices 0<=a_0<...<a_k<=p-1 give intervals
(a_(i-1),a_i] of product 1; conversely successive division gives equal
factorials. The index 0!=1 permits {1}. Excluding that singleton changes a
finite count by at most one and not the all-k question.

Wilson gives

$$
n!\,(p-1-n)!\equiv(-1)^{n+1}\pmod p.
$$

For odd n with n! congruent to 1, reflection R(n)=p-1-n preserves that residue
and odd parity. But R is an involution: iterating it cannot give an unbounded
orbit. The tetrad construction uses two seeds 1,q and their reflections, at most
four indices, or five including 0!.

Its known infinitude argument can be checked directly. Take q=6t+1>=7 and a
prime divisor p of q!-1. Then p>q and q! is 1 modulo p. Both q+2 and 2q+1 are
composite multiples of 3. Thus 1,q,p-1-q,p-2 are distinct positive odd indices
with factorial residue 1. As q grows, p>q gives unbounded primes. This proves
three intervals under the sources' convention and four including {1}, not
arbitrary k. Next test: unboundedly many seed factorials sharing a nonzero
residue at the *same* prime. Stop at varying p or reflecting a fixed seed set.
The existing tetrad claim is the proper home.

## E1065: control of the whole cofactor is missing

Both questions require infinitely many odd primes p, another positive prime q,
and nonnegative exponents, with p-1=2^k q or p-1=2^k3^l q. Guy B46's
largest-prime-factor wording is equivalent. In the first case the odd part of
p-1 is either one prime to exponent one or 1; the latter uses q=2. In the
second, the part supported above 3 is either one prime to exponent one or 1.
Small q=2,3 cause no discrepancy: removing the largest factor still leaves a
2,3-smooth integer.

A large-P(p-1) theorem bounds the *size* of the complementary factor, not its
prime support. Even a cofactor bound p^delta eventually permits 10, which is not
2,3-smooth. Allowing two unrestricted large prime factors in p-1 likewise leaves
one too many. Fixing k=1 would make the first assertion follow from infinitely
many Sophie Germain primes, but that is an extra unproved simultaneous-primality
premise. Dirichlet supplies p in a progression without making its quotient q
prime; varying exponents does not remove this gap. Next test: a theorem
controlling the smoothness of the entire cofactor. Stop if an unrestricted odd
factor remains, or a prime above 3 for the second question. The equivalence
belongs on E1065; no new infinitude result is retained.

## E1072: existing infinitude is on the other side

The targets concern the first factorial attaining -1: infinitely many f(p)=p-1,
and f(p)/p->0 outside a relative-density-zero set of primes. Indices are
nonnegative; allowing 0! affects only p=2. Wilson gives existence, not either
distribution assertion.

Hardy--Subbarao Theorem 2.1 gives infinitely many primes with n! congruent to -1
and p not congruent to 1 modulo n. Since n=p-1 has p congruent to 1 modulo n,
this forces f(p)<p-1. It concerns the complementary primes, with no density
bound. Problem G states the targets as beliefs; Problem C's unbounded factorial
multiplicity is also a question, not a theorem.

A direct strengthening still falls short. For any odd m>=3 take p dividing m!+1.
Then p>m, p is odd, and m! is -1 modulo p. Wilson reflection gives (p-1-m)! also
-1. Both indices are positive, since m cannot be the even number p-1, and their
minimum is at most (p-1)/2. Thus f(p)<p/2 for an unbounded set of primes, as
p>m. This proves neither a ratio tending to zero nor an almost-all-primes
assertion. Next test: estimate the proportion with first hit above epsilon p for
every epsilon>0, or construct infinitely many primes with *no* earlier hit. Stop
at infinitude of non-extremal primes.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/integer_sequences/hardy_2002_modified_problem_pillai_related_questions/_index|hardy
  2002 modified problem pillai related questions]]: Problems C and G and
  no-proof qualification (statement reading). Section 2 Theorem 2.1 with proof
  and Remark 2.8; Section 3 Problems C and G (proof reading). Theorem 2.1 and
  Remark 2.8 reflection mechanism; Section 3 Problem C (account reading).
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy
  2004 unsolved problems number theory]]: B46 opening question, printed p.154
  (statement reading).
