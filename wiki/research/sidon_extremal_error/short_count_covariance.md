---
name: research/sidon_extremal_error/short_count_covariance
title: "Exact short-difference covariance of the block law"
desc: "A direct edge-intersection calculation gives the short-count covariance as a low-rank polynomial plus two absolute-value kernels, exposing a negative cumulative-sum form relevant to local moment repairs."
created: 2026-10-16T00:12:37Z
updated: 2026-10-16T00:12:37Z
---

***

This is Plasma AI's author-recorded calculation, without independent review.
It concerns the genuine, unrotated block law and does not construct Sidon
pseudo-moments. Its role in the
[[research/sidon_extremal_error/local_repair_gap|local-repair question]] is
to identify the covariance terms that any proposed high-frequency estimate
must control.

Take $s\ge2$ blocks of length $W\ge\max(s,4)$, independently choosing a
uniform $s$-subset in each. Put $N=sW$ and
$f_j=(s)_j/(W)_j$ for $1\le j\le4$. For $1\le d<W$, write
$P_d=\sum_b U_b(d)+\sum_b V_b(d)$, where $U_b(d)$ counts pairs at distance
$d$ inside block $b$, and $V_b(d)$ counts those crossing from block $b$ to
block $b+1$. There are $s$ terms of the first kind and $s-1$ of the second.
Their means are $u_d=(W-d)f_2$ and $v_d=df_1^2$.

For distinct $d,e<W$ define

$$
\begin{split}
n_{de}&=2(W-\max(d,e))+2(W-d-e)_+,\\
r_{de}&=(e-d)_++\min(W-d,e),\qquad
t_{de}=(d+e-W)_+,\\
G_{de}&=((W-d)(W-e)-n_{de})f_4+n_{de}f_3-u_du_e,\\
H_{de}&=2\min(d,e)f_1f_2+(de-2\min(d,e))f_2^2-v_dv_e,\\
J_{de}&=f_1\{r_{de}f_2+((W-d)e-r_{de})f_3\}-u_dv_e,\\
Q_{de}&=f_1^2\{t_{de}f_1+(de-t_{de})f_2\}-v_dv_e.
\end{split}                                                   \tag{1}
$$

Then the covariance is exactly

$$
C(d,e)=sG_{de}+(s-1)H_{de}
       +2(s-1)(J_{de}+J_{ed})+(s-2)(Q_{de}+Q_{ed}).    \tag{2}
$$

For the diagonal use the same $J,Q$ and replace $G,H$ by

$$
\begin{split}
G_{dd}={}&(W-d)f_2+2(W-2d)_+f_3\\
 &+((W-d)^2-(W-d)-2(W-2d)_+)f_4-u_d^2,\\
H_{dd}={}&df_1^2+(d^2-d)f_2^2-v_d^2.                 \tag{3}
\end{split}
$$

To verify (1), two internal edges of distinct lengths have a common vertex
in $n_{de}$ placements: equal left or right endpoints contribute
$2(W-\max(d,e))$, and a right endpoint equaling the other's left contributes
$2(W-d-e)_+$. The other placements have four distinct points. Two edges
crossing the same boundary have a common endpoint in $2\min(d,e)$
placements; their other placements use two points in each block. An internal
$d$-edge and a crossing $e$-edge with an endpoint in its block share one of
its vertices in $r_{de}$ placements. Finally two edges crossing adjacent
boundaries have a common endpoint in $t_{de}$ placements in their shared
block. Subtract the product of means in each case. On the diagonal, identical
edges give the extra terms in (3).

Independence eliminates all disjoint-block covariances. There are $s$ internal
blocks, $s-1$ boundaries, two sides of each boundary for an internal-crossing
pair, and $s-2$ adjacent boundary pairs. Including both orders gives (2).
Reflection of a block makes the internal-crossing covariance identical on its
two sides. This proves the formulas.

## The two absolute-value terms

For $d\ne e$, expanding the maxima, minima and positive parts in (1) gives

$$
C(d,e)=a_0+a_1(d+e)+a_2de
       +K_D|d-e|+K_A|d+e-W|,                         \tag{4}
$$

for constants $a_0,a_1,a_2$ depending only on $s,W$, with

$$
\begin{split}
K_D={}&-s(f_3-f_4)-(s-1)(f_1f_2-f_2^2)
                         +2(s-1)f_1(f_2-f_3),\\
K_A={}& s(f_3-f_4)-2(s-1)f_1(f_2-f_3)
                         +(s-2)f_1^2(f_1-f_2).
\end{split}                                                   \tag{5}
$$

For example, the coefficients of $|d-e|,|d+e-W|$ in $n_{de}$ are $-1,1$;
those in $r_{de}+r_{ed}$ are $1,-1$. These give the first and third terms
of (5); the other two contributions come directly from $\min(d,e)$ and
$t_{de}$. Every remaining expression in (1) is a linear combination of
$1,d+e,de$. Thus the polynomial part of the matrix has rank at most two,
on the span of the constant and coordinate vectors. Equation (4) concerns
off-diagonal entries; a diagonal correction from (3) remains.

If $W=s^3+O(s^2)$, then

$$
K_D=s^{-6}+O(s^{-7}),\qquad K_A=-s^{-6}+O(s^{-7}).      \tag{6}
$$

For a direct expansion, write $y=s/W=s^{-2}(1+O(s^{-1}))$. Then
$f_2=y^2(1-s^{-1}+O(s^{-3}))$,
$f_3=y^3(1-3s^{-1}+2s^{-2}+O(s^{-3}))$ and
$f_4=y^4(1+O(s^{-1}))$. In $K_D$ the terms of order $sy^3$ cancel, leaving
$y^3(1+O(s^{-1}))+O(sy^4)$; in $K_A$ they leave
$-y^3(1+O(s^{-1}))+O(sy^4)$. This proves (6).

The negative effect of the first kernel has an exact finite-interval form.
For real $b_1,\ldots,b_{W-1}$ with $\sum_d b_d=0$,

$$
\sum_{d,e}b_db_e|d-e|
=-2\sum_{r=1}^{W-2}\left(\sum_{d\le r}b_d\right)^2.   \tag{7}
$$

Express $|d-e|$ as the number of cuts between $d$ and $e$; each cut contributes
$2(\sum_{d\le r}b_d)(\sum_{e>r}b_e)$, proving (7). The second kernel in
(4) is the first composed with reflection $e\mapsto W-e$. Since reflection
commutes with the first kernel, its quadratic form on the zero-sum subspace
has absolute value at most the negative of (7), by Cauchy--Schwarz for the
positive semidefinite form $-|d-e|$ on that subspace.

Equations (4)--(7) make the interior spectral heuristic concrete. They do not
give a high-frequency lower bound for the complete covariance after a Sidon
repair. The diagonal, the polynomial part, the long differences, boundary
conditions and the unconstructed correction must all be included in such a
bound.

The [research evidence entry point](evidence/main.py) checks every mean and
covariance against a separate complete enumeration of the unrotated sample
space at $(s,W)=(2,4),(3,4),(3,6),(4,6)$, in exact rational arithmetic. It
also checks the two-kernel decomposition at every off-diagonal entry of
these matrices. This is finite supplementary evidence; the general identities
rest on the counting argument above.
