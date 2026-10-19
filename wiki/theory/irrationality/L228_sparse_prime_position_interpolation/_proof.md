---
name: theory/irrationality/L228_sparse_prime_position_interpolation/_proof
title: Paired corrections and a greedy expansion
desc: |
  Proof of L228. Sparse positive corrections to halved gaps are matched
  with later gaps that absorb equal negative corrections. A prime-pair
  sieve bound makes the affected position intervals have density zero;
  a greedy expansion controls the value of the binary series.
created: 2026-10-15T20:52:57Z
updated: 2026-10-15T20:52:57Z
---

***

This proves
[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228]]
at author-recorded standing. All logarithms without a subscript are natural.
Write $h_n=(p_{n+1}-p_n)/2$ for $n\ge2$ and

$$
H_m=\sum_{r\ge0}\frac{h_{m+r}}{2^{r+1}}\qquad(m\ge2).
$$

We first derive the only distributional estimate used in the construction.

## Very small gaps have small upper density

There are absolute constants $A$ and $M_0$ such that, for every
$M\ge M_0$ and $0<\epsilon\le1$,

$$
\#\{2\le n\le M:h_n\le\epsilon\log n\}\le A\epsilon M.
\tag{1}
$$

The source premise is the prime-pair bound at the beginning of the proof of
Theorem 4.2, p. 10 of Nathan McNew, *The convex hull of the prime number
graph*, author's preprint of the 2018 paper. Its
[[../library/primes/mcnew_2018_convex_hull_prime_number_graph/theorem_4_2|library page identifies the edition and proof location]].
For $D(t,x)=\#\{p\le x:p,p+t\text{ are prime}\}$, the displayed Brun-sieve
bound is, with an absolute constant,

$$
D(t,x)\ll \frac{x}{\log^2x}
  \prod_{\substack{\ell\mid t\\\ell\le x}}
       \left(1-\frac1\ell\right)^{-1}.
\tag{2}
$$

All products indexed by $\ell$ in this proof run over primes.

We use it only for positive even $t\le2\log x$, so that the product is
$t/\phi(t)$. The statement, including the absolute constant, was inspected
on the printed page. The sieve argument behind (2) is not reproved here.

For $B\ge1$, the identity
$t/\phi(t)=\sum_{e\mid t}\mu(e)^2/\phi(e)$ gives

$$
\sum_{t\le B}\frac{t}{\phi(t)}
\le B\sum_{e\ge1}\frac{\mu(e)^2}{e\phi(e)}
=B\prod_{\ell\text{ prime}}
 \left(1+\frac1{\ell(\ell-1)}\right)\ll B.
\tag{3}
$$

If $\epsilon\log M<1$, the set in (1) is empty. Otherwise its members
have $p_{n+1}-p_n\le2\epsilon\log M$. Put $x=p_M\sim M\log M$ and
sum (2) over the positive even differences up to
$B=2\epsilon\log M\le2\log x$. By (3), the count is at most

$$
O\left(\frac{x}{\log^2x}\,\epsilon\log M\right)=O(\epsilon M),
$$

with constants independent of $\epsilon$ and $M$ once $M$ is large.
This proves (1) uniformly in $\epsilon$. In particular, if
$b_n=o(\log n)$ is nonnegative,
the indices with $h_n\le b_n$ have density zero: bound $b_n$ eventually by
$\epsilon\log n$ and then let $\epsilon\downarrow0$ in (1).

## Choosing the positions and their capacity

Fix the moduli $(q_n)$ and a prefix length $N$. Put

$$
\Omega_n=\inf_{m\ge n}\log_2\frac{\log m}{q_m}.
$$

Since $q_n=o(\log n)$, the numbers $\Omega_n$ are finite, nondecreasing
and tend to infinity. Choose $n_0\ge\max(N,3)$ such that $\Omega_{n_0}\ge8$,
and set $L_n=\lfloor\Omega_n/4\rfloor$ for $n\ge n_0$. Thus $L_n\ge2$ is
nondecreasing and tends to infinity. Define

$$
i_0=n_0,\qquad i_t=i_{t-1}+L_{i_{t-1}}\quad(t\ge1),\qquad
U_t=2^{L_{i_t}+3}.
\tag{4}
$$

The set of starts $\{i_t:t\ge1\}$ has density zero, since its successive
spacings tend to infinity. We choose distinct, increasing endpoints. Put
$j_0=n_0$ and let $j_t$ be the least integer satisfying

$$
j_t\ge\max(i_t+1,j_{t-1}+1),\qquad h_{j_t}\ge q_{j_t}U_t+1.
\tag{5}
$$

Each choice exists. For fixed $t$, $q_jU_t+1=o(\log j)$, and the last
consequence of (1) says that almost all sufficiently large $j$ satisfy
the second condition in (5). No quantitative bound for the first such
endpoint is needed.

For $j\ge i_t$, the definition of $\Omega$ gives

$$
q_jU_t\le 2^{3-3\Omega_{i_t}/4}\log j
=:\epsilon_t\log j,
\qquad \epsilon_t\downarrow0.
\tag{6}
$$

Define the set of position indices

$$
D=\bigcup_{t\ge1}\{i_t+1,i_t+2,\ldots,j_t\}.
\tag{7}
$$

It has density zero. To prove this, fix an integer $T\ge1$ and discard
the finite union of intervals in (7) with $t<T$. If a remaining $n\in D$
is not an endpoint, choose the smallest $t$ with $i_t<n\le j_t$.
Every earlier endpoint is below $n$: otherwise its start is smaller than
$i_t<n$, so its interval would contain $n$. Therefore
$n\ge\max(i_t+1,j_{t-1}+1)$ and $n<j_t$. By the minimality of $j_t$,
$h_n<q_nU_t+1$, hence, since these are integers,

$$
h_n\le q_nU_t\le\epsilon_t\log n\le\epsilon_T\log n.
$$

The endpoint set has density zero because $j_t>i_t$, so its count up to
$M$ is at most the count of starts up to $M$. By (1), the upper density
of $D$ is at most $A\epsilon_T$. Letting $T\to\infty$ proves the assertion.
It also proves

$$
\frac{j_t}{i_t}\longrightarrow1:
\quad\frac{j_t-i_t}{j_t}\le
\frac{|D\cap[1,j_t]|}{j_t}\longrightarrow0.
\tag{8}
$$

The set $D$, the starts, endpoints and caps depend on the given primes and
moduli, not on the value of the series to be attained.

If, additionally, $q_n\le C(\log n)^\alpha$ eventually, where
$0\le\alpha<1$, then

$$
\Omega_n\ge(1-\alpha)\log_2\log n-\log_2 C
$$

for all large $n$. The start spacings are consequently bounded below
by a positive constant times $\log\log i_t$. There are
$O(M/\log\log M)$ starts up to $M$, by splitting at $\sqrt M$,
and at most that many endpoints. By (8), intervals with
$i_t<\sqrt M$ end below $2\sqrt M$ for all sufficiently large $M$.
An index of $D$ above $2\sqrt M$ which is not an endpoint therefore
has, by the same minimal-endpoint argument as above,

$$
h_n\le\eta_M\log n,\qquad
\eta_M=8\,2^{-3\Omega_{\lfloor\sqrt M\rfloor}/4}
=O\left((\log M)^{-3(1-\alpha)/4}\right).
$$

Apply the uniform bound (1), with this $\eta_M$, to obtain

$$
|D\cap[1,M]|
\le2\sqrt M+O(M/\log\log M)+A\eta_M M
=O(M/\log\log M).
\tag{8a}
$$

This proves the additional quantitative clause about $D$.

## Filling an interval of values

Define positive real weights

$$
w_t=q_{j_t}\left(2^{-(i_t-n_0+1)}-2^{-(j_t-n_0+1)}\right).
\tag{9}
$$

By (8), $q_{j_t}=o(\log j_t)=o(\log i_t)$, so $w_t\to0$. Since $j_t>i_t$,
the factor $1-2^{-(j_t-i_t)}$ lies in $[1/2,1)$. Since the moduli form a
divisibility chain and the endpoints increase, $q_{j_{t-1}}\le q_{j_t}$.
Consequently, for $t\ge2$,

$$
\frac{w_{t-1}}{w_t}\le2^{i_t-i_{t-1}+1}
=2^{L_{i_{t-1}}+1}\le2^{L_{i_t}+1}.
\tag{10}
$$

Also $w_1\ge2^{-L_{n_0}-2}$. For any $b\in[0,1]$ define

$$
r_0=b,\qquad u_t=\left\lfloor\frac{r_{t-1}}{w_t}\right\rfloor,\qquad
r_t=r_{t-1}-u_tw_t\quad(t\ge1).
\tag{11}
$$

Then $0\le r_t<w_t$, so $r_t\to0$ and $\sum_{t\ge1}u_tw_t=b$.
Moreover $0\le u_1\le2^{L_{n_0}+2}<U_1$, and for $t\ge2$, (10) gives
$0\le u_t<w_{t-1}/w_t\le2^{L_{i_t}+1}<U_t$. Thus every digit fits its
prescribed capacity.

Set $v_t=q_{j_t}u_t$ and, for all $n\ge1$, put

$$
a_n=p_n+2\sum_{i_t<n\le j_t}v_t.
\tag{12}
$$

This finite sum is nonnegative. It vanishes for $n\le n_0$ and for
$n\notin D$. For $n\ge2$, the new halved gap is

$$
h'_n:=\frac{a_{n+1}-a_n}{2}
=h_n+\sum_{i_t=n}v_t-\sum_{j_t=n}v_t.
\tag{13}
$$

There is at most one term in each of the two sums. If an endpoint equals
$n$, then $v_t<q_nU_t<h_n$ by (5); therefore $h'_n\ge1$, including when
a start and an endpoint coincide. Also $a_1=2$, $a_2=3$. This proves
strict increase and positivity.

For every active interval in (12), $n\le j_t$, so $q_n\mid q_{j_t}$.
It follows that $a_n\equiv p_n\pmod{2q_n}$ for $n\ge2$. Equation (13)
also shows $h'_n\equiv h_n\pmod{q_n}$, including at starts, because
$i_t<j_t$ and $q_{i_t}\mid q_{j_t}$.

The density-zero conclusion for $D$ implies $a_n/p_n\to1$. Indeed,
$a_n\ge p_n$, and for every fixed $\eta>0$ and all large $n$ there is an
$m\in[n,(1+\eta)n]$ outside $D$. Monotonicity and the prime number theorem
give $a_n\le a_m=p_m\le(1+\eta+o(1))p_n$; let $\eta\downarrow0$.

The changes to gaps are small even on their support. By (6),
$v_t\le\epsilon_t\log j_t$, and by (8), $\log j_t/\log i_t\to1$.
Thus a positive term in (13) is $o(\log i_t)$ and a negative term is
$o(\log j_t)$. There are at most two incident terms at any index, so
$h'_n-h_n=o(\log n)$. These changes also have density-zero support, since
only starts and endpoints can occur.

Finally, all the terms $v_t$ in (12) are nonnegative. Tonelli's theorem
and a finite geometric sum give

$$
\begin{aligned}
\sum_{n\ge1}\frac{a_n-p_n}{2^n}
&=2\sum_{t\ge1}v_t\sum_{n=i_t+1}^{j_t}2^{-n}\\
&=2\sum_{t\ge1}v_t(2^{-i_t}-2^{-j_t})\\
&=2^{2-n_0}\sum_{t\ge1}u_tw_t
=2^{2-n_0}b.
\end{aligned}
\tag{14}
$$

Take $\delta=2^{2-n_0}$ and $b=(T-S)/\delta$ for any
$T\in[S,S+\delta]$. Equations (12)--(14) prove every clause of L228.
Dyadic rationals are dense, so one can choose such a $T>S$ that is dyadic
rational. The construction makes no assertion that the altered terms are
prime. $\square$
