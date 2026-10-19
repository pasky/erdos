---
name: research/erdos_699/remaining/details/small_cofactors_effective
title: "Erdős 699: effective exclusion of small cofactors at indices four and five"
desc: "A uniform p-adic logarithm bound forces both selected cofactors to exceed exp(c log n/log log n). This excludes every fixed logarithmic cofactor range effectively, but does not make either whole index effective."
created: 2026-09-22T06:08:17Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: effective exclusion of small cofactors at indices four and five

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|The effectivity reduction]]

***

For $i\in\{4,5\}$, choose positions $r_2,r_3\in\{0,\ldots,i-1\}$
maximizing the respective valuations, and write

$$
n-r_2=2^a u,\qquad n-r_3=3^b v.
$$

There are effectively computable absolute constants $K>0$ and $N_i$ such
that every bad triple at index $i$ with $n\ge N_i$ satisfies

$$\boxed{\min(u,v)>
\frac14\exp\!\left(\frac{\delta_i\log n}
 {2K\log(3\log n)}\right),\qquad
\delta_4=\frac16,\quad\delta_5=\frac25.}\tag{1}$$

In particular, for every fixed real $A\ge0$, all bad triples with
$\min(u,v)\le(\log n)^A$ have an effectively computable upper row bound.
The exponents $a,b$ are unrestricted. This is an effective exclusion of
an infinite family of rows; the range of larger cofactors remains, so
neither entire index becomes effective by this argument.

## A uniform two-prime valuation estimate

We use Yu's theorem in the form stated as Theorem 3.2 in Bacik,
arXiv:2409.01221v5, §3.1; the source provenance section below records
what is held.
For $q\in\{2,3\}$ there is an effectively computable $C_q>0$ such that,
for nonzero rational $q$-adic units $\alpha_1,\alpha_2$ and integers
$e_1,e_2$, if $\Xi=\alpha_1^{e_1}\alpha_2^{e_2}-1\ne0$, then

$$v_q(\Xi)\le C_q A_1A_2\log B,\qquad
A_j\ge\max\{h(\alpha_j),\log q\},\qquad
B\ge\max\{|e_1|,|e_2|,3\}.\tag{2}$$

Here $h(m/d)=\log\max(|m|,|d|)$ for a reduced nonzero rational number.
The theorem requires nonvanishing of $\Xi$, not multiplicative
independence of its bases. Thus rational dependencies cause no missing
case below.

Suppose $\{p,q\}=\{2,3\}$ and

$$
p^a u-q^b v=d,\qquad 0<|d|\le4,\qquad u,v\ge1.
$$

Put $s=v_q(d)$. If $b\le s$, then $b\log q\le\log4$.
Otherwise $v_q(u)=s$, since $p$ is a $q$-adic unit. Set
$u_0=u/q^s$ and $d_0=d/q^s$. Applying (2) to

$$\alpha_1=p,\quad\alpha_2=u_0/d_0,\quad
e_1=a,\quad e_2=1,\quad
\Xi=p^a u_0/d_0-1=q^{b-s}v/d_0$$

is legitimate: both bases are $q$-adic units and $\Xi\ne0$ because
$v>0$. Its valuation is at least $b-s$; equality holds when $q\nmid v$.
We may take $A_1=\log3$ and $A_2=\log(4u)$. Consequently, with

$$
K=4\bigl(1+\max(C_2,C_3)\bigr),
$$

both branches give the convenient uniform bound

$$\boxed{\log(q^b)\le
K\log(4u)\log\max(a,3).}\tag{3}$$

This includes the cases $q\mid d$, negative $d$, and bases equal to
$1$ or $-1$. If one prefers to omit a base equal to $1$, the one-base
instance of Yu's theorem gives the same statement after increasing
$K$ effectively.

## Applying the quartic and quintic certificates

The retained polynomial estimates imply that badness forces

$$
2^a3^b>\kappa_i n^{1+\delta_i},\tag{4}
$$

where one may take

$$\begin{array}{c|c|c|c}
i&\delta_i&\kappa_i&\text{range}\\ \hline
4&1/6&4^{5/6}/12&n\ge12\\
5&2/5&4^{6/5}/240&n\ge20.
\end{array}$$

For $i=4$, these are exactly inequalities (11) and (12) of the
[effectivity note](../../archive/previous_bounds/effectivity.md).
For $i=5$, its inequality (5) has $m=5$, $A=6$, $d=18$, so
$V_5<n^{18/5}/4^{6/5}$. Also
$\binom n5\ge n^5/240$ for $n\ge20$, whence
$U_5>(4^{6/5}/240)n^{7/5}$.
The off-maximum valuation estimate in that note gives
$U_5\le2^a3^b$: the off-maximum factors contribute at most
$[4!]_{\{2,3\}}=[5!]_{\{2,3\}}=24$ before division by $5!$.
This proves (4) in both cases.

If $r_2=r_3$, then $2^a3^b\mid n-r_2\le n$, contradicting (4)
as soon as $\kappa_i n^{\delta_i}\ge1$. Hence the positions are
distinct in the range below, and $d=r_3-r_2$ is nonzero with
$|d|\le4$.

Let

$$
N_i=\max\{20,\ \kappa_i^{-2/\delta_i}\}.
$$

For $n\ge N_i$, use $2^a=(n-r_2)/u\le n/u$ in (4). Then

$$\log(3^b)>
\delta_i\log n+\log u+\log\kappa_i
\ge\frac{\delta_i}{2}\log n+\log u.
\tag{5}$$

On the other hand, $a\le\log n/\log2$ gives
$\log\max(a,3)\le\log(3\log n)$.
Combining (3) and (5), and dropping the nonnegative $\log u$, proves
the lower bound in (1) for $u$. Interchanging the primes and replacing
$d$ by $-d$ proves the same bound for $v$.

## Effectivity of the logarithmic cofactor exclusion

Given $A\ge0$, choose an integer $T\ge4$ large enough that

$$e^T>\frac{2K}{\delta_i}
(T+\log3)(\log4+AT).\tag{6}$$

Such a $T$ can be found effectively. The ratio of the two sides of (6)
is increasing for $T\ge4$, since the logarithmic derivative of
$e^T/((T+\log3)(\log4+AT))$ is positive there.
For

$$
n\ge\max\{N_i,\exp(e^T)\},
$$

equation (1) therefore gives $u,v>(\log n)^A$.
No numerical value of the Yu constants, and hence no numerical stopping
bound for this subfamily, is evaluated here.

## Source provenance

The form of Yu's theorem used above is Theorem 3.2 of Bacik,
arXiv:2409.01221v5, §3.1, which cites Kunrui Yu, *p-adic logarithmic
forms and group varieties II*, Acta Arithmetica 89 (1999), 337–378,
Theorem 1, [DOI](https://doi.org/10.4064/aa-89-4-337-378). Neither source
is held in the library: the repository has no card for Bacik's preprint
or for Yu's paper, the reading copy of the preprint from which the
statement was taken is not retained here, and the statement has not been
checked against Yu's paper. Only this established logarithmic-form
theorem is used here; no claim about the Skolem problem is needed.
