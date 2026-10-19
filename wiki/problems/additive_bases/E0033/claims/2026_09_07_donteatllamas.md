---
name: problems/additive_bases/E0033/claims/2026_09_07_donteatllamas
title: "donteatllamas's upper bound: the smallest limsup is at most 13 sqrt 2/4"
desc: |
  An unsigned three-page write-up, posted on the erdosproblems.com forum on
  7 September 2026 by the user donteatllamas and made with the help of GPT,
  builds a complement of the squares on the scales $3^k$ with limsup at most
  $13\sqrt2/4\approx4.596$. No review is known, so the claim is pending.
authors: []
status: claimed
claim: proved
scope: partial
published: 2026-09-07
submitted: 2026-09-07
links:
- url: https://www.erdosproblems.com/forum/thread/33#post-8879
  kind: discussion
  date: 2026-09-07
- url: https://github.com/LeanMeanBean/erdos-33/blob/132f71eeb57427f18b8050e780ed49bcf5d68917/erdos33_limsup_4_596.pdf
  kind: preprint
  date: 2026-09-07
created: 2026-10-18T03:06:13Z
updated: 2026-10-18T03:06:13Z
---

***

**Claim.** There is a set $A$ of positive integers such that every
sufficiently large integer is $n^2+a$ with $n\ge0$ and $a\in A$, and

$$
\limsup_{x\to\infty}\frac{A(x)}{\sqrt x}\le\frac{13\sqrt2}{4}\approx4.596,
$$

where $A(x)$ counts the elements of $A$ up to $x$. Hence the smallest possible
value of the limsup in the first question of
[[problems/additive_bases/E0033/_index|Problem 33]] is at most $13\sqrt2/4$.
The write-up, an untitled and unsigned three-page PDF posted with its LaTeX
source in a public GitHub repository (the preprint link, pinned to its upload
commit of 7 September 2026), builds $A$ scale by scale. For $q=3^k$ and
$L_k=(q^2+3)/4$ it takes from $[L_k,L_{k+1})$ the integers congruent to $0$,
$1$ or $2$ modulo $q$ below $q^2$, those congruent to $0$, $1$, $2$, $q$,
$q+1$ or $q+2$ modulo $3q$ in $[q^2,2q^2)$, and those congruent to $0$, $1$ or
$2$ modulo $3q$ from $2q^2$ on, together with finitely many small integers.
Coverage rests on square roots modulo $q$ of the residues congruent to $1$
modulo $3$, lifted by Hensel's lemma. A large $m$ below $q^2$ is reached
through one root $r$; above $q^2$ the write-up uses two or three of the roots
$r$, $q-r$ and $q+r$, whose remainders $m-r^2$, $m-(q-r)^2$ and $m-(q+r)^2$
lie in different classes modulo $3q$. Counting with $x=yq^2$ gives
$A(x)/\sqrt x=2\sqrt y+5/(2\sqrt y)+o(1)$ for $1\le y\le2$, which is largest
at $y=2$, where it equals $13/(2\sqrt2)$; the ranges $1/4\le y\le1$ and
$2\le y\le9/4$ give at most this.

**Submission note.** Posted to the erdosproblems.com forum by donteatllamas
(account llamaboy) on 7 September 2026, in the problem's thread:

> With the help of GPT, I think I can improve the $\limsup \frac{\lvert
> A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}$ bound to $\frac{13\sqrt{2}}{4}$. The
> proof is formalized here.

**Covers.** An upper bound of $13\sqrt2/4\approx4.596$ for the smallest
possible limsup, the first question of
[[problems/additive_bases/E0033/_index|Problem 33]]. The claim does not
determine the smallest limsup and asserts no optimality of its set. The liminf
question is not covered.

**Claimant and assistance.** The write-up prints no author's name. The forum
user donteatllamas (account llamaboy) posted it, saying that it was made with
the help of GPT. The repository belongs to the GitHub account LeanMeanBean,
which gives no name, and was created on 7 September 2026. No real name is
known, so the page lists no author. The post calls the proof formalized, but
the repository holds only the PDF and its LaTeX source; no Lean file is
posted.

**Relation to the other upper bounds.** The bound lies below the
$2\varphi^{5/2}\approx6.66$ of
[[problems/additive_bases/E0033/claims/2025_08_12_van_doorn|van Doorn's construction]],
the bound the erdosproblems.com remarks record.
[[problems/additive_bases/E0033/claims/2026_10_19_plasma_ai|Plasma AI's pending claim]]
gives $9/2$, below this bound.

**Depends on.** No page of this wiki.

**Standing.** Claimed. The thread held no review of the write-up when
erdosproblems.com froze its comments on 6 October 2026, and the
erdosproblems.com remarks, last edited 27 December 2025, predate it; the
problem's proof-claims tab holds no claim (accessed 2026-10-18). There is no
refereed publication and no Lean proof, and this corpus has not checked the
argument.
