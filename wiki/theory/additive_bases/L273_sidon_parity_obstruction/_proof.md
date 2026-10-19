---
name: theory/additive_bases/L273_sidon_parity_obstruction/_proof
title: "Proof of the parity obstruction"
desc: "The alternating-count identity, elementary balanced-sample moments, a common-block incidence bound, cancellation over progression extensions, and control of uniform degreewise renormalization."
created: 2026-10-16T00:12:37Z
updated: 2026-10-16T00:12:37Z
---

***

This is Plasma AI's author-recorded proof of
[[theory/additive_bases/L273_sidon_parity_obstruction/_index|L273]], without
independent review. All constants implicit in $O(\cdot)$ below are absolute
and uniform in $s,W,\alpha$ in the claim's domain. Write $p(T)$ for inclusion
probability under the mixture $\rho$ and set $y=s/W=k/N$.

## The alternating square

Put $\epsilon_x=(-1)^x$ and, in the Boolean-reduced polynomial ring, define

$$
Z=\sum_xz_x,\qquad B=\sum_x\epsilon_xz_x,\qquad
A=\sum_{x<u}\epsilon_x\epsilon_u z_xz_u.
$$

Then $2A=B^2-Z$. In $A^2$ the coefficient of a two-element support is $1$.
For a three-element support $T=\{a,b,c\}$ it is
$2(\epsilon_a\epsilon_b+\epsilon_a\epsilon_c+
\epsilon_b\epsilon_c)$, from the three pairs of incident edges, in both
orders. For a four-element support it is $6\epsilon_T$, where
$\epsilon_T=\prod_{x\in T}\epsilon_x$, from its three pairings in both
orders.

Let $\mathcal N_t$ be the non-Sidon $t$-subsets of the interval. Since the
base law has $Z=k$ and zeroing leaves $L_0(A)=\mathbb E_\rho A$ unchanged,

$$
\begin{split}
4L_0((A-L_0(A))^2)
={}&\operatorname{Var}_\rho(B^2)
-24\sum_{T\in\mathcal N_4}\epsilon_Tp(T)\\
&-8\sum_{\{a,b,c\}\in\mathcal N_3}
 (\epsilon_a\epsilon_b+\epsilon_a\epsilon_c+
  \epsilon_b\epsilon_c)p(T).
\end{split}                                                   \tag{1}
$$

Here $\mathcal N_3$ consists exactly of three-term progressions. Every
non-Sidon four-set either contains such a progression or has a collision
between two disjoint pairs. For four ordered points the latter equation is
$a+d=b+c$; it implies $\epsilon_T=1$.

For every $|T|=t\le4$ we have $p(T)\le y^t$. For the uniform law this follows
factor by factor from $(k-i)/(N-i)\le k/N$. For a fixed block partition, a
block containing $j$ elements of $T$ contributes $(s)_j/(W)_j\le y^j$.
The bound is preserved by rotation and mixing.

## Balanced sampling moments

If $J$ is the sum of $r$ values drawn uniformly without replacement from
$M/2$ signs $+1$ and $M/2$ signs $-1$, then, for even $M\ge4$,

$$
\begin{split}
\mathbb EJ^2&=r-\frac{r(r-1)}{M-1},\\
\mathbb EJ^4&=3r^2-2r-
 \frac{2r(r-1)(3r-4)}{M-1}
 +\frac{3(r)_4}{(M-1)(M-3)}
 \le3r^2-2r.                                           \tag{2}
\end{split}
$$

To derive this, the expected products of two and four distinct draws are
$-1/(M-1)$ and $3/((M-1)(M-3))$. They follow by taking the coefficients of
$t^2,t^4$ in $(1+t)^{M/2}(1-t)^{M/2}=(1-t^2)^{M/2}$ and dividing by the
corresponding binomial coefficients. Expanding $J^4$ according to repeated
indices gives (2). For $r\ge3$ its last positive term is at most
$3r(r-1)(r-2)/(M-1)$, which is no greater than the preceding term's absolute
value; $r=1,2$ follow directly. Thus no sampling comparison theorem is
needed.

Under the unrotated block law, $B$ is the sum of $s$ independent symmetric
block imbalances $I_b$. Write
$v=\mathbb EI_b^2=s(W-s)/(W-1)$. Then
$s(1-s/W)\le v\le s$ and (2) gives

$$
\begin{split}
\operatorname{Var}_\mu(B^2)
&=2s^2v^2+s(\mathbb EI_b^4-3v^2)\\
&\le2k^2+s(6s^3/W-2s)\le2k^2
\end{split}
$$

when $W\ge3s^2$, which holds for $s\ge6$. Since $N$ is even, rotation by $r$
multiplies $B$ by $(-1)^r$; its square has the same distribution under both
block conventions. Apply (2) with $(M,r)=(N,k)$ to the uniform law to get
$\operatorname{Var}_\nu(B^2)\le2k^2+2k^3/N$.

The two means of $B^2$ lie between $k-ks/W$ and $k$. They therefore differ
by at most $ks/W\le2$. The variance formula for a mixture yields

$$
\operatorname{Var}_\rho(B^2)\le2k^2+2k^3/N+1
=2k^2+O(s^2).                                         \tag{3}
$$

## The disjoint-pair collisions

Every four-distinct sum collision has the unique form
$\{i,i+d,i+D,i+D+d\}$ with $1\le d<D$. Its number is

$$
\Pi_N=\sum_{m=3}^{N-1}\left\lfloor\frac{m-1}{2}\right\rfloor(N-m),
\qquad
\frac{N^3}{12}-\frac{N^2}{2}\le\Pi_N\le\frac{N^3}{12}.
                                                               \tag{4}
$$

The lower bound follows by replacing the floor by $(m-2)/2$; the sum is
$(N-1)(N-2)(N-3)/12$. The upper bound follows by replacing it by $m/2$.

For any fixed block partition and four-set $T$, let $\pi(T)$ count its pairs
that lie in a common block. Comparing the falling factorials to $y^4$ and
using $\prod_i(1-u_i)\ge1-\sum_i u_i$ for $0\le u_i\le1$ gives

$$
\mu(T)\ge y^4(1-\pi(T)/s).
$$

There are $s\binom W2\le NW/2$ unordered pairs in a common block. A fixed
pair $u,v$ belongs to at most $3N$ four-distinct sum collisions: after choosing
one other element $w$, the last is one of $u+v-w,u+w-v,v+w-u$. Consequently

$$
\sum_{T\text{ a sum collision}}\pi(T)
\le\frac32N^2W.                                      \tag{5}
$$

This counting is valid for a block partition that crosses the interval cut,
so averaging proves the same bound for the rotated law. It follows that

$$
\mathbb E_\mu\#\{\text{sum collisions}\}
\ge y^4\Pi_N-\frac32\frac{y^4N^3}{s^2}.
$$

For $\nu$, every four-set has probability at least $y^4(1-6/k)$, giving
an error at most $y^4N^3/(2s^2)$ in the same estimate. Hence either component
and every mixture satisfy

$$
24\mathbb E_\rho\#\{\text{sum collisions}\}
\ge\frac{2k^4}{N}-O(s^2),                            \tag{6}
$$

because $y^4N^2\le4$ and $y^4N^3/s^2\le2s^2$.

## Progressions and their extensions

There are at most $N^2/4$ three-term progressions. Their coefficients in
(1) have absolute value at most $24$, so their total contribution is
$O(N^2y^3)=O(s^2)$.

Let $\mathcal G$ consist of the four-sets that contain a progression and
have no disjoint-pair sum collision. For $T\in\mathcal G$ let $a(T)$ be
its number of progression triples. Then

$$
\sum_{T\in\mathcal G}\epsilon_Tp(T)
=\sum_{R\text{ a progression}}\epsilon_R
  \sum_{\substack{x\notin R\\R\cup\{x\}\in\mathcal G}}
     \frac{\epsilon_xp(R\cup\{x\})}{a(R\cup\{x\})}.
                                                               \tag{7}
$$

First replace $1/a$ by $1$. Fix $R$ and a fixed, possibly rotated, block
partition. Define $f_R(x)$ for every $x$ in the interval by applying the
block inclusion formula to the multiplicities in $R$ plus one extra point
in the block of $x$, even when $x\in R$. The value is constant on each
cyclic block and at most $y^4$. Each block has even length, so
$\sum_x\epsilon_xf_R(x)=0$. For $\nu$ use the constant extension
$f_R(x)=(k)_4/(N)_4$, whose alternating sum is also zero.

In the inner sum of (7), this full sum excludes the three points of $R$ and
at most two further points making a disjoint-pair collision. For
$R=\{a,a+t,a+2t\}$ those further points are $a-t,a+3t$ when present.
Its absolute value is therefore at most $5y^4$.

The difference between $1/a$ and $1$ is supported on extensions with at
least two progression triples. For fixed $R$ there are at most six such
new points: relative to $a$ they belong to
$\{-2t,-t,t/2,3t/2,3t,4t\}$. Thus the correction is at most $6y^4$.
Averaging over rotations and mixing preserves these bounds. Summing over
$R$ gives

$$
\left|\sum_{T\in\mathcal G}\epsilon_Tp(T)\right|
\le\frac{11}{4}N^2y^4=O(1).                          \tag{8}
$$

Combining (1), (3), (6) and (8) already proves the claimed bound for $L_0$.

## Uniform degreewise renormalization

Let $E_t=\sum_{T\in\mathcal N_t}p(T)$ be the erased mass. The same counts
give

$$
E_3\le N^2y^3/4=O(s^2),\qquad
E_4\le (N^3/12+N^3/4)y^4=O(s^4).
$$

The original total is $\binom kt$, of orders $s^6,s^8$ for $t=3,4$.
The surviving totals are therefore positive for all sufficiently large $s$,
uniformly in $W,\alpha$, and $a_t-1=O(s^{-4})$ for both degrees.
At degree three the coefficients of $A^2$ have absolute value at most $6$,
so renormalization changes its expectation by $O(s^{-4}s^6)=O(s^2)$.

At degree four its signed coefficient sum before zeroing is $6\mathbb E e_4$,
where $e_4$ is the fourth elementary symmetric function of the $k$ sampled
signs. Newton's identities give

$$
24e_4=B^4-6kB^2+8B^2+3k^2-6k.
$$

Equation (2) and the block moment calculation give
$\mathbb E B^4=O(k^2)$ and $\mathbb E B^2\le k$, hence
$|\mathbb E e_4|=O(k^2)$. Zeroing changes the signed sum by at most
$E_4=O(k^2)$. Its surviving sum is still $O(k^2)$, and multiplying it by
$a_4-1$ changes the expectation by only $O(1)$. Degrees at most two, including
$L(A)$, are unchanged. Thus for $L=L_0$ or $L_1$,

$$
4L((A-L(A))^2)
\le 2k^2-\frac{2k^4}{N}+O(s^2)
=-\frac{2k^2}{N}(k^2-N)+O(s^2).
$$

Choose an absolute $C$ dominating this uniform error divided by four and
an absolute $s_0$ covering the stated estimates. This proves the theorem.
For even $W_s=s^3-\beta s^2+O(s)$, we have
$k^2-N=\beta s^3+O(s^2)$ and $k^2/N=1+O(1/s)$, proving the limsup
consequence. Since $k^2/N\ge1$, the bound is also negative whenever
$k^2-N>2Cs^2$; in particular $k-\sqrt N>2C$ suffices in this family.
