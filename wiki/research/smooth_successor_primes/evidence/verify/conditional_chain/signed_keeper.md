---
name: research/smooth_successor_primes/evidence/verify/conditional_chain/signed_keeper
title: "Signed Type II keeper"
desc: Independent written reconstruction of the signed Type II implication under its explicit shift-cancellation and elementary hypotheses.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Signed Type II keeper

***

Examined on 15 October 2026. The assessed text is
[signed_type_ii.md](../../assets/conditional_chain_subject/signed_type_ii.md.txt), lines 9–481, compared
throughout with Section 6 in
[the supplied source excerpts](../../assets/conditional_chain_subject/source_sections_2_6_7.md.txt),
lines 189–386. This is a written reconstruction under P and the stated
elementary estimates, not a proof of P or an original-source fidelity check.
The source method is OpenAI's; the supplied successor exposition is Plasma
AI's, for the successor application attributed to Shisheng Li and Zhong Zhuang.

No numerical experiment is needed. Reproduction consists of checking the
identities and inequalities below against the retained definitions and the
explicit P statement. The variable called E in the splitting argument below
is a scale, distinct from the hypothesis named E.

## 1. Weight bounds and the group-part tail

Use L=log x, T=log L and W=exp(sqrt L). Group counts are distinct-prime counts,
even when the underlying integer has prime powers. Group primes are below
exp(L^d), with d<0.47, hence below W eventually. The exceptional slot is an
integer rough above W; it cannot contain a group prime.

Fixing this exceptional integer as a divisor of v leaves at most r_0!
arrangements in each band. The normalization cancels those factors, so
a_Q(v)<=tau(v). In each group, the sequence q^(t-ell)(t)_ell is bounded on
nonnegative integers t: it is zero for t<ell and exponential damping dominates
the fixed polynomial otherwise. Multiplication over O(T) groups gives
W_ell<=L^C. Slotwise reciprocal summation gives H_Q<=L^C: each pure prime slot
has bounded harmonic mass, the integer slot has O(L) mass, and there are O(T)
slots. No divisor-moment theorem with a growing number of factors is being
used here.

For theta=L^(-d), set a_p=(p^(1-theta)-1)^(-1). The inequality p^theta<=e
gives a_p<=2e/p eventually. For one group the tilted marked sum is exactly

$$
\frac1{V_g^\ell}\prod_{p\in\mathcal P_g}(1+qa_p)
\sum_{p_1,\ldots,p_\ell\ {\rm distinct,ordered}}
\prod_{i=1}^{\ell}\frac{a_{p_i}}{1+qa_{p_i}}.
$$

The factors for marked primes sum their positive powers with weight a_p; all
other present primes receive the additional factor q. This proves the identity
including prime powers and the normalization q^(-ell). Its value is bounded
in terms of the fixed group data. Taking the product over the groups and
using Rankin's inequality yields

$$
\sum_{v_*=1,\ v>x^{b_*/4}}\frac{W_\ell(v)}v
\le L^{C_1}\exp\{-b_*L^{1-d}/4\}.
$$

An integer N comparable to x has at most O(sqrt L) prime factors above W,
counted with multiplicity. Its divisors rough above W consequently number at
most exp(O(sqrt L)), since a+1<=2^a for every exponent a>=1. Multiplying
harmonic mass by O(x) bounds the discarded u_P>x^(b_*/4) contribution by

$$
xL^{C_2}\exp\{-b_*L^{1-d}/4+O(\sqrt L)\}.
$$

This beats every logarithmic loss because 1-d>1/2. It uses N=2u-1 only through
N comparable to x. It has no dependence on the later splitting precision.

## 2. The split and its costs before Cauchy's inequality

Put E=U L^(-K_0). On a good list assign u_P and the integer slot p to h.
Their product is at most x^(b_*/4+eta_*)<x^(b_*/2). Thus the pure slots still
available have total logarithm at least (1-b_*/2)L-O(1), whereas
log E<=(1-b_*)L-K_0 T. There is a positive initial margin for every fixed
K_0 once x is large. Nonempty Type II scale ranges force b_*<=1/2; larger
b_* gives a vacuous eventual assertion.

Process pure slots from the largest band down, with logarithms v_i. The
residual is R_i=log E-sum_(t<i) delta_t v_t. Taking a slot with positive
probability requires R_i>v_i and reduces both residual and remaining total
by v_i. Skipping with positive probability requires
R_i<(c_2+1)s_(j(i)). If a later band remains, its at least r_0-1 pure slots
have total logarithm at least
(r_0-1)c_1 s_(j(i))/lambda >= (c_2+1)s_(j(i)). If no later band remains,
the residual is at most (c_2+1)s_(j_x). These observations prove by a finite
induction

$$
0\le R_i\le\sum_{t\ge i}v_t+(c_2+1)s_{j_x},
\qquad E L^{-C_s}\le e\le E,\quad C_s=(c_2+1)c_+.
$$

The number of slots is explicitly finite, O(T); the induction does not assume
termination of a separate algorithm. The geometric tail also bounds
R_i/s_(j(i)) by a fixed constant. Thus the fixed compact cutoff rho can be
chosen independently of K_0. The compact transition products sum to one on
every good list and to at most one on arbitrary lists. Adding the latter back
costs only the already bounded group tail.

There is a potential dimension trap here: the number of slot variables grows.
The proof avoids it by multiplying one-dimensional Fourier norms, rather than
using the fixed-dimensional separation lemma in dimension O(T). For N_s slots,
the sum of total variations over all patterns is at most
(2C_F)^(N_s)=L^(O(1)). Truncating each input frequency at L has error at most
2^(N_s) N_s C_M C_F^(N_s-1) L^(-M). The constants in this estimate precede
K_0. The separated slot frequencies are exactly

$$
\sigma_t=-\frac{\xi_t}{s_{j(t)}}
-\delta_t\sum_{i>t}\frac{\xi_i}{s_{j(i)}}.
$$

Since sum_i 1/s_(j(i))=O(1/T), these frequencies are O(L/T). The only
remaining dependence on E in the Fourier exponent is a scalar phase, of
absolute value one.

The smooth cutoff Psi(eh/x) has a fixed one-dimensional Mellin L1 norm.
Its separation contributes common powers e^(i rho) and h^(i rho). After
separation, fixed pure-slot products have only L^(O(1)) ordered assignments:
each band contributes at most r_0! and the number of bands is O(T). Consequently

$$
|a_e(e)|\le L^{C_a},\qquad
a_h(h)=h^{i\varrho}W_\ell(h)
\sum_{pr=h_*}\mathbf1_{p\in I_{**},\ P^-(p)>W}p^{i\sigma}c_r,
\qquad |c_r|\le L^{C_a}.
$$

All of C_a and the expansion-mass exponent C_f are independent of K_0.
The identity (eh)_*=e h_* and W_ell(eh)=W_ell(h) holds because e is
group-free. The integer slot remains in h, with its complete roughness and
interval restrictions.

Uniform truncation errors are bounded against

$$
L^{O(1)}\sum_{u\asymp x}\tau(u)\tau(2u-1)\ll xL^{O(1)}.
$$

Cauchy's inequality and fixed second divisor moments prove this estimate;
2u-1 is an injective selection of positive integers of size O(x). Removing
the compact Psi support during separation does not create an unbounded size
range: m and n remain on their original dyads and force u comparable to x.
Taking the Fourier accuracy large enough therefore gives the stated B_0
expansion with error O(x L^(-D_*-1)).

## 3. Cauchy, the diagonal, and the order of K_0

The smooth majorants of e and n equal one on their original ranges. Applying
Cauchy's inequality in those two variables gives

$$
|B_0|^2\le EVL^{C_3}\mathcal N.
$$

The outside factor follows from the number of e,n pairs and the bounds on
a_e and beta. Enlarging the range in the nonnegative square norm is legitimate.
Only the lower edge of the e cutoff moves by L^(-C_s); its derivative cost
depends on C_s, not K_0.

On the diagonal m=m', the equations force h=h'. For fixed m,n, e divides
(mn+1)/2, and

$$
\sum_{e\mid(mn+1)/2}\tau((mn+1)/(2e))^2\le\tau(mn+1)^3.
$$

There are at most tau(v) pairs m,n with mn=v. Cauchy's inequality and the
second and sixth fixed divisor moments therefore give

$$
\mathcal N_{\rm diag}
\ll L^{O(1)}\sum_{v\ll x}\tau(v)\tau(v+1)^3
\ll xL^{C_5}.
$$

No estimate for a shifted divisor correlation is assumed. Ordinary unshifted
moments suffice. Because EV is comparable to xL^(-K_0), choosing
K_0>=C_3+C_5+2C_f+2D_*+2 controls this contribution even after multiplying
the square root by the whole pre-Cauchy Fourier mass. The quantities on the
right have already been fixed.

## 4. The signed bijection

Suppose

$$
mn=2eh-1,\qquad m'n=2eh'-1,\qquad m\ne m'.
$$

The first congruence implies gcd(n,2e)=1. Subtraction then gives
2e dividing m'-m. Define k=(m-m')/(2e). Direct calculation gives

$$
m'-m=-2ek,\qquad h'-h=-kn,\qquad mh'-m'h=k.
$$

Thus z=m'h and z+k=mh' are both positive. The enlarged e range gives
0<|k|=O(L^(K_0+C_s)); eventually |k|<W.

Conversely, suppose m,m',h,h' are positive, m and m' are rough above W,
0<|k|<W, m'h=z, mh'=z+k, and m'=m modulo 2|k|. If
e=(m-m')/(2k)>0, then e is an integer and

$$
m(h'-h)=-k(2eh-1).
$$

Every prime factor of m exceeds |k|, so gcd(m,k)=1, including the case m=1.
It follows that n=(2eh-1)/m is a positive integer. Substitution recovers
h'-h=-kn and m'n=2eh'-1. All variables of the original pair are recovered
uniquely. This proves the converse, including divisibility and positivity;
it does not merely count a superset.

Both m and m' are odd and coprime to k. Therefore they are units modulo
q_k=2|k|, and all Dirichlet characters modulo q_k impose the congruence exactly:

$$
\mathbf1_{m'=m\ ({\rm mod}\ q_k)}
=\frac1{\varphi(q_k)}\sum_{\chi\bmod q_k}
\chi(m)\overline{\chi(m')}.
$$

The pulled-back cutoff arguments are e=(m-m')/(2k) and

$$
n=\frac{(m-m')z}{kmm'}-\frac1m.
$$

The sign of the last term is essential. The two possible signs of k are both
retained. Extending the smooth cutoffs by zero to nonpositive arguments imposes
the original positivity conditions; it changes no arithmetic restriction.

## 5. Separation, conjugations, and P's normalization

The support gives z comparable to x times a fixed logarithmic power. There
are O(T) dyads Z needed. In t_1=log(m/U), t_2=log(m'/U), t_3=log(z/Z),
the derivatives of e/E are O(U/(|k|E)), and those of n/V are
O(Z/(|k|UV)+(UV)^(-1)). Both are fixed powers of L after K_0 is chosen.
Fixed smooth localizations give a compact three-dimensional box. The
fixed-dimensional Fourier lemma now applies legitimately, with polynomial
total variation and a frequency exponent fixed before the desired tail saving.

Absolute endpoint convolutions have bound L^(O(1)) tau(z_*)^2; with W_ell,
their square sum on a Z dyad is O(Z L^(O(1))). The fourth divisor moment
proves this. Cauchy's inequality at z and z+k bounds the absolute correlation
by Z L^(O(1)); |k| is negligible relative to Z. This controls tails after
all polynomially many shifts and character terms. No cancellation is used to
justify the Fourier truncation itself.

For fixed chi and separated frequencies xi_1,xi_2,xi_3, define

$$
F_0(v)=\sum_{mpr=v_*}\alpha_m\chi(m)m^{i(\varrho-\xi_2)}
\mathbf1_{p\in I_{**},\ P^-(p)>W}p^{-i\sigma}\overline{c_r},
$$

$$
G_0(v)=\sum_{mpr=v_*}\alpha_m\chi(m)m^{i(\xi_1+\varrho)}
\mathbf1_{p\in I_{**},\ P^-(p)>W}p^{-i\sigma}\overline{c_r}.
$$

Conjugating F_0 at z=m'h gives exactly the factors involving conjugate
alpha_(m'), conjugate chi(m'), p^(i sigma)c_r and
(m')^(i xi_2-i varrho). Multiplying by z^(i varrho) restores h^(i varrho).
At z+k=mh', G_0 and (z+k)^(-i varrho) give the other factor
alpha_m chi(m) m^(i xi_1) conjugate(a_h(h')) after its group weight is
restored. Since m,m' are group-free,
z_*=m'h_*, (z+k)_*=mh'_*, W_ell(z)=W_ell(h), and
W_ell(z+k)=W_ell(h'). The separated correlation is consequently

$$
\sum_z\psi_Z(z/Z)z^{i(\varrho+\xi_3)}(z+k)^{-i\varrho}
\overline{F_0(z)}G_0(z+k)W_\ell(z)W_\ell(z+k).
$$

The same original alpha with its actual m restrictions is inside F_0.
Character and power twists are explicit parts of the allowed endpoint, not
a replacement sequence on which discrepancy is being assumed without proof.
Its modulus is 2|k|, its frequencies and coefficients have fixed logarithmic
power bounds, and 0<tau_*<eta_*<b_*/4<=1/8<1/4. The integer slot and the
unrestricted residual coefficient meet P exactly.

With tilde_psi(t)=t psi_Z(t), the displayed unweighted sum is Z times P's
harmonically normalized sum: Z tilde_psi(z/Z)/z=psi_Z(z/Z). P applies to
both signs of k and the actual conjugation. It supplies O(Z L^(-D_0)).
Summing the shifts, dyads, averaged characters and Fourier variation gives
O(x L^(-D_0+C_9)) for the off-diagonal norm. The total character weight at
each k is one; even polynomial overestimates are absorbed in C_9.

Choose positive D_0 at least C_3+C_9-K_0+2C_f+2D_*+2, then choose the
discrepancy exponent B supplied by P. The diagonal and off-diagonal estimates
give |B_0|=O(x L^(-D_*-C_f-1)). Integrating the pre-Cauchy expansion and
adding its errors proves the signed Type II estimate at the claimed strength.

## Result of the attacks

The finite allocation, the two signs, the determinant converse, the character
units, the conjugations, the integer slot, the arbitrary beta sequence and
the factor Z all survive the checks above. The order of choices is acyclic:
fixed geometry and requested saving; K_0; post-Cauchy separation bounds and
D_0; B; then any proxy precision whose coefficient bound is independent of
that precision. No extra analytic hypothesis beyond the stated P/E interfaces
was found in this deduction. This finding supplies no proof of P.
