---
name: research/smooth_successor_primes/shift_sign_analytic_core
title: The shift sign in the weighted-dilation analytic core
desc: |
  The signed shift in the weighted-dilation transference and cancellation
  argument: the memory identity, norm bounds, equality-rank expansion,
  ideal kernels and local Fourier-energy estimates, with their parameter
  order and the precise source estimate still needed by the successor
  route. Author examination, without independent acceptance.
created: 2026-10-15T07:33:49Z
updated: 2026-10-15T07:33:49Z
---

# The shift sign in the weighted-dilation analytic core

***

The [[research/smooth_successor_primes/_index|smooth-successor route]] uses
Sections 3–5 of the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]]
only through the statement of its Theorem 5.1, premise (P) of the
[[research/smooth_successor_primes/signed_type_ii|Type II estimate for 2u-1]].
That statement allows every integer shift $0<|k|\le L^C$, and the manuscript's
own Type II estimate for $2u+1$ already applies it at both signs, since its
$m'-m=2ek$ takes either sign. So the change from $2u+1$ to $2u-1$ needs no new
estimate from Sections 3–5. This page records, as a check of that statement
against its proof, every place where $k$ enters the proof and why none depends
on its sign. It then records how far this reading checked the proof of (P),
re-derives in outline its most intricate step, and states what remains. The
observation that Sections 2–5 are used as stated is Li and Zhuang's; the
inventory, the checks and the re-derivation below are Plasma AI's,
author-recorded.

Notation follows the manuscript: $D$ is the product of the shared and free
labels of an edge, $\sigma_i=\pm1$ marks forward and adjoint edges, $N=2R$ with
$R=\lceil L^{0.52}\rceil$ is the length of the moment, and
$P_*=\exp(L^c)$ is the smallest big-group prime.

## Where k enters

1. **The physical operator** (Definition 3.3). An edge moves the position $n$
   to $n+kD$ with $0<|k|\le L^{C_2}$, and its adjoint moves it by $-kD$.
   Positions range over all of $\mathbb Z$ with counting measure, and the
   absolute bounds of Lemma 3.4 use only divisibility and translation.
2. **Path offsets** (3.8). A path's offsets satisfy
   $h_{i+1}-h_i=\sigma_ikD_i$, so the sign of $k$ enters only through the
   signs of these steps. The paths of $(\mathcal A\mathcal A^*)^R$ already
   contain steps of both signs, from forward and adjoint edges, and every later
   use of the offsets is through their residues, translations and the phase
   $e(\theta h_N)$.
3. **Residue replacement** (Lemma 3.6). The average over the root uses the
   offsets only through their residues modulo group primes and through counts of
   Chinese-remainder classes. The return $h_N=0$ is imposed by
   $\int_0^1e(\theta h_N)\,d\theta$.
4. **The memory construction** (Lemma 3.7 and the edge operation). Residues
   are translated by $\Delta=\sigma_ikD$. Compatibility uses that every group
   prime exceeds $|k|$: a prime active at both ends of an edge divides $kD$,
   hence $D$.
5. **Rare transfers** (Lemma 3.9). A promotion requires
   $r+\sigma_ikD_{\mathcal B}D_{\mathcal S}\equiv0\pmod p$ for a big prime
   $p>|k|$. Since $F$, $k$ and $D_{\mathcal B}$ are units modulo $p$ and the
   $\mathcal D$ products of omitted small labels are distinct integers below
   $p$, at most one omission choice allows a given promotion. Only the
   invertibility of $k$ modulo $p$ is used.
6. **Clean edges** (Lemma 3.10). After Fourier transformation in the small
   residue torus and the pending residues, translation by
   $\sigma_ikd'D_{\mathcal B}$ becomes the phase
   $e(\sigma_i\Theta D_{\mathcal B})$, with a real
   $\Theta$ depending on $k$, $d'$, the memory primes, the frequency and
   $\theta$. Hypothesis (3.6) is a supremum over all real $\Theta$, so $k$,
   whatever its sign, is absorbed into $\Theta$.
7. **Endpoint pairing** (Corollary 3.11). The block length $H$ bounds $|kD|$.
8. **Ideal kernels** (Section 4). The shift does not occur; the norm bound
   (4.1) is uniform in $\Theta\in\mathbb R$ and $|\zeta|\le L^{C_4}$.
9. **The physical lift** (Section 5). The sum (5.5) runs over $z>0$ with
   $z+k>0$. In the lift (5.7), $w'=w+kD_C$ is positive because
   $|kD_C|=x^{o(1)}$ while $w=x^{1+o(1)}$. The free-label exclusion writes
   $w'=p'(v+kD_C/p')$ with $p'\mid D_C$, again for either sign.
10. **Comparison shifts** (5.9)–(5.10). The shift is $kD_AD_B$ and the
    multiplier is $M(\theta)=\mathbb E\,b_1(D_A)b_2(D_B)e(-k\theta D_AD_B)$.
    Its minor-arc bound applies Dirichlet's approximation to $k\theta$ and the
    bilinear Lemma 4.2. Dividing by $k$ places $\theta$ within $L^{O(1)}/H'$ of
    a fraction with denominator at most $|k|r'$; the sign of $k$ changes only
    the numerator.
11. **Major arcs and the Mellin argument** (5.11)–(5.17), Lemmas 5.2–5.4. These
    concern the first endpoint alone; $k$ does not occur.

Every step is therefore either independent of $k$ or uses only $|k|\le
L^{O(1)}$, translation by $kD$, positivity of shifted positions that are
$x^{1+o(1)}$ in size, or invertibility of $k$ modulo primes above $|k|$. These
transformations preserve the proposed proof for both signs. No additional
sign-specific estimate was identified in Sections 3--5. This does not
establish the estimates themselves by sign symmetry.

## What this reading checked

The author examination of 2026-10-15 (UTC) read Sections 3–5 in full in the
linked source's library transcription, at proof depth. The following steps
were checked in detail, and no error was found in them.

- **Corollary 3.11 from Theorem 3.5.** Spectral Hölder for $\mathcal
  A\mathcal A^*$, the trace bound for the positive semidefinite block matrix
  that uses only mark independence of the first vector, the block length
  $\log H=O_J(TL^d)$, and the Hölder summation with exponents $2$,
  $2R/(R-1)$ and $2R$.
- **Lemma 3.6.** The Bonferroni truncation at degree of order $NT$, the count
  $\exp(O(h(L^d+\log N+\log s)))=\exp(o(L))$ of Chinese-remainder terms, which
  needs $0.52+d<1$, and the relative comparison with
  $Q_{\rm act}^{-1}\exp(-O(NT))$.
- **The lifespan expansion** (3.12)–(3.14). Each represented big prime has
  one lifespan and is charged $V_g^{-r}/(pb_p)$ for $r$ active runs, matching
  the original label normalization and the reciprocal-prime cost paid once.
- **The memory charges, prime by prime** (Lemma 3.7). An active birth costs
  $\widetilde\mu_g(p)$ and each later promotion $V_g^{-1}$; a ghost birth
  costs $V_g\widetilde\mu_g(p)=1/(pb_p)$ with the factor $-\eta_j$; a drop
  and a store followed by a ghost termination reproduce the two terms of the
  suffix identity (3.13), and a ghost birth followed by a promotion the prefix
  term; the splitting $\rho\,(q_i/\rho^2)\,\rho$ gives $q_i$ at each internal
  hit of a pending particle, and no damping to a particle that is active,
  stored or promoted at that visit, including at the boundary visits where
  $q_0=q_N=\sqrt q$; the exclusion $p\nmid D$ for stored and promoted particles
  follows from the bans; orphans reproduce (3.14).
- **The factorial measures and absolute bounds.** The ghost adjoint (3.19),
  with the selection of $t$ old zeros among $k+t$; the edge accounting
  (3.23)–(3.25), $(j)_a/j!=1/(j-a)!=(j-a+b)_b/(j-a+b)!$; the weighted Schur
  test (3.18) with $w=v^{j_{\rm tot}}$, the ghost row and column ratios
  (3.20) under the condition (3.21), and the edge bounds (3.26) of Lemma 3.8
  in both directions; and the memory truncation (3.27)–(3.28), where doubling
  every ghost birth keeps (3.21) and charges $2^{-B+O((\ell+m)sN)}$ to the
  paths that exceed the truncation.
- **Lemma 3.9 and (3.32).** The uniform omission choice under the small-group
  symmetrization, at most $B$ of the $\mathcal D$ choices allowing a
  promotion, the reversal argument for stores, and the saving
  $L^{-(c_0/2)\log\binom{J+\ell}\ell}$.
- **The reduction in Lemma 3.10.** The maps $P_{\mathbf d}$ and (3.35), the
  diagonalization of the translations, the identification of the remaining
  operator with $\mathcal T(\Theta)$, and the negligible cost of replacing
  $\mu_g$ by $\widetilde\mu_g$ and of removing the free-label ban.
- **The distinct-birth restoration** (3.40)–(3.47). The cycle-sign identity
  (3.41), the point-mass saving $O(P_*^{-1})$ per dependent birth at large
  rank, and the Fourier representation of the equalities at small rank, which
  keeps the signed contraction on all but $2r=o(N)$ edges.
- **Section 4.** The collapse (4.4), Lemma 4.2 and (4.6), the kernel bounds
  (4.8)–(4.11), Lemma 4.3 in both ranges of the denominator, and the
  cancellation in the proof of Theorem 4.1: the Efron–Stein components, the
  symmetric-probe bound (4.22)–(4.24), which uses $\ell\ge1$, and the sign
  identity (4.26).
- **Section 5.** The endpoint norm bound independent of $J$, the Mellin
  decoupling of $\Psi(n/(ZD))$ into the ideal frequency $\zeta$, the
  raw-pattern identity (5.7), the minor-arc claim, the reduction to local
  Fourier energy (5.11), the small-mark identity (5.12), the Gallagher-type
  conversion (5.14)–(5.16), and Lemmas 5.2–5.4.

The explicit parameter inequalities were checked line by line: in (3.37),
$E_{\rm id}>G+C_s+2$ makes the clean part at most $\frac12L^{-G}$ and the
choice of $J$ does the same for (3.32), and $G>E+C_v+3$ beats the ghost
operations; in (4.20), the five lines control the dyadic sum, (4.14), (4.17),
the square root of (4.16), and (4.11) with (4.19), in that order. The order of
choices stated in the manuscript (the transfer target, then the ideal family,
then $J$; the analytic precisions; the discrepancy exponent last) was followed
through these steps without finding a circular dependence.

## The memory identity as a bijection

The most intricate step is the exact memory identity, Lemma 3.7, which the
manuscript proves in a few paragraphs. It was re-derived here in outline as a
bijection of two expansions.

Work in the independent-residue model of Lemma 3.6 with the phase
$e(\theta h_N)$. A *skeleton* fixes the patterns, the endpoint permutations,
the auxiliary free labels and the active big and small lists at every visit,
with their prime values; it determines the offsets $h_i$ and a weight (the
label normalizations $V_g^{-M}$ at visit $0$ and $V_g^{-t_g}$ at each edge,
the free-label probabilities, the coefficients and the phases). The residue
expectation factors over primes. For a big prime $p$ with no active visit, the
factor is $b_p$ plus one orphan term for each pair $j<i$ of hits, by (3.14).
For a big prime with active visits whose offsets agree modulo $p$, the factor
is $p^{-1}\prod_{i\text{ inactive}}(1-\eta_iH_i)$, and the identities (3.13)
expand it into a start (the first active visit, or a ghost birth at an earlier
hit) and an end (the last active visit, or a ghost termination at a later hit),
leaving $q_i$ at the internal hits. After division by $\prod_pb_p$, the path sum
is a sum over *histories*: a skeleton, a finite set of never-active big primes
each with an orphan interval, and a start and an end for each active big prime.

The operator product $\langle\mathbf 1_\varnothing,G_0\mathcal E_0\cdots
\mathcal E_{N-1}G_N\mathbf 1_\varnothing\rangle$ expands into a sum over
sequences of local choices: at each edge the pattern, the permutations, the
free labels, which unshared source slots are stored and which dropped, which
target slots are promoted and the injection into old pending particles, and
the fresh target values; at each visit the terminated pending zeros and the
ordered batch of ghost births with its values. Under the distinct-birth rule,
sending a history to the local choices it dictates is a bijection. An unshared
source label is stored when its prime has a later active run or a ghost
termination, and dropped otherwise; an unshared target label is promoted when
its prime is pending, and freshly born otherwise; ghost births and terminations
sit at the start and end hits, and an orphan is a ghost birth followed by a
ghost termination. Conversely, distinct births give each prime value a single
birth, so the local choices determine every prime's active visits, start and
end.

The constraints agree on the two sides. A promotion checks displacement zero,
which is the congruence of the offsets of consecutive uses. The operator's
exclusion $p\nmid D$ for stored and promoted particles removes no history,
since an unshared label is neither a shared nor a free label and so does not
divide $D$. The same fact, with $p>|k|$, makes the displacement of a newly
stored particle nonzero after the step, so it cannot be promoted across the
edge that stored it. A pending prime cannot equal an active label, because that
would be a second birth of the same value, while it may equal a free label,
which is not a birth and whose divisibility of $D$ leaves its residue
unchanged. The weights
agree prime by prime, as listed in the previous section, with $V_g^{-1}$ per
active run and $1/(pb_p)$ once per prime. The factor $1/b!$ of a ghost batch and
the factorial memory measure count each set of distinct particles once, by
(3.19) and (3.25). The symmetrizations of two adjacent edges merge into the
single projection between the factors of $(\mathcal A\mathcal A^*)^R$, and the
ghost operations commute with them. The small groups keep their Haar coordinate
and physical lists on both sides.

*The truncation.* Memory grows only by stores, at most $(\ell+m)|\mathcal B|$
per edge, and by ghost births. A history whose memory ever exceeds $B$ thus has
at least $B-O((\ell+m)sN)$ ghost births, and since doubling every ghost birth
keeps (3.21), such histories weigh at most $2^{-B+O((\ell+m)sN)}L^{O(N)}$ in
absolute value, with or without the distinct-birth indicator. In the truncated
evolution, Lemma 3.9 uses $B$ as the bound on pending particles, Lemma 3.10
absorbs the projections into its test vectors as contractions, Lemma 3.8
persists under them, and the rank expansion is applied to the truncated
evolution, its large-rank terms using only absolute bounds and its small-rank
terms using (3.38) for the unaffected truncated edges. So the truncation is
consistent with every later step.

## Quantitative transference obligations

The following calculation explains why the separate source estimates are
strong enough, and which uniformities are essential. It is a reconstruction
of the deductions in Sections 3--4, not an additional assumption that their
unrefereed lemmas have been independently established.

For the memory identity, put

$$
b_p=1-\frac1p\sum_{i=0}^N(1-q_i),\qquad \mu_g(p)=\frac1{V_gp},\qquad
\widetilde\mu_g(p)=\frac1{V_gpb_p},\qquad
q_0=q_N=\sqrt q,\quad q_i=q\ (0<i<N).
$$

All big primes exceed $P_*=\exp(L^c)$, whereas $N=O(L^{0.52})$.
Thus $b_p>0$ and
$\widetilde\mu_g(p)/\mu_g(p)=1+O(N/P_*)$. Counting measure on each pending
residue is essential: the test $r=0$ selects a point and supplies no further
$1/p$. A lifespan with $r$ active runs must carry exactly
$V_g^{-r}/(pb_p)$. A probability measure on that residue coordinate would
charge an extra reciprocal prime at later returns and would not give the
identity.

With memory cutoff $B_{\rm mem}=\lceil L^2\rceil$ and
$\mathcal D=\binom{J+\ell}{\ell}^{|\mathcal S|}$, the two edge estimates
needed from Lemmas 3.9 and 3.10 are

$$
\|\mathcal E_{\rm dirty}\|
\le 2L^{C_a}\sqrt{B_{\rm mem}/\mathcal D},
\qquad
\|\mathcal E_{\rm clean}\|\le2L^{-E_{\rm id}+C_s}.
$$

For the first inequality, fix a pending big prime $p$ and all big-label
choices. If $F$ is the product of the small source labels and $U$ the product
of the omitted ones, promotion requires
$r+\sigma_i kD_{\mathcal B}F/U=0$ modulo $p$, with all denominators units.
The $\mathcal D$ omission products are distinct positive integers smaller
than $p$. Therefore a fixed pending particle permits at most one omission
choice, and at most $B_{\rm mem}$ choices permit any promotion. The absolute
row bound gains $B_{\rm mem}/\mathcal D$; the column bound does not need
that gain. Schur's inequality gives its square root. Reversal treats stores.
This reasoning is unchanged when $k<0$.

For the clean edge, the small-state maps in (3.34) obey
$\sum_{\mathbf d}\|P_{\mathbf d}w\|^2\le L^{C_s}\|w\|^2$. In one small
group the multiplier is bounded by

$$
\sup_{y\ge M}q^{y-M}\frac{(y-M+\ell)_\ell}{V_g^\ell},
\qquad M=J+\ell,
$$

which is independent of $J$. With memory prime lists fixed, translations of
the small and pending residues have a finite Fourier decomposition. Each
fiber sees the ideal operator at some real frequency $\Theta$, even for
negative $k$. The density perturbation from $\mu_g$ to
$\widetilde\mu_g$, and the cost of removing the free-label collision ban,
are each $L^{O_J(1)}/P_*$ in norm. These are smaller than any fixed negative
power of $L$. The stated clean bound follows from the uniform ideal bound.

The ghost operations have norm at most $L^{C_v}$, with $C_v$ independent
of $J$ and of the comparison complexity. Choose

$$
G>E+C_v+3,\qquad E_{\rm id}>G+C_s+2,
$$

then construct the ideal family, and finally choose $J$ large enough that
$2L^{C_a}\sqrt{B_{\rm mem}/\mathcal D}\le\frac12L^{-G}$.
The clean term is also at most $\frac12L^{-G}$ eventually. This gives
$\|\mathcal E_i\|\le L^{-G}$ while different births are still permitted
to use the same prime. In particular, $C_a$ may depend on the already chosen
comparison complexity; the target $E_{\rm id}$ must not depend on that
complexity. This is the order supplied by the source.

Global birth distinctness cannot be restored by a single absolute collision
error. For any fixed positive $C_h$,

$$
L^{C_hN}P_*^{-1}
=\exp(C_hN\log L-L^c)
$$

does not even tend to zero, since $c<0.47<0.52$. Thus that proposed shortcut
would lose the required saving. The source instead expands distinctness by
equality rank. At rank $r$ the total absolute inclusion-exclusion coefficient
is at most $L^{C'r}$. The two bounds are

$$
L^{C_h(N+1)}(C/P_*)^r
\quad\hbox{and}\quad
O\!\left(L^{(-G+C_v)N+C_v+2r(G+C_a)}\right).
$$

The first comes from one fresh-label atom bound per dependent birth, keeping
the earlier pivot value in the conditioning even if that particle has died.
The second inserts equality by Fourier phases at the birth operations only.
At most $2r$ edges lose their signed norm bound; all other edges keep their
complete pattern sum and both symmetrizations. A multiplier on a particular
ghost-batch address is averaged over that batch before applying the symmetric
memory operator, so its modulus remains at most one.

Split at
$r_0=\lceil C''N\log L/\log P_*\rceil$. For large $C''$, the first bound
summed over $r\ge r_0$ is $o(L^{-EN})$. Since
$r_0/N=O(\log L/L^c)+O(1/N)=o(1)$, the second bound and the coefficient
count sum to $L^{(-G+C_v+o(1))N}=o(L^{-EN})$ for $r<r_0$.
The memory tail is $\exp(-\Omega(L^2))$, and the residue replacement has
arbitrarily strong relative precision after fixing its Bonferroni order.
This explains the proposed root-moment estimate (3.7). The single-collision
calculation is an obstruction to that shortcut, not a counterexample to the
equality-rank argument or the theorem.

The required ideal bound is also uniform over the entire coefficient use.
For a selected product of labels of size $U$, its probability at a particular
integer is at most $L^\kappa/U$. Fiberwise Cauchy--Schwarz therefore converts
an arbitrary tuple test to an integer coefficient sequence of squared norm
at most $L^\kappa/U$ times its original squared norm. The integer bilinear
estimate handles rational denominators larger than a fixed power of $L$.
For smaller denominators, the cellwise character Gram matrix is
$I+O(Q^2\xi^{-1}L^{-D_*})$ in operator norm and hence has norm at most two
after the precision is chosen. Matching cells control the Mellin and
remaining additive phase. This supplies (4.12) for arbitrary tuple tests,
including the conditional tests used in Theorem 4.1.

For $M\ge(m+\ell)(m+\ell-1)$, the remaining ideal cancellation uses the fraction

$$
\frac{\binom{M-m-\ell}{j-m}}{\binom Mj}
=\frac{(j)_m(M-j)_\ell}{(M)_{m+\ell}}
\le2\ell^\ell m^{-\ell}
$$

of symmetric coordinate components containing every probe and avoiding the
last $\ell$ slots. This is small by choosing $m$ large, precisely because
$\ell\ge1$. Across a block of $\gg\log L$ groups it gives any prescribed
logarithmic saving. Alternating nonempty probe subsets cancel the other
components. The $3^P$ approximation errors are paid by the precision in
(4.12), before choosing $J$. The application takes $\ell=1$ throughout.

## The local Fourier-energy estimate

This is the remaining analytic use of the endpoint hypotheses after the
residual physical pairing. The norm calculation for that pairing uses
$\tau(n_*)^4$, a fixed divisor moment. Summing a prescribed physical list
first contributes its reciprocal product, whose total normalized mass is at
most one. Thus the endpoint norm exponent is independent of $J$.
Corollary 3.11 and the ideal estimate can be chosen in the required order.
Removing shared labels then gives the raw correlation plus comparison shifts
$kD_AD_B$, as in (5.7).

For a comparison, Fourier inversion in the integer position leaves the
multiplier

$$
M(\theta)=\mathbb E\,
b_1(D_A)b_2(D_B)e(-k\theta D_AD_B),\qquad |b_1|,|b_2|\le1.
$$

Both free products are nonempty. The same integer bilinear estimate makes
$M$ smaller than any required negative log power outside arcs of width
$L^{C_{\rm arc}}/H'$ around rationals of denominator at most
$L^{C_{\rm arc}}$. Here $D_AD_B\asymp H'$ and
$\exp(L^c)\le H'\le\exp(O(\log L\,L^d))$. Dirichlet approximation is
applied to $k\theta$; dividing by negative $k$ only changes a numerator
sign. Set $Y=ZH'$ and $H=H'/L^{C_{\rm arc}}$.

On the remaining arcs, the needed estimate is the first endpoint's local
energy

$$
\int_{|\beta|\le1/H}|\widehat{\mathcal U}(a/r+\beta)|^2\,d\beta
\ll_A YL^{-A}.
$$

One small marked prime can be removed because $\ell=1$; the square-divisible
exception costs $YL^{O(1)}\exp(-L^a)$ in squared norm. The factors $m$,
the small prime, and the long rough integer are units modulo the arc
denominator. Splitting the residual factor by its gcd with that denominator
and using characters on the resulting quotient retains principal and
imprimitive characters. These have exactly the modulus bounds allowed by
the discrepancy hypothesis.

The additive-to-Mellin conversion (5.14)--(5.16), followed by dyadic
separation, reduces the estimate to

$$
\int_{|t|\le 2LY/H}|P_s(t)P_l(t)\mathcal R(t)|^2\,dt\ll L^{-A'}
\tag{*}
$$

with

$$
\begin{aligned}
P_s(t)&=\sum_{p_s\asymp P}b_s(p_s)p_s^{-1+it},\\
P_l(t)&=\sum_{\substack{p\asymp P',\ p\in I_{**}\\P^-(p)>W}}
                  \chi_p(p)p^{-1+i\sigma_1+it},\\
\mathcal R(t)&=
\left(\sum_{m\asymp M_0}\alpha_m\chi_m(m)m^{-1+i\sigma_0+it}\right)
\left(\sum_{r\asymp R_0}d_rr^{-1+it}\right).
\end{aligned}
$$

The variable $p$ is an integer, not necessarily prime. The parameters satisfy
$\exp(L^a)/2\le P\le\exp(L^b)$,
$x^\tau/2\le P'\le x^\eta$ with $\eta<1/4$, and
$PM_0P'R_0\asymp Y$. Every fixed subproduct, collapsed to a polynomial
of size $U$, has coefficient-square sum $L^{O(1)}/U$. The remaining mark
weight has already been bounded by a fixed log power; it does not increase
the order of the divisor moment.

Here is how the three time regimes prove $(*)$.

- Where $|P_s(t)|\le L^{-A_s}$, ordinary mean square for $P_l\mathcal R$
  gives $O(L^{-2A_s+C})$. Its size is $Y/P$, which exceeds the time range:
  $H/(2LP)\to\infty$ because $b<c$.
- The set where $|P_s(t)|>L^{-A_s}$ meets only $Y^{o(1)}$ unit intervals.
  Indeed, for $j=\lfloor\log Y/\log(2P)\rfloor$, the squared coefficients
  of $P_s^j$ sum to at most $j!(C/P)^j$. A unit-separated mean square gives
  an interval count at most $YL^{O(1)}j!(CL^{2A_s}/P)^j$. Its logarithm is
  $O(L^b+L^{1-a}\log L)=o(\log Y)$.
- On these exceptional intervals, $\mathcal R$ has a sparse mean square
  bounded by $L^{O(1)}$. Its size is
  $U\asymp Y/(PP')\ge Y^{1-\eta-o(1)}>Y^{0.6}$. For unit-separated
  sample times, the Gram kernel satisfies
  $|\sum_{n\asymp U}n^{iz}|\ll U/(1+|z|)+Y^{1/2}$ for $|z|\ll Y$,
  by the first and second derivative tests. With $R=Y^{o(1)}$ samples,
  the absolute row sum is $O(U\log(2Y)+RY^{1/2})=O(U\log(2Y))$.
  Multiplying by the coefficient-square sum proves
  $\sum_j\sup_{t\in I_j}|\mathcal R(t)|^2\ll L^{O(1)}$.

For completeness, the long factor is uniformly small on those intervals
when $L^{B_0}\le|t|$ and $|t+\sigma_1|\le x^2$. A block-sieve upper
polynomial with $h_s=2\lceil(\log L)^2\rceil$ and
$D=W^{4h_s+2}=x^{o(1)}$ replaces roughness with absolute harmonic error
$O(e^{-h_s}+D/P')$. Its coefficients obey
$\sum_d|\lambda_d|/d\ll\sqrt L$. For each $d$, split into character residue
classes and apply the derivative tests to
$\exp(iu\log(q'y+a))$, where $u=t+\sigma_1$ and
$N=P'/(dq')\ge x^{\tau/2}$. For $|u|\le cN$ the normalized bound is
$O(|u|^{-1})$. Otherwise finitely many ranges
$N^{j-2+1/10}\le|u|\le N^{j-1/10}$ cover $cN<|u|\le x^2$.
After $j-2$ differencing steps with shifts at most $N^{1/(20j)}$, the second
derivative test saves a fixed power $N^{-\delta_\tau}$. Partial summation and
the sum over $d$ give

$$
|P_l(t)|\ll e^{-h_s}+D/P'
+\sqrt L\bigl(L^{-B_0}+x^{-\tau\delta_\tau/2}\bigr).
$$

Thus $|P_l|\ll L^{-A_l}$ for any fixed $A_l$ by choosing $B_0$ large
enough after the fixed frequency bound. Combining this with the sparse
mean square bounds the high-time exceptional contribution to $(*)$ by
$L^{-2A_l+C}$, with no factor counting the exceptional intervals.

Finally, for $|t|\le L^{B_0}$ the $m$-polynomial is at most $L^{-B}$
by the original discrepancy hypothesis, after $B$ exceeds all character,
frequency and interval requirements. The other factors have absolute
log-power bounds. This part is therefore $O(L^{-2B+B_0+C})$.
Choose $A_s$, then $A_l$ and $B_0$, and finally $B$. All three contributions
have the saving required in $(*)$. The Fourier tails are controlled by
ordinary mean square; their fixed cutoff exponents do not grow when their
accuracy is increased. This completes the proposed comparison cancellation
at the uniformity required in (P), without a new restriction on the sign.

## What remains

No failing estimate or counter-configuration was found. The memory argument
and the quantitative deductions above are author examinations of
OpenAI's source proof. They supply no independent acceptance. The classical
prime number theorem, Siegel--Walfisz theorem, multiplicative large sieve
and derivative tests are used in the forms stated in Section 2.

The remaining mathematical dependence is (P), together with the elementary
source inputs (E) specified in the combined sketch. It is not merely a
missing label on an established result: the unrefereed analytic proof remains
the premise being consumed. The absence of a detected error does not prove
its uniform assertion.

The full Theorem 5.1 is stronger than the application needs. A sufficient
replacement is this precise restriction. For every fixed group and band data
and every fixed $D_0,C>0$, there must be a fixed $B$ such that the harmonic
correlation displayed as (P) is $O(L^{-D_0})$, uniformly for all
$0<|k|\le L^C$, $xL^{-C}\le Z\le xL^C$, the allowed cutoffs and frequencies,
and the two endpoint formulas in step 5 of the
[[research/smooth_successor_primes/signed_type_ii|Type II page]].
Here $\alpha$ is the original restricted $W$-rough sequence satisfying
$(\mathrm D_B)$, the common residual coefficient $c_r$ and the common rough
interval $I_{**}$ arise from the band partition, and the character modulus
is $2|k|$. The range includes both signs of $k$. It is enough to prove this
for the prime and roughness proxy differences used in the extraction, with
uniformity in their interval restrictions and their final cell precision.
The required $B$ is chosen before that precision.

This restriction states exactly what could replace (P) if its general form
failed; no such failure is asserted here. A proof for a common uniform
endpoint class would apply to both sign choices. A proof for selected calls
from the predecessor calculation need not apply to all successor calls,
whose separated cutoff coefficients differ.
