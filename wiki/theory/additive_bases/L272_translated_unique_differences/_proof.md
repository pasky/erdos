---
name: theory/additive_bases/L272_translated_unique_differences/_proof
title: Proof of the translated unique-difference bound
desc: |
  A translated difference set forces a large sliding-count correlation.
  Averaging disjoint windows bounds the count's norm and gives the
  k^(5/3) estimate without a diameter restriction on the Sidon set.
tags: []
sources: []
created: 2026-10-15T23:58:19Z
updated: 2026-10-15T23:58:19Z
---

***

Let $A,W,s,k$ satisfy the claim, and put $n=|W|\ge1$. For integers $t,j$
define

$$
r(t)=|\{(a,a')\in A^2:a'-a=t\}|,\qquad
r_W(t)=|\{(w,w')\in W^2:w'-w=t\}|,\qquad
F(j)=|A\cap(j+W)|.
$$

All functions have finite support. Write $\|\cdot\|_2$ and
$\langle\cdot,\cdot\rangle$ for the norm and inner product in
$\ell^2(\mathbb Z)$. An ordered pair $(a,a')$ belongs to
$(j+W)\times(j+h+W)$ for exactly $r_W(a'-a-h)$ values of $j$. Therefore

$$
\langle F,F(\cdot+h)\rangle
 =\sum_t r(h+t)r_W(t).                              \tag{1}
$$

At $h=0$, the term $t=0$ is $kn$ and all other representation counts
are at most one. Since $\sum_t r_W(t)=n^2$ and $r_W(0)=n$,

$$
\|F\|_2^2\le kn+n^2-n.                             \tag{2}
$$

For every $t\in W-W$, the hypothesis $|s|>\operatorname{diam}W$ gives
$s+t\ne0$. Its inclusion in $A-A$ and uniqueness give $r(s+t)=1$.
Equation (1) at $h=s$ consequently gives

$$
\langle F,F(\cdot+s)\rangle=n^2.                    \tag{3}
$$

Cauchy--Schwarz and translation invariance of the norm imply
$\|F\|_2^2\ge n^2$. Combining (2) and (3) gives

$$
\|F-F(\cdot+s)\|_2^2
 =2\|F\|_2^2-2n^2\le2n(k-1).                       \tag{4}
$$

Fix an integer $K\ge1$ and set
$g=K^{-1}\sum_{i=0}^{K-1}F(\cdot+is)$. Telescoping (4), followed by
the triangle inequality, gives

$$
\|F-g\|_2
 \le\frac1K\sum_{i=0}^{K-1}i\sqrt{2n(k-1)}
 =\frac{K-1}{2}\sqrt{2n(k-1)}.                       \tag{5}
$$

For distinct $i,i'\in\{0,\ldots,K-1\}$ we have
$|(i'-i)s|>\operatorname{diam}W$, so $(i'-i)s\notin W-W$.
Thus the windows $j+is+W$ are pairwise disjoint for each fixed $j$.
It follows that $\sum_i F(j+is)\le k$, hence $0\le g(j)\le k/K$.
Each element of $A$ is counted in exactly $n$ windows $j+W$, so
$\sum_j g(j)=\sum_j F(j)=kn$. Therefore

$$
\|g\|_2^2\le\frac{k}{K}\sum_jg(j)=\frac{k^2n}{K}.  \tag{6}
$$

Using (3), (5), (6), and the triangle inequality,

$$
n\le\|F\|_2\le\|g\|_2+\|F-g\|_2
 \le k\sqrt{\frac nK}+\frac{K-1}{2}\sqrt{2n(k-1)}.
$$

Division by $\sqrt n$ proves the inequality for every $K\ge1$, including
$K=1$. Take $K=\lceil k^{1/3}\rceil$. Since $K\ge k^{1/3}$,
$K-1\le k^{1/3}$ and $k-1\le k$, its right-hand side is at most
$(1+1/\sqrt2)k^{5/6}$. Squaring proves

$$
|W|\le(3/2+\sqrt2)k^{5/3}.\qquad\square
$$

**Restricted uniqueness.** The proof only uses $r(t)\le1$ for
$t\in(W-W)\setminus\{0\}$ and $r(s+t)=1$ for $t\in W-W$.
If a set of $k$ integers represents every positive difference up to
$L\ge1$ exactly once, put $u=\lfloor(L+1)/2\rfloor$,
$W=\{0,\ldots,u-1\}$ and $s=u$. The restricted conditions hold because
$s+(W-W)=\{1,\ldots,2u-1\}$ and $2u-1\le L\le2u$.
Hence $L\le(3+2\sqrt2)k^{5/3}$. This recovers the leading term of
L239 under its weaker hypothesis, without using that claim as an input
or imposing uniqueness on differences larger than $L$.
