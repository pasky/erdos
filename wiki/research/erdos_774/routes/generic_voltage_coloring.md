---
name: research/erdos_774/routes/generic_voltage_coloring
title: Generic abelian voltages exclude affine colorings, not arbitrary colorings
desc: Independent incidence variables give flat cofactor relations at Hall deficiency and one finite voltage cover excludes every affine homomorphic q-coloring when the base has more than q times as many columns as rows; arbitrary coloring remains open.
tags: [E0774, proved, construction, obstruction, incomplete]
sources: []
created: 2026-09-18T20:06:47Z
updated: 2026-09-18T21:59:00Z
---


# Generic abelian voltages exclude affine colorings, not arbitrary colorings

***

## Standing and exact scope

The [incidence-cover extraction theorem](incidence_cover_extraction.md)
applies to all finite axis-line incidence covers. This page proves a
restricted coloring obstruction for particularly explicit abelian covers.
It does **not** prove an obstruction to arbitrary finite colorings, and
therefore does not establish unbounded dissociated chromatic number.

Let $A\in\{0,1\}^{X\times V}$, put $r=|X|$, $n=|V|$, and let
$E=\{(x,v):A_{xv}=1\}$. All algebraic statements below concern indexed
columns. For their interpretation as dissociation of a set of vectors,
assume the base columns are distinct and nonzero; then all incidence
covers also have distinct nonzero columns.

Write $G=\mathbb Z^E$, with standard basis $e_{xv}$. The generic
abelian voltage cover has column labels $(v,g)$, row labels $(x,a)$,
and incidence
$$
 (v,g)\sim(x,g+e_{xv})\qquad ((x,v)\in E).
\tag{1}
$$
Only finite-support relations in this infinite cover will be used. They
can subsequently be reduced to finite covers.

The proved finite conclusion is the following.

**Restricted-coloring theorem.** Suppose $n>qr$, where $q\ge1$.
Set
$$
 N=2\operatorname{lcm}(1,2,\ldots,q).
\tag{2}
$$
Take the predetermined finite cover with sheets
$G_N=(\mathbb Z/N\mathbb Z)^E$ and the unit voltages from (1).
Every coloring of the form
$$
 c(v,g)=\phi(g)+c_v\in H,
\tag{3}
$$
where $H$ is a finite abelian group of order at most $q$,
$\phi:G_N\to H$ is a homomorphism, and $c_v\in H$ are arbitrary,
has a nonzero monochromatic ternary relation. Neither surjectivity of
$\phi$ nor equal offsets $c_v$ is required.

This is one cover working for all the displayed choices, not a cover
selected after seeing $\phi$ or the offsets. Its scope is nevertheless
restricted: a general coloring need not have the form (3).

## 1. Generic matching rank and flat cofactors

Let
$$
 R=\mathbb Z[X_e^{\pm1}:e\in E],\qquad
 M_{xv}=\begin{cases}X_{xv},&(x,v)\in E,\\0,&\text{otherwise}.
 \end{cases}
\tag{4}
$$
A vector of Laurent polynomials
$f_v=\sum_g a_{v,g}X^g$ satisfies $Mf=0$ exactly when the
coefficients $a_{v,g}$ give a finite-support integer relation in (1).

For any selected row and column sets of equal size, different nonzero
determinant terms use different sets of incidence variables. Indeed a
matching is recovered from the set of incidences it uses. Consequently:

* Every such nonzero determinant has all its coefficients in
  $\{-1,1\}$, with no repeated monomials.
* The rank of $M$ over $\mathbb Q(X_e:e\in E)$ is exactly the
  maximum matching size of the base incidence graph.

The same statements hold after restricting the base column set to
$S\subseteq V$. Thus the entire fiber types in $S$ have a nonzero
finite-support kernel if and only if their incidence graph has a Hall
deficiency, namely some $T\subseteq S$ satisfies
$$
 |N(T)|<|T|.
\tag{5}
$$
This is a structural-matching statement, not a statement about the
ordinary rational rank of the numerical matrix $A$.

Moreover, whenever this kernel is nonzero, it contains a ternary vector.
For rank zero use the empty-determinant convention, giving coefficient
one on a zero column. Otherwise, choose $k$ independent columns and one further
column in their span. On these $k+1$ columns choose $k$ rows with a
nonzero $k$-minor. The alternating cofactor vector of this
$k$-by-$(k+1)$ matrix is nonzero and annihilates the selected rows.
Those rows span the row space on the selected columns over the fraction
field, so it annihilates every row. Each polynomial coordinate is a
determinant from (4), hence has coefficients $0,\pm1$. Extending by
zero gives the required ternary relation.

The argument concerns complete fiber types. It cannot be applied
unchanged to an arbitrary subset of translated column copies: the same
base incidence variable can then appear in several selected columns.
Section 4 gives an explicit repeated-monomial obstruction.

## 2. One coset per type: the affine coloring argument

First work in $G=\mathbb Z^E$. Let $H$ be a finite abelian group,
let $\phi:G\to H$ be a homomorphism, and color by (3).
Put $I=\operatorname{im}\phi$, $s=|I|$, and
$K=\ker\phi$, so $[G:K]=s$.

For $h\in H$, let
$$
 V_h=\{v\in V:h-c_v\in I\}.
$$
Every column type belongs to exactly $s$ of these sets, and therefore
$$
 \sum_{h\in H}|V_h|=ns.
\tag{6}
$$
If $n>|H|r$, some $h$ satisfies $|V_h|>rs$. Fix that color.
For each $v\in V_h$, choose $b_v\in G$ with
$\phi(b_v)=h-c_v$. The columns of this type having color $h$ are
exactly the sheets in $b_v+K$.

Choose a representative $a_j\in G$ for each $j\in I$. Express
the color-$h$ restriction as a matrix over $\mathbb Z[K]$:

* Column types are the elements of $V_h$, with sheets measured from
  their representatives $b_v$.
* Row types are $(x,j)\in X\times I$, with sheets measured from
  $a_j$.
* The incidence $(x,v)$ occurs in the unique row type with
  $j=\phi(b_v+e_{xv})$, and its entry is the monomial with exponent
  $b_v+e_{xv}-a_j\in K$.

Call this matrix $B$. It has $|V_h|>rs$ columns and $rs$ rows,
so it has a nonzero kernel over the fraction field of $\mathbb Z[K]$.

Crucially, its nonzero determinant terms still have distinct exponents.
For fixed selected row and column sets, a matching term has exponent
$$
 \sum_{v\text{ selected}}b_v
 -\sum_{(x,j)\text{ selected}}a_j
 +\sum_{(x,v)\text{ used}}e_{xv}.
\tag{7}
$$
The first two sums do not depend on the matching. Every base column
type occurs at most once, so the last sum is the indicator of a set of
distinct base incidences. Independence of the standard basis implies
that two matchings give the same exponent only if they are identical.

The cofactor construction of Section 1 now supplies a nonzero ternary
kernel of $B$. All its column copies have color $h$, giving a
monochromatic relation in (1). In particular, this works whenever
$n>qr$ and $|H|\le q$.

For surjective $\phi$, every color uses exactly one coset per base
column type, and $B$ has $n$ columns and $|H|r$ rows. The
averaging in (6) is what permits the non-surjective case.

## 3. One predetermined finite cover

### 3.1 Finite-pattern reduction

For fixed $A,q$, there are finitely many finite abelian groups of
order at most $q$, up to isomorphism. For any one of them there are
only finitely many homomorphisms $G\to H$, since the images of the
finitely many generators determine the homomorphism, and only finitely
many tuples of offsets $(c_v)$.

Choose one finite witness from Section 2 for each such pattern. If
$N$ is divisible by every relevant group exponent, all the patterns
factor through $G_N$. Taking $N$ additionally large enough that
none of these finitely many witness supports collide gives one finite
cover defeating every pattern. This argument alone establishes a
finite-to-finite consequence without choosing a cover after its coloring.

### 3.2 A sharper common-cube support bound

In fact no large support bound or enumeration is needed. Let $C$ be
the $k+1$ column types and $J$ the $k$ row types used in a
cofactor witness for $B$. Define
$$
 T=\sum_{v\in C}b_v-\sum_{(x,j)\in J}a_j\in G.
\tag{8}
$$
A monomial in the cofactor coordinate for $v$ has exponent, relative
to that column's origin $b_v$,
$$
 \sum_{w\in C\setminus\{v\}}b_w
 -\sum_{(x,j)\in J}a_j +\sum_{e\in F}e,
$$
where $F$ is the incidence set of one matching. Its actual sheet is
therefore
$$
 g=T+\mathbf 1_F\in T+\{0,1\}^{E}.
\tag{9}
$$
Here $|F|=k$, and the same $T$ works for every coordinate and
every monomial of this witness.

Consequently reduction modulo **any** $N\ge2$ preserves distinct
selected sheets within each column type. The integer relation remains
valid under the row-coordinate quotient, and its nonzero coefficients
remain $\pm1$. Possible identifications among rows do not damage an
already valid relation. Distinct nonzero base columns ensure that the
surviving distinct column labels are also distinct actual vectors.

Now take $N$ from (2). Every homomorphism $G\to H$, for
$|H|\le q$, factors through $G_N$, because the exponent of $H$
divides $|H|$ and hence divides $N$. Conversely a homomorphism
$G_N\to H$ lifts to one on $G$. Apply Section 2 to this lift and
reduce its witness using (9). This proves the restricted-coloring
theorem stated above.

This proof deliberately takes ranks over the infinite Laurent domain
before reduction. It does not assume that a finite-group ring is an
integral domain.

For the axis-line bases with $d_i=i+2$, one has
$n/r=\sum_{i\le t}1/(i+2)$. Thus, for every fixed $q$, a large
enough base yields a finite covered configuration of uniform extraction
quality for which no affine coloring of the form (3) with at most
$q$ colors is dissociated. The adjective **affine** cannot be removed
by the present argument.

### 3.3 The modulus need not contain the palette group exponent

For a coloring already defined on G_N, the restricted-coloring theorem
holds for **every N>=2**, under the same n>qr hypothesis. Lift its actual
homomorphism G_N -> H to G, apply Section 2, and reduce the resulting
translated-cube witness. This procedure preserves the given actual color
because the lifted homomorphism already factors through G_N. Divisibility
of N by all possible group exponents was only needed to realize all
infinite-group homomorphism patterns simultaneously on one finite group;
it is not needed to exclude all affine colorings available on a chosen
finite cover. In particular, odd and prime moduli are permitted.

There is a different limited result for nonlinear periodic formulas.
Fix d>=1, assume N>=2 and N=1 modulo d, and let

$$
c(v,g)=f_v(\operatorname{rep}_N(g)\bmod d),
\qquad f_v:(\mathbb Z/d\mathbb Z)^E\longrightarrow[q],
\tag{9a}
$$

where rep_N takes coordinate representatives in {0,...,N-1}. If n>qr,
some set of more than r base columns has one common color f_v(0).
Apply the generic cofactor construction to that set. Its sheets are
zero-one incidence vectors. Translate them all by
T=(N-1,...,N-1). After reduction modulo N, every coordinate is either
0 or N-1, and is consequently zero modulo d. Every selected column has
that same actual color. Distinct sheets survive because N>=2, proving
a nonzero monochromatic ternary relation.

For every prescribed finite bound D, one can choose N congruent to one
modulo lcm(1,...,D), and the same cover defeats all formulas (9a) with
d<=D. This does not cover arbitrary functions on G_N: such functions
need not have a small canonical period d. It does show why a parity
formula on an even-modulus cover cannot silently be transferred to an
odd-modulus cover.

## 4. Exact obstruction: a determinant-two minor in the generic cover

Distinct-monomial flatness for the base symbolic matrix does not imply
that its expanded infinite cover is totally unimodular. A small exact
witness already occurs for the distinct nonzero base columns
$$
 A=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix},
\tag{10}
$$
with row types $r_0,r_1,r_2$ and column types $c_0,c_1,c_2$.
Order the seven incidences as
$$
 (r_0,c_0),(r_0,c_1),(r_0,c_2),(r_1,c_0),
 (r_1,c_1),(r_2,c_0),(r_2,c_2),
\tag{11}
$$
and write their unit voltages as $e_1,\ldots,e_7$.

In the base incidence graph take the three theta paths
$$
 P_1=r_0c_0,\qquad
 P_2=r_0c_1r_1c_0,\qquad
 P_3=r_0c_2r_2c_0.
$$
The walk
$$
 P_1P_2^{-1}P_3P_1^{-1}P_2P_3^{-1}
\tag{12}
$$
uses each incidence once in each orientation, so its lift from row
$(r_0,0)$ closes. Its consecutive row and column vertices are the
following; a row sheet equals the adjacent column sheet plus its
incidence voltage, as in (1).

| $i$ | Row vertex $R_i$ | Column vertex $C_i$ |
| --- | --- | --- |
| 1 | $(r_0,0)$ | $(c_0,-e_1)$ |
| 2 | $(r_1,-e_1+e_4)$ | $(c_1,-e_1+e_4-e_5)$ |
| 3 | $(r_0,-e_1+e_2+e_4-e_5)$ | $(c_2,-e_1+e_2-e_3+e_4-e_5)$ |
| 4 | $(r_2,-e_1+e_2-e_3+e_4-e_5+e_7)$ | $(c_0,-e_1+e_2-e_3+e_4-e_5-e_6+e_7)$ |
| 5 | $(r_0,e_2-e_3+e_4-e_5-e_6+e_7)$ | $(c_1,-e_3+e_4-e_5-e_6+e_7)$ |
| 6 | $(r_1,-e_3+e_4-e_6+e_7)$ | $(c_0,-e_3-e_6+e_7)$ |
| 7 | $(r_2,-e_3+e_7)$ | $(c_2,-e_3)$ |

The cycle order is
$R_1,C_1,R_2,C_2,\ldots,R_7,C_7,R_1$.
Inspection of (11) and the sheets in the table shows that these fourteen
vertices are distinct and that there are no extra incidences between
the seven listed rows and the seven listed columns. Their submatrix is
$I+P$, with $P$ a cyclic permutation matrix of order seven, so
$$
 \det(I+P)=2.
\tag{13}
$$
Equivalently, its two perfect matchings have equal determinant sign.
If entries are additionally decorated by their original incidence
variables, each matching uses every variable in (11) once, and its
determinant is $2X_1\cdots X_7$.

**Bounded check performed.** The calculation had one prescribed input:
the seven incidences (11), the fourteen steps (12), and the standard
basis voltages. It accumulated the fourteen lifted vertices, checked
closure and distinctness, formed the selected $7$-by-$7$ matrix,
checked all selected row and column degrees equal two, and evaluated
the determinant by its $7!=5040$ permutation terms. The outputs were
fourteen distinct vertices, the claimed degree sequence, and determinant
$2$. No family of examples or unbounded search was run.

This proves non-total-unimodularity and identifies the repeated-variable
failure in a tempting extension of Section 1. It does **not** itself
exhibit a nonflat circuit among the full lifted columns: those columns
also have incidences outside the seven selected rows.

## 5. Homothetic recurrence does not preserve the voltage equations

If $M(X)p(X)=0$, substitution supplies
$M(X^k)p(X^k)=0$, not generally $M(X)p(X^k)=0$. Even
$$
 M=(X,Y),\qquad p=(Y,-X)
$$
gives
$$
 M(X,Y)p(X^k,Y^k)=XY^k-YX^k\ne0\qquad(k>1).
\tag{14}
$$
Thus a monochromatic homothetic copy of a cofactor support is not
automatically a relation in the fixed unit-voltage cover.

For a base incidence graph containing a cycle, this mismatch cannot be
removed by row and column monomial gauges. If such gauges identified
$M(X^k)$ with $M(X)$, their monomials would satisfy
$$
 X_{xv}^{k-1}=u_xv_v
\tag{15}
$$
on every incidence. Multiplying (15) with alternating exponents around
a simple base cycle cancels all row and column gauges. The remaining
incidence monomial is nontrivial, since its variables are independent
and $k-1\ne0$, a contradiction.

Multiplying a kernel vector by a Laurent polynomial does preserve the
kernel, but it need not preserve flat coefficients or monochromatic
support. Likewise, a fixed translate of a prescribed support is not a
Ramsey pattern merely because arbitrary homothetic copies are available:
already an alternating coloring of $\mathbb Z$ avoids every translate
of $\{0,1\}$. No passage from these recurrence operations to an
arbitrary-color theorem has been proved here.

## 6. Remaining obligation

The generic determinant argument handles complete fiber types and, after
coset splitting, the affine homomorphic colorings (3). For a general
periodic coloring with a period group larger than its palette, a single
color may select multiple cosets of the same base column type. Reused
incidence variables then allow the collisions of Section 4, so the
cofactor coefficients are no longer proved flat. Arbitrary nonperiodic
colorings present at least the same gap.

The open requirement remains a predetermined finite incidence cover
that defeats **every** coloring with a given finite palette. Neither the
matching-rank theorem, its finite affine-color consequence, nor the
bounded determinant calculation establishes that requirement.

The continuation supplies an exact limitation even when odd moduli are allowed.
[Seven-color cofactor avoidance](../lemmas/cofactor_template_coloring.md)
constructs, for distinct-column bases with three universal rows and unbounded
n/r, colorings splitting **all translated rank-correct ordinary single-cofactor
supports**: seven colors suffice for odd moduli, two for even moduli. This does
not color all flat kernel vectors, their polynomial combinations, or
color-coset-split cofactors. It does not apply to line bases merely from their
density. Thus the general cover inequality remains open, but it cannot be proved
by a universal density lower bound for just these ordinary cofactor templates.

### Free noncommuting voltages do not preserve the cofactor mechanism

Let F_E be the free group with one generator per base incidence, and
replace the additive shift in (1) by right multiplication by that generator.
Assume every base column has at least two incident rows. The resulting
infinite incidence cover is a forest. Indeed, a nonbacktracking closed
path would read a nonempty freely reduced word: consecutive inverse
letters could only traverse the same lifted incidence backwards, by
local uniqueness of that incidence port. Such a word cannot equal the
identity in a free group.

Any finite selected set of columns, together with all their incident rows,
is therefore a finite forest in which all column vertices have degree at
least two. A nonempty component has a leaf row. Its relation equation
forces its unique incident column coefficient to vanish. Removing that
column and repeating proves that all selected columns are rationally
independent. Thus there is no nonzero finite-support integer kernel at
all, even for bases with n>qr. A proposed replacement of commuting
cofactors by universally independent noncommuting variables fails for
this reason. Finite nonabelian covers would need specific group relators;
no useful color-unavoidable choice of such relators is established here.

## Determinant sign mixing is not translation-safe

For even sheet modulus, let

$$
 Q(g)=\sum_{x<y,\ v>w}g_{xv}g_{yw}\pmod2.
$$

On an untranslated matching indicator, Q is the inversion parity of its
permutation. Opposite determinant signs therefore give opposite Q values
**before translation**. They need not do so after a common sheet translation.
This issue already occurs in an axis-line rectangle minor.

Label four corner rows and four boundary-line columns so that the allowed
incidences are

$$
 (1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4),(4,1).
$$

This is the four-corner/four-line submatrix of a rectangle in two axis
directions (the full lines may have additional rows). Its two perfect
matchings have column orders (1,2,3,4) and (2,3,4,1); write their incidence
indicators m_0,m_1. Then Q(m_0)=0 and Q(m_1)=3=1 modulo two.
Set T=e_(1,2). The polar cross-term of Q with T is zero for m_0 and one
for m_1: the latter has exactly the later-row, earlier-column incidence
(4,1). Therefore

$$
 Q(T+m_0)=Q(T+m_1)=0\pmod2.
$$

This is a prescribed symbolic check, with no search. It refutes the inference
from opposite matching signs to a translation-safe Q split **even for line
minors**. It is not a full rank-correct cofactor counterexample, not a
coloring theorem for all templates, and not a relation certificate on full
line columns. The earlier K3,3 six-term identity cancels translation terms;
a two-matching sign comparison does not have that property. No new
all-template or arbitrary-color line-cover conclusion follows.
