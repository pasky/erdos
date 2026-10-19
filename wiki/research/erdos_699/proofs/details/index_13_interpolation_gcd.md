---
name: research/erdos_699/proofs/details/index_13_interpolation_gcd
title: "Erdős 699: the index-13 interpolation system has no fixed curve"
desc: "An exact modular rank and polynomial gcd certificate proves that the complete degree-106 fat-point system has a finite, effectively bounded common zero set."
created: 2026-09-22T03:52:03Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: the index-13 interpolation system has no fixed curve

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/proofs/details/index_13_interpolation|The initial interpolation construction]]

***

The complete polynomial space defined below has **constant common gcd**.
Its common zero set is therefore finite and has an explicit coordinate
bound. This supplies the nonvanishing step for the improved, monotone
index-13 certificate. The calculation concerns one fixed interpolation
system; it does not enumerate binomial rows or columns.

## The improved system

Put


$$
h=(57,54,45,39,32,24,13,3,0,0,0,0,0),
\qquad
m=(114,111,111,103,99,99,89,78,70,63,57,51,46).
$$


For each integer grid point $x,y\ge0$, $x+y\le12$, prescribe multiplicity


$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.
$$


Let $V$ be the **complete** rational vector space of polynomials of total
degree at most $106$ with these prescribed multiplicities. Its symmetric
subspace consists of the polynomials satisfying $G(X,Y)=G(Y,X)$.

The exact totals are


$$
\sum R_{xy}=844,\qquad
\sum R_{xy}^2=10738,\qquad
\sum\binom{R_{xy}+1}{2}=5791.
$$


These 5791 jet equations need not be independent. The proof below uses
the rank of the smaller symmetric system, and makes no independence
assumption about the full system.

For $G\in V$, set


$$
H(X,Y)=\prod_{a=0}^{12}((X-a)(Y-a))^{h_a},\qquad F=HG.
$$


Then $\deg H=534$, $\deg F\le640$, and the multiplicity of $F$ at every
Kummer point on row $x+y=t$ is at least $m_t$. Also $H(j,c)>0$ throughout
the physical range $13<j\le c$. Thus common physical zeros introduced by
this construction are precisely those of $V$.

## Exact modular certificate

Use the prime $p=65521$. The symmetric monomial basis consists of


$$
X^aY^b+X^bY^a\quad(a<b),\qquad X^aY^a\quad(a=b),
\qquad a+b\le106,
$$


ordered by increasing total degree and then increasing $a$. There are
2916 basis elements.

At a point $x<y$, impose every Hasse Taylor coefficient of order less
than $R_{xy}$. At a diagonal point $x=y$, retain only coefficients indexed
by $(u,v)$ with $u\le v$; symmetry identifies the omitted coefficients
with these. The conditions at $x>y$ are likewise duplicates. This gives
2911 integer equations and an integer matrix $A$.

The [exact checker](../../computations/erdos_699_index_13_interpolation_gcd.py)
and its [retained certificate](../../computations/erdos_699_index_13_interpolation_gcd.json)
verify:

| Quantity | Exact value |
| --- | --- |
| Modulus | $65521$, prime |
| Matrix shape | $2911\times2916$ |
| Rank modulo $65521$ | $2911$ |
| Symmetric nullity | $5$ |
| Degrees of the two retained kernel sections | $106,106$ |
| Their gcd in $\mathbb F_{65521}[X,Y]$ | $1$ |

The JSON stores the coefficients of the two sections in the stated
symmetric basis. Verification reconstructs the jet matrix, computes its
rank exactly, checks both matrix products are zero, and computes the full
bivariate polynomial gcd. Computing the gcd over
$\mathbb F_p(X)[Y]$ alone would not suffice, because it could discard
factors depending only on $X$.

To reproduce, with the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
installed in the repository's `.venv/`:

```sh
uv run --no-sync --with numpy --with python-flint python wiki/research/erdos_699/computations/erdos_699_index_13_interpolation_gcd.py
```

The checker requires NumPy and `python-flint`, neither declared by the
repository, so the command supplies both. Its
`--regenerate` option
recomputes the retained sections by exact nullspace calculation.

## Why this proves the rational statement

Two modular polynomials with gcd $1$ do not, by themselves, prove that
arbitrary rational lifts are coprime. A rational factor could reduce to a
nonzero constant. The complete interpolation space removes that issue.

First put $R=\mathbb Z_{(p)}$. Full row rank of $A$ modulo $p$ supplies a
maximal minor that is a unit in $R$. Assigning arbitrary lifts to the free
coefficients and solving for the pivot coefficients shows that


$$
\ker_R A\longrightarrow\ker_{\mathbb F_p}\overline A
$$


is surjective. Consequently the two retained modular sections lift to
symmetric polynomials $G_1,G_2\in V\cap R[X,Y]$.

Suppose an irreducible polynomial $f\in\mathbb Q[X,Y]$ divided every
element of the complete space $V$. Then $f$ would vanish at a prescribed
grid point with positive multiplicity. Otherwise $f$ is a unit in the
local ring at every such point. Dividing a section by $f$ then preserves
all prescribed multiplicities and decreases its degree, so the quotient
is still in $V$. Repeating until the factor is removed contradicts its
being common to $V$.

Normalize $f$ to a primitive integer polynomial. Its reduction modulo
$p$ is nonzero, and its zero at an integer support point ensures that
this reduction is nonconstant. Gauss's lemma over $R$ shows that
$G_i/f\in R[X,Y]$. Reduction therefore makes the nonconstant polynomial
$\overline f$ a common divisor of the two retained modular sections,
contrary to their gcd $1$.

Thus $\gcd(V)=1$. The argument uses the completeness of $V$ in its
division step, although the modular sections come from its symmetric
subspace. It does not assert that the particular rational lifts
$G_1,G_2$ are coprime.

## An explicit bound for the common zero set

No rational kernel or rational resultant needs to be computed to prove
effectivity. Put


$$
d=106,\quad N=\binom{108}{2}=5778,\quad
C=N!\,13^{dN},\quad B=NdC,
$$


and


$$
\mathcal R=(2d)!\bigl((d+1)B\bigr)^{2d}.
$$


Every common zero of $V$ satisfies


$$
\boxed{|X|,|Y|\le1+\mathcal R.}
$$


Indeed, every entry of the full integer Hasse-jet matrix has magnitude
at most $13^d$: for a monomial $X^aY^b$, its jet coefficient is
$\binom au x^{a-u}\binom bv y^{b-v}$, bounded by
$(1+x)^a(1+y)^b\le13^d$. Choose a maximal nonsingular minor of this
matrix. Cofactor kernel vectors give an integer rational basis
$F_1,\ldots,F_k$ of $V$ whose individual coefficients have magnitude at
most $C$. This follows directly by expanding determinants; the rank is
less than $N$.

If a basis element is a nonzero constant, the common zero set is empty.
Otherwise choose $F_1\ne0$. It has at most $d$ distinct irreducible
factors. For any one of them, combinations


$$
\sum_{i=1}^k a_iF_i,\qquad (a_1,\ldots,a_k)\in\{0,\ldots,d\}^k,
$$


that are divisible by the factor occupy at most $(d+1)^{k-1}$ choices:
at least one $F_i$ is not divisible by it, and fixing the other
coefficients allows at most one value of that $a_i$. Because
$d(d+1)^{k-1}<(d+1)^k$, some combination $F_2$ is coprime to $F_1$.
Its coefficient height is at most $B$, as is that of $F_1$.

The resultants eliminating $X$ and eliminating $Y$ are nonzero. Expanding
their Sylvester determinants bounds their coefficient norms by
$\mathcal R$: their sizes are at most $2d$, and each entry has coefficient
norm at most $(d+1)B$. Cauchy's root bound gives the displayed coordinate
bound. If both polynomials omit one variable, their coprimality already
makes their common zero set empty.

In particular, every physical common zero satisfies the explicit bound


$$
n=X+Y\le2(1+\mathcal R)<10^{265000000}.
$$


For the final loose decimal inequality, use $N<10^4$, $13<10^2$,
$Nd<10^6$, $d+1<10^3$, and $2d<10^3$. These give
$C<10^{1248048}$ and $\mathcal R<10^{264588720}$.
This is a bound for the common zero set. The complete arithmetic row
bound must also include the BFT thresholds and the bounds obtained from
nonzero polynomial evaluations.
