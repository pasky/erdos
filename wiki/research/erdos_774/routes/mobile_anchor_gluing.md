---
name: research/erdos_774/routes/mobile_anchor_gluing
title: Mobile anchors and triangular gluing
desc: Triangular buffers give exact saturation and small analytic loss; for finite-threshold sources, buffers above an explicit source-dependent length prevent chromatic increase.
tags: [E0774, proved, construction, obstruction]
sources: []
created: 2026-09-18T00:51:00Z
updated: 2026-09-18T00:58:28Z
---


# Mobile anchors and triangular gluing

***

## Motivation and exact remaining requirement

In every proper $q$-coloring of a configuration with coloring number
exactly $q$, each pair of color classes has a nonzero common signed sum:
otherwise their union is dissociated and the two colors can be merged.
These pairwise sums may depend on the coloring and need not be roots.
They offer a possible replacement for the universal anchors lost by
[simplex gluing](anchor_gluing.md).

The constructions below control the **entire rational ternary closure**,
not merely planted rows. For a fixed source with finite $\tau_q$, they
exclude triangular padding whose buffer lengths all exceed the explicit
source-dependent threshold below. They do not exclude shorter buffers,
changing sources with changing thresholds, or sources with $\tau_q=\infty$.
Recurrent constraint interaction is a possible way to leave this excluded
class, not a proved necessary feature of every successful construction.

## Arbitrary mobile words eventually separate — proved

Let $\chi(B)=q$, $U_q(B)=\{0\}$, and $T=\tau_q(B)<\infty$.
Set

$$
H=\max_{\text{rational lines }L}|(\Sigma(B)\cap L)\setminus\{0\}|,
\qquad h=2+\lceil T\log(qH)\rceil.
$$

For any nonzero rational anchor word $u_1,\ldots,u_m$, $m\geq h$,
there are proper base colorings $f_i$ satisfying, for every color $c$,

$$
\bigcap_{i=1}^m
\{t\in\mathbb Q:t u_i\in\Sigma(f_i^{-1}(c))\}=\{0\}. \tag{1}
$$

Fix a $T$-element separating family of colorings. After choosing the
first coloring, at most $qH$ nonzero pairs $(c,t)$ remain. At any
later block each surviving pair is omitted by at least one member of the
family. A greedy choice reduces the survivor count by a factor at most
$1-1/T$. After $m-1>T\log(qH)$ steps the count is less than one.

If $B\subset\mathbb Z^d$ has $N$ points and entries bounded by
$M$, then $H\leq2NM$: a rational line's integer points are integer
multiples of a primitive vector, and a nonzero coordinate bounds the possible
multipliers of any signed sum by $NM$.

## A precise triangular construction

Take independent copies of $\Gamma=\langle B\rangle_{\mathbb Z}$.
Let integral gluing rows be $r_1,\ldots,r_s\in\Gamma^n$. Give each
row a buffer set $P_e$ of size $m_e$, with the sets $P_e$
pairwise disjoint. Assume that on every $v\in P_e$, row $r_e$
has a primitive nonzero anchor $u_{e,v}$, while every later row
$r_f$, $f>e$, vanishes. Earlier rows may overlap these buffers.
Quotient by the rational span of all rows, and denote the image family by
$G$. Put $L_e=\max_{v\in P_e}\lambda_B(u_{e,v})$, using
[primitive width](anchored_phase_gluing.md).

### Saturation and distinctness

Choose one primitive pivot from each buffer set. Integer functionals taking
value one on those pivots give a unitriangular minor of the row matrix.
Thus the rows generate a saturated lattice; the quotient group is free.
In a nonzero rational row combination, its least active row has nonzero
entries on every one of its buffers, since all later rows vanish there.
If every $m_e\geq3$, the combination has at least three nonzero blocks.
Consequently each block embeds, and no new zero, equal, or antipodal labels
occur between blocks.

### Uniform analytic bound

Exactly as in primitive-anchor phase gluing,

$$
\rho(G)\geq\rho(B)-\frac{\pi^2}{2}
                         \max_e\frac{L_e^2}{m_e^2}. \tag{2}
$$

Independently maximize every block polynomial. Correct row constraints in
reverse order, spreading a principal phase $\theta_e\in[-\pi,\pi]$
across its buffers with the separate minimizing functionals
$\ell_{e,v}(u_{e,v})=1$. Later rows are unaffected because they
vanish on these buffers. The disjoint buffer sets mean every polynomial
block moves only once from its independent maximum. Its first-order
variation vanishes, and its quadratic loss is bounded by
$\pi^2L_e^2/(2m_e^2)$ times its coefficient mass. Summing gives (2),
with a maximum rather than a sum over rows.

### Nevertheless the quotient has no chromatic increase

If every $m_e\geq h$, then $\chi(G)=q$. Color each buffer word
using (1) and color all remaining blocks properly. Suppose a nonzero
monochromatic relation had block-sum vector
$x=\sum_e\lambda_e r_e$. On the buffers of its least active row
$e$, its sums are exactly $\lambda_e u_{e,v}$. Equation (1)
forces $\lambda_e=0$, a contradiction. If $x=0$, blockwise
properness already makes the relation trivial. Restriction to an embedded
block gives the matching lower bound $q$.

This proof permits arbitrary mobile labels, not just a finite list of
directions. Its no-increase conclusion requires both finite $T$ and
$m_e\geq h(B,q)$ for every buffer. Analytic smallness alone does not
imply these inequalities, so the theorem does not rule out every cheap
triangular gluing or every iteration with changing sources.

## A full-closure counting criterion without triangularity

For $B\subset\mathbb Z^d$ as above, let
$R\subseteq(\mathbb Q^d)^n$ have dimension $r$, and suppose every
nonzero vector of $R$ has at least $D$ nonzero blocks. The quotient
image family is $q$-colorable whenever

$$
q(2NM+1)^r(1-1/T)^D<1. \tag{3}
$$

Color blocks independently from the fixed $T$-witness family. A coordinate
projection onto $r$ scalar coordinates injects on $R$, so
$|R\cap\Sigma(B)^n|\leq(2NM+1)^r$. Each fixed nonzero vector has
probability at most $(1-1/T)^D$ of belonging to the signed spans of a
fixed color in all blocks. A union bound over these vectors and the colors
proves (3); zero block sums are excluded by blockwise properness.
Again the count covers all induced relations, not just a selected row list.
