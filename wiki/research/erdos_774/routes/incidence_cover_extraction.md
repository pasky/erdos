---
name: research/erdos_774/routes/incidence_cover_extraction
title: Uniform extraction survives every finite incidence cover of axis lines
desc: Arbitrary finite covers of all common row duplications of linear-side axis-line matrices retain one uniform full-dissociation extraction constant; integer relations lift to ternary ones, but no color-unavoidable cover theorem is proved.
tags: [E0774, proved, extraction, construction, conditional, incomplete]
sources: []
created: 2026-09-18T19:31:25Z
updated: 2026-10-13T05:28:09Z
---


# Uniform extraction survives every finite incidence cover of axis lines

***

**Row-projection simplification.**
[Deleting duplicated rows](../lemmas/cover_projection_and_templates.md)
shows that the duplicated-cover family has exactly the same chromatic
supremum as ordinary covers, and inherits the stronger bound
$\rho\ge e^{-\pi^2/2}$ directly. Section 7 remains a valid earlier
proof, but its sine-moment construction is unnecessary for row duplication.
The new fixed-partial-template obstruction on the same linked page also
sharpens Section 8's Ramsey limitation. No unbounded coloring is proved.

## Standing and theorem

Let $L_t=L(d_1,\ldots,d_t)$ be the full axis-line indicator family on
$X_t=\prod_{i\leq t}[d_i]$, with $d_i\geq3$. This page proves that
the [direct axis-line extraction estimate](axis_line_extraction.md)
holds uniformly over **all finite bipartite-incidence covers** of its
point-by-line matrix, not merely over literal boxes or one chosen sequence
of twists.

The stronger Section 7 theorem also permits any common row-duplication
factor before taking the cover, with one bound $\rho\ge e^{-2\pi^2}$
independent of every parameter. Both analytic statements and the integer
lifting construction are author-recorded; a separate reviewer checked them.

For every cover degree $m$, every such covered configuration
$\widetilde L_t$ satisfies
$$
\rho(\widetilde L_t)\geq
\min_{i\leq t}\prod_{j=i+1}^t\cos(\pi/d_j)^{d_i}.
\tag{1}
$$
In particular $d_i=i+2$ gives
$$
\rho(\widetilde L_t)\geq e^{-\pi^2/2}
\tag{2}
$$
independently of $t,m$, and every choice of incidence permutations.
There is one $\delta>0$ giving full dissociated extraction from every
subset of every one of these covers.

Section 7 also permits **any common finite row-duplication factor**
$R$ before taking the incidence cover. For $d_i=i+2$, all of these
larger families have the uniform real-Sidon bound $e^{-2\pi^2}$,
independently of $R$, the cover degree, and the permutations. This
amplifies column support sizes, while each row still has degree $t$.

Separately, every nonzero integer relation of a finite $0/1$ matrix
becomes a nonzero ternary relation in a suitable finite incidence cover.
For an axis-line relation of coefficient height $h$, cover degree at
most $h\lfloor t/2\rfloor$ suffices.

Neither statement controls an arbitrary coloring of the cover. In
particular, it is **not proved** that some cover must have dissociated
chromatic number comparable to the rational coloring number of its base.
That would be a sufficient new route, not a consequence established here.

## 1. Exact meaning of a finite incidence cover

Let $A\in\{0,1\}^{X\times V}$ be a finite matrix. For each incidence
$A_{x,v}=1$, choose a permutation
$\pi_{x,v}$ of $[m]$. The degree-$m$ covered matrix has row labels
$(x,a)\in X\times[m]$, column labels $(v,b)\in V\times[m]$, and
$$
\widetilde A_{(x,a),(v,b)}
=
\begin{cases}
1,& A_{x,v}=1\ \text{and }a=\pi_{x,v}(b),\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
$$
This is precisely a covering of the bipartite incidence graph that
preserves its row and column types. The permutations are independent
choices for different base incidences; connectivity is not required.

Every covered column has the same support size as its base column.
Every covered row has the same degree as its base row. If the base
columns are distinct and nonzero, so are the covered columns: their
projections to base row supports distinguish different base columns, and
different lifts of one base column have disjoint nonempty supports.
In particular covers of $L_t$ are genuine sets of distinct nonzero
$0/1$ vectors, without antipodal pairs.

## 2. Every axis-line cover has the twisted-layer decomposition

Write $X_t=X_{t-1}\times[d]$, $d=d_t$. Split covered rows into the
$d$ sets
$$
\{(x,s,a):x\in X_{t-1},\,a\in[m]\},
\qquad s\in[d].
$$
The old directions $i<t$ in each layer form an arbitrary degree-$m$
cover of $L_{t-1}$. These $d$ covers need not be isomorphic; the
uniform induction applies separately to each one.

The new direction has base columns indexed by $x\in X_{t-1}$.
For its lift labeled $(x,b)$, the row in layer $s$ is
$$
(x,s,\pi_{(x,s),\,\ell_x}(b)).
$$
For each $s$, define the bijection of the covered old row set
$$
T_s(x,b)=(x,\pi_{(x,s),\,\ell_x}(b)).
\tag{4}
$$
Thus the new columns are exactly the disjoint transversals
$$
n_y=\sum_{s=1}^d e_{(T_s y,s)},
\qquad y\in X_{t-1}\times[m].
\tag{5}
$$
An old column lies wholly in one layer and meets each new transversal
in at most one point. This decomposition used no restriction on the
permutations in (3), and therefore covers every finite incidence cover.

## 3. Uniform directional Sidon induction over all covers

Put $a_d=\cos(\pi/d)$. The elementary root-polygon lemma states:
for every $u\in\mathbb T$, there is a finite random $Y\in\mathbb T$
with
$$
Y^d=u,\qquad \mathbb EY=a_d.
\tag{6}
$$
The expectation is target-independent, because the convex hull of the
$d$-th roots of $u$ contains the disk of radius $a_d$.

We prove simultaneously for all degree-$m$ covers that a polynomial
with total coefficient magnitude $W_i$ in direction $i$ obeys
$$
\max\operatorname{Re}P\geq
\sum_{i\leq t}r_{i,t}W_i,\qquad
r_{i,t}=\prod_{j=i+1}^t a_{d_j}^{d_i}.
\tag{7}
$$
For $t=1$, all $m$ covered lines have disjoint supports, so their
characters can be prescribed independently and $r_{1,1}=1$.

At the induction step, decompose $P$ into old layer polynomials and
new terms
$$
\sum_y b_y\prod_{s=1}^d z_{T_s y,s}.
\tag{8}
$$
In every old layer, first multiply every direction-$i$ coefficient
by $a_d^{d_i}$. Choose its phases by (7) for that layer's own covered
matrix, then hold all those phase choices fixed.

For each new transversal label $y$, prescribe $u_y$ so that
multiplying its $d$ point phases by a common $d$-th root of $u_y$
makes its term equal to $|b_y|$. If $b_y=0$, choose any target.
Choose independent $Y_y$ as in (6), and make the replacement
$$
z'_{T_s y,s}=z_{T_s y,s}Y_y
\quad\text{for every }y,s.
\tag{9}
$$
Because $T_s$ is a bijection, this assigns each row phase exactly once.
Each new term is aligned deterministically. Each old direction-$i$
column uses $d_i$ distinct transversal labels, so its expected
multiplier is exactly $a_d^{d_i}$. Thus the expected old polynomial
is precisely the rescaled polynomial optimized earlier. Its directional
bound is $r_{i,t-1}a_d^{d_i}W_i$, while the new terms contribute $W_t$.
A finite random outcome attains the expectation. This proves (7) and (1).

The proof uses neither identical old covers in the different layers nor
independence between layers. It requires independence only across
transversal labels. This is why arbitrary incidence permutations do not
change the estimate.

For $d_i=i+2$, the already proved elementary inequality
$$
-\log\cos(\pi/n)\leq\frac{\pi^2}{2n(n-1)},\qquad n\geq4,
$$
telescopes to $r_{i,t}\geq e^{-\pi^2/2}$, giving (2).
More generally, the same uniform result holds whenever
$\sup_i d_i\sum_{j>i}d_j^{-2}<\infty$, with the constant recorded
in the axis-line extraction theorem.

## 4. One extraction constant for every covered matrix

There are countably many finite covers in question: for each $t,m$
there are finitely many choices of the permutations (3). Place one copy
of each covered configuration in its own free-abelian direct summand.
Let $\Lambda$ be their union in the resulting countable direct sum.

Every finite polynomial on $\Lambda$ splits between finitely many summands.
Their phase choices are independent, so (2) gives the same positive-real Sidon
estimate on the whole union. Pisier's Theorem 2, already checked in the supplied
[full source](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md),
applies **once** to this one Sidon set. It supplies one full-dissociation
extraction constant $\delta>0$ for every finite subset of $\Lambda$, hence
uniformly for all $t,m$ and incidence covers.

No quantitative dependence of $\delta$ on (2) is asserted. The direct
sum is used only to make uniformity across unrelated covers explicit;
compatible covering maps or nested choices of permutations are unnecessary.

## 5. Every integer relation has a ternary covering lift

Let $A$ have nonzero $0/1$ columns, and let
$$
0\ne a=(a_v)_{v\in V}\in\ker_{\mathbb Z}A.
\tag{10}
$$
For each base row $x$, set
$$
p_x=\sum_{\substack{v:A_{x,v}=1\\a_v>0}}a_v
    =\sum_{\substack{v:A_{x,v}=1\\a_v<0}}|a_v|.
\tag{11}
$$
Set $m=\max_x p_x$. This is positive. Also $|a_v|\leq m$ for
every $v$, since every column is nonzero and (11) holds at a row in
its support.

Select copies $1,\ldots,|a_v|$ of each column $v$ and give them
the common sign $\operatorname{sgn}(a_v)$. At a row $x$, its
selected positive incidences and selected negative incidences both
number $p_x$. Pair them bijectively and give the pairs distinct labels
from $[m]$. Define $\pi_{x,v}$ on each selected column copy to send
it to its pair's label.

For each fixed $(x,v)$, distinct selected copies receive distinct row
labels, so this partial injection extends to a permutation of $[m]$.
Choose arbitrary extensions, independently for all incidences. In the
covered matrix, every used row receives exactly one selected positive
incidence and one selected negative incidence; unused rows receive none.
Therefore
$$
\sum_{v:a_v\ne0}\operatorname{sgn}(a_v)
       \sum_{b=1}^{|a_v|}\widetilde A_{v,b}=0
\tag{12}
$$
is a nonzero ternary relation on distinct column labels.
For bases with distinct nonzero columns, including axis lines, these are
also distinct actual vectors, as checked in Section 1.

If $|a_v|\leq h$ and every base row has degree at most $\Delta$,
then
$$
m\leq h\lfloor\Delta/2\rfloor.
\tag{13}
$$
Indeed the positive and negative incident base columns are disjoint
sets, and (11) is at most $h$ times the cardinality of either set.
Their smaller cardinality is at most $\lfloor\Delta/2\rfloor$.
For $L_t$, $\Delta=t$, proving the asserted degree bound.

This is an existence construction for a cover tailored to one integer
relation. It does not say that an arbitrary fixed cover lifts that
relation, or that arbitrary colors of the selected copies agree.

## 6. Exact missing color statement

For a finite base $A$, let
$$
\Gamma(A)=\sup_{\widetilde A\text{ a finite incidence cover}}
                 \chi_1(\widetilde A).
$$
No general lower bound
$$
\Gamma(A)\geq\chi_{\mathbb Q}(A)
\quad\text{or even}\quad
\Gamma(A)\geq |V(A)|/|X(A)|
\tag{14}
$$
has been established here. Either displayed bound, applied to the linear
axis-line bases, would give unbounded covered dissociated coloring because
$$
\frac{|L_t|}{|X_t|}
=\sum_{i\leq t}\frac1{i+2}\longrightarrow\infty.
$$
Together with the uniform extraction theorem, that would complete the
finite-block obligation. Equation (14) is only a proposed sufficient
theorem and is not asserted true.

Section 5 handles a monochromatic relation only when the selected lifted
columns happen to share an actual color. A coloring may use different
colors at different copies of the same base column. Building one cover
for each base relation, or taking their disjoint union, does not remove
that freedom. Covers can also have relations whose signed fiber totals
are all zero, so projection to base relations is not a full description
of their relation systems.

Thus the remaining problem is a genuine color-unavoidable covering
construction, not integer coefficient flattening alone. No computation
or external covering/Ramsey theorem is used in this page.

## 7. Uniform row duplication also preserves covered extraction

For a fixed integer $R\geq1$, replace each row $x$ of the axis-line
matrix by rows $(x,r)$, $r\in[R]$, with identical entries. Denote
this matrix by $A_t^{[R]}$. It has exactly the same integer and
rational relation lattices as $A_t$. Now take an arbitrary
degree-$m$ incidence cover of $A_t^{[R]}$, with independent
permutations for all incidences at these duplicated rows.

**Theorem.** For $d_i=i+2$, every such covered matrix has
$$
\rho\bigl(\widetilde A_t^{[R]}\bigr)
\geq e^{-2\pi^2},
\tag{15}
$$
uniformly in $t,R,m$ and all incidence permutations. The whole
collection consequently has one proportional full-dissociation
extraction constant.

The proof needs controlled moments up to $R$, because an old column
can now meet a new column in as many as $R$ points. No chromatic
amplification follows merely from allowing these extra incidences.

### 7.1 A finite root distribution with several target-independent moments

Let $D=Rd$, where $R\geq1$ and $d\geq4$, and put
$$
L=D-R-1,\qquad
\alpha_j=\sin\frac{(j+1)\pi}{L+2}\quad(0\leq j\leq L),
\qquad
Q=\sum_{j=0}^L\alpha_j^2.
$$
For any $u\in\mathbb T$, give a $D$-th root $y$ of $u$
probability
$$
\mathbb P(Y=y)
=\frac1{DQ}\left|\sum_{j=0}^L\alpha_jy^j\right|^2.
\tag{16}
$$
These weights are nonnegative and sum to one. Indeed the polynomial
inside (16), after taking absolute square, has Laurent degree at most
$L<D$; averaging on the $D$-th roots annihilates every nonconstant
Laurent monomial appearing in it. The remaining coefficient is $Q$.

Similarly, for $0\leq k\leq R$,
$$
Y^D=u,\qquad
\mathbb EY^k=c_k:=
\frac{\sum_{j=0}^{L-k}\alpha_j\alpha_{j+k}}{Q}.
\tag{17}
$$
There are no aliases: after multiplication by $y^k$, all exponents
lie strictly between $-D$ and $D$, since $L+R=D-1$.
Thus (17) is independent of the prescribed target $u$. In particular
$c_0=1$, and $c_k>0$ for $1\leq k\leq R$.

Extend the vector $\alpha$ by zero to $\mathbb Z$, and let $S$
be the shift operator on its square-summable coordinate space. The sine
eigenvector identity gives
$$
c_1=\cos\frac{\pi}{L+2},\qquad
\|(S-I)\alpha\|_2^2=2Q(1-c_1).
$$
Using $S^k-I=\sum_{a=0}^{k-1}S^a(S-I)$ and the triangle inequality,
$$
1-c_k
=\frac{\|(S^k-I)\alpha\|_2^2}{2Q}
\leq k^2(1-c_1)
\leq\frac{\pi^2k^2}{2(D-R+1)^2}.
\tag{18}
$$
For $k\leq R,d\geq4$, the last upper bound is less than $5/9$,
because $\pi^2<10$ and $D-R+1\geq3R+1$.
Hence $-\log c_k\leq-\log(1-v)\leq v/(1-v)\leq9v/4$, with $v$
equal to that bound in (18). As $D-R+1\geq3D/4$, this proves
$$
c_k\geq
\exp\left(-\,\frac{2\pi^2k^2}{D^2}\right)
\quad(0\leq k\leq R).
\tag{19}
$$
All distributions are finite. Their probabilities may depend on $u$;
the moments used in the induction do not.

### 7.2 Geometry of a covered duplicated-row extension

Split the covered rows according to the last base coordinate
$s\in[d]$, $d=d_t$. The old directions in each layer form an
arbitrary degree-$m$ cover of $A_{t-1}^{[R]}$.

The new-axis columns form a partition of all covered rows, each block
having exactly $D=Rd$ points. A new block has a fixed base point
$x\in X_{t-1}$. An old direction-$i$ column lies in one layer
and projects onto $d_i$ distinct old base points, with $R$ covered
rows over each one. Therefore its intersections with the new blocks
have sizes $k_1,k_2,\ldots$ satisfying
$$
0\leq k_a\leq R,\qquad
\sum_a k_a=Rd_i,\qquad
\sum_a k_a^2\leq R^2d_i.
\tag{20}
$$
The upper bound $R$ uses preservation of base point labels in an
incidence cover. It is not claimed for arbitrary unstructured block
partitions of the same total size.

### 7.3 Prescaled induction

For each old covered column $\ell$, define its fixed multiplier
$$
\gamma_\ell=\prod_a c_{k_a},
$$
using its actual intersection sizes in (20). By (19),
$$
\gamma_\ell\geq
\exp\left(-\,\frac{2\pi^2d_i}{d_t^2}\right)
\quad\text{if }\ell\text{ has direction }i<t.
\tag{21}
$$
These multipliers may depend on the incidence permutations and the
column, but do not depend on phase targets.

Multiply every old coefficient by its $\gamma_\ell$, optimize the
resulting polynomial in each old layer, and then fix those phases.
For each new block prescribe $u$ to align its coefficient. Independently
choose its $Y$ from (16), and multiply every row phase in that block
by $Y$. Every new term is exactly aligned because the block has
$D$ points and $Y^D=u$. An old column has expected multiplier
exactly $\gamma_\ell$, by independence across new blocks and (17).
Thus expectation recovers precisely the prescaled old polynomial.

The resulting directional lower bound is
$$
\max\operatorname{Re}P
\geq\sum_{i\leq t}
\exp\left(-2\pi^2d_i\sum_{j=i+1}^t d_j^{-2}\right)W_i.
\tag{22}
$$
At $t=1$, the covered columns have disjoint supports even after
row duplication, so the induction starts with parameter one.
All later sides satisfy $d_t=t+2\geq4$, as required in (16)--(19).
Finally
$$
d_i\sum_{j>i}d_j^{-2}\leq1
$$
for $d_i=i+2$. This proves (15).

For the uniform extraction assertion, enlarge the direct sum in
Section 4 to include all positive integers $R$ as well. The collection
is still countable, and (15) gives one Sidon estimate on its union.
One application of Pisier's theorem supplies one extraction constant for
the entire enlarged collection. No finite-stage or duplication-dependent
sequence of extraction constants is used.

### 7.4 Exact chromatic standing of this enlargement

Duplicating rows leaves the base rational coloring number unchanged,
but arbitrary covers of the duplicated matrix can have new relation
supports. A possible sufficient statement would now be
$$
\sup_{\substack{R\geq1\\
\widetilde A\text{ a finite cover of }A^{[R]}}}
\chi_1(\widetilde A)\geq\chi_{\mathbb Q}(A).
\tag{23}
$$
Equation (23) is **unproved and not asserted true**. Allowing $R$
provides arbitrarily many incidence positions in each column; it does
not increase the number of columns incident to one row, and it does
not by itself force selected covering copies to share a color.

The ordinary-cover and row-duplication estimates, and the integer
flattening construction, are the proved outcomes. No color-unavoidable
covering or sparse-gadget amplification theorem is claimed.

## 8. Scope of the checked Ramsey input

The digest and relevant full passages of
[Nešetřil–Rödl–Sales](../../../../library/integer_sequences/nesetril_2024_pisier_type_theorems/_index.md)
were consulted during research.
[Theorem 3.2](../../../../library/integer_sequences/nesetril_2024_pisier_type_theorems/_index.md)
supplies an ordered partial-Steiner Ramsey host, not a degree-preserving
incidence cover. Its fixed-order application does not provide full dissociation
or an implementation by the operations above. No new positive result here
depends on importing that missing implementation.

A specific full-cover focusing proposal has a precise limitation. An
incidence-preserving embedding over a fixed base of a complete finite cover
into another cover has image a union of connected components: the embedded
vertices already use every allowed incidence port, so no adjacent vertex
can lie outside the image. For a connected nontrivial cover (cover degree
greater than one), two colors can split one column fiber in each host
component isomorphic to it. No embedded copy of that full cover is then
fiber-monochromatic.

This does **not** exclude Ramsey constructions for partial balanced
supports, whose row ports need not be exhausted. It also supplies no
negative conclusion about the row-duplication enlargement in Section 7.
The surviving obligation is still a prechosen finite cover defeating every
coloring, rather than a cover chosen after seeing a relation or its colors.
