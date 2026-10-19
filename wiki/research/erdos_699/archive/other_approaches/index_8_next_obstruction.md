---
name: research/erdos_699/archive/other_approaches/index_8_next_obstruction
title: "Erdős 699: the remaining index-eight cofactor obstruction"
desc: "An exact compatibility check isolates a profile that survives the retained sources; a necessary condition explains why a natural quartic identity does not readily improve them. No index-eight effectivity claim."
created: 2026-09-22T08:46:18Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: the remaining index-eight cofactor obstruction

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/index_9_effective|The effective index-nine proof]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]]

The following abstract cofactor profile survives the retained estimates:

$$(r_2,r_3,r_5,r_7)=(1,3,0,2),\qquad
(e_2,e_3,e_5,e_7)=(3/10,3/10,3/10,3/10). \tag{1}$$

As usual, $r_p$ is a position of a maximal $p$-power among the eight
numerator factors, $u_p=(n-r_p)/p^{v_p(n-r_p)}$, and
$e_p=\log u_p/\log(n-7)$. Equation (1) is a profile of real bounds. It is
not an integer realization, a candidate bad triple, or evidence that a
counterexample exists.

The [exact compatibility checker](../../computations/erdos_699_index_8_profile.py)
and [record](../../computations/erdos_699_index_8_profile.json) verify that
(1) satisfies all 162 relevant ordinary pair alternatives and all 680
applicable retained rational clauses. The latter have positive slack of
at least $2480439/10^8$ in their outward-rounded necessary inequalities.
The applicable ordinary product alternatives are satisfied as well.
Directly transferring the 196 retained index-nine polynomial certificates
to their first eight rows gives no positive gain; the best gain is $-17/5$.

This identifies a specific gap in the present proof inputs. It does not
rule out a new Padé estimate or a different polynomial construction.

## The quadratic identities at this assignment

In the order of the four consecutive factors, (1) reads

$$n\leftrightarrow5,\quad n-1\leftrightarrow2,\quad
n-2\leftrightarrow7,\quad n-3\leftrightarrow3.$$

The constant-gap identities available directly are

$$
 n(n-2)-(n-1)^2=-1,
$$
$$
 (n-1)(n-3)-(n-2)^2=-1,
$$
$$
 (n-1)(n-2)-n(n-3)=2.
$$

They involve, respectively, the prime partitions
$\{5,7\}\mid\{2\}$, $\{2,3\}\mid\{7\}$, and
$\{2,7\}\mid\{3,5\}$.

Numerical searches through the retained 104,527 Padé directions did not
exclude (1). The closest sources in that catalog were $9-8$,
$4375-4374$, and $225-224$. A wider continued-fraction search over seed
powers and coefficients supplied no stronger useful four-factor source.
These searches are discovery calculations, not a proof that all parameter
choices fail.

Likewise, adding the tested affine lines, conics, and symmetric curves of
degrees three through five did not improve the numerical polynomial
objective $1.14476569\ldots$. The omitted family of nonsymmetric conics
and their reflections was subsequently checked: its best normalized
improvement score was $0.735016\ldots$, below the required $1$.
The uniform-exponent transition for the coordinate-factor quadratic
program is approximately $0.33616337$. These are diagnostics of the
specified polynomial method, not universal lower bounds for every
possible polynomial proof.

## A quartic identity with a linear error

There is another exact identity:

$$
X=z(z-2)^3,\qquad Y=(z-1)^3(z-3),\qquad X-Y=2z-3. \tag{2}
$$

Unlike the preceding identities, its difference grows with the height.
The natural extension of the rational-block estimate has the form

$$1\le O\!\left(h^{g+\Delta(t)-Ct}
                   +h^{d+\Delta(t)-Kt}\right),\tag{3}$$

where the products have degree $d$, their difference is $O(h^g)$,
$C,K>0$ are Padé decay rates, and

$$
\Delta(t)=\sum_p\bigl(t\lambda_p-m_p(1-e_p)\bigr)_+.
$$

Here $m_p$ is the multiplicity of the factor associated to $p$, and
$\lambda_p$ is its prime-power block length times $\log p$.
A contradiction from (3) requires both exponent inequalities to be
strictly negative. The factor $h^g$ in the first term cannot be omitted.

There is a useful necessary condition for this mechanism. Suppose all
$e_p=e$, put $S=\sum_p\lambda_p$ and $M=\sum_pm_p$, and suppose
$0<C,K<S$. Since

$$
\Delta(t)\ge\max\{0,tS-M(1-e)\},
$$

maximizing the two resulting triangular upper bounds over $t>0$ gives

$$
\boxed{gS<M(1-e)C,\qquad dS<M(1-e)K.} \tag{4}
$$

These conditions are necessary, not sufficient.

For an additional asymptotic comparison, take unit seed coefficients,
comparable seed bases with $\log P\sim\log Q\sim L$, and seed difference
$\delta$ with $\log\delta\sim\kappa L$. Keep the Padé direction ratios
fixed as $L\to\infty$. If their indices are $A,B,C_1$, then, ignoring
terms of lower order in $L$,

$$
C\sim BL,\quad
K\sim\bigl(A+B+C_1-\kappa(A+C_1)\bigr)L,\quad
S\sim(A+2B+C_1)L.
$$

For products using all their factor multiplicities, $M=2d$.
Eliminating $B/(A+C_1)$ from (4) yields the necessary condition

$$\kappa<
\frac{d(1-2e)-g}{2\bigl(d(1-e)-g\bigr)},
\qquad d(1-e)>g. \tag{5}$$

For (2), $d=4$, $g=1$, and $e=3/10$, so (5) requires
$\kappa<1/6$. Equivalently, a nonunit difference must be unusually small
relative to the seed height. Taking powers of (2) worsens this comparison:
then $d=4k$ and $g=4k-3$. For $k=2$ the numerator in (5) is negative; for $k\ge3$, already $d(1-e)\le g$, which is incompatible with the first limiting inequality in (4).

This asymptotic obstruction has the hypotheses just stated. It does not
exclude every small seed, unequal seed size, or more general Padé
construction. A bounded search for (2), including omitted seed-prime
components, found no positive contradiction margin. The entire index-eight
case remains unresolved by these calculations.
