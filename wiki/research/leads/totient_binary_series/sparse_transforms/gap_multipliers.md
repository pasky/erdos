---
name: research/leads/totient_binary_series/sparse_transforms/gap_multipliers
title: Integer Multipliers with Two Gaps
desc: |
  A sufficient irrationality criterion with exact integral forms, a residue
  nonvanishing test, and a uniform bound on the complete infinite remainder.
problems:
- 249
review_status: unreviewed
created: 2026-09-17T07:14:44Z
updated: 2026-09-17T07:14:44Z
---

***

This is a surviving construction question after the
[[research/leads/totient_binary_series/sparse_transforms/prime_sieve|literal sieve obstruction]]
and the [[research/leads/totient_binary_series/sparse_transforms/logarithmic_products|logarithmic-product obstructions]].
The criterion and proofs below are author-recorded and unreviewed.
An infinite family satisfying the criterion has not been constructed.

Write $A(x)=\sum_{n\ge1}\varphi(n)x^n$ and $S=A(1/2)$.
For $N\ge k\ge3$ let

$$
P(x)=\sum_{i=0}^{N}p_ix^i\in\mathbb Z[x],\qquad
B(x)=\sum_{n=0}^{N}b_nx^n,\qquad b_n=[x^n](PA).
$$

Require the following explicit conditions:

$$
p_N=2,\qquad p_i=0\ (N-k<i<N),
\tag{G1}
$$

$$
b_n=0\ (N-k<n<N),\qquad
[x^n](PA)=0\ (N<n\le N+k).
\tag{G2}
$$

The two gaps in $PA$ flank the possibly nonzero central coefficient
$b_N$. These are finite linear equations in integer coefficients, together
with an affine normalization. The
[[research/leads/totient_binary_series/integer_interpolation/_index|integer
interpolation theorem]] supplies solutions for every fixed $k$, with
$N$ allowed to depend on $k$. It gives no useful bound for $N$ or
the coefficient height.

## The exact arithmetic form and full remainder

Define integers

$$
u=2^NP(1/2),\qquad v=2^NB(1/2),\qquad
\Lambda(P)=uS-v.
$$

Then

$$
\Lambda(P)=\sum_{j\ge1}[x^{N+j}](PA)2^{-j}
 =\sum_{i=0}^Np_iT_{N-i},
\tag{1}
$$

where $T_n=2^nS-\sum_{r\le n}\varphi(r)2^{n-r}$ is the parent's
tail. The second equality is exact, with no extra integer correction.
If $S=a/b$, $b\ge1$, then

$$
b\Lambda(P)=au-bv\in\mathbb Z.
\tag{2}
$$

By (G1)-(G2),

$$
u\equiv2\pmod{2^k},\qquad v\equiv b_N\pmod{2^k}.
\tag{3}
$$

In particular $u\ne0$. Put $H=\max_i|p_i|$. Since $\varphi(t)\le t$,

$$
|b_N|\le\frac{HN(N+1)}2,
\qquad
|\Lambda(P)|\le E_0(P):=
 \frac{\sum_{i=0}^N|p_i|(N+k+2-i)}{2^k}
 \le\frac{H(N+1)(N+k+2)}{2^k}.
\tag{4}
$$

For the remainder bound, all coefficients through $N+k$ after the
central index vanish. Sum
$\sum_i|p_i|(N+j-i)2^{-j}$ over every $j>k$ and use the exact
geometric and arithmetico-geometric sums. This bounds the entire infinite
tail uniformly in the same $N,k,H$ as the lattice computation.

**Proposition 1 (finite certificate).** If (G1)-(G2) hold and
$E\ge|\Lambda(P)|$ is a certified bound, then no rational value of $S$
can have a positive denominator $b$ satisfying

$$
bE<1,\qquad b(|b_N|+3)<2^k.
\tag{5}
$$

*Proof.* The partial sum through six is $41/32$ and its remaining tail
is at most $1/8$, so

$$
\frac{41}{32}<S\le\frac{45}{32}<\frac32.
$$

Consequently $2S$ is not an integer. If $S=a/b$, the integer
$r=2a-bb_N$ is nonzero and satisfies
$|r|<b(|b_N|+3)<2^k$. Equations (2)-(3) show
$b\Lambda(P)\equiv r\pmod{2^k}$, so $b\Lambda(P)$ is a nonzero
integer. But (5) makes its absolute value less than one. $\square$

Notice that the integral form lies in $\mathbb Z$ under rationality;
the modulus $2^k$ is used to certify nonvanishing. It is not a claim that
the form lies in $2^k\mathbb Z$.

**Theorem 2 (growing-family criterion).** Suppose an infinite sequence of
pairs $N\ge k\ge3$ and integer polynomials, with $N\to\infty$,
satisfies (G1)-(G2) and

$$
\frac{H N^2}{2^k}\longrightarrow0.
\tag{6}
$$

Then $S$ is irrational.

*Proof.* Since $k\le N$, (4) makes both $E_0(P)$ and
$(|b_N|+3)/2^k$ tend to zero. For any fixed putative denominator $b$,
(5) eventually holds. $\square$

The missing estimate is the existence of such an affine integer solution
with height $H=o(2^k/N^2)$ for a growing sequence. This is not established
by counting variables or by homogeneous Siegel-lemma bounds: the prescribed
top coefficient must remain exactly two. A shortest homogeneous vector may
have top coefficient zero.

## Normalization and a rational-function control

**Lemma 3.** If $P\in\mathbb Z[x]$ has degree at most $N$ and
$[x^{N+1}]PA=[x^{N+2}]PA=0$, then $p_N$ and $p_{N-1}$ are even.
If the preceding gap in (G1) also holds with $k\ge3$, then $b_N$ is even.

*Proof.* The parity of totients gives $A(x)\equiv x+x^2\pmod2$.
The two following equations give $p_N+p_{N-1}\equiv0$ and
$p_N\equiv0$. The central coefficient is congruent to
$p_{N-1}+p_{N-2}$, both zero in the preceding gap for $k\ge3$.
$\square$

Thus an odd top coefficient cannot work; two is the smallest possible
positive value. A retained witness with top coefficient two proves this
minimum for its specific $(N,k)$, without requiring a complete kernel basis.

**Proposition (truncation transfer).** Let $F\in x\mathbb Z[\![x]\!]$
and $g\in\mathbb Z[\![x]\!]$. Suppose that $N\ge k\ge3$ and that
both $g$ and $gF$ have zero coefficients for
$N-k<n<N$ and for $N<n\le N+k$. For $P=g_{\le N}$ one has

$$
[x^n](PF)=[x^n](gF)\qquad(0\le n\le N+k+1).
$$

Thus $P,PF$ have the preceding and following gaps required above, with
top coefficient $g_N$ and height $\max_{0\le i\le N}|g_i|$.
For $F=A$, this gives (G1)-(G2) exactly when $g_N=2$.

*Proof.* The gap after $N$ gives $g-P\in x^{N+k+1}\mathbb Z[\![x]\!]$.
Since $F$ has no constant term, $(g-P)F$ has order at least $N+k+2$.
The preceding gap of $P$ is inherited from $g$. $\square$

No convergence assumption on $g$ is needed for this finite coefficient
identity. For $F=A$, Lemma 3 forces $g_N$ to be even at any such position;
a sparse integer series with coefficient $+1$ or $-1$ there cannot have
the asserted gaps in its product with $A$. The proposition transfers only
the stated pair of sparse series. It does not assert that arbitrary
product, sieve, or Padé methods supply these gaps or the normalization.

The equations genuinely distinguish the target series from rational
generating functions, in the following precise sense.

**Proposition 4.** Let $F=U/V\in\mathbb Q[\![x]\!]$ be a nonconstant rational
function, with $U,V\in\mathbb Q[x]$, $V(0)\ne0$, and
$d=\max(\deg U,\deg V)$. If $k>d$ and $N\ge k$, there is no polynomial
$P$ of degree $N$ with nonzero $p_N$ for which the same preceding gaps in
$P,PF$ and following gap in $PF$ hold.

*Proof.* Put $C=PF$ and $c_N=[x^N]C$. From $VC=UP$, compare coefficients
at degrees $N,N+1,\ldots,N+d$. The gaps make these equations exactly

$$
c_N V_j=p_N U_j\qquad(0\le j\le d).
$$

Terms below $N$ have degree at most $N-k$ and cannot reach these positions
after multiplication by a polynomial of degree $d<k$; all terms strictly
between $N$ and $N+d$ vanish. Thus $c_NV=p_NU$. As $p_N\ne0$, this would
make $F$ constant, a contradiction. $\square$

The condition that a series is nonrational is much weaker than
irrationality at $1/2$. This control supplies no converse to the criterion.

## Exact finite witnesses and the next construction

The [[research/leads/totient_binary_series/sparse_transforms/evidence/_index|evidence account]]
retains five explicit witnesses, including two gap lengths at $N=300$.
A separate exact checker checks their integer coefficients, all gap
equations, heights, central coefficients, and exact full-tail bounds.
The discovery used lattice reduction. Only the resulting membership and
height upper bounds are claimed; neither minimal height nor saturation of
a sampled kernel basis is inferred from reduction output.

The evidence computes an exact bound sharper than (4). For a fixed
$J\ge k$, let $c_j=[x^{N+j}]PA$ and put

$$
E_J(P)=\left|\sum_{j=k+1}^Jc_j2^{-j}\right|
 +2^{-J}\sum_{i=0}^N|p_i|(N+J+2-i).
\tag{7}
$$

The second term bounds every omitted coefficient, so
$|\Lambda(P)|\le E_J(P)$. Every quantity used in a certificate is
rational and computed exactly; logarithms are only descriptive output.
A finite witness excludes only the bounded denominators in (5), far less
than the parent's continued-fraction exclusion. Its purpose is to test
the construction's constraints and arithmetic, not to improve that exclusion.

A concrete next mechanism is to construct
$P_N=2x^N+P_{0,N}$ with $\deg P_{0,N}$ substantially below $N-k$,
and solve the resulting affine convolution equations with a proved height
bound. One retained witness has $N=300,k=28$ and
$\deg P_{0,N}=155$. A uniform algebraic pattern, or a quantitative theorem
for this particular affine integer system, would advance (6). A larger
table of unstructured short vectors alone would not.

Explicitly, for $D\le N-k$ and $P_{0,N}=\sum_{i=0}^D y_i x^i$,
the equations to solve over $\mathbb Z$ are

$$
\sum_{i=0}^D y_i\varphi(N+j-i)=-2\varphi(j)
 \quad(1\le j\le k),
$$

$$
\sum_{i=0}^D y_i\varphi(N-r-i)=0
 \quad(1\le r<k).
\tag{8}
$$

They give exactly (G1)-(G2), with
$H=\max(2,\max_i|y_i|)$. The next estimate must bound an integer
solution to this inhomogeneous system in a box of size
$o(2^k/N^2)$; rational solvability or a small homogeneous vector is
insufficient.

To compare with the integer-interpolation page, write $z_n=p_{N-n}$
for $n\ge k$ and separate the leading term $p_N=2$. Then (8) becomes
its central-free system, except that its existence theorem uses the
stricter support cutoff $n\ge k+2$. That theorem constructs a solution
within this stricter family for every $k$, so it also proves qualitative
feasibility here. For these reversed coefficients the weighted cost is

$$
C_k(z)=2(k+2)+\sum_n|z_n|(n+k+2)=2^k E_0(P).
$$

It also satisfies $|b_N|+3<C_k(z)$. Therefore $bC_k(z)<2^k$
implies both inequalities of the finite certificate with $E=E_0(P)$.
The weighted-cost criterion can be easier to satisfy than the uniform
height estimate (6), but neither useful asymptotic bound is proved.
All five retained vectors satisfy this page's equations. Reversal of
the $(100,20)$ vector has a nonzero coefficient at $n=20$ and therefore
does not bound the stricter interpolation minimum; the remaining four
have support entirely at $n\ge k+2$ and give finite upper bounds for
its central-free minimum.

## Calibration with Euler's sparse product

Duverney's
[*Irrationalité d'un q-analog de ζ(2)*, C. R. Acad. Sci. Paris Sér. I
321 (1995), pp. 1288-1289, equations (6)-(15)](https://danielduverney.fr/documents/theorie-des-nombres/qAnalogueZeta%282%29.pdf)
supplies the identities

$$
f(x)=\prod_{n\ge1}(1-x^n)
 =1+\sum_{j\ge1}(-1)^j
   \bigl(x^{j(3j-1)/2}+x^{j(3j+1)/2}\bigr),
\qquad f(x)\Sigma(x)=-xf'(x),
$$

where $\Sigma(x)=\sum_{n\ge1}\sigma(n)x^n$.
The required source pages were read visually. Euler's pentagonal identity
is used as a classical input, not proved here. The following direct
truncation argument uses those identities and elementary tail estimates;
it does not use the unread 1993 criterion cited in Duverney's proof.

For $k\ge3$, put $N=k(3k+1)/2$, $\epsilon=(-1)^k$, and
$P_k=f_{\le N}$. Its height is one and its top coefficient is
$\epsilon$. The previous pentagonal index is $N-k$ and the next is
$N+2k+1$. Thus both $f$ and $f\Sigma$ have the required $k-1$
preceding zeros and at least $k$ following zeros. The transfer proposition
gives those gaps for $P_k\Sigma$ and its central coefficient
$c_N=-\epsilon N$. In fact the following gap has exactly $2k$ zeros:
$(P_k-f)\Sigma$ starts no earlier than degree $N+2k+2$, while
$[x^{N+2k+1}]f\Sigma\ne0$.

Let $S_\sigma=\Sigma(1/2)$ and use the same definitions of $u,v,\Lambda$
with $P_k,\Sigma$ in place of $P,A$. Here $\sigma(n)\le n^2$,
since the positive divisors form a subset of $\{1,\ldots,n\}$.
The totient bound (4) therefore does not transfer unchanged. Instead,
summing every term after the following gap of length $k$ gives

$$
|\Lambda_k|
\le 2^{-k}\sum_{i=0}^N|p_i|\bigl((N+k+2-i)^2+2\bigr)
\le\frac{(N+1)((N+k+2)^2+2)}{2^k}\longrightarrow0.
\tag{9}
$$

Here $\sum_{t\ge1}(a+t)^2 2^{-t}=a^2+4a+6$ with $a=N+k-i$,
and $N$ is quadratic in $k$. This controls the complete product remainder,
including the part from $(P_k-f)\Sigma$.

If $S_\sigma=a/b$ with integers $a>0,b\ge1$, then
$b\Lambda_k=au-bv$ is an integer and

$$
b\Lambda_k\equiv\epsilon(a+bN)\pmod{2^k}.
$$

For all sufficiently large $k$, this residue has nonzero absolute value
less than $2^k$, while (9) gives $|b\Lambda_k|<1$, a contradiction.
This recovers the known base-two sigma result by finite multipliers, with
the entire remainder controlled. For the totient series the transfer is
valid, but an infinite family with the requisite even top coefficient,
gaps, and height bound (6) is still missing. No equivalence between this
criterion and all sparse-product methods is asserted.
