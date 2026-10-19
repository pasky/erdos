---
name: research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/report
title: "Endpoint cancellation: whole-statement examination"
desc: Independent adversarial examination of the full endpoint cancellation theorem, its source-proof reconstruction, and its signed application interface.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Endpoint cancellation: whole-statement examination

***

## Subject and independence

**Examination date:** 2026-10-15 UTC. **Subject freeze:** 2026-10-15,
14:29 UTC; the supplied neutral extraction was prepared at 15:09:22 UTC.
**Reviewer:** independent mathematical examiner, disclosed model OpenAI
gpt-6-astra with max reasoning. The examiner was neither an author of this
subject nor a collaborator on its construction. No earlier review was supplied.

The exact retained subjects are the following paths relative to this report;
they must remain beside it when the package is filed under
`wiki/research/erdos_824_uniformity/evidence/verify/`:

| Frozen input | Examined scope |
| --- | --- |
| [../../assets/endpoint_cancellation_subject/derivation.md.txt](../../assets/endpoint_cancellation_subject/derivation.md.txt) | Entire supplied text, especially “The consumed statement,” all supporting derivations, “Closing the quantitative estimate,” and “The order of choices.” |
| [../../assets/endpoint_cancellation_subject/source_sections_2_to_5.md.txt](../../assets/endpoint_cancellation_subject/source_sections_2_to_5.md.txt) | Supplied Sections 2–5 and bibliography in full; every essential deduction of P is within the proof examination below. |
| [../../assets/endpoint_cancellation_subject/signed_application.md.txt](../../assets/endpoint_cancellation_subject/signed_application.md.txt) | Entire supplied text, to identify and check every interface consumed as P, including both signs, the actual endpoints, and the order of choices. |

The mathematical source is OpenAI, *Weighted dilation graphs, smooth shifted
primes and totient fibers*, release of 24 September 2026, an unrefereed
manuscript. Source-owned mathematics retains that attribution. The project
reconstruction and the independent examination are prepared for Plasma AI.
The shared model provider is disclosed; independence here is separation from
authorship and mathematical communications, not a claim of different providers.

The inputs were supplied as a neutral extraction with explicit `[cut]` markers.
They were read from that extraction, remained unchanged, and are retained with the mechanical maintenance listed on the record index. Their identity and the operating-file identities were checked against
the delivered manifest before use. The permitted mathematical read set was
exactly these three files. No original source repository, PDF, outside paper,
web search, author context, previous report, other private memory, inbox, or
feed was read. The subscription tables inspected before and after startup and
at the examination step were empty. There was no excluded mathematical or
communication exposure. Private identity and isolation receipts are separate
from this mathematical record.

Operating reading included the complete `docs/verification.md` and
`campaign/guides/verification.md`, `README.md`, `campaign/AGENTS.md`,
`docs/evidence.md`, `docs/approach_vetting.md`, `docs/math_authoring.md`, and
`docs/weaving.md`; the required claims, evidence, tiers and project-claim
passages of `docs/anatomy.md`; and the permitted reading, lifecycle and
configuration instructions. Those pages supplied procedure, not additional
mathematical premises. Output truncations in some large reads were addressed
by smaller reads of the needed passages; no verdict rests on unseen truncated
text. No mathematical computation, statistical sample, formal proof, or
repository gate is offered as evidence.

An administrative format check initially misidentified two displayed
absolute-value formulas as table rows. The checker was corrected; its
original and successful rerun receipts, together with a rejected private
checkpoint edit, are retained in the private operating accompaniment for
the grader. No mathematical conclusion rests on those operations.

The independent reasoning is retained in
[memory transfer](memory_transfer.md),
[ideal comparison](ideal_comparison.md), and
[Mellin cancellation](mellin_cancellation.md), together with the lift
and application calculations below. [reconstruction](reconstruction.md) gives the
noncomputational reconstruction route. This is a whole-statement examination
of P, not merely containment of the application pair in a narrower theorem.
It does not accept the separate E estimates or the final catalog conclusion.

## Restatement with all quantifiers

Let $L=\log x$, $T=\log L$, and $W=\exp(\sqrt L)$, with $x\to\infty$.
Fix

$$
0<a<b<c<d<0.47,\quad c_0,C_0,v_-,v_+>0,\quad
0<q<1,\quad \ell\in\mathbb Z_{\ge1}.
$$

For each sufficiently large $x$ take pairwise disjoint finite prime groups
$\mathcal P_g$, indexed by disjoint sets $\mathcal S,\mathcal B$, with
$c_0T\le|\mathcal S|,|\mathcal B|\le C_0T$. Small groups are arbitrary
subsets of primes in $[\exp(L^a),\exp(L^b)]$. Each big group is the set of
all primes in an interval contained in $[\exp(L^c),\exp(L^d)]$.
Every group has harmonic mass
$V_g=\sum_{p\in\mathcal P_g}p^{-1}\in[v_-,v_+]$.
The choices may vary with $x$ subject to these bounds; no conclusion assumes
that an inadmissible collection exists.

For a positive integer $n$, let $n_*$ be its largest divisor coprime to
every group prime, and let $\omega_g(n)$ count **distinct** group primes
dividing $n$. With $(y)_\ell=y(y-1)\cdots(y-\ell+1)$, set

$$
W_\ell(n)=\prod_g
q^{\omega_g(n)-\ell}\frac{(\omega_g(n))_\ell}{V_g^\ell}.
$$

A factor is zero when $\omega_g(n)<\ell$. Multiplicities in $n$ do not
increase $\omega_g(n)$. For fixed $\ell,q,v_-$ each group factor is
bounded, hence $0\le W_\ell(n)\le L^{O(1)}$ uniformly in $n$.

Fix $C>0$ and $0<\tau<\eta<1/4$. An endpoint has the form

$$
F_0(n)=\sum_{mpr=n_*}
\alpha_m\chi_0(m)m^{i\sigma_0}
\mathbf1_{p\in I_p,\ P^-(p)>W}p^{i\sigma_1}c_r,
\tag{R1}
$$

where all factors are positive integers, $p$ is an integer rather than a
prime variable, $P^-(1)=\infty$, the coefficients may be complex,
$|\alpha_m|,|c_r|\le L^C$,
$\alpha_m=0$ unless $P^-(m)>W$, and $I_p$ is any interval contained
in $[x^\tau,x^\eta]$. The character $\chi_0$ has modulus at most $L^C$,
and $\sigma_0,\sigma_1$ are real with absolute values at most $L^C$.
There is no roughness, multiplicativity, positivity, or regularity condition
on $c_r$. The two endpoints may have unrelated sequences, intervals,
characters and twists within these common bounds. All these data may depend
on $x$.

The property $(\mathrm D_B)$ for the **original sequence** $\alpha$ is

$$
\left|\sum_{m\in I}\frac{\alpha_m\chi(m)m^{iu}}m\right|
\le L^{-B}
\tag{R2}
$$

for every interval $I\subset[1,x^2]$, every Dirichlet character of modulus
at most $L^B$, including principal and imprimitive characters, and every
real $|u|\le L^B$. Any original interval restriction is already part of
$\alpha$; no replacement convolution inherits (R2) without proof.

For fixed $D_0>0$, a fixed compact interval
$[c_\Psi,C_\Psi]\subset(0,\infty)$, and fixed implied constants in
the derivative bounds below, P asserts that a fixed $B$ exists such that,
for every sufficiently large $x$, uniformly over all the preceding data and

$$
0<|k|\le L^C\ (k\in\mathbb Z),\qquad
xL^{-C}\le Z\le xL^C,\qquad |a_1|,|a_2|\le L^C,
$$

with $a_1,a_2\in\mathbb R$, every smooth $\Psi$ supported in
$[c_\Psi,C_\Psi]$ with
$\|\Psi^{(j)}\|_\infty\ll_jL^{C(j+1)}$, and endpoints $F_0,G_0$
whose first sequence satisfies (R2),

$$
\left|\sum_{\substack{z>0\\z+k>0}}
\frac{\Psi(z/Z)}z z^{ia_1}(z+k)^{ia_2}
\overline{F_0(z)}G_0(z+k)W_\ell(z)W_\ell(z+k)\right|
\ll L^{-D_0}.
\tag{P}
$$

The constants and threshold depend only on the fixed bounds and choices,
not the individual admissible groups, sequences, intervals, characters,
frequencies or shift. No discrepancy is required of the second endpoint.
The assertion includes both signs of $k$ and conjugation of the
discrepancy-bearing endpoint or its coefficients. All constants are fixed
before $x\to\infty$; no effective numerical threshold is asserted.

## Three weakest steps and independent derivations

### 1. Exact memory transfer and restoration of distinct births

[Memory transfer](memory_transfer.md), (M1)–(M14), derives the
single-prime lifespan expansion directly from its residue expectation.
A prime with $r$ active runs has factor $V_g^{-r}/(p b_p)$, paying for its
root residue once. Pending residues use counting measure. The factorial
identities $\binom{k+t}{t}/(k+t)!=1/(k!t!)$ and
$(j)_a/j!=1/(j-a)!$ give the ghost and edge adjoints even on numerical
diagonals. This independently addresses normalization, ghost endpoints,
return visits and reversed edges.

Weighted Schur estimates give a visit exponent $C_v$ independent of the
comparison construction. The memory tail at $B_{\rm mem}=\lceil L^2\rceil$
is $\exp(-\Omega(L^2))$. A dirty edge has norm at most
$2L^{C_a}\sqrt{B_{\rm mem}/\binom{J+\ell}{\ell}^{|\mathcal S|}}$:
the omitted small-label products are distinct integers below every pending
big prime, and each pending residue allows at most one of them. Reversal
handles stores. On clean edges the small-state contraction has exponent
$C_s$ independent of $J$ and comparison complexity; Fourier fibers are
the ideal operator or its adjoint, with negligible density and free-label
exclusion errors.

The collision correction is not discarded. At equality rank $r$ its
weighted count is at most $L^{C'r}$. Chronological fresh births give
$L^{C_h(N+1)}(C/P_*)^r$, where $P_*=\exp(L^c)$.
Phases inserted at the birth addresses give instead
$O(L^{(-G+C_v)N+C_v+2r(G+C_a)})$; at most $2r$ edges lose their
signed estimate, even if a pivot has already died. Splitting at
$r_0\asymp N\log L/L^c=o(N)$ proves the required total correction.
Relative residue replacement factors out the possibly tiny deterministic
active-prime damping before Bonferroni and CRT estimates. Finally, the
positive semidefinite Gram trace and spectral Hölder work with the
unnormalized constant mark vectors $u_n$. This proves the transfer actually
needed by mark-independent endpoints for either sign, without assuming P.

### 2. Ideal comparison for arbitrary tuple tests

[Ideal comparison](ideal_comparison.md), (I1)–(I11), checks the
full operator test space. For a product fiber at $n$, its probability is
at most $L^\kappa/n$, including repetitions. Fiberwise Cauchy–Schwarz
therefore collapses an arbitrary tuple test to square norm
$L^\kappa\|f\|_2^2/U$ on a product dyad; it never assumes the test is
itself a function of the product.

Conditional character Gram matrices on retained log cells have norm at
most two by the absolute, short-interval Siegel–Walfisz specialization.
This has no inverse-cell-mass operator loss. For discarded cells the
correct estimate is a bilinear $L^1$ bound on independent tuple spaces,
$\mathbb P(E)^{1/2}\|f\|_2\|g\|_2$, not a false small-restriction
$L^2$ operator claim. Large rational denominators use the integer
bilinear estimate. Small denominators use all inducing primitive
characters, pointwise reproduction, and the change of **both** matched
log products, of total size at most $2h$.

The full-probe fraction for a symmetric test is exactly
$(j)_m(M-j)_\ell/(M)_{m+\ell}$. Maximization in $j/M$ bounds it by
$2\ell^\ell m^{-\ell}$, and the bound tensorizes across groups even
for entangled tests. The asymmetric kernels leave separated conditional
tests. Alternating nonempty freed subsets cancel the raw pairing exactly;
the exceptional full-probe pieces are summed before taking absolute values.
Kernel precision and the coefficient exponent are consequently fixed before
$J$. This provides the uniform ideal bound used in step 1.

### 3. Full-endpoint local Mellin energy

[Mellin cancellation](mellin_cancellation.md), (F1)–(F18), uses
one small marked prime, not a property peculiar to the application pair.
Prime-square errors are $Y L^{O(1)}e^{-L^a}$. The surviving residual is
the arbitrary bounded coefficient
$c_{r_*}W_{\mathbf t-\mathbf e}^{\mathbf b}(r)$.
At a rational arc, split $r$ by its gcd with the denominator; only the
residual acquires that condition. The original $\alpha$ is unchanged.

The local Fourier-to-Mellin conversion has normalization $Y^{-1}$;
the logarithmic-kernel replacement costs
$(H/Y)^2\sum|a_w|^2$. Smooth product separation, including the exact
conversion to reciprocal coefficients, reduces to
$\int|P_sP_lR|^2$. Ordinary times use the small-prime bound and mean
square because $H/(LP)\to\infty$. The exceptional small-prime set
occupies at most $\exp(O(L^b+L^{1-a}\log L))=Y^{o(1)}$ unit
intervals. Their number is not multiplied by a logarithmic bound:
the residual's Gram kernel and its scale
$U\ge Y^{1-\eta-o(1)}>Y^{0.6}$ give
$\sum_I\sup_I|R|^2\ll L^{O(1)}$ for the entire $\eta<1/4$ range.

The long rough-integer factor saves every fixed logarithmic power on
**every** allowed subinterval, including very short ones. The block sieve
is reconstructed with its coefficient, level and growing-truncation
bounds. First and second derivative tests, iterated finite differencing,
and zero extension on short intervals handle positive and negative
$t+\sigma_1$ up to $x^2$. Low times alone use (R2), on an interval
inside $[1,x^2]$ with a character and frequency of previously fixed
logarithmic sizes. The result is

$$
\int|P_sP_lR|^2
\ll L^{-2A_s+K_1}+L^{-2A_l+K_2}
       +L^{-2B+B_0+K_3}+o(L^{-Q}),
\tag{R3}
$$

where the $K_i$ are fixed without $B$ or proxy precision. Choose $A_s,A_l$,
then $B_0$, then $B$. No relation between the two endpoints, smoothness of
$\alpha$, or roughness of $c_r$ enters this reasoning.

## Strongest attempted refutation and other attacks

The strongest attack was a collision between two births separated by the
death of the first particle. An absolute one-collision estimate really is
insufficient: $\exp(-L^c)$ cannot absorb
$L^{CN}=\exp(CN\log L)$ for $N=2\lceil L^{0.52}\rceil$.
Moreover, a state no longer remembers a dead pivot, so a purported
state-local equality constraint would lose information. This identifies an
exact dangerous inference, not a numerical near miss.

It does not refute the frozen reconstruction. Equality Fourier phases can
be attached to the two births themselves; ghost phases can be symmetrized
within their factorial batches. Unaffected edges retain their full signed
pattern sums. The low-rank estimate and the chronological high-rank estimate
above cover complementary ranges with $r_0/N\to0$. Equations (M11)–(M13)
retain the complete response to this attack. No single-collision shortcut
is used in the verdict.

Additional attacks and their outcomes were:

| Attack | Finding |
| --- | --- |
| Concentrate tuple tests on a cell of tiny or discarded probability; distinguish orderings with equal product. | (I1), the conditional Gram normalization, and the independent-space estimate (I4) remain valid. A general joint test would invalidate (I4), but is not what the proof conditions to. |
| Choose $c_r$ to align the residual with every exceptional Mellin time. | The sparse Gram row bound (F12)–(F13) controls arbitrary residual coefficients by their square norm; no pointwise cancellation or regularity of $c_r$ is assumed. |
| Take unrelated endpoints, or choose $\alpha$ with high-frequency phases or concentrated support invisible to low-frequency discrepancy. | High times use the long factor and the residual square norm, not a nonexistent discrepancy extension. Low times use the literal interval-uniform (R2). The endpoint norm and local energy estimates do not use equality of the endpoint data. |
| Shrink $I_p$ to an empty or one-integer interval, move it to either edge of its range, and let $\eta$ approach $1/4$. | The sieve and derivative bounds are absolute subinterval bounds; an empty interval is zero. (F11) has a margin beyond $Y^{0.6}$ throughout the stated range. No minimum interval length was inserted. |
| Use principal/imprimitive characters, conjugate the discrepancy sequence, or make $t+\sigma_1$ small near the cutoff. | All characters of the quotient are retained; induced primitive characters suffice only where arguments are units. $B_0$ exceeds the fixed twist exponent, and $B$ pays for products of characters. Conjugation is exact as shown below. |
| Reverse $k$, force the signed determinant close to its support boundary, or lose $1/z$ in the lift. | The signed inverse, positive support and the factor $Z$ in the application are exact. The physical harmonic normalization is checked next. |
| Make late comparison complexity or proxy accuracy increase an early exponent. | The endpoint norm, $C_v,C_s$ and early Fourier frequency exponent are fixed before comparison complexity; the final parameter order below contains no such feedback. |

These are analytic attacks, not independent random samples or finite evidence
for a universal assertion. No counterexample or unsupported essential
inference survived them within the declared external boundaries.

## Physical lift, overlap errors, and major arcs

This section checks the bridge between the three retained derivations.
For a fixed physical source list $S'$ with $M=J+\ell$ distinct labels
per group, let $P(S')$ be its product. The state mass is
$\prod_gV_g^{-M}$. On that state, $n_*\mid n/P(S')$ and
$|F_0(n)|\le L^{2C}\tau(n_*)^2$. A fixed fourth divisor moment gives

$$
\sum_{\substack{n\asymp X\\P(S')\mid n}}|F_0(n)|^2
\ll \frac X{P(S')}L^{O(1)},\qquad
\sum_{S'}\frac1{P(S')}\prod_gV_g^{-M}\le1.
\tag{R4}
$$

Here $P(S')=x^{o(1)}$ and $X=x^{1+o(1)}$, so endpoints of the count
do not alter the bound. The damping $q^{(\omega(n)-Ms)/2}\le1$ on
physical states. Thus both endpoint norms are at most
$X^{1/2}L^{C_6}$ with $C_6$ independent of $J$. The two rough divisor
choices in (R1) number at most $\exp(O(\sqrt L))$, because each uses
primes above $W$; hence the required pointwise bound also holds even if
$c_r$ is arbitrary. The vectors are mark independent. Positions outside
the positive supported dyads can be assigned zero, avoiding logarithms of
nonpositive integers.

Use the conjugate-linear-first pairing with
$f(n)=n^{-ia_1}F_0(n)q^{(\omega(n)-Ms)/2}$ and the corresponding
$g(n)=n^{ia_2}G_0(n)q^{(\omega(n)-Ms)/2}$. Insert
$\Psi(n/(ZD))/n$ and $D^{-i(a_1+a_2)}$. Separating the smooth
function of $\log(n/Z)-\log D$ puts its first-variable factor into
$f$ with its conjugate, and supplies ideal frequency
$\zeta=-a_1-a_2-v$. The bounded factor $X/n$ is absorbed in $f$,
and the pairing is divided by $X$. A fixed exponent bounds the retained
$v$ before the eventual tail accuracy. Dyadic and Fourier total mass
costs $L^{C_F}$, with $C_F$ fixed before comparison kernels.

For a pattern with $c_g$ free slots and $t_g=\ell+c_g$ unshared
endpoint slots, split $D=D_RD_C$ into the shared and free products and
write $n=D_Rw$, $n'=D_Rw'$. The joint list normalization is

$$
V_g^{-M-t_g}=V_g^{-(J-c_g)-2t_g}.
$$

The factor $1/n=1/(D_Rw)$ turns each shared label into a harmonic draw
$1/(pV_g)$. Away from overlaps,
$\omega_g(n)-M=\omega_g(w)-t_g$ and the graph/vector half-dampings
give the full marked weights at $w,w'$. The phase identity is

$$
(D_Rw)^{ia_1}(D_Rw')^{ia_2}(D_RD_C)^{-i(a_1+a_2)}
=(w/D_C)^{ia_1}(w'/D_C)^{ia_2},\quad w'=w+kD_C.
\tag{R5}
$$

Endpoints are invariant under multiplication by group primes, so no endpoint
data change. The raw pattern has $D_C=1$, $t_g=\ell$ and coefficient
one. It gives exactly (P) after the negligible exclusions below, not a
different shifted convolution.

For fixed $w,w'$, only $O_J(L)$ prime values can violate the shared
draw exclusions. Each harmonic atom is at most
$v_-^{-1}\exp(-L^a)$; there are $O_J(T)$ draws. Overlap damping can
cost $q^{-2Ms}=L^{O_J(1)}$, which is harmless against that exponential.
The endpoint absolute sums use (R4). If a free big prime divides an
endpoint, it divides both $w,w'$ because it divides $D_C$; writing
$w=pv$ gives an additional $1/p$ in the harmonic sum. Endpoint
invariance and fixed divisor moments bound this contribution by
$L^{O(1)}/p$. These estimates cover all forbidden coincidences after
summing patterns and hold for either sign. In particular there is no
assumption that $c_r$ is small on multiples of a group prime.

Expanding the comparison coefficients into their log-cell and character
factors leaves bounded factors $b_1(D_A),b_2(D_B)$ and endpoint mark
functions independent of the free products. Each free product is nonempty
and has size at least $\exp(L^c)$; their product has cell scale $H'$ and
$Y=ZH'=x^{1+o(1)}$. The Fourier multiplier is

$$
M(\theta)=\mathbb E b_1(D_A)b_2(D_B)e(-k\theta D_AD_B).
\tag{R6}
$$

Product collapse and the integer bilinear estimate control (R6) off major
arcs. More precisely, approximate $k\theta$ with maximum denominator
$\lfloor H'/L^{C'}\rfloor$. A denominator at most $L^{C'}$, after
division by $k$, produces an arc for $\theta$ of denominator at most
$|k|L^{C'}$ and width at most a fixed logarithmic power divided by $H'$.
Every other approximant has both denominator and complementary quotient
large enough for (I2). Choose $C'$ for the required saving, then
$C_{\rm arc}$ to contain all the first arcs. The number of arcs is
polynomial in $L$; changing the sign of $k$ changes only a numerator.

Parseval and the fixed endpoint square norms handle minor arcs. On an arc,
put $H=H'/L^{C_{\rm arc}}$. The first endpoint's local energy is
$O(YL^{-A})$ by (F1)–(F18), whereas the second endpoint needs only its
$O(YL^{C_8})$ full square norm. Cauchy–Schwarz, division by $Y$ and
the polynomial arc, pattern and separation costs give arbitrary saving
after choosing $A$ large enough. Thus the transfer pairing, raw identity
and comparison bounds compose into (P) for the full class (R1).

## Exact signed application interface

This comparison examines what the supplied application consumes as P. It does
not use the application to prove P, and does not award acceptance to E or to
the application's final catalog use.

The band's distinguished integer always belongs to $h$ in the split $u=eh$.
For a fixed assignment pattern and Fourier component the resulting coefficient
is

$$
a_h(h)=h^{i\varrho}W_\ell(h)H(h_*),\qquad
H(t)=\sum_{pr=t}\mathbf1_{p\in I_{**},\ P^-(p)>W}p^{i\sigma}c_r.
\tag{R7}
$$

The interval $I_{**}=[x^{\tau_*},x^{\eta_*}]$ is the original common
band, with $0<\tau_*<\eta_*<b_*/4<1/4$. For the square of a fixed
component, the two copies use the **same** $H$, hence the same interval
and residual $c_r$. No restriction on the prime factors of $r$ is needed.

The early exponent assertions used by this interface can be checked without
P. At each slot the remaining logarithmic budget $R_i$ is nonnegative.
Taking a prime reduces both budget and available logarithms by its log;
skipping requires $R_i<(c_2+1)s_j$. The next band has at least $r_0-1$
remaining pure slots with total log at least $(c_2+1)s_j$. The last-band
slack is at most $(c_2+1)s_{j_x}$. Initially the available log is at least
$(1-b_*/2)L-O(1)$, exceeding $\log E\le(1-b_*)L-K_0T$.
This proves $EL^{-C_s}\le e\le E$, with
$C_s=(c_2+1)c_+$ independent of $K_0$.

There are $N_s=O(T)$ transition factors with fixed smooth compact
arguments. Their Fourier mass over all patterns is at most
$(2C_F)^{N_s}=L^{O(1)}$. Cutting each frequency at $L$ leaves a tail
bounded by $2^{N_s}N_sC_MC_F^{N_s-1}L^{-M}$, and the slot twist is

$$
\sigma_t=-\xi_t/s_{j(t)}
          -\delta_t\sum_{i>t}\xi_i/s_{j(i)}=O(L/T).
$$

Pure-prime assignments at a fixed product number at most
$(r_0!)^{j_x+1}=L^{O(1)}$. Thus the coefficient and Fourier exponents
in (R7) are fixed independently of $K_0$ and of tail accuracy. The
absolute bound against which these tails are taken uses fixed divisor
moments, not discrepancy. For the Cauchy diagonal,
$e\mid(mn+1)/2$ and
$\sum_{e\mid(mn+1)/2}\tau((mn+1)/(2e))^2\le\tau(mn+1)^3$.
Consequently $\sum_{v\ll x}\tau(v)\tau(v+1)^3\ll xL^{C_5}$,
with $C_5$ independent of $K_0$. This verifies the specific independence
needed to fix $K_0$ before the off-diagonal parameters.

For an off-diagonal pair, direct subtraction gives

$$
mn=2eh-1,\quad m'n=2eh'-1,
\qquad m'-m=-2ek,\quad h'-h=-kn,\quad mh'-m'h=k.
\tag{R8}
$$

The first equation makes $n$ a unit modulo $2e$, so $2e\mid m'-m$;
$k$ is a nonzero integer of either sign. Set $z=m'h$, so $z+k=mh'>0$.
The supported range gives $|k|\ll L^{K_0+C_s}$ and $Z=xL^{O(1)}$.

The converse does not lose a divisibility condition. Suppose
$0<|k|<W$, $m,m'$ are rough above $W$,
$m'\equiv m\pmod{2|k|}$, $e=(m-m')/(2k)>0$, and
$m'h=z$, $mh'=z+k$. Then $e$ is a positive integer and

$$
m(h'-h)=-k(2eh-1).
$$

Since $(m,k)=1$, $n=(2eh-1)/m$ is a positive integer and
$m'n=2eh'-1$. These operations invert (R8). Both $m,m'$ are units
modulo $2|k|$, so the congruence is exactly
$\varphi(2|k|)^{-1}\sum_{\chi\bmod2|k|}\chi(m)\overline{\chi(m')}$,
with all characters included.

The pulled-back argument is
$n/V=((m-m')z/(kmm')-1/m)/V$, with the minus sign retained.
On a fixed box in $\log(m/U),\log(m'/U),\log(z/Z)$, derivatives
of $e/E$ and $n/V$ have sizes
$O(U/(|k|E))$ and $O(Z/(|k|UV)+1/(UV))$. After $K_0$ is fixed these
are fixed logarithmic powers. Smooth separation therefore supplies fixed
logarithmic frequency and total-mass exponents. Sharp restrictions of the
original $\alpha$ remain in that sequence; they are not differentiated.
Absolute convolution square norms $ZL^{O(1)}$ pay for separation tails
before any use of P.

For each separated character and frequency triple, the actual pair is

$$
\begin{aligned}
F_0(v)&=\sum_{mpr=v_*}\alpha_m\chi(m)m^{i(\varrho-\xi_2)}
 \mathbf1_{p\in I_{**},\ P^-(p)>W}p^{-i\sigma}\overline{c_r},\\
G_0(v)&=\sum_{mpr=v_*}\alpha_m\chi(m)m^{i(\xi_1+\varrho)}
 \mathbf1_{p\in I_{**},\ P^-(p)>W}p^{-i\sigma}\overline{c_r}.
\end{aligned}
\tag{R9}
$$

Indeed at $z=m'h$, $h^{i\varrho}=z^{i\varrho}(m')^{-i\varrho}$;
at $z+k=mh'$, $\overline{h'^{i\varrho}}=(z+k)^{-i\varrho}m^{i\varrho}$.
Conjugating the first line of (R9) gives the required
$\overline{\alpha_{m'}}\overline{\chi(m')}$ and the unbarred
$p^{i\sigma}c_r$ from $H(h_*)$. The second line gives
$\alpha_m\chi(m)$ and the barred copy from $\overline{H(h'_*)}$.
Thus the separated correlation is precisely $Z$ times (P), with

$$
a_1=\varrho+\xi_3,\qquad a_2=-\varrho,
\qquad \Psi(t)=t\psi_Z(t).
\tag{R10}
$$

Here $(z/Z)/z=1/Z$, which checks the harmonic-to-unweighted factor.
The identity $z_*=m'h_*$ follows because $m'$ has no group prime;
the analogous identity holds for $z+k$. Every part of (R9) is within
the full class (R1), with a single enlarged fixed coefficient/frequency
bound chosen before $D_0$ and $B$.

The closure under conjugation is also literal:

$$
\sum_{m\in I}\frac{\overline{\alpha_m}\chi(m)m^{iu}}m
=\overline{\sum_{m\in I}\frac{\alpha_m\overline{\chi(m)}m^{-iu}}m}.
\tag{R11}
$$

The character class and frequency range are unchanged. Conjugating an
endpoint conjugates its coefficients and character and negates its twists.
Further interval restriction preserves (R2) by intersection of intervals.
No same-$B$ invariance under arbitrary additional twists is claimed:
the required fixed twists are inside (R1), and the final $B$ exceeds
their eventual modulus and low-time frequency demands.

| Clause consumed as P | Finding against the proved scope |
| --- | --- |
| Both signs, $k\ne0$, positive $z,z+k$ | (R8) and its inverse cover both signs. Transfer, arc approximation and all estimates use signed translations or $\lvert k\rvert$; positive support is retained. |
| Full interval of scales and smooth cutoffs | The lift has $Y=x^{1+o(1)}$; the actual application has $Z=xL^{O(1)}$. (R10) preserves compact support and the required derivative bounds. |
| All characters, including principal and imprimitive | Orthogonality is over all characters modulo $2\lvert k\rvert$; rational arcs retain all quotient characters. Their product modulus is paid for when choosing $B$. |
| Original restricted discrepancy sequence | It is the same $\alpha$ in both lines of (R9), and in the low-time factor (F18). No residual or gcd condition is moved into it. |
| Common rough interval and common residual coefficient | They are exactly $I_{**}$ and $\overline{c_r}$ in (R9), inherited from the same (R7). The theorem also covers unrelated endpoints. |
| Coefficient, frequency and cutoff uniformity | Bounds are fixed logarithmic powers before $D_0,B$. No dependence on individual sequence values or later proxy precision is introduced. |
| Conjugated endpoint or coefficients | (R11) and the conjugation of (R1) establish the stated closure. |
| Choice of $B$ before final proxy precision | The order below has that property provided the proxy's coefficient bound is independent of its precision, exactly as the application states. P itself does not establish the proxy's discrepancy. |

## Order of choices and uniformity

For P, fix group bounds, $C,\tau,\eta$, the cutoff family and $D_0$.
The exponent $C_6$ in (R4) and the initial separation exponent $C_F$
fix $E>D_0+2C_6+C_F+3$ and a fixed ideal frequency bound. Choose
$G>E+C_v+3$ and $E_{\rm id}>G+C_s+2$. The exponents $C_v,C_s$ are
independent of comparison complexity. Next fix the probes, comparison
accuracy, cell and character precisions, hence $m,C_1,C_a$. Only then
choose $J$ so that

$$
\tfrac12c_0\log\binom{J+\ell}{\ell}>C_a+G+3.
$$

All comparison costs are now fixed. Choose arc and local-energy targets,
then $A_s$, the long-factor saving $A_l$, its $B_0$, and finally $B$
above every modulus, frequency and low-time saving exponent in (R3).
Arbitrarily small later Fourier tails use more derivatives, not a larger
previously fixed frequency exponent. The inequalities
$0.52+d<1$, $b<c$, $d<1/2$, and $\eta<1/4$ respectively provide
the residue modulus margin, small-prime/time-scale separation, rough
group exclusion and endpoint pointwise bounds, and the residual sparse
mean-square margin. Each is used within its stated range.

In the signed application, first fix group and band data, the designated
band, $b_*,C,D_*$. The transition and early norm exponents do not depend
on $K_0$, as checked above; choose $K_0$ from the diagonal next. Then
fix the separation bounds and $D_0$ to absorb the $k$ sum, Fourier mass,
dyads and Cauchy loss. The normalized character average introduces no
additional unbounded character-count loss. Invoke P to fix $B$. Final
proxy precision comes after this, under the expressly required
precision-independent coefficient bound. Establishing that a prospective
proxy actually satisfies (R2) is an E obligation, not an inference from P.

## Premises, reading depth, and deduction census

The census was derived from the frozen proof on 2026-10-15, including its
consequence sentences. There is no established native L-claim premise.
Accordingly no live claim-ledger row was authorized, requested or read;
there is no unreported tier-0 premise or prospective promotion in this
proof. Definitions 3.1–3.3 define finite label spaces and bounded operators
by the absolute row/column estimates; their use does not presume their
later cancellation assertions. P and source Theorem 5.1 are the target,
never an assumed premise of their own reconstruction.

The following are the exact external classical boundaries. They were
**claims checked in the supplied transcription and specialized here**;
their original cited texts and proofs were **unread**. Reliance is on the
commission's expressly designated classical statements. The report does
not claim an independent proof of them, a visual transcription check, or
an outside bibliographic verification.

1. **Siegel–Walfisz, source Theorem 2.2.** For fixed $A,C>0$,
   uniformly in $(a,r)=1$ and $1\le r\le(\log y)^C$,
   $\pi(y;r,a)=\operatorname{Li}(y)/\varphi(r)
   +O_{A,C}(y/(\log y)^A)$, with constants independent of $y,a,r$
   and not necessarily effective. The source identifies Tao, *254A notes 2:
   Complex-analytic multiplicative number theory*, 9 December 2014,
   Exercise 64, bibliography [22]. For the big-prime cells,
   $y\ge\exp(L^c)$ makes every required modulus $L^{O(1)}$ a fixed
   power of $\log y$. Summing over reduced classes cancels the main term
   for a nonprincipal character. Partial summation gives absolute harmonic
   bounds on arbitrary intersected intervals; it does not assert relative
   equidistribution on tiny intervals. The quotient of two distinct
   primitive characters has nonprincipal character on a common modulus
   at most $Q^2$. Choosing the Siegel–Walfisz precision after $Q$ and
   the cell threshold pays for residue-class and conditional-mass losses.
   The case $r=1$ also supplies any plain prime-number estimate needed;
   no independent stronger prime theorem is assumed.
2. **Mertens, source (2.2).**
   $\sum_{p\le y}p^{-1}=\log\log y+O(1)$ and
   $\prod_{p\le y}(1-p^{-1})\sim e^{-\gamma_E}/\log y$.
   The source identifies Tao, *254A notes 1: Elementary multiplicative
   number theory*, 23 November 2014, Theorems 15 and 26, bibliography [21].
   The first estimate gives the fixed divisor-moment Euler product and
   bounded mass in each sieve block. The second gives
   $\sum_d|\lambda_d|/d\le\prod_{p\le W}(1+p^{-1})\ll\sqrt L$.
   Only those bounds are used; no unquoted error rate is required.
3. **Derivative tests, source Lemma 2.7.** For real $f$ on an interval
   containing $H$ consecutive integers: if $f'$ is monotone in
   $[j+\lambda,j+1-\lambda]$, $j\in\mathbb Z$,
   $0<\lambda\le1/2$, then $\sum e(f(n))\ll\lambda^{-1}$;
   if $f\in C^2$ and $\lambda\le|f''|\le C\lambda$, then
   $\sum e(f(n))\ll_C H\sqrt\lambda+\lambda^{-1/2}$.
   Both hold on every subinterval satisfying their hypotheses, with
   $e(t)=\exp(2\pi it)$. The source identifies Montgomery–Vaughan,
   *Multiplicative number theory II: Primes and sieves*, undated
   author-hosted draft accessed 13 September 2026, Corollary 16.6 and
   Theorem 16.7, bibliography [15]. The first test is used on
   $z\log n/(2\pi)$ with derivative close to zero, using the interval
   $(-1,0)$ for negative derivatives. The second gives the sparse Gram
   kernel and the final differenced logarithmic phase. Higher derivative
   cancellation is derived by finite differencing in (F15)–(F16), not
   assumed as another external theorem.

The same-paper order is acyclic: elementary Section 2 deductions, Section 3
conditional transfer, Section 4 ideal construction, Section 5 physical and
Fourier reductions, the three time ranges, P, then its application interface.
The next table records actual proof inspection and findings. “Proof verified
within this examination” means the supplied proof was read and its essential
inferences checked against the independent reasoning cited; it is not a tier
award or a claim to have checked an original PDF.

| Source deduction and consumed interface | Actual reading depth and finding |
| --- | --- |
| Corollary 2.4: absolute harmonic character estimate, including induced characters and short intervals | Proof verified within this examination by summing Theorem 2.2 over classes and partial summation; arbitrary endpoint errors are absolute. The $t=0$ specialization suffices in the ideal cells. |
| Lemma 2.5: fixed divisor moments and reciprocal convolution norms | Proof verified: the local Euler factor is $1+2^k/p+O_k(p^{-2})$; positivity gives the harmonic bound and multiplication by $Y$ gives the counting bound. A fixed number of factors costs a fixed divisor power. (R4) avoids a moment order growing with $J$. |
| Lemma 2.6: continuous and separated-point mean squares | Proof verified: integration of off-diagonal phases, $\lvert\log(n/m)\rvert\gg\lvert n-m\rvert/Y$, and $2\lvert c_nc_m\rvert\le\lvert c_n\rvert^2+\lvert c_m\rvert^2$ give the harmonic spacing loss. Unit-interval Sobolev and derivative coefficient bound $\log Y$ give separated points. (F10) checks the growing moment does not alter these constants. |
| Lemma 2.8: Fourier/Mellin separation with frequency exponent fixed before accuracy | Proof verified: $j$ integrations give tail $L^{C(j+1)-C'(j-b)}$ in fixed dimension $b$, tending to arbitrary negative powers when $C'>C$. The application's $O(T)$ factors instead have the explicit product-mass and tail estimate above. |
| Lemma 2.9 and Corollary 2.10: block sieve, overcount, coefficients and level | Proof verified in (F14)–(F17): even truncation, disjoint one-block correction supports, $\sum(j+1)2^{-j}=4$, factorial tails uniform in growing even $h$, and nonnegative interval overcount. No external sieve result is substituted for the proof. |
| Definitions 3.1–3.3, Lemma 3.4: spaces, symmetrization, adjoint and absolute bounds | Definitions checked and proof verified. The joint normalization $V_g^{-M-t_g}$ is symmetric under reversal, with $-kD$ and conjugated multiplier. $\sup_{z\ge0}(z+t_g)_{t_g}q^{z/2}/V_g^{t_g}$ has $t_g\le\ell+m$, independent of $J$. |
| Lemma 3.6: relative residue replacement | Proof verified in the end of the memory keeper: deterministic active damping is removed first; active modulus and Bonferroni term count are $\exp(o(L))$, with CRT error negligible relative to the remaining main term. Relative precision absorbs the absolute path mass. |
| Lemma 3.7 and (3.13)–(3.17): exact path-memory realization | Proof verified in (M1)–(M3): one residue per lifespan, boundary ghosts, orphan intervals, ordered active slots and distinct-birth bijection. Both signs have identical invertibility conditions. |
| Lemma 3.8, (3.19), (3.25), (3.28): adjoints, Schur bounds, truncation | Proof verified in (M4)–(M8), including numerical coincidences, counting measure, ordered retrievals, reversed stores and doubled ghost births. Infinite ghost sums converge under these absolute bounds. |
| Lemma 3.9: rare promotions and stores | Proof verified in (M9): distinct omitted small products lie below every big prime; each pending particle permits at most one. Source and reversed target symmetrization are both used. |
| Lemma 3.10: clean-edge ideal norm | Proof verified in (M10) and its following calculation: small-state maps, Fourier fibers, pending contractions, density change and free-label ban; $C_s$ is independent of comparison complexity. |
| (3.39)–(3.47), Theorem 3.5: restore distinctness and transfer | Proof verified in (M11)–(M13) and the residue/closure argument. Rank coefficients, dead pivots, local birth phases, high/low rank sums and the memory tail are retained. No direct assumption of the physical conclusion is used. |
| Corollary 3.11: moment to mark-independent pairing | Proof verified in (M14): positive Gram trace with unnormalized $u_n$, bounded block overlap and spectral Hölder. $d<0.47<0.52$ and the $\exp(O(\sqrt L))$ endpoint bound pay for the block root. |
| (4.3)–(4.6), Lemma 4.2: tuple collapse and integer bilinear sum | Proof verified in (I1)–(I2), including repeated label fibers and denominator blocks of diameter at most $r/2$. Tests are arbitrary tuple functions. |
| (4.7)–(4.20), Lemma 4.3: conditional character comparison | Proof verified in (I3)–(I8): Gram norm, concentrated/discarded cells, primitive induction, rational reproduction, two log-product errors and all real additive frequencies. |
| (4.21)–(4.26), Theorem 4.1: probe cancellation and ideal norm | Proof verified in (I9)–(I11): exact symmetric projection fraction, its extremum, tensorization, asymmetric conditioning, alternating cancellation and summation before absolute values for full-probe terms. |
| (5.6)–(5.7): physical lift and raw identity | Proof verified in (R4)–(R5), including the $J$-independent norm, group-prime invariance, shared harmonic measure, overlap errors and both signs. |
| (5.8)–(5.11): comparison multiplier and major/minor arcs | Proof verified in (R6) and the following bounds: both nonempty products, approximation of $k\theta$, full endpoint square norms, local-energy normalization and polynomial arc count. |
| (5.12)–(5.13): small mark and rational character conversion | Proof verified in (F1)–(F4): prime squares, all quotient characters and residual gcd classes, with the original interval-restricted $\alpha$ preserved. |
| (5.14)–(5.19): local Fourier energy, smooth tails, four-factor boxes | Proof verified in (F5)–(F9): positive compact center range, kernel error, $Y/H$ factors, exact reciprocal conversion, interval intersections and fixed convolution moments. |
| Lemma 5.2: exceptional small-prime intervals | Proof verified in (F10): prime factorization gives the growing factorial moment, and separated-point mean square gives $Y^{o(1)}$ intervals without a hidden growing constant. |
| Lemma 5.3: sparse residual suprema | Proof verified in (F11)–(F13): first/second derivative Gram kernel, three separated classes, arbitrary coefficients, and $U>Y^{0.6}$ throughout the full endpoint class. |
| Lemma 5.4: long rough-integer factor | Proof verified in (F14)–(F17), including all subintervals, small and large times, negative times, character classes, finite differencing, reciprocal normalization and sieve-coefficient sum. |
| Section 5 completion; derivation (3) and order of choices | Proof verified in (F18), (R3) and the parameter order above. The low-time interval lies inside $[1,x^2]$, and the final $B$ is independent of proxy precision. |
| Signed application: P statement, endpoint construction, signed inverse, separation, conjugation and final order | Claims and proofs checked for this interface in (R7)–(R11) and the clause table. No separate acceptance of E or of the final catalog conclusion is inferred. |

Theorem 2.3, the multiplicative large sieve, is not consumed in this P chain:
its statement was read, its external proof was not verified, and the verdict
does not rely on it. Historical references to Efron–Stein,
Matomäki–Radziwiłł, Soundararajan, Ford–Halberstam, Helfgott–Radziwiłł
and Pilatte are not extra premises: the particular projections, moments,
sieve and memory constructions needed here were checked from their supplied
proofs. Basic finite character orthogonality, CRT, Fourier inversion,
Cauchy–Schwarz, Dirichlet approximation and Hilbert-space inequalities are
used in their explicit elementary roles above; no omitted analytic theorem
is hidden under those historical comparisons.

## Checklist verdicts

These are findings for this frozen subject, not inferred standing from an
earlier review. The canonical list, all named patterns, and the Erdos list
are recorded separately because each is required by the commissioned contract.

### Canonical failure modes

| Item | Verdict and evidence |
| --- | --- |
| Almost all upgraded to all | No defect found. P is eventual uniformly over every admissible datum. The small-prime exceptional times are kept and controlled by (F10)–(F17); rare graph events and overlaps have quantified errors. No exceptional endpoint sequence or sign is removed. |
| Induction presupposes termination | No defect found. The memory path has exactly $N$ edges, the rank expansion has finitely many addresses after truncation, the sieve has finitely many nonempty blocks, and differencing uses at most $K-2$ iterations. Infinite ghost sums have absolute Schur bounds. There is no unproved stopping assertion. |
| Probabilistic or averaging heuristic used as proof | No defect found. Residue replacement is a relative CRT/Bonferroni estimate; ghost evolution is an exact identity before bounded errors. Conditional independence is used only on product label spaces, and the application slot probabilities sum to the stated partition identity. |
| Circular use of target or equivalent statement | No defect found. The acyclic deduction order is explicit. Theorem 5.1 is not assumed; Theorem 4.1 provides the ideal antecedent of Theorem 3.5. The application is checked only after establishing P. |
| Exceptional sets dropped | No defect found. Square divisors, shared/free overlaps, dirty edges, memory tails, birth equalities, discarded cells, Fourier tails and exceptional Mellin intervals all retain bounds. In particular (F13) avoids paying the exceptional cardinality with a mere logarithmic saving. |
| Finite verification exceeds base-case coverage | Inapplicable: no finite experiment is used to establish P or its uniformity. All parameter-family conclusions have analytic estimates. |
| Relaxed or averaged model substitutes for actual objects | No defect found. (M1)–(M14) return the independent-label estimate to integer roots with exact memory and distinctness restoration; (R4)–(R6) return the physical pairing to the actual shifted correlation. |

### Named patterns

| Item | Verdict and evidence |
| --- | --- |
| Model-class transport instead of entailment | Inapplicable to classification of axiom-system extensions: the subject makes no such classification or novelty claim. Its analytic model transfers are checked in the preceding row, rather than justified by syntactic similarity. |
| Infinite-family uniformity inferred from finite cases | No defect found. The fixed-parameter dependence and choice order are stated; no sampled group, interval, frequency or coefficient family stands for all families. Thresholds may depend on fixed $J$ and classical constants, as permitted. |
| Extrema checked in the claim's own units | No defect found. The relevant projection fraction is computed in (I9) and maximized in $u=j/M$ in (I10); sparse Gram and Schur bounds are in their actual Hilbert-space measures. No sharpness or attained optimal constant is claimed. |
| Consequence sentences are claim surfaces | No defect found within P and its actual application interface: the moment-to-pairing implication, raw identity, major-arc implication, conjugation and order-of-choice consequences are separately checked. The historical comparison to source Section 6 remains outside the supplied source, as recorded below; E and the catalog conclusion are not silently adopted. |
| Hypotheses used by quantified argument are carried | No defect found. Positivity of $\ell$, bounded group masses, all-prime intervals for big groups, arbitrary small groups, roughness of $m,p$, fixed coefficient bounds, and the rigid character-times-power form of the long factor are retained. No unasserted restriction on $c_r$ or interval length is introduced. |
| Composition inherits unsupported premises | No missing essential same-paper inference found. Every consumed deduction has a row above. The three classical statements remain explicit external boundaries; the application cannot establish its own P antecedent, and the proxy discrepancy still belongs to E. |
| Reproducibility notes are claims | Satisfied for a mathematical examination. The retained three inputs and three derivations, together with this report's bridge calculations, specify the reconstruction in the reconstruction account. No numerical success count or unexecuted mathematical command is asserted. |
| Verifier quotations are claims | Inapplicable to this examiner: no earlier verdict or standing text was supplied or characterized. The distinct grader and integrator own any later characterization of this report. |
| Verdict words spelled in full | Satisfied. The mathematical verdict below is written as **refutation-failed**, not an ambiguous abbreviation. |
| Certified-bracket functions fail on cap exhaustion; periodic windows are safe | Inapplicable: no numerical enclosure, capped solver, or periodic-data computation is used. |
| Executable leg has a meaningful failing input | Inapplicable: there are no executable mathematical verification legs. The retained analytic attacks have explicit failure conditions; administrative input-identity checks are not mathematical evidence. |
| Gate reruns generators instead of trusting caches | Inapplicable: the verdict rides no computational gate or cached output. No repository-wide gate was run or represented as a proof. |

### Erdos-specific checklist

| Item | Verdict and evidence |
| --- | --- |
| Quantifiers and scope | No defect found for the full restatement (R1)–(P): both signs, all admissible scale/frequency/character/coefficient ranges, every interval $I_p$, unrelated endpoints, original restricted $\alpha$, and eventual uniformity are covered. |
| Circularity | No defect found; the dependency order and target/premise distinction above are explicit. |
| Model and convention changes | No defect found. Counting versus probability measure, factorial memory, ordered label lists, repeated prime values, distinct divisor counts, integer $p$, conjugate-linear-first pairing, and harmonic normalization are all checked. |
| Finite and statistical overreach | Inapplicable to finite or statistical inference. The calculation uses exact sums/integrals and inequalities; no correlated samples are counted as independent evidence. |
| Uniformity | No defect found. The early $J$-independent exponents, fixed-dimensional versus $O(T)$ Fourier steps, absolute short-interval estimates, character products and $B$ before proxy precision are tracked explicitly. |
| Extremal conclusions | No defect found for the supremum bounds actually used, especially (I9)–(I10). There is no claim of an optimal exponent or a realized extremizer for P. |
| Consequences and composition | No defect found for P and each consumed application clause in the interface table. The supplied historical Section 6 comparison is unverified, and E/final catalog consequences are not within the verdict. |
| Computation | Inapplicable to mathematical computation; no code, numerical output, tolerance, finite range or failure exit supports the proof. Zero of the two permitted mathematical checks were needed. |
| Reproduction | Satisfied by the retained exact extracts, derivations and explicit reading order in the reconstruction account. No dependence on a private archive, source revision checkout, previous run, or cached mathematical result is required once this package is adopted. |
| Source and verdict fidelity | The supplied source statements, proofs and consumed scope were compared without promoting source theorem labels into native claims. Original classical texts and PDF fidelity remain unexamined; the limitations below are part of the verdict. No prior verifier ruling is quoted. |

The neighboring evidence-coverage discipline is met by identifying which
keeper and calculation supports each essential deduction. There are no
statistical samples for which correlation adjustment is needed. Administrative
identity comparisons do not add mathematical strength to these analytic
findings.

## Verdict, limitations, and next ownership

**Mathematical verdict: refutation-failed.** The entire stated endpoint
cancellation theorem P, its essential source-proof reconstruction through
the order of choices, and every clause consumed as P in the supplied signed
application survived this examination, relative to the three explicitly
designated classical boundaries. The examination is not restricted to the
special application endpoints: (F1)–(F18) allow every coefficient and interval
in (R1), and the second endpoint may be unrelated to the first.

No essential P inference or quantified endpoint range is left as an unfinished
obligation in this report. This is an adversarial mathematical finding, not
an independent grade, a native tier award, a formal proof, or evidence of
refereeing of the unrefereed source.

The limits are exact:

- The source was read as the supplied transcription. Its agreement with an
  original PDF was not inspected. The classical results were accepted only
  in the quoted forms; their original proofs and bibliographic fidelity were
  not independently checked.
- Source Section 6 was not supplied. Therefore the application's assertion
  that it is the source's Theorem 6.1 with precisely the listed sign changes
  remains an **unverified source-fidelity assertion**. The signed algebra
  and the actual P interface are verified directly above and do not depend
  on that comparison. If the historical equivalence is to be retained as
  an independently checked claim, the commissioning coordinator must supply
  its exact Section 6 input to a separately authorized examination.
- The report does not establish that any proposed proxy satisfies
  $(\mathrm D_B)$, accept the separate E estimates, prove the final catalog
  conclusion, or assess text written after the freeze. Those remain with
  their responsible project owners and the coordinator.

The coordinator owns intake, preservation of the entire package at a durable
repository-relative location, and assignment to a distinct fresh grader.
That grader decides contract validity, independence and accepted weight;
the examiner does not grade or promote this report. The coordinator also
owns the limited source-fidelity obligation just stated. Private delivery
alone does not settle any mathematical standing.
