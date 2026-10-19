---
name: research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/ideal_comparison
title: "Arbitrary tuple tests and the ideal comparison"
desc: Independent arbitrary-tuple, concentrated-cell, and probe-cancellation checks for the ideal comparison operator.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Arbitrary tuple tests and the ideal comparison

***

This examines Section 4 of the
[preserved source](../../assets/endpoint_cancellation_subject/source_sections_2_to_5.md.txt). The source
construction is OpenAI's; the independent examination is prepared for
Plasma AI. Its scope includes arbitrary square-integrable tests on ordered
label tuples, not merely functions of their products.

## Collapse does not discard tuple information

A selected set uses at most $m$ slots in each big group. If its product is
$n$, unique factorization determines the multiplicities $a_p$ of its
labels. With $k_g$ selected slots in group $g$, its probability is

$$
\rho(n)=\frac1n\prod_g
          \frac{k_g!}{V_g^{k_g}\prod_{p\in\mathcal P_g}a_p!}
\le\frac{L^\kappa}{n},
$$

where $\kappa$ depends on $m$ and the fixed group bounds but not $J$.
For a tuple test $f$ supported where the product lies in $[cU,CU]$, put
$a_n=\mathbb E(f\mathbf1_{P=n})$. Fiberwise Cauchy–Schwarz gives

$$
|a_n|^2\le\rho(n)\mathbb E(|f|^2\mathbf1_{P=n}),\qquad
\sum_n|a_n|^2\le\frac{L^\kappa}{cU}\|f\|_2^2.
\tag{I1}
$$

Thus a test can distinguish different orderings with the same product;
only the product-dependent phase is collapsed. Repeated numerical labels
are included by the factorials above.

For integer sequences on intervals of lengths $O(U),O(V)$, Cauchy–Schwarz
and a geometric sum reduce the bilinear phase bound to

$$
U+\sum_{1\le h\ll V}
       \min(U,\|\alpha h\|_{\mathbb R/\mathbb Z}^{-1}).
$$

If $\alpha=u/r+\beta$, $(u,r)=1$, $|\beta|\le r^{-2}$, split the
$h$ range into blocks of diameter at most $r/2$. Distinct phases in a
block are at least $1/(2r)$ apart: the rational difference is at least
$1/r$, and its perturbation is at most $1/(2r)$. The nearest point to
zero costs $O(U)$ and the other distances contribute $O(r\log(2r))$.
There are $O(1+V/r)$ blocks. For $r=1$ the trivial estimate suffices.
Combining this with (I1) yields normalized bilinear norm

$$
O\left(L^\kappa
\left(V^{-1}+r^{-1}+\frac{\log(2r)}U+
                  \frac{r\log(2r)}{UV}\right)^{1/2}\right).
\tag{I2}
$$

Multiplication by $(P_AP_B)^{i\zeta}$ only changes the two tests by
unit-modulus factors. This part has no restriction on $\zeta$.

## The concentrated-cell attack

Partition product logarithms into cells of width $h$ and retain those of
mass at least $\xi$. Let $\mathcal C_Q$ be the primitive characters of
conductor at most $Q$, including conductor one. On a retained cell of
mass $\nu$, the comparison kernel is

$$
\frac{\mathbf1_{D\ {\rm in\ cell}}\mathbf1_{X\ {\rm in\ cell}}}{\nu}
\sum_{\chi\in\mathcal C_Q}\overline{\chi(D)}\chi(X).
\tag{I3}
$$

There are at most $Q^2$ such characters. Two distinct ones have a
nonprincipal quotient on their common modulus, at most $Q^2$. Hold all
but one prime label fixed. The product-cell condition intersects its big
prime group with an interval. Siegel–Walfisz followed by partial summation
on this interval gives an absolute error $O_D(L^{-D})$, with any fixed
$D$, since the prime is at least $\exp(L^c)$. Averaging the other labels
preserves that error, regardless of how short the interval is.

Consequently, on the conditional probability space of a retained cell,
the character Gram matrix has diagonal one and off-diagonal entries
$O_D(\xi^{-1}L^{-D})$. Its norm is at most
$1+O_D(Q^2\xi^{-1}L^{-D})$, and hence at most two with sufficient
precision. The kernel in (I3) is the corresponding frame operator. Passing
from conditional probability to the original probability multiplies both
squared norms by the same $\nu$; it creates no $\xi^{-1}$ norm loss.
Different cells are orthogonal blocks. This proves the norm bound on the
full tuple space, including tests concentrated in a retained cell of mass
close to $\xi$.

For discarded cells, let $E$ be the event that either selected product
falls in one. Its probability is at most $(N_A+N_B)\xi$. The comparison
kernel vanishes there. For arbitrary tests on the two independent tuple
spaces, even if one is concentrated on $E$,

$$
\mathbb E\bigl[\mathbf1_E|f(X_B)g(X_A)|\bigr]
\le\mathbb P(E)^{1/2}\|f\|_2\|g\|_2.
\tag{I4}
$$

The second Cauchy–Schwarz factor is
$\mathbb E|f(X_B)g(X_A)|^2=\|f\|_2^2\|g\|_2^2$ by independence.
The tempting objection that restriction to a small event need not have
small $L^2$ operator norm is correct but does not refute (I4), which is a
bilinear $L^1$ estimate on independent spaces. It would be invalid to
apply this argument to an unrestricted joint test instead of the separated
conditional tests used here.

## Uniform comparison at all additive frequencies

On product dyads $U,V$, put $Z=UV$. Dirichlet approximation with maximum
denominator $\lfloor Z/S\rfloor$ gives

$$
\alpha=u/r+\beta,\quad r\le Z/S,\quad
|\beta|\le r^{-2},\quad |\beta|Z\le2S/r.
\tag{I5}
$$

For $r>Q$, use (I2) on the raw term. Move each comparison kernel onto its
own test and use its norm at most two; its support remains within a fixed
enlargement of the original product dyad. Apply (I1) and (I2) again. Since
$U,V\ge\exp(L^c)$ and $\log(2r)\le L^{d+1}$ eventually, both bounds
are at most a constant times

$$
L^\kappa\bigl(o(L^{-A})+Q^{-1}+L^{d+1}/S\bigr)^{1/2}.
\tag{I6}
$$

For $r\le Q$, all selected products are units modulo $r$. Character
expansion of $e(uv/r)$ on the unit group has coefficient $\ell^1$ norm
at most $\sqrt{\varphi(r)}\le\sqrt Q$, by Parseval and
Cauchy–Schwarz. Its imprimitive characters agree on these products with
their primitive inducing characters, which are present in $\mathcal C_Q$.

For each such character $\psi$, integrating (I3) against $\psi(D)$ gives

$$
\mathbb E_D\mathcal K(D,X)\psi(D)
=\psi(X)+O_D(Q^2\xi^{-1}L^{-D})
\tag{I7}
$$

pointwise for retained $X$. The inducing character supplies the exact
diagonal term, and the other terms are the Gram errors just bounded.
Using (I7) on both products and summing the rational character expansion
costs $O_D(Q^{5/2}\xi^{-1}L^{-D})$.

The remaining scalar function of the product logarithm is
$M(v)=\exp(i\zeta v)e(\beta e^v)$. Its derivative is
$O(L^{C_4}+S)$ on the enlarged dyadic range. Each matched pair of logarithms
differs by less than $h$, so their two sums differ by less than $2h$.
Moreover $\mathbb E_D|\mathcal K(D,X)|\le Q^2$ for fixed retained $X$.
The pointwise error of moving $M$ from the free product to the endpoint
product is therefore $O(Q^4h(S+L^{C_4}))$. This is valid for complex
coefficients and does not use positivity of the kernel.

There are at most $L^{d+1}$ product dyads per selected side. For a desired
total error $L^{-A_0}$, take a dyadic target $B_0>A_0+2(d+1)+10$.
Writing $Q=L^{q_*}$, $S=L^{s_*}$, $h=L^{-h_*}$,
$\xi=L^{-x_*}$, sufficient successive choices are

$$
\begin{aligned}
q_*,s_*&>2(B_0+\kappa+10)+d+1,\\
h_*&>4q_*+\max(s_*,C_4)+B_0+10,\\
x_*&>2B_0+d+1+h_*+10,\\
D&>B_0+x_*+\tfrac52q_*+10.
\end{aligned}
\tag{I8}
$$

They pay respectively for (I6), the log-phase error, the square root of
discarded mass in (I4), and (I7) together with the Gram norm. The absolute
Siegel–Walfisz precision is chosen last in this construction. No choice
uses $J$, $\alpha$, or the individual value of $\zeta$.

## Probe cancellation is an identity followed by an extremal bound

Split big groups into two blocks of at least $c_0T/3$ groups each and
designate $m$ probes per group. Average the last $\ell$ slots in both
endpoint tests; these coordinates occur in no multiplier. Let the
resulting tests be $F',H'$, and decompose $F'$ by the averaging projections
on the first block's probes and $H'$ by those on the second block.
These are orthogonal decompositions because the coordinate projections
commute and are orthogonal.

For a symmetric function on all $M=J+\ell$ coordinates of one group,
all projection components of the same cardinality $j$ have equal squared
norm. The fraction of these components containing all $m$ designated
probes and none of the last $\ell$ slots is

$$
\frac{\binom{M-m-\ell}{j-m}}{\binom Mj}
=\frac{(j)_m(M-j)_\ell}{(M)_{m+\ell}}.
\tag{I9}
$$

It is zero for infeasible cardinalities. If
$M\ge(m+\ell)(m+\ell-1)$, the denominator is at least
$\tfrac12M^{m+\ell}$. Maximizing the remaining ratio in its own
coordinate $u=j/M$ gives

$$
2u^m(1-u)^\ell
\le2\left(\frac m{m+\ell}\right)^m
       \left(\frac\ell{m+\ell}\right)^\ell
\le2\ell^\ell m^{-\ell}=:\theta_m.
\tag{I10}
$$

Resolve the orthogonal decomposition by the vector of cardinalities across
groups. Independent permutations make the retained fraction the product of
(I9), even for tests entangled across groups. The full-probe components
therefore have norms at most $\theta_m^{s_i/2}$ times the original norms.
Choose $m$ with $-(c_0/6)\log\theta_m>E_{\rm id}+3$.

For a component pair, let $U,V$ be its missing probes in the respective
blocks. A freed pair $A,B$ survives only when $A\subseteq U$ and
$B\subseteq V$: otherwise an unshared input coordinate or unshared
target coordinate is mean zero and absent from the multiplier. This uses
the construction's asymmetry: the first kernel uses target labels, the
second input labels.

Conditioning on the labels outside $A\cup B$ leaves precisely an
arbitrary tuple test on $X_B$ and one on $X_A$. They are on independent
spaces; the fixed shared product only changes the real additive frequency
in (I5). Conditional Cauchy–Schwarz averages the error with the original
component norms. When $U,V$ are nonempty,

$$
\sum_{\varnothing\ne A\subseteq U,\,
       \varnothing\ne B\subseteq V}(-1)^{|A|+|B|}=1.
\tag{I11}
$$

The initial negative sign of each comparison consequently cancels that
component pair's raw contribution. The exceptional pairs sum *before*
absolute values to
$R(F_{\rm full},H')+R(F'-F_{\rm full},H_{\rm full})$.
The raw pairing has norm at most one, so (I10) controls this whole sum
without a subset-count loss.

Approximation errors have at most $3^P$ component/free-set choices, where
$P\le mC_0T$: a probe is indicated, missing but retained, or freed.
Taking $A_0>E_{\rm id}+mC_0\log3+10$ absorbs them. The number of
comparison patterns is at most $2^P$, and each coefficient is bounded by
$Q^4\xi^{-2}$. Thus the total coefficient exponent is fixed before
choosing $J$. A larger fixed $J$ can meet the transfer requirement without
changing any kernel precision.

The concentrated-cell, repeated-label, imprimitive-character, and
conditional-tuple attacks therefore leave the claimed ideal comparison
intact. No finite numerical experiment is used to infer its uniformity.
