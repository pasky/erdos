---
name: research/leads/totient_binary_series/analytic_sources
title: Mahler and Sparse-Series Criteria for the Totient Generating Function
desc: |
  Non-Mahler specialization, a positive-density obstruction to fixed dyadic
  filters, and transcendental sparse orbit sums with an explicit transfer gap.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T15:14:30Z
updated: 2026-10-13T20:50:32Z
---

***

Put

$$
F(z)=\sum_{n\ge1}\varphi(n)z^n,\qquad S=F(1/2),\qquad\varphi(1)=1.
$$

The series converges absolutely for $|z|<1$ because $\varphi(n)\le n$.
The [[problems/irrationality/E0249/_index|problem page]] records the exact
irrationality question and its partial status search; this page
examines two specified sources, not a new comprehensive status search.
The deductions below are author-recorded and unreviewed. They give no
proof or disproof of the irrationality of $S$.

Bell--Smertnig's theorem implies that $F$ is not $k$-Mahler for any
integer $k\ge2$, hence is not rational as a function. It gives no
arithmetic conclusion about $S$. Kaneko--Suzuki--Tachiya's criteria
fail for the original coefficients, both parity components, and every
fixed nonzero constant-coefficient dyadic filter. A different dyadic
construction does give transcendental values for every nonempty finite
collection of odd-part orbits. Its full omitted tail, however, prevents
transferring the source's small-positive-tail argument to $S$ by simply
letting that collection grow. Signed multipliers remain a distinct
construction question.

## Sources and actual reading

The versions used, filed on their library source cards, are:

- Jason Bell and Daniel Smertnig, *Mahler series with multiplicative
  coefficient sequences*, [arXiv:2603.23456v1](https://arxiv.org/pdf/2603.23456v1),
  submitted 24 March 2026, 29 PDF pages. Theorem 1.3 is on p. 2,
  its totient example on p. 3, the definition of a Mahler equation on
  p. 5, and the final assembly of its proof on p. 27.
- Hajime Kaneko, Yuta Suzuki and Yohei Tachiya, *Refinements of Erdős's
  irrationality criterion for certain sparse infinite series*,
  [arXiv:2601.20743v1](https://arxiv.org/pdf/2601.20743v1), submitted
  28 January 2026, 20 PDF pages; the manuscript's displayed date is
  29 January. Theorems 1--2 are on p. 3, Corollary 2 on p. 4,
  and Theorem 3 and Corollary 3 on p. 5.

The [[../library/irrationality/bell_2026_mahler_series_multiplicative_coefficients/_index|Bell--Smertnig source card]]
names the edition read (arXiv:2603.23456v1) and links
[[../library/irrationality/bell_2026_mahler_series_multiplicative_coefficients/theorem_1_3|Theorem 1.3]].
The [[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/_index|Kaneko--Suzuki--Tachiya holding]]
contains the selected PDF and canonical statements of Theorems 1–3 and
Corollaries 2–3. These extractions have author standing, not independent
acceptance.

Both full PDFs were obtained and their bytes checked. The Bell--Smertnig copy
read is arXiv:2603.23456v1 (687642 bytes), which the library does not hold. The
Kaneko--Suzuki--Tachiya copy read (571434 bytes) is the edition the
[[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/_index|library card]]
names; the library does not hold its file.

All text on Bell--Smertnig pp. 1--29 and Kaneko--Suzuki--Tachiya
pp. 1--20 was read from PDF extraction. Formula fidelity was additionally
checked visually on Bell--Smertnig pp. 2--3, 9--10, 18--19, 27 and
Kaneko--Suzuki--Tachiya pp. 3--7, 11--13, 18--19. Other pages have
text-only reading coverage. The applicable proof routes were followed:
Bell--Smertnig Sections 3--5 and the assembly in Section 8;
Kaneko--Suzuki--Tachiya Lemmas 1--4 and Theorems 1--2, the
integer-base specialization, Corollary 2's polynomial-relation argument,
and the regrouping in Corollary 3. Sections 6--7 of Bell--Smertnig were
also read, but their second case is not needed for the totient.

This is source reading and specialization, not independent acceptance of
complete source-proof compilations. Bell--Smertnig's imported automatic
sequence classification, reduction/lifting theorem, rational multiplicative
sequence classification, and Mahler-denominator criterion remain external
premises at their source standing. Their original proofs were not read here.
The totient-value counting estimate used in KST Corollary 3 is also an
external premise, not a new proof here. None of the elementary support and
tail obstructions below depends on that counting estimate.

## The exact Mahler consequence

A $k$-Mahler equation means a finite relation

$$
P_0(z)F(z)=\sum_{j=1}^{r}P_j(z)F(z^{k^j}),
\qquad P_j\in\mathbb Q[z],\quad P_0\ne0.
\tag{1}
$$

Rational inhomogeneous terms do not enlarge this class: after clearing
denominators, a further Mahler operator annihilates the rational term.
Bell--Smertnig Theorem 1.3 states that a multiplicative coefficient
sequence of a $k$-Mahler series over a characteristic-zero field is
$k$-regular and has a representation

$$
f(p^i m)=g(i)m^r\chi(m)\quad(p\nmid m),
\qquad g(0)=1,
\tag{2}
$$

for some prime $p$, integer $r\ge0$, linear recurrence sequence $g$,
and multiplicative eventually periodic $\chi$.

For $f=\varphi$, setting $i=0$ and $m=\ell$, for primes $\ell\ne p$,
would give

$$
\chi(\ell)=\frac{\ell-1}{\ell^r}.
\tag{3}
$$

The right side takes infinitely many different values. For $r=0$ it is
strictly increasing, for $r=1$ it is $1-1/\ell$, and for $r\ge2$ the
function $(x-1)/x^r$ is strictly decreasing for $x>r/(r-1)$.
An eventually periodic function has finite image. This contradiction
proves the announced specialization: **$F$ is not $k$-Mahler for any
$k\ge2$**. Every rational function regular at zero is $k$-Mahler
(Bell--Smertnig Example 2.4, p. 5), so $F$ is nonrational too.
No distribution theorem for primes in residue classes is needed for
this last specialization.

The applicable branch of the source proof is particularly definite:
for every prime $q$,

$$
\varphi(q^2)-\varphi(q)^2=q(q-1)-(q-1)^2=q-1\ne0.
$$

Thus its Proposition 5.1, pp. 16--19, supplies regularity under the
hypothetical Mahler assumption. Its proof uses roots-of-unity filters
and the denominator calculus of Section 4 to remove non-negligible
Mahler-denominator roots. Proposition 3.4, p. 10, then supplies (2).
For prime-power bases its key Lemma 3.3, p. 9, makes the generating
function restricted to indices coprime to that prime rational, using
reduction to finite fields and the automatic-sequence classification.
Theorem 7.1's completely multiplicative-prime case is unnecessary here.
This identifies the proof dependencies rather than reconstructing their
external proofs.

The multiplicativity hypothesis matters. Corollary 1.4 as printed on
p. 3 omits it, although its proof on p. 27 invokes it through Theorem 1.3
and Proposition 3.1. We use the explicitly stated Theorem 1.3, not that
corollary without its inherited hypothesis.

A rational value at one point does not create an equation (1).
For an explicit separation, the integer series

$$
J(z)=1+(1-2z)F(z)
$$

has $J(1/2)=1$, yet is non-Mahler for every $k$. Otherwise subtracting
the rational function $1$ and dividing by $1-2z$ would make $F$
$k$-Mahler. These closure operations follow by substitution in (1),
clearing denominators, and eliminating a rational inhomogeneous term.
Thus even non-Mahler integer series of radius of convergence at least
one can take rational values at $1/2$. The statement does not assert
that the coefficients of $J$ are multiplicative.

Consequently the source rules out a finite rational-coefficient Mahler
closure containing this $F$. It does not rule out a nonlinear relation,
a relation involving other dilation patterns, a sparse multiplier, or
an arithmetic argument about $S$. Non-Mahler status is also not, by
itself, a proof of transcendence as a function: the latter would need a
separate input. The source's Theorem 1.1 cites such a classification of
algebraic multiplicative series, but that extra conclusion is not needed
here.

## What the sparse criterion actually consumes

For integer coefficients write

$$
\mathcal N_c(x)=\{1\le n<x:c(n)\ne0\},\qquad
S_c(x)=\sum_{1\le n<x}|c(n)|.
$$

KST [[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/theorem_3|Theorem 3]],
p. 5, specializes Theorem 2 to an integer base $t\ge2$.
For fixed integer sequences $a,b$, with $a(n)\ge0$ and infinitely
many nonzero $a(n)$, it requires

$$
\limsup_{n\to\infty}\max\{a(n),|b(n)|\}^{1/n}<t,
\tag{4}
$$

and real sequences $x_j,h_j\ge1$, $x_j\to\infty$, with

$$
S_a(x_j),S_b(x_j)=o(t^{h_j}x_j),\qquad
\#\mathcal N_a(x_j),\#\mathcal N_b(x_j)=o(x_j/h_j).
\tag{5}
$$

Here $h_j$ is the paper's $z_j$, renamed to distinguish it from the
power-series variable. If $b$ has infinite support, there must also
be constants $\Delta,L>1$ such that for every pair $m<m_+$ of
consecutive support positions of $b$ and every real $\mu\ge L$,

$$
m+\Delta\mu<m_+
\quad\Longrightarrow\quad
\mathcal N_a\cap[m+\mu,m+\Delta\mu)\ne\varnothing.
\tag{6}
$$

The conclusion is irrationality of $\sum_{n\ge1}(a(n)+b(n))/t^n$.
The support condition applies separately to both sequences. Signed
cancellation does not waive it.

Theorem 1 exposes the full-tail input behind (5). At $t=2$ the field
has degree one, so its auxiliary coefficient-size factor disappears.
Besides the support condition it requires, for a fixed $0<\eta\le1$,

$$
R_c(2,\eta x_j,h_j)
:=\sum_{1\le N<\eta x_j}\sum_{u\ge h_j}|c(N+u)|2^{-u}
=o(x_j),\qquad c=a,b,
\tag{7}
$$

where $N,u$ are integers. Theorems 1--2 do not replace the infinite
inner sum by a finite window. Lemma 4, pp. 11--12, controls separately
the part with $N+u<x_j$ and the entire part beyond $x_j$; the
subexponential bound in Theorem 2 controls the latter, pp. 12--13.

To see the arithmetic purpose, use the source convention

$$
\xi_N(c)=\sum_{u\ge0}c(N+u)2^{-u}.
\tag{8}
$$

Unlike the parent sketch's $T_N$, this includes the coefficient at $N$.
If $\sum c(n)2^{-n}=A/B$, then
$B\xi_N(c)=A2^N-B\sum_{n<N}c(n)2^{N-n}$ is an integer.
Lemma 2, pp. 7--8, combines the sparse support and (7) to make
$\xi_N(|a+b|)$ small for almost all sampled $N$. Lemma 3, pp. 8--11,
uses (6) to make $\xi_N(a)>\xi_N(|b|)$ on a positive proportion.
Intersecting these sets gives small, nonzero integers under rationality
(Lemma 1, pp. 6--7; Theorem 1, p. 11). This is why both sparsity and
control of the complete tail are essential to this proof.

### Direct and regrouped applications

For $a(n)=\varphi(n)$ and $b(n)=0$, (4) holds, but
$\#\mathcal N_a(x)=x+O(1)$. Since $h_j\ge1$, the last condition in
(5) is impossible for every choice of the auxiliary sequences.
Allowing a signed coefficientwise splitting does not fix this:
if $a(n)+b(n)=\varphi(n)$ then

$$
\#\mathcal N_a(x)+\#\mathcal N_b(x)\ge x+O(1),
$$

which again contradicts (5). The same argument applies to any
coefficient sequence whose support has positive lower density.
It excludes coefficientwise splittings, not different series with
the same value obtained by carrying or an analytic transformation.

Corollary 3, pp. 5 and 18--19, instead groups
$\sum_m f(m)t^{-\varphi(m)}$ by its exponent. Its coefficient at $n$
is $\sum_{\varphi(m)=n}f(m)$, supported on the sparse set of totient
**values**. The proof invokes the Maier--Pomerance bound on that
image and a bound on the size of its inverse images. None makes the
support of $\varphi(n)$ as a numerator sparse. In addition, choosing
$f=\varphi$ would not satisfy the corollary's assumed bound
$\sum_{m\le x}f(m)=O(x(\log x)^\delta)$ for fixed $\delta$.
One can see this without a summatory asymptotic: if $r$ distinct
primes divide $m$, then

$$
\frac{\varphi(m)}m\ge\prod_{i=1}^{r}\frac{i}{i+1}
=\frac1{r+1}\ge\frac1{1+\log_2m}.
$$

Summing over $x/2<m\le x$ gives a lower bound of order
$x^2/\log x$, exceeding $x(\log x)^\delta$ for every fixed $\delta$.
Even if this weight restriction were removed, the denominator would
still be $t^{\varphi(m)}$, a different target.

## The exact dyadic split and a fixed-filter obstruction

Let $O(z)=\sum_{m\text{ odd}}\varphi(m)z^m$ and
$E(z)=F(z)-O(z)$. The identities $\varphi(2n)=2\varphi(n)$ for even $n$ and
$\varphi(2n)=\varphi(n)$ for odd $n$ give, coefficientwise,

$$
E(z)=O(z^2)+2E(z^2)=F(z^2)+E(z^2),
\tag{9}
$$

$$
F(z)-2F(z^2)=O(z)-O(z^2).
\tag{10}
$$

Iteration of (9), justified by absolute convergence, yields

$$
F(z)=O(z)+\sum_{r\ge1}2^{r-1}O(z^{2^r}),\qquad
E(z)=\sum_{r\ge1}F(z^{2^r}).
\tag{11}
$$

The even and odd components each have support density $1/2$ in their
original exponents. Reindexing the even component in base $4$ gives
coefficients $\varphi(2n)$, nonzero at every index, rather than
sparsity. The odd component reindexed in base $4$, up to a factor
$1/2$ and an initial term, similarly has coefficients $\varphi(2n+1)$.
Thus a change of base does not repair (5).

For (10), the coefficient at odd $n$ is $\varphi(n)$, at
$n=2m$ with $m$ odd it is $-\varphi(m)$, and at $4\mid n$ it is zero.
Its support has density $3/4$. One could take $a$ to be its positive
part and $b$ its negative part; their densities are $1/2$ and $1/4$.
Both fail (5). Moreover, rationality of $S$ alone says nothing about
the rationality of $F(1/4)$ or of the value of (10).

**Fixed-filter proposition.** For rational constants $c_0,\ldots,c_J$
not all zero, set

$$
G(z)=\sum_{j=0}^{J}c_jF(z^{2^j}),\qquad
j_0=\min\{j:c_j\ne0\}.
$$

Every exponent $n=2^{j_0}m$ with $m$ odd has coefficient
$c_{j_0}\varphi(m)\ne0$. Terms with $j<j_0$ have zero weight,
and terms with $j>j_0$ cannot reach that exponent. Consequently

$$
\#\mathcal N_G(x)\ge\frac{x}{2^{j_0+1}}+O(1).
\tag{12}
$$

Clearing the fixed rational denominators does not change its support.
No coefficientwise splitting of this fixed filter can meet KST's
support hypotheses. This includes any fixed iterate of a
constant-coefficient dyadic difference operator. It does not include
polynomial coefficients in $z$, products with unrelated series,
infinite filters, or a family whose weights and dilation depth change
with the cutoff. A theorem for such a varying family would require
its own uniform tail estimates; Theorem 3 concerns fixed sequences.

## A genuinely sparse construction: finitely many odd parts

Define

$$
H(z)=z+\sum_{r\ge1}2^{r-1}z^{2^r},\qquad
H(z)-2H(z^2)=z-z^2.
\tag{13}
$$

For odd $m$,
$\varphi(2^rm)=2^{r-1}\varphi(m)$ when $r\ge1$. Therefore

$$
F(z)=\sum_{m\text{ odd}}\varphi(m)H(z^m).
\tag{14}
$$

Let $\mathcal M$ be any fixed nonempty finite set of positive odd
integers and put

$$
F_{\mathcal M}(z)=\sum_{m\in\mathcal M}\varphi(m)H(z^m)
=\sum_{n\ge1}a_{\mathcal M}(n)z^n.
\tag{15}
$$

Its coefficients equal $\varphi(n)$ when the odd part of $n$ belongs
to $\mathcal M$, and zero otherwise. If $s=\#\mathcal M$, then

$$
\#\mathcal N_{a_{\mathcal M}}(x)\le s(1+\log_2x),\qquad
S_{a_{\mathcal M}}(x)\le2sx,\qquad
0\le a_{\mathcal M}(n)\le n.
\tag{16}
$$

For the mass bound, each orbit satisfies
$\sum_{r:2^rm<x}\varphi(2^rm)=2^R\varphi(m)\le x$
if $R\ge1$ is its last included power; the $R=0$ case is smaller
as well. The displayed factor two is a harmless uniform allowance.
Taking $x_j=j+2$, $h_j=\lceil\log_2x_j\rceil$, and $b=0$
verifies every condition of KST Theorem 3. Thus
$F_{\mathcal M}(1/2)$ is irrational.

In fact KST
[[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/corollary_2|Corollary 2]],
p. 4, gives **transcendence**. If $n_k$
enumerates this support, then $k\le s(1+\log_2(n_k+1))$,
while its quantity $Q(x)=\max(x,\max_{m\le x}a_{\mathcal M}(m))$
is just $x$. For every fixed positive integer $\ell$,

$$
\frac{n_k}{k^\ell\log Q(n_k)}
\gg_{s,\ell}\frac{n_k}{(\log n_k)^{\ell+1}}
\longrightarrow\infty.
\tag{17}
$$

The coefficient root-growth is at most one, strictly below two.
Corollary 2 excludes every finite algebraic degree. Its proof,
pp. 14--17, applies the sparse criterion to the coefficients of a
hypothetical polynomial relation; this step is stronger than simply
adding irrational orbit values. No linear independence theorem for
distinct orbits is claimed here.

There is no conflict with Bell--Smertnig. Each fixed $F_{\mathcal M}$
satisfies the inhomogeneous Mahler equation

$$
F_{\mathcal M}(z)-2F_{\mathcal M}(z^2)
=\sum_{m\in\mathcal M}\varphi(m)(z^m-z^{2m}),
\tag{18}
$$

whose right side is a polynomial. Including all odd parts replaces that
polynomial by $O(z)-O(z^2)$, and does not close a Mahler equation.

### The full omitted tail and why the positive transfer fails

For an integer $M\ge1$, take all odd $m\le M$ in (15), denote the
result by $F_M$, and set $R_M=F-F_M$. Its coefficients $r_M(n)$
are nonnegative and supported exactly where the odd part of $n$
exceeds $M$. They vanish for $n\le M$. If $m_*$ is the least odd
integer exceeding $M$, then

$$
0<\varphi(m_*)2^{-m_*}\le R_M(1/2)
\le\sum_{n>M}n2^{-n}=(M+2)2^{-M}.
\tag{19}
$$

This bounds the entire double series omitted from (14), not a finite
number of its orbits. It proves rapid convergence of transcendental
approximants to $S$, but neither their irrationality nor transcendence
is preserved under this limit.

The exact scaled error for a tail test at $N$ is

$$
\xi_N(\varphi)=\xi_N(a_M)+\xi_N(r_M),\qquad
\xi_N(r_M)=2^N\left(R_M(1/2)-\sum_{n<N}r_M(n)2^{-n}\right),
\tag{20}
$$

and (19) gives $\xi_N(r_M)\le(M+2)2^{N-M}$.
The following stronger elementary obstruction distinguishes the two
parameters without relying on that upper bound:

- If $N\le M$, then $a_M(N)=\varphi(N)\ge1$, so
  $\xi_N(a_M)\ge1$.
- If $N>M$, the least odd integer $u\ge N$ has $u-M>0$ and
  $u-N\le1$. It is omitted, so
  $\xi_N(r_M)\ge\varphi(u)2^{N-u}\ge1/2$.

Hence there are no choices $M_j,N_j\to\infty$ for which both positive
scaled tails in (20) tend to zero. In particular, a small tail at a gap
of $F_M$ cannot be transferred to $F$ by discarding its positive
omitted part. Rationality of $S$ also does not make the individual
$F_M(1/2)$ rational, so the source's integer/norm argument cannot be
applied to them under that assumption. This excludes this specific
positive transfer only; signed compensation changes (20) and remains
outside the obstruction.

## A precise next construction that the sources leave available

The supported research choice is to stop seeking a finite Mahler closure
of $F$ or a fixed constant-coefficient dyadic filter satisfying KST.
The finite-orbit construction is a useful calibration of what genuine
sparsity buys, but its positive limit does not supply the target's
integer tail. Pursue a transform that produces a small nonzero form in
$S$ while accounting for all its other values or its full remainder.

One explicit KST-compatible sufficient target is the following. Seek
$G(z)=\sum_{n\ge0}g_nz^n\in\mathbb Z[\![z]\!]$ and
$V(z)=G(z)F(z)=\sum_{n\ge1}v_nz^n$ with fixed constants $C>0$,
integer $d\ge0$, such that:

1. $v_n\ge0$ for every $n$ and infinitely many $v_n$ are nonzero;
   $|g_n|,v_n\le C(n+1)^d$.
2. The union of their positive-index supports has counting function
   $o(x/\log x)$.
3. For every gap $(m,m_+)$ between consecutive support positions
   of $G$ with index at least one, the support of $V$ meets
   $[m+\mu,m+\Delta\mu)$ whenever $\mu\ge L$ and
   $m+\Delta\mu<m_+$, for some fixed $\Delta,L>1$.
   If $G$ has finite positive-index support this requirement is absent.

If these conditions hold and $S=A/B$ with positive integers $A,B$,
apply Theorem 3 with $a(n)=Bv_n$, $b(n)=-Ag_n$ for $n\ge1$.
Use $h_j=\lceil(d+2)\log_2x_j\rceil$: the mass is
$O_{A,B,C}(x_j^{d+1})=o(2^{h_j}x_j)$, the support condition follows
from item 2, and item 3 is exactly (6). Yet absolute convergence and
$V=GF$ give

$$
\sum_{n\ge1}(Bv_n-Ag_n)2^{-n}=Ag_0\in\mathbb Z,
\tag{21}
$$

a contradiction. The constant term was retained explicitly.
This is a sufficient conditional route, not a construction of $G$.
A nonzero $G$ with all coefficients nonnegative cannot satisfy it:
its first positive coefficient makes $GF$ positive at every larger
index. Any viable $G$ must have cancellation.

For any proposed growing truncations, the same parameters must control
the complete tail. For example, let $N\ge1$ and $h\ge0$ be integers.
If $c_n=Bv_n-Ag_n$ vanishes for $N\le n<N+h$, then item 1 gives
the explicit estimate

$$
|\xi_N(c)|\le
C(A+B)2^{-h}(N+h+1)^d K_d,\qquad
K_d=\sum_{u\ge0}(u+1)^d2^{-u}<\infty.
\tag{22}
$$

Indeed, sum every coefficient with $n=N+h+u$ and use
$N+h+u+1\le(N+h+1)(u+1)$. For a family with changing height or
degree, those changes must be included in (22); a finite coefficient
check alone cannot supply the limit. Nonvanishing must also be proved,
either by the KST support-interlacing mechanism or another arithmetic
argument. Equation (7) is the source's averaged alternative to choosing
individual gaps.

This proposed fixed-series target is distinct from the existing
[[research/leads/totient_binary_series/sparse_transforms/gap_multipliers|integer
polynomial multiplier criterion]], which already has a complete-tail
bound and finite feasible witnesses, but lacks a uniform coefficient
cost estimate. Bell--Smertnig does not obstruct that criterion, and
neither source supplies the missing estimate. A next investigation
should exhibit structured signed multipliers, or prove a bound for a
specified growing family, rather than infer impossibility from a
reformulation or from failure of the direct source application.

## Checks and remaining source work

The support statements and bounds above are exposed analytic derivations;
no numerical experiment or formal execution is needed to establish them.
Boundary cases include $m=1$, the exceptional weight at $r=0$ in (13),
$M=1$, and both parities of $N$ in (20). The coefficient at $n=2$ in
(10) is $-1$, whereas that at $n=4$ is zero, confirming the location
of the first dyadic cancellation. No independent review or native tier
is claimed.

The source cards and canonical result extractions linked above
preserve the exact hypotheses and disclosed proof dependencies. Complete
source-proof reconstruction and its independent review remain outstanding;
filing a statement and reading its proof route do not supply that standing.
The missing signed construction and its quantitative full-tail control
remain mathematical work.
