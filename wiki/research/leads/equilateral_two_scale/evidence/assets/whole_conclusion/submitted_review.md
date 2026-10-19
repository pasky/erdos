---
desc: |
  Independent adversarial examination of the complete supplied argument for
  Problem 173, including arbitrary colorings, transcendental scale ratios,
  degenerate triangles, and the source specializations.
---

# Whole-conclusion examination of Problem 173

***

## Subject and independence

**Examination date:** 2026-10-17 UTC. **Subject freeze date:** 2026-10-17.
**Assignment:** attempt to refute the whole conclusion and every essential
step of the supplied proof. **Reviewer:** an independent reviewer in a fresh,
isolated context, neither an author nor a collaborator on this subject. This
is a mathematical examination, not a grade of this report or a tier assertion.

The subject is the statement at
`wiki/problems/discrete_geometry/E0173/_index.md`, lines 24--27, and the
candidate conclusion and seven-step argument at
`wiki/research/leads/equilateral_two_scale/_index.md`, lines 69--83,
91--97, 103--135 and 137--164, as supplied in the frozen extraction. The
project argument is attributed to Plasma AI. The following table identifies
the other native proof inputs. Line numbers refer to the original frozen
pages, not to the shorter extraction.

| Page under `wiki/research/leads/equilateral_two_scale/` | Supplied scope |
| --- | --- |
| `unit_templates.md` | Lines 22--273: finite-cover Theorem 1 and its proof. |
| `rigidity_extension.md` | Lines 26--222: Theorem 2, Corollary 3, field specialization and composition. |
| `transcendental_scales.md` | Lines 112--114, 129--137, 231--259, 341--379, 383--397, 400--445 and 452--473: carrier, templates and conversion. |
| `binary_transfer.md` | Lines 26--62 and 64--210: conventions, two-scale extension, continuous factor, sampling and both transfer directions. |
| `circle_exclusion.md` | Lines 32--196 and 199--282: finite forcing, measurable exclusion and its consequences. |
| `spectral_exclusion.md` | Lines 22--139, 145--200, 229--236 and 256--301: Bessel bounds, measurable exclusion, R0 and the conditional spectral argument. |

The supporting mathematical inputs are the retained excerpts of:

- `library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/openai_2026_euclidean_plane_not_five_colorable.md`,
  Sections 2 and 3 and the supplied Section 4 through Proposition 4.2,
  original lines 83--545, together with the selected bibliography and the
  bibliographic excerpt from that source directory's `_index.md`;
- `library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/jelinek_2009_monochromatic_triangles_two_colored_plane.md`,
  the conventions at lines 48--54 and Lemma 1.3 and Corollary 1.4, including
  the proof, at lines 72--94, together with its bibliographic identity;
- Lahti, arXiv:1804.11216v1, the supplied `main.tex` excerpt containing the
  Euclidean introduction, Theorem 1.1, the metric hypotheses, the boundary
  definition, formulas (2.2)--(2.4), required macros and bibliography.

The fourteen prepared excerpts were read in full. Their retained mathematical
sections, rather than omitted sections of the original pages, define the
scope. The frozen native proof copies accompanying this report belong under
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/`.
The assessment is about those copies of the named project subjects and the
identified source editions, not subsequent revisions at the original paths.
External source prose is not reproduced in this report. The manifest's
identities were checked before reading and remained unchanged during the
examination.

Only the prepared mathematical packet and the authorized operating rules
were read. No original proof page, other checkout, author plan or memory,
prior verdict, outside formalization, message inbox, broad repository search,
network source, or repository gate output was consumed. The review began with
an empty subscription table and remained isolated. No excluded exposure is
known. No claim of independence rests merely on the empty table: it is also
supported by the actual restricted reading and absence of authorship or
collaboration. The complete review contract in `docs/verification.md`, its
procedural adapter, and the applicable source and authoring rules were read.

Source reading was text-only. No PDF or figure was inspected, and no claim is
made to have checked a transcription against its printed edition. The supplied
coordinates remove dependence on Jelínek's figure. The source identities fix
which texts were examined; they confer no accepted proof standing.

The argument below and the retained exact-rational check are the independent
evidence. The check's filing path is
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py`.
Its literal rational inputs are in the program; it reads no other file. No
mathematical conclusion is inferred from cached output.

## Restatement

For a coloring $c:\mathbb R^2\to\{-1,1\}$, let $M(c)$ be the set of
positive lengths $r$ for which $c$ has no monochromatic equilateral triangle
of side $r$. The principal assertion is

$$
\forall c,\qquad |M(c)|\leq1,
$$

and, for the same coloring, every set of three distinct points whose three
mutual distances are not all equal has a monochromatic congruent copy.
Collinear triples are included. There is no measurability, Baire, density or
other regularity hypothesis on $c$. A possible missing length depends on the
coloring; the assertion neither specifies a universal exceptional length nor
requires an exception to exist.

The two-scale assertion is

$$
\forall x\in\mathbb R_{>0}\setminus\{1\}\ \forall c\quad
\exists r\in\{1,x\}\ \exists p\in\mathbb C\ \exists u\in S^1:
\quad c(p)=c(p+ru)=c(p+ru\omega),
\qquad \omega=e^{i\pi/3}.
$$

All real ratios are included, with separate algebraic and transcendental
arguments. Rescaling a coloring missing two lengths reduces to this assertion.
The finite forcing lemma supplies the non-equilateral conclusion; its role is
proved below rather than treated as an extra assumption.

Direct copies in the proof use translations and rotations. An unordered
equilateral triangle has no additional reflected congruence class. For other
triangles the coordinate forcing works for either chosen orientation of the
target, so no reflection invariance of the coloring is needed.

For a measurable coloring, weak avoidance means that monochromatic placements
have zero measure for plane area times arc length on the motion parameters.
The measurable consequence under examination is stronger than the existence
of one copy: every non-equilateral triangle has a positive-measure set of
monochromatic placements. Pointwise avoidance is not silently substituted for
this intermediate weak condition.

For the algebraic and spectral arguments, fix $x$ and let $F_x$ be the real
closure of $\mathbb Q(x)$ inside $\mathbb R$, $L=F_x(i)$, and
$K_x=\{u\in L:|u|=1\}$. For any subfield $N\subset L$, write
$K_N=N\cap S^1$. The group $D=\widehat{L_{\mathrm{disc}}}$ is the compact
dual of the additive group with the discrete topology; its characters are
written additively, so $(d+d')(z)=d(z)d'(z)$. Put
$\psi_z(d)=d(z)$ and $(ad)(z)=d(az)$. The subgroup $C\subset D$ consists
of the ordinary continuous characters
$j(\xi)(z)=\exp(i\xi\cdot z)$, $\xi\in\mathbb R^2$. A rotation-invariant
probability law is called wild when it gives $C$ measure zero. These
definitions impose no regularity on the original coloring.

## Premises and verification order

The dependency examination on 2026-10-17 found no native L-claim used as an
established premise. No live ledger standing was imported. In particular,
R0 is not assumed: its needed conclusion is obtained from the supplied
rigidity proof and the spectral characterization of continuous vectors.
The source card and any external formalization supply no warrant for that
proof. There is no pending native premise grade on which this report's
mathematical verdict is conditioned.

An acyclic order for the consumed deductions is:

1. finite forcing, elementary field facts, continuous-vector facts and the
   classical external interfaces;
2. the finite-cover theorem, its template conversion, and source Lemmas
   2.4--2.7 and 3.1--3.5;
3. the extended Haar-rigidity theorem and its pair-correlation corollary;
4. the binary transfer to a Borel weak avoider;
5. the independent measurable exclusion, using finite forcing, the Bessel
   argument and the circle argument;
6. rescaling and the conclusion for all triangle shapes.

The measurable exclusion does not use the arbitrary-coloring conclusion.
The reverse transfer uses density points and compactness, not rigidity.
The exact-carrier converse uses that compactness mechanism, not a conclusion
obtained from the carrier converse itself. These observations remove apparent
cycles created by the cross-references.

### Source interfaces and reading depth

**OpenAI manuscript.** The edition is the September 23, 2026 OpenAI Math
Release, identified by the supplied bibliographic excerpt. Its retained
Sections 2 and 3 were examined as proof, including the source lemmas used by
the field extension. The required Section 4 interfaces were also examined:
continuous vectors are a spectral subspace and, for Koopman operators, a
factor; an invariant law exists on a closed labeling space. The binary
sampling argument was checked directly in the native proof. No result from
the rest of the manuscript is a premise. The references to Crum and
Gneiting--Sasvári are contextual analogues, not a substitute for rigidity.
The named Furstenberg--Zimmer literature is background to the supplied
compact-tower proof; that proof is checked here instead of being assumed.

**Finite forcing.** The supplied source is Jelínek, Kynčl, Stolař and Valla,
arXiv:math/0701940v1, January 31, 2007. The later Combinatorica citation does
not turn this into an inspection of the published edition. The exact
interfaces are Lemma 1.3(i), from an equilateral triangle to any triangle
having that side, and Lemma 1.3(ii), from a triangle to an equilateral triangle
having one of its sides. The supplied source proof and the independent
coordinate reconstruction were checked, including positive side lengths,
collinear triples, direct motions and the measure version. Corollary 1.4's
relevant implications follow from those two finite statements.

**Finite perimeter.** The edition is Lahti, *Federer's characterization of
sets of finite perimeter in metric spaces*, arXiv:1804.11216v1, April 27,
2018. Theorem 1.1 applies to a measurable set $E$ in an open subset $\Omega$
of a complete metric space with a doubling Borel regular measure and a
$(1,1)$-Poincaré inequality. Finite codimension-one measure of
$\partial^*E\cap\Omega$ implies finite perimeter there. Formula (2.3)
defines this boundary using positive upper density of both sets; formula
(2.4) represents perimeter on that boundary, and (2.2) is the relative
isoperimetric inequality. The specialization here is ordinary $\mathbb R^2$
with Lebesgue measure: the space is complete and has at least two points,
the measure is Borel regular and finite and positive on balls, its doubling
constant is four, and the $(1,1)$-Poincaré inequality holds. The boundary will
be empty, so no normalization of Hausdorff measure affects the conclusion.
The exact statements and specialization were checked; Lahti's original
proofs, Federer's theorem and the standard BV theory behind them remain
explicit external theorem boundaries. They were not independently rebuilt.

The remaining external boundaries are standard classical facts, used at the
following strengths:

| Boundary | Exact use and hypothesis match |
| --- | --- |
| Real-closed transfer | A real-closed subfield of $\mathbb R$ is an elementary substructure in the ordered-field language; only finite polynomial systems with parameters in that subfield are transferred. |
| Compactness and linear algebra | Product compactness for finitely satisfiable finite coloring constraints; König's lemma for a finitely branching tree; extension of a linear functional after finite linear consistency. No compactness of the discrete coefficient field is asserted. |
| Amenability | Countable abelian groups, their extensions, invariant means and finite-set Følner sequences. The labeling action is continuous on a compact metrizable space, so averaged point masses have invariant probability limits. |
| Spectral theorem and Bochner | The spectral theorem is applied to a countable **discrete** abelian group. Bochner is applied only after extending a continuous positive-definite coefficient to $\mathbb R$ or $\mathbb R^2$. The usual topology on the carrier is not incorrectly treated as locally compact. |
| Fourier uniqueness | Finite measures on the compact dual are determined by character coefficients, by the separating conjugation-closed character algebra and Stone--Weierstrass. |
| Standard probability theory | Disintegration for standard Borel models and ergodic decomposition for a countable acting group. Countability permits simultaneous equivariance on a conull set. |
| Hilbert-space facts | Spectral calculus for bounded positive operators, fiberwise Gram--Schmidt, separability, conditional expectation and strong mean ergodicity. The every-Følner form needed here is derived in the supplied argument. |
| Measure and Fourier analysis | Lebesgue density, Fubini--Tonelli, translation continuity in $L^1$, the area formula for a smooth map on the torus, Plancherel, and zero variation implying a constant indicator on connected Euclidean space. |
| Bessel facts | The defining power series, its differentiated identities and differential equation, decay of $J_0(t)$ at infinity, and the Dirichlet Wirtinger inequality. The particular inequalities and their analytic assembly are checked below. |
| Cyclotomic facts | The primitive-root conjugates of $2\cos(2\pi k/m)$, their Ramanujan sum and Euler's totient. The resulting classification is derived below, not inferred from finite numerical searches. |

Original proofs of these classical boundaries were not recursively reviewed.
Their use is explicit and their hypotheses were checked. This is not an
inspection of unavailable external pages.

The supplied bibliography locates the spectral theorem and Bochner theorem
in Bekka, de la Harpe and Valette, *Kazhdan's Property (T)*, author manuscript
of February 23, 2007, D.3.1 and D.2.2; the amenability and Følner interfaces
are G.2.1, G.2.2(ii) and G.5.1. The supplied disintegration reference is Tao,
*254A, Lecture 9: Ergodicity*, February 4, 2008, Theorem 4 and Remark 5.
For the Bessel interfaces the named locations are DLMF 10.2.2, 10.2.1 and
10.17.3. These are source locators supplied with the argument; their external
pages were not inspected. The classical statements and their exact uses,
rather than any claim of external-source inspection, are the boundaries
listed above.

The two-element template Proposition 7 and the separate conditional arbitrary
coloring route in spectral Theorem 3 are not needed as independent acceptance
goals: the all-finite template proof and binary transfer supply the main
route. Their supplied text was read. The definitions and representation
conventions used from the latter were checked. Likewise, the manuscript's
full proper-unit-distance-coloring conclusion is not a premise of this
triangle argument.

## Weakest step 1: finite covers and the rational template

The main algebraic attack was that the algebra spanned by units need not be
finite dimensional or finitely generated over the algebraic numbers. A
finite-dimensional conclusion cannot simply be imported from the original
number-field argument. The supplied proof instead obtains a finite quotient;
the following checks account for that distinction.

Fix transcendental $x$. Write $E$ for the complex algebraic numbers and $F$
for the real algebraic numbers. If a normalized $E$-linear functional
$\lambda$ and a finite nonempty $Q\subset K_L$ supplied the asserted cover,
choose a finite conjugation-stable extension $N/E(x)$ containing $Q$, and
restrict $\lambda$ to $N$. Its fixed real
field $N_0$ satisfies $N=N_0(i)$ and is finite over $F(x)$. For
$T=(x+i)/(x-i)$, the field $B=E(T)$ is $E(x)$, $T$ is transcendental and
unit, and $d=[N:B]$ is finite. Set $A=\operatorname{span}_E K_N$.
This is an algebra: products and inverses of the spanning units remain units.
It contains $T,T^{-1},1,Q$ and is stable under conjugation. It is not being
asserted that $A=N$ or that $A$ is finitely generated.

For the needed general position over $B$, parameterize units by
$(1+iz)/(1-iz)$, $z\in N_0$. In an $F(x)$-basis of $N_0$, inversion gives
rational coordinates over $B$ with denominators nonzero on the real parameter
grid. If a $B$-linear functional killed every such unit, substitute $z=ha$.
The constant and linear coefficients in $h$ give its vanishing on $1$ and
$ia$ for every $a\in N_0$. Since $i\in B$ and $N_0$ spans $N$ over $B$,
that functional is zero. A finite union of proper $B$-subspaces therefore
cannot contain all the units: multiply the nonzero numerator polynomials and
use the infinite grid $F(x)^d$. One can include $1$ in a unit basis and choose
$n>J(d-1)$ units $s_k$ with every $d$ independent.

This gives fixed rows $r_{jk}(T)$ satisfying
$q_js_k=\sum_\ell r_{jk\ell}(T)b_\ell$, with every $d$ rows for a fixed $j$
invertible. For $a\in E$, define
$F_\lambda(a)_\ell=\lambda(b_\ell/(T-a))$. The divided difference of a
rational function separates into a finite sum of functions of $T$ times
functions of $a$. Thus

$$
\lambda\!\left(\frac{q_js_k}{T-a}\right)
 =r_{jk}(a)F_\lambda(a)+D_{jk}(a),
$$

where the rational coefficients in $D_{jk}$ are fixed and its only variable
data are finitely many values of $\lambda$. This uses $a\in E$, the scalar
field of $\lambda$; it does not pull a transcendental parameter through an
$E$-linear functional.

The parameter condition $b=1/\bar a$, $a\ne0$, $|a|\ne1$ does not reduce
the relevant Zariski dimension. The rational substitution
$a=s+it$, $b=1/(s-it)$ has a rational inverse on an open subset, and the
allowed grid $(s,t)\in F^2$ is Zariski dense over $E$. Removing the conditions
$s^2+t^2=0,1$ and finitely many poles leaves a dense set. Moreover,
$a(T-b)/(T-a)$ has norm one. The cover can therefore be applied to
$s_k(T-b)/(T-a)$ after removing its nonzero algebraic scalar.

Pigeonholing the $n$ equations yields finitely many rational branches

$$
F_\lambda(a)=R_\beta(a)+\frac{S_\beta(a)}{a-b}.
$$

The branch partition can be arbitrary. Only branches whose Zariski closure is
the full parameter plane are used for identities. For one such branch, take
two parameter pairs and put $h=a-b$, $k=c-e$. Products of the two scalar
multiples of units still admit the cover. For each fixed $s_k$ (with this
subscript now just a row index), one of finitely many factors has the form

$$
L+hH(a)+kH(c)+\frac{hk}{a-c}(H(a)-H(c))=0,
\qquad H(a)=V(a)+W(a)/h.
$$

The product of those factors vanishes on the Cartesian square of a dense
branch, which is dense in four variables. A rational-function field has no
zero divisors, so one factor is identically zero. In the independent
variables $a,c,h,k$, its coefficients are

$$
\begin{array}{c|c}
hk&(V(a)-V(c))/(a-c)\\
h&V(a)-W(c)/(a-c)\\
k&V(c)+W(a)/(a-c)\\
1&L+W(a)+W(c).
\end{array}
$$

The first makes $V$ constant; varying $a$ in the second then forces that
constant and $W$ to vanish. The last gives $L=0$. For each row index there is
therefore a $j$ with $r_{jk}S_\beta=0$. Another pigeonhole and an invertible
$d$-row matrix give $S_\beta=0$. Taking one pair from each of two dense
branches similarly gives $R_\beta=R_\gamma$. Finite unions of proper closed
subsets cannot cover an irreducible plane, so a dense branch exists; the
nondense branches lie in a single proper exceptional algebraic set.

This proves generic rationality of the transform. It also proves the stronger
uniform fact actually needed: all its possible rational vectors lie in one
finite-dimensional space $W$. The finitely many row inverses and rational
functions in the divided differences are fixed before $\lambda$ varies.
Consequently $W$ has bounded polynomial degree at infinity and bounded pole
orders. This remains true for unnormalized translated functionals
$\lambda_v(z)=\lambda(vz)$, $v\in K_N$.

For such $v$, let $\Phi(v)=R_{\lambda_v}$. A finite linear relation among
units holds for their exact transforms at every parameter. Intersecting the
finitely many generic parameter sets shows that it holds for their rational
vectors. Hence $\Phi$ extends linearly to $A$. Direct multiplication by $T$
gives

$$
\Phi(Tv)(a)=a\Phi(v)(a)+\Lambda(v),
\qquad \Lambda(v)_\ell=\lambda(vb_\ell).
$$

If $\Phi(v)$ had a nonzero polynomial part of degree $q\ge0$, the leading
polynomial degree of $a^m\Phi(v)$ would be $m+q$. The accumulated correction
terms have degree at most $m-1$, including the polynomial terms arising from
the strictly proper part. They cannot cancel that leading term. This
contradicts the degree bound in $W$. Every $\Phi(v)$ is therefore strictly
proper. Comparing the constant term in the one-step identity recovers
$\Lambda(v)$ as minus the coefficient of $a^{-1}$. In particular, $\ker\Phi$
is stable under multiplication by $T$. An annihilating polynomial of the
induced operator on $\Phi(A)$ gives

$$
\lambda(p(T)v)=0\qquad(v\in A).
$$

The finite-quotient argument does not require a Noetherian hypothesis. For
any $d+1$ elements of $A$, take a dependence over $E(T)$, clear denominators
and remove the greatest common power of $T-a$ from its polynomial
coefficients. At least one coefficient is nonzero at $a$. Reduction modulo
$(T-a)A$ is consequently a nontrivial $E$-linear dependence. Thus
$\dim_E A/(T-a)A\le d$. Each successive layer for $(T-a)^m$ is a quotient
of this space. Bézout identities in $E[T]\subset A$ and the Chinese
remainder theorem then give

$$
\dim_E A/p(T)A\le d\deg p.
$$

If $p$ is constant or this quotient is zero, the descended functional already
contradicts $\lambda(1)=1$. Otherwise, real elements of $A$ span its quotient:
use $(z+\bar z)/2$ and $(z-\bar z)/(2i)$. Choose real $z_i$ whose images
span it. For real algebraic parameters $t_i$, the Cayley transform of
$z(t)=\sum t_i z_i$ belongs to $K_N$, and

$$
(1-iz(t))^{-1}=\frac{1+(1+iz(t))/(1-iz(t))}{2}\in A.
$$

Its denominator remains invertible in the quotient. The cover is now a
product of ordinary rational functions on the finite parameter space, zero
on the infinite real algebraic grid. One factor vanishes identically.
Differentiating it at zero gives $\lambda(q_jz_i)=0$ for all $i$.
Since $q_j$ is a unit and the images of the $z_i$ span, the functional is
zero, contradicting its normalization. The finite-cover attack fails.

Finally, the conversion to the **rational** template has two actual steps.
If no finite algebraic-coefficient template exists, the consistent selector
choices on finite initial segments of the countable unit group form an
infinite finitely branching tree. An infinite branch has $1$ outside the
span of all selected vectors: any offending finite relation would already
occur on an initial segment. Define a functional to be one on $1$ and zero
on that span, and extend linearly. It gives exactly the forbidden finite
cover. This avoids any false compactness assertion about $E$ itself.

For the finite algebraic template obtained this way, there are only finitely
many selectors and finitely many coefficients expressing $1$ and $i$.
Put them in one conjugation-stable number field $N_0(i)$. Source Lemma 3.4
supplies rational general position by the following checked argument. A
rational linear functional vanishing on every Cayley unit has, along
$t=ha$, coefficients zero on $1$, $ia$ and $a^2$. The identity
$4a=(a+1)^2-(a-1)^2$ shows that squares span $N_0$, so the functional is
zero on all of $N_0(i)$. The product of the nonzero numerator polynomials
for a finite collection of proper rational subspaces cannot vanish on the
entire rational parameter grid. Successive choices outside these subspaces
give more than $J([N_0(i):\mathbb Q]-1)$ units in rational general position.
Pigeonholing separately in each block of the enlarged
template makes its rational span contain the required algebraic-coefficient
span. Overlaps between blocks only constrain the selector further and do
not invalidate this argument. For algebraic $x$ the same number-field
argument applies directly. No finite number field containing transcendental
cover rotations is asserted.

The span assertion in Proposition 8 has no additional field hypothesis.
For real $a\in F_x$, choose a positive integer $n>|a|$. Then
$u=a/n+i\sqrt{1-(a/n)^2}$ is a unit and
$a=(n/2)(u+\bar u)$. Multiplication by $i$ deals with the imaginary part,
so units span $L$ even over $\mathbb Q$. Given a syndetic set of rotations,
apply the template to a finite covering family and multiply its relation for
$1$ by any chosen unit $v$. The selected products lie in that syndetic set,
so its span contains $v$, and therefore $L$. A normalized functional's
kernel cannot have this span. This checks the other stated implications of
Proposition 8 as well as the implication needed for the proof.

## Weakest step 2: conditional singularity and averaging

The measure-theoretic attack was to let conditioning turn a wild law into
one supported on finitely many ordinary-character cosets, thereby destroying
the rigidity deduction. The proof must rule this out at each stage of the
tower, not merely for independent unconditioned samples.

The preliminary null statements have the needed scope. A positive-mass
$C$-coset has a finite orbit under the rotation group. A finite image of a
divisible abelian group is trivial, so $(u-1)d\in C$ for any $u\ne1$.
Invertibility of the nonzero scalar $u-1$ then puts $d$ in $C$, impossible
for a wild law. Likewise, continuity on two nonparallel $F_x$-lines implies
ordinary continuity on the plane. Infinitely many rotated line events,
pairwise disjoint modulo $C$, each have measure zero.

The line mean uses no ordinary measurability of the Fourier coefficient.
Periodization followed by an invariant mean on $F_x/\mathbb Z$ gives a
positive translation-invariant $I$ on bounded functions of bounded support.
Ordinary circle characters and trigonometric approximation show agreement
with Lebesgue integration on continuous compactly supported functions. A
continuous vector for multiplication by $\psi_{at}$ would have a continuous
positive-definite coefficient extending to $\mathbb R$. Bochner and Fourier
uniqueness would put its spectral mass on the null continuous-line event,
so it is zero. The weak Hilbert integral
$I(\phi(t)\psi_{at})$ is a continuous vector: translation changes it by a
norm at most $\int|\phi(t-s)-\phi(t)|\,dt$. It therefore vanishes. This
proves the line-average statement on precisely the nonmeasurable coefficient
functions later used.

Assume now a first tower stage $Y$ has a conditional difference law giving
$C$ positive mass. The conditional coset mass evaluated at a sample is an
invariant function on the original ergodic system. It is a positive constant
$a$. Consequently almost every conditional law consists of exactly $m=1/a$
cosets of mass $1/m$. Any remaining nonatomic mass over cosets would give a
sampled coset mass zero and contradict constancy.

The center construction is valid even when $C$ is not closed. The function
$\kappa_y(z+C)$ is Borel by parameter integration. On a positive-mass coset,
push its normalized conditional law into $\mathbb R^2$ using the Borel
inverse of the ordinary-character parametrization. The objective

$$
\int\left(\sqrt{1+|s-t|^2}-\sqrt{1+|t|^2}\right)d\lambda(t)
$$

is finite, since its integrand is bounded by $|s|$; is strictly convex;
and is coercive after choosing a ball of mass greater than one half.
Rational approximate minimizers yield a Borel unique minimizer. Translation
and orthogonal covariance make the resulting center independent of the
representative chosen in the coset. Thus one obtains an equivariant factor
$Z$ with a wild center map $b$ and, over $Y$, a uniform law on $m$ centers.
There is no appeal to a measurable selector for an arbitrary quotient by $C$.

Encode the unordered $m$ phases at frequency $1$ by their elementary
symmetric functions. Newton identities make this encoding measurable, and
compactness gives uniform continuity of its inverse for the matching metric,
including repeated phases. Rotating the encoding gives the phase list at
frequency $k$.

The following quantifier order is essential and is respected. Choose a phase
tolerance $\rho$, then a finite moment test $N,c$ that makes conditional
probability of $|z-1|\le4\rho$ smaller than $1/(4m^2)$. Such a test follows
by uniformly approximating a continuous majorant of that arc by a
trigonometric polynomial. Next choose the encoding tolerance $s$, put
$\tau=s/100$, and choose $\gamma$ so that
$2\gamma^2/\tau^2<10^{-4}$. Compact approximation returns finitely many
bounded basis functions with bounded coefficients over an **earlier**
factor $W$. At a limit stage, approximate on an earlier successor first.
Fix the finite number $L$ of coefficient bins, and only then choose
$M$ with $0.9M/L>10m^2$.

Universal induction applies to the new ambient system $Z$, its map $b$ and
the unchanged earlier tower through $W$. Thus its relative difference law
over $W$ is wild. Its coefficient

$$
p(a)=\left\|\mathbb E(\psi_a(b)\mid W)\right\|_2^2
$$

is nonnegative and has zero line mean against every continuous test. A finite
sum of the tests $p(n(j-l)t)$, with $1\le n\le N$ and distinct
$j,l\in\{1,\ldots,M\}$, also has zero mean. Positivity of $I$ then selects
one $0<|t|<1/M$ making all these quantities as small as prescribed.
This uses only finitely many tests, so no countable additivity of the
invariant mean is smuggled in. Taking the prescribed bound below one excludes
$t=0$.

Put $x_j=jt$. Markov's inequality and the finite union bound make all distinct
pair collision probabilities smaller than $1/(4m^2)$ on a set of $W$-fibers
of probability greater than $0.99$. Write

$$
x_j=k_j+k'_j,\qquad
k_j=x_j/2+i\sqrt{1-x_j^2/4},\quad k'_j=\overline{k_j}.
$$

The square roots are in $F_x$. The previously fixed compact approximations
apply to both lists of rotations. Their global squared errors are less than
$\gamma^2$. The probability that at least $0.1M$ indices have one conditional
error at least $\tau$ is at most $20\gamma^2/\tau^2<0.001$.
Choose a fiber on which this estimate and every collision bound hold.
One coefficient bin contains a set $J$ of more than $10m^2$ good indices.
Two errors and the bin diameter give conditional distance at most $3\tau$
from a representative list for each sign. Markov and a union bound show
that the expected fraction $q$ of indices whose two lists match within
$\rho$ exceeds $0.95$.

For any one center in a fiber over $Y$, each matched phase at $x_j$ is within
$2\rho$ of one of at most $m^2$ products of entries of the two representative
lists. The two matchings need not select the same center; that is precisely
why the bound is $m^2$, not $m$. Pigeonholing these products gives the lower
bound

$$
\frac{\mathbb E(q^2\mid W)}{m^2}-\frac1{|J|}
\ >\ \frac{0.95^2-0.1}{m^2}
\ >\ \frac1{4m^2}
$$

for the collision probability of two distinct random indices in $J$.
The earlier simultaneous pair bounds give a strictly smaller upper bound.
Choosing $J$ after the fiber causes no loss: those bounds held for every
pair in the original finite index set on that fiber. This is the required
contradiction and completes the universal induction.

The other source steps cannot be assumed merely from the word “compact.”
For Lemma 3.1, a nonconstant invariant bounded kernel on a nonergodic relative
product has constant coordinate expectations. Subtracting that constant gives
a nonzero Hilbert--Schmidt operator field annihilating constants. A fixed
positive spectral cutoff gives a finite-rank equivariant projection; its rank
is a positive constant by ergodicity of the factor. Projecting a countable
family of measurable dense sections and applying fiberwise Gram--Schmidt
produces a measurable orthonormal basis $e_1,\ldots,e_d$. Spectral cutoff
measurability follows from bounded polynomial approximation and strong
spectral calculus, not from a continuous eigenvector choice.

The function $\sum|e_i|^2$ is invariant on the original ergodic system and
has integral $d$, so it equals $d$ almost everywhere. The basis is bounded.
Adjoining it makes a strict factor extension because its conditional means
are zero and its fiber norms are one. Bounded polynomials in these functions
and their conjugates are dense over the old factor. Under rotation their
coefficients change by unitary matrices with uniformly bounded entries. This
proves the required finite compact approximation. If the tower continued
through every countable ordinal, choosing a unit vector in each new factor
orthogonal to the preceding factor would produce uncountably many mutually
orthogonal vectors in a separable Hilbert space. Termination at a countable
ordinal is proved, not assumed.

For Lemma 3.2, conditional independence turns the squared error in a pair
correlation into an ordinary correlation on $\mathcal R=X\times_YX$ of
centered tensors. The mean ergodic theorem on this ergodic relative product
makes its every-Følner average zero. Surjectivity of each nonzero power map
ensures the same invariant vectors for the powered action. The pair
criterion passes to $\mathcal R$ over $Y$ by multiplying the two conditional
pair correlations for simple tensors. Bounded rectangle-partition
approximations extend it to all bounded functions.

In the multiple-average induction, subtract one exponent and expand the
shifted factors into their conditional means and centered parts. The lower
order induction eliminates each centered term. The remaining scalar
correlation is bounded by
$a(h)=\|P(U_{h^{n_*}}v_*\overline{v_*})\|_2$, whose squared averages
vanish by the pair criterion. The van der Corput step needs uniformity over
translates of its finite shift sets. This follows here from the **every**
Følner conclusion: a sequence of bad translates of a subsequence would itself
be Følner in the abelian group and contradict that conclusion. The limits
are taken first over the original averaging sets for a fixed finite shift
set and then over the shift sets. Finally, conditional independence again
turns the projected squared norm into a scalar integral on $\mathcal R$.
Adding a common integer to all exponents inside that integral makes them
nonzero without changing it. This justifies the final application of the
induction even when an original exponent was zero.

The specialization from algebraic numbers to $F_x(i)$ uses only the field
facts listed above: countability, real closedness, density, divisibility,
nonparallel real-line coordinates, and the displayed square roots. The
finite-number-field selection is the one place that requires replacement,
and Weakest step 1 supplies it. No extra algebraicity of $x$ is used in the
conditional collision or averaging arguments.

## Weakest step 3: preserving avoidance through a measurable sample

A projection of a coloring usually destroys a hyperedge constraint. The
specific protection here is preservation of every **nonzero pair**
correlation, followed by a nonnegative identity specific to three points and
two colors. Both parts are necessary.

First, the continuous-vector space of a representation of the discrete
carrier is exactly its spectral subspace on $C$. Spectral mass on $C$ gives
continuity by dominated convergence. Conversely, a continuous vector's
coefficient is uniformly continuous on the dense carrier, extends to a
continuous positive-definite coefficient on $\mathbb R^2$, and is represented
there by Bochner. Push that measure to the compact dual and use Fourier
uniqueness. This gives the claimed spectral support even though $C$ is not
closed. For a rotation-fixed vector the spectral measure is invariant under
$K_x$. Its restriction to $C^c$, after normalization if nonzero, is Haar by
the proved rigidity statement. The cross terms between the two spectral
subspaces vanish. Haar's coefficient at every nonzero displacement is zero,
which proves Corollary 3. The value at displacement zero is not preserved
and is not needed.

Now restrict an arbitrary avoiding coloring to $L=F_x(i)$. Its orbit lies
in the nonempty closed space of labelings avoiding the two specified
triangles. The countable amenable group $L\rtimes K_x$ preserves this
space. A limit of Følner averages of a point mass gives an invariant Borel
probability. The original coloring need not be measurable: only this compact
labeling space is integrated. The origin sign $f$ is rotation fixed.

For these Koopman translations, continuous vectors form a factor. Products
of bounded continuous vectors are continuous in $L^2$; so are conjugation and
Lipschitz compositions. Indicators lying in the subspace form a sigma-algebra,
using finite unions and closedness for increasing unions. Threshold
approximations to a real continuous vector show it is measurable for this
sigma-algebra. Conversely its simple functions are continuous vectors and
are dense in the factor's $L^2$. Thus projection is conditional expectation,
not an arbitrary positive-looking spectral map. In particular $g=Pf$ is real
and satisfies $-1\le g\le1$.

Translations of $g$ extend to all of $\mathbb C$ by $L^2$ limits from the
dense carrier. The group law and unitarity follow from these limits; the
interval bounds survive because they are closed $L^2$ conditions. The proof
does not require a pointwise action of the uncountable real-plane group.
Its coefficient $\kappa(y)=\langle g,T_yg\rangle$ is continuous.

For a triangle $(0,a,b)$ of distinct points, the three displacements
$a,b,b-a$ are nonzero, including for collinear triples. The exact sign
identity on the original avoiding-labeling space and Corollary 3 give

$$
1+\kappa(ua)+\kappa(ub)+\kappa(u(b-a))=0
\qquad(u\in K_x).
$$

Density extends this equality to every $u\in S^1$. The constant term here
is the number $1$, coming from a probability measure, not $\|g\|_2^2$.
There is no illicit replacement of the discarded zero-displacement
correlation.

For $a_1,a_2,a_3\in[-1,1]$,

$$
1+a_1a_2+a_1a_3+a_2a_3
 =\frac{\prod(1+a_i)+\prod(1-a_i)}2\ge0.
$$

Both products must vanish for equality. Thus one coordinate is exactly
$-1$ and another exactly $1$. For any fixed placement, the integral of this
nonnegative expression in the three translated $g$'s is zero by the
coefficient identity. It therefore vanishes almost surely for that placement.
This is an actual constraint on the three values, not merely a negative
average that is supposed to survive arbitrary rounding.

The remaining uncountable-null-set issue is handled explicitly. Choose Borel
maps $q_n:\mathbb C\to L$ with countable ranges so that
$\|T_{q_n(y)}g-T_yg\|_2\le2^{-n}$ uniformly in $y$. This is possible because
the orbit is uniformly continuous and $L$ is dense. Bounded Borel versions of
the countably many translates give jointly Borel fields $G_n$. For each
fixed $y$, the sum of the $L^1$ norms of successive differences is finite,
so $G_n(y,\cdot)$ converges almost surely to a representative of $T_yg$.
Define its limit where it exists and zero elsewhere. This is one jointly
Borel field $G$, with values in $[-1,1]$. Its exceptional sample set is
allowed to depend on $y$.

Apply Tonelli to the nonnegative three-point expression on each bounded
spatial disk times $S^1$ times the probability space. Each parameter section
has integral zero, so there is a conull set of samples on which the spatial
integral is zero. The family of disks and the family of triangle templates
are countable. One sample satisfies all of them. Thresholding that sample
at zero preserves its occurrences of both endpoint signs and gives a Borel
weak avoider. No common exceptional set for all real-plane points has been
assumed.

The reverse transfer is also sound at its stated weaker output. If three
points of a template were density-one points of one color, randomizing its
translation in a disk of radius $h$ and its rotation in an arc of size
proportional to $h/(1+|a|+|b|)$ puts each other vertex in a disk of radius
$2h$ with density at most $1/(\pi h^2)$. The probability of a monochromatic
copy tends to one, contradicting weak avoidance. Hence the two density
classes, which cover a conull set, have no such exact copy. Every finite
point set has a translate inside that conull set. Finite-constraint product
compactness gives an arbitrary avoiding coloring of the whole plane. It does
not assert a measurable completion on the omitted null set.

## Remaining essential interfaces and conclusions

### Fields, the exact carrier and radial completion

For a fixed real $x$, $\mathbb Q(x)$ and its algebraic closure are countable.
The real closure $F_x$ inside $\mathbb R$ is dense and real closed, and
$L=F_x(i)$ is algebraically closed. It contains the complex algebraic numbers
and the placed triangles of sides $1,x$. For transcendental $x$ it is also
the algebraic closure of $E(x)$ inside $\mathbb C$. A complex root of a unit
in $L$ is still a unit, proving divisibility of $K_x$. Rational
half-angle parameters give its usual density in $S^1$. Nonparallel
$a,b\in L$ form an $F_x$-basis, and every $t\in F_x\cap[-1,1]$ is a real
part of a unit. These are the field facts actually consumed.

The frequency map $j$ is continuous and injective, since $L$ is dense in the
plane. Its image $C$ is a countable union of compact images of closed balls,
and the inverse on each compact image is continuous. Thus $C$ and $j^{-1}$
are Borel without any assertion that $C$ is closed. Scalar multiplication
by a nonzero element of $L$ preserves $C$; on frequency parameters it acts
by the transpose real-linear map, which is orthogonal for elements of $K_x$.

The exact-carrier converse is not an approximation by nearby triangles.
For a finite plane point set, list every relevant equilateral triple and
write its orientation equation and its exact squared length equation with
parameters $x,\sqrt3$. Elementary transfer to $F_x$ realizes all those
equations simultaneously. Each listed triangle retains three distinct
vertices because its side is positive. Other vertices may coincide; pulling
a coloring back along this map still satisfies every listed nonmonochromatic
constraint. No injective embedding or preservation of nonedges is needed.
Finite compactness then gives a whole-plane coloring. This establishes the
claimed equivalence at every real $x$.

For the completion of rigidity, let $g_z$ be the conditional character at the
terminal factor and $m(z)=\|g_z\|_2^2$. Conditional independence identifies
$m$ as the Fourier transform of its wild relative difference law. Equal
moduli differ by a rotation in $K_x$, so $m$ is radial on $F_x$, is
nonnegative, and equals one at zero.

The polynomial identity

$$
|A-Bu^2|^2
 =(A-B)^2+4AB(\operatorname{Im}u)^2
 =| -\sqrt{AB}+(A-B)u+\sqrt{AB}u^2|^2
$$

uses only $\sqrt{AB}\in F_x$. Conditional multiple averaging on the first
expression gives limit $m(A)m(B)$. On the second, the two outside conditional
characters have modulus at most one, leaving an upper bound $m(|A-B|)$.
Thus $w=-\log m$ satisfies
$w(|A-B|)\le w(A)+w(B)$, with the stated infinity convention when a factor
vanishes. The cases $A=0$ or $B=0$ are identities. Applying the same argument
to $ru+r\bar u$ gives the every-Følner average

$$
\operatorname{Avg}_u m(2r|\operatorname{Re}u|)\longrightarrow m(r)^2.
$$

If $m(r)>0$, choose $H$ with $e^{-H}<m(r)^2$. The rotations for which
$w(2r|\operatorname{Re}u|)\le H$ are syndetic. Otherwise translated
Følner sets could be chosen entirely outside them; their averages would be
at most $e^{-H}$, contradicting the every-sequence identity. Positivity along
one preselected averaging sequence would not suffice; the proved stronger
quantifier does.

The rational template makes finitely many possible selections, each spanning
$1$ and $i$. Clearing denominators gives a common positive integer $D_0$
and a bound $M_0$ on the coefficient length expressing $D_0$. The presence
of both $1$ and $i$ makes
$\max_k|\operatorname{Re}(kv)|$ positive for every ordinary unit $v$.
Compactness of $S^1$ and the finite number of selections give a common
$c_0>0$. None of these constants is claimed uniform in $x$ or the cover.

The bounded-residue lemma has no hidden convergence step. Keep partial signed
sums of lengths $p_k\le p$ in $[0,p)$. A negative input has cost at most
$2H$ by replacing it by $p-p_k$. If two residues sum below $p$, two
applications involving $p$ bound the new cost by the old two costs plus
$2H$; if they sum above $p$, one replacement by $p-b$ costs at most $H$;
if they sum to $p$, the residue is zero. Adding at most $M_0$ signed inputs
therefore costs at most $4M_0H$.

Taking real parts of the rational selection relation consequently bounds
$w(2rD_0|\operatorname{Re}v|)$ by $4M_0H$ whenever that argument is below
the selection's maximal length. Real closedness realizes every required real
part, giving

$$
m(s)\ge e^{-4M_0H}\qquad(s\in F_x,\ 0<s<2rc_0).
$$

A nonnegative continuous test function supported inside that interval has a
positive $I$-integral against $m$, contrary to the wild line-average lemma.
Thus $m$ vanishes off zero. Since $|\widehat\mu(z)|\le\sqrt{m(z)}$, Fourier
uniqueness gives Haar in the ergodic case. Ergodic decomposition extends this
to arbitrary invariant wild laws; almost every component remains wild
because $C$ is invariant Borel. This completes the source specialization
needed by the pair-correlation argument.

### Finite forcing, orientations and degenerate triangles

Take $a>0$ and $z\ne0,a$. The eight points in the supplied reconstruction
are

$$
A=0,\quad B=a,\quad C=a\omega,\quad D=z,\qquad
B'=\omega z,\quad A'=a+\omega z,\quad
C'=a\bar\omega+\omega z,\quad D'=a-\bar\omega z.
$$

For the base ordered triple $(a,0,z)$, direct substitution in the six
motions gives exactly

$$
(B,A,D),\ (C,A,B'),\ (C,B,D'),\
(B',A',D'),\ (C',A',B),\ (C',B',D).
$$

Their multipliers are respectively
$1,\omega,-\bar\omega,-1,-\omega,\bar\omega$ and all have modulus one.
The translations are the listed $0,0,a,a+\omega z,a+\omega z,\omega z$.
The two equilateral triples of side $a$ have displacement pairs
$(a,a\omega)$ and $(-a,-a\omega)$; those of side $|z|$ have pairs
$(z,\omega z)$ and $(-z,-\omega z)$; those of side $|z-a|$ have pairs
$(z-a,\omega(z-a))$ and $(a-z,\omega(a-z))$. All are genuine positive-side
equilateral triangles. These equalities use
$1-\omega=\bar\omega$ and $\omega+\bar\omega=1$.
The respective pairs of triples are $(A,B,C),(A',B',C')$,
$(A,D,B'),(A',D',B)$, and $(B,D,C'),(B',D',C)$.

Starting with $A,B,C$ of one color and forbidding the six target copies
forces $D,B',D'$ to the other color, then $A'$ back, then $C'$ to the
other color. The last target triple is monochromatic. Starting instead
with $B,A,D$ of one color and forbidding the six equilateral triples forces
$B',C,C'$ to the other color, then $A'$ back, then $D'$ to the other color;
the last equilateral triple is monochromatic. Coincident points in different
listed triples can only contradict a forced color earlier. Each individual
triple remains distinct by the displacement formulas. In particular there
is no missing case when $z$ is real, including $z$ outside the segment
$[0,a]$.

The positive-measure deduction is also exact. For a fixed motion
$h=(t,v)$, right composition sends a placement $(p,u)$ to
$(p+ut,uv)$. In local angle coordinates its Jacobian is block triangular
with identity on the two translation coordinates and derivative one on the
angle coordinate. Its determinant is one. Hence this right composition
preserves area times arc length; no unsupported use of Haar invariance on an
arbitrary non-unimodular group is involved. A finite union of preimages of
null monochromatic-placement sets is null. The two forcing implications
therefore remain true with “occurs” replaced by “has positive measure.”

If a coloring missed two equilateral lengths $a<b$, a monochromatic triangle
with side lengths $(a,b,b)$ would contradict forcing (ii). Conversely, with
at most one equilateral length missing, any non-equilateral triangle has two
distinct side lengths, at least one present, and forcing (i) realizes the
chosen target. This proves the stated equivalence and the whole-conclusion
use of the source. It also handles reflection by choosing the target's
orientation before constructing the configuration.

### Bessel bounds and the wide-ratio exclusion

The finite arithmetic in the nine-row table was recomputed exactly by the
retained program. It evaluates the two Taylor polynomials by Horner's rule
in $q^2/4$ with rational coefficients, rather than calling a numerical Bessel
routine. All nine claimed strict enclosures held. The two energy margins
were respectively $15583/100000000$ and $3/62500$, both positive; the final
exclusion gap was exactly $1/375$.

The analytic justification was checked separately from the finite arithmetic.
For each listed $q\le10$, the ratio between successive absolute series
terms after index $21$ is at most
$100/(4\cdot22(22+\nu))<1$, and decreases afterward. Thus $S_{\nu,21}$
and $S_{\nu,20}$ really bracket $J_\nu(q)$, even though earlier terms need
not decrease. The analogous tail after degree three gives

$$
\frac{2J_1(t)}t\ge1-y/2+y^2/12-y^3/144>0,
\qquad y=t^2/4\le9/4,
$$

because the polynomial is decreasing and its value at $9/4$ is $223/1024$.
There is no positive zero of $J_1$ at most $3$.

For two successive positive zeros $a<b$, the function
$v(t)=\sqrt t J_1(t)$ satisfies
$v''+(1-3/(4t^2))v=0$. Integration by parts and Wirtinger yield
$(\pi/(b-a))^2<1$. The signs at $19/5$ and $4$ therefore locate the first
zero between them; an earlier zero would violate the spacing bound.
There can be no second zero before $24/5$, or third before $10$. Simplicity
of zeros follows from uniqueness for the differential equation. Thus the
minimum of $J_0$ on $[24/5,10]$ is at an endpoint: any intervening critical
point is the next local maximum, not a new minimum.

Differentiating gives

$$
\frac{d}{dt}(J_0(t)^2+J_1(t)^2)=-2J_1(t)^2/t.
$$

Together with the table this yields $J_0(t)>-403/1000$ globally,
$J_0(t)>-1/4$ for $t\ge24/5$, and $J_0(t)>-261/1000$ on $[0,3]$.
The energy is strictly decreasing between distinct positive arguments,
so the asserted global-minimum statement at the first zero of $J_1$ is
also justified.

For $x\ge3/2$, if either $t$ or $xt$ lies outside $(3,24/5)$, these bounds
give a sum greater than $-83/125$. Otherwise
$3<t<16/5<t_0<9/2<xt<24/5$. Monotonicity on both pieces and the table give
a sum greater than $-642/1000$. Taking the infimum proves
$m(x)\ge-83/125>-2/3$. The substitution $t\mapsto t/x$ gives the reciprocal
range. The closed endpoints $x=3/2$ and $x=2/3$ are included.

For a weak measurable avoider, cutoff to a disk gives a positive-definite
correlation with total spectral mass one by Plancherel. Angular averaging is
the Bessel transform. Comparing the cutoff pair integrals with the exact
three-sign identity loses only boundary bands of area $O(rR)$ for a fixed
side $r$. Translating the third pair changes the integration disk by another
such band. Thus the radial correlations at $1$ and $x$ tend to $-1/3$.
The constants may depend on the fixed side; the argument does not exchange a
limit with an unbounded family of sides.

Push the spectral measures to radii and compactify by one point at infinity.
Both Bessel test functions extend there by zero. The limit restricted to
finite radii has mass at most one, not necessarily one. For
$a=\min(m(x),0)$, its integral of the sum is at least its mass times $a$,
which is at least $a>-2/3$. This contradicts the sum $-2/3$ of the two limiting
correlations. Escape of mass is therefore accounted for rather than dropped.

### The central interval, circles and perimeter

Let $2/3<x<3/2$, $x\ne1$. Put
$A=\arcsin(x/2)$ and $B=\arcsin(1/(2x))$. They lie in $(0,\pi/2)$ and
$\sin A\sin B=1/4$. If both were rational multiples of $\pi$, then

$$
\alpha-\beta=1,\qquad
\alpha=2\cos(A-B),\quad\beta=2\cos(A+B).
$$

For a primitive root of order $m\ge3$, the average conjugate of its real
trace is $2\mu(m)/\varphi(m)$; for orders one and two it is respectively
$2,-2$. The only values of absolute value one are from orders three and
six. Among the remaining nonzero averages the absolute value is at most
one half, with equality only at orders five and ten. This follows also by
listing the possibilities with $\varphi(m)=4$: $5,8,10,12$, with the
nonsquarefree orders eight and twelve contributing zero.

Averaging $\alpha-\beta=1$ in a common cyclotomic field leaves only average
pairs $(2,1),(1,0),(0,-1),(-1,-2),(1/2,-1/2)$. In the third pair,
$\beta=-1$ itself, so the original relation forces $\alpha=0$; an average
zero alone would not justify this. The fourth pair forces $\beta=-2$.
The angle ranges exclude both cases. The other cases give, respectively,

$$
(A,B)=(\pi/6,\pi/6),\qquad
\{A,B\}=\{5\pi/12,\pi/12\},\qquad
\{A,B\}=\{3\pi/10,\pi/10\}.
$$

The resulting lengths are $1$, the golden ratio and its inverse, and
$2\sin(5\pi/12),2\sin(\pi/12)$. The larger member of each nontrivial
reciprocal pair exceeds $3/2$; hence the smaller is below $2/3$. Thus one
of the two chord angles $2A,2B$ is irrational relative to $\pi$. There is
no finite search over denominators in this argument.

The isosceles triangle having that angle has sides in $\{1,x\}$. Finite
forcing (ii) in its measure form makes it weakly avoided. Fix its leg length
$r$; this single radius is used at every boundary point.

For the red class let $S$ be the complement of the density-zero and
density-one points. Ball averages are continuous in the center; rational
radii suffice for their upper and lower limits. Consequently $S$ is Borel
and, by density differentiation, has area zero. It is precisely the boundary
where both colors have positive upper density, not a topological boundary.

The apex lemma uses a sequence of radii on which the apex color has density
at least some $\delta>0$. If the other two vertices were density-one points
of that color, perturb translation in a disk of radius $h$ and rotation
through an interval of size $h/r$. Each other vertex has probability of the
opposite color tending to zero: its distribution is bounded by
$1/(\pi h^2)$ and supported in the disk of radius $2h$ around its density
point. A union bound gives monochromatic probability at least
$\delta-o(1)>0$ along that sequence. This contradicts weak avoidance.
No conditioning on the apex being red, or independence of the three colors,
is required.

At a point $p\in S$, suppose its radius-$r$ circle met $S$ on an
arc-length-null set. The two density classes then partition the circle
modulo null sets. The apex lemma for the equilateral triangle forces each
color to alternate under angle $\pi/3$; their measures are both half the
circle. The isosceles triangle makes translation by its angle $\gamma$
interchange the same halves. Hence $1_R-1/2$ changes sign under $\pi/3$
and is invariant under $\gamma-\pi/3$.

An independent way to finish this circle step is by Fourier coefficients.
The sign change gives mean zero. Invariance under the irrational rotation
$\gamma-\pi/3$ makes every nonzero Fourier coefficient zero. Thus
$1_R-1/2=0$ in $L^2$, impossible for an indicator. This verifies the
closed-subgroup argument without substituting an averaged coloring for an
indicator. The supplied finer rational-angle condition also checks. Write
$\gamma=2\pi P/Q$ in lowest terms. After scaling angles by $\pi/3$,
membership of $\pi/3$ in the generated subgroup is equivalent to
$k(6P-Q)/Q$ being an odd integer. If $Q$ is odd, take $k=Q$; if $4$ divides
$Q$, take $k=Q/2$. Both give an odd integer. If $Q=2q$ with $q$ odd,
then $P$ is odd and $(6P-Q)/Q=(3P-q)/q$ has even numerator and odd
denominator even after reduction, so no integer multiple is odd. Thus the
condition is exactly $Q\not\equiv2\pmod4$.

It follows that every $p\in S$ has positive arc-length intersection of its
radius-$r$ circle with $S$. This is a stronger statement than the existence
of some exceptional center. Fixing one $p\in S$, the set of pairs of
successive angles landing twice in $S$ has positive two-dimensional measure
by Fubini; positivity at each first landing point suffices, without a uniform
positive lower bound. The addition map

$$
(\theta,\varphi)\longmapsto p+re^{i\theta}+re^{i\varphi}
$$

has Jacobian $r^2\sin(\varphi-\theta)$, nonzero outside a null set. Its
multiplicity is at most two away from $p$, and the exceptional fiber maps to
one point. The area formula gives positive area to its image, contained in
$S$. This contradicts $|S|=0$. Therefore $S$ is empty.

This is exactly the boundary in Lahti's formula (2.3). The Euclidean space,
Lebesgue measure and measurable red set meet Theorem 1.1's hypotheses on
every open ball. Its empty boundary has zero codimension-one measure, so
perimeter is finite there; formula (2.4) makes that perimeter zero. Applying
this on a larger ball containing the dilation required in (2.2), that
inequality says that on each smaller ball one color has zero measure.
Overlapping balls force the same choice throughout the plane. Equivalently,
the distributional gradient of the indicator is zero and the indicator is
constant almost everywhere. This verifies the candidate's final BV inference
without confusing its reduced-boundary language with the source's notation
for measure-theoretic boundary. No rectifiability hypothesis on $S$ was
assumed before finite perimeter was obtained.

A null or conull color makes almost every unit-equilateral placement
monochromatic, contradicting weak avoidance. This completes the central
interval and hence all positive unequal scales. The positive-measure
finite forcing implication then gives circle Corollary 5 for every
non-equilateral triangle, including collinear triples. Finally the arbitrary
two-scale conclusion follows from Weakest step 3, and the whole triangle
conclusion follows from the finite forcing and rescaling already checked.

## Strongest attacks and negative controls

The strongest attempted proof break was the passage from the functional cover
to a finite algebraic object. A span of units in a function field can be an
infinite algebra, so treating it as a number field would invalidate the
transcendental case. The actual proof avoids this: the rational transforms
have a common finite-dimensional range, multiplication by $T$ acts on that
range, and a polynomial annihilator leads to the explicitly bounded quotient.
The reduction of a $d+1$-term relation modulo $T-a$, with common powers removed,
is the decisive check. It works without finite generation and survives
localizations where a quotient can instead be zero. The Cayley denominators
are units in the algebra itself. No counterexample to that inference was
found.

A separate attack tried to concentrate a conditional wild law on ordinary
cosets. Unconditional null cosets alone would not exclude that. The finite
center construction, universal induction on the earlier factor, and the
strict collision bounds supply the missing protection. In particular,
choosing test frequencies after the coefficient-bin count and choosing the
index set after a fiber would be dangerous without their respective
uniformities. The supplied finite order of choices and simultaneous pair
bounds establish both. The conditional collision contradiction is numerical
in its constants but not a statistical heuristic.

Two exact controls test exceptional-set and endpoint failures:

1. A plane-null Borel set can fill an entire circle centered at one of its
   own points: $S=\{0\}\cup rS^1$ has
   $|\Theta_r^0(0)|=2\pi$. Thus discarding the null boundary on every
   centered circle would be false. The argument does not do that. It derives
   positive circle measure at **every** point of $S$, a condition this test
   set fails at each point of its circular part. The two-step area argument
   then rules out exactly that stronger condition.
2. The excluded ratio $x=1$ is substantive. Put $h=\sqrt3/2$ and color
   successive half-open horizontal strips of height $h$ alternately. This
   coloring avoids equilateral side one. Indeed, the vertical width $R$ of
   a unit equilateral triangle is at least $h$: the sum of the three squared
   vertical edge projections is $3/2$, whereas for three heights of range
   $R$ that sum is at most $2R^2$. It cannot fit in one half-open strip.
   Its width is at most one, so a monochromatic triangle occupying multiple
   strips would occupy two same-color strips separated by a gap of height
   $h$. Its isolated vertex would then differ in height from each other
   vertex by more than $h$. Its height difference from their midpoint would
   also exceed $h$, although its distance from that midpoint is exactly
   $h$. This is impossible. The control refutes the strengthening that
   includes $x=1$, not the frozen statement, which excludes it.

The Bessel criterion likewise cannot replace the central-circle argument:
at $x=1$, the checked value at $19/5$ gives
$2J_0(19/5)<-805/1000<-2/3$. By continuity the same obstruction to that
criterion persists for some unequal ratios near one. The proof's separate
central interval is therefore essential.

A generic conditional projection is another invalid shortcut. For the uniform
law on the six nonmonochromatic sign triples, projection to the trivial
factor produces $(0,0,0)$, whose threshold is monochromatic. But that
projection changes the pair correlations from $-1/3$ to zero. It does not
satisfy the correlation identity proved here. The nonnegative $Q$ argument
specifically uses that identity and the exact endpoint characterization.

None of these controls is a counterexample to the exact whole-plane
conclusion. They expose concrete failure modes that the supplied proof had
to avoid and show where its hypotheses and extra arguments are used.

## Independent calculation and reproduction

The retained `bessel_bounds.py` contains the nine rational rows as its exact
inputs. It uses only Python's standard library and exact `Fraction`
arithmetic. Taylor polynomials are evaluated in descending degree by Horner's
rule. This is an independent implementation of the displayed finite
inequalities, not a rerun of author code or a numerical library comparison.
The alternating-tail and ODE arguments are established in the preceding
mathematical examination; the program alone does not prove them or the
infinite two-scale assertion.

From an ordinary repository clone containing the retained keeper, run:

```sh
python -I wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py
```

The computation performed for this examination returned exit status zero for
all nine enclosures and the scalar margins. The input that must fail is:

```sh
python -I -O wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py --negative-control
```

It changes the first upper bound from $-260/1000$ to $-2601/10000$, keeping
a nonempty proposed interval. The recomputed $S_{0,20}(3)$ is not below
that upper bound. The observed result was exit status one, identifying that
failed inequality, even with optimization enabled. No bare assertion carries
a check. The displayed paths are the filing paths of the delivered program;
its inputs and behavior are independent of its directory. The program writes
no files and needs no private source, PDF, cached artifact or repository
module. Runtime is ordinarily a few seconds or less.

There is no computational batch of claims and no commissioned second review
cycle. The special requirement for a structurally disjoint batch reproduction
or a second cycle's distinct attacks is therefore inapplicable. The exact
calculation is only one finite leg of an analytic examination. The separate
Fourier re-derivation of circle alternation and the endpoint and null-set
controls do not derive their conclusions from that leg's success.

## Checklist

### Erdos-specific checklist

| Item | Applicability and finding |
| --- | --- |
| Quantifiers and scope | Applicable; no defect found. The proof covers each real $x>0$, $x\ne1$, every arbitrary coloring, and three distinct vertices, including collinear ones. The exception is per coloring. Almost-everywhere statements remain in the weak measurable stage until a contradiction to its existence is obtained. The reciprocal ranges and their closed endpoints are covered. |
| Circularity | Applicable; no defect found. The dependency order above is acyclic. Compact-tower termination follows from separability. Conditional singularity uses universal induction strictly at an earlier ordinal. Multiple averaging reduces the number of exponents. R0 and the final two-scale conclusion are not assumed. |
| Model and convention changes | Applicable; no defect found. Exact real-closed equations, the discrete spectral theorem, Bochner on Euclidean space, conditional expectation, and the $Q$ equality condition supply the transfers. Direct-isometry and collinear conventions were checked. No assertion of a measurable original coloring or pointwise uncountable action is needed. |
| Finite and statistical overreach | Applicable; no defect found. The finite forcing is a universal coloring implication on one exact configuration. The numerical leg checks only explicit rational inequalities; series remainders, zero spacing and the argument split supply the infinite range. The probabilistic estimates are exact inequalities on probability spaces, not sampled evidence. |
| Uniformity | Applicable; no defect found. The rational-transform range is fixed before translating the functional. The compact approximation and bin count precede frequency selection. All conditional pair bounds precede fiber-dependent index selection. Every-Følner convergence justifies bad-translate arguments. Selection constants are uniform over finitely many selections for fixed data, not over all $x$. Tonelli is followed by a countable sample intersection. |
| Extremal conclusions | Applicable; no defect found. The Bessel infimum is bounded in its actual dimensionless argument coordinates; taking an infimum weakens a pointwise strict bound to the stated non-strict bound, which still has gap $1/375$ from $-2/3$. Energy monotonicity justifies the asserted global minimum. At most one missing side is a cardinality conclusion, not an unproved claim of a specified exceptional side. |
| Consequences and composition | Applicable; no defect found. The exact carrier equivalence, all-real-ratio extension, non-equilateral and degenerate conclusions, reflection issue, positive-measure corollary and rescaling were separately checked. Every essential source clause is either rederived here or identified as a classical external boundary. |
| Computation | Applicable only to the finite Bessel inequalities. Exact inputs and arithmetic are retained. A false upper bound produces a nonzero exit under optimized Python. No numerical search, floating-point enclosure, exhausted iteration cap or computer-generated universal classification is used. |
| Reproduction | Applicable to that finite leg; no defect found. The keeper was executed afresh and the deliberately false input was rejected. All required mathematical data are literal in the program. No repository gate or cached report is a premise. Filing and separate grading remain outside this mathematical verdict. |
| Source and verdict fidelity | Applicable; no defect found within the permitted source scope. Versions and reading depth are explicit. The OpenAI source proof was not promoted from a card label; Jelínek's conventions were checked against the supplied version and coordinates; the Lahti specialization retains completeness, doubling and Poincaré hypotheses. No previous verifier ruling was supplied or characterized. |

### Canonical failure modes

| Mode | Applicability and finding |
| --- | --- |
| “Almost all” upgraded to “all” | Applicable; attack failed. The parameter-dependent exceptional sets in sampling are handled by Tonelli. The arbitrary conclusion is obtained by excluding the existence of the resulting weak avoider, not by claiming that its exceptional placements disappeared. |
| Induction presupposing termination | Applicable; attack failed. The tower's termination has the explicit uncountable-orthogonality contradiction; the two other inductions descend in ordinal or integer complexity. |
| Probabilistic or averaging heuristics presented as proof | Applicable; attack failed. Mean ergodicity, conditional moment bounds, finite union bounds and collision counts are proved inequalities with the required limiting order. No empirical probability is used. |
| Circular use of an equivalent statement | Applicable; attack failed. The equivalent two-scale formulation is reached through the finite forcing proof; neither it nor Haar rigidity is used to establish its own consumed premises. |
| Exceptional sets dropped from density arguments | Applicable; attack failed. The Borel boundary is retained until the two-step area argument makes it empty. A plane-null set is not presumed circle-null at every center. Frequency mass at infinity is retained. |
| Finite verification exceeding base-case coverage | Applicable; attack failed. The finite rational table has precisely its stated scope, with the analytical extension supplied separately. The chord-angle classification uses cyclotomic traces for every order, not finitely many denominators. |
| Relaxed or averaged convergence replacing actual objects | Applicable; attack failed. Projection preserves the needed pair correlations, and $Q=0$ forces actual opposite endpoint values before thresholding. The proof does not infer an avoiding sign coloring from a generic relaxed field. |

### Named patterns

| Pattern | Applicability and finding |
| --- | --- |
| Model-class transport instead of entailment | Applicable to the field and spectral transfers; no defect found. Every required field operation and group property is identified. The number-field selection is replaced rather than syntactically copied to a transcendental field. The carrier converse is exact entailment of finite constraints. No novelty claim about an axiom extension is being made. |
| Uniformity over an infinite family from finitely many instances | Applicable; no defect found. Uniformity in rotations or translated functionals comes from finite bases, compactness or every-Følner convergence. The constants are allowed to depend on the fixed ratio and finite cover. The Bessel table is not itself offered as a uniform-in-$x$ proof. |
| Extremal claims in their own units | Applicable; no defect found. The infimum concerns $J_0(t)+J_0(xt)$ at the specified ratio; the exact gap and the excluded endpoint were checked in those coordinates. |
| Consequence sentences as claim surfaces | Applicable; no defect found in the commissioned implications. In particular positive measure, exact carrier equivalence, all real ratios, every non-equilateral shape and the at-most-one-congruence-class conclusion each have a stated derivation. Unused alternative routes are not being separately accepted. |
| Carry hypotheses used by a quantified argument | Applicable; no defect found. Countability, real closedness, divisibility, bounded approximants, finite covers and three distinct vertices are all supplied. Positive-upper-density and density-one roles are not interchanged. |
| A composition inherits its unproved premises | Applicable; no unresolved essential premise found beyond the explicit external theorem boundaries. The source rigidity lemmas and their specializations were examined as part of the argument. R0 is discharged internally and no native tier-0 claim is silently imported. |
| Reproducibility notes are claims | Applicable to the retained exact-rational leg. The code, input scope, exit behavior and directory independence were checked; the false bound is a concrete failing input. No full-plane computational coverage is claimed. |
| Verifier quotations are claims | Inapplicable to the mathematical packet: previous review and standing text were excluded, and this report quotes no other reviewer's ruling. Checking later characterizations of this report belongs to the separate grading and filing process. |
| Verdict words spelled in full | Applicable. The mathematical verdict is written as **refutation-failed**, distinct from **refuted-as-stated** and **proof defective; statement unresolved**. No abbreviated verdict is used. |
| Certified-bracket functions fail loudly | Applicable to the finite bounds only; no defect found. These are fixed Taylor polynomials with an analytically justified alternating tail, not an iterative numerical routine returning a cap artifact. Inputs outside the stated domain and failed inequalities return failure. |
| A harness leg with no failing input is decoration | Applicable to the one executable leg; no defect found. The valid-domain false upper bound is rejected with exit status one. The remaining evidence is mathematical derivation, not a collection of unconditional success checks. |
| A gate reading caches instead of rerunning is defective | No gate is used as mathematical evidence. The exact-rational program was rerun; no cached output was consulted. Repository-wide gate output was outside the read set and was not read. |

The neighboring disciplines also have their actual scope: no inference from
correlated statistical samples is made, and the finite computation is not
credited with any of the field, measure, density or whole-plane conclusions.

## Verdict and limits

**Refutation-failed.** The exact whole-conclusion proof survived this
adversarial examination. No counterexample to the stated conclusion, real
error, or unsupported essential inference was found in the supplied route.
The argument covers arbitrary two-colorings, every real unequal ratio,
collinear triples of distinct points, and the stated measurable consequence.
The conditional and transformed objects are returned to the claimed
conclusion through the checked implications, rather than by ignoring their
qualifications.

This verdict is limited to the frozen subject and the exact external theorem
interfaces stated above. It is not a proof of the omitted portions of the
source manuscripts, a PDF-fidelity audit, a Lean audit, a novelty or public
status determination, or coverage of later corrections. Original proofs of
the identified classical theorems, including the finite-perimeter criterion,
remain external boundaries. The exact-rational keeper supplies only the
finite inequalities it documents.

The report does not grade itself, assert a verification tier, or claim outside
acceptance. An eligible separate grader must assess its independence,
completeness and evidence. No defect or unresolved mathematical qualification
has been suppressed to obtain a favorable verdict.
