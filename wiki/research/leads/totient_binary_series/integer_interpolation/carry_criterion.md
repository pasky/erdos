---
name: research/leads/totient_binary_series/integer_interpolation/carry_criterion
title: The Aggregated Carry Criterion
desc: |
  Two carry conditions retain complete-tail control and admit small finite
  witnesses; positivity refutes the proposed uniform character bound, while
  separate tail and residue depths leave a less restrictive construction.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T11:40:00Z
updated: 2026-10-14T00:26:52Z
---

***

The [[research/leads/totient_binary_series/integer_interpolation/_index|integer
interpolation criterion]] imposes $2k$ or $2k-1$ exact linear equations on
the coefficients and bounds the complete tail by a weighted cost. Its
proof uses only two aggregates of those equations: the residue of one
integer modulo $2^k$ and the vanishing of one other integer. This page
imposes only those two conditions. The tail control is unchanged and
termwise. The conditions admit vectors that fail the exact gap equations;
the best retained witnesses at the sampled orders cost about $2k^2$. All
arguments are author-recorded and unreviewed. Nothing here resolves
[[problems/irrationality/E0249/_index|Problem 249]]: the sufficient asymptotic
condition below is unproved. A proposed all-character covering condition
is refuted below by an unavoidable character. The
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|separate-depth
criterion]] retains the construction while reducing the residue modulus.

## Notation and the exact tail identity

Retain $\Phi_n=\sum_{m\le n}\varphi(m)2^{n-m}$ and
$T_n=2^nS-\Phi_n=\sum_{j\ge1}\varphi(n+j)2^{-j}\in(0,n+2]$ from the
[[research/leads/totient_binary_series/_index|main sketch]]. For $k\ge1$ and
$n\ge0$ put

$$
U_k(n)=\Phi_{n+k}-2^k\Phi_n=\sum_{j=1}^{k}2^{k-j}\varphi(n+j),
\qquad 2^kT_n=U_k(n)+T_{n+k}.
$$

Fix $k\ge3$, a nonzero integer $c$, and a finitely supported integer
vector $y=(y_n)_{n\ge k}$. The support may begin at $n=k$; the
normalization $n\ge k+2$ of the interpolation page is not needed. Define
the integers

$$
u=c+\sum_ny_n2^n,\qquad v=\sum_ny_n\Phi_n,\qquad
W_k(y)=c\,\Phi_k+\sum_ny_nU_k(n),
$$

$$
C_k(y)=|c|(k+2)+\sum_n|y_n|(n+k+2),
$$

and the real number

$$
\Lambda=uS-v=cS+\sum_ny_nT_n.
$$

For $c=2$ these are the quantities of the interpolation page.

**Lemma 1 (exact tail identity).** With
$\rho_k=2^{-k}\bigl(cT_k+\sum_ny_nT_{n+k}\bigr)$,

$$
\Lambda=2^{-k}W_k(y)+\rho_k,\qquad|\rho_k|\le2^{-k}C_k(y).
$$

*Proof.* Substitute $T_n=2^{-k}(U_k(n)+T_{n+k})$ for every $n$ in the
support and $S=T_0=2^{-k}(\Phi_k+T_k)$ for the leading term. The bound
uses $0<T_m\le m+2$ termwise. $\square$

The estimate covers the entire infinite remainder with no averaging and no
exchange of limits; it is the bound (4) of the interpolation page with the
$k$ following gap equations replaced by the one integer $W_k$.

## The criterion

**Proposition 2 (strict form).** Suppose $v\equiv0\pmod{2^k}$ and
$W_k(y)=0$. Then $S\ne a/b$ for every integer $b\ge1$ with
$bC_k(y)<2^k$.

*Proof.* If $S=a/b$ in lowest terms, then $b\Lambda=au-bv\in\mathbb Z$ and
Lemma 1 gives $|b\Lambda|\le b2^{-k}C_k<1$, so $b\Lambda=0$. Since the
support lies in $n\ge k$, $u\equiv c\pmod{2^k}$, and $v\equiv0$, so
$0=b\Lambda\equiv ca\pmod{2^k}$. Now $1<S<3/2$ gives $0<a<3b/2$, and
$C_k\ge|c|(k+2)\ge5|c|$, hence

$$
0<|c|a<\tfrac32|c|b\le\tfrac3{10}\,bC_k(y)<2^k .
$$

So $ca\not\equiv0\pmod{2^k}$, a contradiction. $\square$

The leading coefficient need not be even. Lemma 3 of the
[[research/leads/totient_binary_series/sparse_transforms/gap_multipliers|gap-multiplier
page]] forces an even leading coefficient from the parity of the two
following gap equations; the single aggregate $W_k\equiv0\pmod2$ is
automatic because every $\Phi_m$ and $U_k(m)$ with $m\ge3$ is even, and
the witnesses below include solutions with $c=1$.

**Proposition 3 (slack form).** Let $|c|\le2$ and let $\tilde v$ be the
centered residue of $v$ modulo $2^k$, so $|\tilde v|\le2^{k-1}$. Suppose
$|\tilde v|\le C_k(y)$ and $|W_k(y)|\le C_k(y)$. Then $S\ne a/b$ for every
$b$ with $2bC_k(y)<2^k$.

*Proof.* Lemma 1 gives $|\Lambda|\le2^{1-k}C_k$, so $b\Lambda=0$ as before,
and $b\Lambda\equiv ca-b\tilde v\pmod{2^k}$. The residue is nonzero: it
would vanish only if $\tilde v=cS$, while $S$ and $2S$ are not integers.
Its magnitude is below $\tfrac32|c|b+bC_k\le3b+bC_k\le2bC_k<2^k$, using
$C_k\ge3$. $\square$

For $|c|\ge3$ the slack form needs the additional fact $cS\notin\mathbb Z$,
which a rigorous enclosure can certify for a specified $c$ when it
separates $cS$ from the integers. No such certification for every $c$
is assumed; that would already imply irrationality. The strict form
needs no additional nonvanishing input.

**Relation to the exact systems.** Write $b_{N+j}$ for the product
coefficients of the gap-multiplier page, so that $b_{N+j}=c\varphi(j)+
\sum_ny_n\varphi(n+j)$ for $j\ge1$ and $b_{N-i}=\sum_ny_n\varphi(n-i)$ for
$i\ge0$. Then

$$
W_k(y)=\sum_{j=1}^{k}2^{k-j}b_{N+j},\qquad
v\equiv\sum_{i=0}^{k-1}2^ib_{N-i}\pmod{2^k}.
$$

The central-zero system (1) of the interpolation page makes all $2k$ of
these coefficients vanish and therefore satisfies Proposition 2 with
$c=2$; the central-free system (7) leaves $b_N=c_0$ and satisfies
Proposition 3, since $|c_0|\le C_k$. The gap coefficients need not vanish
here: they must cancel as 2-adic digits with carries. Define

$$
\Gamma^*_k=\min\bigl\{C_k(y):\ c\ne0,\ v\equiv0\ (2^k),\ W_k(y)=0\bigr\}.
$$

The minimum exists and is attained, because the central-zero solutions
supplied by the integer span theorem are admissible with $c=2$. Hence
$\Gamma^*_k\le\Gamma_k$ for the central-zero minimum $\Gamma_k$, and

$$
\liminf_{k\to\infty}\frac{\Gamma^*_k}{2^k}=0
$$

is a sufficient condition for irrationality that is weaker than the
corresponding condition (6) of the interpolation page.

## Two congruences

Let $L$ satisfy $2^L>C_k(y)$ and $L\le k$. Then $v\equiv0\pmod{2^k}$ and
$W_k(y)=0$ hold together exactly when

$$
\sum_ny_n\Phi_n\equiv0\pmod{2^k},\qquad
\sum_ny_n\Phi_{n+k}\equiv-c\,\Phi_k\pmod{2^{k+L}}.
\tag{1}
$$

Indeed $W_k=c\Phi_k+\sum_ny_n\Phi_{n+k}-2^kv$. If $v=2^kq$ then
$2^kv=4^kq\equiv0\pmod{2^{k+L}}$, so the second congruence says
$W_k\equiv0\pmod{2^{k+L}}$. Since $\Phi_k<2^{k+1}$ and
$0<U_k(n)<2^k(n+2)$,

$$
|W_k|<2^k\Bigl(2|c|+\sum_n|y_n|(n+2)\Bigr)\le2^kC_k(y)<2^{k+L},
$$

so the congruence forces $W_k=0$; the converse is immediate. Thus the
criterion is a covering problem for the pairs

$$
g_n=\bigl(\Phi_n\bmod2^k,\ \Phi_{n+k}\bmod2^{k+L}\bigr)
\in G=\mathbb Z/2^k\times\mathbb Z/2^{k+L},
\qquad\tau=(0,\,-c\Phi_k),
$$

with small coefficients. Modulo $2^k$ the integer $\Phi_n$ depends only on
$\varphi(n),\dots,\varphi(n-k+1)$, so the same $2k$ consecutive totients
enter as in the exact system, but aggregated.

**Separate depths and other base points.** The
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
argument]] proves that $v\equiv0\pmod{2^d}$ and $W_J=0$ suffice whenever
$bC_J<2^J$ and $3|c|b\le2^{d+1}$. In particular the residue depth can
grow logarithmically while the tail depth grows linearly in the order.
The two depths need not be equal.
For a different base tail $T_{n_0}$, the leading tail bound becomes
$|c|(n_0+J+2)$ and the residue is $cbT_{n_0}$; its nonvanishing and
magnitude must be kept in the corresponding criterion.

## Integer geometry and the limits of shortcuts

On a finite support of $M\ge1$ indices, strict solutions, when they
exist, form a coset of

$$
K=\left\{y\in\mathbb Z^M:
 \sum_ny_nU_k(n)=0,\quad\sum_ny_n\Phi_n\equiv0\pmod{2^k}\right\}.
$$

This lattice has rank $M-1$. In contrast, the two congruences (1)
define a full-rank affine lattice without the cost restriction;
their equivalence to the strict conditions was proved only inside
that restriction. Let $g$ be the gcd of the positive entries $U_k(n)$.
The integer kernel of the scalar row has covolume $\|U_k\|_2/g$,
and the residue constraint has index at most $2^{k-1}$ because all
$\Phi_n$ are even. Thus

$$
\det K\le2^{k-1}\|U_k\|_2/g\le2^{k-1}\|U_k\|_2.
$$

A determinant bounds a product of lengths, not the covering radius
of a prescribed coset. The descending rounding proof in the
[[research/leads/totient_binary_series/integer_interpolation/geometry|geometry
page]] applies to this finite-index sublattice of the real scalar
kernel, provided that the inhomogeneous coset is nonempty.
On the full interval $[k,R]$, $R\ge2k$, the real minimum-norm solution
has norm $O(|c|\log R/R^{3/2})$: the first summand gives
$U_k(n)\ge2^{k-1}\varphi(n+1)$, and the elementary bound
$\varphi(n+1)\ge(n+1)/(1+\log_2(n+1))$ controls the last half of the
interval. This is not an estimate on arbitrary sparse supports.
For bounded $c$ and $2k\le R=O(k)$, a kernel basis with
$\sum_j\|b_j^*\|_2^2=O(k)$ would give $C_k=O(k^2)$ by that rounding
bound. No such basis estimate is proved.

For an exact scalar equation, the Fourier integral measures the local
mass of $\sum_ny_nU_k(n)$ at its prescribed value. The trivial-character
term $(2h+1)^M/|H|$ in a finite-group count is valid, but the other
scalar modes cannot all be discarded as small errors. Conditioning
on the scalar equation first retains that mass and leaves a separate
residue-distribution obligation.

Some narrower observations replace earlier unsupported exclusions.

- A single nonzero coefficient cannot give a strict solution when
  $|c|\le2$. The totient is two only at 3, 4 and 6, as follows
  directly from its prime factorization formula. For $n\ge6$,
  all $\varphi(n+j)\ge4$, so
  $U_k(n)\ge4(2^k-1)>2\Phi_k$. The remaining pairs $3\le k\le n\le5$
  have $U_k(n)=18,26,24,56,54,112$, respectively for
  $(k,n)=(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)$; each also exceeds
  $2\Phi_k$. Hence no nonzero integer multiple of $U_k(n)$ equals
  $-c\Phi_k$. This conclusion is restricted to these $c$.
- Two or three indices need not have an individually divisible prefix
  numerator. At $k=4$, $c=2$, $y=-e_4-e_5+e_7$ has
  $(\Phi_4,\Phi_5,\Phi_7)=(18,40,170)$, none divisible by 16, but
  $v=112$ and $W_4=36-56-54+74=0$. The contrary necessity claim is
  refuted; no growing few-term family follows from this example.
- Reparametrization through $\Phi_n=2\Phi_{n-1}+\varphi(n)$ can lead
  to a small Diophantine phase. It does not force a large multiplier
  without a separate lower bound for that phase. Under a hypothetical
  rational value, a bounded denominator multiple can make it zero.
  No general exclusion of this approach is retained.
- A homogeneous short-vector theorem does not automatically supply a
  nonzero prescribed leading coefficient. Nor does one expensive
  digit-by-digit construction rule out reductions using other lattice
  directions. These remain construction obligations, not impossibility
  theorems.

## A conditional covering theorem

Let $h\ge1$, let $\mathcal N\subset\{n\ge k\}$ be a finite index set with
$|\mathcal N|=M$, and put

$$
C_{\max}=|c|(k+2)+h\sum_{n\in\mathcal N}(n+k+2),
$$

so every $y\in\{-h,\dots,h\}^{\mathcal N}$ has $C_k(y)\le C_{\max}$.
Choose $L$ with $2^L>C_{\max}$ and $L\le k$, and let
$H\le G$ be the subgroup generated by $\{g_n:n\in\mathcal N\}$. For a
character $\chi$ of $H$ let $\theta_n(\chi)\in\mathbb R/\mathbb Z$ be the
phase of $\chi(g_n)$, and let $\|\cdot\|$ denote the distance to the
nearest integer.

**Theorem 4.** Assume $\tau\in H$ and that every nontrivial character
$\chi$ of $H$ satisfies

$$
\#\Bigl\{n\in\mathcal N:\ \|\theta_n(\chi)\|\ge\frac1{2h+1}\Bigr\}
\ \ge\ B:=2k+L+1.
\tag{2}
$$

Then some $y\in\{-h,\dots,h\}^{\mathcal N}$ satisfies (1); consequently
$\Gamma^*_k\le C_{\max}$, and Proposition 2 excludes every denominator
$b<2^k/C_{\max}$.

*Proof.* For $y\in\{-h,\dots,h\}^{\mathcal N}$ put $\sigma(y)=\sum_ny_ng_n
\in H$. Orthogonality of characters of the finite group $H$ gives

$$
\#\{y:\sigma(y)=\tau\}
=\frac1{|H|}\sum_{\chi}\overline{\chi(\tau)}\,F(\chi),\qquad
F(\chi)=\sum_y\chi(\sigma(y))=\prod_{n\in\mathcal N}D_h(\theta_n(\chi)),
$$

where $D_h(\theta)=\sum_{|t|\le h}e(t\theta)=\sin((2h+1)\pi\theta)/
\sin(\pi\theta)$. The trivial character contributes $(2h+1)^M/|H|$.
For $\|\theta\|\ge1/(2h+1)$ one has
$|D_h(\theta)|\le1/\sin(\pi\|\theta\|)\le1/(2\|\theta\|)\le(2h+1)/2$,
and always $|D_h|\le2h+1$. Under (2) every nontrivial $\chi$ therefore
has $|F(\chi)|\le(2h+1)^M2^{-B}$, and

$$
\Bigl|\#\{y:\sigma(y)=\tau\}-\frac{(2h+1)^M}{|H|}\Bigr|
\le\frac{|H|-1}{|H|}(2h+1)^M2^{-B}
<\frac{(2h+1)^M}{2|H|},
$$

because $2^B=2\cdot2^{2k+L}\ge2|G|\ge2|H|$. The count is positive.
$\square$

For every integer $c$, target membership $\tau\in H$ holds for
sufficiently long prefixes: Proposition 3 of the
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
argument]] supplies $c=1$, and integer multiples supply the others.
There is no quantitative endpoint. More importantly, the other
hypothesis of Theorem 4 can never hold under its stated cost bound.

**Proposition 4a (forced character).** If $\mathcal N\ne\varnothing$,
there is a nontrivial character of $H$ with at most two indices satisfying
the inequality in (2). Thus (2) is impossible for these parameters,
regardless of target membership.

*Proof.* Since $L\le k$, the formula

$$
\chi(x,z)=\exp\left(2\pi i\left(-\frac{x}{2^L}
                                 +\frac{z}{2^{k+L}}\right)\right)
$$

defines a character of $G$. At $g_n$ it has a representative phase

$$
\theta_n=\frac{U_k(n)}{2^{k+L}}>0,
\qquad
\sum_{n\in\mathcal N}\theta_n
 <\frac{\sum_n(n+2)}{2^L}<\frac1h.
\tag{3}
$$

Every phase is less than one, so the restriction to $H$ is nontrivial.
A good index in (2) has $\theta_n\ge1/(2h+1)$, whether or not its
nearest-integer distance is represented by $\theta_n$ itself.
Consequently the number of good indices is strictly less than
$(2h+1)/h\le3$, and is therefore at most two. But
$B=2k+L+1>2$. $\square$

For example, $k=32$, $h=1$, $\mathcal N=\{32,\ldots,159\}$ and $L=15$
have $C_{\max}=16644<32768$. Every phase is below
$161/32768<1/3$, so there are no good indices although (2) asks for
80. The retained full-integer-image certificate at $k=32$, with
support in $[34,100]$, supplies $\tau\in H$ for $c=2$ here.

The Fourier identity and its conditional implication are correct;
its mixing hypothesis is unattainable in this application. This
refutes the proposed proof target, not the carry criterion or its
short solutions. A viable Fourier approach must account for the
scalar direction instead of trying to make all its characters small.
The two-depth page does this algebraically by first conditioning on
$\sum_n y_nU_J(n)=-c\Phi_J$. Existence and residue cancellation in
that bounded slice remain open.

## Character conventions and remaining elementary observations

The observations in this section are retained without a consuming
proof. They do not repair the refuted all-character hypothesis or
establish the needed conditioned residue estimate.

Characters of $H$ can be represented by restrictions of ambient
characters of $G$, but their orders need not agree. For example,
the nontrivial character of $2\mathbb Z/4\mathbb Z$ has order two
and extends to a character of order four on $\mathbb Z/4\mathbb Z$.
Even generators make ambient order-two characters trivial; they do
not remove all order-two characters of $H$.

For a displayed ambient representative

$$
\theta_n=\frac{\alpha\Phi_n+\beta\Phi_{n+k}}{2^j}\pmod1,
$$

with $\alpha,\beta$ not both even and with denominators compatible
with $G$, the following elementary observation remains valid.

**Lemma 5.** Suppose $j\ge2$ and $2^{j-1}\le2h+1$. Put

$$
A_1=\{n\ge4:\varphi(n)\equiv2,\ \varphi(n+k)\equiv0\pmod4\},
\quad
A_2=\{n\ge4:\varphi(n)\equiv0,\ \varphi(n+k)\equiv2\pmod4\}.
$$

The representative phase is at distance at least $1/(2h+1)$ on
$A_1$ when $\alpha$ is odd, and on $A_2$ when $\alpha$ is even
and $\beta$ is odd.

*Proof.* For $m\ge4$, $\Phi_m\equiv\varphi(m)\pmod4$. Thus the
numerator on the indicated set is two modulo four. Its distance
from a multiple of $2^j$ is at least two. $\square$

When $5\nmid k$, primes $p\equiv3\pmod4$ and
$p\equiv-k\pmod5$ belong to $A_1$; primes $p=n+k$ with
$p\equiv3\pmod4$ and $p\equiv k\pmod5$ give $n\in A_2$.
Both are reduced classes modulo 20. The earlier proposed choice
between 5 and 13 did not cover all $k$: both fail at $k=65$.
No quantitative prime count in a growing window is used here.
Likewise, prescribing $j$ distinct auxiliary primes each congruent
to one modulo $2^j$ gives a product at least $2^{j^2}$; that
particular construction is not a polynomial-modulus argument when
$j$ is of order $\log k$. This does not exclude other constructions.

For $n\ge j$, the exact identity

$$
\theta_n=\left\{(\alpha+2^k\beta)2^{n-j}S
             -\frac{\alpha T_n+\beta T_{n+k}}{2^j}\right\}
$$

follows by writing $\Phi_n=2^j\Phi_{n-j}+U_j(n-j)$.
It identifies a relation to the binary orbit of $S$, but supplies
no distribution theorem. The forced character (3) is already
concentrated independently of whether $S$ is rational. Describing
(2) merely as an unproved stronger irrationality hypothesis would
therefore obscure its unconditional failure.

## Finite witnesses

The [[research/leads/totient_binary_series/integer_interpolation/evidence/_index|evidence
folder]] retains exact witnesses of Proposition 2 in
`assets/carry_witnesses.json`, replayed by [carry.py](evidence/carry.py):
for every witness it recomputes $\varphi$ by trial division, $\Phi_n$ by
the recurrence, checks $v\equiv0\pmod{2^k}$ and $W_k=0$ exactly, and
recomputes the cost, support, ratio and the largest excluded denominator
$\lfloor(2^k-1)/C_k\rfloor$. Two kinds of witness are retained.

The first kind is an exact minimum over a finite box: support
$k\le n<k+M$ and $|y_n|\le h$ with the stated $c$, found by
meet-in-the-middle enumeration of both halves of the box on the pair
$(v\bmod2^k,\ W_k)$. The option `--box-minima` re-derives each declared
minimum by the same enumeration in well under a minute; the default
replay takes under a second. A box minimum is an upper bound for $\Gamma^*_k$.

| $k$ | $c$ | box $(M,h)$ | minimum $C_k$ | $C_k/k^2$ | witness |
| --- | --- | --- | --- | --- | --- |
| 3 | 2 | (10,1) | 47 | 5.2 | $-e_5-e_6+e_{11}$ |
| 4 | 2 | (14,2) | 46 | 2.9 | $-e_4-e_5+e_7$ |
| 4 | 1 | (10,1) | 48 | 3.0 | $-e_4-e_7+e_{13}$ |
| 5 | 2 | (16,2) | 78 | 3.1 | $-e_6+2e_8-e_{14}$ |
| 5 | 1 | (12,1) | 78 | 3.1 | $e_5-e_{11}-e_{13}+e_{14}$ |
| 6 | 2 | (16,2) | 90 | 2.5 | $-e_6+e_8+e_{11}-e_{17}$ |
| 6 | 1 | (14,1) | 100 | 2.8 | five terms |
| 8 | 2 | (18,2) | 140 | 2.2 | $e_8+e_{11}-2e_{16}+e_{19}$ |
| 8 | 1 | (18,1) | 170 | 2.7 | six terms, $\pm1$ |
| 10 | 2 | (22,1) | 271 | 2.7 | eight terms, $\pm1$ |
| 12 | 2 | (24,1) | 303 | 2.1 | eight terms, $\pm1$ |
| 14 | 2 | (26,1) | 493 | 2.5 | twelve terms, $\pm1$ |
| 16 | 2 | (28,1) | 614 | 2.4 | twelve terms, $\pm1$ |

For example, at $k=3$ the witness $-e_5-e_6+e_{11}$ has
$v=-\Phi_5-\Phi_6+\Phi_{11}=-40-82+2794=2672=8\cdot334$ and
$W_3=16-(344-320)-(694-656)+(22398-22352)=0$, with cost
$10+10+11+16=47$; numerically $\Lambda=2S-T_5-T_6+T_{11}=0.3506$,
below the bound $47/8$.

The second kind is found by the optional
[carry_reduce.py](evidence/carry_reduce.py), which embeds the two
conditions and the weights $n+k+2$ in an integer lattice, runs LLL and
BKZ with block size $20$ from fpylll on support $[k,R]$ (LLL alone at
$k=384$, in dimension $1157$), and applies exact
improving passes along kernel vectors; every proposal is checked exactly
before output, and the retained values are upper bounds only. The best
retained witness per order and leading coefficient:

| $k$ | best $C_k$ ($c$) | $C_k/k^2$ | support size, $\max\lvert y_n\rvert$ | retained exact-gap cost | its $C_k/k^2$ |
| --- | --- | --- | --- | --- | --- |
| 16 | 510 (2) | 2.0 | 10, 1 | 9776 | 38 |
| 24 | 1026 (1) | 1.8 | 14, 1 | 38364 | 67 |
| 32 | 2157 (1) | 2.1 | 23, 2 | 107670 | 105 |
| 48 | 4988 (1) | 2.2 | 32, 3 | 727704 | 316 |
| 64 | 7736 (1) | 1.9 | 42, 2 | 2433103 | 594 |
| 96 | 17375 (1) | 1.9 | 61, 1 | — | — |
| 128 | 30860 (2) | 1.9 | 81, 3 | — | — |
| 192 | 75379 (1) | 2.0 | 129, 3 | — | — |
| 256 | 140585 (2) | 2.1 | 182, 2 | — | — |
| 384 | 282876 (2) | 1.9 | 248, 2 | — | — |

The exact-gap column is the best retained central-zero cost from the
[[research/leads/totient_binary_series/integer_interpolation/computation|finite
certificates]], also an upper bound. Three statements are supported and
no more. First, $\Gamma^*_k\le\Gamma_k$ holds by definition, and the
retained relaxed witnesses are between $19$ and $315$ times cheaper than
the retained exact-gap witnesses at the common orders. Second, at the
sampled orders from 4 through 384 the best retained
relaxed cost lies between $1.7k^2$ and $3.2k^2$ (the table displays
rounded ratios). The exact-gap column increases from about $38k^2$
to $594k^2$ on its common sampled orders. A heuristic based on the
determinant scale suggests quadratic costs, but a determinant alone
proves no bound for the prescribed coset. Third, no
finite value here excludes a denominator beyond the certified
continued-fraction record, and no table proves $\Gamma^*_k=o(2^k)$; each
lattice witness is one output of a heuristic reduction at one support.
The slack form is vacuous at tiny orders: at $k=3$ it accepts $y=-e_3$
with $C_3=18$, which excludes no denominator.

## Remaining obligations

The all-character condition (2) is refuted and is not a live premise.
The equal-depth criterion still asks for strict carry certificates with
$\Gamma^*_k/2^k$ tending to zero along unbounded orders. The
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
criterion]] permits a slowly growing residue depth and a longer tail;
its qualitative leading-coefficient-one solvability is proved, while
its weighted-cost bound is open. Its conditional residue-count identity
separates the exact scalar equation from the modular constraint, without
assuming independent coordinates after conditioning.

The same page's homogeneous criterion removes the leading coefficient
and the prescribed nonzero target altogether. It asks for an exact
scalar-kernel vector with odd normalized-prefix pairing, support
cutoff $B\to\infty$, and cost $C=o(2^J)$. Such vectors are feasible
on $[J,2J]$ for all sufficiently large $J$ not divisible by 5, using
the stated fixed-modulus prime theorem; their small cost is unproved.
The general positive-row counterexample there explains why many short
even relations and qualitative odd feasibility alone do not suffice.

The finite witnesses support neither an asymptotic law nor a lower
bound on the true minima. Direct integer constructions, controlled
rounding, and analysis of the conditioned residue counts remain possible
next approaches. No single-index obstruction above rules out growing
few-term supports or a different normalization.
