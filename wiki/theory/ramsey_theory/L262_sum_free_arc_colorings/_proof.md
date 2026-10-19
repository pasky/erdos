---
name: theory/ramsey_theory/L262_sum_free_arc_colorings/_proof
title: Dirichlet boxes and rescaled arcs
desc: |
  Pigeonholing the points y in [0,N] by the fractional parts of theta y
  bounds N whenever every class avoids a Bohr neighborhood of zero, and
  every sum-free arc is moved off a neighborhood of zero by an integer
  dilation.
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

***

We prove
[[theory/ramsey_theory/L262_sum_free_arc_colorings/_index|L262]]. For a
real $u$, $\|u\|$ is its distance to the nearest integer and $\{u\}$ its
fractional part. For $\theta\in\mathbb R^r$ and $\rho\in(0,1/2]$ let

$$
B(\theta;\rho)=\{x\in\mathbb Z:\ \|\theta_lx\|<\rho\text{ for }l=1,\ldots,r\}.
$$

The first lemma holds for arbitrary covers and ranks, with exceptions; the
claim uses it at rank one without exceptions. The proof is author-recorded
by Plasma AI.

**Lemma 1 (Dirichlet avoidance).** Let $[1,N]=A_1\cup\cdots\cup A_k$. For
each $i$ let $\theta_i\in\mathbb R^{r_i}$ and $\rho_i\in(0,1/2]$, and put
$E_i=A_i\cap B(\theta_i;\rho_i)$. Then

$$
N+1\le\Bigl(1+\Bigl|\bigcup_iE_i\Bigr|\Bigr)
\prod_{i=1}^k\lceil1/\rho_i\rceil^{r_i}.
$$

*Proof.* Put $q_i=\lceil1/\rho_i\rceil$. Split $\mathbb R/\mathbb Z$ into
$q_i$ half-open arcs of length $1/q_i$ for each coordinate of $\theta_i$,
and send $y\in[0,N]$ to the box containing $(\{\theta_{i,l}y\})_{i,l}$.
Some box holds at least $(N+1)/\prod_iq_i^{r_i}$ points
$y_0<y_1<\cdots<y_M$. Each $x=y_j-y_0\in[1,N]$ has
$\|\theta_{i,l}x\|<1/q_i\le\rho_i$ for every $i$ and $l$, so $x$ lies in
$E_i$ for its own class $A_i$. The $M$ differences are distinct, so
$M\le|\bigcup_iE_i|$. $\square$

**Lemma 2 (rescaling sum-free arcs).** If $I$ is a nonempty sum-free arc,
some integer $n\ge1$ has $\|nt\|\ge1/8$ for every $t\in I$.

*Proof.* $0\notin I$, since $0+0=0$. Lift $I$ to an interval of $(0,1)$
with endpoints $a\le b$. The map $t\mapsto-t$ preserves sum-freeness and
$\|nt\|$, so assume $a+b\le1$.

- If $a\ge1/8$, then every $t\in I$ has $1/8\le a\le t\le b\le1-a\le7/8$,
  and $n=1$ works.
- If $a<1/8$, suppose $b>2a$. Points of $I$ near $a$ have sums near $2a$,
  inside $I$ and below $1/4$, so the sums do not wrap; this contradicts
  sum-freeness. Hence $b\le2a$, and $a>0$ because $I$ is nonempty. Put
  $n=\lfloor1/(4a)\rfloor\ge2$. Then $na\le1/4$ and $na>1/4-a>1/8$, so
  every $t\in I$ has $nt\in[na,2na]\subseteq(1/8,1/2]$ and
  $\|nt\|>1/8$. $\square$

*Proof of the claim.* Each set $\{x:\{\theta x\}\in I\}$ with $I$ a
sum-free arc is sum-free, since $\{\theta(x+y)\}$ is congruent to
$\{\theta x\}+\{\theta y\}$ modulo 1; so the classes are sum-free. By
Lemma 2 choose $n_i$ with $\|n_it\|\ge1/8$ on $I_i$; then
$A_i\cap B(n_i\theta_i;1/8)$ is empty. Lemma 1 with $r_i=1$,
$\rho_i=1/8$ and no exceptions gives $N+1\le8^k$. $\square$

The [[research/schur_number_growth/evidence/_index|research evidence]]
checks Lemma 2's choice of $n$ on every sum-free closed arc with endpoints
in $\tfrac1{120}\mathbb Z$; Lemma 2 itself is proved for every arc.
