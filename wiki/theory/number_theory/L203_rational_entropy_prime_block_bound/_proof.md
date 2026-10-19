---
name: theory/number_theory/L203_rational_entropy_prime_block_bound/_proof
title: Exact masses, type classes and a prime realization
desc: A fixed rational measure has projection entropy below 0.56213 times its joint entropy; exact type classes turn this strict margin into an all-size prime-block bound.
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

***

All logarithms are natural. On the following seven points $(a,b)$ use
the indicated integer weights, divided by $D=10^6$:

| $(a,b)$ | Weight |
| --- | ---: |
| $(0,1)$ | $250$ |
| $(1,1)$ | $28156$ |
| $(1,0)$ | $224250$ |
| $(2,0)$ | $494688$ |
| $(2,-1)$ | $224250$ |
| $(3,-1)$ | $28156$ |
| $(3,-2)$ | $250$ |

These are Lemm's seven points. Their differences $a-b$ are respectively
$-1,0,1,2,3,4,5$. Let $H$ be the entropy of this probability measure,
and let $h$ be the largest of the entropies of $a$, $b$ and $a+b$.
The marginal weights for $a$ and $b$, in increasing order of their
values, are both

$$
(250,252406,718938,28406),
$$

and those for $a+b$ are $(449000,551000)$. The exact arithmetic
certificate gives

$$
1.2238605<H<1.2238606,\qquad
0.6879584<h<0.6879585,\qquad
\frac hH<\frac{56213}{100000}=:\tau.
$$

**The logarithm certificate.** For a positive rational $t$, reduce it
to $t=2^e r$ with $1\le r<2$. For $v=(r-1)/(r+1)$ and any positive
integer $n$,

$$
0\le\log r-2\sum_{j=0}^{n-1}\frac{v^{2j+1}}{2j+1}
\le\frac{2v^{2n+1}}{(2n+1)(1-v^2)}.
$$

This follows by integrating the geometric series for $2/(1-v^2)$;
the displayed upper bound dominates its positive tail. Use the same
series with $v=1/3$ to enclose $\log2$. Since $v<1/3$ for $r<2$,
$n=32$ suffices for all the displayed enclosures. Applying these rational
bounds to $-\sum p\log p$, with interval directions reversed when
needed, proves the strict inequality $h<\tau H$. The retained
[checker](evidence/main.py) does precisely these rational operations and
fails unless that inequality and the marginal identities hold.

**Integer cells with injective differences.** Replace each source point
by $(x,y)=(2b,a+b)$. Its difference $y-x$ equals $a-b$, and its
projections $x,y,2y-x$ equal $2b,a+b,2a$. Thus the projection
entropies are unchanged. For each integer $m\ge1$ form words of
length $Dm$ in these seven cells, using cell $i$ exactly $m w_i$ times,
where $w_i$ is its weight. Encode a word as

$$
\left(\sum_{j=0}^{Dm-1}x_j11^j,
      \sum_{j=0}^{Dm-1}y_j11^j\right).
$$

The difference digits lie in $[-1,5]\subset[-5,5]$, so balanced
base-eleven uniqueness implies that the encoded difference determines
the word. The cell set $S_m$ therefore has distinct differences and
exactly

$$
n_m=\frac{(Dm)!}{\prod_{i=1}^7(mw_i)!}
$$

cells. A projected word has fixed multiplicities given by the associated
marginal weights. Consequently each projection has at most its
corresponding multinomial count. Writing $N_m$ for the largest of these
three counts, Stirling's formula gives

$$
\log n_m=DmH+O(\log m),\qquad
\log N_m=Dmh+O(\log m).
$$

These are deductions about exact counts, not numerical extrapolations.
In particular $n_m\to\infty$ and
$\log N_m/\log n_m\to h/H<\tau$. Choose a fixed number
$\sigma$ with $h/H<\sigma<\tau$. For sufficiently large $m$,
$N_m\le n_m^\sigma$; increasing a constant covers the remaining $m$.

**Every requested number of primes.** The sequence $n_m$ is strictly
increasing: appending any one fixed word with $w_i$ occurrences of each
cell injects the words for $m$ into those for $m+1$, with additional
words available. Moreover

$$
\frac{n_{m+1}}{n_m}
=\frac{\prod_{j=1}^D(Dm+j)}
       {\prod_{i=1}^7\prod_{j=1}^{w_i}(mw_i+j)}
\longrightarrow
\frac{D^D}{\prod_i w_i^{w_i}}=e^{DH}.
$$

Thus these ratios have a finite bound $R$. Given $u\ge2$, choose the
least $m$ with $n_m\ge u$. For $m>1$ we have $n_m<Ru$, while $m=1$
is covered by a fixed larger constant. Select any $u$ cells of $S_m$.
They still have injective differences, and their three projection sizes
sum to at most $3N_m$. L202 realizes them with exactly this projection
sum as the count in a block of $\lfloor\alpha P\rfloor$ consecutive
positive integers for every $3\le\alpha<4$. It follows that

$$
G_\alpha(u)\le3N_m\le C_0 n_m^\sigma
\le C u^\tau.
$$

All constants arise from the fixed seven-point measure. They are
independent of $\alpha$, which enters only the prime realization.
