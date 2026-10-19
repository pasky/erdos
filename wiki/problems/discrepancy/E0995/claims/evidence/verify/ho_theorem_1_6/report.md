---
name: problems/discrepancy/E0995/claims/evidence/verify/ho_theorem_1_6/report
title: "Ho's p=2 large-partial-sum theorem: independent examination"
desc: >-
  Independent attempted refutation of Boon Suan Ho's Theorem 1.6 at p=2,
  including its almost-everywhere consequence for the example in Problem 995.
created: 2026-10-15T11:43:59Z
updated: 2026-10-15T11:43:59Z
---

# Ho's p=2 large-partial-sum theorem: independent examination

***

## Subject and independence

**Mathematical verdict: refutation-failed.** The frozen proof of Theorem 1.6
at $p=2$, including the stated consequence for the example question in
Problem 995, survives the attacks below. This is a whole-proof examination
of that specialization, not an assertion about every $p$ or the rest of the
paper. A nonconsumed transcription discrepancy is recorded under Source
fidelity. No essential missing lemma or repair was needed for the assigned
conclusion.

The reviewer is an independent mathematical examiner; the disclosed model is
gpt-6-astra. The examination date is **2026-10-15 UTC**. The mathematical
subject was frozen on **2026-10-15 at 05:52:55.296610 UTC**. Its canonical
locations are:

- wiki/problems/discrepancy/E0995/_index.md, Statement;
- wiki/problems/discrepancy/E0995/claims/2026_04_20_ho.md, the supplied
  mathematical statement, consequence, Covers and Depends on passages;
- library/analysis/ho_2026_counterexamples_lacunary_dilates_via_dyadic_spike/ho_2026_counterexamples_lacunary_dilates_via_dyadic_spike.md,
  Notation, Theorem 1.6, Sections 2–4, and the proof of Theorem 1.6 in
  Section 7.

The source is Boon Suan Ho, *Counterexamples for lacunary dilates via dyadic
spike blocks*, arXiv:2604.18535v2. The source mathematics and construction are
Ho's. The independent examination and derivations in this report are
attributed to Plasma AI.

The exact assessed text is retained in the
[catalog extract](../../assets/ho_review_subject/catalog_statement.md.txt),
[claim extract](../../assets/ho_review_subject/claim_math.md.txt), and
[source extract](../../assets/ho_review_subject/source_math.md.txt).
The [subject provenance](../../assets/ho_review_subject/provenance.json)
records their canonical origins, exact excerpt boundaries, freeze time, and
omission marker. These snapshots identify what was examined even if a
canonical page subsequently changes. The report covers no later correction.

This examination began in a fresh context, separate from authorship and
collaboration on the subject. It received the commission, the permitted
operating rules, and a neutral extraction prepared separately from the
reviewer. It received no author's private working material, earlier review,
sibling verdict, or mathematical steering. The configured isolation was
blind and sealed, with synchronization disabled. Subscription checks after
startup and before mathematical reading returned empty tables. Those checks
support isolation; the additional factual basis is the restricted reading
described here, not a claim that configuration alone proves independence.

All three extracts were read in full. Their sizes and identities were
compared with the neutral manifest before reading and at package preparation;
the assessed bytes and retained copies agree. The permitted operating files
were checked against their separately supplied manifest before use. The
operating reading comprised the repository instructions, README, the
relevant Claims, Evidence, Tiers, naming and problem-claim parts of
docs/anatomy.md, all of docs/verification.md and
campaign/guides/verification.md, campaign/AGENTS.md, the Reading section of
campaign/guides/research.md, docs/evidence.md, docs/approach_vetting.md,
docs/math_authoring.md, docs/weaving.md, and the permitted operational
instructions. Links and examples in those documents were not followed into
additional mathematical material.

The only additional mathematical reading was the expressly permitted print
comparison against the matching PDF passages, detailed below. No canonical
source card or full transcription, ledger, history, other review, message
channel, external repository, or web search was read. There was **no
excluded exposure**. The print comparison did not expose neighboring proof
sections or Remark 7.1. To locate boundary crops, the PDF text layer on the
permitted page numbers was processed for known heading and proof-end
markers; only their coordinates were displayed. Neighboring text was not
displayed or retained, and only the permitted passage images were viewed.

The mathematical evidence is the derivation and attempted refutations in this
report. No numerical experiment, executable theorem check, formal proof, or
cached success output is used. There is consequently no computational
reproduction leg to run. The retained text suffices to repeat the mathematical
assessment from an ordinary clone.

## Restatement and conventions

Equip $\mathbb T=\mathbb R/\mathbb Z$ with normalized Lebesgue measure.
There are a real measurable representative $f$ on $\mathbb T$, with
$\int f=0$ and $\int |f|^2<\infty$, a fixed sequence of positive integers
$n_1<n_2<\cdots$ with $n_{j+1}/n_j\geq2$, and a measurable set
$X\subseteq\mathbb T$ of measure one such that

$$
\forall x\in X\ \forall\varepsilon>0,\qquad
\limsup_{N\to\infty}
\frac{\sum_{j=1}^{N}f(n_jx)}
     {N(\log N)^{1/2-\varepsilon}}=+\infty.
$$

The same $f$, sequence, and full-measure set work for every $\varepsilon$.
The numerator is signed, not replaced by its absolute value. $N$ counts
selected summands; it is neither the largest selected exponent nor the
largest dilation. Logarithms are natural, and limits concern sufficiently
large integer $N$, so the initial undefined logarithmic expressions do not
enter.

Taking $\varepsilon=1/4$ contradicts the proposed
$o(N\sqrt{\log\log N})$ estimate almost everywhere for this pair. This
answers the example question in the supplied catalog statement. It does not
give an optimal general growth estimate for its open-ended first sentence.
Although the catalog statement does not require mean zero, a mean-zero
counterexample lies within its class.

The intermediate depth, layer, digit, exponent, spacing and count parameters
used below are integers. The source's finite sums and digit windows require
these discrete types. The actual stage construction realizes them:
$\ell,L,T,U,D,M$ are chosen as integers and $d$ can be chosen by the ceiling
of a base-two logarithm. We do not rely on a claim that the auxiliary
digit-window lemmas hold for arbitrary real depths or offsets.

## Weakest steps and independent derivations

### 1. A rare central hit must survive every negative term

Write $\rho=2^{-d}$, using $\rho$ to distinguish the spike probability
from the theorem's exponent $p=2$. On the interval of length $\rho$ the
spike is $h=\sqrt{2^d-1}$; elsewhere it is $-g=-1/\sqrt{2^d-1}$.
Directly,

$$
\rho h=(1-\rho)g,\qquad
\rho h^2+(1-\rho)g^2=1.
$$

Thus the spike is centered with variance one. Apart from dyadic rationals,
$\phi_d(2^v x)$ is determined by the bits in
$[v+1,v+d]$. The probability of any prescribed values of finitely many
distinct binary digits is $2^{-r}$, where $r$ is their number: refine to the
partition by the largest digit and count the intervals. This proves the
finite independence used here for all window positions, rather than
inferring it from numerical samples.

For the source's Fourier argument, integration of the interval indicator
gives, at nonzero integer frequency $r$,

$$
\widehat{\mathbf1_{[0,2^{-d})}}(r)
=\frac{1-e^{-2\pi i r2^{-d}}}{2\pi i r}.
$$

It vanishes when $2^d$ divides $r$. Dilation by $2^v$ places the nonzero
coefficients only at frequencies with valuation in $[v,v+d-1]$.
The zero coefficient is zero. Disjoint such bands therefore give
orthogonality by Parseval, as used in Lemma 3.1 and Proposition 4.3.

Put $\alpha=\sqrt{\lambda/L}$ and
$F=\alpha\sum_{q=1}^L\phi_d(2^{U+qD}\,\cdot)$.
The within-block windows and bands are disjoint for $D\geq d+2$.
Consequently $\int F=0$ and $\|F\|_2^2=\lambda$. Moreover

$$
\sqrt{\lambda L}\,g
\leq \sqrt{\frac{2\lambda L}{2^d}}
\leq\frac{\lambda}{4\sqrt2 B}.
$$

Here $2^d\geq64B^2L/\lambda$ and $2^d-1\geq2^{d-1}$ were used.
In particular the source's absolute lower-floor constant can be taken to be
$C_3=1$, uniformly in all stage parameters.

Expanding a trial sum gives weights

$$
w_h=\#\{(q,r):1\leq q\leq L,\ 1\leq r\leq\ell,\ q+r=h\}.
$$

Counting the pairs gives $\sum_h w_h=L\ell$.
For $\ell+1\leq h\leq L+1$, each $r\in[1,\ell]$ gives the allowed
$q=h-r$, so $w_h=\ell$. This verifies the central range, including its
two endpoints.

The deliberately hostile configuration is exactly one central hit and
every other spike in the trial at its negative value. Its weighted value is

$$
\alpha\{\ell h-(L\ell-\ell)g\}.
$$

Any additional hit increases this value. Even discarding the positive
$\alpha\ell g$ gives the source's lower estimate

$$
\sum_{r=1}^{\ell}F(2^{M+rD}x)
\geq \ell\{\alpha h-\sqrt{\lambda L}\,g\}
\geq (4\sqrt2-1)B\ell
>2B\ell.
$$

The last bound uses $\alpha h\geq4\sqrt2 B$ and
$\lambda/(4\sqrt2 B)\leq B$. Thus the attempted cancellation by all
noncentral terms fails with an absolute margin.

There are $n_c=L-\ell+1$ independent central windows.
For $1\leq\ell\leq L/8$ we have $7L/8\leq n_c\leq L$, and

$$
\frac{\lambda}{128B^2L}<\rho\leq\frac{\lambda}{64B^2L}.
$$

Let $u=n_c\rho\leq1/64$. Then
$1-(1-\rho)^{n_c}\geq1-e^{-u}\geq u/2$.
It follows that the success probability is at least
$c_0\lambda/B^2$ with the single absolute choice
$c_0=7/2048$. No constant deteriorates as $L$, the depth, the offset,
or the stage number grows.

The local statement has no admissible integer trial when $L<8$; that case
is vacuous. Actual stages have $\ell\geq20$ and $L\geq160$.
An allowed negative $M$ causes no noninteger dilation: $M+D\geq0$
implies $M+rD\geq0$, and
$U+M+hD\geq U+D\geq0$ for $h\geq2$.

### 2. Independence must yield the same function at all selected dilations

There are two distinct independence questions.

The undilated block $F_k$ uses the bit windows

$$
J_{k,q}=[U_k+qD_k+1,\ U_k+qD_k+d_k],
\qquad 1\leq q\leq L_k.
$$

Their largest coordinate is $V_k^{\max}+1$. Since
$U_k=V_{k-1}^{\max}+1$, the first coordinate of the new block is
$V_{k-1}^{\max}+D_k+2$, beyond every coordinate of the old blocks.
Within a block consecutive windows are disjoint because $D_k=d_k+2$.
Thus the $F_k$ are mutually independent centered variables. This conclusion
uses the actual bit sets; disjoint Fourier supports alone would not imply
independence.

For a trial, all the relevant translated spike windows, including more than
the central ones, lie between

$$
U_k+M_{k,t}+2D_k+1
\quad\hbox{and}\quad
H_{k,t}=U_k+M_{k,t}+(L_k+\ell_{k,t})D_k+d_k.
$$

By (4.11), the first such coordinate of the next trial is
$H_{k,t}+2D_k+3$, strictly beyond this range.
The second inequality in (4.10) places the first range of a new stage
beyond $\Omega_{k-1}$, and (4.14) bounds all previous ranges.
Hence the central-hit events for distinct trials are mutually independent.
No independence between a block and its success event, or between an event
and all the other blocks, is asserted or needed.

Now use the source's explicit choice $a_k=2^{-k-2}$ at $p=2$, so
$\lambda_k=a_k$ and $\sum_k\lambda_k=1/4$.
The disjoint Fourier bands give, for every finite tail,

$$
\left\|\sum_{k=m}^{n}F_k\right\|_2^2
=\sum_{k=m}^{n}a_k.
$$

Completeness gives an $L^2$ limit, with integral zero by continuity of the
integral. The permitted convergence theorem for independent centered
variables with summable variances gives almost-sure convergence of the same
series. The almost-sure and $L^2$ limits agree almost everywhere, since
$L^2$ convergence implies convergence in probability and that limit is
unique.

Here is an explicit representative and exceptional-set reconstruction.
Let $E$ be the measurable full-measure set on which the series converges to
a finite value, with the dyadic rationals removed. Define $f$ to be that
sum on $E$ and zero on its complement, as a function on $\mathbb T$.
It is real, measurable, periodic when pulled back to $\mathbb R$, belongs
to $L^2$, and has integral zero.
With the source's finite constant

$$
\mu=C_3\sum_i\frac{a_i}{B_i},
$$

every finite block sum is at least $-\mu$.
Removing any one block leaves a convergent series on $E$, and each of
its finite sums has the same lower bound. Therefore, simultaneously for
all $k$ and all $y\in E$,

$$
f(y)\geq-\mu,\qquad f(y)-F_k(y)\geq-\mu.
$$

For a positive integer $n$, the map $y\mapsto ny$ on $\mathbb T$
preserves Lebesgue measure, by splitting $[0,1)$ into its $n$ inverse
branches and changing variables. In particular it pulls back null sets to
null sets. Thus

$$
X_0=(\mathbb T\setminus D_{\rm dyad})
\cap\bigcap_{j\geq1}\{x:n_jx\in E\}
$$

has measure one. On $X_0$ the preceding bounds apply at every selected
dilation and for every omitted block. This is a countable intersection;
there is no uncountable exceptional-set deletion hidden here.
Changing the representative of the $L^2$ class would likewise change none
of these sums outside a countable union of inverse images of a null set.

At a successful trial endpoint $N=P+\ell$, the preceding $P$ summands,
the current block on the $\ell$ new summands, and the remaining blocks on
those new summands give exactly

$$
\sum_{j\leq N}f(n_jx)
\geq -\mu P+2B_k\ell-\mu\ell
=2B_k\ell-\mu N.
$$

The ordered exponent construction ensures that these are precisely the
first $N$ summands, without an intervening selection from another trial.
Since $P\leq\ell/20$, division by $N$ yields at least
$2B_k/(1+1/20)-\mu\geq B_k-\mu$.
This lower bound controls the signed sum regardless of dependence among
its different contributions.

### 3. Large trial counts must not destroy the logarithmic gain

The most dangerous interaction is between the number of trials needed for
almost-sure success and the final number of selected terms. Both increase
when $B_k$ increases. A bound involving the much larger selected
exponents would not suffice.

At the beginning of a fixed stage let $P=P_{k,1}$, already determined.
Because $P_{k,t}$ is an integer and $\eta^{-1}=20$, the ceiling in
(4.3) is redundant:

$$
\ell_{k,t}=20(P_{k,t}+1),\qquad
P_{k,t+1}+1=21(P_{k,t}+1).
$$

Consequently the actual count satisfies the exact identity

$$
N_k^*+1=(P+1)21^{T_k}.
$$

Large gaps in the exponent sequence add no selected terms.
With $A_k=\Gamma\log(k+1)/a_k$ and
$T_k=\lceil A_kB_k^2\rceil$,

$$
\log N_k^*
\leq\log(P+1)+(A_kB_k^2+1)\log21
\leq K_k B_k^2\quad(B_k\geq100),
$$

where one possible choice is

$$
K_k=A_k\log21+
\frac{\log(P+1)+\log21}{100^2}.
$$

$K_k$ is finite and independent of the proposed value of $B_k$.
It may depend on $k$ and previous stages; the proof needs no uniform
bound on that dependence.

There is also a future-independent bound on the floor. For any allowed
future choices $B_i\geq100$, both $\mu$ and the source's
$\overline\mu_k(B)$ are at most

$$
M_*=\frac{C_3}{100}\sum_i a_i=\frac{C_3}{400}.
$$

In particular this bound does not assume that future stages already exist.
It follows directly from the three sums in (7.4), with
$\lambda_i=a_i$ and $B\geq100$.

Set $\delta_k=1/(4(k+2))$ and $\beta_k=1/2-\delta_k>0$.
For $B\geq\max(100,2M_*)$ the preceding estimates imply

$$
\frac{B-\overline\mu_k(B)}{(\log N_k^*)^{\beta_k}}
\geq \frac{B^{2\delta_k}}{2K_k^{\beta_k}}
\longrightarrow+\infty
\quad\hbox{as }B\to\infty.
$$

This bound holds despite all jumps of the ceiling in $T_k$.
Thus a finite $B_k$ satisfying (7.5) exists at every fixed stage.
For example, choosing an integer beyond the displayed bound is legitimate;
no observation of $x$ or of trial successes enters the choice.

After such a choice, $T_k$ is a finite positive integer, every recursive
count and length is finite, and so is $L_k$.
Writing $R=64B_k^2L_k/a_k$, the integer
$d_k=\lceil\log_2 R\rceil$ satisfies $R\leq2^{d_k}<2R$.
Then $D_k=d_k+2$ and $U_k$ are integers.
The two strict lower bounds on $M_{k,1}$ concern only finite integers, so
an integer satisfying both exists. The remaining offsets and bookkeeping
quantities are finite. This verifies the recursion without assuming its
termination or its eventual conclusion.

The selected exponents are positive and strictly increasing. The first
one exceeds $m_0^{\rm last}=0$; within a trial the increment is $D_k$;
between trials (4.11) places the next first exponent strictly after the
previous last; and (4.10) does the same between stages.
Their powers of two are therefore positive integers with successive ratio
at least two.

The independent-trial probability estimate now gives

$$
\Pr(S_k^c)
\leq\exp\!\left(-c_0T_k\frac{a_k}{B_k^2}\right)
\leq(k+1)^{-8},
$$

since $\Gamma\geq8/c_0$. First Borel–Cantelli gives a measure-one
event $X_1$ on which every sufficiently large stage has a successful
trial. This implication needs no independence between different stages.
Let $X=X_0\cap X_1$.

For $x\in X$, choose a successful trial in each sufficiently large stage
and denote its endpoint by $N_k(x)$. These endpoints are strictly
increasing between stages and at least $20$, so $\log N_k(x)>1$.
The endpoint lower bound and (7.5) give

$$
\frac{\sum_{j\leq N_k(x)}f(n_jx)}
     {N_k(x)(\log N_k(x))^{\beta_k}}\geq k.
$$

In making the denominator comparison with $N_k^*$, the numerator is
positive: (7.5) already implies
$B_k-\overline\mu_k(B_k)>0$, and
$\mu\leq\overline\mu_k(B_k)$.
Thus the direction of that comparison is justified.

Now fix any $\varepsilon>0$, after fixing $x\in X$.
Eventually $\delta_k<\varepsilon$, so
$(\log N_k(x))^{1/2-\varepsilon}
\leq(\log N_k(x))^{\beta_k}$.
The same positive sums and the same endpoints give a ratio at least $k$.
This argument also covers $\varepsilon\geq1/2$. It proves the claimed
positive infinite limsup on one $X$ for every $\varepsilon$, without
intersecting an uncountable collection of separately obtained full-measure
sets.

For the catalog implication, at $\varepsilon=1/4$ put $t=\log\log N$.
Then

$$
\frac{(\log N)^{1/4}}{\sqrt{\log\log N}}
=\frac{e^{t/4}}{\sqrt t}\longrightarrow+\infty.
$$

If the catalog-normalized sums tended to zero at any $x\in X$, multiplying
them by $\sqrt{\log\log N}/(\log N)^{1/4}$ would make the
theorem-normalized sums tend to zero there, contradicting their infinite
limsup. Defining the restriction of the periodic representative on $[0,1]$
gives exactly $f(\{\alpha n_j\})=f(n_j\alpha)$.
Integer translation of $\alpha$ leaves these values unchanged, and
countably many translates of a null subset of $[0,1)$ are null in
$\mathbb R$. The consequence therefore has the catalog's almost-everywhere
meaning.

## Strongest attack and attempted refutations

The strongest attack was to make the stage selection circular or quantitatively
impossible. Increasing $B_k$ increases $T_k$, which makes the trial
lengths and the end count grow exponentially. At the same time, the
denominator in (7.5) and an apparently unknown future floor both depend on
the construction. Ignoring either dependence could falsely manufacture the
claimed gain.

This attack fails for the precise reasons in the third derivation:
the count is exactly $(P+1)21^{T_k}-1$, its logarithm is bounded by
$K_kB_k^2$ with $K_k$ independent of the proposed $B_k$, and the future
floor is bounded before future choices by $C_3/400$. The resulting lower
bound grows as $B_k^{2\delta_k}$, with strictly positive exponent at
each fixed stage. Although that exponent tends to zero with $k$, no
uniform choice in $k$ is being claimed: the recursive choices occur after
the previous stages are fixed.

Other concrete attacks were:

- Put every spike except one central hit at its most negative value.
  The exact weighted value in the first derivation still exceeds the
  required positive signal; the lower floors cannot cancel it.
- Look for a shared bit at adjacent block and trial boundaries, or confuse
  orthogonality with independence. The explicit coordinate comparisons in
  the second derivation rule out those overlaps for the families actually
  required to be independent.
- Let convergence fail at a selected dilation, or change the representative
  on a null set. The explicit countable pullback defining $X_0$ handles
  both possibilities.
- Replace signed sums by absolute values, or reverse a denominator
  comparison with a negative numerator. Positivity is obtained before the
  comparison, and no absolute-value conclusion is substituted.
- Let the successful endpoints depend on $\varepsilon$, creating
  incompatible exceptional sets. $X$ and the stage endpoints are fixed
  first; decreasing the logarithmic exponent proves every later
  $\varepsilon$ assertion on the same set.
- Try to infer the catalog conclusion from a large value in the wrong
  normalization. The exact logarithmic ratio above tends to infinity in
  the catalog's count variable $N$.

These are mathematical attacks on arbitrary legal stages and on the
infinite construction, not tests of finitely many favorable parameter values.

The explicit constants, exact count recurrence, parameter types, and common
exceptional set above are routine reconstructions of inferences in the
frozen proof. They do not replace a failed step with a different proof.
The source supplies the particular sequence $a_k=2^{-k-2}$ used here.
Summability alone would not imply $a_k\leq1$ for an arbitrary positive
sequence; using the already supplied sequence satisfies that required bound.
No extra hypothesis has been added to the theorem.

## Premises and reading depth

The dependency census was checked against the frozen statement, proof, and
consequence passages on **2026-10-15 UTC**. It contains **no native
L-claim premise or quoted L-claim definition**. This follows from the
actual argument, not merely the claim page's Depends on sentence.
The commissioned dependency channel therefore has no ledger rows to read.
No live ledger was accessed, no pending native grade is assumed, and no
native dependency acceptance order is needed.

All source entries below refer to Ho's v2 and to the retained source
extract. “Proof verified” means verified in this examination at the
specified scope; it does not assert a separate accepted grade for those
auxiliary results.

| Source interface | Required specialization and use | Actual reading and assessment |
| --- | --- | --- |
| (2.1), Lemma 2.1, pp.7–8 | Integer depths and nonnegative integer shifts; centered unit-variance spikes, disjoint-bit independence, and Fourier valuation support. | Text and print read; proof verified for these interfaces in derivations 1–2. |
| Lemma 3.1, (3.4)–(3.5), pp.9–10 | Legal block parameters; mean zero, squared norm $\lambda$, and an absolute lower floor $-C_3\lambda/B$. | Text and print read; these clauses and their proofs verified. Fourier-tail clauses are outside the consumed scope. |
| Lemmas 3.2–3.3, pp.10–11 | Only $p=2$: the norm identity and the Hilbert-space Cauchy criterion for independent centered blocks. | Text and print read; the $p=2$ arguments verified. The $p>2$ Rosenthal arguments are context, not consumed premises. |
| (3.10)–(3.14), Definition 3.4, Lemma 3.5, pp.11–12 | Integer trials of length at most $L/8$; uniform probability $c_0\lambda/B^2$ and signed signal $2B\ell$. | Text and print read; multiplicities, range, probability, and signal verified in derivation 1. |
| (4.1)–(4.16), Lemma 4.1, pp.12–14 | Finite integer stage choices, ordered exponent selections, and the count of actual summands. | Text and print read; recursion and existence of each choice verified in derivation 3. |
| Lemma 4.2, pp.14–15 | The actual central-hit events; independent trial windows and the stage failure bound. | Text and print read; digit-coordinate argument and probability composition verified in derivations 2–3. |
| Proposition 4.3, pp.15–16 | $p=2$, $\sum\lambda_k<\infty$, and part (ii); convergence, floors, selected-dilation endpoint estimates, and eventually successful stages. | Text and print read; all consumed deductions verified. Part (i) is not needed for Theorem 1.6. |
| Section 7, pp.21–23; Theorem 1.6, p.4 | $p=2$, $a_k=2^{-k-2}$; stage selection, simultaneous positive limsup, and the E995 example consequence. | All supplied text and matching print passages read; the complete assigned argument verified under the stated foundations. |

The exact external interfaces are:

- **Lebesgue measure and probability foundations.** Measurability of finite
  digit events and countable limits, probabilities of binary cylinders,
  countable unions of null sets, and measure preservation by integer circle
  dilations. The specific cylinder and inverse-branch applications are
  derived above.
- **Hilbert-space and Fourier foundations.** Parseval/orthogonality,
  completeness of $L^2$, continuity of the integral on this probability
  space, and uniqueness of limits in probability. They turn the disjoint
  bands and summable squared norms into the stated $L^2$ limit.
- **Convergence of independent square-summable series.** Independent
  centered real variables with finite variances whose sum is finite have
  an almost-sure finite series sum. Here the variables are exactly $F_k$;
  their independence, centering and variance $a_k$ have been checked.
- **First Borel–Cantelli.** If $\sum_k\Pr(A_k)<\infty$, almost surely only
  finitely many $A_k$ occur. Here $A_k=S_k^c$ with
  $\Pr(A_k)\leq(k+1)^{-8}$. Second Borel–Cantelli appears in the source's
  unused Proposition 4.3(i), but is not a premise of the assigned route.

These are standard foundations expressly permitted by the commission.
No additional literature was read to establish them, and no independent
reconstruction of their general proofs is claimed. There is no Rosenthal
interface at $p=2$. Lemma 2.2, the Fourier-tail conclusions of Lemma 3.1,
and the auxiliary thresholds $Q_k$ do not enter the assigned conclusion.
The source's reference to Section 1.2 for interpretation of parameters
requires no missing theorem: their mathematical definitions are present in
the supplied notation and construction.

## Checklist

### Erdos-specific checklist

| Item | Verdict and reason |
| --- | --- |
| Quantifiers and scope | No failure found. One fixed $f$, sequence and measure-one $X$ give every positive $\varepsilon$ and the positive limsup. Initial logarithm exceptions and dyadic null sets are explicit. |
| Circularity | No failure found. Every finite stage is constructible from prior finite data; the bound on future negative contributions does not assume future success or the theorem. |
| Model and convention changes | No failure found. Binary-cylinder events describe the actual circle functions off a null set. Measure-preserving pullbacks and periodic representatives justify all transfers to dilated sums and fractional parts. |
| Finite and statistical overreach | No failure found. General counting and probability identities, rather than samples or finite searches, prove the required bounds. The relevant independence is established by disjoint coordinates. |
| Uniformity | No failure found. $c_0,C_3$ are absolute. $K_k$ may depend on the fixed stage and its past but not the proposed $B_k$. All series-limit and null-set uses are justified. |
| Extremal conclusions | No failure found in the positive infinite limsup, checked in the actual selected-term count $N$. No optimum, sharp constant, or attainment assertion is assigned. |
| Consequences and composition | No failure found. The block, probability, recursion, floor and exceptional-set interfaces compose at their stated strengths. The E995 logarithmic comparison is checked separately. |
| Computation | Inapplicable as a mathematical mode: there is no numerical, enumerative or executable theorem check. Exact arithmetic and general inequalities are exposed in the report. Print rendering is source inspection, not a mathematical computation. |
| Reproduction | The exact three textual inputs and derivations are retained. No mathematical rerun, pass count or cached computational result is claimed. The print discrepancy has an exact retained image. |
| Source and verdict fidelity | The assigned source statements and essential deductions match the print passages. The nonconsumed (3.8) discrepancy is disclosed below. No prior verifier ruling or public acceptance is inferred. Verdict words are written in full. |

### Canonical failure modes

| Failure mode | Verdict and reason |
| --- | --- |
| “Almost all” upgraded to “all” | No failure found. All pointwise conclusions are on the constructed $X$; no conclusion is asserted on its complement. |
| Induction presupposing termination | No failure found. The finite choices $B,T,L,d,D,U,M$ are justified in order; their sizes may be large but each is finite. |
| Probabilistic or averaging heuristics as proofs | No failure found. Exact independent finite trials give the failure estimate and first Borel–Cantelli gives eventual success. Expectation alone is not used to infer a pointwise result. |
| Circular use of the claim or an equivalent statement | No failure found. None of the construction bounds assumes large partial sums or the catalog conclusion. |
| Exceptional sets dropped from density arguments | No failure found. There is no density-to-universal transfer; the convergence, binary-expansion and dilation exceptional sets are retained explicitly. |
| Finite verification beyond base-case coverage | Inapplicable as an evidence mode. No finite computation is offered as a universal warrant; the formulas are proved for arbitrary legal parameters. |
| Relaxed or averaged convergence substituted for actual objects | No failure found. The almost-sure sum is identified with the $L^2$ limit, and the endpoint estimate concerns the actual enumerated dilates. |

### Canonical named patterns

| Pattern | Verdict and reason |
| --- | --- |
| Model-class transport instead of entailment | Inapplicable to axiom-system or certificate-class extensions: none occurs. The actual binary-to-circle transfer is nevertheless verified in derivation 2. |
| Uniformity over an infinite family asserted from finitely many instances | No failure found. Constants come from symbolic bounds for every legal block, and stage-dependent constants are not advertised as uniform in the stage. |
| Extremal claims are audited in the claim's own units | No failure found. The endpoint identity counts summands, and the normalization is precisely $N(\log N)^{1/2-\varepsilon}$. No neighboring exponent-size estimate substitutes for it. |
| Consequence sentences are claim surfaces | No failure found. Both the claim's example consequence and its Covers assertion follow from the separately checked logarithmic comparison and positive limsup. |
| Carry hypotheses actually used by a quantified argument | No failure found. Integer windows, finite stage data, $0<a_k\leq1$, $B_k\geq100$, summable costs, and positive logarithms are all supplied at their uses. |
| A composition inherits its unproved premises | No missing consumed clause found. All essential same-paper interfaces are examined, and the permitted foundational theorem boundaries are stated explicitly. No native claim is silently imported. |
| Reproducibility notes are claims | No unsupported mathematical execution or coverage claim is made. The retained subject and derivations define the reproduction route; rendering alone is not described as verification. |
| Verifier quotations are claims | Inapplicable to this blind subject: it contains no prior verifier ruling to adopt. Excluded standing prose was not opened. A later characterization of this report remains a matter for the independent grader and integrator. |
| Verdict words spelled in full | Satisfied: the verdict is refutation-failed. No ambiguous abbreviation is used as a verdict. |
| Certified-bracket functions fail loudly | Inapplicable. No numerical bracket, enclosure, stopping cap, or periodic numerical window is used. |
| A harness leg with no failing input is decoration | Inapplicable. No executable mathematical leg is claimed or manufactured. The pessimistic one-hit configuration is instead analyzed exactly. |
| A gate that reads caches instead of re-running is defective | Inapplicable. No repository gate or cached output supports the verdict. Source text and page images were read directly. |

The two neighboring disciplines are also covered: the probability calculation
does not count correlated samples as independent evidence, and each proof
interface is restricted to the coverage recorded in the premise table.
This is neither a computational batch nor a second independent cycle;
neither a structurally different computational reproduction leg nor a
comparison with prior-cycle attacks is applicable.

## Source fidelity and retained witness

The print comparison used the PDF at the canonical library path with the
same stem as the transcription, identified by the commission as v2.
Theorem 1.6 on printed p.4; the supplied Sections 2–4 on pp.7–16; and
Section 7 through the proof's final sentence on pp.21–23 were inspected
as page images rendered at 300 dpi. Boundary crops excluded preceding
material on pp.4, 7 and 21 and excluded Remark 7.1 on p.23.
A crop before the next section on p.17 contained only the running header;
it contributed no additional proof text. No other source sections were read.
The full supplied text was available; no print access gap affects an
essential $p=2$ inference.

There is one explicit, nonconsumed transcription discrepancy:
display **(3.8)** in the supplied source extract has the right-hand
coefficient $C_2^2\lambda Q/N$, whereas the PDF on printed p.9 has
$C_2\lambda Q/N$. The
[retained equation image](../../assets/ho_review_subject/p09_equation_3_8.png)
shows the printed coefficient. This is a discrepancy in the extraction's
transcribed text, not in Ho's printed formula. Neither version of that
Fourier-tail estimate is used in the assigned proof, so it supplies no
refutation or missing premise for Theorem 1.6 at $p=2$. The frozen
extract has been preserved without correcting it.

The source text and equation image retain Boon Suan Ho's attribution and
the source's CC-BY-4.0 license. Reading context about $p>2$ and Fourier
tails does not extend this report's mathematical verdict to those results.
The v1 result numbering and publication-history parentheticals are likewise
outside the commissioned mathematical conclusion.

## Verdict and grading

**refutation-failed** for the entire assigned specialization of Ho v2
Theorem 1.6 at $p=2$ and for its stated negative answer to the
$o(N\sqrt{\log\log N})$ example in E995.

The report covers the periodic representative, all selected-dilation null
sets, quantifier order, positive signed limsup, actual selected-term count,
stage recursion, both required independence arguments, uniform constants,
external foundations, and the catalog implication. No essential mathematical
coverage is left unfinished within that scope. There is no computational
or kernel warrant, no all-$p$ verdict, and no finding about an optimum,
the Fourier-tail theorem, E996, or Remark 7.1.

This mathematical verdict does not grade the report, promote a native claim,
change catalog standing, or assert journal or community acceptance.
A grader distinct from the source author, reviewer, and any collaborator
must assess the complete frozen report and its independence under the
commissioned contract.
