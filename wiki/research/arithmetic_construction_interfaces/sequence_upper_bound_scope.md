---
name: research/arithmetic_construction_interfaces/sequence_upper_bound_scope
title: Binomial-divisibility bounds and the formal improvement question
desc: |
  White's pending upper bound supplies the formal little-o improvement
  in Problem 1063. The stronger claimed LEAP formula has the same target
  interface; its proof fidelity and the sharp growth remain separate.
created: 2026-10-14T22:16:04Z
updated: 2026-10-18T10:11:03Z
---

# Binomial-divisibility bounds and the formal improvement question

***

For $k\ge2$, [[problems/integer_sequences/E1063/_index|Problem 1063]]
defines $n_k$ as the least $n\ge2k$ such that exactly one of the integers
$n-i$, $0\le i<k$, fails to divide $\binom nk$. It asks to estimate $n_k$.
The [[problems/integer_sequences/E1063/claims/2026_10_01_leap|LEAP claim]]
records an external Lean proof of a better upper bound, with status claimed.
That proof has not been built or audited by this account.

The
[formal-conjectures statement](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1063.lean),
read on 2026-10-14, asks in `erdos_1063.better_upper` for a function $U$ such
that

$$
n_k=O(U(k)),\qquad
U(k)=o\!\left(k\operatorname{lcm}(1,\ldots,k-1)\right).
$$

The same file's `erdos_1063.variants.subexponential_upper_bound` states the
conjunction of those two properties for

$$
U(k)=\exp\!\left(\frac{k}{\log k}
  (\log\log k+\log\log\log k+\log2)\right).
$$

Only sufficiently large $k$ matters to either asymptotic assertion; arbitrary
finite initial values can be assigned if the real formula is left undefined
there. Thus the variant, if its claimed proof is valid, answers the formal
existence question by taking exactly this $U$. There is no further estimate
to derive and no finite complement to test. The formula matches the explicit
claim already recorded on the problem's claim page; this is a statement-level
specialization, not a new proof of that claim.

The comparator must use the natural-number least common multiple before
casting to the reals. The current formal file explicitly warns that placing
the real type annotation inside the lcm operation changes it to a real lcm
and collapses the nonzero comparison to $k$. The statement comparison here
uses the displayed natural-number version; fidelity of the linked external
proof to that version is part of the unperformed proof examination.

The distinction matters for the request to estimate $n_k$: this bound does
not determine the sequence's sharp growth. Whether the formal improvement is
the whole definite question being evaluated must be stated separately from
whether the external proof is correct. The formal file's solved tag and proof
pointer are not a local verification. The remaining proof obligation is the
external theorem with its least-value definition, exceptional-divisor
condition, natural-number least common multiple and both asymptotic conjuncts
intact. A formulation check can settle the witness specialization; it must
stop at that external proof dependency and cannot award
acceptance or an asymptotic formula.


## Independently examined upper bound

[[problems/integer_sequences/E1063/claims/2026_07_25_white|White's pending bound]]
supplies $\log n_k=o(k)$ and
$n_k=o(k\operatorname{lcm}(1,\ldots,k-1))$ under its explicit classical
interfaces. Its whole-proof review and separate passing grade cover these
consequences as well as the eventual quantitative bound. Thus the formal
little-o improvement has a witness from this result, pending sign-off. The
conditional statement comparison for the stronger LEAP formula above remains
limited to that claim's interface and does not inspect its external proof.
Neither result in this account specifies the sharp growth of $n_k$.
