---
name: problems/diophantine_problems/E0261/claims/2026_04_27_zeraoulia
title: Zeraoulia's rational with two representations
desc: |
  Answers a variant (Erdős's weakened question, a rational with two
  representations), not the Statement (a rational with $2^{\aleph_0}$
  representations), so it does not count toward the problem's standing. Rafik
  Zeraoulia's thread post claims that $7/4$ has two representations.
authors:
- Rafik Zeraoulia
status: rejected
claim: proved
scope: full
published: 2026-04-27
submitted: 2026-04-27
links:
- url: https://www.erdosproblems.com/forum/thread/261#post-5959
  kind: discussion
  date: 2026-04-27
created: 2026-10-14T00:55:25Z
updated: 2026-10-14T00:55:25Z
---

***

**Claim.** Rafik Zeraoulia's post of 27 April 2026 in the discussion thread of
[[problems/diophantine_problems/E0261/_index|Problem 261]] claims a positive
answer to the weakened question of Erdős's 1988 paper, whether some rational
$x$ has two representations $x=\sum_{a\in A}a/2^a$ over sets $A$ of distinct
positive integers. From $4/2^4=5/2^5+6/2^6$ and $\sum_{m\ge1}m/2^m=2$, the
rational $7/4$ is the sum over $\mathbb N\setminus\{5,6\}$ and over
$\mathbb N\setminus\{4\}$. The post notes that the two representations share a
large common tail and that a stronger non-degeneracy condition would make a
different question.

**Submission note.** Posted to the erdosproblems.com forum by Rafik Zeraoulia on
27 April 2026:

> I would like to point out a small observation about the weakened question
> mentioned in [Er88c], namely the existence of a rational number \(x\) which
> has two representations.
>
> Interpreting a representation as a choice of a set \(A\subseteq \mathbb N\) of
> distinct positive integers, so that\[ x=\sum_{a\in A}\frac{a}{2^a}, \]one gets
> such an example from the finite identity\[
> \frac{4}{2^4}=\frac{5}{2^5}+\frac{6}{2^6}. \]Both sides are equal to \(1/4\).
>
> Now use the classical identity\[ \sum_{m=1}^{\infty}\frac{m}{2^m}=2. \]Let\[
> A=\mathbb N\setminus\{5,6\}, \qquad B=\mathbb N\setminus\{4\}. \]Then\[
> \sum_{a\in A}\frac{a}{2^a} = 2-\frac{5}{2^5}-\frac{6}{2^6} = 2-\frac14 =
> \frac74, \]whereas\[ \sum_{b\in B}\frac{b}{2^b} = 2-\frac{4}{2^4} = 2-\frac14
> = \frac74. \]Therefore the rational number\[ x=\frac74 \]has two different
> representations:\[ \frac74 = \sum_{a\in \mathbb
> N\setminus\{5,6\}}\frac{a}{2^a} = \sum_{b\in \mathbb
> N\setminus\{4\}}\frac{b}{2^b}. \]Thus, under this literal interpretation, the
> weakened question has a positive answer. Of course, this uses two
> representations with a large common tail; if the intended question requires
> some stronger non-cancellation or non-degeneracy condition, then that would be
> a different version.

**Why it is rejected.** It answers a variant, not the Statement. The third
question of [[problems/diophantine_problems/E0261/_index|Problem 261]] asks for
a rational with at least $2^{\aleph_0}$ representations. Erdős's 1988 paper asks
only for a rational with two, a weakening that the problem page records as a
variant and that, as a reply in the thread reports, is generally believed to be
a misprint for $2^{\aleph_0}$. Two representations of $7/4$ say nothing about
whether any rational has $2^{\aleph_0}$ of them, and nothing about the first two
questions, so its mathematics answers the variant and does not settle this
problem; the value `proved` is its answer to that variant.

**Standing.** Rejected, as answering a variant. The identities are elementary
and the thread disputes none of them; this corpus has not checked them.
formal-conjectures marks its variant `erdos_261.variants.two_representations`
research solved and cites a Lean proof that follows the post; this corpus
has not built it.

**Depends on.** No page of this wiki.
