---
name: problems/factorials_binomials/E0401/claims/2026_01_10_sothanaphan
title: Sothanaphan's disproof of the reading with all large n
desc: |
  Answers a variant (the inequality for all sufficiently large $n$), not the
  Statement (for infinitely many $n$), so it does not count toward the
  problem's standing. Nat Sothanaphan's thread post, with an argument found by
  ChatGPT, claims that for $r\ge2$ and $n=p_{r+1}^k-1$ every admissible pair
  has $a_1+a_2\le n+2p_{r+1}$.
authors:
- Nat Sothanaphan
status: rejected
claim: disproved
scope: full
submitted: 2026-01-10
links:
- url: https://www.erdosproblems.com/forum/thread/401#post-2914
  kind: discussion
  date: 2026-01-10
- url: https://chatgpt.com/share/6962a547-7fb0-8010-bfca-f3a9171e95b7
  kind: discussion
  date: 2026-01-10
created: 2026-10-14T00:55:25Z
updated: 2026-10-14T00:55:25Z
---

***

**Claim.** Nat Sothanaphan's post of 10 January 2026 in the discussion thread
of [[problems/factorials_binomials/E0401/_index|Problem 401]] claims that the
inequality cannot hold for all sufficiently large $n$. For $r\ge2$ and every
$n=p_{r+1}^k-1$, where $p_{r+1}$ is the $(r+1)$-th prime, any $a_1,a_2$ with
$a_1!a_2!\mid n!\,2^n3^n\cdots p_r^n$ have $a_1+a_2\le n+2p_{r+1}$, so no
$f(r)\to\infty$ gives $a_1+a_2>n+f(r)\log n$ for every large $n$. The argument
is the ChatGPT conversation linked from the post, which uses Kummer's theorem;
the post says that the poster checked it by hand and had pointed ChatGPT to
Problems 728 and 729 and to Kummer's theorem.

**Submission note.** Posted to the erdosproblems.com forum by Nat Sothanaphan on
10 January 2026:

> I am happy to announce that the "all $n$" version is false!
>
> Specifically, ChatGPT shows that taking $n = p_{r+1}^k - 1$ we must have
> $a_1+a_2-n \le 2p_{r+1}$ for $r \ge 2$. Thus in fact $\omega(r) = 0$ for all
> $r \ge 2$. I have checked the argument manually; it is pretty readable. It's
> not autonomous because I gave a hint to look at #728, #729 and to use Kummer.
> ChatGPT took $27+13=40$ minutes.

**Why it is rejected.** It answers a variant, not the Statement. Erdős and
Graham's source leaves the quantifier on $n$ open, and the erdosproblems.com
wording when the post was made asked for the inequality for all sufficiently
large $n$; the erdosproblems.com curator wrote in the thread the next day that
this wording was a misreading of the source and that the reading with infinitely
many $n$ was intended.
[[problems/factorials_binomials/E0401/_index|Problem 401]] states that reading.
A bound on $a_1+a_2$ along the sparse sequence $n=p_{r+1}^k-1$ refutes the
inequality for all large $n$ but says nothing about the other $n$, and the
problem asks only for infinitely many, so its mathematics answers the variant
and does not settle this problem; the value `disproved` is its answer to that
variant.

**Standing.** Rejected, as answering a variant. The thread records the
poster's own check of the argument and no other review, and this corpus has
not checked it.

**Depends on.** No page of this wiki.
