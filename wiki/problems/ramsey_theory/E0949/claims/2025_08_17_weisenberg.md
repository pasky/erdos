---
name: problems/ramsey_theory/E0949/claims/2025_08_17_weisenberg
title: Weisenberg's counterexample to the wording asking for a set closed under addition
desc: |
  Answers a variant (erdosproblems.com's earlier wording, asking for $A$ with
  $A+A\subseteq A$), not the Statement ($A+A\subseteq\mathbb R\setminus S$), so
  it does not count toward the problem's standing. Desmond Weisenberg claims a
  sum-free union of intervals whose complement has no uncountable subset
  closed under addition.
authors:
- Desmond Weisenberg
status: rejected
claim: disproved
scope: full
submitted: 2025-08-17
links:
- url: https://www.erdosproblems.com/forum/thread/949#post-108
  kind: discussion
  date: 2025-08-17
created: 2026-10-14T00:53:37Z
updated: 2026-10-14T00:53:37Z
---

***

**Claim.** Desmond Weisenberg, in a post of 17 August 2025 in the discussion
thread of [[problems/ramsey_theory/E0949/_index|Problem 949]], claims the
answer no to the erdosproblems.com wording of that time, which asked for a set
$A\subseteq\mathbb R\setminus S$ of cardinality continuum with
$A+A\subseteq A$. The counterexample is
$S=\bigcup_{n\in\mathbb Z}[3n+1,3n+2)$, which is sum-free; every
$a\notin S$ that is not a multiple of $3$ has a multiple in $S$, so the
subsets of $\mathbb R\setminus S$ closed under addition are sub-semigroups of
$3\mathbb Z$, all countable. A later edit of the post says that the corrected
problem asks for $A+A\subseteq\mathbb R\setminus S$, which the construction
does not resolve.

**Submission note.** Posted to the erdosproblems.com forum by Desmond Weisenberg
(account DesmondWeisenberg) on 17 August 2025:

> The answer is no. Let $S$ be the set of all intervals of the form $[3n+1, 3n
> + 2)$, with $n \in \mathbb{Z}$. Then $S$ is sum-free. Furthermore, if $a \in
> \mathbb{R}\backslash S$ and $a$ is not a multiple of $3$, then $a$ has a
> multiple in $S$. As such, the only subsets of $\mathbb{R}\backslash S$ that
> are closed under addition are the sub-semigroups of $3\mathbb{Z}$, so
> $\mathbb{R}\backslash S$ certainly has no uncountable subsets that are closed
> under addition.
>
> The website mentions the variant where we instead require that $S$ is Sidon.
> That's probably a lot harder, and my construction is very much not Sidon.
>
> EDIT: Vjeko pointed out that the problem should actually ask about $A$ such
> that $A + A \subseteq \mathbb{R}\backslash S$, not $A + A \subseteq A$. So my
> construction actually doesn't resolve the corrected problem.

**Why it is rejected.** It answers a variant, not the Statement. The
construction answers erdosproblems.com's earlier wording, which asked for $A$
closed under addition. [[problems/ramsey_theory/E0949/_index|Problem 949]] asks,
as Erdős did and as the erdosproblems.com wording corrected on 17 and 18 August
2025 does, for $A\subseteq\mathbb R\setminus S$ of cardinality continuum with
$A+A\subseteq\mathbb R\setminus S$, and its Formulation sets the earlier wording
aside. For the construction's $S$ that question has the answer yes, with
$A=[0,1/2)$, so the counterexample settles no instance of it; its mathematics
answers the variant and does not settle this problem. The value `disproved` is
its answer to that variant.

**Standing.** Rejected, as answering a variant. The thread's next comment
pointed out the mismatch with Erdős's wording and gave a set $A$ that works
for this $S$, and the author replied that no counterexample to the corrected
formulation was at hand. This corpus has not checked the construction beyond
what the problem page records.

**Depends on.** No page of this wiki.
