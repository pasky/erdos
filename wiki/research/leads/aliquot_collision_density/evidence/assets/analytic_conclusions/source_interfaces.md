# External interfaces used in the analytic review

These are the reviewer's mathematical restatements of the supplied source
statements, not copies of their proofs. Examination date: 2026-10-16 UTC.
The actual reading was limited to the commissioned text excerpts and their
source manifest. No original PDF or live web page was inspected.

## Prime number theorem

Source: Daniel R. Johnston and Andrew Yang, *Some explicit estimates for the
error term in the prime number theorem*, edition dated April 21, 2022,
Introduction, especially the prime-counting definitions and Corollary 1.3.
Canonical supplied source path:
`library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem.md`.

For the number of primes at most the real number x, the supplied corollary is

$$
|\pi(x)-\operatorname{li}(x)|
\le 9.59x(\log x)^{0.515}\exp(-0.8274\sqrt{\log x})\qquad(x\ge2).
$$

Only its consequence $\pi(x)\sim x/\log x$ is consumed. Here the logarithmic
integral has its usual principal-value meaning; for large x it differs from
$\int_2^x dt/\log t$ by a fixed constant. The latter is asymptotic to
$x/\log x$, by differentiating the numerator and denominator in the ratio.
The displayed error divided by $x/\log x$ tends to zero. The introduction also
explicitly states the PNT interface.

Specializations checked in the report: $\pi(x)=o(x)$, and for fixed
$0<a<b$,

$$
\sum_{az<p\le bz}\frac1p\sim\frac{\log(b/a)}{\log z}
\qquad(z\longrightarrow\infty).
$$

The review uses $(a,b)=(5/9,10/11)$. It does not assume a PNT error uniform in
moving a or b. The source's other explicit estimates and their proofs are not
certified by this review.

Reading depth: **claims checked**, against the supplied statement and its
specialization. The original proof and transcription-to-print fidelity were
not checked.

## Mertens product theorem

Source: Terence Tao, *254A, Notes 1: Elementary multiplicative number theory*,
November 23, 2014, Theorem 26,
[the supplied source page](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/).
The supplied manifest dates its retrieval to 2026-10-16, 18:33 UTC. That is
provided provenance, not a retrieval made by this reviewer.

With gamma the Euler--Mascheroni constant, the supplied statement is

$$
m_t:=\prod_{p\le t}(1-1/p)
=\frac{e^{-\gamma}+O(1/\log t)}{\log t}
\qquad(t\longrightarrow\infty).
$$

Specializations: $m_t\to0$; $m_{100z}\sim e^{-\gamma}/\log z$; and
$\log(1/m_y)=\log\log y+\gamma+o(1)$, which bounds the prime reciprocal
error sum in Theorem A. Each is derived in the report.

Reading depth: **claims checked**, against the supplied theorem statement.
The proof is absent from the excerpt. This source is an expository statement,
not an inspected original Mertens paper. The review neither reconstructs nor
claims primary-proof verification of Mertens' theorem.

## Uniform finite-target theorem

Source: Pollack, Pomerance and Thompson, *Divisor-sum fibers*,
2017 author manuscript, Theorem 1.2, published in *Mathematika* in 2018.
Canonical supplied source path:
`library/arithmetic_functions/pollack_2018_divisor_sum_fibers/pollack_2018_divisor_sum_fibers.md`.

Let $h(x)$ be any fixed function tending to zero. For the proper-divisor sum
$s$, there is a quantity $u_h(x)\to0$ such that for all sufficiently large x,
and every set B of positive integers satisfying
$|B|\le x^{1/2+h(x)}$,

$$
\#\{n\le x:s(n)\in B\}\le u_h(x)x.
$$

This rephrases the supplied uniform little-o statement; it supplies no
particular rate for $u_h$, and it does not claim uniformity over choices of
h. Adding zero to the allowed target universe changes the count by at most
one, since $s^{-1}(\{0\})=\{1\}$.

Reading depth: **claims checked**, at this exact interface. The proof is not
included in the commissioned reading. The theorem is used only to check the
comparison with Theorem B(4), never to prove Theorem B or the target problem.

## Local supporting material

The frozen subject comes from
`wiki/research/leads/aliquot_collision_density/_index.md`, from Target and
conventions through the final semiprime paragraph preceding Exact census.
The abstract countermodel comes from
`wiki/problems/arithmetic_functions/E0955/_index.md`, Exact scope of the
arithmetic reduction. Both were frozen on 2026-10-16 and read only as supplied
extractions. Their retained snapshots are `subject.md` and `countermodel.md`
beside this file. The report reconstructs their supporting arithmetic and the
countermodel; no native L-claim is taken as an established premise.

No source in this packet establishes a literature-wide assertion that condition
(D) is, or is not, known to be equivalent to the target problem. The supplied
mathematics proves the sufficient implication only. The sentence about what is
known retains this explicit source-coverage limitation.
