---
name: problems/integer_sequences/E0432
title: Problem 432
desc: |
  Asks how dense $A+B$ can be for infinite sets $A,B\subseteq\mathbb{N}$ when
  the elements of $A+B$ are pairwise coprime.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 432

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $A,B\subseteq \mathbb{N}$ be two infinite sets. How dense can
$A+B$ be if all elements of $A+B$ are pairwise relatively prime?

**Status.** Open, the erdosproblems.com label (OPEN). A comment of 23 June 2026
on the erdosproblems.com discussion thread links Sungchul Lee's manuscript *On
the Density of Pairwise Coprime Sumsets*
([GitHub](https://github.com/lsngchl/Erdos432/blob/37d60fd8142f933f3a5679b072f78696b7d4e013/2026-06-23_Erdos432.pdf)).
The author used OpenAI's GPT-5.5 Pro to explore proof strategies. Write
$S(x)=|(A+B)\cap[1,x]|$. The manuscript proves $S(x)\le\pi(x)$ whenever the
distinct elements of $A+B$ are pairwise coprime. It constructs infinite $A,B$
with pairwise coprime sums and $S(x)\gg(\log x/\log\log x)^2$ for all large
$x$. For every $F(x)=x^{o(1)}$, it constructs infinite $A,B$ with
$S(x_j)\ge F(x_j)$ along a sequence $x_j\to\infty$. Assuming the
Hardy--Littlewood prime-tuples conjecture, for every $\omega(x)\to\infty$ it
gives $A,B$ whose sums are distinct primes, with
$S(x_j)\ge x_j/(\log x_j)^{\omega(x_j)}$ along a sequence. These bounds settle
no instance of the question, so the manuscript has no claim page.

**Source.** [erdosproblems.com/432](https://www.erdosproblems.com/432), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #432,
https://www.erdosproblems.com/432.

**Formalization.** None recorded.

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

Let $A,B$ be infinite positive-integer sets, with distinct elements of $S=A+B$
pairwise coprime. At most one element of $S$ is even. An infinite parity class
of $A$ would give infinitely many even sums if $B$ contained that parity. So all
of $B$ has the opposite parity. Since $B$ is infinite, the same argument forces
all of $A$ to have the original parity. Every sum is therefore odd.

If $p\mid a+b$, then
$$
 A\cap(a+p\mathbb Z)=\{a\},\qquad
 B\cap(b+p\mathbb Z)=\{b\};
$$
another member would give a distinct sum sharing $p$.
Choosing a prime divisor of each distinct sum is an injection into the
primes, giving $S(x)\le\pi(x)$ (one may exclude 2).
This does not assume unique representations of a sum. If 0 is permitted
and 1 occurs as a sum, the count needs an additional 1; the nonunit
argument is unchanged.

These restrictions are too weak for the requested growth bounds. The Lee
manuscript linked by the problem page was not read; no argument here depends on
its reported claims.

The unresolved obligation is to exploit several translates jointly to improve
the prime-divisor injection bound. A useful test is to check whether two fixed
translates give a uniform density saving beyond the local exclusions, without
assuming prime-tuples conjectures. Stop if a count of representations is
substituted for distinct sums or a conditional construction is treated as
unconditional.
