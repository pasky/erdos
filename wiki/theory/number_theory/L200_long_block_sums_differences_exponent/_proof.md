---
name: theory/number_theory/L200_long_block_sums_differences_exponent/_proof
title: Projections of progressions and tensor powers of cell sets
desc: Every long block yields a cell set whose projections are counted multiples, and tensor powers of a near-extremal cell set with primes chosen by averaging give the matching upper bound.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

***

For a cell set $S$ write $X(S)$, $Y(S)$ and $W(S)$ for the sets of
values of $x$, $y$ and $2y-x$, so $N(S)=\max(|X(S)|,|Y(S)|,|W(S)|)$.

**The range of $\beta$.** A cell is determined by its pair $(x,y)$, so
$|S|\le|X(S)||Y(S)|\le N(S)^2$. If $|S|\ge2$ then $N(S)\ge2$, since
otherwise $x$ and $y$ would both be constant on $S$. Hence every ratio is
at most $2$ and $\beta\le2$. The cells $(0,1)$, $(2,1)$, $(2,2)$ have
differences $1,-1,0$ and $X=\{0,2\}$, $Y=\{1,2\}$, $W=\{2,0\}$; their
ratio is $\log3/\log2>1$, so $\beta>1$.

**Lower bound.** Let $\alpha\ge3$, $u\ge2$, let $p_1<\cdots<p_u$ be
primes with $P=p_u$, and let $J$ be a block of $K=\lfloor\alpha P\rfloor$
consecutive positive integers. Since $K\ge3P$, the block contains at
least three consecutive multiples of each $p_i$; choose
$m_i,m_i+p_i,m_i+2p_i\in J$. The cell set
$S=\{(m_i,m_i+p_i)\}$ has the distinct differences $p_i$, so $|S|=u$.
Its projections $X(S)$, $Y(S)$ and $W(S)$ consist of the multiples
$m_i$, $m_i+p_i$ and $2(m_i+p_i)-m_i=m_i+2p_i$, all of which are
counted integers of $J$. So the count of $J$ is at least $N(S)$, and the
definition of $\beta$ gives $\log u\le\beta\log N(S)$. Hence the count is
at least $u^{1/\beta}$, and $G_\alpha(u)\ge u^{1/\beta}$. In particular
$\liminf_{u\to\infty}\log G_\alpha(u)/\log u\ge1/\beta$.

**Upper bound.** Fix $3\le\alpha<4$ and $1<\beta'<\beta$. Choose a cell
set $S_0$ with $n=|S_0|\ge2$, $N=N(S_0)$ and $\log n/\log N>\beta'$.
Let $D=\max|y-x|$ and $\Omega=\max(|x|,|y|)$ over $S_0$, and put
$B=2D+1$.

*Tensor powers.* For $k\ge1$ let $S_k$ be the set of pairs
$\bigl(\sum_{i=1}^kx_iB^{i-1},\ \sum_{i=1}^ky_iB^{i-1}\bigr)$ with every
$(x_i,y_i)\in S_0$. The difference of such a pair is
$\sum_i(y_i-x_i)B^{i-1}$, whose digits lie in $[-D,D]$; balanced
base-$B$ digits are unique, so the difference determines every
$y_i-x_i$, hence every cell $(x_i,y_i)$. Therefore $|S_k|=n^k$ and
$y-x$ is injective on $S_k$. The maps $x$, $y$ and $2y-x$ are linear, so
$X(S_k)$ consists of sums $\sum_ix_iB^{i-1}$ with $x_i\in X(S_0)$, and
likewise for $Y$ and $W$; thus $N(S_k)\le N^k$. Finally
$|x|,|y|\le\Omega(B^k-1)/(B-1)\le\Omega B^k=:\omega_k$ on $S_k$.

*Choice of $q$.* By the prime number theorem there is $Q_*$ such that
$\pi(31Q/16)-\pi(17Q/16)\ge Q/(2\log Q)$ for every $Q\ge Q_*$. Let $Q$
be an integer with
$Q\ge\max\bigl(Q_*,\,32\omega_k,\,(16\omega_k+1)/(4-\alpha)\bigr)$.
Every cell $c$ of $S_k$ has $|d(c)|\le2\omega_k\le Q/16$, where
$d(c)=y-x$, so $(Q+d(c),2Q+d(c)]$ contains $(17Q/16,31Q/16]$. Summing
over the $Q$ integers $m\in(Q,2Q]$,

$$
\sum_{Q<m\le2Q}\#\{c\in S_k:\ m+d(c)\text{ prime}\}
=\sum_{c\in S_k}\#\{\text{primes in }(Q+d(c),\,2Q+d(c)]\}
\ \ge\ n^k\,\frac{Q}{2\log Q}.
$$

So some $q\in(Q,2Q]$ makes $q+d(c)$ prime for at least
$n^k/(2\log Q)$ cells $c$. Let $S^*$ be the set of these cells.

*The block.* Take any $S\subseteq S^*$ with $|S|=u\ge1$. The primes
$q+d(c)$, $c\in S$, are distinct, $|x|,|y|\le\omega_k$ on $S$, and
$(4-\alpha)q\ge16\omega_k+1$. By L198 some block of
$\lfloor\alpha P\rfloor$ consecutive positive integers, $P$ the largest of
these primes, contains exactly $|X(S)|+|Y(S)|+|W(S)|\le3N(S_k)\le3N^k$
counted integers. Hence

$$
G_\alpha(u)\le3N^k\qquad\text{whenever }1\le u\le\frac{n^k}{2\log Q}.
$$

*Parameters.* Let $Q_k$ be the least integer satisfying the three lower
bounds above. Since $\omega_k=\Omega B^k$, there is $c_2$, depending on
$\alpha$ and $S_0$, with $\log Q_k\le k\log B+c_2$ for every $k\ge1$.
Given $u\ge2$, let $k\ge1$ be least with $n^k\ge2u(k\log B+c_2)$; then
$u\le n^k/(2\log Q_k)$, so $G_\alpha(u)\le3N^k$. If $k\ge2$, minimality
gives $n^{k-1}<2u((k-1)\log B+c_2)$. Hence
$n^k<2nu(k\log B+c_2)$, and taking logarithms shows $k=O(\log u)$.
Since $N^k=(n^k)^{\log N/\log n}$ and $\log N/\log n<1/\beta'$,

$$
G_\alpha(u)\ \le\ 3\bigl(2nu(k\log B+c_2)\bigr)^{1/\beta'}
=u^{1/\beta'+o(1)}.
$$

Thus $\limsup_{u\to\infty}\log G_\alpha(u)/\log u\le1/\beta'$ for every
$\beta'<\beta$, hence $\le1/\beta$. With the lower bound, the limit
exists and equals $1/\beta$. This completes the proof.
