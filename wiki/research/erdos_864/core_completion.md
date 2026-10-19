---
name: research/erdos_864/core_completion
desc: Reflection completion, outer-sector symmetrization, the marked-Sidon formulation of one-sided outsiders, and residue-fiber bounds for unary obstructions.
tags: [proved, reductions, bounds, obstacles]
sources: []
created: 2026-09-24T00:00:00Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_864/core_completion

***

The paired core controls every repeated difference. This gives a
reflection-completion criterion, a symmetrization retaining all but the
central-third outsiders, and additional residue constraints when an
outsider's triple lies in the core.

## Reflection-completion criterion

### Conditional reduction when completion is admissible

Suppose the proposed sharp bound has been proved for all integer sets
that are symmetric about an integer or half-integer. Then it also holds
for every admissible set whose reflection closure is admissible.
The qualification about half-integer centers is part of this hypothesis.

Indeed, center the exceptional sum at zero and write the original
interval as $[-L,R]$, where $R\ge L\ge0$ after reflection and
$L+R=N-1$. The centered coordinates can be half-integers. Put
$C=A\cap(-A)$ and $T=A\cup(-A)$. Then $C$ and $T$
are symmetric admissible sets of diameters at most $2L$ and $2R$,
respectively, and

$$
 2|A|=|C|+|T|.
$$

The hypothesized symmetric bound therefore gives, with $K=2/\sqrt3$,

$$
 |A|\le\frac K2\bigl(\sqrt{2L}+\sqrt{2R}\bigr)+o(\sqrt N)
       \le K\sqrt N+o(\sqrt N).
$$

The last step is Cauchy--Schwarz. The error remains uniform when one
of the two diameters is small: for every fixed $\varepsilon>0$,
the symmetric hypothesis gives the bound
$(K+\varepsilon)\sqrt h+O_\varepsilon(1)$ at every diameter $h$.
Ordinary Sidon sets, for which no exceptional center is needed, already
satisfy the stronger classical bound.

Thus off-center geometry causes no additional loss in the unobstructed
completion case. Neither the hypothesized symmetric bound nor
admissibility of reflection closure is asserted for general sets.

### Reflection closure and four-term relations

Translate the exceptional sum to zero, allowing half-integer coordinates,
and suppose the central element has been omitted. Write

$$
 C=A\cap(-A),\qquad D=A\setminus C.
$$

Thus $C=-C$, $D\cap(-D)=\varnothing$, and $D$ is ordinary
Sidon. Then the reflection closure $C\cup D\cup(-D)$ is admissible
with exceptional sum zero if and only if

$$
 C\cap3D=\varnothing,\qquad D\cap3D=\varnothing,
 \qquad 0\notin4D.                                      \tag{1}
$$

Here $jD$ means the $j$-fold sumset, allowing repetitions,
not a dilation. The omission of the central element is part of this
statement; deleting it costs at most one point in asymptotic applications.

For sufficiency, a forbidden equality in the closure is a nontrivial
signed four-term relation. Classify it by the number of occurrences
from $D$, counting multiplicity and absorbing signs of core terms
into $C=-C$. With at most two outsider occurrences, it can be
written as a forbidden equality of two pairs already in $A$, unless
its coefficients cancel. With three outsider occurrences and mixed
signs, the same is true; equal signs instead give $C\cap3D\ne\varnothing$.
With four outsider occurrences, the two-against-two case is an ordinary
Sidon equality in $D$. The remaining cases are precisely the last
two obstructions in (1). The pair equalities involving outsiders cannot
have common sum zero, since outsiders have neither an opposite outsider
nor an opposite core element. These observations also prove necessity:
each obstruction in (1) gives a nontrivial signed four-term relation.

There is some sparsity in the first obstruction. Each unordered pair
of outsiders belongs to at most one unordered triple whose sum is in
$C$: two distinct completions would repeat a difference $c-d$
involving an outsider, contrary to the
[difference-reflection lemma](established_bounds.md). Distinct triples
with the same core target have disjoint supports, by pair-sum uniqueness.
In particular, the distinct-vertex triples form a partial Steiner triple
system. Such a condition alone does not supply the large independent
set that a symmetrization argument would require.

### New closure collisions lie in $\pm(D+D)$

With the same hypotheses, the four sets

$$
 (C+C)\setminus\{0\},\qquad C+D,\qquad C-D,\qquad
 (D-D)\setminus\{0\}
$$

are pairwise disjoint. Indeed, since $C=-C$, they represent
differences of types core--core, outsider--core, core--outsider, and
outsider--outsider, respectively. The difference-reflection lemma
allows a repeated nonzero difference only between two core--core
pairs. It also shows that the representations in each of the last
three types are unique. In the first type, the original sum condition
gives a unique unordered representation.

The only remaining pair-sum types in the closure
$T=C\cup D\cup(-D)$ are $D+D$ and $-D-D$, each with
unique unordered representations. The first is disjoint from
$C+C$ and $C+D$, by admissibility of $A$; the second is
disjoint from $C+C$ and $C-D$, by admissibility of $-A$.
Consequently every new nonzero collision lies in
$\pm(D+D)$. There are at most $d(d+1)$ such values, where
$d=|D|$, and each has at most three unordered representations.
Three representations can occur only through the types
$D+D$, $-D-D$, and $D-D$.

## Outer-sector symmetrization loses only central-third outsiders

Let $A\subset[-R,R]$, with $R>0$, have no repeated unordered
pair sum except possibly zero, and suppose $0\notin A$. Set

$$
 C=A\cap(-A),\qquad D=A\setminus C,\qquad
 d_0=|D\cap[-R/3,R/3]|.
$$

Then there is a symmetric admissible set $T\subset[-R,R]$ such
that

$$
 \boxed{\quad |T|\ge |A|-d_0.\quad}
$$

The assertion holds for integer or half-integer centered coordinates.
Deleting a central element before applying it costs at most one point.

To prove it, choose the larger of the two outsider sectors

$$
 D\cap(R/3,R],\qquad D\cap[-R,-R/3),
$$

and reflect the entire set if necessary so that the selected set
$H$ is positive. The subset $C\cup H\subset A$ has paired
core exactly $C$. Every sum of three elements of $H$ exceeds
$R$, including sums with repeated terms. Therefore

$$
 C\cap3H=\varnothing,\qquad H\cap3H=\varnothing,
 \qquad 0\notin4H.
$$

The completion criterion proves that
$T=C\cup H\cup(-H)$ is admissible. Its pieces are disjoint,
and hence

$$
 |T|=|C|+2|H|\ge |C|+|D|-d_0=|A|-d_0.
$$

Reflecting back, when necessary, gives the claimed set in the original
centered interval.

More precisely, this construction is lossless whenever either outer
sector contains at least $|D|/2$ outsiders. In particular, all sets
with $d_0=0$ reduce losslessly to the symmetric case, whether or
not their full reflection closures are admissible. On either fixed
centered lattice, if $M_{\mathrm{sym}}(R)$ denotes the maximum
size of a symmetric admissible subset of $[-R,R]$, the finite
inequality is

$$
 |A|\le M_{\mathrm{sym}}(R)+d_0.
$$

Thus a sharp symmetric bound would also cover centered families with
$d_0=o(\sqrt R)$. Any excess of size $\varepsilon\sqrt R$
over the symmetric maximum forces at least that many central-third
outsiders.

The interval in this statement is centered at the reflection center
determined by the exceptional sum.
If an original interval becomes $[-L,R]$ with $L<R$, its
symmetric hull has diameter $2R$, rather than $L+R$.
Applying this construction to the hull therefore does not by itself
preserve the original interval length. The earlier conditional
completion argument avoids that loss when the full closure is
admissible.

## One-sided outsiders and marked Sidon sets

Let $B\subset E\subset(0,\infty)$ be finite sets, and put
$A=E\cup(-B)$. Then

$$
 \boxed{\quad
 A\text{ has no repeated unordered pair sum except possibly zero}
 \quad\Longleftrightarrow\quad
 E\text{ is Sidon and }E\cap(E+E+B)=\varnothing.
 \quad}
$$

All sums include repeated terms. This describes precisely the sets
with positive outsiders after centering and deleting zero: their
positive part is $E$, their negative part is $-B$, and their
core is $B\cup(-B)$.

For necessity, all sums from $E+E$ are positive, so admissibility
forces $E$ to be Sidon. A relation
$e_3=e_1+e_2+b$, with $e_i\in E$ and $b\in B$, would
give the forbidden collision

$$
 e_1+e_2=e_3+(-b)>0.
$$

The two unordered pairs are different because only one contains a
negative element.

Conversely, suppose the two conditions hold. Positive same-sign sums
are unique by Sidonicity of $E$, and negative same-sign sums are
unique because $B\subset E$. If two mixed sums coincide, then

$$
 e-b=e'-b'\quad\Longrightarrow\quad e+b'=e'+b.
$$

Sidonicity says either the mixed pairs are identical or
$e=b$ and $e'=b'$, in which case their common sum is zero.
A positive same-sign sum colliding with a mixed sum would give
$e_1+e_2=e_3-b$, contrary to $E\cap(E+E+B)=\varnothing$.
A negative same-sign sum colliding with a mixed sum would give

$$
 -b_1-b_2=e-b_3
 \quad\Longrightarrow\quad b_3=e+b_1+b_2,
$$

which contradicts the same condition. Positive and negative same-sign
sums cannot coincide. This exhausts all pair types and proves
sufficiency.

Equivalently, mark the elements of $B$ inside an ordinary Sidon
set $E$. No marked element may occur in any of the three input
positions of a relation $x+y+z=w$ in $E$. The cardinality of
$A$ is the weighted count

$$
 |A|=|E|+|B|=\sum_{e\in E}\bigl(1+1_B(e)\bigr).
$$

For nonempty $B$, its span is $\max E+\max B$. The missing
weighted extremal statement for this subclass is therefore

$$
 (|E|+|B|)^2
 \le \left(\frac43+o(1)\right)(\max E+\max B)
$$

under the displayed marked-Sidon conditions, for positive integer or
half-integer centered coordinates as the span tends to infinity.
The symmetric problem is only the case $B=E$, when the condition
becomes $E\cap3E=\varnothing$. Its conclusion does not directly
control arbitrary markings; in particular, the unmarked elements may
participate in three-input relations. If $B=\varnothing$, the
ordinary Sidon bound already applies.

## A weighted residue-fiber inequality

Return to integer coordinates $A\subset[1,N]$, with exceptional
sum $s$, core $C=A\cap(s-A)$, and outsiders $D=A\setminus C$.
Put

$$
 k=|A|,\quad c=|C|,\quad d=|D|,\qquad
 w_a=\begin{cases}1/\sqrt2,&a\in C,\\1,&a\in D,\end{cases}
$$


$$
 W=\sum_aw_a=k-(1-1/\sqrt2)c,
 \qquad Q=\sum_aw_a^2=k-c/2.
$$

For every positive integer $q$, let

$$
 H=\lceil N/q\rceil,\qquad
 W_r=\sum_{a\equiv r\pmod q}w_a.
$$

For every integer $h\ge1$,

$$
 \boxed{\quad
 \sum_{r\bmod q}W_r^2
 \le (H+h-1)\left(1+\frac{Q-1}{h}\right).
 \quad}                                                   \tag{2}
$$


To prove this, divide the coordinates in each residue fiber by $q$
after a translation, obtaining an interval of at most $H$ integer
positions. Let $X_{r,h}(t)$ be its weighted length-$h$ window
count. The repeated-difference structure gives

$$
 \sum_{a-b=j}w_aw_b\le1\qquad(j>0):
$$

a repeated difference has two core-core representations of weight
$1/2$ each, and an unrepeated difference has weight at most one.
Consequently

$$
 \begin{aligned}
 \sum_{r,t}X_{r,h}(t)^2
 &=hQ+2\sum_{j=1}^{h-1}(h-j)
                 \sum_{a-b=qj}w_aw_b\\
 &\le hQ+h(h-1).
 \end{aligned}
$$

Each fiber has at most $H+h-1$ nonzero window positions and total
window mass $hW_r$. Applying Cauchy--Schwarz separately in the
fibers gives (2).

When $Q\ge1$, choose

$$
 h=\max\{1,\lceil\sqrt{(H-1)(Q-1)}\rceil\}.
$$

Writing the right side of (2) as
$H+Q-2+h+(H-1)(Q-1)/h$ shows that

$$
 \sum_rW_r^2
 \le\bigl(\sqrt{H-1}+\sqrt{Q-1}\bigr)^2+1.                 \tag{3}
$$

In particular, for fixed $q$, the established $k=O(\sqrt N)$
bound implies

$$
 q\sum_rW_r^2\le N+O_q(N^{3/4}).                           \tag{4}
$$

The finite form (2) remains valid for growing moduli; no uniform
fixed-modulus asymptotic is being asserted for them.

## Outsiders with a unary obstruction

Call $a\in D$ unary-obstructed when
$3a-s\in C$, and let $U$ be their set, $u=|U|$.
In centered coordinates this is the relation $3a\in C$, which
prevents adjoining the individual reflected point $-a$.

Each $a\in U$ forces the core pair

$$
 3a-s,\qquad 2s-3a.
$$

These $2u$ points are all distinct. A within-pair coincidence
would put $a=s/2$ in the core; a coincidence between different
pairs would give two outsiders summing to $s$. All lie in the
single residue class

$$
 r_0=-s\pmod3.
$$

Thus $W_{r_0}\ge\sqrt2u$. Minimizing three squared masses with
given total $W$ and this lower bound, then using (4), proves

$$
 \boxed{\quad
 W^2+\frac92\left(\sqrt2u-\frac W3\right)_+^2
 \le N+O(N^{3/4}).
 \quad}                                                   \tag{5}
$$

The finite right side is
$3(H+h-1)(1+(Q-1)/h)$, where $H=\lceil N/3\rceil$.
This works without doubling the interval when $s$ is odd.

The residue formulation is as follows. Label the other two
residues $r_1,r_2$, and write

$$
 c_0=|C\cap(r_0\bmod3)|,\qquad d_i=|D\cap(r_i\bmod3)|.
$$

Reflection interchanges the other two core fibers. The elementary
identity for the sum of three squares therefore gives

$$
 W^2+\frac92\left(\frac{c_0}{\sqrt2}+d_0-\frac W3\right)^2
       +\frac32(d_1-d_2)^2
 \le N+O(N^{3/4}).                                        \tag{6}
$$

If $u_0=|U\cap(r_0\bmod3)|$ is known, $\sqrt2u$ in (5)
can be replaced by $\sqrt2u+u_0$.

## The pure unary template cannot improve the lower constant

Suppose that the entire core consists of the forced pairs:

$$
 C=\{3a-s,\ 2s-3a:a\in D\}.
$$

Then $c=2d$, $k=3d$. After centering, this is precisely the
template $D\cup3D\cup(-3D)$ with three disjoint pieces, where
$3D$ in this sentence denotes dilation.

The residue weights are

$$
 W_{r_0}=\sqrt2d+d_0,\qquad W_{r_1}=d_1,\qquad W_{r_2}=d_2.
$$

Since $d_0+d_1+d_2=d$,

$$
 \begin{aligned}
 \sum_rW_r^2
 &\ge(\sqrt2d+d_0)^2+\frac{(d-d_0)^2}{2}\\
 &=\frac52d^2+(2\sqrt2-1)dd_0+\frac32d_0^2
 \ge\frac52d^2.
 \end{aligned}
$$

Using (3) with $Q=2d$ proves the finite inequality

$$
 \frac52d^2
 \le\bigl(\sqrt{\lceil N/3\rceil-1}+\sqrt{2d-1}\bigr)^2+1,
$$

and hence

$$
 \boxed{\quad
 k^2\le\frac65N+O(N^{3/4}),\qquad
 k\le\sqrt{\frac65N}+O(N^{1/4}).
 \quad}                                                   \tag{7}
$$

This excludes the whole integer template, independently of any
algebraic construction used for its input.

A small extension is also immediate. If every outsider is unary-obstructed
and

$$
 2d\le c\le\frac{31+\sqrt2}{14}\,d,
$$

then $k^2\le(4/3)N+O(N^{3/4})$. In this range the active
left side of (5) is

$$
 6d^2+\frac34\bigl(c+(\sqrt2-2)d\bigr)^2,
$$

which is at least $3(c+d)^2/4$ exactly when the displayed upper
bound on $c/d$ holds. This does not cover a core much larger than
the forced $2d$ points, or non-unary completion obstructions.

## Why the residue information matters

The corresponding unweighted continuum difference-capacity test at
every shift admits a supercritical profile. Put

$$
 E=\pm\bigl((1/3,1]\cup(1/27,1/9]\cup(1/243,1/81]\bigr),
 \qquad f_D=\tfrac12 1_E,\quad f_C=\tfrac13 1_{3E},
 \quad f_A=f_C+f_D.
$$

The supports of $f_C,f_D$ are disjoint, and $f_C$ is exactly
the profile obtained from the two reflected dilations of $f_D$.
Writing $\widetilde f(t)=f(-t)$, interval-overlap calculation
gives

$$
 \max_t\left[(f_A*\widetilde f_A)(t)
                  -\tfrac12(f_C*\widetilde f_C)(t)\right]
 =\frac{458}{729},\qquad \int f_A=\frac{182}{81}.
$$

The maximum is attained at $t=2/9$. After rescaling the heights
to make that maximum one, the squared mass divided by the support
span is

$$
 \frac{(182/81)^2}{6(458/729)}
 =\frac{8281}{6183}>\frac43.
$$

The retained verifier
checks all 44 nonnegative differences of interval endpoints. They
include every knot of this continuous piecewise-affine correlation,
so this is a finite certificate for the stated calculation.

This profile is not an integer construction and is not claimed to
satisfy every possible vector-weighted or higher-order relaxation.
The residue theorem (7) proves that it cannot come from an admissible
integer set of the pure unary form. It illustrates a concrete
arithmetic restriction missed by this all-shift macroscopic test.

## A separate modular check for a Ruzsa input

There is also a short obstruction for the analogous dilation template
in a particular cyclic group. For a prime $p\ge5$, fix a generator
$g$ of $\mathbb F_p^*$, put

$$
 v(x)=(\log_gx,x)\in\mathbb Z_{p-1}\times\mathbb F_p,
 \qquad D_T=\{v(x):x\in T\},
$$

and suppose $D_T\cup3D_T\cup(-3D_T)$ is admissible with
exceptional sum zero, where the multiples here are group dilations.
For every $w\ne0$,

$$
 v(w)+3v(-2w)=v(-8w)+3v(w).                                \tag{8}
$$

The logarithmic coordinates agree because
$w(-2w)^3=(-8w)w^3$; the other coordinate is $-5w$.
The equality is nontrivial: either identification of its unordered
pairs would force $p=3$ or $p=2$. Its common sum is nonzero
when $p\ne5$; for $p=5$, its first coordinate is
$\log_g2\ne0$ modulo four, so it remains nonzero.

Thus $T$ must miss a vertex of each three-element set
$\{w,-2w,-8w\}$. Counting these as a multihypergraph, there
are $p-1$ edges and each vertex occurs exactly three times.
Consequently

$$
 |T|\le\frac23(p-1).
$$

This modular statement is construction-specific. The interval theorem
(7) is stronger for its own integer template and requires no Ruzsa
input or homomorphic encoding.
