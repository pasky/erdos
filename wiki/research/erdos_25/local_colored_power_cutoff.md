---
name: research/erdos_25/local_colored_power_cutoff
desc: A period-free conditioned power-cutoff estimate and fixed-power-delay natural density for arbitrary local recombinations of finitely many profinite centers.
tags: [density, colored-residues, sieve, conditioned-tails, partial-results]
sources: []
created: 2026-09-22T04:58:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/local_colored_power_cutoff

***

This extends the [coherent power-cutoff argument](coherent_power_cutoff.md)
to systems whose residues can choose different centers at different
primes. The estimate is conditional on actual full first-kill cells and
has no constant depending on an earlier period. It proves natural
density with every fixed power delay, not with the original activation.

## Hypothesis and finite theorem: proved

Fix an integer $R\ge1$ and centers
$\alpha_1,\ldots,\alpha_R\in\widehat{\mathbb Z}$. Consider a finite
increasing-modulus family
$$
 C_q=[a_q]_q
$$
satisfying the following local condition:
$$
 p^e\Vert q\quad\Longrightarrow\quad
 a_q\equiv\alpha_j\pmod{p^e}
 \quad\text{for some }1\le j\le R.
 \tag{1}
$$
The choice of $j$ may depend on both $p$ and $q$. In particular, a
single modulus need not use one common center at all its prime factors.
Thus (1) is more general than a union of $R$ coherent families.

Write
$$
 F_q=C_q\setminus\bigcup_{r<q}C_r,
 \qquad e_q=\mu(F_q).
$$
For any selection $J$ of these cells, put $\tau=\sum_{q\in J}e_q$.
For $0<\eta\le1/2$ and any interval $I$ of $H\ge2$ consecutive
integers, let
$$
 N=\#\{n\in I:n\in F_q\text{ for some }q\in J,
                         \ q\le H^{1-\eta}\}.
$$
There is a constant $C_R$, depending only on $R$, such that
$$
 \frac NH\le C_R\left\{
       \left(\frac{\tau}{\eta^R}\right)^{1/(R+1)}
       +\frac1{\eta\log H}\right\}.
 \tag{2}
$$
The bound is uniform in the centers, local choices in (1), residues,
moduli, selected cells, and location of $I$. The trivial bound $N/H\le1$
may of course be combined with (2). If $\tau=0$, all selected finite
clopen cells are empty and $N=0$.

The proof uses only elementary progression counting, the Selberg
quadratic form proved below, and the estimates
$$
 \sum_{p\le y}\frac{\log p}{p-1}\ll\log y,
 \qquad
 Z_y:=\prod_{p\le y}(1-1/p)^{-1}\ll\log(2y).
 \tag{3}
$$
Their proofs and the checked Euler-product source passage are recorded
in [the coherent argument](coherent_power_cutoff.md#two-elementary-sieve-ingredients).

## An elementary upper sieve of fixed dimension

For each prime $p\le y$, let $\Omega_p\subseteq\mathbb Z/p\mathbb Z$
have size $k_p$, where
$$
 0\le k_p\le R,\qquad k_p<p.
$$
There are constants $B_R,C_R$ such that, on every real interval $K$
of length $M\ge y^{B_R}$,
$$
 \#\{t\in K\cap\mathbb Z:t\bmod p\notin\Omega_p\ (p\le y)\}
 \le C_RM V_y,
 \qquad V_y=\prod_{p\le y}(1-k_p/p).
 \tag{4}
$$

Here is a proof including the uniformity in the residue sets. Omit
primes with $k_p=0$, and set
$$
 g(p)=k_p/p,\qquad h(p)=\frac{g(p)}{1-g(p)}.
$$
Extend these functions multiplicatively to squarefree products of the
remaining primes. All divisor sums in this argument use only such
products. For weights supported on $d\le z$, with $\lambda_1=1$,
the square of the sieve sum majorizes the indicator in (4). CRT gives
the upper bound
$$
 M\sum_{d,e\le z}\lambda_d\lambda_e g([d,e])
 +O\left(\sum_{d,e\le z}|\lambda_d\lambda_e|\,k([d,e])\right),
 \tag{5}
$$
where $k(d)=\prod_{p\mid d}k_p$.

Define $G(z)=\sum_{d\le z}\mu^2(d)h(d)$. The quadratic form in (5)
diagonalizes as
$$
 \sum_{d,e}\lambda_d\lambda_e g([d,e])
 =\sum_r\frac1{h(r)}
           \left(\sum_{r\mid d}\lambda_dg(d)\right)^2.
$$
This follows by expanding
$1/g((d,e))=\sum_{r\mid(d,e)}1/h(r)$.
Its minimum subject to $\lambda_1=1$ is $1/G(z)$. Explicitly, prescribe
$$
 y_r:=\sum_{\substack{d\le z\\r\mid d}}\lambda_dg(d)
       =\frac{\mu(r)h(r)}{G(z)}\qquad(r\le z),
$$
with $y_r=0$ for $r>z$. Here $r$, like $d$, ranges over the supported
squarefree products. Möbius inversion then gives
$$
 \lambda_d=
 \frac{\mu(d)}{g(d)G(z)}
       \sum_{\substack{r\le z\\d\mid r}}\mu^2(r)h(r),
 \qquad |\lambda_d|\le1/g(d)\le d.
$$
In particular the error in (5) is $O(z^6)$, since
$k([d,e])\le[d,e]\le de$.

Normalize the full Euler product
$$
 \sum_d\mu^2(d)h(d)=V_y^{-1}.
$$
It becomes the law of a random squarefree integer $T$ that includes
each prime $p\le y$ independently with probability $g(p)$. By (3),
$$
 \mathbb E\log T=\sum_{p\le y}g(p)\log p\ll R\log y.
$$
Choose a sufficiently large constant $A_R$. Markov's inequality gives
$\Pr(T\le y^{A_R})\ge1/2$, and consequently
$$
 G(y^{A_R})\ge\tfrac12V_y^{-1}.
$$
Also $V_y\gg_R(\log(2y))^{-R}$: the finitely many primes $p\le2R$
cost at most a constant depending on $R$, and at the remaining primes
the ratio of $1-R/p$ to $(1-1/p)^R$ has a convergent product.
Set $z=y^{A_R}$ in (5). For a sufficiently large fixed $B_R$, the
assumption $M\ge y^{B_R}$ absorbs $z^6$ into $C_RMV_y$.
This proves (4).

## The colored smooth part on a translated interval

Discard all moduli above $H^{1-\eta}$. This leaves each retained
first-kill cell unchanged: every discarded modulus is larger than its
label. The total mass of retained selected cells is at most the original
$\tau$, so this truncation is harmless.

Fix a parameter
$$
 0<\theta\le c_R\eta,\qquad y=H^\theta>2R,
 \tag{6}
$$
where $c_R\le1/10$ is small enough that
$H^{\eta/2}\ge y^{B_R}$.
For each $p\le y$, let $b_p$ be minimal with
$p^{b_p}>H^{\eta/4}$. Exclude points satisfying
$n\equiv\alpha_j\pmod{p^{b_p}}$ for at least one pair $(p,j)$.
Progression counting bounds their proportion by
$$
 R\sum_{p\le y}(p^{-b_p}+H^{-1})
 \le R(H^{\theta-\eta/4}+H^{\theta-1}).
 \tag{7}
$$
Profinite centers cause no difficulty here: every count uses only a
specified residue modulo one finite prime power.

Outside this exceptional set, put
$$
 m_p(n)=\max_{1\le j\le R}v_p(n-\alpha_j),\qquad
 D(n)=\prod_{p\le y}p^{m_p(n)}.
$$
All these valuations are finite and smaller than $b_p$. Moreover
$$
 \log D(n)
 \le\sum_{j=1}^R\sum_{p\le y}\sum_{1\le b<b_p}
             (\log p)\mathbf1_{n\equiv\alpha_j\ (p^b)}.
$$
The average of the expression on the right over $I$ is at most
$$
 R\sum_{p\le y}\frac{\log p}{p-1}
 +\frac RH\sum_{p\le y}(b_p-1)\log p
 \ll_R\theta\log H+\eta H^{\theta-1}\log H.
$$
Thus Markov's inequality, together with (7), shows that
$$
 D(n)\le H^{\eta/2}
 \tag{8}
$$
except on a proportion
$$
 \ll_R\frac\theta\eta+H^{-3\eta/20}.
 \tag{9}
$$
Call the remaining points good.

## Haar atoms contained in the actual first-kill cells

Suppose a good point $n$ is counted in $F_q$. For each $p\le y$,
record the pair
$$
 \bigl(m_p(n),\ n\bmod p^{m_p(n)}\bigr).
$$
Define
$$
 M=\prod_{p\le y}p^{m_p(n)}
       \prod_{\substack{p>y\\p^e\Vert q}}p^e.
$$
Condition (1) and $n\in C_q$ imply $m_p(n)\ge v_p(q)$ for every
$p\le y$. Hence
$$
 M=qs\quad\text{for a $y$-smooth integer }s\ge1,
 \qquad M\le qD(n)\le H^{1-\eta/2}.
 \tag{10}
$$

Attach a Haar atom $A$ to this pattern as follows. At each $p\le y$,
fix the recorded residue modulo $p^{m_p}$ and exclude all next-digit
classes modulo $p^{m_p+1}$ belonging to centers that extend that
residue. At $p>y$ with $p^e\Vert q$, fix $a_q\bmod p^e$ and exclude
all center extensions to the next digit. At every other prime
$y<p\le H$, exclude all center residues modulo $p$. Primes above $H$
are unrestricted.

Write $k_p$ for the number of distinct next digits excluded at $p$.
For $p\le y$, the pattern is realized by $n$, so $k_p<p$; also
$k_p\le R$. For $p>y$, we have $k_p\le R<p$. Therefore $A$ is
nonempty and
$$
 \mu(A)=\frac1M\prod_{p\le H}(1-k_p/p).
 \tag{11}
$$

The key inclusion is
$$
 A\subseteq F_q.
 \tag{12}
$$
First, the retained residues show $A\subseteq C_q$. If a point of $A$
matched an earlier class $C_r$, consider each prime power in $r$.
Since $r<q\le H^{1-\eta}<H$, no prime above $H$ needs to be checked.
At $p\le y$, the atom has precisely the same center matches as $n$:
matches through level $m_p$ are determined by the recorded residue,
and every longer center match is excluded. At $p>y$ dividing $q$,
matches through level $v_p(q)$ are also matches of $n$, while longer
matches are excluded. At the other large primes, no center match is
allowed even at level one. Thus matching $C_r$ would force $n\in C_r$,
contrary to $n\in F_q$. This proves (12).

The atom need not contain its generating integer $n$: at large primes
it can discard further center matches possessed by $n$. The inclusion
argument uses only that it never creates a match absent from $n$.

For a fixed $q$, different recorded small-prime patterns give disjoint
atoms. If their maximal valuations differ at a prime, the shallower
pattern excludes every center extension needed by the deeper one; if
the valuations agree but the recorded residues differ, disjointness is
immediate. Consequently the sum of their Haar masses is at most $e_q$.

## Counting a pattern and finishing the finite estimate

All actual points assigned to one pattern lie in a single progression
modulo $M$. We count them using only this progression and the
small-prime exclusions, not the extra large-prime exclusions of the
associated Haar atom. At each $p\le y$, the next-digit exclusions become exactly
$k_p$ forbidden residues modulo $p$ in its quotient variable. This
holds also when $p\mid M$: divide the congruence by the exact power
$p^{m_p}$ in $M$, and the remaining coefficient is invertible modulo
$p$.

The quotient interval has length $H/M\ge H^{\eta/2}\ge y^{B_R}$.
Applying (4), and ignoring any further restrictions on actual points,
bounds their number by
$$
 C_R\frac HM\prod_{p\le y}(1-k_p/p)
 \le C_RH\mu(A)\prod_{y<p\le H}(1-R/p)^{-1}.
$$
Since $y>2R$, the last product is
$$
 \ll_R (Z_H/Z_y)^R
 \ll_R\left(\frac{\log H}{\log y}\right)^R
 =O_R(\theta^{-R}).
$$
Here (3) bounds $Z_H$, while expanding the Euler product gives
$Z_y\ge H_{\lfloor y\rfloor}\ge\log y$.

Sum the disjoint atoms for each selected $q$, then sum the selected
cells and add (9). The result is
$$
 \frac NH\ll_R\frac\tau{\theta^R}
                   +\frac\theta\eta+H^{-3\eta/20}.
 \tag{13}
$$
Choose a constant $A_R'>\log(2R)$ and set
$$
 \theta=\max\left\{(\eta\tau)^{1/(R+1)},
                         \frac{A_R'}{\log H}\right\}.
$$
If $\theta>c_R\eta$, one of the two terms on the right of (2) is
bounded below by a positive constant depending only on $R$, so (2)
follows from $N/H\le1$ after enlarging $C_R$. Otherwise (6) holds,
and substitution in (13), using
$H^{-3\eta/20}\ll1/(\eta\log H)$, proves (2).

## Fixed power delay and the activation checks

For an infinite increasing-modulus family satisfying (1), put
$$
 B_\eta=\{n\ge1:\exists q\le n^{1-\eta},\ n\in C_q\},
 \qquad \beta=\mu\left(\bigcup_q C_q\right),
 \qquad 0<\eta<1.
$$
Then $B_\eta$ has natural density $\beta$, and its complement has
natural density $1-\beta$. Equivalently, every activation rule
$n\ge q^{1+\varepsilon}$, $\varepsilon>0$, has the Haar candidate.

To check the connection with full first-kill cells, let $q(n)$ be the
least full covering modulus of $n$, when one exists. If any modulus is
power-active at $n$, then $q(n)$ is also power-active. Thus the
difference from a fixed finite power-delayed prefix consists precisely
of points in later full first-kill cells with
$q(n)\le n^{1-\eta}$. In particular, for $n\le X$ their labels are at
most $X^{1-\eta}$.

Let the finite prefix have full union measure $\beta_k$ and put
$\tau_k=\beta-\beta_k\downarrow0$. Apply (2) on $[1,X]$ to the finite
system of all moduli at most $X^{1-\eta}$, selecting the cells after
the fixed prefix. These cells are unchanged by the truncation, and
their total Haar mass is at most $\tau_k$. For $0<\eta\le1/2$, the
omitted upper natural density is therefore at most
$$
 C_R(\tau_k/\eta^R)^{1/(R+1)}.
$$
Every fixed prefix has natural density $\beta_k$: its power-delayed
union differs from its periodic full union in only finitely many
integers. Letting $k\to\infty$ proves the assertion. For $1/2<\eta<1$,
squeeze $B_\eta$ between its fixed finite prefixes and $B_{1/2}$.

The finite estimate is uniform over the centers and local choices.
For a fixed infinite system, the natural-density conclusion is also
uniform under common profinite affine automorphisms of all residues:
they preserve the masses $e_q$ and hence $\tau_k$, and the finite-prefix
counting errors are uniform. No uniform decay of $\tau_k$ over
arbitrarily unrelated choices of all the centers is asserted.

## What remains unresolved

The original activation $n\ge q$ corresponds to the missing endpoint
$\eta=0$. Estimate (2) supplies no bound there. The arbitrary locally
$R$-colored problem with original activation remains unresolved by this
argument, already for $R=1$. General arbitrary residues need not satisfy
(1) for any finite $R$; positive Haar survivor measure alone has not
been shown to substitute for that hypothesis.
