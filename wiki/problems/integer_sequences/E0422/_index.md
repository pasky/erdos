---
name: problems/integer_sequences/E0422
title: Problem 422
desc: |
  Asks how the sequence given by $f(1)=f(2)=1$ and
  $f(n)=f(n-f(n-1))+f(n-f(n-2))$ behaves, and whether it misses infinitely many
  integers.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 422

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $f(1)=f(2)=1$ and for $n>2$

$$
f(n) = f(n-f(n-1))+f(n-f(n-2)).
$$

Does $f(n)$ miss infinitely many integers? What is its behaviour?

**Status.** Open.

**Source.** [erdosproblems.com/422](https://www.erdosproblems.com/422), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #422,
https://www.erdosproblems.com/422.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/422.lean).

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

For the exact Hofstadter Q recurrence
$f(1)=f(2)=1$,
$$
 f(n)=f(n-f(n-1))+f(n-f(n-2)),
$$
direct substitution gives, for $1\le n\le16$,
$$
 1,1,2,3,3,4,5,5,6,6,6,8,8,8,10,9.
$$
All indices used are positive and earlier. In particular
$f(12)=f(6)+f(6)=8$,
$f(15)=f(7)+f(7)=10$, and
$f(16)=f(6)+f(8)=9$.
Global monotonicity and a bound of 1 on every upward increment therefore
both fail. This is a finite calculation, not eventual evidence.

An invariant $f(j)\le j$ would keep subsequent indices positive,
but direct induction does not close: that hypothesis only gives
$$
 f(n)\le2n-f(n-1)-f(n-2),
$$
which requires the additional $f(n-1)+f(n-2)\ge n$ to be at most
$n$. No invariant establishing all required inequalities is proved here.

Fox's [arXiv:1609.06342 abstract](https://arxiv.org/abs/1609.06342v1) was read
to distinguish the original initial values from other solutions. Regular
alternative initial-value solutions do not prove eventual behavior for this one.
Their symbolic algorithm and proofs were not inspected.

The unresolved obligation is to prove a global index-validity invariant for the
exact initial conditions before inferring any eventual behavior. A useful test
is to try to close an explicit inductive envelope and check every delayed
argument; any proposed monotone or step-1 envelope already fails at 12 or 16.
Stop at unproved total existence, an unbounded delayed-history state, or
numerical generation patterns.
