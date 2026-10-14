---
name: problems/number_theory/E0981/claims/2025_12_27_tang_zhang
title: Tang and Zhang's asymptotic for the first-passage threshold
desc: |
  Answers a variant (the site's earlier first-passage threshold), not the
  Statement (the eventual-time threshold), so it does not count toward the
  problem's standing. Quanyu Tang and Hao Zhang's preprint proves
  $\sum_{p\le x}f_\epsilon(p)\sim c_\epsilon x/\log x$ for
  $f_\epsilon(p)=\min\{\ell:S_\ell(p)<\epsilon\ell\}$.
authors:
- Quanyu Tang
- Hao Zhang
status: rejected
claim: proved
scope: full
submitted: 2025-12-27
links:
- url: https://www.erdosproblems.com/forum/thread/981#post-2457
  kind: discussion
  date: 2025-12-27
- url: https://github.com/QuanyuTang/erdos-problem-981/blob/main/Erd%C5%91s_Problem_981.pdf
  kind: preprint
  date: 2025-12-27
- url: https://arxiv.org/abs/2512.24631
  kind: preprint
  date: 2025-12-31
created: 2026-10-14T00:55:25Z
updated: 2026-10-14T00:55:25Z
---

***

**Claim.** Quanyu Tang and Hao Zhang, *Average first-passage times for
character sums*, arXiv:2512.24631 (v1 31 December 2025, v2 18 January 2026;
carded as
[[../library/number_theory/tang_2025_average_first_passage_times_character_sums/_index|Tang and Zhang 2025]]),
first posted as a PDF on 27 December 2025 in the discussion thread of
[[problems/number_theory/E0981/_index|Problem 981]], proves in its
[[../library/number_theory/tang_2025_average_first_passage_times_character_sums/theorem_1_2|Theorem 1.2]]
that for every $\epsilon>0$, with $p$ an odd prime,
$S_\ell(p)=\sum_{n\le\ell}(n/p)$ and the first-passage time
$f_\epsilon(p)=\min\{\ell\ge1:S_\ell(p)<\epsilon\ell\}$, there is a constant
$c_\epsilon\in(0,\infty)$ with
$\sum_{p\le x}f_\epsilon(p)\sim c_\epsilon x/\log x$. The post presents the
paper as resolving the formulation then stated on the site, and records that
Erdős's original display (80) is the eventual-time problem, which Elliott's
1969 paper resolves, and that the eventual-time asymptotic does not imply the
first-passage one.

**Submission note.** Posted to the site's forum by Quanyu Tang on 27 December
2025:

> In joint work with Hao, we wrote a paper resolving the formulation currently
> stated on this page (the “first-passage time” version), proving that
> \(\sum_{p\le x} f_\varepsilon(p)\sim c_\varepsilon x/\log x\). Since our arXiv
> submission is not yet publicly announced due to the holiday schedule, I am
> temporarily posting a preprint PDF (and TeX source) in my GitHub page here. (I
> will update this comment with the arXiv link as soon as it becomes public; I’m
> posting this now mainly to help avoid duplicated effort over the next couple
> of days.)
>
> Along the way we encountered an unexpected twist, so let me briefly explain
> the story.
>
> 1. Solving the page’s formulation (Problem 1). We first proved the asymptotic
>    for the quantity \(f_\varepsilon(p)\) as defined on this page. Our approach
>    avoids the potential pitfall highlighted by Terence Tao (18:42 on 01 Oct
>    2025); unfortunately, I did not see the earlier comment at 18:09, which has
>    since been deleted. At that point we began preparing a write-up.
>
> 2. Erdős’s original formulation is different (Problem 2). While writing the
>    Introduction, we checked Erdős’s original statement in [Er65b, Eq. (80)]
>    and realized it is a genuinely different “eventual-time” problem. Namely,
>    for \(\varepsilon>0\) and each odd prime \(p\), let \(F_\varepsilon(p)\) be
>    the least integer such that\[S_\ell(p)<\varepsilon \ell \qquad \text{for
>    every }\ell\ge F_\varepsilon(p).\]Erdős asked whether there exists
>    \(C_\varepsilon>0\) such that\[\sum_{p\le x} F_\varepsilon(p)\sim
>    C_\varepsilon \frac{x}{\log x}.\]Thus Problem 2 concerns an eventual-time
>    threshold, whereas Problem 1 concerns a first-passage threshold.
>
> 3. Literature search: Problem 2 was already solved by Elliott. We then
>    searched the literature to see whether Erdős’s eventual-time formulation
>    (Problem 2) had already been solved. I asked ChatGPT three times to search
>    for relevant references, but none of them turned up anything relevant. I
>    then searched manually on Google Scholar (using the keywords “conjecture
>    character sums”) and found the following paper:
>
> [El69] Elliott, P. D. T. A. "A CONJECTURE OF ERDiiS CONCERNING CHARACTER
> SUMS." (1969).
>
> This paper is difficult for AI tools to retrieve because it is hosted on
> ScienceDirect behind a human-verification gate, which likely explains why it
> did not appear in our earlier AI-assisted searches. After accessing it
> manually, we confirmed that it indeed resolves Problem 2.
>
> 4. Why our result is still new. Although one clearly has \(f_\varepsilon(p)\le
>    F_\varepsilon(p)\) for each \(p\), an asymptotic formula for \(\sum_{p\le
>    x}F_\varepsilon(p)\) does not by itself imply the corresponding asymptotic
>    for \(\sum_{p\le x} f_\varepsilon(p)\). To the best of our knowledge, the
>    first-passage version (Problem 1) was previously open, and our paper
>    establishes the claimed asymptotic.

**Why it is rejected.** It answers a variant, not the Statement. When the post
was made, the site's page defined $f_\epsilon(p)$ as the first-passage time
$\min\{m:S_m(p)<\epsilon m\}$; the site corrected the page the same day to
Erdős's eventual-time threshold, the least $m$ with $S_N(p)<\epsilon N$ for
every $N\ge m$, which is the Statement of
[[problems/number_theory/E0981/_index|Problem 981]]. The first-passage time
is at most the eventual-time threshold for each $p$, but, as the paper itself
notes, an asymptotic for the sum of one does not by itself give an asymptotic
for the sum of the other, so its mathematics answers the variant and does not
settle this problem; the value `proved` is its answer to that variant.

**Standing.** Rejected, as answering a variant. The preprint is unrefereed;
Terence Tao replied the same day that ChatGPT Pro, through which he had run
the paper, raised a fixable issue with the odd-primes convention and no major
concern, which is a thread comment, not a review. The site's commentary
credits the variant to the paper. This corpus has checked Theorem 1.2's
statement clause by clause and not its proof.

**Depends on.** No page of this wiki.
