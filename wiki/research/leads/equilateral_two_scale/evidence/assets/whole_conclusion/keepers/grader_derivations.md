---
desc: |
  Independent derivations and attempted breaks supporting the grade of the
  frozen whole-conclusion review of Problem 173.
---

# Derivations supporting the whole-conclusion grade

***

These are the grader's mathematical checks on the subject frozen on
2026-10-17 and the complete report examined on 2026-10-17 UTC. They support
`wiki/research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade.md`.
They are not new claim cards or a second commissioned review cycle. The
project mathematics being examined is attributed to Plasma AI. The native
inputs are identified by the asset home's `subject_manifest.json`; the source
editions and external theorem boundaries are stated in the grade.

## 1. Attempts to break the algebraic finite quotient

The first attack was to replace the proposed finite quotient by an arbitrary
infinite algebra and check whether the argument accidentally uses finite
generation. It does not suffice that the ambient function field has finite
degree over a rational function field: its subalgebras can have infinitely
many generators or invert infinitely many denominators.

Use the supplied notation: $E$ is the algebraic numbers in $\mathbb C$,
$F=E\cap\mathbb R$, $B=E(T)$, $N/B$ has degree $d$, and
$A=\operatorname{span}_E K_N$. A hypothetical normalized functional
$\lambda$ and finite cover $Q$ are the contradiction assumptions. The algebra
$A$ contains $E[T,T^{-1}]$, is stable under conjugation, and contains the
inverses of its spanning unit vectors. No assertion $A=N$ is needed.

For general position over $B$, the real fixed field $N_0$ spans $N=N_0(i)$
over $B$. If a $B$-linear functional killed all Cayley units, the constant and
linear coefficients of its rational identity at $z=ha$ would kill $1$ and
$ia$ for every $a\in N_0$. Because $i\in B$, that kills $N_0$ as well.
Thus the functional is zero. In coordinates over the infinite field $F(x)$,
a finite product of nonzero numerator polynomials cannot vanish on the whole
grid. This proves arbitrarily large general-position selections without
assuming continuity of the functional.

The cover makes a Cauchy transform rational only after an actual parameter
argument. If $r(T)=P(T)/Q(T)$, then

$$
\frac{r(T)-r(a)}{T-a}
=\frac{P(T)Q(a)-P(a)Q(T)}{(T-a)Q(T)Q(a)}.
$$

The numerator after cancellation is a polynomial in $T,a$. It is therefore
a finite sum of fixed rational functions of $T$ times rational functions of
$a$. This is the required separation before applying an $E$-linear
functional; $a$ is algebraic, whereas $T$ is not.

The admissible pairs $b=1/\bar a$, $a\ne0$, $|a|\ne1$, are not confined
to a complex algebraic curve. Indeed

$$
a=s+it,\qquad b=(s-it)^{-1},\qquad
s=(a+b^{-1})/2,\quad t=(a-b^{-1})/(2i)
$$

are inverse rational changes of variables on open subsets. The real
algebraic grid in $(s,t)$ is Zariski dense over $E$. Removing the circle
condition and finitely many poles leaves it dense. Direct conjugation gives
$|a(T-b)/(T-a)|=1$. Thus the functional cover applies after removing a
nonzero scalar in $E$.

With more than $J(d-1)$ general-position rows, one cover index occurs on at
least $d$ rows. Their invertible matrix gives finitely many possible branches

$$
F_\lambda(a)=R_\beta(a)+S_\beta(a)/(a-b).
$$

A finite partition of a dense subset of an irreducible plane has a dense
part. The Cartesian square of that part is dense in four variables: a
polynomial vanishing on it first has all its coefficients in the second pair
zero on the first part, and then is identically zero. Removing $a=c$ and
the finitely many poles preserves this argument.

Here is the decisive coefficient check, independently expanded. Put
$h=a-b$, $k=c-e$ and $H(a)=V(a)+W(a)/h$. One factor of the product cover
on two units must be the zero rational function:

$$
L+hH(a)+kH(c)+\frac{hk}{a-c}(H(a)-H(c)).
$$

Its coefficients in the independent variables $h,k$ are

$$
\begin{array}{c|c}
hk&(V(a)-V(c))/(a-c)\\
h&V(a)-W(c)/(a-c)\\
k&V(c)+W(a)/(a-c)\\
1&L+W(a)+W(c).
\end{array}
$$

The first makes $V$ constant. The second, as $a$ varies independently of
$c$, then makes that constant zero and $W=0$. The last gives $L=0$.
Pigeonhole and the invertible row matrices imply $S_\beta=0$. Using two
different dense branches yields equality of their $R$ vectors in the same
way. The exceptional branch sets lie in a finite union of proper algebraic
sets. The rational vectors therefore agree with the exact transforms on a
dense parameter set, which is enough for each rational identity used later.

The space containing all these vectors is fixed before the functional
varies. Its generators consist of finitely many row inverses and divided
differences, with finitely many scalar functional values as coefficients.
This supplies a common finite-dimensional space $W$ and a uniform bound on
polynomial degrees at infinity. It also applies to the translates
$\lambda_v(z)=\lambda(vz)$ for units $v$, without normalization.

A finite relation among units gives the same relation among their exact
transforms. Intersecting finitely many generic parameter sets gives the
relation among their rational vectors, so these vectors define a linear map
$\Phi:A\to W$. The identity

$$
\Phi(Tv)=a\Phi(v)+\Lambda(v),\qquad
\Lambda(v)_\ell=\lambda(vb_\ell)
$$

holds first for units and then linearly on $A$. If $\Phi(v)$ had polynomial
part of degree $q\ge0$, the polynomial part of $a^m\Phi(v)$ would have a
term of degree $m+q$. Its proper part and all accumulated correction terms
have degree at most $m-1$, so cannot cancel that term. This contradicts the
uniform degree bound. Every $\Phi(v)$ is strictly proper. Consequently
$\Lambda(v)$ is minus its $a^{-1}$ coefficient, and $\ker\Phi$ is stable
under multiplication by $T$.

Let $p$ annihilate the induced operator on the finite-dimensional image of
$\Phi$. Then $\Phi(p(T)v)=0$, hence $\Lambda(p(T)v)=0$; the coordinate
$b_1=1$ gives $\lambda(p(T)v)=0$ for all $v\in A$.

The possible non-Noetherian obstruction now has an exact answer. Given
$d+1$ representatives in $A$, choose a dependence over $E(T)$, clear the
coefficients' denominators, and divide them all by the largest common power
of $T-a$. At least one remaining coefficient has nonzero value at $a$.
Reducing in $A/(T-a)A$ produces a nontrivial $E$-linear dependence. Thus

$$
\dim_E A/(T-a)A\le d.
$$

Multiplication by $(T-a)^j$ gives a surjection from this space to each
successive layer, so $\dim_E A/(T-a)^mA\le md$. Factor $p$ over $E$ and
use polynomial Bezout identities, which remain valid in $A$. The resulting
Chinese remainder decomposition gives $\dim_E A/p(T)A\le d\deg p$.
This remains valid if localization has made one quotient zero. If the whole
quotient is zero, the descended normalized functional is already impossible.

There is no residual pole loophole in a nonzero quotient. Real elements of
$A$ span it over $E$, even if the ideal $p(T)A$ is not conjugation invariant:
real and imaginary parts span $A$ before taking the quotient. Choose real
representatives $z_i$ whose images span the quotient. For real algebraic
parameters $t_i$, let $z=\sum t_i z_i$. The Cayley denominator is a unit
already in $A$, since

$$
(1-iz)^{-1}=\frac{1+(1+iz)/(1-iz)}2\in A.
$$

Its image is therefore invertible in the quotient. In finite algebra
coordinates the cover is a product of rational functions of the $t_i$,
zero on the full real algebraic grid. One factor is identically zero. Its
derivatives at zero are $2i\lambda(q_jz_i)=0$. Since $q_j$ is a unit and
the images of the $z_i$ span, this contradicts $\lambda(1)=1$.

The algebraic-to-rational template conversion was tested independently of
this quotient. Failure of every finite algebraic-coefficient template gives
an infinite finitely branching tree of consistent selectors. Along a branch,
$1$ is outside the span of all selected vectors, since membership would have
a finite witness. Define a functional on that span plus $E1$, then extend it
linearly. This is algebraic linear extension, not compactness of the
coefficient field. It gives the prohibited cover.

For a successful finite template, only finitely many coefficients for all
selectors are needed. Put them in one conjugation-stable number field and
apply rational general position in each finite block. In the number-field
argument a rational functional killing all Cayley units kills $1$, $ia$ and
$a^2$ by expansion in a rational parameter; squares span the real field
because $4a=(a+1)^2-(a-1)^2$. The required general position follows by the
same polynomial-grid reasoning. Overlapping blocks restrict a global
selector and cause no loss of the pigeonhole argument within each block.
For algebraic $x$ the original number-field selection applies directly.
The attempted finite-generation and pole attacks therefore fail.

## 2. Conditioning, tower termination and the order of limits

An unconditional wild law can become singular on a coset after conditioning;
the null-coset lemma alone is not the required theorem. The report does
examine the stronger relative-singularity proof.

For the preliminary lemma, a positive-mass coset of the Borel subgroup $C$
has a finite rotation orbit. The image of the divisible abelian rotation
group in this finite permutation action is trivial. Thus $(u-1)d\in C$;
any $u\ne1$ and invertibility of the scalar give $d\in C$, a contradiction.
Continuity on two nonparallel real-field lines gives continuity on the
plane. Infinitely many rotated line events are pairwise disjoint modulo
$C$, so each has measure zero. These arguments still hold over $F_x(i)$.

The line functional $I$ is defined on all bounded functions of bounded
support by periodization and an invariant mean on $F_x/\mathbb Z$. The
agreement with ordinary integrals is needed only for continuous compactly
supported tests. A continuous vector for multiplication by $\psi_{at}$
would have a continuous positive-definite coefficient on $\mathbb R$.
Bochner and uniqueness on the compact dual would concentrate its spectral
mass on the null continuous-line event. Hence that vector is zero. The weak
Hilbert integral $I(\phi(t)\psi_{at})$ is continuous, since its translation
difference has norm at most $\int|\phi(t-s)-\phi(t)|dt$; it is therefore
zero. No ordinary measurability of the wild Fourier coefficient is assumed.

At a supposed first failed tower stage, conditional coset mass evaluated at
a sample is an invariant function on the ergodic ambient system. It is a
positive constant $a$. Each sampled coset then has mass $a$, and finite
additivity on disjoint Borel cosets forces exactly $m=1/a$ cosets exhausting
the conditional law. There cannot be residual mass distributed over
zero-mass cosets: it would contradict this almost-sure constant value.

The map assigning a center to a positive-mass coset uses its probability
kernel, not an arbitrary selector for the possibly nonsmooth quotient by
$C$. For the location objective in the source, the integrand is bounded by
$|s|$, so no first moment is needed. More than half the measure in a bounded
ball gives coercivity; strict convexity gives uniqueness; rational
approximate minimizers give Borel measurability. Translation and orthogonal
covariance make the center well defined on a coset and equivariant. The
factor generated by these centers is ergodic and its center law remains
wild, because no positive-mass conditional coset is $C$ itself.

The finite collision argument was checked with its quantifiers intact:

1. Fix the phase tolerance, then a finite Fourier-moment test for a small
   arc, then the approximation error and its fixed bounded basis over an
   earlier factor $W$.
2. Fix a finite coefficient-bin count $L$, then choose $M$ with
   $0.9M/L>10m^2$.
3. Universal induction applies to the new center factor and its unchanged
   earlier tower through $W$. Its nonnegative coefficient
   $p(a)=\|\mathbb E(\psi_a(b)\mid W)\|_2^2$ has zero line mean.
4. A finite sum of tests $p(n(j-l)t)$ has zero line mean, so one nonzero
   sufficiently small $t$ makes all tests small. This uses positivity, not
   countable additivity of the invariant mean.
5. Markov's inequality and a finite union bound make all pairwise
   conditional collisions small simultaneously on most $W$-fibers. The
   fixed compact approximations also have small conditional error on most
   fibers.
6. Only after choosing a fiber in the intersection is a common bin and its
   index set $J$ selected.

Each $x_j=jt$ is a sum of two unit directions in the real-closed field.
Matching both corresponding phase lists does not require the same center
in the two matches. It gives at most $m^2$ products, not $m$. The
conditional expected fraction $q$ of matched indices is greater than
$0.95$, and $|J|>10m^2$. Therefore the collision lower bound for distinct
random indices exceeds

$$
\frac{\mathbb E(q^2\mid W)}{m^2}-\frac1{|J|}
>\frac{0.95^2-0.1}{m^2}
>\frac1{4m^2}.
$$

Every pair in the original index set already had a simultaneous strict
upper bound $1/(4m^2)$ on that fiber. Selecting $J$ there cannot evade it.
This closes the induction step, including a limit stage where the bounded
phase encoding is first approximated on an earlier successor factor.

The compact tower does not assume its termination. A nonconstant invariant
bounded kernel on a nonergodic relative product gives a nonzero measurable
Hilbert--Schmidt operator field annihilating constants. A fixed positive
spectral cutoff has positive finite rank, constant by ergodicity of the
factor. Bounded polynomial approximation to the spectral cutoff, applied
to measurable dense sections, gives measurable projected sections and a
fiberwise orthonormal basis. Equivariance makes the sum of their squared
absolute values invariant on the original system; it equals the rank and
bounds every basis function. Adjoining them gives a strict extension with
the required finite bounded approximation. If strict extensions continued
through all countable ordinals, one could select uncountably many mutually
orthogonal vectors in a separable Hilbert space. This proves termination.

The multiple-average proof uses the invariant projection for the powered
representation itself. Surjectivity of $u\mapsto u^n$ identifies its invariant
vectors; no claim about unweighted images of finite Følner sets is used.
The pair criterion follows on the ergodic relative product, and passes to
that product over $Y$ by expanding simple tensors and bounded finite
rectangle approximations.

In the higher-order induction, subtracting one exponent leaves distinct
nonzero exponents. Expand the shifted factors into conditional means and
centered terms. Lower-order induction kills the latter. The remaining
correlation is bounded by
$\|P(U_{h^{n_*}}v_*\bar v_*)\|_2$, even when the centered factor was the
unshifted one. Its averages vanish along every Følner sequence. This implies
uniform vanishing over translates of a fixed sequence: bad translates of a
subsequence would themselves be Følner in an abelian group. In the
van der Corput estimate the original averaging limit is taken first for a
fixed finite shift set, and only then does that shift set grow. Finally a
common shift of all exponents inside a scalar invariant integral removes
zero exponents. The necessary limit orders and zero cases are supplied.

These results give the radial difference inequality and the every-Følner
identity. If $m(r)>0$, a suitable bounded-cost set of rotations is syndetic;
otherwise bad translates would contradict that identity. The rational
template then gives finitely many selections spanning both $1$ and $i$.
Clearing denominators and taking a minimum on the ordinary compact unit
circle give constants $D_0,M_0,c_0$ for these fixed data. None must be
uniform in $x$. Signed additions of lengths can be performed modulo their
maximum, with cost at most $4H$ per input by the difference inequality.
This gives a positive lower bound for $m$ on a real-field interval, contrary
to the line mean. Fourier uniqueness and ergodic decomposition complete
Haar rigidity. The conditional and limit-order attacks fail.

## 3. Pair preservation and a measurable coloring

The distinction between unitary and Koopman representations is important.
For any unitary representation of the discrete carrier, the continuous
vectors are the spectral range of the Borel ordinary-character subgroup
$C$: one direction is dominated convergence, the other extends a continuous
positive-definite coefficient to $\mathbb R^2$, uses Bochner there, and
uses uniqueness on the compact dual. Even for a nonseparable representation,
this scalar argument applies to each vector; the countable cyclic part is
sufficient.

For a rotation-fixed vector, its spectral measure and both restrictions to
$C,C^c$ are invariant. Haar rigidity applies to the normalized latter
restriction if it is nonzero. Its Fourier coefficients vanish at nonzero
translations. Orthogonality of the two invariant spectral subspaces proves
the stated pair-correlation identity. This says nothing false about the
zero translation.

In the labeling application the operators are Koopman. Their bounded
continuous vectors are closed under products, conjugation and Lipschitz
composition. Indicators in the subspace form a sigma-algebra; threshold
approximations and density of simple functions identify its $L^2$ with the
subspace. Thus projection is conditional expectation and sends the origin
sign to $g\in[-1,1]$. An arbitrary orthogonal projection would not suffice.
Amenability produces an invariant probability on the compact space of
avoiding labelings without integrating the original nonmeasurable coloring.

For three distinct template vertices, every edge displacement is nonzero,
including in the collinear case. The original signs and the pair identity
give $1+\kappa(ua)+\kappa(ub)+\kappa(u(b-a))=0$. Continuity extends this
from carrier rotations to every ordinary unit direction. The constant $1$
is the integrated constant from the original sign identity; it is not
replaced by the possibly smaller $\|g\|_2^2$.

For $s_1,s_2,s_3\in[-1,1]$,

$$
Q=1+s_1s_2+s_1s_3+s_2s_3
=\frac{\prod(1+s_i)+\prod(1-s_i)}2.
$$

Both products are nonnegative. Equality holds exactly when some coordinate
is $1$ and another is $-1$. At each fixed placement the integral of $Q$
is zero, so $Q=0$ almost surely there.

This is not yet a simultaneous statement for uncountably many placements.
Choose Borel countable-range approximants to the translation parameter with
uniform $L^2$ error at most $2^{-n}$. Bounded representatives of the
countably many translates give jointly Borel functions. Their successive
$L^1$ differences are summable for each fixed parameter, so their pointwise
limit, set to zero where it does not exist, represents the desired vector
for every fixed parameter. Tonelli on each bounded spatial disk and the
circle gives a conull sample set for each template and disk. The family is
countable, so one sample works for all of them. Thresholding preserves both
endpoint signs and gives the Borel weak avoider. No common pointwise action
of the uncountable group or universal exceptional sample set was assumed.

The reverse transfer uses a different implication. Three density-one points
of one color would, after a small translation and rotation, give a
monochromatic copy with probability tending to one. Each displaced vertex
has density bounded by $1/(\pi h^2)$ in a disk of radius $2h$, so the density
hypotheses justify this by a union bound. Weak avoidance forbids it. Every
finite point set has a translate into the conull union of the two density
classes. Product compactness gives an arbitrary avoiding coloring. It does
not give a measurable completion on the exceptional null set.

## 4. Finite forcing, collinear cases and exact carriers

For $a>0$, $z\ne0,a$, use the supplied eight coordinates and
$\omega=e^{i\pi/3}$. Direct substitution in the six motions sends the
ordered base $(a,0,z)$ to

$$
(B,A,D),\ (C,A,B'),\ (C,B,D'),\ (B',A',D'),\ (C',A',B),\ (C',B',D).
$$

The multipliers are respectively $1,\omega,-\bar\omega,-1,-\omega,
\bar\omega$; their translations are $0,0,a,a+\omega z,a+\omega z,\omega z$.
For example the last map sends $z$ to $(\omega+\bar\omega)z=z$ and $a$
to $a\bar\omega+\omega z=C'$. These are direct isometries for either
orientation of $z$, including real $z$ outside the base segment.

The displacement pairs for the six equilateral triangles are

$$
(a,a\omega),\ (-a,-a\omega),\ (z,\omega z),\ (-z,-\omega z),
\ (z-a,\omega(z-a)),\ (a-z,\omega(a-z)).
$$

Every side is positive. Different named vertices may coincide, but none of
these individual equilateral triangles or the six direct copies loses a
vertex. A coincidence can only make the forced-color contradiction occur
earlier. The two finite coloring implications follow by propagating the
forced opposite color around the six triples, as the report details.

For positive measure, right composition by $(t,v)$ sends
$(p,u)$ to $(p+ut,uv)$. In local angle coordinates its Jacobian has identity
translation block and angle derivative one, hence determinant one.
Consequently a finite union of such preimages of null monochromatic sets is
null. Both finite forcing implications remain true for positive-measure
occurrence. This is verified in the motion group's actual measure and does
not rely on a false assertion that every group's left Haar measure is right
invariant.

If two missing equilateral lengths satisfy $a<b$, the valid triangle with
sides $(a,b,b)$ would have to be missing by the second forcing implication.
Conversely, every non-equilateral triangle has at least two different
positive sides, so at most one missing equilateral length leaves a usable
side for the first implication. This proves the equivalence with the whole
triangle assertion, including every collinear triple of distinct points.
The equilateral two-scale contradiction rescales a missing pair to $1,b/a$;
all-real quantification is essential here.

The carrier converse preserves exact constraints, not approximate distances.
For each finite plane point set, its finitely many relevant triples are
encoded by their orientation and squared-side equations with parameters
$x,\sqrt3$. Real-closed transfer realizes them in $F_x^2$. Positive side
length preserves each triple's distinct vertices. Unrelated vertices may
coincide without harming a coloring pulled back along the realization.
Finite constraint compactness then gives a whole-plane avoider. This
converse is not used circularly in constructing the invariant law from an
already given arbitrary coloring.

## 5. Infinite range behind the finite Bessel calculation

The positive and negative reproductions verified the retained nine exact rational
rows and scalar margins, and rejected the stated false upper bound under
optimized Python. This does not by itself prove any assertion about all
arguments or all ratios.

For $q\le10$, after the omitted term of index $21$ the absolute-term ratio
is $q^2/[4\cdot22(22+\nu)]<1$ and decreases. Thus the alternating tail
really puts $J_\nu(q)$ between the displayed degree-21 and degree-20 sums.
For $0<t\le3$, the analogous lower polynomial for $2J_1(t)/t$ is
$P(y)=1-y/2+y^2/12-y^3/144$, $y=t^2/4\le9/4$. Its derivative is
$-((y-4)^2+8)/48<0$, and $P(9/4)=223/1024>0$. Hence no positive zero of
$J_1$ lies at most three.

For consecutive positive zeros $a<b$, the ODE for $\sqrt t J_1(t)$,
integration by parts and Wirtinger give $b-a>\pi$. The signs at $19/5$
and $4$ locate the first zero between them; another zero in $(3,4)$ would
violate the spacing. There is no second zero before $24/5$ or third before
$10$. The zeros are simple by ODE uniqueness. Between $24/5$ and $10$ there
can therefore be only a local maximum of $J_0$, so its minimum is at an
endpoint. This reasoning also covers the possibility of no such critical
point in that interval.

The decreasing energy $J_0^2+J_1^2$ and the checked endpoint values imply
$J_0>-.403$ globally, $J_0>-.25$ on $[24/5,\infty)$, and $J_0>-.261$ on
$[0,3]$. Strict decrease of energy after the first critical point, where
$J_1=0$ and $J_0<0$, proves the stated global minimum there. The exact
energy slacks are $15583/100000000$ and $3/62500$.

For $x\ge3/2$, if one of $t,xt$ is outside $(3,24/5)$ these inequalities
give $J_0(t)+J_0(xt)>-83/125$. If both are inside, then
$3<t<16/5<t_0<9/2<xt<24/5$, and monotonicity and the two endpoint rows
give a stronger lower bound $-642/1000$. Taking an infimum gives the
non-strict bound $m(x)\ge-83/125$, whose gap from $-2/3$ is exactly
$1/375$. Substitution proves $m(x)=m(1/x)$ and includes both closed
endpoints of the claimed outer ranges.

For a weak measurable avoider, a disk cutoff of the sign function has
normalized spectral mass one by Plancherel. Averaging over directions gives
the Bessel transform. Each comparison with the three-sign identity loses
only boundary bands of area $O(rR)$ at a fixed side $r$, including the
translated third pair. Thus the two radial correlations tend to $-1/3$.
The constants need not be uniform over all sides at once.

After compactifying the radii by one point, weak limits retain total mass
one but may have mass at infinity. Both Bessel test functions take value
zero there. Their sum integrates to $-2/3$ against a finite-radius measure
of mass at most one. Its lower bound is at least
$\min(m(x),0)>-2/3$, which contradicts that value. Lost mass has not been
silently replaced by a probability on finite radii.

## 6. Circle angles, null boundaries and the external interface

If $A=\arcsin(x/2)$ and $B=\arcsin(1/(2x))$ are both rational multiples
of $\pi$, put $\alpha=2\cos(A-B)$, $\beta=2\cos(A+B)$. Their difference
is one. In a common cyclotomic field the averages of their conjugates are
$\tau(m)=2\mu(m)/\varphi(m)$ for $m\ge3$, with values $2,-2$ for
$m=1,2$. Apart from $1,-1,0$, the possible nonzero values have absolute
value at most $1/2$. The difference-one pairs are exactly

$$
(2,1),\ (1,0),\ (0,-1),\ (-1,-2),\ (1/2,-1/2).
$$

This is a classification of possible trace values, not a numerical scan of
root orders. In the pair $(0,-1)$ it is $\beta=-1$ itself that forces
$\alpha=0$; trace zero alone would not. The angle ranges exclude this and
the pair with $\beta=-2$. The remaining orders give $x=1$, the golden-ratio
pair, or $2\sin(5\pi/12),2\sin(\pi/12)$. The larger element of each
nontrivial reciprocal pair exceeds $3/2$, and the smaller is below $2/3$.
Thus the central unequal-scale interval has at least one irrational chord
angle. Finite forcing supplies weak avoidance of the corresponding
isosceles template with a fixed radius $r\in\{1,x\}$.

The boundary $S$ is where both colors have positive upper density. Ball
averages are continuous in the center and at each positive radius, so the
rational-radius upper/lower limits define Borel sets. Density
differentiation makes $S$ plane-null, not necessarily null on a circle
centered at one of its points.

The apex argument uses a sequence of radii with one color occupying at
least a fixed fraction $\delta>0$ at the apex. If its two other vertices
were density-one points of that color, their wrong-color probabilities
under disk and angular perturbation would tend to zero. The union bound
would give monochromatic probability at least $\delta-o(1)>0$. Thus the
apex prohibition holds at every boundary point.

Suppose the chosen radius circle about a boundary point were boundary-null.
Its red and blue density sets would partition the circle modulo null sets.
The equilateral prohibition forces their measures to be half the circle
and translation by $\pi/3$ to interchange them. The isosceles prohibition
forces the same interchange by $\gamma$. Their indicator minus one half
is then invariant under $\gamma-\pi/3$ and has mean zero. Irrationality
kills every nonzero Fourier coefficient, impossible for this indicator.
The report's Fourier rederivation and the source's closed-subgroup argument
therefore have the required force.

The finer rational-angle consequence also survives. If
$\gamma=2\pi P/Q$ in lowest terms, membership of $\pi/3$ in the subgroup
generated by $2\pi/3$ and $\gamma-\pi/3$ is equivalent to an integer
multiple of $(6P-Q)/Q$ being odd. For odd $Q$ use multiplier $Q$; for
$4\mid Q$ use $Q/2$. For $Q=2q$ with odd $q$, the reduced expression has
even numerator and odd denominator, so no integral multiple is odd. This
gives exactly $Q\not\equiv2\pmod4$.

Thus every point of $S$ has positive circle intersection with $S$, at the
same radius $r$. If $p\in S$, the measurable set of two successive angles
landing in $S$ has positive measure by Fubini: its section is positive at
every first landing point, and no uniform lower bound is needed. The map

$$
(\theta,\varphi)\longmapsto p+re^{i\theta}+re^{i\varphi}
$$

has Jacobian $r^2\sin(\varphi-\theta)$, nonzero off a null set. Its
multiplicity is at most two except over $p$. The area formula would give
positive area to an image contained in $S$, contradicting its nullity.
Therefore $S$ is empty.

This is precisely Lahti's measure-theoretic boundary in formula (2.3), not
a topological boundary. In Euclidean space, completeness, Borel regularity,
doubling, positive finite ball measure and the $(1,1)$-Poincare inequality
hold. Theorem 1.1 on each ball gives finite perimeter from the empty
boundary; formula (2.4) then gives zero perimeter. Applying (2.2) with a
large enough surrounding ball makes one color null on each smaller ball.
Overlapping balls force the same choice throughout the plane. This is the
exact external theorem interface used; its original proofs are not being
reconstructed. A null or conull color contradicts weak avoidance of the
unit equilateral triangle.

## 7. Controls and their logical scope

The null set $\{0\}\cup rS^1$ fills the entire radius-$r$ circle about
zero. At a point on its circular part, however, intersection with that
point's radius-$r$ circle is finite. It defeats a shortcut about every
circle center and does not meet the self-supporting hypothesis just proved.

For the ratio-one control set $h=\sqrt3/2$ and alternate the colors of
$\{(s,t):nh\le t<(n+1)h\}$, $n\in\mathbb Z$. A unit equilateral
triangle has vertical range $R\le1$ and sum of squared vertical edge
projections $3/2$. For three heights of range $R$, that sum is at most
$2R^2$, so $R\ge h$. The triangle cannot lie in one half-open strip.
If monochromatic across strips it can meet only two same-color strips,
since three would require range greater than $3h>1$. One vertex is then
isolated in one strip and its vertical distance from each other vertex is
strictly greater than $h$. Its vertical distance from their midpoint is
also greater than $h$, whereas its Euclidean distance from that midpoint is
exactly $h$. This contradiction proves the claimed single-scale avoider.
It refutes only the strengthening that allows $x=1$.

Likewise, projecting the uniform law on six nonmonochromatic sign triples
to a trivial factor produces zeros and changes each pair correlation from
$-1/3$ to zero. It defeats an arbitrary-projection argument, not the proved
pair-preserving transfer. At $x=1$ the Bessel value at $19/5$ has doubled
value below $-2/3$; continuity gives the same obstruction to that criterion
near one. This explains why the separate central-interval argument is
load-bearing.

None of these controls is a counterexample to the frozen whole conclusion.
The existence of a single-scale avoider comes from its explicit construction,
not from the assertion that at most one scale can be missed. Similarly,
the carrier and transfer equivalences are implications on the existence of
avoiders, and do not themselves assert that their antecedents occur.
