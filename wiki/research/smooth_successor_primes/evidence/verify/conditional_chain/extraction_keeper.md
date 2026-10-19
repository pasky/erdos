---
name: research/smooth_successor_primes/evidence/verify/conditional_chain/extraction_keeper
title: "Successor extraction keeper"
desc: Independent reconstruction of the successor extraction, its balanced sieve, and the failure of an unrestricted reading of its dyadic bound.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Successor extraction keeper

***

Examined on 15 October 2026. Inputs are the complete
[successor extraction](../../assets/conditional_chain_subject/extraction.md.txt), the
[signed Type II text](../../assets/conditional_chain_subject/signed_type_ii.md.txt), and Sections 2 and 7
of [the supplied source excerpts](../../assets/conditional_chain_subject/source_sections_2_6_7.md.txt).
The weighted-dilation method is OpenAI's; the successor application is
attributed to Shisheng Li and Zhong Zhuang, and the project exposition and
parameter checks to Plasma AI. This keeper checks deductions under P and E.
It neither establishes those antecedents unconditionally nor certifies the
transcription against a PDF.

No computation is used. All claimed checks are reproducible from the retained
formulas, the classical statements explicitly included in E, and the derivations
below. The balanced specialization and the unrestricted reading of the dyadic
display have different findings and are treated separately.

## 1. Candidate geometry and the E interfaces

The choices q=1/2, ell=1, lambda=2, c_1=1, c_2=6/5, c_3=3/2,
c_4=9/5 and s'=1/[r_0(c_1+c_2)] meet the signed theorem's conditions.
The inequalities c_2<c_3<c_4<2c_1 separate groups from all adjacent bands.
There are (1/10)T/log 2+O(1) groups of each kind: the conditions placing
[c_3s_j,c_4s_j] inside each prescribed logarithmic range determine an interval
of indices of that length. PNT and partial summation give their harmonic masses
log(c_4/c_3)+o(1), uniformly over these ranges. Thus positive fixed lower and
upper mass bounds are available. The smallest band primes are at least L^20,
and all group primes are below W eventually.

Proposition 7.1 is an E premise. Its candidate depends on u, not the sign of
2u±1. In particular, all supported prime factors of u are between L^20 and
x^delta, X_A is comparable to x H_Q H_P/L and at least c_A x L^(-C_A), and
the pointwise weight on u comparable to x is at most exp(C_w sqrt L).
The comparability constants are independent of fixed j_**>=j_0; thresholds
may depend on that fixed index. This distinction is needed later.

The supplied proof also contains an exact inequality used outside the formal
statement of that proposition. It follows directly from the definitions.
For one group let F_g(q)=product_(p in group)(1+q/(p-1)). Its contribution to
H_P is

$$
\frac{F'_g(q)}{V_g}
=F_g(q)\frac1{V_g}\sum_{p\in\mathcal P_g}\frac1{p-1+q}
\ge F_g(q).
$$

The last inequality uses q<1 and V_g=sum 1/p. Consequently

$$
H_P\ge\prod_{p\ {\rm group\ prime}}(1+q/(p-1))\ge1.
$$

This verifies the precise (7.6) input rather than silently adding it as a new
premise. Prime powers are included by the geometric series 1/(p-1).

For clarity, the candidate proof's uniformity is consistent with its use.
The total midpoint logarithm of the infinite pure-slot model is L. A fixed
prefix can make the entire remaining range smaller than a fixed fraction of
the free band-0 slot's logarithmic width. Restricting the other prefix slots
near their midpoints costs a fixed positive harmonic probability. Keeping the
group part's logarithm below another fixed fraction costs o(1), by its tilted
Euler-product tail. The free pure slot can then place the product in a fixed
positivity interval of Psi with probability comparable to 1/L. The exceptional
slot lies beyond this prefix and is controlled by its range alone. Hence the
comparison constant does not need to depend on which later fixed j_** is used.
This explains why the E hypothesis has the uniformity actually consumed.

## 2. Type I is a deduction, not an additional assumption

For odd squarefree d, the congruence d dividing 2u-1 forces gcd(u,d)=1 and
u=2^(-1) modulo d. Character orthogonality has the unit scalar
conjugate(chi(2^(-1))). It therefore differs from the predecessor case only
by a scalar of absolute value one after the principal character is separated.

For a supported u, its distinct prime factors are at least L^20 and number
O(L/T). The error in replacing the principal coprime mass by X_A is at most

$$
X_A\max_u\sum_{l\mid u}\frac1{l-1}
\sum_{d'\le x}\frac{\mu^2(d')}{\varphi(d')}
\ll X_A L^{-18}.
$$

The second sum is O(L), by its Euler-product upper bound and Mertens.
The first is O(L^(-19)/T). This accounts for the coprimality exceptional set;
it is not discarded.

Because j_**>=1, band 0 has a pure slot. Fixing one labelled slot writes
A(u)=sum_(pr=u,p in Q_0) b(r), with b(r)>=0 and
b(r)<=L^C tau(r). The fixed slot is group-free, so it does not change W_1.
Every contributing dyad has PU comparable to x and both P,U between
constant multiples of x^a and x^(1-a), for a fixed a>0.

A nonprincipal character modulo squarefree d is induced from a primitive
nonprincipal character of conductor f>1. Write d=hf, with gcd(h,f)=1.
The extra restrictions are gcd(p,h)=gcd(r,h)=1. For fixed h, Mellin separation
of Psi(pr/x) preserves coefficient square sums O(P) and U L^C. Applying the
multiplicative large sieve in a conductor dyad f comparable to R gives

$$
\begin{aligned}
&\sum_{f\asymp R}\frac1{\varphi(f)}\sum_{\chi\bmod f}^{*}
 |P(\chi)|\,|Q(\chi)|\\
&\quad\ll\frac{L^C}{R}
 \sqrt{(P+R^2)(U+R^2)PU}\\
&\quad\ll xL^C\left(R^{-1}+P^{-1/2}+U^{-1/2}+R/\sqrt x\right).
\end{aligned}
$$

For R>L^(C'), the first term saves the required logarithmic power when C'
is large; the others save a fixed power of x because R<=x^vartheta and
vartheta<1/2. The dyadic sums and sum over squarefree h with weight 1/phi(h)
cost only logarithmic powers. Restrictions on f can be discarded in this
positive upper bound.

For 1<f<=2L^(C'), use Siegel–Walfisz on the p sum with the original smooth
cutoff. Summing characters over reduced residue classes and partial summation
give arbitrary logarithmic saving. There are O(1) primes in the p range
dividing h: each is at least x^a while h<=x^vartheta. Removing them costs
O(U L^C) for each fixed set of outer data, hence x^(1-a)L^C after all
logarithmic costs. The result is exactly

$$
\sum_{d\le x^\vartheta,\ d\ {\rm odd,squarefree}}|r(d)|
\ll xL^{-D}+X_A L^{-18}
$$

for every fixed vartheta<1/2 and D>0. No additional distribution theorem or
uniformity in a varying positive power a is required.

## 3. The elementary sieve and local proxy interfaces

The block sieve's coefficient bound is important: Type I controls an unweighted
sum of absolute remainders. Its proof really has coefficients at most one.
In block j, even h_j=(j+1)h gives a nonnegative inclusion–exclusion upper
polynomial U_j, and U_j-I_j<=E_j, where E_j has degree h_j+1. The product
upper bound U and each one-block correction have disjoint monomial supports:
the distinguished block has degree h_j+1 only in that correction. Thus U,
V=U-sum_j E_j product_(k!=j) U_k, and U-V have absolute coefficients at
most one. Their product indices are at most z^(4h+2), since
sum_(j>=0) h(j+1)2^(-j)=4h and a correction adds at most one.

In the independent model, each block avoidance probability is at least
exp(-C/eta_0), while its correction expectation is at most
C^(h_j+1)/(h_j+1)!. The sum of their ratios is O(exp(-h)) for large even h,
and bounded for h=2. Product expectations give the stated relative error or
the h=2 upper bound. Evaluating the polynomials in the actual weighted problem
adds only sum |r(d)|. The independent probabilities are a device for evaluating
known multiplicative main terms; they are not a probabilistic heuristic about
the integers.

Apply this first to odd primes up to x^b_1, with g(p)=1/(p-1). Here g(3)=1/2,
all densities are bounded away from one, and their mass in each logarithmic
block is bounded. With h=2 floor(1/(40b_1)), the level exponent is at most
1/5+2b_1, below vartheta=1/2-kappa/2 for sufficiently small b_1. Taking
D>C_A+10 makes the Type I error o(X_A/L). The preliminary mass is therefore

$$
\frac{\mathfrak S X_A}{L}
\left\{\frac{e^{-\gamma_E}}{b_1}
 (1-O(e^{-c/b_1}))+o(1)\right\}.
$$

The omission of the prime 2 is necessary and justified: 2u-1 is odd. The
singular-series normalization follows from

$$
\frac{1-1/(p-1)}{1-1/p}=1-\frac1{(p-1)^2}\quad(p\ge3),
\qquad V_1(y)/V(y)\longrightarrow\mathfrak S.
$$

Lemma 7.3 is assumed as E, with its full interval and character uniformity.
The supplied proof confirms the relevant interface: use full-cell counts,
then impose the range restriction K. Denominators are positive because their
main term is Delta_L Y V(W), whereas the sieve level is
D_W=exp(O(sqrt L T^2))=x^(o(1)) and Y is a fixed positive power of x.
Both tests are subsets of the rough integers, so the coefficient bound one
does not depend on S.

For a principal character, every supported m is coprime to its polylogarithmic
modulus. Full-cell unweighted cancellation, followed by the variation of
m^(it-1), costs O(L^(B-S)). The at most two cut cells cost
O(L^(-S)+x^(-b_1/4)). For nonprincipal characters, the actual rough test can
be enumerated by its unique nondecreasing list of at most O(1/b_1) prime
factors. Fixing all but the last leaves one prime interval and a bounded
reciprocal mass for the preceding factors. Siegel–Walfisz gives the needed
absolute harmonic error, including short intervals and imprimitive characters.
For the proxy, CRT and the sieve in each reduced residue class give the common
main term |J'|V(W)/phi(r), which cancels. The remaining errors are
exp(-T^2) times logarithmic powers and x^(-b_1/4+o(1)) times logarithmic
powers. Thus the stated D_B condition uses actual interval restrictions, and
S>2B+3 leaves room for the required bound with constant one.

The sign transfer for Lemma 7.4 needs more than changing a label N_u. Its
short-cell rough-number estimate is about ordinary integers: with
w=log Y/L, it is

$$
\#\{m\in(Y,e^{\Delta_L}Y]:P^-(m)>x^\gamma\}
\le (D_\gamma(w)+o(1))\frac{\Delta_LY}{L}.
$$

Repeated prime factors cost at most O(Y x^(-b_1)), negligible here.
For the squarefree part, ordered l-prime lists with weight 1/l! reduce the
last prime count by PNT to the integral defining D_gamma. All denominators
are bounded away from zero on the fixed compact region, and boundary strips
of the moving simplex have uniformly vanishing volume. Finite grid
approximation justifies the uniform passage from reciprocal prime measures
to dt/t. The prime proxy is the one-prime version. Division by the same rough
cell count gives the two proxy estimates.

For both 2u+1 and 2u-1 on this support, log N_u/L=1+O(1/L). If the selected
factor has exponent a in (gamma,gamma'], the other cell has
w=1-a+o(1). The gap w-gamma>=2kappa+o(1) keeps it in the required compact
region. Joint continuity therefore supplies the same (7.17) bound for the
successor case. No distribution assertion about N_u is hidden in this step.

The density identity can be checked directly on the finite simplices. For
each l>=2, the symmetric measure is
(1/l!) dt_1 ... dt_(l-1)/(t_1 ... t_l), with sum t_i=1 and t_i>=b_1.
Except on a null set it has a unique minimum alpha. Choosing its coordinate
in l ways changes the coefficient to 1/(l-1)!, and the remaining density is
D_alpha(1-alpha). Hence its integral is D_b1(1)-1; the removed one-prime
term is exactly 1. The elementary sieve upper bound for ordinary rough
integers, compared with their lower density from ordered prime lists, gives
D_b1(1)<=exp(-gamma_E)/b_1 times 1+O(exp(-c/b_1)). These are the exact E
interfaces needed; none concerns a density of shifted primes.

## 4. Removing composites away from balance

Every preliminary-sieve composite with least prime p in (x^gamma,x^gamma']
has cofactor rough above x^gamma. Repeated least primes cause no exception.
Both factors lie in the Type II range with b_*=b_1/3, with exponent slack
absorbing the fixed constants in N_u comparable to x. The signed theorem
applies to alpha=I_gamma-B_gamma with its actual dyadic and interval cuts,
and to the arbitrary bounded prime-bin coefficient on the other factor.
There are only a fixed number of bins and a logarithmic number of dyads, so
choosing D_* sufficiently large gives total replacement error o(X_A/L).

The resulting rough-cofactor condition is equivalent to roughness of N_u
above W because p>W. For each p, the small-prime sieve has base mass
X_A/(p-1), densities 1/(l-1), and remainders r(pd), including d=1.
With h=2 ceil(T^2), all products pd are below
x^(1/2-kappa+o(1))<x^(1/2-kappa/2). Distinct pairs (p,d) give distinct
products, since p is their unique prime factor exceeding W. Thus the summed
Type I remainders incur no multiplicity loss. The result is

$$
X_A V_1(W)\sum_{x^\gamma<p\le x^{\gamma'}}\frac1{p-1}
+o(X_A V(W)).
$$

PNT and partial summation give the reciprocal sum tending to
log(gamma'/gamma). Multiplying by the rough proxy bound gives the bin's
displayed coefficient. The stronger interval limit is obtained from PNT, not
from subtracting two unspecified O(1) errors in a weak Mertens formula.

Joint continuity permits the finite upper mesh sum to approach
the integral of D_alpha(1-alpha)/alpha on [b_1,1/2-kappa]. Enlarging to
1/2 only increases this nonnegative integral. The exact density identity and
bound in E leave

$$
\frac{\mathfrak S X_A}{L}
\{1-1/10-O(b_1^{-1}e^{-c/b_1})+o(1)\}
\ge\frac{\mathfrak S X_A}{2L}.
$$

Its support is primes together with composites whose least prime exceeds
x^(1/2-kappa). The bins are open on their lower and closed on their upper
endpoints, matching the strict preliminary roughness and the remaining
strict lower bound. No exceptional boundary primes disappear.

## 5. The balanced estimate at the scope actually used

A remaining composite has exactly two prime factors counted with multiplicity:
three would make it exceed a fixed multiple of x because
3(1/2-kappa)>1. Both factors belong eventually to
[x^(1/2-2kappa),x^(1/2+2kappa)]. Squares are included; ordering the factors
only overcounts. Two successive Type II replacements are legitimate: in the
second, the first proxy is an arbitrary coefficient bounded by one. Their
product is bounded by C/[L^2 V(W)^2] times the two roughness indicators,
with C independent of 0<kappa<1/50.

Here and throughout this subsection, the dyads meet this balanced range.
In particular M_i=O(x^0.54), and M_1 M_2 is comparable to x. These size
conditions are necessary for the lattice-error argument.

Choose j' and theta before kappa so that the micro bands' total upper
logarithmic size is at most L/25, 10theta<=1/20, and theta lies between
the top micro band and the bottom omitted macro band. Put the exceptional
slot in the micro bands by requiring j_**>=j_0>=j'. An assignment contains
all ordered micro slots and one marked prime from each group. Its product
D_1 includes multiplicities and the entire exceptional integer, so it need
not be squarefree. Nevertheless

$$
D_1\le x^{1/20},\qquad
\sum_{\rm assignments}\frac\lambda{D_1}=H_Q^{\rm mic},\qquad
\sum_{\rm assignments}\lambda\le x^{1/20}H_Q^{\rm mic}.
$$

The first bound uses the deterministic micro product and the group-mark
product exp(O(T L^(2/5)))=x^(o(1)). Each normalized mark has reciprocal mass
one, proving the second identity. Omitting finitely many fixed pure macro
bands gives H_Q^mic<=C H_Q with C independent of j_**.

For a fixed genuine assignment dividing u, all nongroup prime factors of u
below x^theta are in D_1. This includes prime factors of the exceptional
integer that are not band primes. There is exactly one distinct group mark
per group. Independently allowing each unmarked group prime with probability
q therefore gives expectation q^(omega(u)-s), exactly the damping in W_1.
For fixed residual product, the normalized number of macro lists is a product
of reciprocal multiplicity factorials, at most one. Discarding their
restrictions proves the stated pointwise mask majorant. The argument neither
assumes squarefree u nor confuses a distinct-prime count with multiplicity.

Fix a mask and assignment. D_1 is odd. The congruence for the successor is
mn=-1 modulo D_1. Dropping parity enlarges the original set. For an odd
prime l not dividing D_1, the roughness failure mn=0 has 2l-1 residue
pairs, while a banned prime's failure mn=-1 has l-1 residue pairs. The two
sets are disjoint. Thus

$$
g(l)=\frac{(2l-1)\mathbf1_{l\le W}+(l-1)\mathbf1_{l\ {\rm banned}}}{l^2}
\le\frac3l.
$$

The largest possible value at l=3 is 7/9, so the densities are uniformly
bounded away from one. Their logarithmic-block sums are uniformly bounded.

There are exactly phi(D_1) solutions to mn=-1 modulo D_1, even with prime
powers in D_1: choose any unit m, then n is forced. CRT gives
phi(D_1)nu(d) classes modulo D_1d for a squarefree sieve product d coprime
to D_1. Each class has box count equal to its area term plus
O(1+(M_1+M_2)/(D_1d)). Since nu(d)<=d 3^omega(d), the total remainder to
D=x^(10theta) is at most

$$
L^C\{(M_1+M_2)D+D_1D^2\}.
$$

The h=2 block-sieve upper bound has exactly this level. After summing with
assignment weights, the error is at most
x^0.64 L^C H_Q^mic: the larger term is x^0.54 x^0.05 x^0.05, while the
other is at most x^0.20. This is o(X_A V(W)^2), because
X_A V(W)^2 is comparable to x H_Q H_P/L^2, H_Q^mic<=C H_Q and H_P>=1.

For a banned l<=W the sieve factor is (1-1/l)(1-2/l). Above W it is
1-1/l+1/l^2. An allowed group prime contributes (1-1/l)^2. Comparing these
with V(W)^2 V(x^theta), including the harmless omitted prime 2, gives

$$
C V(W)^2 V(x^\theta)
\prod_{l\mid D_1}(1-1/l)^{-3}
\prod_{p\ {\rm allowed},\ p\nmid D_1}(1-1/p)^{-1}.
$$

The convergent O(l^(-2)) product costs an absolute constant. Every prime
dividing D_1 is at least L^20, and D_1<=x^(1/20), so the first compensation
product is uniformly bounded. The mask expectation of the second is
product_(group p not dividing D_1)(1+q/(p-1))<=H_P, by the independently
derived inequality in subsection 1.

Summing main terms uses phi(D_1)/D_1^2<=1/D_1 and gives

$$
xV(W)^2 V(x^\theta)H_Q^{\rm mic}H_P
\ll X_A V(W)^2.
$$

The implied constant depends only on early geometry and theta, not on kappa,
b_1, j_**, S or later analytic precisions. This proves the required balanced
dyadic estimate. There are O(kappa L+1) possible m dyads, and O(1) n dyads
for each because mn is comparable to x. After the proxy prefactor, their
total is C_bal(kappa+L^(-1))X_A/L+o(X_A/L), with C_bal fixed before kappa.

## 6. Exact witness against the unrestricted dyadic reading

The separate display headed “Dyadic bound” in extraction lines 256–266
mentions only M_1 M_2 comparable to x. Read without the surrounding balanced
restriction, that statement is false. The following is a written asymptotic
witness under the same E inputs; it uses neither P nor a finite experiment.

Take x=2^j tending to infinity, the dyad m in [1,2), and the dyad
n in [2x,4x). Thus m=1 and P^-(m)=infinity. Smoothness and support of Psi
in [1,2] imply Psi(1)=Psi(2)=0. Every nonzero candidate summand therefore
has integer x<u<2x and 2x<=2u-1<4x. Consequently the left side of the
unrestricted dyadic display is exactly

$$
S_W=\sum_{P^-(2u-1)>W}A(u)\Psi(u/x).
$$

Apply the block sieve with odd prime densities 1/(p-1), cutoff W and
h=2 ceil(T^2). Its level is x^(o(1)), hence below any fixed positive
Type I level less than x^(1/2). Type I with D>C_A+10 gives

$$
S_W=X_A V_1(W)(1+O(e^{-h}))
+O(xL^{-D}+X_A L^{-18})
\sim\mathfrak S X_A V(W).
$$

Because V(W) is asymptotic to exp(-gamma_E)/sqrt L,

$$
\frac{S_W}{X_A V(W)^2}
\sim\mathfrak S e^{\gamma_E}\sqrt L\longrightarrow\infty.
$$

No fixed implied constant can give the unrestricted bound. The witness has
M_1M_2=2x, so it satisfies the product-size condition written in that display.
It violates the balanced size restriction and therefore does not refute the
bound proved in subsection 5 or its actual use on balanced composites.
The proof's explicit use of M_i<<x^0.54 supplies that distinction. This
keeper accepts only the balanced specialization; it does not silently repair
or accept the unrestricted reading. Any use of the display for arbitrary
dyads would require a different statement or argument.

The reusable failure mode is that a two-variable sifted estimate can lose one
of its two roughness factors when one variable degenerates to 1. A product
size restriction alone does not preserve the uniform lattice-error estimate.

## 7. Closing the choices and obtaining A+

Fix delta and the candidate geometry, the candidate prefix, j',theta and j_0
first. The preceding balanced proof then fixes C_bal independently of the
later parameters. Choose 0<kappa<1/50 with C_bal kappa<mathfrak S/4.
Next choose b_1 small enough for the preliminary sieve and density subtraction,
put b_*=b_1/3, choose a fixed sufficiently late j_**, and choose the finite
mesh. Choose the required Type II accuracy to absorb dyadic sums. Its proof
chooses K_0, then its Fourier costs and D_0, then B. Finally take S>2B+3
and the required PNT accuracies. There is no return dependence of a coefficient
bound on S. All these constants precede x tending to infinity.

Subtracting the balanced upper bound from the surviving mass gives eventually

$$
\sum_{2u-1\ {\rm prime}}A(u)\Psi(u/x)
\ge\frac{\mathfrak S X_A}{5L}.
$$

The maximum summand is at most exp(C_w sqrt L), after absorbing the fixed
bound on Psi. The map u to 2u-1 is injective. Thus the number of distinct
primes in [2x-1,4x-1] with P^+(p+1)<=x^delta is at least

$$
c x L^{-C_A-1}\exp(-C_w\sqrt L).
$$

The factor 2 in p+1=2u is at most x^delta eventually. For each fixed eta>0,
the logarithm of this lower bound divided by x^(1-eta) is
eta L-(C_A+1)log L-C_w sqrt L+log c, which tends to positive infinity.
Setting x=y proves A+ for every sufficiently large real y and each fixed
delta,eta. It does not prove a uniform threshold as delta tends to zero.
The interval is contained in (2x-2,5x], as the final range-comparison sentence
states; the original Li–Zhuang Theorem 1.4 itself was not supplied for fidelity
inspection and is not a premise of this calculation.

All uses needed for this extraction, including the complete balanced sieve,
are covered above. No additional analytic premise beyond the stipulated P/E
interfaces was found. The unrestricted auxiliary wording remains qualified
by the explicit witness in subsection 6.
