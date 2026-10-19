---
name: theory/additive_bases/L208_two_parabola_maximal_sidon/_proof
desc: |
  Pair sums of the two parabolas are classified by which outer coordinates
  vanish, the non-square separates the two kinds at height zero, and three
  explicit formulas block every point outside the set.
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# theory/additive_bases/L208_two_parabola_maximal_sidon/_proof

[[theory/additive_bases/L208_two_parabola_maximal_sidon/_index|..]]

***

Throughout, $q$ is an odd prime power, $\mu\in\mathbb F_q$ is a non-square
and, for $t,u\in\mathbb F_q$,

$$
P(t)=(t,t^2,0),\qquad C(u)=(0,\mu u^2,u),\qquad
A=\{P(t)\}\cup\{C(u)\}.
$$

**Size.** $P(t)=C(u)$ forces $t=0$ and $u=0$, so the two parabolas share
only the origin $P(0)=C(0)=0$ and $|A|=2q-1$.

**A pair lemma.** For $s,r\in\mathbb F_q$ the conditions $t+t'=s$ and
$t^2+t'^2=r$ determine the unordered pair $\{t,t'\}$: they give
$2tt'=s^2-r$, so $t$ and $t'$ are the two roots of
$X^2-sX+(s^2-r)/2$, and $2$ is invertible.

**Strong Sidon.** Every pair of elements of $A$, doubles included, has a
sum of one of the forms

$$
P(t)+P(t')=(t+t',\,t^2+t'^2,\,0),\quad
C(u)+C(u')=(0,\,\mu(u^2+u'^2),\,u+u'),\quad
P(t)+C(u)=(t,\,t^2+\mu u^2,\,u),
$$

where a pair containing the origin may be read in more than one form. Let
$\sigma=(\sigma_1,\sigma_2,\sigma_3)$ be such a sum. We show that $\sigma$
determines the pair.

1. If $\sigma_1\ne0$ and $\sigma_3\ne0$, the pair is not inside $P$
   (third coordinate $0$) and not inside $C$ (first coordinate $0$). So it
   is $\{P(t),C(u)\}$ with $t=\sigma_1$ and $u=\sigma_3$.
2. If $\sigma_3=0$, a pair meeting $C\setminus\{0\}$ in some $C(u)$ must
   be $\{C(u),C(-u)\}$, since $P(t)+C(u)$ has third coordinate $u\ne0$.
   Otherwise the pair lies in $P$ and the pair lemma recovers it from
   $(\sigma_1,\sigma_2)$. A pair $\{C(u),C(-u)\}$ is recovered from
   $\sigma_2=2\mu u^2$. The two cases cannot share a sum: that would need
   $t+t'=0$ and $2t^2=2\mu u^2$ with $u\ne0$, so $\mu=(t/u)^2$ would be a
   square.
3. If $\sigma_1=0$ and $\sigma_3\ne0$, a pair meeting $P\setminus\{0\}$ in
   some $P(t)$ would have first coordinate $t\ne0$ (with a point of $C$) or
   third coordinate $0$ (with a point of $P$). So the pair lies in $C$, and
   the pair lemma applied to $u+u'=\sigma_3$, $u^2+u'^2=\sigma_2/\mu$
   recovers it.

The cases are exhaustive and disjoint, so distinct pairs have distinct
sums.

**Maximality.** Let $x=(x_1,x_2,x_3)\notin A$. We give $a,b,c\in A$ with
$c\notin\{a,b\}$ and $x=a+b-c$.

1. $x_1\ne0$. Put $\sigma=(x_2-\mu x_3^2)/x_1$, $t=(\sigma+x_1)/2$ and
   $w=(\sigma-x_1)/2$, and take $a=C(x_3)$, $b=P(t)$, $c=P(w)$. Then
   $a+b-c=(t-w,\ \mu x_3^2+(t-w)(t+w),\ x_3)=x$. Here $c\ne b$ because
   $t-w=x_1\ne0$, and $c=a$ would force $w=x_3=0$ and $x=P(t)\in A$.
2. $x_1=0$ and $x_3\ne0$. Put $\sigma=x_2/(\mu x_3)$, $u=(\sigma+x_3)/2$
   and $v=(\sigma-x_3)/2$, and take $a=P(0)$, $b=C(u)$, $c=C(v)$. Then
   $a+b-c=(0,\ \mu(u-v)(u+v),\ u-v)=x$. Here $c\ne b$ because $u\ne v$,
   and $c=a=0$ would force $v=0$ and $x=C(u)\in A$.
3. $x_1=x_3=0$, so $x_2\ne0$. Put $t'=-x_2/2$ and take $a=P(1)$,
   $b=P(t')$, $c=P(1+t')$. Then $a+b-c=(0,\ -2t',\ 0)=x$. Here $c=a$ would
   need $t'=0$, and $c=b$ would need $1=0$.

In each case $a+b=x+c$, and the pairs $\{a,b\}$ and $\{x,c\}$ differ
because $x\notin A$. Hence $A\cup\{x\}$ is not strong Sidon, and $A$ is
maximal. $\blacksquare$

**Remarks.** The midpoint condition $2x\in A+A$ is never needed. The proof
uses only that $2$ is invertible and that $\mu$ is not a square, so the
same set works over every finite field of odd characteristic, and through
$\mathbb F_q^3\cong(\mathbb Z/p)^{3k}$ it gives maximal Sidon sets of size
$2p^k-1$ in elementary abelian $p$-groups of rank $3k$.
