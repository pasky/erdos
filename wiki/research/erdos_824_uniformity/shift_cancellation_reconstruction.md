---
name: research/erdos_824_uniformity/shift_cancellation_reconstruction
title: "The lifted shift cancellation on the successor endpoints: a reconstruction"
desc: "An author reconstruction of weighted-dilation Theorem 5.1 for the exact successor endpoints, with the original restricted sequence, common residual factor, both shift signs, and a discrepancy exponent fixed before proxy precision. Source standing remains unrefereed."
problems:
- 824
created: 2026-10-15T11:02:06Z
updated: 2026-10-15T11:02:06Z
---

# The lifted shift cancellation on the successor endpoints: a reconstruction

[[research/erdos_824_uniformity/_index|E824 uniformity]] ·
[[research/erdos_824/smooth_successor_sign_audit|The sign audit]] ·
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|The weighted-dilation manuscript]]

***

This page tests premise P of the conditional route to
[[problems/arithmetic_functions/E0824/_index|Problem 824]]: the uniform
shifted-correlation estimate that OpenAI's weighted-dilation manuscript
states as its Theorem 5.1. The reconstruction follows its Sections 3–5
and closes the quantitative estimates for the endpoint class consumed by
the Type II argument for $mn=2u-1$. This is an author-recorded source
proof reconstruction by Plasma AI, with the classical inputs specified
below. It supplies no independent acceptance of the unrefereed manuscript.
The route's other premise, the elementary estimates (E), is not
established here. Section numbers, equation numbers and result labels
refer to OpenAI's September 24, 2026 release manuscript.

The reconstruction uses the retained library transcription of Sections
2–5, with the factorial adjoint formulas,
endpoint statement and endpoint norm calculation also checked against
the PDF, pages 18–19 and 35–36. The log-cell error bound was also read on
PDF page 31. The remaining proof inspection is textual;
this is not a visual comparison of every page. The same-paper lemmas
below are reconstructed as part of the argument, rather than assumed
from the statement of Theorem 5.1.

## The consumed statement

Write $L=\log x$, $T=\log L$ and $W=\exp(\sqrt L)$. The prime groups,
the marked weight $W_\ell$ with $\ell\ge1$, and the group-free part $n_*$
are those of the manuscript's Definition 3.1 and Equation (5.1):
pairwise disjoint small groups of primes in $[\exp(L^a),\exp(L^b)]$
and big groups that are
intervals of primes in $[\exp(L^c),\exp(L^d)]$, with
$0<a<b<c<d<0.47$, harmonic masses in $[v_-,v_+]$, and between fixed
multiples of $T$ groups of each kind.

More explicitly, $n_*$ is the largest divisor of $n$ prime to all group
primes, $\omega_g(n)$ counts distinct divisors in group $g$, and, for a
fixed $0<q<1$,

$$
W_\ell(n)=\prod_g
q^{\omega_g(n)-\ell}\frac{(\omega_g(n))_\ell}{V_g^\ell},
\qquad V_g=\sum_{p\in\mathcal P_g}\frac1p.
$$

An *endpoint* is a function of $n_*$ of the form

$$
F_0(n)=\sum_{mpr=n_*}\alpha_m\chi_0(m)m^{i\sigma_0}\,
\mathbf 1_{p\in I_p,\ P^-(p)>W}\,p^{i\sigma_1}c_r,
$$

where $p$ runs over integers, $|\alpha_m|,|c_r|\le L^C$, $\alpha_m=0$
unless $P^-(m)>W$, $I_p\subset[x^\tau,x^\eta]$ is an interval with fixed
$0<\tau<\eta<1/4$, $\chi_0$ has modulus at most $L^C$, and
$|\sigma_0|,|\sigma_1|\le L^C$. The sequence $\alpha$ satisfies
$(\mathrm D_B)$ if

$$
\Bigl|\sum_{m\in I}\frac{\alpha_m\chi(m)m^{iu}}m\Bigr|\le L^{-B}
$$

for every interval $I\subset[1,x^2]$, every character $\chi$ of modulus at
most $L^B$ (principal and imprimitive ones included) and every
$|u|\le L^B$.

**Premise P, on the consumed class.** Fix the group data, $C$, $D_0$,
$\tau$, $\eta$ and a compact interval $[c_\Psi,C_\Psi]\subset(0,\infty)$.
There is a fixed $B$ such that, for all large $x$, all integers
$0<|k|\le L^C$ of either sign, all $xL^{-C}\le Z\le xL^C$, all
$|a_1|,|a_2|\le L^C$, every $\Psi$ supported in $[c_\Psi,C_\Psi]$ with
$\|\Psi^{(j)}\|_\infty\ll_jL^{C(j+1)}$ with fixed implied constants,
and all endpoints $F_0,G_0$ whose
first sequence $\alpha$ satisfies $(\mathrm D_B)$,

$$
\sum_{\substack{z>0\\ z+k>0}}\frac{\Psi(z/Z)}z\,z^{ia_1}(z+k)^{ia_2}\,
\overline{F_0(z)}\,G_0(z+k)\,W_\ell(z)\,W_\ell(z+k)\ll L^{-D_0}.
$$

For the successor Type II step the exact pair is

$$
\begin{aligned}
F_0(v)&=\sum_{mpr=v_*}\alpha_m\chi(m)m^{i(\varrho-\xi_2)}
\mathbf1_{p\in I_{**},\ P^-(p)>W}p^{-i\sigma}\overline{c_r},\\
G_0(v)&=\sum_{mpr=v_*}\alpha_m\chi(m)m^{i(\xi_1+\varrho)}
\mathbf1_{p\in I_{**},\ P^-(p)>W}p^{-i\sigma}\overline{c_r}.
\end{aligned}
\tag{S}
$$

Here $\chi$ is modulo $2|k|$, $I_{**}=[x^{\tau_*},x^{\eta_*}]$ is the
common band interval with $0<\tau_*<\eta_*<b_*/4<1/4$, and $c_r$ is the
common residual
coefficient from that band partition, with no roughness condition.
The first factor is the original $\alpha$, including its interval
restrictions. All frequencies, coefficient sizes and cutoff derivatives
have fixed logarithmic bounds. Substitution in P uses
$a_1=\varrho+\xi_3$, $a_2=-\varrho$ and
$\Psi(t)=t\psi_Z(t)$; the separated unweighted correlation is $Z$
times the displayed harmonic one.

Thus it suffices to establish the stated wider endpoint class. Proving
that class does not enlarge the application: (S) keeps the original
sequence, common rough interval and common residual coefficient. The
frequency and coefficient bounds are fixed before $D_0$ and $B$;
the final proxy cell precision is chosen after $B$.

## The proof chain

The proof has four components. Their estimates are composed below,
with the quantifier order recorded at the end.

1. **The physical lift** (Section 5). The correlation is the raw-pattern
   term of a pairing $\langle f,\mathcal Ag\rangle$ for the physical
   dilation operator $\mathcal A$ of Definition 3.3. Positions move by
   $kD$, where $D$ is the product of the shared and free labels. The
   vectors $f(n)=n^{-ia_1}F_0(n)q^{(\omega(n)-Ms)/2}$ and $g$ are
   mark-independent. The added comparison patterns of Section 4 produce
   shifted correlations with shift $kD_AD_B$, where $D_A,D_B$ are free
   products of size $\exp(L^c)\le D_AD_B\le x^{o(1)}$.
2. **Transference** (Section 3). If the ideal operator $\mathcal T(\Theta)$
   on independent big-group labels has norm at most $L^{-E_{\rm id}}$
   uniformly in $\Theta$, then the root-averaged moment
   $\langle u_n,(\mathcal A\mathcal A^*)^Ru_n\rangle$ with
   $R=\lceil L^{0.52}\rceil$ is at most $L^{-2RE}$ (Theorem 3.5), and
   Corollary 3.11 turns this into $|\langle f,\mathcal Ag\rangle|\ll
   XL^{-E+2C_3}$ for a mark-independent $f$.
3. **The ideal kernels** (Section 4). Comparison patterns with
   log-cell and character kernels make
   $\sup_{\Theta,|\zeta|\le L^{C_4}}\|\mathcal T(\Theta)\|\le L^{-E_{\rm id}}$
   (Theorem 4.1).
4. **The comparison correlations** (Section 5). Their multiplier
   $\mathbb E\,b_1(D_A)b_2(D_B)e(-k\theta D_AD_B)$ is small off major arcs
   by an integer bilinear estimate. On the arcs, the first endpoint's
   local Fourier energy reduces to a Mellin integral of
   $P_sP_l\mathcal R$: a small marked prime, the long rough integer, and
   $\alpha$ times the residual factor. The small-prime polynomial, an
   oscillation bound for the long rough factor, and $(\mathrm D_B)$ handle
   the three time ranges.

## What was checked, and how

Each item below names the step and what was verified. "Re-derived" means
that the argument was rebuilt independently of the source's wording;
"checked" means that each inequality of the source argument was verified
in order.

**Corollary 3.11, re-derived.** The Gram matrix
$(\langle u_n,(\mathcal A\mathcal A^*)^Ru_m\rangle)$ over a block of
positions is positive semidefinite, so its top eigenvalue is at most its
trace. Spectral Hölder gives
$|\langle f_j,\mathcal Ag_j\rangle|\le\|g_j\|\,\|f_j\|^{1-1/R}
\langle f_j,(\mathcal A\mathcal A^*)^Rf_j\rangle^{1/(2R)}$. Blocks of
length $H$ with $\log H=O_J(TL^d)$ make the factor
$(H\sup|f_n|^2)^{1/(2R)}$ bounded, because $d<0.47<0.52$ and
$\sup|f_n|\le\exp(O(\sqrt L))$. Hölder with exponents $2$,
$2R/(R-1)$ and $2R$ over the blocks gives the stated bound.

**Lemma 3.6, re-derived.** With $Q_{\rm act}$ the product of the active
primes along a path, $\log Q_{\rm act}=O_J(NTL^d)=o(L)$ needs
$0.52+d<1$. Bonferroni truncation at degree of order $NT$ has
$\exp(o(L))$ terms whose moduli multiply to $\exp(o(L))$; the counting
error $\exp(o(L)-\gamma L)$ is relative to the main term
$Q_{\rm act}^{-1}\exp(-O(NT))$. The deterministic damping of active
primes can be tiny, of order $q^{O(N^2Ms)}$, but it is the same factor in
both models and cancels exactly, so the relative estimate stands.

**Lemma 3.7, re-derived on the path weights.** For an active big prime,
the factor $p^{-1}\prod_{i:\,p\notin\Lambda_i}(1-\eta_iH_i)$ expands by
the two telescoping identities into one lifespan, with an optional ghost
birth and ghost termination at hits outside the active visits. For a
never-active prime the factor is $b_p$ plus orphan intervals. Relative to
the baseline $\prod_pb_p$, a lifespan with $r$ active runs carries exactly
$V_g^{-r}/(pb_p)$. On the operator side a fresh birth costs
$\widetilde\mu_g(p)$, each promotion $V_g^{-1}$, and a ghost birth
$V_g\widetilde\mu_g(p)$ times $-\eta_j/\rho$. Following one particle
through the visit and edge operations, its $\rho$ factors combine to
$-\eta_j$ at a ghost birth, $q_t$ at each pending hit, and $-\eta_i$ at a
ghost termination, and a nonzero residue gives no factor; this is the
residue-side weight. The local choices correspond one to one with
lifespan terms under the distinct-birth rule: dropping an unshared label
ends a lifespan, storing it and later terminating it is the suffix term,
a ghost birth followed by promotion is the prefix term, and the injection
of promoted slots is forced because each pending prime has one birth. The
path expression uses row actions only, so the factorial memory measure
enters the norm bounds but not the identity. The adjoint formula (3.19)
and the accounting (3.25) were checked as written.

**Lemma 3.8 and the truncation.** To obtain the ghost adjoint, partition
an input memory into $k$ continuing and $t$ terminated particles. Its
factorial measure times the subset count is
$\binom{k+t}{t}/(k+t)!=1/(k!t!)$. A batch of $b$ fresh particles
adds $1/b!$. Thus interchanging the terminated and fresh variables in
the joint integral interchanges the birth and termination coefficients,
with no reciprocal-prime factor. For an edge, retrieving $a$ ordered
particles from memory size $j$ leaves measure $1/(j-a)!$. Reversal
retrieves the $b$ stores from memory size $j-a+b$ and leaves exactly
the same measure. Residues have counting measure; a prescribed residue
has mass one. This derives (3.19) and (3.25), including numerical
coincidences, rather than treating them as a probability normalization.

The ghost row ratio is
$\exp(|C_i|v\,\widetilde\mu_g(\mathcal P_g))(A_i+|D_i|/v)^{z}$, and
(3.21) makes the second factor at most one for both damping values; the
column ratio swaps $C_i$ and $D_i$ and is covered by the factor
$\max(1,v_+)$ in (3.21). Promotions are controlled by
$\sup_z(z)_a\rho^{z-a}$, and on reversal stores become ordered
retrievals controlled in the same way. The memory cap $\lceil L^2\rceil$
costs $\exp(-\Omega(L^2))$.

**Lemma 3.9, re-derived.** In each small group, source symmetrization
omits a uniform $\ell$-subset of the $M$ distinct labels, independently of
every big-group choice, because the coefficients use big labels only. The
omitted products $U$ are distinct integers below
$\exp(\ell|\mathcal S|L^b)<\exp(L^c)\le p$ for every pending big prime
$p$, so they are distinct modulo $p$. A promotion needs
$r+\sigma kD_{\mathcal B}F/U\equiv0\pmod p$, with $F$, $k$ and
$D_{\mathcal B}$ invertible, which fixes $U$. So at most
$\lceil L^2\rceil$ of the $\binom M\ell^{|\mathcal S|}$ choices allow any
promotion, one for each pending particle under the memory cap. For stores, the
same count uses the target-side symmetrization of the reversed edge.
Schur's test gives (3.30).

**Lemma 3.10, re-derived.** On a clean edge, the small-state maps
$P_{\mathbf d}$ factor the physical normalization $V_g^{-M-\ell}$
symmetrically, with $\sum_{\mathbf d}\|P_{\mathbf d}w\|^2\le
L^{C_s}\|w\|^2$ and $C_s$ independent of $J$. Fourier transformation on
the small torus and the pending residues turns translation by
$\sigma kd'D_{\mathcal B}$ and the closure phase into
$e(\sigma\Theta D_{\mathcal B})$ with $\Theta=kd'(\theta+\vartheta)$
real, where $\vartheta$ is the fiber's frequency. Each fiber is the ideal
operator, up to the density change $1+O_J(sN/P_*)$ and the
free-label ban, both of norm cost $o(L^{-A})$.

**The equality-rank expansion, re-derived.** The identity (3.41) is the
sign sum over value-preserving permutations, and the rank-$r$
coefficients sum to at most the coefficient of $t^r$ in
$\prod_{j<A_*}(1+jt)$, hence at most $A_*^{2r}$. Large rank uses one
point mass $O(1/P_*)$ per dependent birth; with
$r_0\asymp NT/L^c$ the tail is $o(L^{-EN})$. Small rank inserts each
equality through phases at its two birth addresses, so at most $2r$
edges lose the signed bound, and $r_0=o(N)$ keeps the total at
$L^{(-G+C_v+o(1))N}$.

**Section 4, re-derived.** The collapse (4.4) of tuple tests to integer
sequences; the integer bilinear Lemma 4.2; Lemma 4.3 for denominators
above $Q$ (bilinear bound for both terms, the kernels being operators of
norm at most $2$) and at most $Q$ (character expansion of $e(uv/r)$ with
$\sum|c_\psi|\le\sqrt Q$, the reproduction formula (4.18), discarded cells
and the Lipschitz error of the log-phase); and the cancellation in
Theorem 4.1. There, the symmetric Efron–Stein components that contain
every probe of a block and avoid the last $\ell$ slots form a fraction at
most $2\ell^\ell m^{-\ell}$ per group, and the alternating sum over
nonempty freed subsets equals one exactly. Each of the two matched log
products changes by less than $h$, so their sum changes by less than
$2h$; this constant is absorbed by the error term in (4.17).

**Section 5, re-derived or checked.** The raw pattern's lifted pairing
equals the target sum: removing the shared product $D_R$ turns $1/n$
into harmonic draws of mass one, leaves $W_\ell(w)W_\ell(w+k)$, and
cancels the phases. The endpoint norm $X^{1/2}L^{C_6}$ has $C_6$
independent of $J$, through a fixed fourth divisor moment. The minor-arc
claim follows from Dirichlet approximation of $k\theta$ and Lemma 4.2.
On the arcs the factors $m,p_s,p$ are units modulo the arc denominator,
and splitting $r$ by $(r,r_0)$ leaves a unit modulo $r_0/(r,r_0)$, so
principal and imprimitive characters are kept. The Gallagher conversion
(5.14)–(5.16), Lemma 5.2 (at most $\exp(O(L^b+L^{1-a}\log L))$
exceptional intervals), Lemma 5.3 (the Gram kernel bound and
$U>Y^{0.6}$, which needs $\eta<0.4$), Lemma 5.4 (van der Corput with
$K=\lceil4/\tau\rceil+3$ derivatives) and the completion were all
re-derived. The low-time range uses $(\mathrm D_B)$ with modulus at most
$L^{C+C_{\rm arc}}$, frequency at most a fixed power of $L$, and an
interval inside $[1,x^2]$.

**Section 2 inputs used by Sections 3–5.** The block sieve (Lemma 2.9)
and the rough-integer polynomial (Corollary 2.10), which Lemma 5.4
needs, were re-derived: the truncated inclusion–exclusion
$\sum_{a\le h}(-1)^a\binom ta=\binom{t-1}h$ for even $h$ and $t\ge1$
(the sum is one when $t=0$), the disjoint
supports giving coefficients of modulus one, and the level
$z^{4h+2}$. The Siegel–Walfisz theorem, the divisor moments, the mean
value and derivative tests, and Fourier separation are classical and are
used in their stated forms.

## Closing the quantitative estimate

The bounds above compose as follows. This calculation records the
uniformity that is needed in addition to the sign check.

Let $C_6$ be the endpoint norm exponent and $C_F$ the logarithmic cost
of the initial dyadic and Fourier separations. Both are fixed by the
endpoint data before the comparison family. Choose a transfer exponent
$E>D_0+2C_6+C_F+3$. The physical list normalization is essential here:
if $S'$ is a list of $M$ primes in each group and $P(S')$ its product,
then

$$
\sum_{S'}\frac1{P(S')}\prod_g V_g^{-M}\le1.
$$

Applying the fixed fourth divisor moment after fixing $S'$ bounds
$\|f\|^2$ and $\|g\|^2$ by $XL^{2C_6}$ without a power of $L$
depending on $J$. The pointwise bound required in Corollary 3.11 follows
because only $O(\sqrt L)$ prime factors above $W$ can divide an integer
of size $x^{O(1)}$; the two rough divisor choices therefore number
$\exp(O(\sqrt L))$.

Set $P_*=\exp(L^c)$ and $B_{\rm mem}=\lceil L^2\rceil$, keeping this
cutoff distinct from the discrepancy exponent $B$. The memory argument
gives, before restoring birth distinctness,

$$
\|\mathcal E_i\|
\le 2L^{-E_{\rm id}+C_s}
+2L^{C_a}\sqrt{B_{\rm mem}/\binom{J+\ell}{\ell}^{|\mathcal S|}}.
$$

Choose $G>E+C_v+3$ and $E_{\rm id}>G+C_s+2$. The ideal construction
chooses its probes and all kernel precisions with this target. Only then
choose $J$ so that
$\tfrac12c_0\log\binom{J+\ell}{\ell}>C_a+G+3$.
The last display is at most $L^{-G}$ eventually. Neither $C_v$ nor
$C_s$ depends on the comparison complexity, so this order has no cycle.

For completeness, the rank correction does not replace distinct births
by an absolute single-collision error. For rank $r$, the number of
weighted equality patterns is at most $L^{C'r}$, and their two usable
bounds are

$$
L^{C_h(N+1)}(C/P_*)^r,
\qquad
O\!\left(L^{(-G+C_v)N+C_v+2r(G+C_a)}\right),
\quad N=2\lceil L^{0.52}\rceil.
$$

In the first bound, chronological dependent births each pay a fresh
atom $O(P_*^{-1})$; remembering a pivot after its death only conditions
future bounds on a fixed value. In the second, Fourier phases impose
equalities at their birth operations. At most $2r$ edges lose their
signed estimate. Splitting at
$r_0=\lceil C''N\log L/L^c\rceil$, the first bound summed over
$r\ge r_0$ is $o(L^{-EN})$ for large fixed $C''$. Since
$r_0/N=o(1)$, the second summed below $r_0$ is
$L^{(-G+C_v+o(1))N}=o(L^{-EN})$.
The memory tail is $\exp(-\Omega(L^2))$ and residue replacement has
arbitrary relative precision. Hence the root moment has the required
saving, and Corollary 3.11 bounds the residual physical pairing.

Removing shared harmonic draws makes its raw term exactly the desired
correlation. For a comparison term, put $Y=ZH'$ and
$H=H'/L^{C_{\rm arc}}$, where $H'$ is the product scale of the two
nonempty free products. The integer bilinear estimate controls the
multiplier off the arcs. On an arc the character expansion retains
every character of the quotient modulus, including the principal one;
the residual gcd restriction goes into $d_r$, not into a replacement
for $\alpha$.

The local Fourier-energy estimate reduces, with fixed logarithmic costs,
to the following bound for each four-factor box:

$$
I=\int_{|t|\le2LY/H}|P_s(t)P_l(t)\mathcal R(t)|^2\,dt.
$$

The small prime has size $P\le\exp(L^b)$, the rough integer has
$x^{\tau_*}/2\le P'\le x^{\eta_*}$, and the residual has size
$U\asymp Y/(PP')>Y^{0.6}$. The boxed coefficients have squared norm
$L^{O(1)}/U$ by a fixed divisor moment, uniformly in $c_r$.
The preceding lemmas give constants $K_1,K_2,K_3$, fixed without $B$
or the proxy precision, such that

$$
I\ll L^{-2A_s+K_1}+L^{-2A_l+K_2}
+L^{-2B+B_0+K_3}+o(L^{-Q})
\tag{3}
$$

for any prescribed fixed $Q$, with choices in the order described next.

For the first term use $|P_s|\le L^{-A_s}$ and ordinary mean square
for $P_l\mathcal R$. Its size exceeds the time range because
$H/(2LP)\to\infty$, using $b<c$. On the complementary set, the
$j$-th moment with $j=\lfloor\log Y/\log(2P)\rfloor$ gives at most
$\exp(O(L^b+L^{1-a}\log L))=Y^{o(1)}$ occupied unit intervals.
The Gram kernel for the residual is bounded by
$U/(1+|t-t'|)+Y^{1/2}$; its row sum on those intervals is
$O(U\log Y)$ since $U>Y^{0.6}$. This bounds the sum of residual
suprema by $L^{K_2}$ without multiplying by the number of intervals.
Choose $A_l$ large enough, and then the long-rough-factor lemma gives
$|P_l(t)|\ll L^{-A_l}$ for $L^{B_0}\le|t|$ throughout the retained
time range. This proves the second term.

For $|t|\le L^{B_0}$, the first factor of $\mathcal R$ is

$$
\sum_{m\in I}\frac{\alpha_m\chi_m(m)m^{i(t+\sigma_0)}}m,
\qquad I\subset[1,x^2].
$$

It is the same restricted sequence as in (S). The character modulus and
the frequency are bounded by fixed powers of $L$ chosen earlier. Taking
$B$ above those exponents gives a bound $L^{-B}$, and integration over
an interval of length $2L^{B_0}$ gives the last term of (3). The other
factors have harmonic bounds independent of $B$.

Given $Q$, first choose $A_s>(Q+K_1)/2+1$ and
$A_l>(Q+K_2)/2+1$, then choose $B_0$ from the long-factor lemma, and
finally choose $B>(Q+B_0+K_3)/2+1$ as well as the modulus and frequency
requirements. Then $I\ll L^{-Q}$. Taking $Q$ large enough for all the
already fixed separation costs proves the local energy bound
$\int_{|\beta|\le1/H}|\widehat{\mathcal U}(u/r+\beta)|^2d\beta
\ll YL^{-A}$. Cauchy--Schwarz with the second endpoint's norm controls
each major arc; the polynomial number of arcs and comparison patterns
is absorbed by choosing $A$ first. Combining the comparison bounds with
the small residual pairing proves P at the asserted uniformity.

The argument uses no feature of the final proxy cells. It applies to
every sequence in (S) satisfying the fixed coefficient bounds and
$(\mathrm D_B)$, including arbitrary further interval restrictions.
It does not prove that the proxies have that discrepancy: that is part
of E. The use of $|k|$, translations, and units modulo primes larger
than $|k|$ covers both signs without modifying the chosen exponents.

## The order of choices

For the consumed class the order is consistent. The group and band data,
$C$ and $D_0$ come first. The endpoint norm exponent, which is independent
of $J$, fixes the transfer target $E$; then $G>E+C_v+3$ and
$E_{\rm id}>G+C_s+2$. The probe count $m$, the comparison precision $A_0$
and the kernel precisions of Theorem 4.1 follow, hence $C_1$, and then
$J$, large enough for the rare-transfer saving (3.32). Next come the arc
exponent, the local-energy target, $A_s$, the long-polynomial saving and
$B_0$. The discrepancy exponent $B$ is chosen last within the theorem.
None of these depends on the proxy precision of the prime extraction, so
that precision can be chosen after $B$, as the Type II application needs.
Both signs of $k$ are covered: $k$ enters only through $|k|\le L^{O(1)}$,
translation by $kD$, invertibility modulo primes above $|k|$, and the
Dirichlet approximation of $k\theta$, whose sign changes only a numerator.

## Standing and what remains

The reconstruction closes P on the consumed class at author-recorded
standing. Its source is still an unrefereed manuscript, and no
independent acceptance or tier is conferred. The retained derivation
supports this conclusion at author-recorded standing. The classical
boundaries are Siegel--Walfisz in
Theorem 2.2, Mertens' estimates in (2.2), and the first and second
derivative tests in Lemma 2.7. Divisor moments, mean squares, smooth
separation and the block-sieve input are derived in Section 2 as used
above; the multiplicative large sieve is not needed for P itself.

The
[[research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/_index|whole P examination of 2026-10-15]]
records **refutation-failed** for the full supplied endpoint class and signed
application. Its distinct grade is **VOID for present acceptance**, with
zero accepted independent weight. A separate ruling found the grader's
unrelated-status exposure immaterial, but expressly supplies no new
whole-contract PASS. The source reconstruction therefore retains its author
standing; the original classical proofs and PDF fidelity remain outside the
examination.

Premise P does not settle Problem 824. The route also needs (E): the
Section 2 estimates, the candidate mass of Proposition 7.1, the proxy
discrepancy of Lemma 7.3 and the proxy densities of Lemma 7.4. Only the
Section 2 inputs used inside the proof of P were checked here. With P and
E, the [[research/erdos_824/_index|conditional route]] gives Hypothesis
$\mathrm A^+$ and then Li and Zhuang's bound $h(x)>x^{2-\varepsilon}$.
The
[[research/smooth_successor_primes/evidence/verify/conditional_chain/_index|whole conditional implication has a separate examination]],
whose distinct grade is pending; it does not supply either antecedent.

The P examination's scrutiny includes:

- the factorial adjoint measures (3.19) and (3.25) of the memory space,
  on which the column bounds of Lemmas 3.8 and 3.9 rest;
- the completeness of the clean and dirty decomposition of each edge;
- the claim that every exponent fixed before $J$ is independent of $J$:
  $C_{\rm abs}$, $C_v$, $C_s$, $C_6$ and the cost of the comparison
  family.
