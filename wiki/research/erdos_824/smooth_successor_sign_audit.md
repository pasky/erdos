---
name: research/erdos_824/smooth_successor_sign_audit
title: The smooth-successor count from the weighted-dilation argument
desc: |
  Every place where the sign of 2u+1 enters the weighted-dilation
  manuscript's proof of its smooth-predecessor count, with the identity,
  divisor bound, unit class, residue count or range that replaces it for
  primes 2u-1; the sign-free steps remain the manuscript's unrefereed
  argument.
created: 2026-10-15T04:45:32Z
updated: 2026-10-15T04:45:32Z
---

***

This page checks the sign change behind Theorem 1.4 of Li and Zhuang's draft
(the version of 11 October 2026 recorded on
[[problems/arithmetic_functions/E0824/claims/2026_10_07_li_zhuang|their claim page]]):
the argument by which the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]]
proves its
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/theorem_1_2|Theorem 1.2]],
the count of primes $p$ with $P^+(p-1)\le x^\delta$, is rerun for primes
$N_u=2u-1$ in place of $N_u=2u+1$. The observation and the outline of the
change are Li and Zhuang's; the check below is Plasma AI's, author-recorded
and unreviewed. It is a check of every step at which the sign enters, read in
the library's transcription of Sections 2–7 of the manuscript. The steps that
do not involve the sign are used as the manuscript writes them; they, and
Sections 3–5, are premises of this sign audit. The
[[research/smooth_successor_primes/_index|complete conditional derivation]]
writes out the Type II and sieve arguments and separately examines the
analytic core at author standing. Its uniform premises (P) and (E) remain
unrefereed inputs.

## The claimed conclusion

**Conditional count.** Assume that the manuscript's argument for its
Theorem 1.2 is correct in every step that does not involve the form $2u+1$:
the results of its Section 2, Theorem 5.1 (with Sections 3 and 4 behind
it), Proposition 7.1, Lemmas 7.3 and 7.4, and the sign-free steps of the
proofs of Theorem 6.1 and of Section 7. Then for every fixed
$0<\delta<1/4$, as $x\to\infty$ through real values,

$$
\#\{p\text{ prime}:\ 2x-1\le p\le4x-1,\ P^+(p+1)\le x^\delta\}
\ge x^{1-o(1)}.                                                \tag{1}
$$

In particular Hypothesis $\mathrm A^+$ holds: for $0<\delta<1/4$ and
$\eta>0$, (1) at $x=y$ gives at least $y^{1-o(1)}\ge y^{1-\eta}$ primes
$p\le5y$ with $P^+(p+1)\le y^\delta$ for all large real $y$. The range in
(1) lies inside the range $2x-2<p\le5x$ of Li and Zhuang's Theorem 1.4.

The manuscript fixes the notation used below: $L=\log x$, $W=\exp(\sqrt L)$,
the weight $A(u)=a_Q(u_*)W_\ell(u)$ on integers $u$ (its (6.3) and the
Section 7 choices $q=1/2$, $\ell=1$), whose definition involves only $u$,
the smooth cutoff $\Psi(u/x)$ with $\Psi$ supported in a fixed compact
subinterval of $(0,\infty)$ (in Section 7, inside $[1,2]$), and the mass
$X_A=\sum_uA(u)\Psi(u/x)$. The sign enters only through $N_u$.

## The Type II estimate

The changed statement is Theorem 6.1 with $mn=2u-1$ in place of $mn=2u+1$
in its display (6.5), with the same hypotheses and constants. Its proof
changes at the following places and nowhere else.

**Large group-prime factor.** The bound $\exp(O(\sqrt L))$ for the number of
divisors $m$ of $N_u$ all of whose prime factors exceed $W$ uses only
$N_u\ll x$, which holds on the support of $\Psi(u/x)$: such an integer has
$O(L/\log W)=O(\sqrt L)$ prime factors above $W$, counted with
multiplicity. It holds for $2u-1$.

**Absolute control.** The bound (6.10) becomes
$\sum_{u\asymp x}\tau(u)\tau(2u-1)\ll xL^{O(1)}$, by Cauchy's inequality and
the fixed divisor moments of the manuscript's Lemma 2.5 applied to $u$ and to
the odd integers $2u-1\ll x$.

**The diagonal.** For $m=m'$ the two equations $mn=2eh-1=2eh'-1$ force
$h=h'$. For fixed $m,n$ the admissible $e$ divide $(mn+1)/2$, and

$$
\sum_{e\mid(mn+1)/2}\tau\Bigl(\frac{mn+1}{2e}\Bigr)^2\le\tau(mn+1)^3,
$$

since each term is at most $\tau(mn+1)^2$ and there are at most
$\tau(mn+1)$ terms. Collecting by $v=mn$ gives

$$
\mathcal N_{\rm diag}\ll L^{O(1)}\sum_{v\asymp x}\tau(v)\tau(v+1)^3
\ll xL^{C_5},
$$

again by Cauchy's inequality and Lemma 2.5. The exponent is independent of
the splitting parameter $K_0$, as in the manuscript.

**The determinant identity.** Take an off-diagonal pair

$$
mn=2eh-1,\qquad m'n=2eh'-1,\qquad m\ne m'.                    \tag{2}
$$

The first equation gives $mn\equiv-1\pmod{2e}$, so $n$ is a unit modulo
$2e$. Subtracting, $(m'-m)n=2e(h'-h)$, hence $2e\mid m'-m$. Write
$m'-m=-2ek$ with an integer $k\ne0$. Then $h'-h=-kn$, and

$$
mh'-m'h=m(h-kn)-(m-2ek)h=-k(mn-2eh)=k.
$$

So the cross products are again $z=m'h$ and $z+k=mh'$, with the shift $k$
of the opposite sign to the manuscript's choice; Theorem 5.1 allows every
integral $0<|k|\le L^C$. The size bound $0<|k|\ll L^{K_0+C_s}$ of (6.17)
follows from $|m'-m|\ll U$ and $e\gg EL^{-C_s}=UL^{-K_0-C_s}$.

**The converse.** Fix an integer $k\ne0$, positive integers $m,m',h,h'$ with
$P^-(m),P^-(m')>W$, $m'h=z$ and $mh'=z+k$, and suppose $m'\equiv
m\pmod{2|k|}$ and $e=(m-m')/(2k)>0$. Then $e$ is an integer, and

$$
m(h'-h)=k+(m'-m)h=k-2ekh=-k(2eh-1).
$$

Every prime factor of $m$ exceeds $W$, while $|k|\le L^{O(1)}<W$ for large
$x$, so $(m,k)=1$ and $m\mid2eh-1$. Put $n=(2eh-1)/m$, a positive integer.
Then $h'-h=-kn$ and
$m'n=mn-2ekn=2eh-1+2e(h'-h)=2eh'-1$, which recovers (2). The forward and
converse maps are inverse to each other, as in the manuscript. Both $m$ and
$m'$ are odd and coprime to $k$, hence units modulo $2|k|$, so the
congruence is imposed by the same character expansion (6.19).

**The cutoff arguments.** In place of (6.20) the smooth $(e,n)$ cutoffs are
evaluated at

$$
e=\frac{m-m'}{2k},\qquad
n=\frac{2eh-1}m=\frac{(m-m')z}{kmm'}-\frac1m,
$$

which differ from the manuscript's expressions only by the sign of $k$ and
of the last term. Their derivatives in $\log(m/U)$, $\log(m'/U)$ and
$\log(z/Z)$ obey the bounds stated after (6.20), so the Fourier separation
has the same total variation.

**The endpoints.** Since $m,m'$ are free of group primes,
$z_*=m'h_*$, $(z+k)_*=mh'_*$, $W_\ell(z)=W_\ell(h)$ and
$W_\ell(z+k)=W_\ell(h')$, exactly as before. The endpoint functions (6.22)
and (6.23) and the separated summand are unchanged, with character modulus
$2|k|$, and the discrepancy hypothesis is still carried by the original
sequence $\alpha$. Theorem 5.1 bounds each separated correlation, and the
remaining steps, including the order of precisions in Remark 6.2, are
unchanged.

## The extraction of primes

**Candidate mass.** Proposition 7.1 concerns $A(u)$, $X_A$ and the prime
factors of $u$ only, and is used as stated.

**Type I distribution.** For odd squarefree $d$, the congruence
$2u-1\equiv0\pmod d$ holds exactly when $u\equiv\bar2\pmod d$, where
$\bar2$ is the inverse of $2$ modulo $d$, which is a unit class. The proof
of Proposition 7.2 uses only that the congruence fixes one unit class of
$u$: character orthogonality on that class, the cost of the noncoprime
moduli, and the large sieve and Siegel–Walfisz bounds for the twisted sums
are all taken in absolute value. The remainder bound (7.8) therefore holds
for $N_u=2u-1$, and it excludes $d$ with $(d,u)>1$ automatically.

**Preliminary sieve.** For an odd prime $p$ the Type I main term gives
density $1/(p-1)$ for $p\mid N_u$, as before, so the sieve bound (7.11) and
its singular series $\mathfrak S$ are unchanged. Every $N_u$ is odd, so the
prime $2$ never divides it.

**Composites away from balance.** Theorem 6.1 for $2u-1$, Lemmas 7.3 and
7.4 and the sieve with moduli $pd$ through the Type I bound give (7.21) and
(7.22) unchanged. Lemma 7.4's bound (7.17) uses only $mn=N_u$ with
$N_u\asymp x$.

**Balanced composites.** The two applications of Theorem 6.1 now concern
$mn=2u-1$. In the two-variable sieve, $D_1$ contains the complete micro-band
lists, including the exceptional rough integer, and one marked prime per
P-group. Its pure prime entries are at least $L^{20}$, and every prime
factor of the exceptional integer exceeds $W$, so $D_1$ is odd. Hence
$D_1\mid u$ and $mn=2u-1$ give

$$
mn\equiv-1\pmod{D_1}
$$

in place of $mn\equiv1$. For each unit residue of $m$ modulo $D_1$ exactly
one residue of $n$ satisfies this, including when $D_1$ has prime-power
factors, so there are again exactly $\varphi(D_1)$ residue pairs. For an odd
prime $l\nmid D_1$ the bad events are $mn\equiv0\pmod l$ for $l\le W$, with
$2l-1$ residue pairs, and, for a banned prime, $l\mid u$, which now reads
$mn\equiv-1\pmod l$, with $l-1$ residue pairs. The two sets are disjoint, so
$\nu(l)$, the densities $g(l)$, the Chinese-remainder counts, the lattice
errors (7.28) and the Euler product (7.29) are unchanged, and so is the
dyadic bound (7.30) and the balanced bound (7.31), with the same constant
$C_{\rm bal}$.

**Counting the primes.** The parameter choices are made in the manuscript's
order. Subtracting (7.31) from (7.22) leaves
$\sum_{2u-1\text{ prime}}A(u)\Psi(u/x)\gg X_A/L$. Each summand is at most
$\exp(O(\sqrt L))$ by Proposition 7.1, $X_A\gg xL^{-C_A}$, and
$u\mapsto2u-1$ is injective, so at least $x^{1-o(1)}$ distinct primes
$p=2u-1$ occur. Since $\Psi(u/x)\ne0$ forces $x\le u\le2x$, they satisfy
$2x-1\le p\le4x-1$, and

$$
P^+(p+1)=P^+(2u)=\max\bigl(2,P^+(u)\bigr)\le x^\delta
$$

for large $x$, because every prime factor of a supported $u$ lies in
$[L^{20},x^\delta]$. This is (1).

## Quantifiers, errors and the order of choices

The transfer retains the manuscript's quantifiers, not an effective
numerical threshold. Fix $\delta\in(0,1/4)$ and the candidate geometry,
including $\Psi$, $r_0$, the Q/P bands, the finite lower-bound prefix, and
$j',\theta$ of (7.24). Its estimates give constants $C_A,C_w,c_A>0$ with
$X_A\ge c_AxL^{-C_A}$ and each prime summand at most
$\exp(C_w\sqrt L)$ once $x$ exceeds a threshold depending on the fixed
parameters. None of these bounds depends on the sign.

The balanced error is exactly of the form

$$
C_{\rm bal}(\kappa+L^{-1})\frac{X_A}{L}+o(X_A/L),
$$

where the source asserts that $C_{\rm bal}$ is independent of
$\kappa,b_1,j_{**}$ and the later discrepancy precision $S$. The residue
calculation above preserves that independence. Choose
$\kappa\in(0,1/50)$ with $C_{\rm bal}\kappa<\mathfrak S/4$, then $b_1$
small enough for (7.11), (7.19) and (7.22), and set $b_*=b_1/3$. Choose
$j_{**}$ so that $\eta_*<b_*/4$, as required by Theorem 6.1 and (7.10),
and fix the finite exponent mesh. Type I is used at the source's level
$x^{1/2-\kappa/2}$; changing a unit class does not enlarge that level.

Next choose the Type II saving $D_*$ so large that its error
$xL^{-D_*}$, including the fixed powers of $L$ from all dyadic sums and
separations, is $o(X_A/L)$. For example, if those losses are at most
$L^{C_{\rm loss}}$, it is enough to take
$D_*>C_A+1+C_{\rm loss}$. Those coefficient exponents are fixed independently
of $S$. Theorem 6.1 then fixes its required discrepancy exponent $B$;
only afterwards is $S$ chosen large enough for Lemma 7.3 to supply it.
The source's sign-free assertions of these bounds and their uniformity
remain explicit premises of this argument.

With every parameter fixed in that order, subtraction leaves
$cX_A/L$ on primes for a fixed $c>0$ and all sufficiently large real $x$.
Consequently the retained lower bound is

$$
c' xL^{-C_A-1}\exp(-C_w\sqrt L).
$$

For each fixed $\eta>0$, its ratio to $x^{1-\eta}$ tends to infinity,
because $\eta L-(C_A+1)\log L-C_w\sqrt L+\log c'\to\infty$.
Taking the maximum of the earlier thresholds and this last threshold
gives $x_0(\delta,\eta)$ valid for every real $x\ge x_0$. No uniformity
as $\delta\downarrow0$, and no computable value of $x_0$, is claimed.
This is exactly the fixed-$\delta$ quantification needed by
$\mathrm A^+$.

## Places checked and not checked

Read in full here, in the transcription, for every use of the sign: the
statements of Theorem 1.2, Theorem 5.1 with its endpoint form (5.1)–(5.4),
and Theorem 6.1; the results of Section 2 that Sections 6 and 7 use
(Theorems 2.2 and 2.3, Corollary 2.4, Lemmas 2.5–2.9 and Corollary 2.10),
none of which involves the sign; the whole proof of Theorem 6.1; and the
whole of Section 7, including the proofs of Propositions 7.1 and 7.2 and
Lemmas 7.3 and 7.4.
Sections 1–5 and 8 were searched for the form $2u+1$, which occurs there
only in the description of the method in the introduction. Every use of the
sign in those proofs is listed above, each with the identity, bound or count
that replaces it. The sign-free steps were read for their role, not checked
line by line.

Outside this sign audit: Sections 3–5, the transference theorem, the ideal
kernels and the lifted shift cancellation, which carry the new analytic method and on
which Theorem 5.1 rests; the sign-free steps of Sections 6 and 7; and the
cited external results. The
[[research/smooth_successor_primes/shift_sign_analytic_core|separate analytic-core
examination]] records proof-depth author reading of Sections 3–5 and the
precise uniform assertion still needed; it grants no independent standing.
Li and Zhuang record that Lean statements for the
manuscript required the hypothesis $\ell\ge1$ in its definition of prime
groups; Section 7 takes $\ell=1$, so this does not affect the count.
