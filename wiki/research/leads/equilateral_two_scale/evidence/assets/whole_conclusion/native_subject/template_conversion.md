# wiki/research/leads/equilateral_two_scale/transcendental_scales.md

[cut]

Let $F_x$ be the real closure of $\mathbb Q(x)$ in $\mathbb R$, let
$E_x=F_x(i)$, the algebraic closure of $\mathbb Q(x)$ in $\mathbb C$, and let
$K_x$ be its unit vectors. 

[cut]

- Lemma 2.4 uses that $K_x$ is divisible and that $E_x=aF_x+bF_x$ for
  nonparallel $a,b$; Lemma 2.5 uses an invariant mean on $F_x/\mathbb Z$;
  Lemma 2.6 is general; Lemma 2.7 uses small $t\in F_x$ and the
  decomposition $t=k+k'$ with $k,k'\in K_x$, available because $F_x$ is real
  closed; Lemmas 3.1 and 3.2 hold for any countable divisible abelian
  acting group; Lemma 3.3 uses $\sqrt{AB}\in F_x$ and that equal moduli
  differ by an element of $K_x$; Lemma 3.5 is a statement about any function
  on $F_x\cap[0,\infty)$ satisfying (3.12).


[cut]

## The exact carrier

For every real $x>0$ let $F_x$, $E_x$ and $K_x$ be as above; for algebraic
$x$ they are $F$, $E$ and $K$. A coloring of $E_x$ *avoids* a side when no
equilateral triangle of that side with all vertices in $E_x$ is
monochromatic.

**Proposition 3 (exact carrier).** For every real $x>0$, some two-coloring of
the plane avoids the equilateral triangles of sides $1$ and $x$ if and only
if some two-coloring of $E_x$ does.

*Proof.* Restriction gives one direction. For the other, product compactness,
as in part (b) of the
[[research/leads/equilateral_two_scale/binary_transfer|binary transfer]],
reduces the plane to its finite subsets. Let $p_1,\dots,p_n\in\mathbb C$ and
list the equilateral triangles of sides $1$ and $x$ among them, recording for
each its side and the sign in $p_c-p_a=\omega^{\pm1}(p_b-p_a)$. These
equations, with $|p_b-p_a|^2$ equal to $1$ or $x^2$ as recorded, form in real
coordinates a polynomial system with coefficients in $\mathbb Q(\sqrt3,x)$
that has a real solution. The field $F_x$ is real closed and contains $\sqrt3$
and $x$, and the theory of real closed fields is model complete, so the
inclusion $F_x\subset\mathbb R$ is elementary and the system has a solution
$z_1,\dots,z_n$ with coordinates in $F_x$, that is with $z_k\in E_x$. Each
recorded triple $(z_a,z_b,z_c)$ is an equilateral triangle of side $1$ or $x$
in $E_x$. A coloring of $E_x$ avoiding both sides, read at the $z_k$ and
assigned to the $p_k$, makes no recorded triangle monochromatic, and the
recorded triangles are all the triangles of the finite set. $\square$



[cut]

## A combinatorial form of the number-field step

The proof of Theorem 2.3 in the release uses number fields only in Lemma 3.4
and the completion. The completion needs, for the syndetic cover
$q_1,\dots,q_J$ of (3.16), finitely many finite sets of rotations, each with
$1$ and $i$ in its rational span, one of which lies in $A_0v^{-1}$ for every
$v$. The following property supplies such sets directly.

**Template property.** A finite set $Q=\{q_1,\dots,q_J\}\subset K_x$ has the
template property when there is a finite $\Sigma\subset K_x$ such that, for
every map $j:\Sigma\to\{1,\dots,J\}$, both $1$ and $i$ lie in the
$\mathbb Q$-linear span of $\{q_{j(s)}s:s\in\Sigma\}$.

**Proposition 6.** Suppose every finite subset of $K_x$ has the template
property, and that Lemmas 2.4 to 2.7, 3.1 to 3.3 and 3.5 of the release hold
over $(E_x,K_x)$, as the inspection under the algebraic closure of
$\mathbb Q(x)$ above indicates. Then every $K_x$-invariant probability
measure on the dual of $(E_x)_{\rm disc}$ giving no mass to its continuous
characters is Haar measure.

*Proof.* Follow the completion of the release with the terminal factor and
radial function $m$ on $F_x$. If $m(r)>0$, the set $A_0$ of the release is
syndetic in $K_x$ with some cover $q_1,\dots,q_J$, by the release's argument
from (3.13) along every Følner sequence. Take $\Sigma$ for this cover. For
$v\in K_x$ and $s\in\Sigma$ choose $j(s)$ with $q_{j(s)}sv\in A_0$. The set
$T_v=\{q_{j(s)}s\}$ is one of at most $J^{|\Sigma|}$ sets, each with $1$ and
$i$ in its rational span. Clearing denominators gives one integer
$D_0\ge1$ and one bound $M_0$ with $D_0\cdot1=\sum_{k\in T}a_kk$,
$a_k\in\mathbb Z$, $\sum|a_k|\le M_0$, for every possible $T$; since the real
span of each $T$ contains $1$ and $i$, (3.18) holds with a common $c_0>0$.
The rest of the completion runs verbatim: Lemma 3.5 on $F_x$ gives
$w(2rD_0|\operatorname{Re}v|)\le4M_0H$ when $|\operatorname{Re}v|<c_0/D_0$;
every $t\in F_x\cap[-1,1]$ is a real part of an element of $K_x$, because
$F_x$ is real closed; so $m$ is bounded below on $F_x\cap(0,2rc_0)$,
contradicting Lemma 2.5 over $F_x$. Hence $m$ vanishes off $0$, the measure
is Haar in the ergodic case, and the ergodic decomposition gives the
general case. $\square$



[cut]

The property is an algebraic statement about unit vectors of
$E_x$, with no measure theory. It holds trivially when all the $q_j$ lie in
one coset $q_1K$: take $\Sigma=q_1^{-1}S$ with $S$ from Lemma 3.4 in a number
field containing the algebraic ratios $q_j/q_1$. In general it can be
reduced to algebraic coefficients. If a finite $\Pi\subset K_x$ has, for
every map $l:\Pi\to\{1,\dots,J\}$, both $1$ and $i$ in the $E$-linear span
of $\{q_{l(p)}p\}$, choose a conjugation-stable number field $N=N_0(i)$
containing all the finitely many coefficients, take $S\subset K\cap N$
from Lemma 3.4 with
$|S|>J([N:\mathbb Q]-1)$, and put $\Sigma=\{ps:p\in\Pi,s\in S\}$. For any
$j:\Sigma\to\{1,\dots,J\}$, pigeonhole within each block $pS$ gives a value
$l(p)$ taken on a rational basis $q_{l(p)}pS'$ of $q_{l(p)}pN$, so the
rational span contains $\sum_pq_{l(p)}pN$, which contains $1$ and $i$.



[cut]

**Proposition 7.** Every two-element subset of $K_x$ has the template
property.

*Proof.* Take $Q=\{1,q\}$. If $q\in K$ the one-coset case applies.
Otherwise $q$ is transcendental, since an algebraic unit vector lies in $K$,
and $E(q)$ is a rational function field; write $T$ for $q$ in it. Choose
$b_1,b_2\in E$ with $0<|b_k|<1$ and $b_1/\bar b_1\ne b_2/\bar b_2$, put
$a_k=1/\bar b_k$ and $B_k=(T-b_k)/(1-\bar b_kT)=-a_k(T-b_k)/(T-a_k)$, a
unit vector because $|q|=1$. Let

$$
\Pi=\{1,\;T^{-1},\;B_1,\;B_2,\;T^{-1}B_1,\;T^{-1}B_2,\;B_1B_2\}.
$$

We show that for every choice of $p$ or $Tp$ for each $p\in\Pi$, the
$E$-span of the choices contains $1$. Otherwise some $E$-linear $\lambda$ on
the span $W$ of $1,T,T^{-1},(T-a_1)^{-1},(T-a_2)^{-1}$, which contains
$\Pi$ and $T\Pi$, has $\lambda(1)=1$ and kills every choice. The choices at
$1$ and $T^{-1}$ force $\lambda(T)=\lambda(T^{-1})=0$. If
$\lambda(B_k)\ne0$, the choices at $B_k$ and $T^{-1}B_k$ force
$\lambda(TB_k)=\lambda(T^{-1}B_k)=0$; but

$$
TB_k-a_k^2T^{-1}B_k=-a_k\bigl(T+(a_k-b_k)-a_kb_kT^{-1}\bigr),
$$

so $\lambda(1)=0$, as $a_k\ne b_k$. Hence $\lambda(B_1)=\lambda(B_2)=0$.
Write $B_1B_2=a_1a_2+\sum_kR_k/(T-a_k)$ and
$B_k=-a_k+r_k/(T-a_k)$, with $r_k=a_k(b_k-a_k)$ and
$R_k=r_kB_{k'}(a_k)$, where $k'$ is the other index. Cancelling the poles,

$$
B_1B_2-\sum_k\frac{R_k}{r_k}B_k
=\frac{a_1a_2(b_2-b_1)}{a_1-a_2},\qquad
TB_1B_2-a_1a_2T-\sum_k\frac{a_kR_k}{r_k}B_k
=\frac{a_1a_2(a_1b_1-a_2b_2)}{a_2-a_1},
$$

using $r_k+a_k^2=a_kb_k$ and
$B_{k'}(a_k)=a_{k'}(a_k-b_{k'})/(a_{k'}-a_k)$. Both constants are nonzero,
since $b_1\ne b_2$ and $a_kb_k=b_k/\bar b_k$. So either choice at
$B_1B_2$ forces $\lambda(1)=0$, a contradiction. The $E$-span of every
choice therefore contains $1$ and $i$, and the reduction to algebraic
coefficients gives the template property. $\square$



[cut]

**Proposition 8.** The following are equivalent: (a) every finite subset of
$K_x$ has the template property; (b) every syndetic subset of $K_x$ spans
$E_x$ over $E$; (c) for no $E$-linear functional $\lambda$ on $E_x$ with
$\lambda(1)=1$ is the set $\{u\in K_x:\lambda(u)=0\}$ syndetic in $K_x$.

*Proof.* (a) implies (b): let $K_x=\bigcup_jq_j^{-1}C$ and take $\Sigma$ for
these $q_j$. For $v\in K_x$ choose $j(s)$ with $q_{j(s)}sv\in C$; from a
rational relation $1=\sum_sa_sq_{j(s)}s$ we get $v\in\operatorname{span}C$,
and $K_x$ spans $E_x$. (b) implies (c), since that set spans a subspace of
$\ker\lambda$, which misses $1$. (c) implies (a): if a finite
$Q=\{q_1,\dots,q_J\}$ fails the template property, it fails the
algebraic-coefficient form, so for every finite $\Pi$ some choice
$p\mapsto q_{j(p)}p$ has $1$ outside its $E$-span. Enumerate $K_x$; the
choice sequences on initial segments whose linear systems
$\lambda(1)=1$, $\lambda(q_{j(p)}p)=0$ are consistent form an infinite,
finitely branching tree, and König's lemma gives an infinite branch. A linear
system all of whose finite subsystems are consistent is consistent, so some
$\lambda$ on $E_x$ has $\lambda(1)=1$ and, for every $p\in K_x$, some $j$
with $\lambda(q_jp)=0$; then $\{u\in K_x:\lambda(u)=0\}$ is syndetic with
cover $Q$. $\square$



[cut]
