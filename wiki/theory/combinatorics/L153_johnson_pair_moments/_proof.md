---
name: theory/combinatorics/L153_johnson_pair_moments/_proof
title: Projection and color-moment construction
desc: Binomial inversion gives the projection onto the highest-degree Johnson space; its color decomposition supplies the feasible two-point moments and their forced intersection counts.
created: 2026-10-15T11:42:54Z
updated: 2026-10-15T11:42:54Z
---

# Projection and color-moment construction

***

This proves [[theory/combinatorics/L153_johnson_pair_moments/_index|L153]].
Write $N=\binom{2k}k$, $p=k+1$, and let $J_V$ be the $N$ by $N$
all-ones matrix. Let $D$ be the inclusion matrix from $k$-sets to
$(k-1)$-sets, so $(Dh)(T)=\sum_{C\supset T}h(C)$. Define

$$
E(B,C)=\frac{(-1)^{|B\cap C|}}{p\binom{k}{|B\cap C|}}.
$$

We first prove that $E$ is the orthogonal projection onto $\ker D$.
Fix $B$ and a $(k-1)$-set $T$, and set $s=|B\cap T|$. There are $k-s$
extensions of $T$ whose intersection with $B$ has size $s+1$ and $s+1$
whose intersection has size $s$. Hence the corresponding column sum is
zero, because

$$
\frac{(k-s)(-1)^{s+1}}{\binom{k}{s+1}}
+\frac{(s+1)(-1)^s}{\binom{k}s}=0.
$$

Thus the range of $E$ lies in $\ker D$. For $h\in\ker D$, repeated
downward summation gives $\sum_{C\supseteq T}h(C)=0$ for every $|T|<k$:
each downward step counts each extension a fixed positive number of
times. Fix $B$ and put $h_s=\sum_{|B\cap C|=s}h(C)$. Summing those
identities over the $j$-subsets of $B$ gives

$$
\sum_{s=0}^k\binom sjh_s=0\quad(j<k),\qquad h_k=h(B).
$$

Binomial inversion therefore gives
$h_s=(-1)^{k-s}\binom ks h(B)$. Since $k$ is even,

$$
(Eh)(B)=\frac1p\sum_{s=0}^k\frac{(-1)^s h_s}{\binom ks}
=\frac{k+1}{p}h(B)=h(B).
$$

Symmetry of $E$, its range containment, and this identity prove that it
is the asserted orthogonal projection. In particular it is positive
semidefinite. Its trace also gives $\dim\ker D=N/p$.

The matrix in the statement satisfies $K=J_V/p+(p-1)E$, so it is
positive semidefinite. Its diagonal is one. At intersection sizes
$s=0,k$ its entry $K_s$ is one; for $0<s<k$, use $\binom ks\ge k$ to
get $0\le K_s\le1$. Also $K_{k-1}=0$.

For the matrix $M$ on $V\times\{1,\ldots,p\}$, the same-color block is
$K/p$ and every different-color block is $(J_V-K)/(p(p-1))$.
On the constant color direction their sum is $J_V/p$; on every color
direction perpendicular to constants their difference is

$$
\frac Kp-\frac{J_V-K}{p(p-1)}
=\frac{pK-J_V}{p(p-1)}=E.
$$

Both are positive semidefinite. Moreover $yy^{\mathsf T}$ has
operator $J_V/p$ on the constant color direction and zero on its
orthogonal complement. Consequently $M-yy^{\mathsf T}$ is positive
semidefinite. The Schur complement of the top-left entry one now shows
that the block matrix with blocks $1,y^{\mathsf T},y,M$ is positive
semidefinite. The entrywise inequalities and marginal and edge
conditions follow directly from $0\le K_s\le1$, $K_k=1$ and
$K_{k-1}=0$.

There are $\binom ks^2$ sets $C$ with $|B\cap C|=s$. The two sums in
the statement are therefore

$$
\binom ks^2K_s
=\frac{\binom ks(\binom ks+k(-1)^s)}p,
\qquad
\binom ks^2\frac{1-K_s}{p-1}
=\frac{\binom ks(\binom ks-(-1)^s)}p.
$$

They are nonnegative by the already proved entrywise inequalities.
When $p=k+1$ is prime, the congruence
$\binom{p-1}s\equiv(-1)^s\pmod p$ makes both numerators divisible
by $p$. This includes $s=0,k$ and proves all assertions. $\square$
