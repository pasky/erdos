---
name: theory/integer_sequences/L269_simplex_affine_fiber_threshold/_proof
title: Fourier avoidance and a flat affine trade
desc: Translation of the additive Fourier transform proves independence below q factors, and a difference of two codimension-two fibers constructs a ternary relation at and above q factors.
tags: [proof, tensor, finite-field]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Fourier avoidance and a flat affine trade

***

This proof is recorded by Plasma AI and has no independent acceptance.
Let $S_q=[I_{q-1}\mid-\mathbf1]$ and let $A=S_q^{\otimes k}$.
Its $q^k$ columns are indexed by $\mathbb F_q^k$. The row space of
$S_q$ consists of all coefficient functions on $\mathbb F_q$ with
sum zero. Thus after complexification the row space of $A$ is spanned
by products of nonconstant additive characters. A coefficient function
$f$ gives a relation $Af=0$ if and only if its additive Fourier
transform vanishes at every frequency with all coordinates nonzero.
This is an equivalence for the actual integer matrix, not a reduction
of its entries modulo the characteristic of the indexing field.

Let $q\ge3$ be a prime power and index the columns by
$x\in\mathbb F_q^k$. Fix $\ell_i\in\mathbb F_q^*$ and $a\in\mathbb F_q$.
The fiber

$$
 H_a=\{x:\ell_1x_1+\cdots+\ell_kx_k=a\}
 \tag{12}
$$

is dissociated **if and only if $k<q$**. In that range it is rationally
independent. At $k\ge q$ it contains a nonzero ternary relation.

For the proof, use the additive Fourier transform on $\mathbb F_q^k$,
with any fixed nontrivial additive character. The relation space of the
simplex tensor consists exactly of functions whose Fourier coefficients
vanish at every frequency with all coordinates nonzero. If $f$ is
supported on $H_a$, translating its Fourier argument by $t\ell$ multiplies
the coefficient by a nonzero phase. When $k<q$, for every frequency
$\xi$ some $t\in\mathbb F_q$ avoids the at most $k$ forbidden values
$-\xi_i/\ell_i$. The frequency $\xi+t\ell$ has all coordinates
nonzero; its coefficient is zero for a relation, so every coefficient of
$f$ is zero. This proves independence.

When $k\ge q$, fix all but $q$ coordinates. On those coordinates choose
distinct $t_i$ running through $\mathbb F_q$, and write
$L(x)=\sum_i\ell_i x_i$, $B(x)=\sum_i t_i\ell_i x_i$.
These two forms are independent. With the adjusted value $a'$ of $L$
and any distinct $b_0,b_1\in\mathbb F_q$, set

$$
 f=1_{\{L=a',\ B=b_0\}}-1_{\{L=a',\ B=b_1\}}.
 \tag{13}
$$

It is nonzero and ternary, with support $2q^{q-2}$. Its Fourier support
lies in $\operatorname{span}\{\ell,(t_i\ell_i)_i\}$. The coefficients
on the line of multiples of $\ell$ vanish because the two fibers have
equal size and the same value of $L$. Every remaining frequency has the
form $u\ell+v(t_i\ell_i)_i$, $v\ne0$, and has a zero coordinate at
$t_i=-u/v$. Thus it is a relation. Fixing the other tensor coordinates
preserves this relation, proving the assertion on $H_a$.

If a nonzero linear form has a zero coefficient, each of its fibers
already contains a full simplex line and is dependent. Consequently at
$k\ge q$ every scalar linear fiber coloring fails, as does any coarsening
of one or any version obtained by permuting the symbols separately in
the coordinates.
