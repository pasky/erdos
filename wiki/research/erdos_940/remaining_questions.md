---
name: research/erdos_940/remaining_questions
title: Remaining questions and retained approaches
desc: Open density and higher-exponent questions, retained mechanisms, and rejected bounded tests.
tags: []
sources: []
created: 2026-09-22T02:24:55Z
updated: 2026-10-28T16:29:39Z
---


# Remaining questions and retained approaches

***

## The unresolved targets

Positive lower density of the complement is accepted for $r=3$, on
[[problems/diophantine_problems/E0940/claims/2026_07_26_beyer_de_ryke|Beyer de Ryke's claim]],
and for $r=4$, on
[[problems/diophantine_problems/E0940/claims/2026_10_28_plasma_ai|Plasma AI's claim]].
Both acceptances rest on the
[[../library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/_index|separate Lean formalization]].
The [quartic argument](quartic_complement.md) remains author-recorded as
prose, and its stronger progression statement is outside that acceptance.
No argument here establishes infinitude for $r\ge5$, or decides density
zero versus positive upper density of any $S_r$, $r\ge3$.

## Unordered count congruences

The last new attempt was [divisibility of representation
counts](representation_count_congruences.md), not another local-solubility test.
A proved criterion would give a positive-density complement if, on a progression
of relative mean $\mu$, the unordered count were divisible by an integer
$m>\mu$ outside a density-zero exception. No such congruence was established.

The exact Newton and prime-adic layer identities retain the
five-distinct-part count. The mixed layers have order-$X$ mass;
at the prime five, the all-prime-free five-part family and one
specific four-free-plus-one-divisible family even have equal leading
means. They cannot be discarded. Repeated prime-free kernels and
nontrivial target-preserving changes supported on finitely many
fixed primes affect only $o(X)$ source tuples, so those carry or
valuation actions supply no generic extra orbit.

One bounded computation through $100000$, reproducible by the
[preserved script](evidence/util/representation_count_congruences.py),
found witnesses against every residue class for six specified pairs of
target and count moduli. Its conclusion is finite:
it rules out the corresponding congruences holding throughout a
residue class, not eventual congruences or untested moduli.

Renewed attempts at bounded typical multiplicity for
$x^3+2y^3+4z^3$, and at descent on
$(r+1)p^r$ or $(r+1)q^{rk}$, also supplied no target result.
In particular, the ray arguments did not force a common root divisor.
No new unconditional critical estimate was obtained from the source
checks. The tentative finite-curve direction was not completed or
adopted as a theorem.

The strongest target conclusions are unchanged: the complements have
positive lower density for $r=3,4$; complement infinitude for
$r\ge5$ and every density question remain unresolved here.
An integer-fiber estimate, a deletion comparison, or a new
cross-kernel count symmetry would be additional arithmetic input.
These are provisional possibilities, not demonstrated routes.
The proof is incomplete.

## Composition, shifted fibers, and cube differences

Neither of the two algebraic statements below resolves a target. Both are
proved and author-recorded.

The [rational-composition theorem](cubic_rational_composition.md) excludes
every total-degree-two polynomial identity
$F(C(\mathbf x,\mathbf y))=F(\mathbf x)F(\mathbf y)$ for a positive
diagonal ternary cubic. It handles the possible pure quadratic terms by
the absence of a nonconstant rational map from $\mathbb P^2$ to a
smooth plane cubic, followed by two bidegree comparisons. Consequently
every fixed rational composition has only $O(N^{17/3})$ positive
integral input pairs in balanced boxes. This does not control arbitrary
product representations or maps varying with the scale.

The [joint-shift calculation](joint_shift_fibers.md) treats
$F_j(\mathbf x_j)=n+h_j$ for any number of distinct shifts.
Its natural complete intersection is geometrically integral and normal,
with dualizing sheaf $\mathcal O(-r-1)$, independent of the number
of shifts. Thus increasing that number does not create general type.
No point-counting contradiction to cofiniteness follows; the affine
critical scale remains $B^r$. The finite-core consequence of
cofiniteness requires a fixed tuple only along an unbounded sequence
of scales, not necessarily at every scale.

For actual cubes,
[difference inversion](energy_and_multiplicity.md#inverting-a-cube-difference-is-already-almost-unique)
has vanishing average logarithmic multiplicity, by the existing binary-cubic
collision theorem. Nevertheless $\omega(|w^3-z^3|)/\log\log N\to2$ in
probability. Every positive-mass pair restriction therefore retains an unbounded
logarithmic divisor majorant. This identifies a loss in that attempted entropy
argument, not a bound for the weighted incidence among three independent
differences.

No bounded-fiber theorem for a fixed critical diagonal form, and no
arithmetic void comparison for powerful sums, was obtained. Density
remains undecided here for every $r\ge3$; complement infinitude for
$r\ge5$ remains unproved.

## Three auxiliary results with explicit limitations

None of the three auxiliary results below resolves a target. Each is
retained with its limitations explicit.

The
[metric countermodel](metric_coefficients.md#a-fixed-sequence-for-which-every-rational-tuple-is-exceptional)
is one increasing integer sequence $f(n)=n^r+O((\log n)^{1+o(1)})$. It agrees
eventually with actual powers modulo every fixed modulus and obeys the same
uniform power-difference bound, yet every positive rational coefficient tuple
has a density-zero value set, while almost every real rounded tuple has positive
upper density. This disproves extraction from those metric and congruence inputs
alone. It does not concern actual powers or preserve every growing-modulus
estimate. No tight arithmetic coefficient average or finite-dilation
decorrelation estimate for actual powers was obtained.

For an odd prime $p$, the
[prime-degree geometric form](cubic_carry_spectrum.md#prime-degree-geometric-forms-exact-local-and-first-layer-facts)
$\sum_{i=0}^{p-1}p^i x_i^p$ is exactly uniform modulo every $p^m$. Its first
digit box is bijective modulo $p^p$, and a box of side $B=p^k$ is uniform modulo
$pB$. Neither statement reaches the modulus $B^p$ needed to control integer
fibers. The valuation $v_p((u+p^jv)^p-u^p)=j+1+v_p(v)$ for unit $u$ explains why
characteristic-$p$ digit interleaving cannot simply be iterated over the
integers. No carry correction or positive-density induction was proved;
numerical box counts are not retained as certificates.

The [affine-fiber Brauer calculation](affine_fiber_brauer.md) proves
$\operatorname{Br}(U)=\operatorname{Br}(\mathbb Q)$ for
$U:\sum_{i=1}^r d_i x_i^r=n$, with $r\ge5$ and all $d_i,n$ nonzero.
Thus ordinary Brauer--Manin on the full affine fixed-core fibers
provides no additional obstruction to already existing local points.
This is not an integral local-global theorem. Punctured opens and
height restrictions are outside the calculation; the attempted
punctures supplied no uniform estimate over the other root variables.

An elliptic/Selmer transfer was also unsuccessful. For
$x^3+y^3=m=n-az^3>0$, the exact substitution

$$
u=\frac{12m}{x+y},\qquad v=\frac{36m(x-y)}{x+y}
$$

gives $v^2=u^3-432m^2$. Its index is $m$, which changes with $z$,
not the fixed full target $n$. No bounded-multiplicity map indexed
only by $n$, nor a height-sensitive average over these linked indices,
was established. Likewise, renewed quadratic-fiber and exact-covering
attempts did not improve the critical integer count.

The best target conclusions are unchanged: complement infinitude is
established here for $r=3,4$ only, and no density question is settled.
Possible future work must add exact-polynomial, finite-height input to
one of the counting or void mechanisms; that is a provisional direction,
not a demonstrated route. The proof is incomplete.

## Birational maps, dilation, and large primes

No target case was resolved. Three additional arguments have been
checked and retained.

For $r\ge4$, the [birational-similitude theorem](birational_diagonal_forms.md)
classifies every birational rational transformation satisfying
$F\circ T=mF$: it is monomial. The proof applies de Fernex's checked
superrigidity theorem to the generic degree-$r$ level in $\mathbb P^r$,
then uses its anticanonical embedding and a $t$-adic valuation argument.
This excludes composition laws birational in one input, not arbitrary
rational correspondences. The same note proves that ordinary products
of proper powerful subsums with at most $r$ expanded summands have
count $O_r(X^{1/2}(\log X)^{k-1})$.

The
[global dilation countermodel](palm_void_strategy.md#even-exact-global-dilation-identities-do-not-force-further-holes)
has precisely one missing target, a nonnegative primitive decomposition,
monotonicity under every powerful multiplier, and any prescribed mean
$\lambda\ge1$. Thus even the exact mean and these global dilation identities do
not imply the missing Palm comparison. The model is not an additive
representation function.

The
[large-prime secant lemma](cubic_secant_content.md#a-large-target-prime-cannot-occur-in-the-secant-content)
excludes a target prime $p>2HK$ from secant content, without assuming that
direction coordinates are units. A prime-target example rules out automatic
height-decreasing secant descent. For the special cubic, the direction factor
$J(\mathbf k)=\gcd(F(\mathbf k),|k_1k_2k_3|)$ has bounded logarithmic mean under
uniform primitive-direction sampling. Actual collisions weight those directions
by the unknown quadratic-fiber counts; replacing that weighting by uniform
sampling is the unresolved step.

Two further alternatives also fall short. Coprime binary traces
give simultaneous-square conditions in a quotient interval of length
$B$, with expected count $B^{-1}$ for each of $B^4$ parameter choices.
The available pointwise divisor bound is only $B^\epsilon$, not the
required averaged saving. An entropy-inverse argument from binary
energy cannot extract positive input mass from a slowly divergent
ternary entropy deficit: the asymmetric energy remains far below its
maximal scale. Neither is a multiplicity theorem.

Bounded numerical tests at the natural small-prime moduli for
$r=6,8,10$ gave very large representation means, not deficits. They
are not adopted as certificates or as all-modulus results. There is
still no density resolution and no infinitude proof for $r\ge5$.

## Exact scope of the fixed-field route

The attempted fixed-field route turned out to refine the
[previous Eisenstein parametrization](#an-eisenstein-height-counting-attempt),
not to evade its obstruction. The
[expanded proof](eisenstein_collision_content.md) classifies all
integral multipliers of a primitive Eisenstein parameter, gives
the exact height scale $B^4/g$, and proves that a content-tail
bound $B^6/D$ with logarithmic losses in $B^3/D$ would suffice
for critical cubic energy. The local permutation calculation and
the K3 common-zero geometry are also checked. The endpoint
$D\asymp B^3$ already contains the original primitive collision
problem; no needed estimate there was established.

[Integer translation averaging](cubic_carry_spectrum.md#what-averaging-integer-root-translations-actually-proves)
does converge to ambient Haar measure and gives the genuine bound
$A_{N,H}\ll N^3+N^6H^{-2+\varepsilon}$ for $H\ge N$. It works in the previously
controlled short-box range, not at the bounded aspect ratio required for density
extraction.

The [covering attempt](critical_covering.md) proves local
anti-concentration of proper powerful subsums. Cassels bases
satisfy even stronger estimates and are nevertheless additive
bases. This rules out a universal argument based only on those
estimates, bounded-error counting, and a finite mean. It does
not rule out using the exact root tracks or multiplicative closure.

The [split-prime normal-order theorem](cubic_split_prime_counts.md)
shows that typical inputs to $x^3+2y^3+4z^3$ have
$(1/6+o(1))\log\log N$ distinct, exactly-once prime factors
splitting completely in the splitting field of $T^3-2$.
Restricting this number to be bounded therefore loses almost all
input mass. No assertion that the local classes yield small
positive integral partners was established.

The [all-three-traces construction](cubic_trace_counterexample.md)
gives arbitrarily many interior representations of cube targets
with all three families of pairwise trace ratios of full height.
It rules out unrestricted deterministic trace pigeonholing.
No primitivity is claimed, and the constructed family has zero
input mass, so a statistical estimate remains possible.

The renewed coefficient-separation and prime-denominator attempts
also did not resolve a target. A fixed large coefficient only
reduces the number of possible competing roots to a constant
multiple of $N$, not to a bounded number. On a missing prime
ray, the case of $r$ summands all prime to the denominator still
requires the uncontrolled index-one hypersurface count and a
size-sensitive core tail.

Possible further work on the content-tail endpoint, integral
heights in local descent classes, or exact arithmetic covering
is provisional. None is an established route to completion.
The density cases and the infinitude cases $r\ge5$ remain
unresolved here.

## Trace slices and bounded core statistics

Three additional lemmas are proved and author-recorded, without
resolving a target case.

The
[binary-trace slice bound](cubic_collision_ranges.md#binary-trace-ratios-uniformly-in-the-prescribed-ratio)
shows that, for $x^3+y^3+cz^3$, each prescribed reduced ratio $(u+v)/(x+y)$
permits only $O_{c,\varepsilon}(N^{2+\varepsilon})$ nontrivial collisions,
uniformly in the ratio. Consequently all ratios of height at most $N^{1/2-\eta}$
can be removed at a cost of $o(N^3)$ input mass, also in the logarithmic moment.
In particular the common-trace stratum has a power saving. The unrestricted
trace-ratio tail is not controlled.

The
[canonical entropy identity](finite_core_reduction.md#mixing-the-canonical-cores-costs-bounded-entropy)
shows that mixing the infinitely many canonical forms contributes only $O_r(1)$
conditional entropy under uniform representation sampling. Thus competition
between cores is tight relative to the selected form's self-multiplicity.
Integer-coefficient averaging has not supplied an estimate for that
self-multiplicity; useful coefficient ranges growing with the scale have
vanishing canonical input mass.

The
[Palm truncation inequalities](palm_void_strategy.md#quantitative-stability-under-core-truncation)
show that the bounded comparison statistic changes by at most a constant times
the first-moment tail. This would transfer a finite-family arithmetic comparison
to all powerful coefficients. No such comparison was proved. Individual
representation events at different target values are negatively correlated,
while the positive association on prime exponents along a missing ray may put
all its void mass at the original seed. Neither supplies the required new
arithmetic input.

The attempted local quadratic and varying-trace constructions also
did not close the density problem. Exact quadratic cancellation is
available on a cubic trace slice, but interactions between different
slices remain uncontrolled. For degree at least four, positive
fourth directional derivatives prevent an exact affine quadratic
reduction on a nonconstant positive patch. These are limitations
of the tested constructions, not impossibility theorems for a
positive-density solution.

The open density cases and the infinitude cases $r\ge5$ remain
unresolved here.

## A different proposed mechanism: deleting a sampled representation

The [Palm/deletion strategy](palm_void_strategy.md) changes the question
from collision moments to a bounded void-probability statistic. Compare
a uniform target's fiber with the fiber of a uniformly sampled
representation after that representation is deleted. A proved
one-point comparison criterion would force a positive density of
missing targets at any finite mean, including means above the quintic
first-moment floor. Compound-Poisson clustering is compatible with it.

The arithmetic comparison is unproved; no deletion coupling has been
constructed. The complementary lower comparison is equivalent to the
positive-density problem, not an independent theorem. An explicit
covering by convex power tracks shows why spacing and critical
cardinality alone cannot establish the proposed comparison. The
unresolved targets above are unchanged.

## Checked additions from the secant and grouping approaches

The [local secant-content formula](cubic_secant_content.md) identifies the
good-prime valuation of $\gcd(F(\mathbf k),3\sum a_i x_i k_i^2)$ as
$\min(v_p(n),2\min_{i<j}v_p(x_i k_j-x_j k_i))$, under primitivity of
both endpoints. Two exact squarefree-output examples show that this
content can be nontrivial and that the third secant point can even be
integral. Output squarefreeness alone does not remove the uncontrolled
secants; their alignment indices still need an averaged estimate.

The [powerful-subsum theorem](powerful_subsum_counts.md) gives, uniformly
for $|h|\le X$, an upper bound
$O_{r,k,\varepsilon}(X^{k/r-\delta_r+\varepsilon})$ for ordered
$k$-tuples of $r$-powerful integers with total at most $X$ whose total
plus $h$ is $r$-powerful, where
$\delta_r=(r-1)/(r^2(2r+1))$. Its proof uses the checked
coefficient-uniform plane-curve bound, not the primitive ternary
theorem. A local sieve also shows that grouping given summands into
fewer blocks of any fixed powerful exponent at least two retains
only $o(X)$ of the original $r$-tuple input mass. Neither result
counts arbitrary targets, and the quantitative bound is still much
larger than the population of near-powerful targets.

The
[polynomial missing-ray lemma](finite_core_reduction.md#polynomial-identities-on-a-missing-ray)
shows that a linear-denominator polynomial identity on $t m^r$, with
$t\notin S_r$, has a fixed nontrivial denominator content. Finitely many fixed
univariate polynomial identities cover only $O(M^{1/2})$ prime denominators up
to $M$. Representations outside such fixed families remain uncontrolled.

These additions do not change the unresolved targets above. In
particular, no unconditional positive-density theorem or
higher-exponent gap theorem has been established.

## Comparison with the independent record

The
[independent input](independent/canonical_decomposition_and_quartic_zero_target.md)
has been compared with the topical proofs. Its canonical-core equivalence,
energy criterion, cubic quadratic-fiber reformulation, Hessian argument and norm
obstruction agree with existing work; the existing canonical tail bound is
stronger, attaining the exponent $1/[r(r+1)]$ without the independent argument's
loss. The current higher-exponent progression theorems, especially the quintic
certificate, also go beyond its large-good-prime limitation.

Checked additions are the [homogeneity counterexample and polynomial-summand
restriction](finite_core_reduction.md), the [prime-adic injectivity
obstruction](energy_and_multiplicity.md), and the sharper
[nonzero-target local bound](local_first_moments.md). The
[quartic comparison](quartic_finite_families.md) verifies the paired-family
obstruction and its global density bound, and explains how the current proof
bypasses it. One restricted optimization failure is
[certified exactly](quartic_residue_obstruction.md). The independent record's
statement that quartic infinitude was not proved is superseded by the
current proof; none of its checked obstructions invalidates that proof.
The unresolved targets above are unchanged.

### Comparison with the second independent record

The
[later independent input](independent/quartic_pattern_elimination_and_random_omission.md)
does prove the same quartic complement theorem already established here. Its
[random omission completion](quartic_random_omission.md) has been checked and
retained as an alternative to the finite bounded-budget construction. New useful
inputs are the [two-sided quadratic prime-harmonic
bound](quadratic_prime_harmonics.md) and an [explicit radical-size Gaussian
modulus](quartic_euler_majorant.md#a-conductor-bound-in-terms-of-the-coefficient-radical).
The local trace, principal-character elimination, and lattice-density passage
agree with the existing proof.

Its finite-mask warning applies to the earlier equal-budget construction, not
the successful weighted finite distribution. The
[quartic comparison](quartic_finite_families.md#comparison-with-the-later-random-omission-record)
records that distinction and checks its mixed-principal, valuation-class, and
simultaneous-splitting examples. Its fixed-form equivalence is already known
here and its coefficient tail is weaker; its additional
[growing unrestricted tuple constant](finite_core_reduction.md#unrestricted-tuple-counting-has-a-growing-constant)
is correct but yields no distinct-value bound.

The record's named supplementary files were not supplied in this research
folder. The checks use the arguments in the record and the relevant full source
passages, not its reports of internal review. Its numerical Euler products
remain noncertified diagnostics. Its cubic and higher-exponent conclusions are
compatible with the more detailed established collision, profinite, and
first-moment notes; none supplies the missing integer-fiber estimate or an
additional target case. The unresolved targets are unchanged.

### Comparison with the third independent record

The [new independent input](independent/quartic_analytic_architecture.md)
includes its auxiliary working proofs, unlike the second record. Its
conservative statement that the assembled quartic argument had not been
finally certified is historical, not a disagreement with the established
theorem. The analytic assembly is checked and retained as
the [universal-selector proof](quartic_universal_selector.md).

One infinite negatively biased set of primes controls every positive
squarefree determinant and every cutoff interval simultaneously.
The maximal Hoeffding estimate and its countable union bound are valid;
the two-sided quadratic estimate bounds the infinite character mixture.
Removing all coefficient primes, including those absent from the
squarefree determinant, costs only an exponential in the radical's
number of prime factors. A growing deterministic support cutoff then
gives a single summable majorant for both regular and exceptional tuples.
The resulting moduli and residues can be compatible and nested, but the
conclusion is still only the existing quartic complement theorem.

The local check yielded an additional refinement. Prescriptions are needed only
at primes occurring to odd valuation in some coefficient, even for the mixed
principal-character cases. The weighted exceptional tail with such a prime
exceeding $Y$ is $O(Y^{-3/2})$. The
[finite-family note](quartic_finite_families.md#odd-valuation-support-and-a-sharper-exceptional-tail)
proves this for the whole exceptional union; the independent record gave it only
for square products. That note also records the harmless $81$ versus $81e$
logarithmic-exponent discrepancy and the precise failure of iterating an
unconditioned negative one-prime mean.

The [Euler note](quartic_euler_majorant.md#tracking-principal-constituents)
retains the valid interpolation counting principal constituents. Its
regular case is already established, with a slightly sharper defining
ideal than the independent $(32R)$. The
[quadratic harmonic note](quadratic_prime_harmonics.md)
includes the independent elementary Landau nonvanishing proof, so it needs no
fixed-character prime-distribution input.
The supplementary lower-Hecke-$L$ route is unnecessary: neither the
baseline nor either random completion requires lower bounds for
Gaussian Hecke $L$-functions.

The finite-core equivalence, tuple-count formula, cubic energy criterion
and Perazzo mismatch agree with existing, more detailed arguments.
The truncated numerical Euler products are not adopted as certificates.
The independent higher-exponent limitation is weaker than the established
uniform progression floor and quintic obstruction. No density question
or infinitude case $r\ge5$ is resolved.

## Positive density and energy

For fixed positive coefficients $\mathbf a=(a_1,\ldots,a_r)$, let


$$
V_{\mathbf a}(N)=\left\{\sum_i a_i x_i^r:1\le x_i\le N\right\},
\quad
E_{\mathbf a}(N)=\#\left\{\mathbf x,\mathbf y\in[1,N]^r:
\sum_i a_i x_i^r=\sum_i a_i y_i^r\right\}.
$$


Cauchy–Schwarz gives $|V_{\mathbf a}(N)|\ge N^{2r}/E_{\mathbf a}(N)$. Thus a
uniform estimate $E_{\mathbf a}(N)\ll N^r$ for even one fixed positive
coefficient tuple would give positive lower density of its value set and, after
a fixed dilation, of $S_r$. A bound along an unbounded sequence would already
give positive upper density.

The [finite-core equivalence](finite_core_reduction.md) shows that letting
coefficients grow with $N$ does not bypass the fixed-form issue: outside any
sufficiently large fixed canonical core, the total candidate tuples are at most
an arbitrarily small constant times the target range.

Wang's Theorem 1.3 gives the needed bound for three cubes only under Conjectures
1.2, 1.4, and 1.5. The theorem statement and hypotheses have been checked in
[the full supplied paper](../../../library/diophantine_problems/wang_2021_sums_cubes_ratios_conjectures/_index.md).
This is a conditional negative answer to density zero, not an unconditional
resolution. The signed almost-all results elsewhere in that paper do not supply
positive summands.

These notes isolate a weaker target: bounded multiplicity on a positive
fraction of input tuples is equivalent to positive upper density, and bounded
average logarithmic multiplicity is sufficient. The
[complete statements and proofs](energy_and_multiplicity.md) also show
convergence of the good-prime energy product for every $r\ge3$. For cubes, the
associated real quadric-fiber volumes sum to the expected $O(N^3)$, but a
pointwise lattice bound at that volume scale is false because of permutation
families. No averaged bound removing this obstruction was proved.

The subsequent [real-coefficient theorem](metric_coefficients.md) achieves the
log-free near-collision bound after averaging over a real coefficient box. It
proves positive upper density of rounded values for almost every real vector.
All rational vectors may lie in its exceptional set, so this is not a
counterexample to the density-zero question. Atomic coefficient measures cannot
satisfy the proof's general inverse-width slab bound, and any successful
countable weighted energy estimate would already imply the requisite estimate
for each supported form.

The special cubic $x^3+2y^3+4z^3$ eliminates rational zeros at infinity and
coordinate-permutation identities, but does not eliminate split positive fibers:
an [explicit two-parameter identity](energy_and_multiplicity.md) demonstrates
this. Its ruling directions through a fixed nonzero-coordinate diagonal point
lie on a genus-two curve. Finiteness at each fixed point is established; a
uniform estimate over varying points is not.

## Fixed linear changes of variables do not remove the coefficients

Suppose $r\ge3$, $F_{\mathbf a}=\sum_i a_i x_i^r$,
$F_{\mathbf b}=\sum_i b_i x_i^r$, and


$$
F_{\mathbf b}(T\mathbf x)=\lambda F_{\mathbf a}(\mathbf x),\qquad
T\in\operatorname{GL}_r(\mathbb Q),\quad\lambda\ne0.
$$


Then $T$ is monomial. Indeed, the Hessian determinant of a nondegenerate
diagonal form is a nonzero constant times $(x_1\cdots x_r)^{r-2}$. The Hessian
transformation rule forces the product of the row linear forms of $T$ to be a
constant times $x_1\cdots x_r$. Unique factorization makes each row a scalar
coordinate. Consequently an invertible rational linear transfer to equal
coefficients requires all the $a_i$ to lie in one rational $r$-th-power class.
This is a proved limitation of that specific transfer mechanism, not a theorem
excluding all positive-density constructions.

## Higher exponents need more than the present first-moment method

For $r\ge5$, [the uniform lower-bound theorem](local_first_moments.md) gives
$c_r>0$ such that every fixed progression has normalized ordered representation
mean at least $c_r$. The good-prime error is summable even at zero targets and
at arbitrary prime powers. This rules out arbitrarily small first moments, the
precise conclusion used in the cubic and quartic arguments.

For $r=5$ the quintic note proves more: [every unordered progression first
moment exceeds $385732347/156250000>2.468$](quintic_first_moment_barrier.md),
strengthening the earlier $429/400$ bound. The finite coefficient family, exact
small-prime convolutions, rational product comparisons, and analytic tail
estimates are preserved with the proof. Consequently neither complete ordered
nor complete unordered representation counting can directly produce a deficit
below one on a fixed progression. This does not exclude a method that controls
or removes repeated representations. No comparable below-one obstruction is
asserted here for every $r\ge6$.

No monotonicity of the required sumsets transfers the quartic complement theorem
to $r\ge5$: although $r$-powerful integers are 4-powerful, the allowed number of
summands increases with $r$.

There is a stronger obstruction to transferring the quartic proof by identities.
The [quadratic-compression proposition](quadratic_compression.md) excludes any
rational-function representation of a positive diagonal degree-$r$ form in
$r\ge5$ variables by a fixed positive quadratic form in at most four variables,
even with arbitrary denominators. For $r\equiv2\pmod4$, it excludes every
smaller quadratic dimension. This is a limitation of the compression mechanism,
not an infinitude theorem.

The quintic first-moment obstruction is not confined to fixed moduli. The
[uniform lattice inequalities](moving_moduli.md) show it persists for
$M=o(X^{1/5})$, and on intervals $(A,B]$ of length $H\gg M B^{4/5}$ with a
sufficiently large fixed constant. For $H/(MB^{4/5})\to\infty$, the normalized
unordered mean has liminf at least $429/400$. Distinct values might still leave
gaps in these intervals.

A qualitative simultaneous-approximation proposal also fails: for every finite
collection of fifth-power cores, the root fractional parts $(n/d)^{1/5}$ are
equidistributed along a suitably chosen represented ray $n=(b^5+4)m^5$. Thus
every nonempty open pattern of finitely many axis intercepts occurs among
represented targets. This does not exclude shrinking-target conditions or
arguments using the full lattice shell.

A scaling obstruction cannot exclude an entire positive rational homothetic ray
either. Every $q\in\mathbb Q_{>0}$ is $d x^r$ with $d$ a canonical core and
$x\in\mathbb Q_{>0}$: reduce every prime valuation modulo $r$ using the
canonical exponents. Clearing denominators turns any fixed positive rational
decomposition into a powerful-number decomposition after a common $r$-th-power
dilation. In particular, every positive integer $n$ has the $r$-powerful
multiple $n^{r+1}$. This rules out nonrepresentability over positive rationals
as that particular obstruction; it does not rule out missing integers along a
ray.

## Bounded tests retained only as rejected ideas

An initial quartic optimization restricted to character profiles determined by
coefficients modulo $16$ did not produce a deficit. With canonical Euler factors
truncated at primes $10^6$, the ordered-to-unordered normalization gave a
minimum near $87.14$ for the class $8\pmod{16}$, and near $59.84$ after also
imposing $v_3(n)=1$. These are exploratory approximations, not certified
constants; the restricted profile family was abandoned. The successful proof
uses a different distribution and does not depend on these computations.

The tempting sequence $8\prod_{p\le Y,\ p\equiv3\pmod4}p$ is not generally
excluded. For example,


$$
8\cdot3\cdot7\cdot11\cdot19
=35112=625+1296+16384+16807,
$$


and every summand is 4-powerful. This exact certificate defeats that proposed
direct construction.

Suggested next work remains provisional: a special fixed diagonal form with
controlled collision count, or a genuinely nonlocal argument for gaps when
$r\ge5$. Neither has yet been supplied.

## Exact status of the controlled cubic ranges

The [controlled cubic ranges](cubic_collision_ranges.md) are bounded at
$O(N^3)$: coordinate-zero differences, differences of size at most
$N^{2/3-\eta}$, and primitive difference directions of size at most
$N^{1/2-\eta}$. The last two bounds have power savings away from coordinate-zero
differences. The proof uses a coefficient-uniform elementary ternary quadratic
bound. For $x^3+2y^3+4z^3$, what remains in this energy approach consists
entirely of nonsingular fibers with large primitive direction. The range
$\|\mathbf k\|\asymp N$, $t=1$ is still uncontrolled. Neither the inspected
singular-cubic counting theorem nor an unjustified average over binary ideal
classes removes this gap.

The [linear identity rank theorem](linear_collision_families.md) gives a precise
limitation of redundancy constructions. A positive nontrivial identity with $r$
degree-$r$ terms on each side has parameter rank at most $r-1$. If a
nonproportional relation survives, the rank is at most $\lfloor r/2\rfloor+1$.
Thus a fixed finite collection removes only $o(X)$ representation pairs. Even
when identity heights grow, linear mass requires at least order $X^{1/r}$
families; for genuinely nonproportional quintic families the necessary threshold
is $X^{2/5}$. No collection achieving the required mass was found.

### Scaling along a ray: an exact identity, not a descent

For fixed $F_{\mathbf d}=\sum_{i=1}^r d_i x_i^r$ and a positive integer $t$, let


$$
A_{\mathbf d,t}(h)=\#\{\mathbf v\in\mathbb N^r:
F_{\mathbf d}(\mathbf v)=th^r,\ \gcd(h,v_1,\ldots,v_r)=1\}.
$$


If $R_{\mathbf d}(n)$ counts positive integral representations by this form,
then exactly


$$
R_{\mathbf d}(tm^r)=\sum_{h\mid m}A_{\mathbf d,t}(h).
\tag{1}
$$


Given a representation, take $g=\gcd(m,x_1,\ldots,x_r)$, $h=m/g$, and
$\mathbf v=\mathbf x/g$. Conversely scale a primitive tuple by $m/h$. These maps
are inverse.

If $t\notin S_r$, then $A_{\mathbf d,t}(1)=0$ for every canonical core tuple. At
a prime $p$, (1) therefore leaves precisely the primitive denominator-$p$ points
on


$$
\sum_i d_i v_i^r=t p^r.
$$


It does not force a representation to descend to $t$. For exactly $r$ summands
this is a smooth degree-$r$ hypersurface in $\mathbb P^r$, of index one; no
estimate sparse enough on prime denominators was established. There are two
additional gaps in a proposed prime-ray argument: the global core tail
$O(XT_r(Y))$ cannot control a population of only order $X^{1/r}/\log X$, and
fewer-than-$r$ summands cannot be discarded on that ray merely because they have
global density zero. The analogous denominator identity holds for those shorter
tuples too, but no sufficient count was proved.

Any next step is provisional. The critical large-direction cubic average and
nonparametric control of distinct higher-degree values remain possible targets;
none of the foregoing results settles them.

### Divisibility-minimal multipliers on a missing ray

The following elementary structure statement is proved. It does not produce
an unrepresented target.

Fix $t\notin S_r$ and put

$$
M_t=\{m\ge1:tm^r\in S_r\},\qquad
B_t=\{b\in M_t:\text{no proper divisor of }b\text{ belongs to }M_t\}.
$$

The set $M_t$ is upward-closed under divisibility: multiply every summand in a
representation by $q^r$ to pass from $m$ to $mq$. Also $1\notin M_t$.

**Lemma.** If $M_t$ contains every sufficiently large prime, then $B_t$
consists of those sufficiently large primes and finitely many additional
elements. In particular this holds if $M_t$ is cofinite.

**Proof.** Every prime in $M_t$ is a minimal element, since its only proper
divisor is $1$. Choose $P$ such that every prime greater than $P$ belongs to
$M_t$. A composite minimal element cannot have a prime divisor greater than
$P$, since that prime would be a proper divisor lying in $M_t$. The composite
minimal elements are therefore supported on finitely many primes. Their
exponent vectors form an antichain under coordinatewise comparison, so there
are finitely many by Dickson's lemma. One elementary proof of the needed
fact is that every infinite sequence in $\mathbb N^k$ has an infinite
coordinatewise nondecreasing subsequence: successively extract such a
subsequence in each coordinate, using either an infinitely repeated value or
an increasing subsequence. Two distinct elements of an antichain cannot
belong to such a sequence. $\square$

Thus either infinitely many prime nonmembers of $M_t$ or infinitely many
composite members of $B_t$ would prove infinitely many missing targets on the
ray. Neither has been established. A bound
$\sum_{b\in B_t}b^{-1}<\infty$ would suffice, because it precludes every
sufficiently large prime being a generator, but no such bound follows
from the available canonical-core estimates.

Nor would proving density one for $M_t$ settle its cofiniteness. This is an
actual limitation of the divisibility-ideal argument: choose an infinite set
$\mathcal Q$ of primes with convergent reciprocal sum, and let $M$ be the
set of integers divisible by some prime outside $\mathcal Q$. Then $M$ is
upward-closed and misses every prime in $\mathcal Q$. Nevertheless it has
density one. For any finite set $E$ of primes outside $\mathcal Q$, the upper
density of its complement is at most $\prod_{p\in E}(1-1/p)$ by CRT; these
products tend to zero because the reciprocal sum over primes outside
$\mathcal Q$ diverges. This example concerns abstract divisibility ideals,
not a construction of the actual set $M_t$.

### Cube-free estimates and near-neighbor implications

The [cube-free estimates](cubefree_cubic_values.md) retain positive input mass
but do not bound distinct-value multiplicity. Two additional observations
are checked in the [energy note](energy_and_multiplicity.md):
unrestricted multiplicities for $x^3+2y^3+4z^3$ satisfy
$r_F(2n)=r_F(n)$ exactly, and a vanishing proportion of inputs with a neighbor
on the same level surface at distance at most $\varepsilon N$ would imply
positive lower density. The latter is a conditional implication; the needed
near-neighbor estimate is unproved. The existing short-difference estimates
do not reach the required fixed-relative-distance scale.

## Direct completion attempt: still unresolved

A further attempt to close the two main gaps did not produce a solution. For
cubic near neighbors, even primitive differences of size $\varepsilon N$ leave
the uncontrolled critical quadratic-fiber average; choosing only a nearest
neighbor supplies no proved arithmetic descent. The
[exact carry formulation](energy_and_multiplicity.md) likewise leaves the
bounded-multiplicity question intact. Maynard's 2026 survey, whose introduction
was checked, also identifies typical multiplicity as the unresolved issue for
three positive cubes and states Wang's positive-density result only
conditionally
([Section 1](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.70554)).
This does not establish that every possible special-coefficient approach must
fail.

For the higher-exponent prime-ray route, one additional reduction is exact.
Let $r<t<2^r$ and let $p>t$ be prime. If $tp^r$ has a representation by at
most $r$ positive $r$-powerful summands, every summand divisible by $p$ is
exactly $p^r$. Indeed its $p$-adic valuation is exactly $r$, since
$p^{r+1}>tp^r$, and its quotient by $p^r$ is $r$-powerful and less than
$2^r$, hence is $1$. Remove the $k$ such terms. The residual relation is

$$
a_1+\cdots+a_s=(t-k)p^r,\qquad
2\le s\le r-k,\quad p\nmid a_i,\quad\gcd(a_1,\ldots,a_s)=1.
$$

There is at least one residual term because $t>r$, and there cannot be just
one because it would be divisible by $p$. Their gcd is $r$-powerful,
coprime to $p$, and divides $t-k<2^r$, so it is $1$.

This includes the elementary missing seed $t=r+1$, but the dominant case
$k=0,s=r$ remains. Its fixed-core projective equation
$\sum_i d_i v_i^r=tp^r$ has degree $r$ in $\mathbb P^r$, hence index one,
not general type. No estimate at the necessary $P/\log P$ scale for prime
denominators, and no suitable coefficient-tail estimate on that ray, was
obtained. These observations are not an infinitude or density theorem.

Nor does the size restriction exclude every prime $p>r+1$. Already

$$
6\cdot7^5=2^5+2^{12}+3^8+2^7 3^5+3^{10}=100842
$$

is a representation by five $5$-powerful integers prime to $7$.
This exact identity refutes that stronger proposed prime-ray exclusion;
it says nothing about infinitely many other prime denominators.

## Open questions from the moment, carry, and descent approaches

No unresolved part of the target problem is settled by the following
checked results and failures:

- [Primitive cubic fibers](primitive_cubic_fibers.md): removing common
  dilations costs $O(X)$ in the logarithmic moment; a uniform bound for
  primitive logarithmic multiplicity is equivalent to one for all
  representations. Low-height projected collision planes contribute
  $o(N^3)$ to that moment. Every curve over $\mathbb Q$ on
  $x^3+2y^3+4z^3=nw^3$ has degree divisible by three, but varying
  higher-degree curves and primitive large fibers remain uncontrolled.
- [Dyadic carries](cubic_carry_spectrum.md): exact local uniformity and an
  exact lift recurrence hold, but a proposed uniform decay of primitive
  high-conductor carry characters is false. The explicit obstruction is
  the persistent rational resonance $1/9$. A spectral argument retaining
  these resonances remains an idea, not an established estimate.
- [The Perazzo transfer](cubic_collision_ranges.md): adding the required
  cubic term changes a quadratic-character Fourier transform into the
  explicit Salié-sum expression (14). The needed cancellation in that sum
  was not proved; the singular-cubic theorem cannot simply be substituted.
- [Prime-ray descent](local_first_moments.md): for every fixed core and
  all sufficiently large good primes there are nonsingular zero residues
  with no proper zero subsum, and these lift and combine by CRT. Thus
  denominator factorization alone cannot force a shorter relation. The
  Archimedean size restriction still has not been exploited sufficiently.
- [Adaptive coefficient averaging](metric_coefficients.md): a bounded
  logarithmic moment plus positive mass on a fixed finite arithmetic
  coefficient set would extract a successful fixed form. Neither the
  required arithmetic average nor its discrete tightness was established.

Possible next steps are therefore provisional: control primitive
large-fiber input mass, obtain a resonance-aware carry estimate, or find
an arithmetic gap argument using size as well as congruences. The present
notes contain no theorem furnishing any of those missing estimates.

## Two cubic estimates, no resolution

The [coordinate-zero refinement](cubic_collision_ranges.md) now gives
$O(N^{1+\sqrt3}(1+\log N)^4)=o(N^3)$ off-diagonal coordinate-sharing
collisions for $x^3+2y^3+4z^3$. Its proof uses the checked uniform diagonal
surface estimate of Salberger. Deleting all participating inputs changes
the logarithmic moment by only $o(N^3)$. More generally, coordinate-sharing
near neighbors contribute $O(\varepsilon N^3)+o(N^3)$ for every positive
ternary diagonal cubic, including the weighted-swap cases. Thus the
near-neighbor criterion now leaves only all-nonzero coordinate differences.

The [major-arc estimate](cubic_major_arcs.md) proves a sharp
$Q^{-2/3}$ tail for rational resonance weights and an asymptotic
$N^3\mathfrak J\mathfrak S+O(N^{11/4})$ on major arcs of denominator
at most $N^{3/8}$. Their contribution to the input mass over fibers of
size greater than $K$ is $O(N^3/\sqrt K)$. The complementary Fourier
correlation is not bounded; this is not a full high-fiber tail estimate.

The higher-exponent search found no main-term duplication or
size-sensitive gap argument. In particular, no infinitude case $r\ge5$
and no density question has been resolved here.

## Large-prime input trial

The last distinct approach restricted each cubic root to
$\mathcal A_\theta(N)=\{x\in(\delta N,N]:P^+(x)>N^\theta\}$, for fixed
$0<\delta<1$ and $1/2<\theta<1$. The
[complete argument](large_prime_roots.md) proves

$$
|\mathcal A_\theta(N)|
=\bigl((1-\delta)\log(1/\theta)+o(1)\bigr)N.
$$

This is a positive-mass subset of inputs to a fixed integral form, not
an extraction of rational coefficients from a real metric theorem.
Writing $x=mp$ gives bilinear cubic sums, but neither their critical
sixth moment nor a sufficient logarithmic moment was bounded.

The negative conclusions are specific. A large prime dividing an input
root need not divide a competing root; all-unit nonsingular local
solutions remain available. Cauchy in the cofactor variable followed by
termwise absolute values leaves a factor equal to its range in the
pointwise bound. Restricting cofactors to a subpower range loses positive
input density. These statements defeat that divisibility argument and
that Cauchy estimate, not every joint bilinear argument.

Two checks address proposed rough-target filters. For every prescribed
roughness threshold and number of target prime factors, the note
constructs represented targets with all root primes in one fixed finite
set. Separately, for fixed $r\ge5$, $k\ge1$, and $0<\eta<1/2$, a
checked application of the lower linear sieve gives

$$
\#\left\{\mathbf z\in(Z,2Z]^r:
 P^-\!\left(\sum_i z_i^{rk}\right)\ge Z^\eta\right\}
\gg_{r,k,\eta} Z^r/\log Z.
$$

Their canonical roots $z_i^k$ are comparable and have no prime factor
above $2Z$. This tests a stated range of power-scale roughness as well.
It counts input tuples, not distinct outputs; for $k>1$ the input
family is sparse at the root scale. Neither construction excludes a
statistical roughness argument.

## An Eisenstein height-counting attempt

A separate attempt used a rational parametrization rather than local
Fourier estimates. Here is the exact arithmetic issue it left open.
Put $K=\mathbb Q(\sqrt{-3})$, $\delta=\sqrt{-3}$, and, for fixed
positive integers $a_1,a_2,a_3$, define

$$
A(\mathbf w)=\sum_{i=1}^3 a_iw_iN_{K/\mathbb Q}(w_i).
$$

For $z_i=(x_i-y_i)+\delta(x_i+y_i)$,
$\operatorname{Re}A(\mathbf z)=4\sum_i a_i(x_i^3-y_i^3)$.
Conversely, when $A(\mathbf w)\ne0$, the vector
$\mathbf z=\delta\overline{A(\mathbf w)}\mathbf w$ has
$A(\mathbf z)=3\delta N(A(\mathbf w))^2$, so
$\operatorname{Re}A(\mathbf z)=0$. Scaling $\mathbf w$ by
$\alpha\in K^\times$ scales $\mathbf z$ by the positive rational
number $N(\alpha)^2$.

Take $\mathbf w\in\mathcal O_K^3$ primitive as an ideal vector,
let $H=\max_i|w_i|$, and let $c$ be the integer content of $A(\mathbf w)$
in an integral basis of $\mathcal O_K$. Since this ring is a PID,
the common ideal divisor of the coordinates of $\mathbf z$ is exactly
$(\delta\overline A)$. Multiplication by $\delta$ has determinant
three on the integral basis, so the integer content of
$\delta\overline A$ is between $c$ and $3c$. The rational inverse
linear map from $\mathbf z$ to $(\mathbf x,\mathbf y)$ has fixed
denominators. Consequently the resulting primitive rational point has
height

$$
B\asymp H|A(\mathbf w)|/c.
$$

Positivity removes the small-$A$ complication: it forces each $w_i$
to lie within angle $\pi/6$ of $A(\mathbf w)$. Hence
$|A(\mathbf w)|\ge\cos(\pi/6)\sum_i a_i|w_i|^3\asymp H^3$,
and $B\asymp H^4/c$ on the relevant cone.

A bound of the proposed shape $O(H^6/G)$ for primitive parameters
with $c\ge G$ would address the collision count. It was **not proved**
in the necessary endpoint range $G\asymp H^3$. There,
$q=A/c\in\mathcal O_K$ ranges over a fixed finite set; fixing $q$
imposes

$$
\operatorname{Im}(\overline q\,A(\mathbf w))=0.
$$

The additional sign is $\operatorname{Re}(\overline q A)>0$.
The fixed rational rotation $\mathbf w\mapsto\delta\overline q\mathbf w$
turns this back into the critical positive cubic collision equation.
Small-modulus divisibility counts do not bound this large-content
range. Thus the parametrization and its checked height formula do not
supply the missing energy or multiplicity estimate.

## The Cartesian-extraction theorem and the entropic sieve

The [Cartesian-extraction theorem](cartesian_extraction.md) applies
to every fixed degree-$r$ diagonal form in $r\ge3$ variables. An
output-defined restriction keeps $1-o(1)$ of all input tuples, but
every Cartesian rectangle inside it has volume at most
$N^r\exp(-c_r\log N/\log\log N)$. The cubic specialization has
vanishing relative entropy from the product law while removing an
exponentially large product-sieve expectation. This checks a concrete
attempt to use the new weighted entropic sieve of Croot, Mao, Pohoata,
Sheffer, and Yip: its independent-coordinate and pointwise bounded-fiber
hypotheses cannot simply be replaced by high input mass or small
relative entropy. The theorem does not prove that the actual
bounded-fiber input set is small, and it gives no density conclusion.

The subsequent [joint congruence calculation](profinite_cubic_density.md)
proves a second-moment bound uniform in every modulus, bounded profinite
entropy, and quantitative convergence of the local densities for
$x^3+2y^3+4z^3$. It also gives exact descent by 27 and the complete
$3$-adic distribution. These do not control integer-box fibers: the
required comparison between complete residue boxes and roots of size
$N$ at output scale $N^3$ remains unproved. No additional target case
was settled here.

The requested proof is incomplete. The established infinitude cases
remain $r=3,4$; the density question for every $r\ge3$ and infinitude
for $r\ge5$ are unresolved in this work. The new collision, resonance,
and sieve arguments have been documented with their hypotheses and
scope, and none is asserted to supply the missing global estimate.

Possible further work is provisional: all-nonzero near-neighbor
existence, minor-arc correlation with heavy fibers, a joint estimate
for the bilinear sums before the lossy Cauchy step, or a different
size-sensitive higher-exponent argument. No such argument is
claimed here.

## Further checks of the structural and Fourier routes

No target case was resolved here. The following additional
statements are proved and have been checked.

The
[extended quintic certificate](quintic_first_moment_barrier.md#6-extending-the-finite-core-family-at-five)
raises the uniform unordered progression mean above $2.468$ by allowing
canonical five-parts in one coefficient. A checked third-moment gap inequality
is useful only below mean two under Poisson moments; above that threshold a
positive-supported law matches all three moments. This does not estimate the
actual collision moments or prove gaps.

The [congruence-preserving sampling theorem](congruence_preserving_thinning.md)
constructs synthetic integer multiplicities with the actual cubic marginals
modulo $N^2$ and every fixed modulus, the same joint profinite limit, and
all the established pointwise and integrated major-arc estimates. Their
support is only $O(N^2\log N)$ although their mass is $N^3$, and their
logarithmic multiplicity is at least $\log N-\log\log N-O(1)$. The missing
minor-arc correlation can carry essentially the entire mass. These are
not polynomial representation functions: their Fourier transform need
not factor into three cubic sums. The theorem pinpoints the need for
additional factorization or integer-fiber information, rather than
settling the density question.

The
[nearest-neighbor Pell family](energy_and_multiplicity.md#nearest-neighbor-secants-need-not-decrease-height)
gives reciprocal nearest positive cubic neighbors whose third secant point has
height more than six times the endpoint height asymptotically. It excludes a
universal secant descent but not an averaged argument. Also, the
[constant-field norm obstruction](finite_core_reduction.md#a-fixed-number-field-norm-cannot-equal-the-diagonal-form)
rules out an identity expressing the diagonal form as a norm from a fixed
nontrivial number field, even by rational functions. Reduced norms and varying
fields are outside that statement.

### A cofinite abstract model with the available dilation properties

The proposed dilation-only proof of higher-exponent gaps has a precise
obstruction. Fix an $r$-th-power-free integer $t>1$, and define

$$
R(n)=\sum_{d^r\mid n}\mathbf1_{n/d^r\ne t}
=\tau_r(n)-\mathbf1_{\{n=tm^r\}},\qquad
\tau_r(n)=\prod_p\left(\left\lfloor v_p(n)/r\right\rfloor+1\right).
$$

This abstract nonnegative count vanishes only at $t$. Indeed,
$\tau_r(tm^r)=\tau(m)$, and hence

$$
R(tm^r)=\tau(m)-1=\sum_{h\mid m}A(h),
\qquad A(1)=0,\quad A(h)=1\ (h>1).                       \tag{2}
$$

Its mean has the strong estimate

$$
\sum_{n\le X}R(n)
=\sum_{d\le X^{1/r}}\lfloor X/d^r\rfloor
 -\lfloor(X/t)^{1/r}\rfloor
=\zeta(r)X+O_r(X^{1/r}).                                \tag{3}
$$

Here the tail $X\sum_{d>X^{1/r}}d^{-r}$ and the floor errors are both
$O_r(X^{1/r})$. For every nontrivial $r$-powerful $k$, at least one prime
exponent increases by $r$ or more, so
$\tau_r(nk)\ge\tau_r(n)+1$. This offsets any increase of the subtracted
indicator, proving $R(nk)\ge R(n)$.

Thus an initial missing seed, bounded mean, closure under every powerful
multiplier, and the exact primitive-denominator convolution are compatible
with a cofinite support. In this model the minimal represented multipliers
on the missing ray are precisely all primes. It is not the actual
representation function of powerful sums, and asserts nothing about that
function's support. A higher-exponent proof needs arithmetic information
not contained in these structural properties.

## A controlled secant stratum, no target resolution

The
[secant-slice estimate](cubic_collision_ranges.md#a-uniform-bound-on-each-secant-ratio-slice)
is uniform and has no logarithmic or epsilon loss. For a primitive direction $k$
of height $K$, a fixed step $t$, and one prescribed value of $B/C$, there are
$O(1+N/K)$ collision endpoints. The proof intersects an affine plane of lattice
covolume comparable to $K^2$ with a nonsingular conic and counts parallel
lattice lines.

Its
[bounded-denominator consequence](cubic_collision_ranges.md#fixed-normalized-ratios-and-bounded-denominators)
bounds short collisions by $O(D^2N^2H/\eta)$ when the reduced denominator of
$B/(tC)$ is at most $D$ and $|F(k)|\ge\eta K^3$. This yields bounded energy and
a vanishing near-neighbor existence limit on each fixed $D,\eta$ stratum. There
is no estimate for the complementary input mass as $D\to\infty$ and
$\eta\downarrow0$. Thus it does not close the positive-density criterion.

The
[binary-norm calculation](energy_and_multiplicity.md#a-binary-norm-majorant-cannot-be-bounded-on-positive-input-mass)
checks a separate failed simplification. For $Q=x^2-xy+y^2$, the number of split
prime factors is asymptotic to $\log\log N$ in probability on a root box,
forcing unbounded logarithmic norm multiplicity on every positive-mass input
restriction. This excludes discarding the binary trace condition and then
selecting a bounded norm-divisor subfamily; it does not estimate the actual
cubic fibers.

### What cofiniteness would force on a missing ray

For this statement use all canonical cores and every number of summands
$1\le j\le r$, not just a fixed form. Fix $t\notin S_r$, and let
$R_t(m)$ be the number of unordered powerful-sum representations of
$tm^r$. In each summand use its unique canonical expression $d_i x_i^r$.
Let $A_t(h)$ count such representations of $th^r$ satisfying
$\gcd(h,x_1,\ldots,x_j)=1$. Every count is finite. Extracting
$g=\gcd(m,x_1,\ldots,x_j)$ gives the exact identity

$$
R_t(m)=\sum_{h\mid m}A_t(h),\qquad A_t(1)=0.             \tag{4}
$$

Canonical uniqueness makes this operation well-defined also for
unordered representations.

If $S_r$ were cofinite, then $A_t(p)=R_t(p)\ge1$ for every sufficiently
large prime $p$. Hence, for some fixed $P_0$,

$$
R_t(m)\ge\omega_{>P_0}(m),\qquad
\sum_{m\le M}R_t(m)\ge M\log\log M-O_t(M).              \tag{5}
$$

The mean bound follows by summing $\lfloor M/p\rfloor$ over
$P_0<p\le M$ and using the prime harmonic sum. Also
$\omega_{>P_0}(m)$ tends to infinity in density: for any fixed finite
prime set its divisibility indicators become independent in the limit
by CRT, with variance at most their mean; the means over increasing
finite prime sets diverge, so Chebyshev applies. Thus cofiniteness would
force divergent typical multiplicity on this ray.

This gives no contradiction to the available estimates. In particular,
if one hypothetically had
$\sum_{h\le H}A_t(h)\sim cH$ with $c>0$, then partial summation in
(4) would give

$$
\sum_{m\le M}R_t(m)
=M\sum_{h\le M}\frac{A_t(h)}h
+O\left(\sum_{h\le M}A_t(h)\right)
=cM\log M+o(M\log M),                                  \tag{6}
$$

which is compatible with (5). No asymptotic for these actual primitive
counts is asserted. An $o(M\log\log M)$ upper bound would disprove
cofiniteness, but it is not proved and is not the consequence of a
linear primitive-point asymptotic. No additional infinitude case was
obtained from this route.

The unresolved targets remain unchanged: no density conclusion for any
$r\ge3$, and no infinitude conclusion for $r\ge5$, was established
here. Further use of the secant slices or of the exact
trace--norm condition is provisional; neither supplies the missing
uniform tail estimate.

## Direct completion attempt: the small-prime ray fails

The missing seed $t=r+1$ does not generate missing targets by repeatedly
scaling by a small prime. In fact, for every prime $q\le r+1$,

$$
(r+1)q^{rk}\in S_r\qquad(k\ge1).
$$

Write $r+1=\sum_j c_jq^j$ in base $q$. Since $r+1\ge q$, its
digit sum is strictly less than $r+1$, hence at most $r$. Thus

$$
(r+1)q^r=\sum_j c_jq^{r+j}
$$

is a sum of at most $r$ positive $r$-powerful integers. Multiplication
by $q^{r(k-1)}$ proves the assertion. This excludes that specific
fixed-ray construction, not missing targets on other rays.

For larger denominator primes, the unresolved issue is still the exact
bounded-root equation, not complete congruence counts. The attempted
positive-density construction likewise still requires the
[cross-coordinate cubic correlation](energy_and_multiplicity.md#the-cross-coordinate-correlation-still-needed)
or a sufficient weaker multiplicity estimate. Neither was established. No new
target case was resolved, and there is no complete proof.

## Checked norm-ratio, transformation, and analytic statements

These results add no target resolution. For $F=x^3+y^3+cz^3$, the
[binary norm-ratio estimate](cubic_collision_ranges.md#binary-norm-ratios-of-small-height)
bounds nontrivial collisions of reduced norm-ratio height at most $D$ by
$O_{c,\varepsilon}(DN^{2+\varepsilon})$. Thus heights at most $N^{1-\eta}$ can
be removed with negligible input mass and logarithmic moment. There is no tail
bound up to the possible height $N^2$. The
[exact entropy identity](energy_and_multiplicity.md#the-cross-coordinate-correlation-still-needed)
separates the already controlled binary multiplicity from the uncontrolled
quantity $H(Z\mid X^3+Y^3+cZ^3)$ for independent uniform inputs
$X,Y,Z\in\{1,\ldots,N\}$. Neither that conditional entropy nor the corresponding
shifted four-cube correlation is estimated here.

The
[balanced-cone observation](cubic_collision_ranges.md#nearly-vanishing-directions-near-a-balanced-positive-ray)
locates nearly vanishing directions near coordinate-swap directions, but the
available thin-sector count is too large at fixed relative distance. It does not
extend the exact coordinate-sharing estimate. Also, choosing different positive
cubic coefficients cannot give the [generic collision quadric a rational
section](energy_and_multiplicity.md#coefficient-choice-cannot-give-this-generic-quadric-a-rational-section):
specialization to positive differences would make it positive definite. Passing
to $\mathbb Q(\sqrt{-3})$ produces a point but returns to the existing
integral-height obstruction.

Two [rational-transformation results](rational_transformations.md) are
also proved. A fixed rational self-map preserving a positive diagonal
form acts on only $o(N^r)$ positive integral inputs unless it is a
monomial symmetry. The nonpolynomial case has the explicit bound
$O_{T,\varepsilon}(N^{r-1+\varepsilon})$. Separately, rational linear
similitude multiplier classes form a finite group of order dividing $r$.
Their integer representatives have summable reciprocals, and such
multiplicative saturation preserves density zero. These results exclude
fixed-map amplification and a nonsummable linear dilation family, not
families of transformations of growing complexity.

The proposed extensions of the quintic first-moment certificate to
additional primitive or subsum restrictions were not completed and are
not adopted as results. The established quintic floor
and its stated scope remain unchanged.

The following checked statements also settle no target case. The
[composition-law argument](rational_transformations.md#no-composition-law-linear-in-one-input)
excludes rational composition laws linear in one input, not arbitrary nonlinear
constructions. The
[fifth-moment inequality](quintic_first_moment_barrier.md#8-a-fifth-moment-gap-certificate)
would force gaps under five Poisson factorial-moment asymptotics of mean at most
$3.1$; neither the required upper bound on the actual progression mean nor those
asymptotics is proved. The
[special target-class estimate](primitive_cubic_fibers.md#three-special-target-cube-classes-have-negligible-input-mass)
removes the targets $2^e m^3$, $e=0,1,2$, for the special cubic at negligible
input and logarithmic-moment cost. No uniform counting consequence for the
remaining surfaces, including from exploratory Picard-rank considerations, is
adopted here.

The new analytic attempts also leave precise gaps. The
[square-class reformulation](energy_and_multiplicity.md#a-square-class-reformulation-retains-the-unknown-collision-mass)
has elementary mass and moment bounds, but its grouped coefficient at square
class $3$ is exactly the unknown majorant $T_N$. Ignoring this coefficient in a
quadratic large-sieve application is invalid; an explicit abstract weight
example shows that the two proposed moment bounds alone would not suffice. The
[truncated restriction theorem](cubic_major_arcs.md#truncated-restriction-estimates-leave-a-moderate-amplitude-range)
controls only high Fourier amplitudes, and its combination with the available
lower moments retains a power of $N$. The
[packing calculation](energy_and_multiplicity.md#what-the-available-packing-estimate-actually-yields)
likewise controls only fibers of polynomially growing size, not fixed large
size. None of these calculations excludes a sharper estimate using the
additional arithmetic structure.

For the higher-exponent rays, the exact identity
$6\cdot7^5=2^5+2^{12}+3^8+2^7 3^5+3^{10}$ also excludes a proposed
uniform obstruction for all primes larger than the seed. Attempts
with moduli exceeding the root scale did not establish either a
below-one full unordered representation mean or a tail estimate
uniform on the selected progression. No global basis obstruction
or large/composite-exponent positive-density construction was proved.

Further work, if undertaken, would need a new estimate for primitive
integer fibers or their unrestricted ratio tails, or a genuinely
size-sensitive higher-exponent argument with the coefficient tail
included. These are provisional ideas, not claims that the present
reductions can be completed. The density question for every $r\ge3$
and infinitude for $r\ge5$ remain unresolved here. The proof is
incomplete.

## New multiplicative and analytic trials: checked obstructions

The [matrix-composition attempt](cubic_matrix_composition.md) embeds
$a x_1^3+b x_2^3+a^2b x_3^3$ as the determinant of an explicit
three-dimensional matrix family. This includes the special cubic.
It avoids the fixed number-field norm obstruction, but ordinary
products can be conjugated back only on two proportional-coordinate
loci. Their product values up to $T$ number
$O(T^{2/3}(\log(2T))^2)$, even with arbitrary input-dependent
conjugating matrices.

A modified product does remove both trace obstructions. Its determinant
is an explicit sextic $H$, not the product of the original determinants.
Even scalars chosen separately at every positive integer input cannot
repair this on a substantial product set: coefficient-uniform
Bombieri–Pila bounds give
$O_\varepsilon(T^{17/18+\varepsilon})$ admissible input pairs with
product at most $T$. The proof includes all unbalanced root heights.
The matrix identities were checked by an exact
[symbolic certificate](evidence/util/cubic_matrix_composition.py).
These statements exclude this composition mechanism, not arbitrary
nonlinear constructions or positive density of the original value set.

The [generating-function calculation](generating_function_positivity.md)
tests cofiniteness through positivity after subtracting an integer-tail
pole. All fixed finite tests at rational or irrational limiting angles,
including $O(t)$ angular offsets, reduce precisely to the progression
first moments. The quintic floor makes their limiting matrices strictly
positive, so even lower-order terms cannot contradict cofiniteness in
such a fixed test. Increasing-complexity tests remain outside the result.

The
[local-repair lemma](critical_covering.md#an-arithmetic-obstruction-to-local-repair)
is another checked restriction: for fixed nonzero $h$, only $o(X)$ targets
$n\le X$ admit representations of both $n$ and $n+h$ whose matched physical
roots are within $B^{1/(r-1)-\eta}$, where $B=X^{1/r}$. Its proof sums a
fixed-core binary norm-divisor bound and removes the core tail at the
target-existence level. Cofiniteness does not force such small jumps, and the
elementary cap-packing scales do not meet the counting estimate.

No additional target case was resolved. Density for every $r\ge3$
and complement infinitude for $r\ge5$ remain open here. A different
composition operation, growing-complexity analytic test, or arithmetic
root-coherence argument would require new input; these are provisional
possibilities, not reductions claimed to solve the problem.
