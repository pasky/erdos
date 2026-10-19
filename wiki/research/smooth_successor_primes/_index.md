---
name: research/smooth_successor_primes
title: Smooth successor primes from the weighted-dilation argument
desc: "Independently graded conditional chain to smooth successor primes and coprime squarefree equal-divisor-sum pairs, using the surviving elementary estimates and explicit unaccepted P and classical premises."
problems:
- 824
created: 2026-10-15T07:33:49Z
updated: 2026-10-16T04:55:23Z
---

# Smooth successor primes from the weighted-dilation argument

[[research/_index|..]]

[[research/smooth_successor_primes/evidence/_index|evidence/]]: Frozen subjects, conditional whole-conclusion examination and passing grade, preserving the balanced-range qualification, P and classical premises.

[[research/smooth_successor_primes/li_zhuang_reduction|li_zhuang_reduction]]: Li and Zhuang's counting reduction from smooth successor primes to
h(x)>x^(2-epsilon), with the overlap bound, multiplicity of gcd removal,
strict real endpoint, and squarefree conclusion written out.

[[research/smooth_successor_primes/shift_sign_analytic_core|shift_sign_analytic_core]]: The signed shift in the weighted-dilation transference and cancellation
argument: the memory identity, norm bounds, equality-rank expansion,
ideal kernels and local Fourier-energy estimates, with their parameter
order and the precise source estimate still needed by the successor
route. Author examination, without independent acceptance.

[[research/smooth_successor_primes/signed_type_ii|signed_type_ii]]: The independently graded conditional Type II derivation for mn=2u-1, retaining both signed determinant directions, the diagonal and exact unaccepted shift-cancellation endpoint hypothesis.

[[research/smooth_successor_primes/successor_prime_extraction|successor_prime_extraction]]: The independently graded conditional extraction of primes p=2u-1 with smooth p+1, using the proved balanced dyadic scope and exact P and classical premises; the unrestricted dyadic claim is refuted.

***

This folder's results that are not drawn from a cited source are Plasma AI's,
at the exact conditional scope accepted by the
[[research/smooth_successor_primes/evidence/verify/conditional_chain/_index|whole-conclusion examination and distinct passing grade]]. The route is Shisheng Li and
Zhong Zhuang's, recorded on
[[problems/arithmetic_functions/E0824/claims/2026_10_07_li_zhuang|their claim page]]:
their reduction follows Pollack and Pomerance after an idea of Erdős, and the
counting method is OpenAI's
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]].
This combined sketch derives the successor count from precise source estimates
and carries their provisional standing into the final implication.
The [[research/erdos_824/smooth_successor_sign_audit|compact sign audit]]
lists the substitutions relative to the predecessor proof; the derivations
below supply their full conditional interfaces.

## Target

[[problems/arithmetic_functions/E0824/_index|Problem 824]] asks about the count

$$
h(x)=\#\{(a,b)\in\mathbb N^2:
1\le a<b<x,\ (a,b)=1,\ \sigma(a)=\sigma(b)\}.
$$

The question is whether, for every $\varepsilon>0$ and every sufficiently
large real $x$, $h(x)>x^{2-\varepsilon}$. Its recorded status is open.
Pollack and Pomerance proved $h(x)>x^{1.4}$
([[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/theorem_p24|their Section 6 result]]).
Write $L=\log x$ and $P^+(m)$ for the largest prime factor of $m$.
The route derives three statements under the source premises below.

1. **Successor count.** For every fixed $0<\delta<1/4$ there are
   $c,C_A,C_w>0$ such that, for every sufficiently large real $x$, at least
   $c xL^{-C_A-1}\exp(-C_w\sqrt L)$ primes $p$ satisfy
   $2x-1\le p\le4x-1$ and $P^+(p+1)\le x^\delta$.
2. **Hypothesis $\mathrm A^+$.** For every $0<\delta<1/4$ and $\eta>0$,
   every sufficiently large real $y$ has at least $y^{1-\eta}$ primes
   $p\le5y$ with $P^+(p+1)\le y^\delta$.
3. **Coprime pairs.** For every $\varepsilon>0$ and every sufficiently large
   real $x$, $h(x)>x^{2-\varepsilon}$, even when both entries must be
   squarefree.

## Exact source premises

**(P)** is the manuscript's Theorem 5.1, its lifted shift-cancellation
estimate, restated with all endpoint hypotheses on the
[[research/smooth_successor_primes/signed_type_ii|Type II page]]. It bounds

$$
\sum_{z>0,\ z+k>0}\frac{\Psi(z/Z)}z\,
z^{ia_1}(z+k)^{ia_2}\overline{F_0(z)}G_0(z+k)W_\ell(z)W_\ell(z+k)
\ll L^{-D_0}
$$

for arbitrary fixed $D_0$, uniformly for nonzero integer shifts
$|k|\le L^C$, $Z=xL^{O(1)}$, and the prescribed endpoint class, once the
original coefficient sequence $\alpha$ has sufficiently strong character
and Mellin discrepancy. That endpoint class includes a compulsory integer
factor in a fixed positive power range, rough above $\exp(\sqrt L)$.
The source proposes a proof in Sections 3--5. It is an unrefereed premise
here. The manuscript's
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/theorem_1_2|predecessor-count statement]]
concerns $p-1$ and does not itself imply $\mathrm A^+$.

The [[research/erdos_824_uniformity/shift_cancellation_reconstruction|local
reconstruction of P]] supplies an author-recorded argument for the endpoint
class used here. Its displayed pair (S) is the pair in the Type II page:
the original restricted $\alpha$, the common interval $I_{**}$, the common
residual coefficient $\overline{c_r}$, and characters modulo $2|k|$ are
unchanged. Substitution uses $a_1=\varrho+\xi_3$, $a_2=-\varrho$ and
$\Psi(t)=t\psi_Z(t)$; multiplication by $Z$ recovers the unweighted
correlation. No discrepancy of a different sequence is inferred. The
reconstruction's internal mark parameter $J$ is distinct from the proxy
precision $S$ of the extraction: every choice inside P, including $B$, is
fixed before $S>2B+3$. This is an interface identification, not independent
acceptance of P or a proof of proxy discrepancy.

**(E)** consists of the manuscript's Section 2 estimates, Proposition 7.1
(candidate mass, uniformly in the exceptional-slot position), Lemma 7.3
(proxy discrepancy, uniformly under interval restrictions), and Lemma 7.4
(proxy densities and the Buchstab identity). Their needed statements,
parameters and roles are given on the
[[research/smooth_successor_primes/successor_prime_extraction|extraction page]].
Only the bound (7.17) mentions $2u+1$, and its proof uses that expression
only through its size $x$ up to fixed factors. It gives the same bound for
$2u-1$. The
[[research/smooth_successor_estimates/_index|elementary reconstruction of E]]
supplies written author proofs at these consumed ranges. Its
[[research/smooth_successor_estimates/block_sieve|block sieve]] has coefficients
of modulus at most one and the required level, for both growing even $h$ and
the fixed upper-bound choice $h=2$. Its
[[research/smooth_successor_estimates/proxy_discrepancy|proxy discrepancy]]
uses full-cell averages followed by arbitrary interval restrictions inside
$[x^{b_1/4},x^{1-b_1/4}]$. It handles principal and imprimitive characters
and all twists of size at most $L^B$ once $S\ge2B+2$, with coefficient
bound one independent of $S$.

The [[research/smooth_successor_estimates/proxy_densities|density proof]]
supplies the balanced proxy bound with absolute constant three, the cofactor
estimate on $\gamma\ge b_1$, $w-\gamma\ge\kappa$, $w\le1$, the
minimum-coordinate identity and the finite-mesh subtraction. The actual
cofactors have $w-\gamma\ge2\kappa+o(1)$, so no density at $w=\gamma$
is assumed. The
[[research/smooth_successor_estimates/candidate_mass|candidate-mass proof]]
makes its comparison constants independent of the later fixed
$j_{**}\ge j_0$; only the threshold for $x$ may depend on that slot.
The [[research/smooth_successor_estimates/classical_inputs|classical-input inventory]]
derives the consumed moments and smooth separation and gives the complete
Type I large-sieve application. Its external boundary is PNT with arbitrary
logarithmic accuracy, Mertens, Chebyshev, Siegel--Walfisz and the
multiplicative large sieve, in the precise versions stated there.

No E proof uses P. The candidate geometry, finite prefix and $j_0$ precede
$\kappa$; then come $b_1$, the exceptional slot and the bin mesh; then the
Type II saving and P's choices, including $B$; finally $S>2B+3$ and the
prime-number-theorem accuracy $S+2$. The numerical coefficient bound does
not feed the last choice back into P. The E deductions have an independent passing grade at the quoted classical
boundaries. P remains author-recorded with zero accepted independent weight;
the source manuscript remains unrefereed.

## The combined argument

1. **Type II for $2u-1$.** Assuming (P) and the Section 2 estimates, the
   [[research/smooth_successor_primes/signed_type_ii|signed Type II derivation]]
   gives $\sum_{mn=2u-1}A(u)\Psi(u/x)\alpha_m\beta_n\ll xL^{-D_*}$ for
   bounded $\beta$ and an appropriately restricted $W$-rough $\alpha$ with
   discrepancy. The partition $u=eh$ retains all group factors and the
   compulsory rough integer in $h$. The off-diagonal identities are
   $m'-m=-2ek$, $h'-h=-kn$, and $mh'-m'h=k$. Their converse, using
   $(m,k)=1$, recovers a positive integral $n$. The resulting cross-products
   $z=m'h$ and $z+k=mh'$ have exactly the endpoint form of (P), with the
   original $\alpha$ still carrying discrepancy.
2. **Prime extraction.** Under (E), the
   [[research/smooth_successor_primes/successor_prime_extraction|signed sieve argument]]
   proves Type I distribution in the unit class $u\equiv\bar2$ for odd
   moduli, uses the Type II estimate to replace roughness and prime tests by
   their cell proxies, and subtracts composites. The balanced range uses
   $mn\equiv-1\pmod{D_1}$ and the same residue counts as the predecessor
   argument. It leaves weighted prime mass $\gg X_A/L$. Candidate mass
   $X_A\gg xL^{-C_A}$ and the pointwise bound
   $A(u)\Psi(u/x)\le\exp(C_w\sqrt L)$ give the successor count. Its ratio to
   $x^{1-\eta}$ tends to infinity for every fixed $\eta>0$, so taking $x=y$
   gives the exact $\mathrm A^+$ above for all large real $y$.
3. **Counting pairs.** The
   [[research/smooth_successor_primes/li_zhuang_reduction|full counting reduction]]
   gives Li and Zhuang's Theorem 1.3, including the squarefree conclusion and
   the strict range $1\le a<b<x$. For a fixed $0<\varepsilon<1$, choose
   $B\ge8/\varepsilon$, $\eta=\varepsilon/16$ and $\delta=1/(2B)$. It uses
   $\mathrm A^+$ at $y=(\log x)^B$. Products of
   $k=\lfloor\log x/\log(5y+1)\rfloor$ distinct available primes give
   $N\ge x^{1-\eta-1/B-o(1)}$ squarefree integers below $x$, with at most
   $U=x^{o(1)}$ divisor-sum values. Removing pairs with many common primes
   and dividing by the gcd costs a multiplicity of at most $2x^\eta$.
   Therefore $h(x)\ge N^2/(4Ux^\eta)>x^{2-\varepsilon}$. This implication
   uses neither (P) nor (E) except through $\mathrm A^+$.

The [graded composition](evidence/verify/conditional_chain/interface_disposition.md)
uses operative E1 and the exact E2–E5 scopes to deduce $\mathrm A^+$ under
the complete P endpoint hypothesis and quoted classical premises, then the
squarefree-pair bound. Its independent passing grade accepts that conditional
argument. P's author reconstruction still has zero accepted independent
weight; the source manuscript remains unrefereed and the original-source
reading limits persist. No unconditional accepted resolution of Problem 824
follows.

## Sign, ranges and uniformity

The change from $p-1$ to $p+1$ occurs inside the Type II and sieve proofs.
Its essential checks are:

- **Divisibility and positivity.** The signed identities and their converse
  retain $UV\asymp x$, $x^{b_*}\le U,V\le x^{1-b_*}$,
  $E=UL^{-K_0}$, $\tfrac12EL^{-C_s}\le e\le2E$ and
  $0<|k|\ll L^{K_0+C_s}<W$. The cutoffs impose $e>0$ and $n\asymp V$ after
  reconstruction; no unsigned ordering of $m,m'$ is imposed.
- **Units and local counts.** The rough integers $m,m'$ are units modulo
  $2|k|$. Type I uses odd squarefree $d$ and its unit class $\bar2$.
  The balanced sieve's odd $D_1$ may have repeated prime factors and includes
  the exceptional integer. The congruence $mn\equiv-1\pmod{D_1}$ has
  $\varphi(D_1)$ unit pairs. Modulo each odd sieve prime $l$, the two
  disjoint bad sets $mn\equiv0$ and $mn\equiv-1$ have $2l-1$ and $l-1$
  pairs.
- **Moments and partition.** Fixed divisor moments control
  $\sum_{u\asymp x}\tau(u)\tau(2u-1)$ and
  $\sum_{v\ll x}\tau(v)\tau(v+1)^3$. Only pure band primes enter $e$;
  all group factors and the exceptional rough integer stay in $h$.
  The costs before choosing $K_0$ do not depend on $K_0$.
- **Analytic estimates.** The
  [[research/smooth_successor_primes/shift_sign_analytic_core|analytic-core examination]]
  follows the memory identity, rare transfers, clean norm, equality-rank
  expansion, ideal comparison kernels and local Fourier-energy argument.
  The shift enters through $|k|$, translation, or invertibility modulo
  group primes larger than $|k|$. Positive shifted positions remain of
  size $x^{1+o(1)}$. Theorem 5.1 already asserts both signs.

No sign-specific obstruction was found in these deductions. The two Type II
arguments use a common uniform class of instances of (P): endpoint forms,
character moduli $2|k|$, polynomial logarithmic frequency bounds, scales
$Z=xL^{O(1)}$, and both signs of $k$. Their pulled-back cutoffs and Fourier
coefficients differ. This is a statement about a class of permitted data,
not an assertion that the arguments make identical individual calls to (P).

A proof uniform over that endpoint class would support both transfers.
Checking particular endpoints used by one argument, or accepting the
predecessor-count statement alone, does not supply that uniform proof.
Failure of (P) outside the consumed class would not by itself refute this
route. The sufficient restriction is stated at the end of the
[[research/smooth_successor_primes/shift_sign_analytic_core|analytic-core page]].

## Standing and the remaining dependence

The signed Type II and sieve implications are derived by Plasma AI under
(P) and the operative E estimates. The final counting implication is Li and
Zhuang's, written out here with its parameters checked. Their complete
conditional examination has a [distinct whole-contract PASS grade](evidence/verify/conditional_chain/grade.md),
examined on 2026-10-16 UTC, retaining every antecedent and reading limit. The reported external Lean proof covers the
lower-bound implication at natural $x$, without the squarefree addendum;
it has not been built or audited here.

The first deep analytic input is (P). Its author reconstruction depends on
transference Theorem 3.5 and Corollary 3.11, ideal-kernel Theorem 4.1, and the
comparison analysis of Section 5. It records derivations of these steps,
with the classical source boundaries stated on its page; the manuscript
remains unrefereed and the reconstruction has no independent acceptance.
The
[[research/smooth_successor_estimates/_index|separate E reconstruction]]
supplies the elementary estimates at the intervals and choice order consumed
above, with a separate passing grade relative to the quoted classical
premises. The [graded interface comparison](evidence/verify/conditional_chain/interface_disposition.md)
finds no missing clause at the actual consumed scopes: the original restricted $\alpha$, common
residual coefficient, rough interval, both shift signs, and modulus $2|k|$
in P agree with the Type II input; E supplies that original sequence's
discrepancy and every density and mass bound used by the sieve.

The
[[research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/_index|P examination and its VOID grade]]
retain zero accepted independent weight. The separate exposure ruling
resolves the eligibility question only; it supplies no whole-contract PASS.
The
[[research/smooth_successor_estimates/evidence/verify/elementary_estimates/_index|E examination]]
and the
[[research/smooth_successor_primes/evidence/verify/conditional_chain/_index|conditional-chain examination]]
have distinct **PASS** grades at their separate stated scopes. The latter
accepts **refutation-failed** for
the complete P-and-E implication at every sufficiently large real $x$ with
strict $1\le a<b<x$, coprimality and squarefreeness. It does not establish
its antecedents. The frozen unrestricted E1 cutoff and isolated dyadic
formulations have separate **refuted-as-stated** findings; only the consumed
$z\ge1$ and balanced ranges survive. Their current explicit restrictions
are disclosed on the owning pages. The complete proposal has no accepted
unconditional conclusion here.
Nothing here assesses the manuscript's further totient-fiber argument or
changes the standing of Problem 821 or Problem 824.
