---
name: number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_a_1
title: "Theorem A.1: in each fixed angular mode the twisted first moment matches its model, so every nonzero mode cancels at scale X^{5/6}/log X"
desc: |
  The claimed angular extension: for each fixed integer l, the first moment
  twisted by (pi/|pi|)^l equals the equally twisted model sum up to
  o(X^{5/6}/log X), so each nonzero mode cancels; the fixed powers G^k with k
  not divisible by 3 and |k| > 1 cancel likewise. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

The notation is that of
[[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_1_1|Theorem 1.1]]:
$\mathcal O=\mathbb Z[\omega]$, primary means congruent to $1$ modulo $3$,
$G$ is the normalized cubic Gauss sum and
$c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$; every sum below runs over the primary
primes $\pi$ of $\mathcal O$ with $N\pi\le X$. For nonzero $z\in\mathbb C$ and
an integer $\ell$ put $\theta_\ell(z)=(z/|z|)^\ell$, evaluated at the primary
generator (p. 42). The manuscript notes that the primary convention lets
every integer $\ell$ occur, with no divisibility condition.

**Theorem A.1.** Fix an integer $\ell$. As $X\to\infty$,
$$
\sum_{N\pi\le X}\theta_\ell(\pi)\bigl(G(\pi)-c_*N(\pi)^{-1/6}\bigr)
=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr)
\qquad\text{(A.1)},
$$
and, when $\ell\ne0$,
$$
\sum_{N\pi\le X}\theta_\ell(\pi)G(\pi)
=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr)
\qquad\text{(A.2)}.
$$

The rate in the $o$-terms may depend on $\ell$, and the manuscript states
that nothing is claimed uniformly in a growing angular parameter. The case
$\ell=0$ of (A.1), with the prime ideal theorem, is Theorem 1.1. For $\ell\ne0$
the manuscript notes that a conjugate pair contributes
$2\operatorname{Re}(\theta_\ell(\pi)G(\pi))$ and asserts no identification with
the rational Kummer summand.

**The fixed-power consequence (A.14)** (Section A.6, p. 51). The manuscript
takes $G(\pi)^3=-\theta_1(\pi)$ and $|G(\pi)|=1$ from the cubic Gauss-sum
identity in Equation (1.8) of Dunn and Radziwiłł, and deduces that for every
fixed integer $k$ with $3\nmid k$,
$$
\sum_{N\pi\le X}G(\pi)^k
=\mathbf 1_{k\in\{-1,1\}}\,\frac65\,c_*\,\frac{X^{5/6}}{\log X}+
o_k\Bigl(\frac{X^{5/6}}{\log X}\Bigr),
$$
since $G(\pi)^{3m+1}=(-1)^m\theta_m(\pi)G(\pi)$ and
$G(\pi)^{3m-1}=(-1)^m\overline{\theta_{-m}(\pi)G(\pi)}$. The manuscript reads
the cases $3\nmid k$, $|k|>1$, as part of Patterson's complementary
conjecture (Equation (1.9) of Dunn and Radziwiłł), and says that the nonzero
multiples $k=3m$ remain outside its conclusion: there
$G(\pi)^k=(-1)^m\theta_m(\pi)$, and the Hecke prime estimates it uses do not
bound those angle sums at scale $X^{5/6}/\log X$.

The release's comparator file
`lean/ComparatorChallenges/PattersonFirstMoment.lean`
states (A.1) as `patterson_angularComparison` and (A.2) as
`patterson_angularCancellation`; (A.14) is not stated there. The card's
Formalization paragraph records what was read of it, and nothing was built
or audited here.

**Source.** OpenAI, *An unconditional first moment for cubic Gauss sums*,
release folder
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026`;
TeX file `build/sections/angular.tex`, label `thm:angular` (lines 19--35), PDF
p. 42, with the definitions at lines 10--16 and the scope remark at lines
37--40; the proof closes at lines 745--793 (PDF pp. 50--51); (A.14),
label `eq:gauss-power-cancellation`, is at lines 812--819 with its derivation
in Section A.6, lines 802--838 (PDF p. 51). Provenance and attestations are on
[[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/_index|the card]].

**Read depth.** Claims checked: Theorem A.1, the definitions it rests on, the
remark on its scope, the closing remark on $\ell\ne0$ (lines 795--800) and
Section A.6 with (A.14) were read clause by clause in the TeX source. The
proof, Appendix A together with the parts of Sections 2--7 it reuses, was
read for its structure only, as summarized below; no step was checked.
Nothing here is independently reviewed.

## Proof pointer

The proof reruns the argument for Theorem 1.1 with the angle carried in the
coefficients, and checks each interface. On ideals prime to $3$, the
function $\Theta_\ell$ given by $\theta_\ell$ of the primary generator is
multiplicative and is a unitary Hecke character of angular order $\ell$ with
conductor dividing $(3)$ (Section A.1). Lemma A.2 records, from Rajan and from
Kaneko and Thorner's restatement of Iwaniec and Kowalski's Theorem 5.13, the
functional equation with gamma factor $\Gamma(z+|\ell|/2)$ for the primitive
character $\Psi$ inducing $\chi\Theta_\ell$ ($\chi$ a finite-order cubic
character) and a bound $x(\log x)^{-M}$ for its prime sums at polylogarithmic
conductor; no exceptional real zero occurs, because a nonzero infinity type
or a nonreal cubic character excludes it.

Section A.2 takes from Dunn and Radziwiłł's Propositions 5.2--5.3 an angular
level Voronoi formula, checking its phases by multiplying their (5.80) by
$G(r)\theta_\ell(r)$; its main term is present only for $\ell=0$. It proves
the angular Type I estimates (Proposition A.4), including a lattice bound
showing that the model's $\theta_\ell$-weighted squarefree sums are small for
$\ell\ne0$; at large heights Lemma A.3 bounds the dual frequency range of the
completed sum and takes the place of Heath-Brown's mean square. Section A.3
extends the exceptional moments of Proposition 4.1 to twisted prime
convolutions $\Theta_\ell\beta$ (Proposition A.5): twisting by $\Theta_\ell$
commutes with Dirichlet convolution, a full-length factor is dualized by the
angular functional equation, and the Gram matrix is unchanged because
$\Theta_\ell$ cancels in each row product.

Section A.4 verifies the Siegel--Walfisz property for the twisted
coefficients by isolating a largest prime and applying Lemma A.2 (Lemma A.6),
and extends dispersion and the bilinear estimates (Proposition A.7). The cube
frequencies now give a main term built from the twisted model polynomial,
which need not vanish for $\ell\ne0$; it still cancels in the corrected
square, because the mixed term keeps a radial weight in the long variable,
so Proposition 3.1 applies unchanged. Section A.5 checks that the
decomposition of Proposition 6.1 splits the phase multiplicatively between
the two variables and assembles (A.1) exactly as in Section 7.5. For
$\ell\ne0$, Lemma A.2 with $\chi$ principal gives
$\sum_{N\pi\le y}\theta_\ell(\pi)\ll y(\log y)^{-M}$ for every fixed $M$, and
Abel summation makes the model's sum $o(X^{5/6}/\log X)$, which with (A.1)
gives (A.2).

## Dependencies

The inputs of
[[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_1_1|Theorem 1.1]],
and in addition, taken at statement level and not checked here: Rajan's
completion, functional equation and zero-free region for Hecke characters of
infinite order (Section 1 and Proposition 1 of the 1998 paper); Kaneko and
Thorner's Theorem 1.2, with the conductor dependence also recorded in Chen,
Park and Swaminathan's Lemma 2.1; Dunn and Radziwiłł's Propositions 5.2--5.3
in their all-integer-index form and the identity in their Equation (1.8).

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem or (A.14).
