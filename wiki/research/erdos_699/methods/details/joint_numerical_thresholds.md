---
name: research/erdos_699/methods/details/joint_numerical_thresholds
title: "Erdős 699: numerical heights for joint cofactor clauses"
desc: "Finite integral constants and uniform coefficient-gcd bounds give numerical starting heights for the positive-part Padé inequalities, including zero actual product gap."
created: 2026-09-22T00:00:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: numerical heights for joint cofactor clauses

***

The [unequal-block argument](off_diagonal_pade.md)
gives rational necessary inequalities

$$
\sum_p(g_p+b_pe_p)_+\ge R.\tag{1}
$$

The [numerical checker](../../computations/erdos_699_off_diagonal_explicit_clauses.py)
supplies an explicit height beyond which each such inequality holds.
Its input coefficient-gcd bound must be valid for both adjacent Padé
rectangles at every integer $m\ge m_0$.

Write the seed as $aP-bQ=D_0>0$, put $T=aP$, and use positive integer
directions $(A,B,C)$, with $H=A+B+C$. The adjacent rectangles are

$$ (Am+\varepsilon,\;Bm-1-\varepsilon,\;Cm+\varepsilon),
\qquad\varepsilon\in\{0,1\}.$$

Let $C_0,K_0$ be the two decay rates, including a verified logarithmic
gcd rate $\ell$. Let $M_Q,M_E$ be the maxima of the corresponding base
integrands, as defined in the
[finite-constant note](off_diagonal_numerical_thresholds.md).
For $m\ge2$, set

$$
F=\max\left\{B,\frac{(H+1)B^2}{AC}\right\},\qquad\gamma=2/B.
$$

Removing the $(m-\gamma)$-th power of the base integrand leaves every
exponent nonnegative for both rectangles. The multinomial theorem then
gives the explicit integral estimates

$$|Q|\le FmM_Q^{-\gamma}e^{qm},\qquad
|E|\le FmM_E^{-\gamma}e^{em}.\tag{2}$$

Suppose $X,Y$ are degree-$d$ products of factors in $[h,h+s]$, and
$|X-Y|\le D$. Here $D\ge0$ is a bound on the actual product gap,
distinct from the positive seed gap $D_0$. Let $t>0$ be the rational
block parameter retained with (1), and put $x=\log h$,
$m=\lfloor tx\rfloor$.

If (1) fails, the logarithmic cost of clearing residual prime-power
denominators is less than $Rx$. This follows from the outward rounding
$g_p>tL_{s(p)}a_p\log p-b_p$, where $a_p$ is the seed exponent and
$L_0=A+B$, $L_1=B+C$. Therefore the exact nonzero-integer argument,
together with (2), gives

$$1\le tx\left(A_1e^{C_0}e^{-\eta_1x}
             +2^d A_2e^{K_0}e^{-\eta_2x}\right),\tag{3}$$

where

$$A_1=DTF M_Q^{-\gamma},\qquad
A_2=\frac{D_0^3}{T}F M_E^{-\gamma},$$
$$
\eta_1=tC_0-R,\qquad\eta_2=tK_0-R-d.
$$

The input clause has positive margins; these remain positive whenever
the coefficient-gcd rate is increased. Crucially, $X=Y$ is allowed:
the first term disappears, while the seed determinant still ensures
that one of the two adjacent integer combinations is nonzero.

The checker finds an integer $K$ such that, at $x=K\log10$,

$$
tx\ge m_0+1,\qquad x\ge\log(s+1),
$$

and each nonzero term in (3) is strictly below $1/2$. It verifies
$\eta_i x>1$ and the directed logarithmic comparisons

$$
\log(2tA_1)+C_0+\log x-\eta_1x<0,
$$
$$
\log(2^{d+1}tA_2)+K_0+\log x-\eta_2x<0.
$$

Each left side decreases at every larger $x$, so the contradiction holds
for all $h\ge10^K$. No asymptotic constant remains unevaluated.

The checker also accepts an independently certified weakening
$R\mapsto R-\delta$, with $0\le\delta<R$. This changes neither the
intercepts nor the sign branches, and permits a weaker gcd rate when
the resulting two decay margins are positive. The whole-index proof
must separately verify that its exact linear contradictions survive
this weakening. Keeping $R-\delta>0$ is necessary for a branch tree
which omits the empty positive-part mask.

## The 790 index-nine clauses

The [index-nine source calculation](../../computations/erdos_699_index_9_joint_numerical.py)
applies this argument to all 790 joint clauses used by the retained
proof. The [exact weakening certificate](../../computations/erdos_699_nine_source_weakening.py)
assigns a separate positive $\delta$ to every source and checks that,
at each of the 23,973 Farkas leaves, the combined cost is at most half
the available margin. The resulting polynomial height requirement is
$h\ge10^{2756506683}$.

For each clause the numerical source calculation chooses a uniform gcd
rate exceeding

$$\max\left\{\ell_{\rm old}/2,
              \ell_{\rm old}-\frac{\delta}{2t}\right\}.$$

The two new decay margins therefore exceed half the weakening budget,
in addition to the old strict rounding margin. The sharper uniform
gcd bounds use the
Broadbent–Kadiri–Lumley–Ng–Wilk source
and [Johnston–Yang source](../../../../../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/_index.md).
Finite-range prime estimates are patched with global estimates before
being used for an infinite tail.

The [compressed numerical certificates](../../computations/erdos_699_index_9_joint_numerical.json.gz)
give

$$
h\ge10^{27\,829\,083\,464\,213}\tag{4}
$$

as a common sufficient height for all 790 weakened joint clauses.
The maximizing source is `source_0406`, with directions $(32,25,45)$,
$t=1352650/866762331$, and numerical gcd starting index $m_0=10^{11}$.
The calculation retains 739 uniform gcd certificates and every directed
finite-constant comparison. This is the joint-source contribution to
the stopping bound; the initial pair and ordinary product sources are
checked separately by the
[index-nine numerical-tail checker](../../computations/erdos_699_index_9_numerical_tail.py).
