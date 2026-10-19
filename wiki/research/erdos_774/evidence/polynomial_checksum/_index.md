---
name: research/erdos_774/evidence/polynomial_checksum
title: Exact mixed relation defeating a polynomial checksum coloring
desc: A bounded six-instance test found eight-column ternary witnesses against one explicit binary checksum palette; the retained witnesses are checked by elementary integer sums and are not an arbitrary-color theorem.
tags: [E0774, computation, certificate, coloring, incomplete]
sources: []
created: 2026-09-19T00:35:00Z
updated: 2026-09-19T00:48:35Z
---

# Exact mixed relation defeating a polynomial checksum coloring

[[research/erdos_774/evidence/_index|..]]

***

## Question and finite range

This tested whether one explicit small palette could color the polynomial line
variant of the [field matching candidate](../../routes/field_tower_lines.md). It
did not search for a counterexample to E0774 or test arbitrary palettes.

Over $\mathbb F_2[t]$, put $V_j=\{$polynomials of degree at most $j\}$.
Stage $m$ has rows $V_m\times V_{2m}$. For every polynomial slope $r$ of
degree $j\le m$, use all cosets of $\{(x,rx):x\in V_j\}$; the slopes zero
and one have $j=0$. Include also cosets of the initial vertical direction
$\{(0,a):a\in\mathbb F_2\}$.

Let $L(t^i)=\mathrm{Catalan}_i$ modulo two, where
$\mathrm{Catalan}_i=\binom{2i}{i}/(i+1)$. Color a slope-$r$ coset with
representative $(u,v)$ by $L(v-ru)$, and a vertical coset by $L(u)$.
These are well-defined on the cosets. Only degrees at most four are needed
in this test; no infinite Hankel or coloring theorem is assumed.

The **entire prescribed range** was $p=2$, $m=0,1,2$, both colors. Each
of the six mixed-integer feasibility instances had a 20-second cap. The
variables were $a_E,b_E\in\{0,1\}$ with $a_E+b_E\le1$,
$\sum(a_E+b_E)\ge1$ and $A(a-b)=0$; the objective was $\sum(a_E+b_E)$.

| Stage | Rows | All columns | Columns per color | Returned result in each color |
|---|---:|---:|---:|---|
| 0 | 4 | 6 | 3 | Solver reported infeasible |
| 1 | 32 | 64 | 32 | Eight-column ternary witness |
| 2 | 256 | 640 | 320 | Eight-column ternary witness |

All six instances finished, the last two in under two seconds each. The
first witnesses already refuted the proposed coloring; no range extension
or repeated search was made. Infeasibility and objective optimality are not
used as mathematical certificates.

## Scripts, inputs and checks

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/polynomial_checksum/main.py
```

The [checker](main.py) reads the four retained
[witnesses](assets/checksum_witnesses.json), one per color at stages one
and two, and verifies with the standard library, exact integer arithmetic
and the shared root `tools` checker that every listed column is a genuine
coset whose support and palette color match the formulas above, that the
eight supports are distinct, that the coefficients are $\pm1$, and that
the signed sum of the indicator columns is exactly zero. It performs no
search and finishes in under a second; a failed clause exits nonzero.

The discovery script is [produce.py](produce.py). It needs NumPy and SciPy,
which the repository does not declare, writes every returned result to the
ignored `output/` folder beside it, and is not evidence by itself. The
original run used Python 3.13.15, NumPy 2.5.3, and SciPy 1.18.1 with
single-threaded BLAS; solver choices need not reproduce the same witnesses.

## A standalone certificate at stage one

Encode a polynomial by its binary coefficient string. A row $(x,y)$ is
numbered $x+4y$, with $0\le x<4$ and $0\le y<8$. The following signed
columns all have color zero:

| Sign | Direction | Representative $(u,v)$ | Row support |
|---:|---|---|---|
| $-$ | vertical | $(3,4)$ | $\{19,23\}$ |
| $+$ | vertical | $(3,6)$ | $\{27,31\}$ |
| $-$ | $0$ | $(0,3)$ | $\{12,13\}$ |
| $+$ | $0$ | $(2,4)$ | $\{18,19\}$ |
| $+$ | $1$ | $(1,2)$ | $\{9,12\}$ |
| $-$ | $1$ | $(2,6)$ | $\{26,31\}$ |
| $-$ | $t$ | $(0,0)$ | $\{0,9,18,27\}$ |
| $+$ | $t+1$ | $(0,0)$ | $\{0,13,23,26\}$ |

Every displayed row occurs once with each sign. Therefore the sum is
exactly zero. At this stage $L(1)=L(t)=1$ and $L(t^2)=0$, which verifies
every claimed color directly. The supports are obtained by the displayed
coset formula, and are distinct. This is a genuine monochromatic ternary
relation, not a modular or rational relation.

The two newest directions and six old columns participate together.
This shows why splitting elementary two-direction bundle templates does
not by itself color the full kernel. It disproves only this particular
checksum coloring; the stage-one configuration does admit another
rationally independent two-coloring, proved below.
No unbounded coloring or negative solution is claimed.

## Analytic strengthening: every binary linear-intercept checksum fails

Let $L:\mathbb F_2[t]\to\mathbb F_2$ be any linear functional. Color a
slope-$r$ column by $L(v-ru)$, and a vertical column by $L(u)$, as above.
A monochromatic ternary relation always occurs at stage zero or one. There
are three cases.

1. If $L(1)=0$, the horizontal and vertical parallel classes inside the
   constant $\mathbb F_2^2$ plane all have color zero. Their difference is
   a four-column trade.
2. Suppose $L(1)=1$ and the two-by-two matrix with rows
   $(L(1),L(t))$ and $(L(t),L(t^2))$ is singular. Put $a=L(t)$, so
   $L(t^2)=a$, and $P=t+a$. Then $L(Px)=0$ for every $x\in V_1$. The
   eight-point group $H_0+H_P$ is partitioned both by four horizontal
   two-point columns and by two four-point $P$-columns. All six columns
   have color zero: their checksums are respectively $L(Px)$ and
   $-uL(P)$, $u\in\mathbb F_2$. The two partitions give a ternary
   relation.
3. Suppose $L(1)=1$ and the same matrix is nonsingular. In each old
   affine $\mathbb F_2^2$ layer, all color-zero initial lines form a
   three-edge star. Its center is the unique point satisfying
   $L(x)=L(y)=0$ in that layer. The two new lines $y=tx$ and
   $y=(t+1)x$ have color zero. They meet the same four old layers, and
   coincide only at the origin. A point on either line is a star center
   only if $L(x)=L(tx)=0$; nonsingularity forces $x=0$ in $V_1$. In
   each of the other three layers, the two new points are distinct
   noncenter vertices. The difference of their point indicators equals
   the difference of the two star edges joining them to the center. These
   six old edges and the two new lines give an eight-column monochromatic
   ternary relation. Edges from different layers are distinct, so no
   coefficient collision is hidden.

For the common-layer assertion in case 3, write $x=a+bt$ and
$y=c+et+ft^2$. The old layer is indexed by $(b,e,f)$. On $y=tx$, $f=b$
and $e=a$; on $y=(t+1)x$, $f=b$ and $e=a+b$. Thus both lines meet exactly
the four layers with $f=b$, once each. This verifies the only geometric
coupling used in that case.

This proves failure of the whole linear-intercept checksum class without
any further search or infinite Hankel theorem. It remains a restricted
palette theorem, not a proof about arbitrary colorings. The author and a
separate reviewer checked the algebra.

## The same whole stage actually has a proper two-coloring

Direction-dependent offsets change the conclusion. At $p=2$, $m=1$ use
$L(a+bt+ct^2)=a+b$, and put

$$
h_\infty=h_0=h_1=h_t=0,\qquad h_{t+1}=1.
$$

Color a slope-$r$ coset by $L(v-ru)+h_r$, and a vertical coset by $L(u)$.
**Each of the two resulting 32-column classes is rationally independent.**
This is an analytic certificate, obtained after the finite experiment;
no further solver run is needed.

Write a row as $x=A+Bt$ and $y=C+Et+Ft^2$. The eight initial planes are
indexed by $(B,E,F)$. Their color-zero old columns form the star centered
at $(A,C)=(B,E)$; their color-one old columns form the triangle on the
other three points. Both old triples are independent in each plane.

Every newest column has exactly one star center, and for each color
each of the eight centers occurs in exactly one newest column of that
color. Explicitly, for $r=t+a$, $a\in\mathbb F_2$, color $\gamma$, write
its intercept as $(\gamma+a+u)+ut+vt^2$. Its center layer is

$$
(B,E,F)=(\gamma+a,\ (1+a)(\gamma+a)+u,\ \gamma+a+v).
$$

This gives a bijection from the eight newest columns in either color
to the center layers.

For color one, the old triangle columns span all three noncenter
coordinates in each plane. Modulo those spans, newest columns project
to the eight different center coordinate vectors. The whole class is
therefore independent; its determinant has absolute value $2^8$, the
product of the eight old triangle determinants.

For color zero, quotient each old star span using the linear functional
that is plus one at the center and minus one at each of its three
leaves. Let $T=\mathrm{span}_{\mathbb F_2}\{(0,1,0),(1,0,1)\}$ in the
group of center layers. A newest column whose center is $h$ meets
precisely the four layers $h+T$, and its other three points are leaves.
Its projected column is consequently $2e_h-1_{h+T}$. The quotient matrix
splits into two blocks $2I_4-J_4$. Each has eigenvalues $-2,2,2,2$, hence
is invertible. Together with the independent old stars this proves
independence of the entire color-zero class. Old-star elimination is
unimodular, so this class also has determinant of absolute value
$16^2=2^8$.

The whole configuration is not dissociated, because its initial plane
already contains a difference of two parallel classes. Thus the exact
stage-one dissociated coloring number is **two**. The preceding
four/six/eight-column theorem excludes common-functional, zero-offset
checksums only; it does not exclude affine offset palettes or arbitrary
two-colorings. A separate reviewer checked this distinction.

## The proposed stage-two quotient certificate fails

A possible continuation is to use the new columns as binary digits modulo
each color's old integer lattice. In the proposed stage-two extension, the
old rows split into eight translated stage-one blocks; the established
offset pattern on each is equivalent by translation to the pattern above.
Thus each old color lattice has index $(2^8)^8=2^{64}$, and each color
adds 64 newest columns, of size eight.

That particular certificate is impossible. Every old and new column has
even cardinality. Total row-coordinate sum modulo two is consequently a
nonzero character on either old quotient of order $2^{64}$, and it
vanishes on all new column classes. Those classes lie in a subgroup of
size $2^{63}$, so their $2^{64}$ binary subset sums cannot all be
distinct. This also excludes the stronger proposed full-mod-two-rank test
for the triangle color. No stage-two computation was run for the offset
pattern.

This is only a failure of the quotient-injectivity certificate. A
quotient collision gives an integer old preimage, not necessarily one
whose coefficients are zero or plus/minus one. Actual stage-two
dissociation and an all-depth coloring theorem remain unproved.
