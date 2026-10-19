---
name: research/leads/equilateral_two_scale/unit_templates
title: Finite covers of a function-field unit group
desc: |
  A finite cover of the unit group by translated kernels of a functional
  linear over the algebraic numbers would force a finite-dimensional
  quotient, where Cayley transforms rule out the cover. This supplies the
  unit-vector template for the transcendental rigidity argument.
created: 2026-10-17T03:20:00Z
updated: 2026-10-17T03:20:00Z
---

***

Theorem 1 and the all-finite template conversion are covered by the
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|graded whole-conclusion review]].
The project argument is credited to Plasma AI. It supplies the template
input of Proposition 6 of the
[[research/leads/equilateral_two_scale/transcendental_scales|transcendental
account]]. The field hypotheses of the other rigidity lemmas are checked
in the [[research/leads/equilateral_two_scale/rigidity_extension|rigidity
extension]], which composes this input with the triangle argument.

Let $E$ be the complex algebraic numbers, let $F=E\cap\mathbb R$, and let
$x\in\mathbb R$ be transcendental. Write $L$ for the algebraic closure of
$E(x)$ in $\mathbb C$, with its usual conjugation, and
$K_L=\{u\in L:u\bar u=1\}$. All vector spaces and linear functionals in
this account have scalars in $E$, unless a different field is indicated.

**Theorem 1.** There are no finite $Q=\{q_1,\ldots,q_J\}\subset K_L$
and $E$-linear $\lambda:L\to E$ such that $\lambda(1)=1$ and

$$
\prod_{j=1}^J\lambda(q_j u)=0\qquad(u\in K_L).
$$

Consequently every finite subset of $K_L$ has the template property of
Proposition 6 of the transcendental account, by Proposition 8 there.

## Reduction to a finite function field

Suppose such $Q$ and $\lambda$ exist. Choose a finite extension
$N/E(x)$ inside $L$ containing $Q$ and stable under conjugation. Put
$N_0=N\cap\mathbb R$, so $N=N_0(i)$ and $N_0/F(x)$ is finite. Define

$$
T=\frac{x+i}{x-i},\qquad B=E(T)=E(x),\qquad d=[N:B],
\qquad K_N=N\cap K_L.
$$

Thus $T$ is a transcendental unit. The algebra
$A=\operatorname{span}_E K_N\subset N$ contains $T,T^{-1}$ and every
$q_j$, and each $q_j$ is a unit of $A$. It is stable under conjugation.
We restrict $\lambda$ to $N$; the assumed cover still holds on $K_N$ and,
by homogeneity, on every nonzero $E$-multiple of an element of $K_N$.

We need units in linear general position over $B$. There are arbitrarily
large finite subsets of $K_N$ such that every $d$ distinct members are a
$B$-basis of $N$. Here is the number-field general-position argument of
Lemma 3.4 of the
[[../library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|OpenAI plane-coloring manuscript]],
with the infinite base field $F(x)$ in place of $\mathbb Q$.
For $z\in N_0$ use the unit $(1+iz)/(1-iz)$, and express $z$ in a basis of
$N_0/F(x)$. The coordinates of this unit in $N/B$ are rational functions
of those parameters, by the matrix formula for inversion in a finite
extension. Their denominators are nonzero at every tuple in $F(x)^d$.
No nonzero $B$-linear functional $\ell$ vanishes at all these units:
for fixed $a\in N_0$, apply $\ell$ to $(1+iha)/(1-iha)$ for
$h\in F(x)$ and expand the resulting rational identity at $h=0$.
Its constant and linear coefficients give $\ell(1)=\ell(ia)=0$.
As $N_0$ spans $N$ over $B$, this would give $\ell=0$.
The product of the nonzero numerator polynomials for finitely many
hyperplanes cannot vanish on the whole grid over the infinite field
$F(x)$. Choosing each new unit outside the spans of all smaller subsets
of the preceding choices proves the assertion.

Choose a $B$-basis $b_1=1,b_2,\ldots,b_d$ of units, and choose
$n>J(d-1)$ units $s_1,\ldots,s_n$ in this general position. Write

$$
q_j s_k=\sum_{\ell=1}^d r_{jk\ell}(T)b_\ell,
\qquad r_{jk\ell}\in E(T).
$$

For every fixed $j$, any $d$ of the row vectors
$r_{jk}=(r_{jk\ell})_\ell$ form an invertible matrix over $E(T)$.

## A rational Cauchy transform forced by the cover

For $a\in E$ define the vector and the scalar transforms

$$
F_\lambda(a)=\left(\lambda\left(\frac{b_\ell}{T-a}\right)\right)_\ell,
\qquad H_{jk}(a)=\lambda\left(\frac{q_j s_k}{T-a}\right).
$$

There are rational functions $D_{jk}(a)\in E(a)$ with

$$
H_{jk}(a)=r_{jk}(a)F_\lambda(a)+D_{jk}(a).
$$

To see this, subtract $r_{jk\ell}(a)$ from $r_{jk\ell}(T)$ before
dividing by $T-a$. For a fixed rational function $r$, the divided
difference $(r(T)-r(a))/(T-a)$ is a finite sum of fixed rational functions
of $T$ times rational functions of $a$. Apply $\lambda$ after multiplying
by $b_\ell$. Thus each $D_{jk}$ depends linearly on finitely many fixed
values of $\lambda$. Poles in the parameter $a$ are excluded below.

Use parameter pairs

$$
\Omega=\{(a,b):a\in E\setminus\{0\},\ |a|\ne1,
\ b=1/\bar a\}.
$$

This set is Zariski dense in $E^2$. Indeed, the rational change of
variables $a=s+it$, $b=1/(s-it)$ is invertible on a nonempty open set,
and the grid $(s,t)\in F^2$, after removing finitely many polynomial zero
sets, is Zariski dense over $E$. Put

$$
U_{a,b}=\frac{T-b}{T-a}=1+\frac{a-b}{T-a}.
$$

For $(a,b)\in\Omega$, the element $aU_{a,b}$ is a unit, since
$|T|=1$. The cover applied to $s_kU_{a,b}$ gives, for each $k$, some $j$
such that

$$
0=\lambda(q_j s_k)+(a-b)
\bigl(r_{jk}(a)F_\lambda(a)+D_{jk}(a)\bigr).
$$

For any assignment of these $j$'s, at least $d$ selected rows have the
same $j$. Invert their matrix. After excluding finitely many additional
values of $a$, this expresses $F_\lambda(a)$ in one of finitely many forms

$$
F_\lambda(a)=R_\beta(a)+\frac{S_\beta(a)}{a-b},
$$

where $R_\beta,S_\beta$ are rational vectors. Choose one valid branch
at each parameter pair. The resulting finitely many branch sets cover
the remaining part of $\Omega$.

We claim that every Zariski-dense branch has $S_\beta=0$, and that all
Zariski-dense branches have the same $R_\beta$.
For the first assertion, take two pairs $(a,b),(c,e)$ from the same
dense branch and write $h=a-b$, $k'=c-e$. For a fixed $s_k$, apply the
cover to $s_kU_{a,b}U_{c,e}$. The partial-fraction identity gives, for
some $j$,

$$
0=L_j+hH_j(a)+k'H_j(c)
 +\frac{hk'}{a-c}\bigl(H_j(a)-H_j(c)\bigr),
$$

where $L_j=\lambda(q_j s_k)$ and, on this branch,

$$
H_j(a)=V_j(a)+\frac{W_j(a)}h,
\qquad
V_j=r_{jk}R_\beta+D_{jk},\quad W_j=r_{jk}S_\beta.
$$

The product of the displayed expressions over $j$ vanishes on a
Zariski-dense subset of $E^4$. Therefore at least one factor is the zero
rational function. In that factor compare coefficients in the independent
variables $h,k'$. The coefficient of $hk'$ says $V_j(a)=V_j(c)$, so
$V_j$ is constant. The coefficient of $h$ is
$V_j(a)-W_j(c)/(a-c)$; varying $a$ forces both that constant and $W_j$
to vanish. The constant coefficient then gives $L_j=0$.
For each $k$ we have therefore found a $j$ with
$r_{jk}S_\beta=0$. Pigeonhole and the invertibility of any $d$ rows for
one $j$ give $S_\beta=0$.

For two dense branches $\beta,\gamma$, repeat the argument using one
pair from each. Both $S$'s vanish. A zero factor now has coefficients
$L_j=0$, $r_{jk}R_\beta+D_{jk}=0$ and
$r_{jk}R_\gamma+D_{jk}=0$. Again pigeonhole gives
$R_\beta=R_\gamma$. This proves the claim.

There is at least one dense branch: finitely many proper algebraic
subsets cannot cover a dense subset of $E^2$. Every nondense branch lies
in a proper algebraic subset. Consequently there is a unique rational
vector $R_\lambda(a)$ agreeing with $F_\lambda(a)$ outside a proper
algebraic subset of the parameter plane. Moreover all possible
$R_\lambda$, as $\lambda$ varies over functionals obeying the cover,
lie in one fixed finite-dimensional subspace $W\subset E(a)^d$.
For each branch the row inverse is fixed, and its other terms are linear
in finitely many values of $\lambda$; take the sum of these finitely many
spaces. In particular the polynomial degrees at infinity and pole orders
of vectors in $W$ are bounded independently of $\lambda$.
This construction used only the cover equation, so the same $W$ applies
without the normalization $\lambda(1)=1$, including to the zero functional.

## A finite-dimensional quotient

For every $v\in K_N$, the functional $\lambda_v(z)=\lambda(vz)$ obeys
the same cover. Let $\Phi(v)=R_{\lambda_v}\in W$. Finite linear relations
among units hold for their Cauchy transforms, and hence for their rational
vectors: intersect the complements of the finitely many exceptional
algebraic sets. This is still a dense parameter set. Thus $\Phi$ extends
to an $E$-linear map $A\to W$.

Since $T$ is a unit, the exact Cauchy identity yields

$$
\Phi(Tv)(a)=a\Phi(v)(a)+\Lambda(v),
\qquad \Lambda(v)=\bigl(\lambda(vb_\ell)\bigr)_\ell
\quad(v\in A).
$$

Every $\Phi(v)$ is strictly proper at infinity. Otherwise its nonzero
polynomial part, multiplied by $a^m$ in

$$
\Phi(T^m v)=a^m\Phi(v)+
\sum_{j=0}^{m-1}a^{m-1-j}\Lambda(T^jv),
$$

has degree at least $m$, while the sum has degree at most $m-1$.
This contradicts the uniform bound on polynomial degrees in $W$ for
large $m$. Comparing the constant polynomial parts in the one-step
identity shows that $\Lambda(v)$ is minus the $a^{-1}$ coefficient of
$\Phi(v)$. It is therefore determined linearly by $\Phi(v)$.
Multiplication by $T$ consequently induces a linear operator on the
finite-dimensional image of $\Phi$. A nonzero annihilating polynomial
$p\in E[t]$ of that operator gives

$$
\lambda(p(T)v)=0\qquad(v\in A),
$$

using $b_1=1$. If the image is zero the same assertion holds with $p=1$.

The algebra $R=A/p(T)A$ is finite dimensional over $E$. For completeness,
$\dim_E A/(T-a)A\le d$ for every $a\in E$. Any $d+1$ representatives
in $A\subset N$ have a relation over $E(T)$. Clear denominators and
divide all coefficients by their largest common power of $T-a$.
Reduction modulo $(T-a)A$ gives a nontrivial relation over $E$.
The filtration by powers of $T-a$ gives the corresponding bound for
$(T-a)^m$, and factorization of $p$ over $E$, followed by the Chinese
remainder theorem, gives $\dim_E R\le d\deg p$ when $p$ is nonconstant.
The functional $\lambda|_A$ descends to an $E$-linear functional on $R$.
If $R=0$, this already contradicts $\lambda(1)=1$; otherwise proceed as
follows.

## The cover is impossible in the quotient

Real elements of $A$ span $A$ over $E$, since $A$ is stable under
conjugation. Choose real $z_1,\ldots,z_m\in A$ whose images span $R$.
For $t=(t_1,\ldots,t_m)\in F^m$ put $z(t)=\sum t_i z_i$ and

$$
u(t)=\frac{1+iz(t)}{1-iz(t)}\in K_N.
$$

The denominator is invertible in $A$, since
$(1-iz(t))^{-1}=(1+u(t))/2$. In the finite-dimensional algebra $R$,
the coordinates of $u(t)$ are rational functions of $t$ with denominator
nonzero on $F^m$. The cover therefore makes
$\prod_j\lambda(q_j u(t))$ the zero rational function: $F^m$ is
Zariski dense over $E$. One factor, say the $j$th, is identically zero.
Its formal first derivatives at $t=0$ give

$$
2i\lambda(q_j z_i)=0\qquad(1\le i\le m).
$$

The images of $z_i$ span $R$, and $q_j$ is a unit of $R$. Hence the
descended functional is zero on all of $R$. This contradicts
$\lambda(1)=1$, and proves Theorem 1. $\square$
