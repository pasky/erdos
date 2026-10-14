---
name: problems/arithmetic_functions/E0417
title: Problem 417
desc: |
  Asks whether the ratio of the number of totient values up to $x$ to the number
  of distinct values $\phi(m)$ with $m\le x$ has a limit, and whether that limit
  exceeds 1; open.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-07T20:31:26Z
---

# Problem 417

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0417/claims/_index|claims/]]: The 0 claim pages of Problem 417, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let

$$
V'(x)=\#\{\phi(m) : 1\leq m\leq x\}
$$

and

$$
V(x)=\#\{\phi(m) \leq x : 1\leq m\}.
$$

Does $\lim V(x)/V'(x)$ exist? Is it $>1$?

**Formulation.** The second question, whether the limit is $>1$,
presupposes the first. It is read as the formal-conjectures statement linked
under Formalization states it (`erdos_417.parts.ii`): whether $V(x)/V'(x)$
tends to a limit $L>1$, possibly infinite, so a yes to it includes a yes to
the first.

**Status.** Open. Bloom's catalog labeled the problem OPEN, and the derived
standing is open. The erdosproblems.com proof-claims thread carried no claim on
2026-10-06. No claim page is recorded, since no one claims either question.
Theorem 2.2 of the OpenAI release manuscript of 25 September 2026 bears on the
problem without claiming it. With $k=1$ it implies, by a deduction drawn here,
that $\liminf V(x)/V'(x)>1$, so any limit would exceed $1$; the theorem is
unrefereed, and whether the limit exists stays open. The Current assessment
records this item, the deduction and why neither is a claim.

**Source.** [erdosproblems.com/417](https://www.erdosproblems.com/417), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #417,
https://www.erdosproblems.com/417.

**References.**

- [Er98] Erdős, Paul, Some of my new and almost new problems and results in
  combinatorial number theory. Number theory (Eger, 1996) (1998), 169-180.

**Formalization.** Statement in the file
[`ErdosProblems/417.lean`](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/417.lean)
of formal-conjectures, pinned at its last change of 18 September 2026:
`erdos_417.parts.i` (the existence of the limit) and `erdos_417.parts.ii` (a
limit exceeding $1$), each an `answer(sorry)` equivalence marked
`research open` with no `formal_proof` attribute.

## Current assessment

**The question (erdosproblems.com formulation, 2026-09-04).** Whether
$\lim V(x)/V'(x)$ exists and whether it exceeds $1$. OPEN. The erdosproblems.com
commentary records that $V'(x)\le V(x)$ trivially and that Erdős [Er98]
suggested the limit may be infinite.

**Standing.** No claim page: no one claims either question, and the derived
standing is open.

**The OpenAI release item (family 024).** Theorem 2.2 of the release
manuscript of 25 September 2026, *An asymptotic formula for the number of
totients*
([[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|intake card]],
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/theorem_2_2|Theorem 2.2 page]]),
claims, for each fixed $k\ge1$, an asymptotic for
$N_k(x)=\#\{v\le x\text{ totient}:kx<\ell(v)\le(k+1)x\}$, with $\ell(v)$
the least preimage of $v$, and that $N_k(x)$ is of order $V(x)$ for $k=1$
and $2$; the manuscript is unrefereed, and this corpus has not built the
release's Lean for these counts (`weighted_totient_asymptotic`,
`weighted_totient_one_two`). The manuscript does not mention $V'$ or this
problem, and the release claims nothing about it, so the item is recorded here
and not as a claim.

**A consequence drawn here.** Every value $\phi(m)$ with $m\le x$ is at most
$x$, so $V'(x)$ counts the totients $v$ with $\ell(v)\le x$, and $V(x)-V'(x)$
counts the totients $v\le x$ with $\ell(v)>x$, which is
$\sum_{k\ge1}N_k(x)\ge N_1(x)$. If Theorem 2.2 holds, its first alternative for
$k=1$ gives $N_1(x)\ge cV(x)$ for some $c>0$ and all large $x$, so
$V'(x)\le(1-c)V(x)$ and $\liminf V(x)/V'(x)\ge1/(1-c)>1$. With
$V(x)\asymp V'(x)$ under Known Results, any limit of $V(x)/V'(x)$ would then be
finite and greater than $1$. The Theorem 2.2 page draws the same inference. This
answers neither question, since whether the limit exists stays open, but if
Theorem 2.2 holds, a yes to the first question is also a yes to the second. The
deduction rests on the unrefereed Theorem 2.2, whose Lean this corpus has not
built, and it is not a claim, since neither the release nor anyone else claims
the problem.

**Search scope.** The erdosproblems.com page and its proof-claims thread (empty
on 2026-10-06), the formal-conjectures statement file and the OpenAI release at
the pinned revision of its manuscript; no other literature search was made, and
no proof was independently assessed.

## Known Results

The ratio $V(x)/V'(x)$ is bounded: Pollack, Pomerance and Treviño quote
$V(x)\asymp V'(x)$ from Ford on p. 7 of their manuscript, which excludes the
infinite limit erdosproblems.com reports Erdős suggested.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|openai_2026_asymptotic_formula_number_totients]]
- [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/theorem_2_2|openai_2026_asymptotic_formula_number_totients / theorem_2_2]]

<!-- END problem library links -->
