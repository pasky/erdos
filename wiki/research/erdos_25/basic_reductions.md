---
name: research/erdos_25/basic_reductions
desc: Verified finite-truncation bounds and the exact unresolved tail.
tags: [density, reductions]
sources: []
created: 2026-09-21T22:37:44Z
updated: 2026-10-16T06:44:50Z
---


# research/erdos_25/basic_reductions

***

All residues are normalized as $0\le a_i<n_i$. The delayed excluded progression is
$B_i=\{a_i+n_it:t\ge1\}$, including $n_i$ exactly when $a_i=0$.
Write $A^{(k)}=\mathbb N\setminus\bigcup_{i\le k}B_i$ and
$\delta_k=d(A^{(k)})$. This density exists because membership is periodic
modulo $\operatorname{lcm}(n_1,\ldots,n_k)$ once $n\ge n_k$.
Thus $\delta_k\downarrow\delta\in[0,1]$.

For a set $E$, write $H_E(X)=\sum_{n\le X,n\in E}1/n$.
The lower and upper logarithmic densities are the liminf and limsup of
$H_E(X)/\log X$; natural densities use $|E\cap[1,X]|/X$ instead.
Always
$$
\overline d(A)\le\delta,\qquad
\overline{\operatorname{ld}}(A)\le\delta.
$$
In particular $\delta=0$ already implies natural density zero.
Neither bound supplies the missing lower logarithmic estimate.

## Summable reciprocals: proved

For every $X$,
$$
|B_i\cap[1,X]|=\max\{0,\lfloor(X-a_i)/n_i\rfloor\}\le X/n_i.
$$
Only moduli $n_i\le X$ can contribute. Hence
$$
|(A^{(k)}\setminus A)\cap[1,X]|
 \le X\sum_{i>k}1/n_i.
$$
If $\sum_i1/n_i<\infty$, squeezing between the finite truncations proves
$d(A)=\delta$, and partial summation gives logarithmic density $\delta$.
This justifies the infinite union bound directly; countable subadditivity of
upper natural density is not assumed. If the moduli are pairwise coprime,
$\delta_k=\prod_{i\le k}(1-1/n_i)$, so either this case applies or $\delta=0$.

These results agree with Theorems 3.1–3.2 in the
[Chojecki source](../../../library/integer_sequences/chojecki_2026_truncated_congruence_sieves_erdos_problem_25/_index.md),
whose relevant passages were checked.

## Exact first-kill formulation: proved

Put $E_i=B_i\setminus\bigcup_{j<i}B_j$. The $E_i$ are disjoint and exhaust
$\mathbb N\setminus A$. Their periodic densities are
$e_i=\delta_{i-1}-\delta_i$, with $\delta_0=1$, and
$\sum_i e_i=1-\delta$.
Every element of $B_i$ is at least $n_i$, so all earlier congruences are
already active there. Thus its quotient variable $t\ge1$ must avoid exactly
the compatible quotient classes modulo $n_j/\gcd(n_i,n_j)$.
No activation error remains in this quotient description.

The unresolved estimate is
$$
\liminf_{X\to\infty}H_A(X)/\log X\ge\delta.
$$
An equivalent formulation of this candidate-value conclusion is that
$\lim_{k\to\infty}\limsup_{X\to\infty}
H_{A^{(k)}\setminus A}(X)/\log X=0$.
The ambient tail $\bigcup_{i>k}B_i$ need not have small logarithmic density
(example: zero classes for all primes). Any general tail estimate must
retain conditioning on the earlier survivors.

## The conditioned excess does not depend on the prefix: proved

For every $k\ge0$, with $A^{(0)}=\mathbb N$ and $\delta_0=1$,

$$
\limsup_{X\to\infty}\frac{H_{A^{(k)}\setminus A}(X)}{\log X}-(\delta_k-\delta)
=\delta-\liminf_{X\to\infty}\frac{H_A(X)}{\log X}=:\Delta .
\tag{1}
$$

Indeed $A\subseteq A^{(k)}$ and $H_{A^{(k)}}(X)=\delta_k\log X+O_k(1)$, by
eventual periodicity, so the limsup on the left equals
$\delta_k-\liminf_X H_A(X)/\log X$. The conditioned tail therefore exceeds its
Haar mass $\delta_k-\delta$ by the same amount $\Delta\ge0$ for every prefix,
including the empty prefix, where it is the excess of the whole excluded union
over $1-\delta$. Thus the numerical excess is independent of the prefix;
proving that it vanishes is still the unresolved estimate. The identity does
not replace a conditioned estimate by an ambient tail bound.

Consequently the unresolved estimate holds if and only if, for some constant
$C$ that may depend on the family, and for infinitely many $k$,

$$
\limsup_{X\to\infty}\frac{H_{A^{(k)}\setminus A}(X)}{\log X}
\le C(\delta_k-\delta).
$$

Necessity holds with $C=1$. For sufficiency, (1) gives
$\Delta\le(C-1)(\delta_k-\delta)$ along those $k$, and $\delta_k\to\delta$. A
bound $f(\delta_k-\delta)$ with $f(0)=0$ and $f(t)\to0$ as $t\downarrow0$
works equally well. More generally, a bound
$C_k(\delta_k-\delta)+\eta_k$ suffices along any unbounded sequence of prefixes
on which both $C_k(\delta_k-\delta)\to0$ and $\eta_k\to0$. The factors $C_k$
need not themselves stay bounded; their uncontrolled growth is the problem.

The zero class at every prime is the adversarial case for such factors. There
$A=\{1\}$ and $\delta=0$, so $\Delta=0$ and the limsup in (1) equals
$\delta_k$, while the relative tail
$H_{A^{(k)}\setminus A}(X)/H_{A^{(k)}}(X)$ tends to one for every $k$. Hence a
bound on the conditional probability of a later kill, given survival of the
prefix, that tends to zero with the prefix is false in general. For zero
classes the association argument for (2) applies to the increasing event of a
later kill and the decreasing event of prefix survival; it bounds the
conditioned tail by the density of the ambient tail times $H_{A^{(k)}}(X)$, and
that density is one here. The fiber
decomposition of
[[research/erdos_25/unresolved_estimates|the unresolved-estimates note]]
loses a multiplicity factor up to $\tau(L_k)$ for the prefix period $L_k$; its
harmonic change of variables costs only $O(\log L_k)$, which disappears in the
limsup. For zero classes at the first $k$ primes, $\tau(L_k)=2^k$ and

$$
2^k(\delta_k-\delta)
=\prod_{i\le k}2(1-1/p_i)\ge(4/3)^{k-1}.
$$

Thus the universal upper envelope $\tau(L_k)$ cannot simply be absorbed into
the remaining mass. This is an obstruction to that bound, not an assertion
that the prime family has actual quotient-modulus multiplicity $2^k$: for a
new prime the actual multiplicity is one.

The same defect occurs with $\delta>0$, the unresolved case. Choose one prime
$p_j$ in each interval $[2^j,2^{j+1})$, and again take zero residues. The
reciprocals are summable and $\delta=\prod_j(1-1/p_j)>0$. With
$\varepsilon_k=\delta_k-\delta$,

$$
\varepsilon_k\ge\delta_k/p_{k+1}\ge\delta/p_{k+1},\qquad
2^k\varepsilon_k>\delta/4.
$$

The first inequality is just the mass removed by the next prime, still
conditioned on prefix survival. So even a hypothetical estimate with loss
$\tau(L_k)$ does not force a vanishing bound on this already summable family.
A successful general fiber estimate needs a controlled product
$C_k\varepsilon_k$, for example a bounded factor, or a way to exploit actual
multiplicity. Changing the activation shift alone does not provide it.

## An exact finite harmonic inequality for multiples: proved

For a finite set $D$ of positive integers and $M(D)=\bigcup_{q\in D}q\mathbb N$,
$$
H_{M(D)}(X)\le d(M(D))H_{\lfloor X\rfloor}.
\tag{2}
$$
It suffices to retain $q\le X$. Take independent geometric valuations
$\Pr(V_p=e)=(1-1/p)p^{-e}$ for $p\le X$, and put $N=\prod_{p\le X}p^{V_p}$.
The event $N\in M(D)$ is increasing in all valuations, whereas $N\le X$
is decreasing. The association inequality for product measures gives
$$
\Pr(N\in M(D),N\le X)\le d(M(D))\Pr(N\le X).
$$
The law of $N$, conditioned on $N\le X$, gives integer $n\le X$ mass
$1/(nH_{\lfloor X\rfloor})$, proving (2).

For completeness, product association follows by induction on the number
of independent coordinates. In one coordinate,
$2\operatorname{Cov}(f,g)=\mathbb E[(f(V)-f(V'))(g(V)-g(V'))]\ge0$
for increasing $f,g$, where $V'$ is an independent copy. Condition on the
last coordinate, apply induction to the conditional covariance, and then
apply the one-coordinate inequality to the increasing conditional means.
Negating the decreasing indicator gives the displayed reversed inequality.
The same argument applies to the finite number of unbounded geometric
coordinates, or by truncation and bounded convergence.

Inequality (2) also gives a direct proof of the logarithmic-density part of
the Davenport–Erdős theorem. For arbitrary $D$, write
$\beta=\lim_{Y\to\infty}d(M(D\cap[1,Y]))$. Apply (2) to $D\cap[1,X]$ to get
$H_{M(D)}(X)\le\beta H_{\lfloor X\rfloor}$; each fixed finite union supplies
the matching lower limit. Hence $\operatorname{ld}(M(D))=\beta$.
This argument concerns multiples, not arbitrary translated congruences:
the latter event is not increasing in the valuation coordinates.

## A quantitative finite Dirichlet comparison for multiples: proved

The auxiliary estimate in Section 7 of the
[[research/erdos_25/independent/harmonic_bounds_and_common_shifts|independent input]] is valid.
For nonempty finite $D$, put $M=\max D$ and $\beta=d(M(D))$. For $s>1$,
$$
 M^{1-s}\beta
 \le\frac1{\zeta(s)}\sum_{n\in M(D)}n^{-s}
 \le\beta.
 \tag{3}
$$
In particular its convergence to $\beta$ is uniform when
$(s-1)\log M\to0$. The lower bound is an equality for singleton $D$.

Here is a self-contained proof. Under the probability law assigning
integer $n$ mass $n^{-s}/\zeta(s)$, the prime valuations are independent
and satisfy $\Pr(V_p\ge e)=p^{-se}$. For $s>1$ they are stochastically
dominated by the independent Haar valuations, whose tails are $p^{-e}$.
Thus every finite multiples union has Dirichlet probability at most its
natural density, and its complement has probability at least its density.
Only the finitely many primes dividing the generators matter for these
comparisons. This proves the upper bound in (3).

Order the generators $m_i$ and partition $M(D)$ by its first dividing
generator. Its $i$th piece is $m_iS_i$, where
$$
 S_i=\{t\ge1:m_j/(m_i,m_j)\nmid t\text{ for every }j<i\}.
$$
If the piece has density $e_i$, then $d(S_i)=m_ie_i$. Applying the
complement comparison to $S_i$ gives
$$
 \frac1{\zeta(s)}\sum_{n\in m_iS_i}n^{-s}
 \ge m_i^{-s}d(S_i)
 =e_im_i^{1-s}\ge e_iM^{1-s}.
$$
Sum over $i$ to obtain the lower bound. This proof does not extend to
moving residues, since the quotient sets are then not complements of
multiples unions.

## Why the finite-periodic candidate is the right universal target

The statement that **every** delayed singleton family has logarithmic density
is equivalent to the stronger-looking statement that every such density is
the finite-periodic value $\delta$. This is a subfamily extraction principle,
not a proof that either statement holds.

**Proof.** Write $U=\mathbb N\setminus A$, let $\beta=1-\delta$, and suppose
$\lambda=\overline{\operatorname{ld}}(U)>\beta$ for some family. Put
$\varepsilon=(\lambda-\beta)/10$. Choose a finite original prefix $F_0$ whose
excluded periodic density is at least $\beta-\varepsilon$. All subsequently
selected families will contain $F_0$ and be subfamilies of the original.

Suppose the current selected family $F$ is finite. Choose a recovery cutoff
$X$ beyond the previous cutoffs and all its moduli, large enough that
$H_{U_F}(X)/\log X\le\beta+\varepsilon$. Let $m$ be the first original index
with $n_m>X$. The selected family is contained in the original prefix with
indices below $m$. There exist arbitrarily large $Y>X$ such that
$$
\frac{H_U(Y)}{\log Y}\ge\beta+6\varepsilon,
\quad
\frac{H_{U^{(m-1)}}(Y)}{\log Y}\le\beta+\varepsilon,
\quad
\frac{H_{U_F}(Y)}{\log Y}\ge\beta-2\varepsilon.
$$
The first inequality follows from the limsup, and the latter two hold at
every sufficiently large $Y$ by finite periodicity. Thus the original tail
removes harmonic mass at least $5\varepsilon\log Y$ outside the entire
prefix $U^{(m-1)}$, hence outside $U_F$.

Add all original congruences with $X<n_i\le Y$. They capture that entire
tail contribution up to $Y$, and the selected union at $Y$ has normalized
harmonic mass at least $\beta+3\varepsilon$. No newly added class is active
at or below $X$. Repeat, choosing the next recovery cutoff above $Y$.

The final subfamily still uses strictly increasing, unrepeated moduli.
Activation protects both selected cutoff subsequences from every future
addition. Its excluded union therefore has lower logarithmic density at
most $\beta+\varepsilon$ and upper logarithmic density at least
$\beta+3\varepsilon$, so neither it nor its survivor set has logarithmic
density. This proves the extraction claim. Since every original $U$ has
lower logarithmic density at least $\beta$ by finite truncation, the stated
universal equivalence follows. $\square$

A different, structure-preserving version follows from the
[translation-dynamical dichotomy](translation_dynamics.md): any excess
over $\beta$ produces a common profinite translate with logarithmic
oscillation, keeping the entire modulus set and all cylinder compatibility
relations unchanged. This does not establish the needed upper bound.
