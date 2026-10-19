---
name: theory/additive_combinatorics/L38_restricted_difference_basis_convergence/_proof
title: Proof of restricted difference-basis convergence
desc: The modular carry covers the initial interval, a square-root-cost patch covers the endpoint, and a liminf subsequence closes the convergence argument.
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Proof of restricted difference-basis convergence

***

Write $F(N)$ for the minimum in
[[theory/additive_combinatorics/L38_restricted_difference_basis_convergence/_index|the statement]].
This minimum exists because the full interval is a permissible set.

Fix an integer $n\ge1$ and choose a set $D\subseteq\{0,\ldots,n\}$ of
size $F(n)$ whose differences contain $0,\ldots,n$.

## External premises and prime choice

[[../library/additive_bases/singer_1938_theorem_finite_projective_geometry_some_applications_number_theory/theorem_p380|Singer's perfect difference-set theorem]]
gives, for every prime $p$ and $q=p^2+p+1$, a set
$S\subseteq\{0,\ldots,q-1\}$ of size $p+1$ such that $S-S$ represents
every residue modulo $q$. Its statement is the consumed premise; its
projective-geometric proof is not independently reconstructed here.

The prime number theorem implies that the largest prime at most $x$ is
$(1+o(1))x$ as $x\to\infty$. Indeed, for each fixed $\varepsilon>0$,
$\pi(x)-\pi((1-\varepsilon)x)\sim\varepsilon x/\log x>0$.
Choose the largest prime $p=p(N)$ with $p^2+p+1\le N/(n+1)$. Then

$$
\frac qN\longrightarrow\frac1{n+1},\qquad
\frac{p+1}{\sqrt N}\longrightarrow\frac1{\sqrt{n+1}}.
$$

Here $n$ is fixed while $N$ tends to infinity. The same prime-number-theorem
input is stated in Section II of the
[[../library/additive_combinatorics/erdos_1948_representation_1/theorem_p1155|Erdős–Gál account]].
Neither classical theorem is claimed as a locally verified source proof.

## The lifted interval

Put $C=qD+S$. It lies in $[0,(n+1)q-1]\subseteq[0,N]$ and has at most
$F(n)(p+1)$ elements. We claim that every integer $x\in[0,nq]$ belongs
to $C-C$.

Write $x=aq+b$ with $0\le b<q$. If $b=0$, use any $s\in S$ twice and
a difference $a\in D-D$, where $0\le a\le n$; this includes $x=nq$.
If $b>0$, then $0\le a\le n-1$. Choose $s,t\in S$ with
$s-t\equiv b\pmod q$. The range of the representatives forces
$s-t=b$ or $s-t=b-q$. In the first case use a difference $a$ from
$D-D$, and in the second use $a+1$. Both are available. Thus $x$ is a
difference of two members of $C$ in either case.

## The endpoint patch

Set $\Delta=N-nq$, $s=\lceil\sqrt\Delta\rceil$ and
$J=\lceil\Delta/s\rceil$. For fixed $n$ and sufficiently large $N$,

$$
Js\le\Delta+s<N,
$$

because $\Delta/N\to1/(n+1)<1$ and $s/N\to0$. Consequently every mark
in

$$
P=\{0,1,\ldots,s\}\ \cup\ \{N-js:0\le j\le J\}
$$

lies in $[0,N]$. For a fixed $j$, subtracting $0,\ldots,s$ from $N-js$
covers every integer in $[N-(j+1)s,N-js]$. These intervals join without
gaps, and $Js\ge\Delta$, so their union contains $[nq,N]$. Moreover,

$$
|P|\le s+J+2\le2\sqrt\Delta+4.
$$

The second inequality follows from $s\le\sqrt\Delta+1$ and
$J\le\Delta/s+1\le\sqrt\Delta+1$.
The set $C\cup P$ is therefore a restricted difference basis for $[0,N]$,
and

$$
F(N)\le F(n)(p+1)+2\sqrt{N-nq}+4.
$$

Dividing by $\sqrt N$ and taking the limit superior proves

$$
\limsup_{N\to\infty}\frac{F(N)}{\sqrt N}
\le\frac{F(n)+2}{\sqrt{n+1}}. \tag{1}
$$

## Convergence and the infimum

Taking $n=1$ in (1) makes the limit superior finite. Let
$\ell=\liminf_N F(N)/\sqrt N$, and take $n_j\to\infty$ such that
$F(n_j)/\sqrt{n_j}\to\ell$. Apply (1) separately for each fixed $n_j$,
then let $j$ tend to infinity. Its right side tends to $\ell$, so the
limit superior is at most the limit inferior. The finite limit $L$ exists.

For each $n$, (1) gives $L\le(F(n)+2)/\sqrt{n+1}$. These right sides
themselves tend to $L$ as $n\to\infty$, proving

$$
L=\inf_{n\ge1}\frac{F(n)+2}{\sqrt{n+1}}.
$$

The construction supplies no cost-free coverage of $(nq,(n+1)q)$, so it
does not prove the different infimum formula without the additive two.
