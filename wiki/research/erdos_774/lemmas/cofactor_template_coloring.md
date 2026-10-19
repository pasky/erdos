---
name: research/erdos_774/lemmas/cofactor_template_coloring
title: Seven colors avoid all ordinary cofactor templates on a dense-base odd torus
desc: A quadratic matching statistic gives a uniform seven-color avoidance of all translated rank-correct single-cofactor templates for bases with three universal rows; even moduli need only two colors. This is not a coloring of all ternary relations.
tags: [E0774, proved, obstruction, coloring, incomplete]
sources: []
created: 2026-09-18T20:45:43Z
updated: 2026-09-18T20:53:07Z
---


# Seven colors avoid all ordinary cofactor templates on a dense-base odd torus

***

## Scope

This page gives an obstruction to the proposed cofactor-template shortcut to the
[incidence-cover coloring obligation](../routes/incidence_cover_extraction.md).
It concerns the generic symbolic matrix and its torus cover from
[generic abelian voltages](../routes/generic_voltage_coloring.md).

For the dense bases below, the hypergraph of **all translated, rank-correct
single-cofactor supports of the original symbolic matrix** has chromatic
number at most seven for every odd modulus, and at most two for every even
modulus. The base column-to-row ratio is unbounded.

This is **not** a coloring avoiding every ternary relation of the cover.
It does not handle arbitrary polynomial combinations or multiples of the
cofactor vectors, nor the cofactors of a color-coset-split matrix. The bases
used here are not the axis-line bases. Thus this is not an upper bound for
the cover invariant $\Gamma(A)$, and does not resolve the required
problem.

## 1. The exact family of cofactor templates

Let $A\in\{0,1\}^{X\times V}$ have three distinct **universal rows**:
each of these rows is incident to every column. Fix total orders on the
rows and columns. Let
$$
 E=\{(x,v):A_{xv}=1\},\qquad
 M_{xv}=\begin{cases}X_{xv},&(x,v)\in E,\\0,&\text{otherwise}.
 \end{cases}
$$
All incidence variables are independent. Work initially over the Laurent
domain $\mathbb Z[X_e^{\pm1}:e\in E]$.

A rank-correct single-cofactor witness consists of column and row sets
$C,J$ with
$$
 |C|=k+1,\qquad |J|=k,\qquad
 \operatorname{rank}_{\mathbb Q(X)}M_{X,C}=k,
$$
such that $M_{J,C}$ has rank $k$. Its alternating maximal-minor
vector, extended by zero outside $C$, is a nonzero kernel vector of
the full matrix. Each nonzero monomial corresponds to a matching of
$J$ onto $C\setminus\{v\}$, in coordinate $v$.

The generic matching-rank proof is elementary: different determinant
matchings use different sets of independent incidence variables, so their
monomials do not cancel. Hence symbolic rank equals maximum matching size.
It also shows that every cofactor coefficient is $0,\pm1$.

For $N\ge2$, reduce the voltage sheets modulo $N$, obtaining
$G_N=(\mathbb Z/N\mathbb Z)^E$. A translate by $T\in G_N$
of such a witness has support vertices
$$
 (v,T+\mathbf1_F),
 \tag{1}
$$
where $F$ runs through the relevant matching incidence sets. Distinct
matching indicators remain distinct modulo $N$, so these are the
supports of nonzero flat relations in the finite cover.

## 2. Every nonzero coordinate contains six permutation points

Every universal row belongs to $J$. Indeed, choose $v\in C$ for
which the cofactor is nonzero and a matching of $J$ onto
$C\setminus\{v\}$. If a universal row $u$ were outside $J$,
adjoining the incidence $(u,v)$ would produce a matching covering all
$k+1$ columns of $C$. This contradicts the rank assumption.
In particular $k\ge3$.

Fix a nonzero cofactor coordinate $v$, and fix one of its determinant
matchings. Keep all its edges outside the three universal rows fixed.
Exactly three distinct matched columns remain. These columns are adjacent
to all three universal rows, so all six bijections between these rows and
columns extend the fixed matching.

Consequently the support in this one coordinate contains
$$
 (v,T'+\mathbf1_{F_\sigma}),\qquad \sigma\in S_3,
 \tag{2}
$$
where $T'$ incorporates the original translate and the fixed matching
edges, and $F_\sigma$ is the three-edge permutation matching in this
$K_{3,3}$. This applies to every nonzero coordinate, not just to
minimal-Hall witnesses. Minimal-Hall cofactor templates are included as
a special case.

## 3. A quadratic six-point identity

Define the quadratic polynomial, with values modulo $N$,
$$
 Q(g)=\sum_{\substack{x<y,\ v>w\\(x,v),(y,w)\in E}}
                  g_{xv}g_{yw}.
 \tag{3}
$$
Order the three selected rows and the three selected columns increasingly.
For $\sigma\in S_3$, let $\epsilon_\sigma$ be its permutation
sign. Then
$$
 \sum_{\sigma\in S_3}\epsilon_\sigma
            Q(T'+\mathbf1_{F_\sigma})=-1\pmod N.
 \tag{4}
$$
To prove (4), expand the quadratic. Its constant term cancels because
there are three even and three odd permutations. Every linear incidence
term cancels because each edge of the $K_{3,3}$ occurs in two of its
perfect matchings, one of each sign. This also cancels all contributions
from the fixed complement and the translate.

On a three-edge permutation indicator, $Q$ is the inversion count.
The six inversion counts, grouped with their signs, give
$$
 0-1-1+2+2-3=-1.
 \tag{5}
$$
This proves the identity over the integers before reduction and hence
over every modulus.

## 4. Seven colors for every odd modulus

Let $N\ge3$ be odd and put
$$
 d=(N-1)/2,\qquad L=\lceil d/3\rceil
                  =\lceil(N-1)/6\rceil.
$$
For $g\in G_N$, let $z(g)\in\{0,\ldots,N-1\}$ be the
canonical representative of $dQ(g)$. Color every column $(v,g)$
by
$$
 c(v,g)=\left\lfloor\frac{z(g)}L\right\rfloor.
 \tag{6}
$$
The number of colors is $\lceil N/L\rceil\le7$. Indeed, if
$d=3a$, then $L=a$ and $N=6a+1\le7a$; otherwise
$L=a+1$ and $N\le6a+5\le7(a+1)$. The first case has
$a\ge1$. Explicitly $N=3,5,7$ use $3,5,7$ colors,
respectively. Also
$$
 3(L-1)<d.
 \tag{7}
$$

Suppose the six vertices in (2) had one color. Their six canonical
$z$-values would lie in one integer interval of length at most $L$.
Since three signs are positive and three negative,
$$
 \left|\sum_{\sigma\in S_3}\epsilon_\sigma
             z(T'+\mathbf1_{F_\sigma})\right|
 \le3(L-1)<d.
$$
But (4) says that this integer is congruent to $-d$ modulo
$N=2d+1$. Every integer in that residue class has absolute value
at least $d$, a contradiction.

Thus every six-point set (2) is split. By Section 2, no translated
rank-correct single-cofactor support is monochromatic.

## 5. Two colors for even moduli

If $N\ge2$ is even, reduction modulo two is well defined on
$G_N$. Color $(v,g)$ by $Q(g)\bmod2$. If all six points
in (2) had one color, their signed sum in (4) would be zero modulo two.
Equation (4) makes that sum one instead. Hence this two-coloring avoids
all the same cofactor supports.

## 6. Unbounded base density and the exact negative conclusion

For $s\ge1$, take $r=s+3$ rows and one column for each
$b\in\{0,1\}^s$, with column vector
$$
 (1,1,1,b_1,\ldots,b_s)^\mathsf T.
$$
These are $n=2^s$ distinct nonzero columns, with three universal rows,
and
$$
 \frac nr=\frac{2^s}{s+3}\longrightarrow\infty.
$$
Nevertheless the hypergraph of translated ordinary single-cofactor
supports on every generic voltage torus has chromatic number at most
seven (at most two for even moduli). Already $s=6$ gives
$n/r=64/9>7$.

Therefore a universal lower bound by $n/r$ for **this cofactor-support
hypergraph** is false, even when arbitrary odd moduli are allowed.
The coloring may leave other ternary relation supports monochromatic;
no upper bound for the full dissociated chromatic number is proved.
The construction does not apply to the axis-line bases merely from
their density: it uses three universal rows essentially.

No computation or external theorem is used in this proof.
