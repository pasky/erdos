---
name: research/erdos_864/obstructions
desc: Explicit failed reductions and algebraic construction obstructions; none is a counterexample to the target.
tags: [proved, obstacles]
sources: []
created: 2026-09-23T02:15:22Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_864/obstructions

***

These are limitations of specific arguments, not evidence that the
Erdős bound is false. The target remains unresolved.

## Reflection completion is not valid in general

For an integer $q\ge13$, let

$$
 D=\{q^i:0\le i<r\},\qquad
 C=\{\pm3q^i:0\le i<r\},\qquad A=C\cup D.
$$

In an equality between two pair sums the coefficient at any power of
$q$ lies in $[-12,12]$. Reduction modulo $q$, followed by
division by $q$, shows that all those coefficients vanish. At a
single exponent, the unordered sums of coefficients in $\{-3,1,3\}$
are $-6,-2,0,2,4,6$, all distinct. A pair using distinct exponents
also determines its two coefficients uniquely. Thus only zero has
multiple representations.

But adjoining $-q^i$ creates

$$
 q^i+q^i=3q^i+(-q^i).
$$

No unpaired element can be reflected while retaining the existing
core. These examples have exponentially large diameter; they do not
exclude a dense asymptotic symmetrization theorem.

### A binary phase does not always repair symmetric completion

Even an ordinary Sidon input need not admit a signed binary lift.
Take

$$
 E=\{-3,-1,2,6\}.
$$

Its ten unordered sums are
$-6,-4,-2,-1,1,3,4,5,8,12$, so it is Sidon, and
$E\cap(-E)=\varnothing$. For arbitrary bits $f_x,e$, consider

$$
 T=\{(f_x,x),(e+f_x,-x):x\in E\}
 \subset\mathbb Z_2\times\mathbb Z.
$$

The second-coordinate sum $-4$ has three distinct representations

$$
 (-3)+(-1)=2+(-6)=(-2)+(-2).
$$

Their lifted sums occupy only $(0,-4)$ and $(1,-4)$.
Two therefore coincide away from the designated exception $(e,0)$.
This proves that universal binary-phase symmetrization is false.
It does not exclude an asymptotic version permitting a negligible
deletion.

A separate span issue remains in any such proposal:
$\mathbb Z_2\times\mathbb Z$ is not cyclic. A lift there is not
automatically an integer construction with twice the original span.

## Two-point continuum packing is insufficient

On $[0,1]$, let the core profile $c$ equal
$a=\sqrt{12/5}$ on the outer thirds and zero on the middle third.
Let the unpaired profile $u$ equal $a/2$ on the middle third and
zero elsewhere. Put $f=c+u$, and let $\widetilde f(x)=f(-x)$.
Then

$$
 \int f=\sqrt{5/3}>2/\sqrt3.
$$

Nevertheless

$$
 Q(t)=(f*\widetilde f)(t)-\tfrac12(c*\widetilde c)(t)
$$

is even and piecewise linear, with

$$
 Q(0)=1,\quad Q(1/3)=4/5,\quad Q(2/3)=2/5,\quad Q(1)=0.
$$

Hence $Q(t)\le1$ for all $t$. These are precisely the coarse
difference-capacity constraints from
$\rho_A-\rho_C/2\le1$. The coarse sum constraint is also satisfied:
since $f$ is symmetric about $1/2$,
$\max(f*f)=\int f^2=9/5<2$.

This profile is not an integer construction. It proves that these
two-point continuum constraints, even at all shifts, cannot alone give
the conjectured constant.

## Fourier uniformity does not supply a four-variable counting lemma

For a Sidon set $B$ of size $b$, the fourth Fourier moment equals
the additive energy $2b^2-b$. At the scale $b\asymp\sqrt L$,
both this diagonal energy and the natural scale for the forbidden count
$x+y+z=w$ are $L$. Controlling only the large Fourier coefficients
does not make the remaining fourth-order contribution negligible.

Ortega–Prendiville's *Extremal Sidon sets are Fourier uniform, with
applications to partition regularity* does prove Fourier uniformity
near the ordinary Sidon maximum, but its partition-regularity application
requires at least five variables. See the hypotheses in the
[primary paper](https://www.numdam.org/item/10.5802/jtnb.1239.pdf).
It does not provide the missing four-variable result.

## A four-fiber template and its remaining cubic conditions

For an abelian group $H$, consider

$$
 T=(1,B)\cup(2,C)\cup(3,-C)\cup(4,-B)
 \subset\mathbb Z_5\times H.
$$

A direct classification by first-coordinate sum shows this is symmetric
Sidon provided

$$
 \begin{gathered}
 B,C\text{ are Sidon},\qquad (B-B)\cap(C-C)=\{0\},\\
 (C+C+C)\cap B=\varnothing,\qquad
 (B+B+B)\cap(-C)=\varnothing.
 \end{gathered} \tag{1}
$$

For instance, in residue one the competing types are $C-B$ and
$-C-C$; their collision is equivalent to $3C\cap B\ne\varnothing$.
In residue two the competing types are $B+B$ and $-C-B$, giving
the other cubic condition. Residues three and four follow by symmetry.
Residue zero consists of the within-fiber differences, whose only common
value must be zero. The disjoint-difference condition also makes every
cross-fiber sum or difference injective.

If $H$ is cyclic, $\gcd(5,|H|)=1$, and
$|B|,|C|\sim\sqrt{|H|/2}$, (1) would give the counterexample constant
$\sqrt{8/5}>2/\sqrt3$. The cubic conditions are not established.

The difference packing itself is achievable. For odd prime $q$, let
$h=(q-1)/2$, let $Q$ be the squares in $\mathbb F_q^*$, let
$\omega$ generate $Q$, and choose a nonsquare $\nu$. In the
cyclic group $H=\mathbb Z_h\times\mathbb F_q$, take

$$
 B=\{(x,\omega^x):x\in\mathbb Z_h\},\qquad
 C=\{(x,\nu\omega^x):x\in\mathbb Z_h\}.
$$

At a nonzero first-coordinate difference $s$, the possible second
coordinates are respectively $(\omega^s-1)Q$ and
$\nu(\omega^s-1)Q$, disjoint, and each occurs once. The first-coordinate
zero difference is only zero. Hence both fibers are Sidon and their
nonzero differences are disjoint.

However, for primes $q\equiv3\pmod4$, $q\ge7$, the first cubic
condition fails. It is equivalent to the absence of

$$
 \nu(u+v+w)=uvw,\qquad u,v,w\in Q.
$$

Since $|Q|$ is odd, the map
$(u,v,w)\mapsto(1/(vw),1/(uw),1/(uv))$ permutes $Q^3$.
The displayed equation is thus solvable if and only if
$1/\nu\in Q+Q+Q$. Cauchy–Davenport gives
$|Q+Q+Q|\ge\min(q,3|Q|-2)=q$.
So this natural full-fiber construction does not work.

## A cyclic conic construction whose quotient fails

Let $q$ be odd, $c\in\mathbb F_q^*$, and $c^2\ne1$. In
$\mathbb F_{q^2}^*$, define

$$
 S_c=\{z:\operatorname{Tr}(z)=c(\operatorname{Norm}(z)+1)\}.
$$

It is inversion invariant, has $q+1$ elements, and is symmetric Sidon
in the multiplicative group. Indeed
$\overline z=(c-z)/(1-cz)$, and if $xy=t\ne1$, the two elements
are roots of

$$
 c(1-\overline t)X^2+
 (\overline t-t+c^2(\operatorname{Norm}(t)-1))X
 +ct(1-\overline t)=0.
$$

Its leading coefficient is nonzero, so the pair is unique. The size
follows from
$\operatorname{Norm}(z-1/c)=1/c^2-1\ne0$.
Also $S_c\cap(-S_c)=\varnothing$.

Quotienting by $\{\pm1\}$ would almost double the squared density,
but introduces nonexceptional collisions for every $q\ge17$.
Here is a uniform proof. Put $a=c^2$ and

$$
 f(t)=a(t+1)^2-4t.
$$

For $t\in\mathbb F_q^*\setminus\{1\}$, a product representation
$xy=t$, with $x,y\in S_c$, exists exactly when
$\chi(f(t))\in\{-1,0\}$, where $\chi$ is the quadratic character.
The two factors must be conjugates of norm $t$ and trace
$c(t+1)$; these are precisely the roots of
$X^2-c(t+1)X+t$. Distinct roots in $\mathbb F_q$ do not qualify,
while nonsquare discriminant or a double root does.

If $a\ne2$, the polynomial $f(t)f(-t)$ is squarefree of degree
four. Each quadratic has nonzero discriminant $16(1-a)$, and common
roots would imply $t=0$, where $f(0)=a\ne0$.
Its leading coefficient is the square $a^2$, so the smooth genus-one
completion of $Y^2=f(t)f(-t)$ has two rational points at infinity.
The Hasse bound therefore gives

$$
 \sum_{t\in\mathbb F_q}\chi(f(t)f(-t))\ge-1-2\sqrt q.
$$

Since $\sum_t\chi(f(t))=\sum_t\chi(f(-t))=-1$,

$$
 \sum_t\frac{(1-\chi(f(t)))(1-\chi(f(-t)))}4
 \ge\frac{q+1-2\sqrt q}{4}.
$$

The at most four roots of the two quadratics contribute at most two.
Thus for $q\ge17$ some $t$ has both characters equal to $-1$.
Such a $t$ is not $0,1,-1$. If $a=2$, then $f(t)=f(-t)$,
and the ordinary quadratic character sum likewise gives a nonsquare
value at some $t\notin\{0,1,-1\}$.
Therefore both $t$ and $-t$ are products from $S_c$, giving
different representations of a nonexceptional product in the quotient.
This rules out this particular density-improvement mechanism, not
other cyclic symmetric Sidon constructions.

The stronger arbitrary-thinning obstruction now
shows that even replacing the full conic by an arbitrary subset cannot
make this sign-quotient scheme improve the target constant.

## A mixed three-fiber construction fails even after arbitrary thinning

This obstruction does not establish an upper bound for general admissible sets.

Let $p$ be an odd prime, $h=(p-1)/2$, $Q$ its nonzero quadratic
residues, $\omega$ a generator of $Q$, and $\nu$ a nonsquare.
In $H=\mathbb Z_h\times\mathbb F_p$ put

$$
 B=\{(x,\omega^x):x\in\mathbb Z_h\},\qquad
 D=\{(x,\nu\omega^x):x\in\mathbb Z_h\}.
$$

For arbitrary $B'\subseteq B$, $D'\subseteq D$, consider

$$
 A=(\{1\}\times B')\cup(\{2\}\times(-B'))
   \cup(\{0\}\times D')\subset\mathbb Z_3\times H.
$$

If only the group sum zero can have multiple representations, then

$$
 3|B'|+4|D'|\le6h+O(\sqrt h),\qquad
 |A|\le\frac{11}{4}h+O(\sqrt h). \tag{2}
$$

Since $3|H|=3hp\sim6h^2$, the latter constant is
$11/(4\sqrt6)<2/\sqrt3$. Thus even arbitrary thinning cannot turn
this particular mixed template into a counterexample.

To prove (2), first note the necessary condition $D'\cap3B'=\varnothing$:
$d=b_1+b_2+b_3$ would give

$$
 (0,d)+(2,-b_3)=(1,b_1)+(1,b_2),
$$

a nonexceptional collision. Parameterize a vertex of $B$ by
$a=\omega^x\in Q$, and a vertex of $D$ by its corresponding
parameter $t\in Q$. The full forbidden triples satisfy

$$
 a+b+c=\nu abc,\qquad t=abc. \tag{3}
$$

Use only triples with three distinct $B$-vertices as hyperedges, each
also incident to its target $D$-vertex.

For fixed $a\in Q$, the number $N(a)$ of ordered choices
$b,c\in Q$ in (3) is obtained from

$$
 c=\frac{a+b}{\nu ab-1}.
$$

Quadratic-character expansion gives
$N(a)=p/4+O(\sqrt p)$ uniformly unless $\nu a^2=-1$.
Indeed the nonconstant terms are a nondegenerate quadratic character
sum and the sum for the cubic
$b(a+b)(\nu ab-1)$; the latter has three distinct roots and is
bounded by $2\sqrt p$ by Hasse. Indicator corrections at zeros and
poles are $O(1)$. The exceptional equation $\nu a^2=-1$ can hold
for at most one $a\in Q$: it requires $p\equiv3\pmod4$, and its
two roots have opposite quadratic characters. In that case
$c=-a\notin Q$, so $N(a)=0$.

Repeated-coordinate triples total $O(p)$: when $a=b$, the third
coordinate is uniquely determined because $\nu a^2\ne1$.
Consequently the hypergraph has

$$
 E=p^2/48+O(p^{3/2})
$$

edges, and every $B$-vertex has degree at most
$p/8+O(\sqrt p)$. For a fixed target $t$, two distinct triples
cannot share a vertex. A common $a$ determines
$bc=t/a$ and $b+c=\nu t-a$, hence determines the remaining
unordered pair. Thus each $D$-vertex has degree at most $h/3$.

Write $b_0=|B'|$, $d_0=|D'|$. The removed vertices must cover
all edges, so

$$
 \frac{p^2}{48}-O(p^{3/2})
 \le(h-b_0)\left(\frac p8+O(\sqrt p)\right)
 +(h-d_0)\frac h3.
$$

Substituting $p=2h+1$ yields
$3b_0+4d_0\le6h+O(\sqrt h)$. Finally

$$
 2b_0+d_0=\tfrac54b_0+\tfrac14(3b_0+4d_0)
 \le\tfrac{11}{4}h+O(\sqrt h).
$$


## Fiber-amplification obstruction

Let $S=-S\subset K\times H$ be symmetric Sidon, and suppose its
nonempty projection to $K$ consists of $r$ pairs $\{a,-a\}$,
with $2a\ne0$. For one representative of each pair, let
$C_a=\{x:(a,x)\in S\}$ and $k_a=|C_a|$.
Every $C_a$ is Sidon, since a collision within that fiber has
nonzero first coordinate $2a$. Their nonzero difference sets are
pairwise disjoint: an overlap gives two distinct representations of
the same nonzero sum $(0,d)$ using opposite fibers. Therefore

$$
 \sum_a k_a(k_a-1)\le|H|-1.
$$

Since $\sum_a k_a=|S|/2$, Cauchy–Schwarz gives

$$
 |S|\le r+\sqrt{r^2+4r(|H|-1)}.
$$

This explains why a small symmetric Sidon pattern with a good
finite ratio cannot simply be amplified by independent large Sidon
fibers while preserving that ratio.

## Optimizing ordinary-Sidon transversals at macroscopic scales

Every set obtained by retaining one element of each reflected core pair and all
the unpaired elements is ordinary Sidon. The possible central element may also
be retained. Thus, for a symmetric set $A=\pm B\subset[-L,L]$ lying in a
translate of $\mathbb Z$, every orientation $X=\{\varepsilon_b b:b\in B\}$
satisfies

$$
 |(X+X)\cap I|\le |I|/2+7|I|^{1/2}(2L+1)^{1/4}
$$

for an integer interval $I$, after an appropriate translation. This is Theorem
1, equation (3.2), in
[source record](../../../library/additive_bases/erdos_et_al_1995_sum_sets_sidon_sets_ii/_index.md).
It includes diagonal pairs.

Optimizing this inequality over orientations does not strengthen the
existing macroscopic energy bound. To see this, normalize the
positive half by $L$, and divide its counting measure by
$\sqrt L$. Along any sequence with a limiting density $g$ on
$[0,1]$, the ordinary Sidon local-difference bound gives
$\int_0^1g^2\le1$. For an oriented limiting density $f$,

$$
 f(x)+f(-x)=g(x),\quad f(x),f(-x)\ge0,
 \qquad \int_{-1}^1f^2\le\int_0^1g^2\le1.
$$

Cauchy--Schwarz then gives $(f*f)(s)\le1$ for every $s$.
These are exactly the limiting sum-interval inequalities, since
unordered sums have limiting density $(f*f)/2$; diagonal pairs
have vanishing normalized mass. In particular $g\equiv1$, which
corresponds to $|B|^2\sim L$, passes every such macroscopic
orientation test. This conclusion does not dispose of a microscopic
orientation argument, but none was established.

## Strict sum-order preservation makes exception repair too expensive

A possible upper-bound strategy would repair an admissible $k$-point
set into an ordinary Sidon set in length $N+k^2/4+o(N)$. Such a
repair would give the target by the ordinary Sidon upper bound.
Unrestricted relocation merely reformulates the target asymptotically;
a construction using the input is required. The following example
rules out a universal repair that preserves every original strict
comparison between pair sums.

For $b\ge2$, put

$$
 x_i=3^{i-1}-\tfrac12,\qquad N=2\cdot3^{b-1},\qquad
 A=\{(N+1)/2\pm x_i:1\le i\le b\}\subset[1,N].
$$

Since $x_{i+1}>3x_i$, domination by the largest uncanceled term
rules out any nontrivial signed relation of length at most four among
the $x_i$. Therefore $A$ is admissible; its only repeated sum
is $N+1$.

Suppose a Sidon integer realization sends the elements corresponding
to $-x_i,x_i$ to $u_i,v_i$ while preserving all strict pair-sum
comparisons. Write $q_i=u_i+v_i$ and $w_i=v_i-u_i$.
Preservation of the diagonal comparisons preserves the order of the
elements, so $w_i>0$. Sidon uniqueness makes the $q_i$ distinct.
The original central sums lie strictly between the sums corresponding
to $-2x_1$ and $2x_1$. Consequently

$$
 2u_1<q_i<2v_1,
 \qquad w_1\ge\left\lceil\frac{b+1}{2}\right\rceil.
$$

The comparisons $2x_i<x_{i+1}-x_i$ and their negative reflections
give, using integrality,

$$
 v_{i+1}\ge3v_i-q_i+1,
 \qquad u_{i+1}\le3u_i-q_i-1.
$$

Equivalently,

$$
 w_{i+1}\ge3w_i+|q_{i+1}-q_i|+2\ge3w_i+3.
$$

Thus the repaired diameter is at least

$$
 w_b\ge 3^{b-1}\left\lceil\frac{b+1}{2}\right\rceil
       +\frac32(3^{b-1}-1)=\Omega(bN).
$$

Here $k=2b$, so this is much larger than $N+k^2/4+o(N)$.
Infinitesimal real perturbation followed by an integer realization
preserving the strict sum order cannot supply the proposed repair.
The example itself is sparse, with $k=O(\log N)$. A
square-root-dense extension now gives the same
obstruction with $k^2/N\to1/(1+\delta)$, for fixed
$0<\delta<1$. This still does not reach the supercritical regime,
and no unrestricted repair allowing substantial reordering was found.

## Reflection patterns still admit the uniform pair model

Even allowing fixed macroscopic vector weights, rather than scalar
ones, does not remove the following two-point relaxation.
Normalize a hypothetical symmetric set in $[-L,L]$ by its
counting measure divided by $\sqrt L$, and consider the limiting
density $f=1_{[-1,1]}$. Its mass corresponds to
$k\sim2\sqrt L$, or coefficient $\sqrt2$ relative to an
interval of length $2L$.

For a normalized positive difference $0<t<2$, the endpoint
fiber is $(x,x-t)$, with $t-1\le x\le1$. Reflection pairs
its parameter $x$ with $t-x$. For $t/2<x\le1$, write

$$
 \mathcal O_{t,x}=
 \delta_{(x,x-t)}+\delta_{(t-x,-x)}.
$$

These are exactly the allowed two-edge reflected configurations.
There is the identity of endpoint measures

$$
 \int_{t/2}^{1}\mathcal O_{t,x}\,dx
 =\int_{t-1}^{1}\delta_{(x,x-t)}\,dx.                           \tag{3}
$$

The integration interval on the left has length
$q(t)=1-t/2\le1$. Thus the right side is a convex mixture of
allowed configurations: use the empty configuration with probability
$1-q(t)$, and otherwise choose a reflection orbit uniformly.
The fixed orbit $x=t/2$, which would be a singleton configuration,
has measure zero and does not affect this leading-order statement.

The right side of (3) is the difference-fiber disintegration of
$f(x)f(y)\,dx\,dy$. Inserting any bounded fixed endpoint test,
including a matrix weight $v(x)v(y)^*$, preserves the identity.
Consequently every linear test that uses the allowable reflected
configuration separately at each difference is compatible with this
uniform profile. The usual continuum convolution positivity and
Cauchy--Schwarz constraints also hold, since $f$ is an actual
nonnegative density.

This is stronger than merely imposing multiplicity at most two: the
reflection partner locations have been retained exactly. It does not
assert that independently chosen difference configurations can come
from one integer set. Microscopic or growing-dimensional weights,
and consistency constraints involving several differences, remain
outside this obstruction.
