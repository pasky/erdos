---
name: research/leads/two_representation_exponent_frontier
title: Two-representation exponent frontier
desc: |
  Restricted exponent diagnostics and incomplete fiber, compatible-code,
  ambiguity-token, and online routes beyond the discrete-logarithm bounds.
tags: []
sources: []
problems:
- 158
research_state: blocked
review_status: unreviewed
created: 2026-09-09T02:22:43Z
updated: 2026-10-19T04:19:07Z
---

# Two-representation exponent frontier

[[research/leads/_index|..]]

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and standing

For $A\subseteq\mathbb Z_{>0}$, write $A(x)=|A\cap[1,x]|$ and
count representations by unordered pairs, including a diagonal $a+a$ once.
Call $A$ a $B_2[2]$ set when every integer has at most two such
representations. The long-term construction target is one infinite $B_2[2]$
set with $A(x)\ge c\sqrt x$ for some $c>0$ and every sufficiently
large real $x$. This would answer
[[problems/additive_bases/E0158/_index|Problem 158]] negatively. A logarithmic
counting exponent $1/2$ alone would not supply that positive constant.

The current native baselines are
[[theory/additive_bases/L2_two_representation_exponent/_index|L2]] and
[[theory/additive_bases/L4_random_modulus_exponent/_index|L4]]. Their
statements and proofs own the exponents $3/7$ and
$\gamma_0=\sqrt6-2$, respectively. Both are author-recorded at tier 0,
without independent whole-claim acceptance or native Lean verification.
L2 also owns the zero endpoint ratio for subsets of its particular ambient
encoding. L4's explicit subexponential loss and all-real-cutoff conclusion
supersede both the general constant-$3/7$ milestone and the older
$(5-\sqrt{17})/2$ counting threshold discussed below. Neither baseline
supplies an optimized schedule or a positive constant at its top exponent.

This note records conditional counting diagnostics, explicit invalid
shortcuts, and incomplete construction routes. The routes are incomplete,
not refuted. No stronger exponent or resolution of the square-root question
is proved here. The problem page records the limits of public-literature
compilation; this note makes no fresh status or priority assessment.

## What the fixed-modulus count spends

Use the shell and auxiliary-modulus notation of the
[[theory/additive_bases/L2_two_representation_exponent/_proof|L2 proof]].
For the following parameter diagnostic, let $3/7\le\gamma<1/2$ and put

$$
X=2^{\gamma K^2},\quad Y=2^{\gamma L^2},\quad
M=Q_L,\quad N=Q_K/Q_L,\quad \lambda=L^2/K^2,
\qquad K>L.
$$

Here $\log_2Q_J=J^2+O(J)$. The congruence fiber of an upper and lower
prime pair is the level set of

$$
\Phi_{K,L}(P,R)=(P\bmod N,PR\bmod M).
$$

Write $r_{u,v}$ for its occupancy and
$T_{K,L}=\sum_{u,v}\binom{r_{u,v}}3$ for the exact number of fiber
triples. Equal encoded sums lie in a common fiber; the converse is not
asserted. In their constructions, the native proofs establish injectivity
of both coordinate projections within a fiber and recover the shell pair
from an integer sum.
In particular, their cross-shell triples have six distinct prime labels.

Set

$$
U=X/N,\qquad Z=XY/M,\qquad W=2XY^2/(MN).
$$

The diagnostic below is conditional on the fixed-modulus estimate

$$
T_{K,L}\le U^2Z^2W\,2^{o(K^2)}
\tag{1}
$$

holding uniformly in the relevant lower shells, with the digital and
same-shell arguments still valid. L2 proves the required estimate at its
own parameter. The
[[theory/additive_bases/L4_random_modulus_exponent/_proof|L4 proof]]
uses that mechanism only on the lower part of its collision band and gives
a different argument on the upper part. Formula (1) is not being asserted
throughout $3/7\le\gamma<1/2$ merely by varying its notation.

Two distinct points in a fiber require $N<X$ and $M<XY$. At the leading
exponent scale this gives the band

$$
1-\gamma<\lambda<\frac\gamma{1-\gamma}.
\tag{2}
$$

The leading exponents of $U,Z,W$, in units of $K^2$, are respectively

$$
\gamma-1+\lambda,\qquad
\gamma-(1-\gamma)\lambda,\qquad
\gamma+2\gamma\lambda-1.
$$

Multiplying the three factors in (1) therefore gives

$$
E_\gamma(\lambda)=5\gamma-3+4\gamma\lambda,
\qquad
E_\gamma\left(\frac\gamma{1-\gamma}\right)-\gamma
=\frac{7\gamma-3}{1-\gamma}.
\tag{3}
$$

The endpoint in (3) is a supremum of the leading exponent over the strict
band, not an attained shell pair. The leading exponent of $Z$ there is
zero. Reducing only the $Z^2$ contribution thus gives no fixed power
improvement at that boundary in this ledger.

The cofactor represented by $W$ has a different role. In the native
factorization proof, the offsets $a,b,s,t$ and the integer $d$ satisfy

$$
\begin{aligned}
P_2-P_1&=Na,& P_3-P_1&=Nb,\\
P_2R_2-P_1R_1&=Ms,& P_3R_3-P_1R_1&=Mt,\\
s(R_3-R_1)-t(R_2-R_1)&=dN,&0<|d|&<W.
\end{aligned}
$$

Multiplying the last equality by $P_1$ and substituting the two product
offsets gives $dP_1=atR_2-bsR_3$. Adding $dNa$ or $dNb$ then gives

$$
\begin{aligned}
dP_2&=a(t-s)R_1-s(b-a)R_3,\\
dP_3&=b(t-s)R_1-t(b-a)R_2.
\end{aligned}
$$

These identities describe three coupled prime-divisor conditions. The
pointwise divisor bound counts reconstructions after $d$ has been fixed;
it does not save choices in the range $0<|d|<W$.

A uniform replacement of $W$ by $W^{1-\varepsilon}$ in (1), for one
fixed $0<\varepsilon\le1$, is an unproved analytic interface. At
$\gamma=3/7$ the boundary exponent of $W$ is $1/14$, so this would
reduce the right side of (3) by $\varepsilon/14$. Continuity would permit
a parameter slightly above $3/7$, provided all other uniform arguments
and the simultaneous selection still apply. This is a conditional
improvement of that route, not an improvement of the current L4 baseline.

Even formally removing $W$ completely leaves the boundary condition

$$
\frac{-\gamma^2+5\gamma-2}{1-\gamma}<0,
\qquad
\gamma<\gamma_*:=\frac{5-\sqrt{17}}2<\gamma_0.
\tag{4}
$$

For the comparison, $\gamma_*<4/9<\gamma_0$ follows by squaring
$\sqrt{17}>37/9$ and $\sqrt6>22/9$, respectively.

There is also a proof-range issue at the same threshold. The native
nonvanishing argument requires $WU^3<M$. Its leading exponent margin is

$$
4\gamma-4+(2\gamma+2)\lambda,
$$

whose supremum on (2) is
$-2(\gamma^2-5\gamma+2)/(1-\gamma)$. A strictly negative uniform
power follows from $\gamma<\gamma_*$; it does not follow at the
endpoint or above it. Thus extending a rational expression in $\gamma$
does not extend the full-band factorization proof. L4 explicitly avoids
this extrapolation by changing the argument above $\lambda=2/3$.

The proposed random-fiber asymptotic
$T_{K,L}\asymp(XY)^3/(MN)^2$ for fixed nested moduli remains unproved
here. L4 reaches $\gamma_0$ by lower-modulus averaging and collision-plane
estimates. That theorem does not prove this asymptotic or the proposed
uniform cofactor saving.

Where L4's balance binds is visible in its proof, whose $\gamma$ is
$\gamma_0$ and whose fixed-modulus coefficient
$F_\gamma(\lambda)=5\gamma-3+4\gamma\lambda$ is the $E_\gamma$ of (3). On
the lower range $\lambda\le2/3$ that coefficient is at most $\gamma-\eta$
with $\eta=3-20\gamma/3>0$ ((33) in the
[[theory/additive_bases/L4_random_modulus_exponent/_proof|L4 proof]],
"Exponent balance and one infinite auxiliary realization"). On the upper
range $\lambda\ge2/3$ the first and third rows of the averaged bound (31)
lie below the fourth by at least $\gamma/3$ and by exactly $1-2\gamma$ (the
two differences stated under (31), "Conditional averaging, including the
line contributions"), and the second row's coefficient $H_\gamma$ is at most
$\gamma-\eta$ there ((34)); only the area coefficient
$D_\gamma(\lambda)=4\gamma-2+(4\gamma-1)\lambda$, increasing in $\lambda$,
approaches $\gamma$, at the upper endpoint $\lambda=\gamma/(1-\gamma)$ of
the collision band (12), where the equality $\gamma^2+4\gamma-2=0$ fixes
$\gamma$ ((35)). An exponent gain inside this method must therefore reduce
that area term for shell ratios near the upper endpoint of the band, or
improve on the generic independent-set guarantee (38) ("Simultaneous
selection using every full lower shell"); the fiber-selection section below
records what the second route needs.

## Restricted alteration guarantees

These are deductions from the counting model (1), not upper bounds on the
largest independent set or on all constructions. If $m_K$ is the number of
distinct forbidden upper three-sets, only
$m_K\le\sum_{L<K}T_{K,L}$ is justified: different fibers and lower
shells may project to the same edge. An equality of these counts, or a
matching edge-count lower bound inferred from (1), is unsupported.

With $n_K=2^{\gamma K^2+o(K^2)}$ vertices, generic three-uniform
alteration has the dense-edge guarantee $n_K^{3/2}/m_K^{1/2}$. Substituting
the worst upper bound from (3) gives the guaranteed leading exponent

$$
F_3(\gamma)
=\frac{3\gamma-E_\gamma(\gamma/(1-\gamma))}{2}
=\frac{3-5\gamma-2\gamma^2}{2(1-\gamma)}.
\tag{5}
$$

Its derivative is
$(\gamma^2-2\gamma-1)/(1-\gamma)^2<0$ on $[3/7,1/2)$, and
$F_3(3/7)=3/7$. This substitution therefore certifies no gain from a
larger starting parameter. It does not prohibit a larger independent set
than the generic guarantee.

For independent thinning from shell exponent $\gamma$ to
$0<\alpha\le\gamma$,
a cross-shell triple has survival factor
$2^{-3(\gamma-\alpha)(K^2+L^2)}$, since its six prime labels are
distinct. Requiring its expected count to have exponent less than the
upper-shell supply $\alpha$ gives

$$
E_\gamma(\lambda)-3(\gamma-\alpha)(1+\lambda)<\alpha.
$$

For $\alpha>0$ the left side minus the right side increases with
$\lambda$. Substituting the upper boundary of (2) yields

$$
\alpha<F_6(\gamma)
:=\frac{\gamma^2-5\gamma+3}{\gamma+2}.
\tag{6}
$$

Again $F_6(3/7)=3/7$ and
$F_6'(\gamma)=(\gamma^2+4\gamma-13)/(\gamma+2)^2<0$ on
$[3/7,1/2)$. This is the threshold furnished by the indicated thinning
and deletion calculation, conditional on its uniform count and assembly.
It is not a general six-uniform model of integer sum obstructions: that
model would omit diagonals, as explained below. Neither (5) nor (6)
extends the factorization range beyond (4).

An ideal checksum calculation has a similar restriction. Suppose extra
digits increase the physical label exponent from $1$ to $1+\delta$,
and assume their two independent equality constraints save precisely
$2\delta$ in the triple-count exponent. These independence and cost
assumptions are part of the model, not a supplied checksum construction.
For generic deletion to have a strict exponent saving, (3) requires

$$
\delta>\frac{7\gamma-3}{2(1-\gamma)}.
$$

At equality the limiting output exponent would be
$2\gamma(1-\gamma)/(5\gamma-1)$. Its derivative is
$-2(5\gamma^2-2\gamma+1)/(5\gamma-1)^2<0$, and its value at
$3/7$ is $3/7$. This particular idealized accounting supplies no gain.
It does not constrain a checksum with different proved correlations or costs.

A smaller number of candidate primes does not by itself reduce the ranges
of their differences or product differences. A narrow-shell argument must
state an interval-diameter bound; a progression argument must state the
step, occupied interval, and resulting divisibility. Cardinality alone
cannot justify substituting a smaller difference exponent. Likewise,
changing shell spacing or redistributing modulus sizes needs a new
collision-band calculation and control at the intervening physical
cutoffs. No optimized schedule or general impossibility theorem for these
variants is supplied.

## Activity markers and subleading losses

L2's restricted-encoding obstruction is already proved on its canonical
page. It transfers to L4's own ambient encoding, which has the same shape.
In the
[[theory/additive_bases/L4_random_modulus_exponent/_proof|L4 proof]]
("One random sequence and fixed source shells", displays (1) to (5)), the
auxiliary primes satisfy $2^{2j-1}<q_j\le2^{2j}$ by the proof's (1); the
digits are $x_j(p)\in[q_j+1,2q_j-1]$ with radix $b_j=4q_j$, and the radix
products $B_K=4^KQ_K$ satisfy $2^{K^2+2K}<B_K$ for every auxiliary outcome
by the proof's (2); the source shells $\mathcal P_k$ of the proof's (3) are
disjoint prime intervals whose union through shell $K$ lies in
$(1,2^{\gamma_0K^2}]$; and a label of shell $k$ has top digit
$x_k(p)\ge q_k+1$ at position $k$ by the proof's (4), all its digits being
nonnegative. Let $A_0$ be L4's full ambient label set before any
selection, and take the cutoffs
$x_K=(q_{K+1}+1)B_K-1$ of the
[[theory/additive_bases/L2_two_representation_exponent/_index|L2 card]]
("Restricted-encoding zero endpoint ratio"). A label from a shell $k>K$
is at least $(q_k+1)B_{k-1}\ge(q_{K+1}+1)B_K=x_K+1$, since $q_k\ge q_{K+1}$
and $B_{k-1}\ge B_K$. So $A_0(x_K)$ counts labels from shells through $K$
only, and by injectivity of $p\mapsto a_p$ there are at most
$2^{\gamma_0K^2}$ of them. Also
$x_K>q_{K+1}B_K>2^{2K+1}\cdot2^{K^2+2K}=2^{K^2+4K+1}$ by the proof's (1) and
(2), again for every auxiliary outcome. Hence

$$
\frac{A_0(x_K)}{x_K^{\gamma_0}}
\le2^{\gamma_0K^2-\gamma_0(K^2+4K+1)}
=2^{-\gamma_0(4K+1)}\longrightarrow0,
$$

the L2 card's bound with $\gamma_0$ in place of $3/7$. Every subset
$S\subseteq A_0$, including L4's selected set, has $S(x_K)\le A_0(x_K)$
along these cutoffs, so $\liminf_{x\to\infty}S(x)/x^{\gamma_0}=0$. This
closes the alternative that L4's encoding, unlike L2's, admits a subset with
an eventual positive constant times $x^{\gamma_0}$; the
[[theory/additive_bases/L4_random_modulus_exponent/_index|L4 card]]
("Scope and relationships") claims no such constant, and a positive constant
at exponent $\gamma_0$ needs a different encoding. The deduction is
author-recorded here and concerns L4's ambient encoding with its fixed
shells; it is not an obstruction to other constructions.

One proposed variation replaces an active logarithm digit by
$1+3\ell_j(p)$, where $0\le\ell_j(p)\le q_j-2$, and uses radix
$6q_j$. Inactive digits are zero. A single active digit is $1\bmod3$,
and the sum of two is $2\bmod3$. All sums are below the radix, so these
residues recover the number of active summands. After subtracting that
number and dividing by three, equal digits again give the corresponding
logarithm-sum congruences. Thus the activity and product interfaces survive,
with an active digit as small as one.

This removes the forced factor $q_{K+1}$ in L2's particular leading-digit
gap, but the radix overhead alone still obstructs a constant endpoint for
the unchanged source shells. Write $B_K=\prod_{j\le K}6q_j$ for this
variation, and let $A_0$ be its full ambient label set. A label from any
later shell is at least $B_K$, because its
$(K+1)$st digit is positive. At the real cutoff $x=B_K-1/2$, only
labels from shells through $K$ can appear. Even before selection their
number is at most $2^{\gamma K^2}$, whereas $B_K>6^K2^{K^2}$.
Consequently

$$
\frac{A_0(B_K-1/2)}{(B_K-1/2)^\gamma}
\le 2^\gamma6^{-\gamma K}\longrightarrow0.
$$

This deduction concerns this modified ambient encoding with unchanged
shells. It is not an obstruction to all marker constructions.

The supply and selection losses also require separate attention. In the
more precise count, put $S_J=\log_2Q_J$ and
$H_J=\log_2X_J$. The main expression is
$5H_K+4H_L-3S_K$. At the critical leading relation
$S_L=(3/4+o(1))S_K$, replace $H_J=(3/7)S_J$ by
$H_J=(3/7)S_J+h_J$. The edge expression changes by $5h_K+4h_L$;
the upper vertex expression changes by $h_K$. The dense-edge alteration
expression $(3\log_2n_K-\log_2m_K)/2$ therefore changes by
$-h_K-2h_L$ in this bookkeeping. Positive oversupply has the wrong sign
in that fixed calculation. Uncontrolled $o(S_K)$ errors cannot, however,
establish impossibility for every subexponential retuning.

Prime density, the precision of the fiber count, and distribution within
each selected shell remain additional losses. A constant-factor bound
needs all-cutoff control; an arbitrary large subset of a shell may be
concentrated near its upper end. L4's present loss and cutoff argument are
specified in its proof, not replaced by these prospective repairs. The separate
[[research/leads/balanced_auxiliary_prime_density/_index|balanced auxiliary-prime lead]]
retains a reviewed balanced-schedule refinement of that loss to
$\exp\{-C\sqrt{\ln x\,\ln\ln x}\}$ at the same exponent $\gamma_0$,
improving the order of the loss and not the exponent, without a positive
constant multiple of $x^{\gamma_0}$.

## Fiber selection beyond an edge count

For a fixed lower shell and fiber, its upper projections form a complete
three-uniform hypergraph: choosing three of them exceeds capacity two.
The full upper-shell obstruction is a union of these cliques. The relevant
pair codegree counts distinct third upper vertices in that union:

$$
\begin{aligned}
D_K(P_1,P_2)=\bigl|\{P_3\in\mathcal P_K\setminus\{P_1,P_2\}:\;&
\text{for some }L<K\text{ and }R_1,R_2,R_3\in\mathcal P_L,\\
&\Phi_{K,L}(P_1,R_1)=\Phi_{K,L}(P_2,R_2)
=\Phi_{K,L}(P_3,R_3)\}\bigr|.
\end{aligned}
$$

The necessary pair conditions
$P_1\equiv P_2\pmod N$ and $P_1R_1\equiv P_2R_2\pmod M$
do not bound this quantity by themselves. A new selection argument must
control admissible lower pairs, fiber sizes, repeated upper pairs across
lower shells, and the number of distinct third vertices after taking their
union. Counting the same extension many times gives an upper bound, not
the improved arithmetic codegree estimate this route needs.

Clique structure alone supplies no uniform power improvement. On one
fiber with $r$ upper vertices, every color class respecting capacity two
has at most two vertices. At least $\lceil r/2\rceil$ colors are
necessary, already of the order of the generic square-root degree bound
for a complete three-graph. Arithmetic restrictions on clique size and
overlap might still help. The missing result is a simultaneous selection
or coloring theorem with those restrictions proved for these fibers, and
with enough quantitative gain and prefix control for the desired density.

## Compatible finite towers

Dense finite sets at unrelated scales do not supply a single infinite set.
A sufficient tower interface would specify an initial finite $B_2[2]$
set, a reserve invariant, and an extension lemma iterable indefinitely.
For example, fix $0<\alpha\le1/2$ and suppose there are nested sets
$S_j\subset[1,N_j)$ at strictly increasing scales $N_j\to\infty$,

$$
|S_j|\ge N_j^{\alpha-o(1)},\qquad
\frac{\log N_{j+1}}{\log N_j}\longrightarrow1,
$$

would give their union logarithmic lower exponent at least $\alpha$,
provided every $S_j$ is $B_2[2]$. Every finite collection of
representations lies in some common $S_j$, and for
$N_j\le x<N_{j+1}$ the count is at least $|S_j|$. These two facts
justify the conditional transfer. No such reserve invariant or extension
lemma is supplied here. A block bound $|T|\ge L^{\alpha-o(1)}$ alone
is insufficient if the block length $L$ has no suitable relation to its
location or the preceding cumulative count.

A digital formulation needs additional hypotheses before the same transfer
applies. If coordinate $j$ has digits in $[0,b_j-1]$, for an integer
$b_j\ge2$, the usual carry-free embedding needs an integer physical
radix $\rho_j\ge2b_j-1$, so that every digit
sum is strictly below $\rho_j$. Its physical scale is
$D_k=\prod_{j\le k}\rho_j$, not $\prod_{j\le k}b_j$. For fixed
$b,\rho$, a code of size $b^{\theta k}$ gives exponent
$\theta\log b/\log\rho$ relative to $\rho^k$. A rate claimed only
in alphabet units cannot be transferred unchanged.

The codes must also control unordered pairs of whole words, be compatible
under a specified embedding, and produce natural numbers. Nested zero-tail
embeddings give finite-support labels and place any finite collection in
one common code. Projection compatibility alone may give paths with
infinitely many nonzero digits, which are not natural-number labels.
Finally, counts at the scales $D_k$ need interpolation between physical
scales, or stronger prefix bounds if a constant-factor density is sought.
Carry control, finite-support compatibility, an indefinitely maintained
reserve, and these cutoff bounds are the missing tower lemmas.

## An ambiguity token must control whole-word pairing

A token proposal allows one local coordinate to have two decodings while
requiring uniqueness elsewhere. The invalid shortcut is to infer global
representation control from those local unordered-pair counts. Even no
locally ambiguous coordinate is insufficient.

Indeed, $\{0,1\}$ is locally Sidon: its unordered sums $0,1,2$ come
only from $0+0,0+1,1+1$, respectively. Encode all three-digit words over
this alphabet in radix three. For a sum with digit word $111$, each
coordinate has the unique unordered local pair $\{0,1\}$. Assigning
which summand receives the one gives $2^3$ ordered word pairs. Global
interchange identifies exactly two assignments at a time, leaving four
unordered representations. Explicitly,

$$
0+13=1+12=3+10=4+9=13.
$$

All additions are carry-free. Translating every label by one gives the
positive-integer version

$$
1+14=2+13=4+11=5+10=15.
$$

Thus local Sidon behavior does not prevent different orientations across
coordinates from creating more than two global pairs. This refutes that
local-to-global inference, not the possibility of a token construction.
Such a construction needs a global pairing lemma for entire codewords and
their states, in addition to the carry, physical-rate, compatibility, and
finite-support conditions above. No automaton with those properties is
given here.

## Online extension and diagonal obstructions

For a finite $B_2[2]$ set $S$, let
$\Sigma_2(S)=\{n:r_S(n)=2\}$ be its saturated sums. There is a simple
exact test for adding one new positive integer $x\notin S$. The new
representations are $x+s$ for $s\in S$ and $2x$; all these sums are
distinct because $x\notin S$. Hence $S\cup\{x\}$ remains $B_2[2]$
if and only if

$$
(x+S)\cap\Sigma_2(S)=\varnothing,
\qquad 2x\notin\Sigma_2(S).
$$

Equivalently, exclude $(\Sigma_2(S)-S)$ and the integral halves of
saturated sums. This exact test gives no useful density of available
choices without bounds on the size and distribution of those forbidden
sets and on how the reserve changes after additions.

A block extension must handle old-old, old-new, and new-new
representations together. Three distinct unordered pairs with the same sum
cannot share an element, because canceling it identifies the other
element. There is at most one diagonal pair. Thus a forbidden triple has
six distinct elements when all pairs are off-diagonal, but five when one
pair is diagonal. For example,

$$
1+5=2+4=3+3=6
$$

uses five elements. A strictly six-uniform obstruction hypergraph misses
this configuration. The six-label thinning factor in (6) was legitimate
only because the native shell recovery and same-shell uniqueness exclude
this case in that particular cross-shell model.

An online extension theorem must preserve quantified bounds on saturated
sums and their translates, difference multiplicities, vertex and pair
degrees of the full five- and six-element obstruction system, and counts
inside every new block. It must leave the same reserve invariant available
for the next step and control the gaps between block scales. Neither the
one-point test nor a large finite set at one scale supplies that theorem.

## Reading boundary and next mathematical inputs

The native L2 and L4 statements and complete proofs were read for their
exact construction, uniformity, representation conventions, and method
limits. Their external theorem interfaces and source-reading records remain
on those canonical proofs. The relationship to
[[../library/additive_bases/cilleruelo_2014_infinite_sidon_sequences/_index|Cilleruelo's mixed-radix method]]
is through those native accounts; no additional source-proof inspection is
claimed here. This page is an author-recorded research account without
independent mathematical acceptance or computational evidence.

The next useful inputs are a uniform arithmetic third-moment or codegree
bound in the stated fibers, or an explicit compatible tower, token pairing,
or online reserve-extension lemma with its physical-scale count. Each
would need its own precise hypotheses and proof. The conditional ledgers
identify what the corresponding mechanism would have to improve; they do
not supply those missing results or refute their possible conclusions.
