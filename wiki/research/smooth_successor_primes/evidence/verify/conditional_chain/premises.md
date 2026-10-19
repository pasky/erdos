---
name: research/smooth_successor_primes/evidence/verify/conditional_chain/premises
title: "Assumptions and source interfaces"
desc: Exact conditional assumptions, classical theorem interfaces, and source-reading limits of the squarefree-pair examination.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Assumptions and source interfaces

***

This is part of the restatement and premise account of
[the examination report](report.md), dated 15 October 2026. The census comes
from the supplied statements, proof sites and consequence sentences. It is
not inferred from the metadata's premise list. All references below resolve
within the retained frozen subject.

## P: the complete consumed shift-cancellation hypothesis

Use L=log x, T=log L, W=exp(sqrt L), with all fixed parameters chosen before
x tends to infinity. Prime factors are positive-prime factors of positive
integers; P^-(1)=infinity and P^+(1)=1. Falling factorials count ordered
distinct marks. A dyad means [Y,2Y), or a fixed constant enlargement.

The group data are fixed constants 0<a<b<c<d<0.47, c_0,C_0,v_-,v_+>0,
q in (0,1), and integer ell>=1. For each large x there are disjoint small
and big group index sets, each of cardinality between c_0 T and C_0 T.
All prime groups are mutually disjoint. Small primes belong to
[exp(L^a),exp(L^b)]. Each big group consists of all primes in an interval
inside [exp(L^c),exp(L^d)]. Its harmonic mass V_g is between v_- and v_+.
For omega_g(n) the number of distinct divisors from group g, define n_* as
the largest group-free divisor of n and

$$
W_\ell(n)=\prod_g q^{\omega_g(n)-\ell}
\frac{(\omega_g(n))_\ell}{V_g^\ell}.
$$

For B fixed, D_B means that for every interval I contained in [1,x^2],
every Dirichlet character chi of modulus at most L^B, including principal
and imprimitive characters, and every real |t|<=L^B,

$$
\left|\sum_{m\in I}\frac{\alpha_m\chi(m)m^{it}}m\right|\le L^{-B}.
$$

An allowed endpoint has the form

$$
F_0(n)=\sum_{mpr=n_*}\alpha_m\chi_0(m)m^{i\sigma_0}
\mathbf1_{p\in I_p,\ P^-(p)>W}p^{i\sigma_1}c_r.
$$

Here p is an integer, not necessarily prime; alpha is supported on integers
rough above W; |alpha_m|,|c_r|<=L^C; I_p is an interval in [x^tau,x^eta]
for fixed 0<tau<eta<1/4; chi_0 has modulus at most L^C; and
|sigma_0|,|sigma_1|<=L^C. There is no roughness condition on r. The endpoint
depends on n only through n_*.

P asserts the following entire uniform implication, as supplied in
[signed_type_ii.md](../../assets/conditional_chain_subject/signed_type_ii.md.txt), lines 80–108.
For fixed group data, endpoint bounds C,tau,eta, target D_0>0, and a fixed
positive compact support interval [c_Psi,C_Psi], there exists a fixed B
such that, for all large x, all nonzero integers k with |k|<=L^C, both
signs included, all xL^(-C)<=Z<=xL^C, all |a_1|,|a_2|<=L^C, all smooth
Psi on that support with derivative bounds
norm(Psi^(j))_infinity<<_j L^(C(j+1)), and all allowed F_0,G_0 whose
alpha in F_0 satisfies D_B,

$$
\left|\sum_{z>0,\ z+k>0}\frac{\Psi(z/Z)}z
z^{ia_1}(z+k)^{ia_2}\overline{F_0(z)}G_0(z+k)
W_\ell(z)W_\ell(z+k)\right|\ll L^{-D_0}.
$$

The hypothesis also includes conjugation of the discrepancy-bearing endpoint
or its coefficients. This review assumes the full statement, including its
coefficient classes and uniformity. It supplies no proof of P and no audit of
the omitted Sections 3–5. The supplied statement is the interface being tested;
its fidelity to an original Section 5 PDF is not separately established.

## E and the band weight in the deductions

The general Type II bands have fixed 0<c_1<c_2, s'>0 and lambda>1, with
c_2s'<1/4 and s_j=s'L lambda^(-j), for 0<=j<=j_x. The band Q_j consists
of all primes with logarithms in [c_1s_j,c_2s_j]. These bands are pairwise
disjoint and disjoint from the groups. The last scale lies between c_- T
and c_+ T for fixed 0<c_-<=c_+. Each band has a fixed integer number r_0
of labelled slots, with repetitions allowed and
(r_0-1)c_1/lambda>=c_2+1. All slots contain band primes except a designated
slot of fixed band j_**, containing an integer rough above W in
[x^tau_*,x^eta_*], where tau_*=c_1s'lambda^(-j_**) and
eta_*=c_2s'lambda^(-j_**). The normalized list count is a_Q, with factor
product_j (1/r_0!), and A(u)=a_Q(u_*)W_ell(u).

The signed Type II statement quantifies over every fixed D_*,b_*,C>0 with
eta_*<b_*/4, fixed smooth Psi supported in a positive compact interval,
UV comparable to x with x^b_*<=U,V<=x^(1-b_*), and complex sequences alpha,beta
bounded by L^C. Alpha is rough-supported and its actual dyadic and any
further interval restriction satisfies the required D_B. Some B depending
only on the fixed data suffices; beta has no discrepancy hypothesis. The
conclusion is the uniform bound O(x L^(-D_*)) for the weighted sum over
mn=2u-1. This is a deduction from P and E, not an extra premise.

For extraction, fix 0<delta<1/4 and a nonnegative smooth Psi supported on
[1,2], positive on a closed interior interval of positive length. Take
q=1/2, ell=1, lambda=2, (c_1,c_2,c_3,c_4)=(1,6/5,3/2,9/5),
s'=1/[r_0(c_1+c_2)], with r_0 fixed so c_2s'<delta and
(r_0-1)c_1/2>=c_2+1. Take j_x maximal with c_1s_(j_x)>=20T. The group
logarithms [c_3s_j,c_4s_j] lie wholly in either [L^(1/10),L^(1/5)] or
[L^(3/10),L^(2/5)]. Fix the exceptional band j_**>=j_0 after the early
geometry. Put X_A=sum A(u)Psi(u/x), H_Q=sum a_Q(v)/v and
H_P=sum_(r_*=1) W_1(r)/r.

The sieve normalizations are
V(y)=product_(p<=y)(1-1/p),
V_1(y)=product_(3<=p<=y)(1-1/(p-1)), and
mathfrak S=2 product_(p>=3)(1-1/(p-1)^2)>0.
Thus V_1(y)/V(y) tends to mathfrak S; the factor 2 accounts for the
omitted prime 2 when the sifted integer is 2u-1.

E, as specified in extraction lines 3–17 together with signed lines 3–7,
contains the elementary Section 2 estimates and Proposition 7.1 and Lemmas
7.3,7.4 at their stated strength. The exact consumed clauses are:

| Input | Required statement and uniformity |
| --- | --- |
| Lemma 2.5 | For each fixed nonnegative integer k, both sum_(n<=Y) tau(n)^k/n and Y^(-1) sum_(n<=Y) tau(n)^k are bounded by a fixed power of log(2Y). Fixed-length bounded-coefficient convolutions have the resulting square-sum bounds. |
| Lemma 2.8 | In fixed dimension, smooth functions on a fixed compact box with derivatives of order j bounded by C_j L^(C(j+1)) have Fourier absolute mass L^O(1). A frequency exponent chosen before the desired accuracy permits errors O_A(L^(-A)) for every fixed A. |
| Lemma 2.9 | Nonnegative weighted objects with bad-condition counts Xg(d)+r(d), including d=1; multiplicative g with 0<=g(p)<=1-eta_0 and bounded mass in every interval (w,w^2]. For sufficiently large even h, avoidance mass equals X product(1-g)(1+O(exp(-h)))+O(sum_(d<=z^(4h+2)) |r(d)|), uniformly in h. At h=2 there is a constant-factor upper bound. Bounding-polynomial absolute coefficients are at most one. |
| Proposition 7.1 | A(u)<=L^C tau(u_*), A(u)<=exp(C_w sqrt L) on u comparable to x, H_P asymptotic to exp(q sum V_g), and X_A comparable to x H_Q H_P/L and at least c_A x L^(-C_A). Comparison constants are independent of fixed j_**>=j_0; thresholds may depend on it. Every prime factor of a supported u belongs to [L^20,x^delta]. |
| Lemma 7.3 | The full-cell proxy is its exact test count divided by its exact W-rough count, times the rough indicator. Denominators are positive and proxies belong to [0,1]. For every fixed B, any S>2B+3 makes each actual test-minus-proxy, restricted to any interval K in a dyad of the stated factor range [x^(b_1/4),x^(1-b_1/4)], satisfy D_B uniformly. The coefficient bound is independent of S. |
| Lemma 7.4 | The prime proxy on [x^(1/2-2kappa),x^(1/2+2kappa)] is at most C/[L V(W)], with C absolute for 0<kappa<1/50. The rough proxy for a complementary exponent a in (gamma,gamma'] is at most [sup D_gamma(1-a)+o(1)]/[L V(W)]. The density is jointly continuous for w>gamma>0. Its integral and upper bound are specified below. |

The tests are I_gamma(m)=1 when P^-(m)>x^gamma and I_pr(m)=1 when m is
prime. Cells are (Y,exp(Delta_L)Y] with Delta_L=L^(-S); their defining
counts remain full-cell counts even when K cuts a cell. The rough-number
density is the finite sum

$$
D_\gamma(w)=\frac1w+
\sum_{l\ge2}\frac1{l!}
\int_{t_i\ge\gamma,\ \sum_{i<l}t_i\le w-\gamma}
\frac1{w-\sum_{i<l}t_i}\prod_{i<l}\frac{dt_i}{t_i}.
$$

At fixed small b_1 it satisfies

$$
\int_{b_1}^{1/2}D_\alpha(1-\alpha)\frac{d\alpha}{\alpha}
=D_{b_1}(1)-1,
\qquad
D_{b_1}(1)\le\frac{e^{-\gamma_E}}{b_1}(1+O(e^{-c/b_1})).
$$

The endpoint alpha=1/2 is read by a left limit and has no effect on the
integral. The density application uses N_u comparable to x, a fact verified
for the changed sign in [the extraction keeper](extraction_keeper.md).

The PNT, Mertens, Siegel–Walfisz and large-sieve statements explicitly supplied
in Section 2 are also required. They are not omitted from E's external
interface merely because the word elementary precedes that label. Their exact
forms and reading limits are recorded next. No assertion of the truth of the
complete antecedent E is part of this examination's verdict.

## Classical external interfaces and reading depth

The versions below are identified by the supplied manuscript bibliography.
The original sources were not supplied or read. “Claims checked” here means
the supplied statement was checked against its actual specialization, not
verified against an unavailable original. These statements remain explicit
assumptions of the conditional argument.

| Result and exact supplied interface | Source identification and locator | Specialization and actual depth |
| --- | --- | --- |
| PNT: pi(Y)=Li(Y)+O_A(Y/(log Y)^A), for each fixed A. | Terence Tao, *254A, notes 2: Complex-analytic multiplicative number theory*, 9 December 2014, Corollary 39 and Exercise 40, as cited in source Section 2. | Used at fixed positive powers of x, at exp(L^c), and at endpoints of logarithmic cells of fixed precision; partial summation supplies harmonic interval estimates. Supplied claims checked; original source unread. |
| Mertens: sum_(p<=Y)1/p=log log Y+O(1), and product_(p<=Y)(1-1/p) asymptotic to exp(-gamma_E)/log Y. | Terence Tao, *254A, notes 1: Elementary multiplicative number theory*, 23 November 2014, Theorems 15 and 26, as cited in (2.2). | Euler products, fixed moments, V(W), V(x^b_1), singular series and compensation bounds. Reciprocal interval limits use the stronger PNT input. Supplied claims checked; original unread. |
| Siegel–Walfisz: for fixed A,C>0, all reduced a modulo r<=log^C Y have pi(Y;r,a)=Li(Y)/phi(r)+O_(A,C)(Y/log^A Y); constants independent of Y,a,r, possibly ineffective. | The same Tao notes 2, Exercise 64; supplied Theorem 2.2. | Sum over classes for nonprincipal characters with polylogarithmic conductor, then partial summation with fixed logarithmic twist bounds. Used in Type I and proxy discrepancy. Supplied claims checked; original unread. |
| Multiplicative large sieve: for coefficients on an interval of length H, sum_(r<=R) r/phi(r) sum_primitive chi |sum a_n chi(n)|^2 << (H+1+R^2) sum |a_n|^2. | Hugh L. Montgomery and Robert C. Vaughan, *Multiplicative number theory II: Primes and sieves*, undated author-hosted draft identified in the bibliography as accessed 13 September 2026, Theorem 19.16; supplied Theorem 2.3. | Applied separately to the prime and residual dyads after coprimality restrictions and unit-modulus twists; the exact 1/R conductor weight is derived in the keeper. Supplied claims checked; original unread. |

The full Section 2 text was read. The proofs of the consumed local fixed-moment,
Fourier and block-sieve forms were examined at their displayed scope, with
their classical inputs exposed. Corollary 2.4's harmonic character estimate
is a derived interface of Siegel–Walfisz, not a new external premise. Section
2's mean-square lemma, derivative tests and rough-polynomial corollary were
read but are not load-bearing inputs to the deductions outside the assumed P/E
results; no independent certification of their unused scopes is claimed.

Kevin Ford and Heini Halberstam, *The Brun–Hooley sieve*, 2000, Section 1
Lemma 1, is credited behind the block construction. A. Buchstab, 1937,
is credited behind the density identity. Their original papers are unread.
The full local block construction and finite-simplex identity are supplied and
examined; the deductions do not import an unspecified stronger theorem from
those citations. The remaining bibliography entries are not premises merely
because they occur in the source list.

## Other source ownership and boundaries

OpenAI's *Weighted dilation graphs, smooth shifted primes and totient fibers*,
24 September 2026 release, is identified as an unrefereed manuscript.
Sections 2, 6 and 7 and the bibliography were read in the supplied
transcription in full. The signed proof and all essential source-proof
reconstructions consumed in the extraction were examined, including Type I
and the whole balanced sieve. The keepers record the actual derivations.
There is no original classical-proof reading or PDF-image comparison, and
no claim of manuscript-wide acceptance.

The successor application and final reduction are attributed to Shisheng Li
and Zhong Zhuang, *Coprime pairs with equal sum of divisors, assuming smooth
shifted primes*, 11 October 2026 draft, Theorem 1.3 and Section 3, pages 1–3.
The provided form is the full project exposition, whose counting proof has
been examined in full. The original PDF is unread, so original-source
statement and proof fidelity are not certified. Pollack and Pomerance after
Erdos is method provenance, not a separate imported premise of the explicit
counting proof. The comparison to Li–Zhuang Theorem 1.4 in the extraction is
checked for interval containment only; its original wording is unavailable.

The catalog excerpt supplies only the formulation of Problem 824. No live
catalog standing or external acceptance evidence was read or inferred.

## Native premise census

No native L-claim is consumed as an established premise by the supplied
statements, proofs or consequence sentences. The mathematical census on
15 October 2026 found none; no live ledger read was performed or authorized.
There is no prospective native grade being used as if already accepted.

The internal logical order is P/E, then signed Type II, Type I and the
successor sieve, then A+, then the squarefree-pair reduction. Each intermediate
deduction is examined in this package; no circular native promotion or
unreported established premise supplies a missing link. The assumption truth,
original-source fidelity, and eventual independent grading remain separate
from this conditional deduction review.
