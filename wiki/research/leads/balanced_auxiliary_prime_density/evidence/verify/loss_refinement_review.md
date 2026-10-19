---
name: research/leads/balanced_auxiliary_prime_density/evidence/verify/loss_refinement_review
title: Independent review of the balanced auxiliary-prime argument
desc: |
  The full substantive refutation-failed assessment of the exact frozen
  proof, retaining independent derivations, attacks and source limits.
created: 2026-09-15T05:31:30Z
updated: 2026-09-15T05:31:30Z
---

***

## Record and current scope

This is the substantive review of the exact
[reviewed subject](../assets/loss_refinement_reviewed.txt). First-person
passages retain the original independent reviewer's voice. The review was
made on 15 September 2026 by an independent reviewer in a fresh context
distinct from the argument's author. The subsequent
[contract grade](loss_refinement_grade.md) is by the commissioning grader,
distinct from both author and reviewer. It addresses the original report
contract and independence, not a second blind mathematical review.

The present filing was prepared by the exposed author. It does not provide
independent correspondence review of this native rendering or a new verdict.
The original report remains in working storage.
The current [proof text](../../loss_refinement.md) and
[research owner](../../_index.md) distinguish this retained assessment from
any later mathematical revision.

## Mathematical verdict

**refutation-failed.** The complete frozen argument survives this review of
its unconditional existence statement, all its essential deductions, and its
stated density consequences. I found no counterexample, omitted essential
case, or unsupported bridge to the claimed bound.

This verdict relies on the exact standard external theorem interfaces
identified below. It does not claim independent proofs of those external
theorems, literature priority, a solution of E0158, or acceptance of any
native claim at a numerical tier. A distinct report-contract grader and
ordinary-clone integration remain necessary for any subsequent tier-bearing
use. The original review did not itself complete corpus integration.

## Subject, independence, and actual reading

Reviewer: the independent reviewer, in the fresh context identified above. I
did not construct the subject or previously build on it. My mathematical
context for this review comprised the admitted frozen subject, the expressly
permitted L4 comparison/standing index, and the four permitted public
source artifacts. No sibling verdict, private plan, author or collaborator
advocacy file, other attack file, or excluded local proof was opened.

The frozen subject is the complete
[retained original](../assets/loss_refinement_reviewed.txt), 667 lines.
Its scope includes the standing, comparison, consequence and external-input
sections. I read it completely; two observed hashes matched admission.

The frozen subject
`wiki/research/leads/balanced_auxiliary_prime_density/evidence/assets/loss_refinement_reviewed.txt`
as it stood on 2026-09-15T05:40:27Z carries the argument's own standing text at
lines 21-26 and 661-667 (author-recorded, without independent review or
acceptance; L4 and L2 at tier 0); a separately spawned materiality grader (model
Claude Fable 5.1) ruled that exposure immaterial by the content test, because
the text states only the null standing, implies no verdict, and the review's
reasoning rests on its own rederivations and attacks rather than on that text.

The only other local mathematical page read was the complete
[L4 comparison index](../../../../../theory/additive_bases/L4_random_modulus_exponent/_index.md)
as it stood on 2026-09-15T02:18:25Z.
I used it solely to compare the exact loss, conventions, scope, and
recorded tier-0 standing. Its descriptions of author checks supply no
mathematical support in this verdict. Its proof, L2, and all sibling
claims and reports remained unopened. The current link is navigation;
the date identifies the historical comparison actually read.

The separate operating read set comprised the complete admission and
applicable organization, workspace, repository, anatomy, research, evidence,
verification, approach-vetting and PDF-reading instructions. Those were
operating context, not mathematical evidence. No additional mathematical
read was authorized by their links.

I visually inspected nine selected full PDF pages. The initial direct web
opens also exposed extracted text from the Erdős article and an introductory
portion of Conrad's note; those automatic excerpts do not enlarge the
proof-coverage claims below. No mathematical executable, solver, test,
Lean command, package installation, or author run was used. The review
did not modify the source proof or the native corpus and did not delegate
mathematical work. Exact external-source identities and the substantive
accounting limitations are retained below.

## Full quantified restatement

Let $\gamma=\sqrt6-2$. The proposition asserts the existence of a
single infinite set $A\subseteq\mathbb Z_{>0}$, a real $C>0$, and a
real $x_0>e$, such that both statements hold:

1. For every integer $n$, there are at most two pairs
   $(a,b)\in A^2$ satisfying $a\le b$ and $a+b=n$.
   These are unordered representations; $a+a$ counts once.
2. For every real $x\ge x_0$,

$$
|A\cap[1,x]|
\ge x^\gamma\exp\{-C\sqrt{\ln x\,\ln\ln x}\}.
$$

The set and constants are chosen before the real cutoff. The same set
therefore has the following additional property: for each real
$\alpha<\gamma$, there is a threshold $x_\alpha$ such that
$|A\cap[1,x]|\ge x^\alpha$ for every real $x\ge x_\alpha$.
In particular its counting-function logarithm has limit inferior divided
by $\ln x$ at least $\gamma$. The latter observation does not assert a
matching upper bound or a positive constant times $x^\gamma$.

The comparison is with L4's stated loss
$\sqrt{\ln x}\,\ln\ln x$, with the same representation and cutoff
conventions. The new loss exponent divided by that one is
$1/\sqrt{\ln\ln x}$, which tends to zero. This is an improvement in
the order of the explicit loss, without a larger power exponent or a
public-record claim.

## Setup and transfer checks

The elementary scale estimates are sufficient at their exact strength.
The final half of the summands in
$S_k=\sum_{j\le k}\lceil j\log_2(j+1)\rceil$ gives
$S_k\gg k^2\log(k+1)$; the maximum summand gives the reverse bound.
Thus $w_k=O(R_k)$, $R_k=o(S_k)$, and
$R_k^2=O(S_k\log(S_k+2))$, where
$R_k=k\log_2(k+1)$. Also $R_{k+1}=O(R_k)$.
The strict increase of $w_j$ makes the half-open prime intervals
disjoint. Each is nonempty, and every auxiliary-prime outcome satisfies
the product bounds (3).

From the prime number theorem,
$\pi(2^{w+1})-\pi(2^w)\asymp2^w/(w+1)$. The finitely many
remaining intervals are absorbed by a single constant using nonemptiness.
Unique factorization and the disjoint intervals make a tuple of lower
primes recoverable from its product. Hence its atom probability is at most
$$
2^{-S_L}\prod_{j\le L}C(w_j+1)
=2^{-S_L+O(L\log(L+1))}.
$$
Conditioning on the finitely many higher coordinates leaves that law
unchanged. The source-shell count uses no short-interval theorem: the
discarded interval has at most $X_{k-1}$ integers, and
$X_{k-1}\ln X_k/X_k\to0$.

A sufficiently large deterministic $k_0$ ensures that a source prime
in shell $k$ exceeds every auxiliary prime through $k$. The exponent
interval $[q_j+1,2q_j-1]$ contains exactly $q_j-1$ representatives
modulo $q_j-1$, so the discrete-log digit exists uniquely. All digits
are below their radices. Mixed-radix uniqueness and
$X_k<Q_k$ prove injectivity of the labels within a shell; the last
nonzero digit distinguishes different shells.

For sums, the largest digit is $4q_j-2<4q_j$, so no carries occur.
The double, single, and zero digit ranges are disjoint. They recover both
shell indices from a sum. A same-shell equality gives congruent products
modulo $Q_k$; both products are below $Q_k$, since $2\gamma<1$.
Unique factorization then identifies the unordered pair, including a
diagonal.

For unequal shells, only the implication from a sum equality to a fiber
of $(P\bmod N,PR\bmod M)$ is needed. Fixing $P$ permits cancellation
modulo $M$ and uses $Y<M$. Fixing $R$ permits cancellation modulo
$M$, then combines the two coprime moduli and uses $X<MN$.
There is no cancellation of a lower-shell prime modulo $N$.
Thus both fiber projections are injective. Distinct points have nonzero
upper and product differences: shell disjointness excludes a crosswise
factorization. Their sizes force $N<X$ and $M<XY$, and consequently
$$
1-\gamma<\lambda=\frac{S_L}{S_K}
<\frac{\gamma}{1-\gamma}.
$$
In particular all potentially contributing lower shells are comparable
in scale to the upper shell. No unproved L-claim is needed for this
transfer.

## Weakest step 1: degeneracies in the fixed-modulus count

I rederived the two equations used for elimination from
$$
P_1(R_2-R_1)+NaR_2=Ms,\qquad
P_1(R_3-R_1)+NbR_3=Mt.
$$
Eliminating $P_1$ gives $NA=MB$, where
$$
A=aR_2(R_3-R_1)-bR_3(R_2-R_1),\quad
B=s(R_3-R_1)-t(R_2-R_1).
$$
Since $(M,N)=1$, $A=dM$ and $B=dN$ for an integer $d$.
The direct triangle bound is $|d|<2XY^2/(MN)=W$.

For $\lambda\le2/3$, the first three comparisons in (14) have a
negative fixed multiple of $S_K$ plus $O(R_K)$ in their logarithms.
The logarithm of $WU^3/M$ is at most
$$
1+(4\gamma-4)S_K+(2\gamma+2)S_L
\le 1+\frac{16\gamma-8}{3}S_K,
$$
whose coefficient is negative. This verifies all four comparisons
uniformly, including lower endpoints of the source shells.

If $d=0$, reducing $A=0$ modulo the distinct lower prime $R_2$
gives $R_2\mid bR_3R_1$, and hence $R_2\mid b$. But
$0<b<U<R_2$. This rules out the first degeneracy without a sign
assumption on the product offsets.

For $\Delta=at-bs\ne0$, put
$\rho=R_2-R_3$, $\sigma=atR_2-bsR_3$. Multiplying the first
equation in (13) by $t-s$ and substituting the second gives
$$
\rho\sigma=d\{M(s-t)-NaR_2+NbR_3\}.
$$
The inverse linear transformation is
$$
R_2=(\sigma-bs\rho)/\Delta,\qquad
R_3=(\sigma-at\rho)/\Delta.
$$
Substitution and multiplication by $\Delta$ give exactly
$$
(\Delta\rho-dN(b-a))(\Delta\sigma-dNab(s-t))
=d(s-t)\{\Delta^2M+dN^2ab(b-a)\}.
$$
This verifies both the signs and the factor of $s-t$ in (16).

The right side cannot vanish. Here $d\ne0$, $s\ne t$, and vanishing
of the braces would imply $M\mid dab(b-a)$, by coprimality with $N$.
Yet $0<|dab(b-a)|<WU^3<M$. This also excludes cancellation when
$d$ is negative.

Every parameter and factor in this formula has magnitude
$2^{O(S_K)}$, uniformly over outcomes and lower shells. The exposed
divisor argument is valid: primes at most $\sqrt{\ln H}$ contribute
at most $O(\sqrt{\ln H}\log\ln H)$ to $\log\tau(n)$; larger
primes have total multiplicity at most $2\ln H/\log\ln H$.
The first contribution is also $O(\ln H/\log\ln H)$ eventually.
Thus there are $2^{O(S_K/\log S_K)}$ signed ordered factor pairs.
Each determines $\rho,\sigma,R_2,R_3$, then $R_1$ from
$s\ne t$, and $P_1$ from $R_2\ne R_1$. The remaining upper
coordinates follow. Invalid reconstructions only reduce the count.

For the separate case $\Delta=0$, coprimality after dividing
$a,b$ by their gcd gives
$a=ea'$, $b=eb'$, $s=fa'$, $t=fb'$, with $f\ne0$.
Writing $C_0=fM-NeR_1$ gives
$$
a'C_0=P_2(R_2-R_1),\qquad b'C_0=P_3(R_3-R_1).
$$
The inequalities $a'<P_2$, $b'<P_3$ force both distinct upper
primes to divide $C_0$. Also
$|C_0|<2XY<P_2P_3$. Thus $C_0=0$, contradicting distinct
lower coordinates. This handles the branch where the inverse linear
transformation would otherwise be unavailable.

Finally, $U^2$, $4Z^2$, and $2W$ bound the numbers of gaps,
signed offsets, and nonzero $d$'s. Their product has main factor
$$
U^2Z^2W=\frac{2X^5Y^4}{(MN)^3}.
$$
This gives (18), including its error scale and uniformity. The larger
divisor error need not fit inside $O(R_K)$: in this part of the
band a fixed exponential saving absorbs it later.

## Weakest step 2: the line contribution and conditional averaging

I checked the lattice bound with the line contribution retained. For a
primitive integer normal, the two proposed kernel vectors have cross
product $c$. The scalar product of $c$ with the proposed third vector
is one, so the three vectors form an integer basis of determinant one.
This proves both the kernel basis and its covolume $\|c\|_2$.
The special normal with its first two coordinates zero is immediate.

A shortest nonzero lattice vector is primitive in lattice coordinates and
extends to a basis. Reducing the other basis vector along it makes its
parallel component at most half the shortest length. Minimality then
forces the perpendicular height to be at least $\sqrt3/2$ times that
length. Counting parallel lattice lines and points on each line inside a
ball containing the cube yields
$$
O(1+Y/\ell+Y^2/D).
$$
An area term alone would not justify the subsequent argument.

After reducing $s,t$ by their gcd, their values and $s-t$ are all
nonzero. A prime outside the three upper primes cannot divide the entire
normal $((t-s)P_1,-tP_2,sP_3)$, since it would divide both reduced
offsets. A common prime equal to one of the upper primes would have to
divide a nonzero reduced offset multiplying a different upper prime.
That offset has smaller magnitude than the putative common prime, which
is impossible. Thus the normal is primitive, with length at least $P_-h$.

For a kernel vector $v$, the first brace in
$$
P_1\{(t-s)v_1-tv_2+sv_3\}
+N\{-ta v_2+sb v_3\}=0
$$
is divisible by $N$. If $\|v\|_\infty<N/(3h)$, its absolute
value is below $N$, so both braces vanish. The transformed integer
vector
$$
((t-s)v_1,-tv_2,sv_3)
$$
is then a nonzero integer multiple of
$((b-a)/g,-b/g,a/g)$. Its second coordinate implies
$\|v\|_\infty\ge b/(gh)$. Consequently every nonzero vector has
length at least $\min\{N/(3h),b/(gh)\}$, which gives (21).
All cancellations here use $P_1$ coprime to $N$.

The small-coefficient hypothesis is justified uniformly:
$$
\log_2(Z/P_-)=-(1-\gamma)S_L+\gamma w_K.
$$
The band supplies $S_L>(1-\gamma)S_K$, while $w_K=o(S_K)$.
Thus even the unreduced difference of the offsets is eventually below
every upper prime.

Under conditioning on the higher auxiliary primes, $N$, the source
shells, the candidate upper coordinates, and the ranges $U,Z$ are
fixed. For each candidate point and nonzero $s$, at most one lower
product can work:
$$
M=(P_2R_2-P_1R_1)/s.
$$
It has probability zero if inadmissible, and at most
$2^{-S_L+O(R_K)}$ otherwise. Repeated candidate points producing the
same $M$ do not require independent indicators: finite linearity of
expectation gives an upper bound including all their multiplicities.

The gcd sum is also uniform. For a fixed positive $b$,
$$
\sum_{0<a<b}\gcd(a,b)\le b\tau(b),
$$
by summing common divisors. Summing $\tau(b)$ by divisors gives
$\sum_{b<U}\tau(b)\le U(1+\ln U)$. The signed offset sums are
bounded respectively by $O(Z^2)$, $O(Z^3)$, $O(Z^2)$ for
the weights $1,h,1/h$.

Multiplying these counts by the three terms in (21) yields, before
division by $M_0$, precisely
$$
XU^2Z^2,\quad XYUZ^3,\quad XYU^2Z^3/N,\quad U^2Y^2Z^2,
$$
up to $2^{O(R_K)}$. The logarithm in the gcd sum and the factor
$X/P_-=2^{\gamma w_K}$ fit inside that error. Using the lower
bound for $N$, their coefficients after division by $M_0$ are
$$
\begin{array}{c|l}
1&5\gamma-2+(2\gamma-1)\lambda\\
2&5\gamma-1+(4\gamma-3)\lambda\\
3&6\gamma-3+(4\gamma-1)\lambda\\
4&4\gamma-2+(4\gamma-1)\lambda .
\end{array}
$$
The first minus fourth is $\gamma(1-2\lambda)<0$; the third
minus fourth is $2\gamma-1<0$. This independently recovers
(25)--(27), with the line term still present.

## Weakest step 3: critical endpoints, one outcome, and every cutoff

Let $\eta=3-20\gamma/3$. Its positivity follows from
$\sqrt6<49/20$, using $6<(49/20)^2$. The deterministic
coefficient on $\lambda\le2/3$ is at most $\gamma-\eta$.
Its uniform $o(S_K)$ divisor error is eventually smaller than
$\eta S_K/2$.

On the remaining band, the line coefficient
$H_\gamma(\lambda)=5\gamma-1+(4\gamma-3)\lambda$ decreases, and
$H_\gamma(2/3)=\gamma-\eta$. The area coefficient
$D_\gamma(\lambda)=4\gamma-2+(4\gamma-1)\lambda$ increases, and
$$
D_\gamma\!\left(\frac{\gamma}{1-\gamma}\right)
=\frac{5\gamma-2}{1-\gamma}=\gamma,
$$
because $\gamma^2+4\gamma-2=0$. This is a non-strict endpoint
bound. The proof correctly uses no positive distance from that endpoint.
Summing fewer than $K$ lower shells therefore yields
$\mathbb E T_K\le2^{\gamma S_K+C_1R_K}$ with a single constant.

Each $T_K$ is a finite-cylinder, nonnegative finite random variable.
Markov's inequality with threshold $2^{\gamma S_K+C_1R_K+K}$
makes its failure probability at most $2^{-K}$. For any $J$,
the union of failures after $J$ has probability at most
$\sum_{K\ge J}2^{-K}$, which tends to zero. Thus a single infinite
auxiliary sequence has only finitely many failures. This uses no
independence between shell events.

For a finite three-uniform hypergraph, independently retaining vertices
with probability $p$ gives expected vertices minus edges $pn-p^3m$.
An outcome at least as good as the expectation exists. Deleting at most
one vertex per surviving edge leaves an independent set. The two
specified cases of $p$ give a fixed positive constant times
$n/\sqrt{1+m/n}$. Combining this with
$n_K=2^{\gamma S_K-O(\log S_K)}$ and
$m_K\le2^{\gamma S_K+O(R_K)}$ gives (32).

All lower shells used in defining an upper hypergraph are full source
shells. Hence the upper independent sets may be selected simultaneously:
later or earlier deletions cannot create an unrecorded triple.
Lexicographic choice of a maximum independent set makes each finite
selection definite; exceptional early shells are empty. If three distinct
representations remained, digit ranges would force a common shell pair.
The equal-shell case was already excluded. In the unequal case, fiber
injectivity supplies three distinct selected upper vertices, contradicting
independence. This covers all integer sums and diagonal conventions.

For every sufficiently large real $x$, there is a unique $K$ with
$B_K\le x<B_{K+1}$. All selected shell-$K$ labels are below $x$,
and with $t=\log_2x$,
$$
S_K+2K<t<S_K+w_{K+1}+3K+3.
$$
Therefore $t-S_K=O(R_K)$ and
$R_K=O(\sqrt{t\log_2 t})$. The shell lower bound gives
$$
\log_2 A(x)\ge\gamma t-O(\sqrt{t\log_2 t}).
$$
Multiplying by $\ln2$ changes the loss to a constant times
$\sqrt{\ln x\,\ln\ln x}$, since
$\ln(\log_2x)=\ln\ln x-\ln\ln2$. Constants absorb this fixed
logarithm-base correction eventually. The finitely many exceptional
shells only enlarge $x_0$. Since $R_K=o(S_K)$, the retained shell
sizes tend to infinity. The loss divided by $\ln x$ tends to zero,
which proves the same-set consequence for every fixed $\alpha<\gamma$.

## Strongest attempted refutation

The main attack was to seek a positive-dimensional family missed by the
fixed-modulus divisor count. Two dangerous possibilities are
$\Delta=0$, where the coordinate recovery is singular, and
$\Delta\ne0$ with the right side of (16) zero, especially for negative
$d$. Either would invalidate the finite divisor-pair count and could
destroy the saving needed below $\lambda=2/3$.

The attack failed under the actual hypotheses. In the singular branch,
both distinct upper primes divide $C_0$, while
$|C_0|<P_2P_3$, forcing equal lower coordinates. In the resonant
branch, coprimality forces the nonzero integer $dab(b-a)$ to be a
multiple of $M$, while its magnitude is below $M$. These
contradictions do not discard negative offsets or assume generic
parameters.

I also tested the reason a line term is essential. In a potential
arithmetic-progression configuration $a=u,b=2u,s=1,t=2$, with
an integer $u>0$, the
collision plane has the short direction $(1,1,1)$. Its diagonal
integer points would defeat an area-only estimate in suitable scales;
they are not asserted to be actual fiber triples with distinct lower
primes. The proof retains and sums the line contribution, whose exponent
$H_\gamma$ remains strictly below $\gamma$ on the upper band.
Finally I allowed shell ratios arbitrarily close to the critical upper
endpoint. The argument still closes with a non-strict main exponent and
the explicit $O(R_K)$ loss.

## Audit checklist

| Item | Verdict and reason |
| --- | --- |
| Quantifiers and scope | Pass. One outcome and one set precede all real cutoffs and all fixed $\alpha<\gamma$. Only thresholds absorb finite exceptions. All integer sums and diagonals are covered. |
| Circularity | Pass. Neither L4's theorem nor the desired density conclusion is assumed. The product model, counts, alteration, and cutoff transfer are supplied separately. |
| Model and convention changes | Pass. Mixed-radix encoding is injective and carry-free. Actual collisions imply fibers; no converse is used. Counting all lower integer points enlarges a set for an upper bound. |
| Finite and statistical overreach | Pass. There are no numerical samples. Finite expectation estimates reach one infinite outcome through a summable-event argument. Shared indicators need not be independent. |
| Uniformity | Pass. Source endpoint losses are $O(R_K)$; lower-band divisor error is absorbed by fixed slack. The upper endpoint needs no spacing assumption. All conditioning is finite and its bounds are uniform. |
| Extremal conclusions | Pass. Finite maximum independent sets exist. No optimality, sharpness, attained asymptotic density constant, or square-root conclusion is inferred. |
| Consequences and composition | Pass. Full lower shells make selection simultaneous; same-shell uniqueness and fiber injectivity give the representation bound. The every-real-cutoff transfer and the same-set $\alpha$ consequence follow at their claimed strengths. |
| Computation | Inapplicable as mathematical evidence. This is a noncomputational argument. Arithmetic, signs, degenerate cases, and exponent comparisons were independently rederived above; no cached run or numerical enclosure is used. |
| Reproduction | Inapplicable to mathematical execution: there is no required program or computational input. The admitted text and pinned public PDFs suffice. Exact source versions and page coverage are retained here; rendering served source inspection only. |
| Source and verdict fidelity | Pass for every mathematical external interface and the admitted L4 comparison/standing clause. Source proofs are not recursively certified. Cilleruelo attribution, L2 standing, and the author's historical reading assertions remain explicitly uninspected non-premise limits, as detailed below. |

## Exact premise scope and source reading

No native L-claim, local component theorem, or prior independent report is
consumed as an established premise. L4 is recorded as tier 0 in the
admitted index; its old loss and scope match the comparison. Its theorem
is not applied to the new schedule. The subject supplies the necessary
digital, factorization, lattice, averaging, and selection arguments, all
reviewed here. There is no batch acceptance order or unproved mathematical
antecedent of the asserted existence theorem.

Ordinary foundational arithmetic used includes unique prime factorization,
Bézout's identity and gcd divisibility, finite linearity of expectation,
and elementary limits and inequalities. Their relevant applications and
cancellation hypotheses are exposed above. The nontrivial standard
external interfaces and reading boundaries are:

- [Erdős, Beweis eines Satzes von Tschebyschef, admitted 1932 artifact](https://users.renyi.hu/~p_erdos/1932-01.pdf):
  section 5, printed 197--198, PDF pages 4--5, both visually inspected.
  The interface is existence of a prime $m<q\le2m$ for each integer
  $m\ge1$, applied at $m=2^{w_j}$. The inclusive upper endpoint
  and the $m=1$ case agree with the visible source. The theorem
  statement and application were checked; the full external proof was
  not independently reconstructed.
- [Conrad, Cyclicity of the nonzero residues modulo a prime](https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf):
  Theorem 2.6, PDF/printed page 3, visually inspected. The interface is
  cyclicity of the multiplicative group of each prime field, applied
  separately at every selected $q_j$. The downloaded SHA256 exactly
  matches the admission's recorded hash. The statement was checked;
  the displayed local proof was read without recursively reviewing its
  earlier lemmas.
- [Zagier, Newman's Short Proof of the Prime Number Theorem, 1997](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf):
  printed 705, PDF page 2, visually inspected. The interface is
  $\pi(x)\sim x/\ln x$. It supplies the dyadic auxiliary-prime
  count and the source-shell count by the explicit endpoint deductions
  above. The theorem statement was checked, not its analytic proof.
- [Durrett, Probability: Theory and Examples, version 5, 11 January 2019](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf):
  the version was visually verified on PDF page 1. Theorem 2.1.21,
  printed 53/PDF 61, supplies a probability measure for consistent
  finite-dimensional real laws; products of the finite uniform prime
  laws satisfy consistency and concentrate on the intended prime
  sequences. Theorem 1.6.4, printed 29--30/PDF 37--38, gives Markov
  after taking $\phi(u)=\max(u,0)$ and a positive tail threshold.
  Theorem 2.3.1, printed 68/PDF 76, requires summable event probabilities
  and no independence. All these pages were visually inspected.
  Statements were checked; the two short displayed probability
  arguments were read, and the needed Markov and tail-union deductions
  were independently rederived. The extension theorem's proof was not
  reviewed.

The Cilleruelo manuscript was not opened. Its method attribution and the
subject author's claimed manuscript reading are not certified. L2 was
not opened, so its historical/current standing assertion is not
independently authenticated here. Neither supplies a density premise or
an essential omitted deduction. No fresh literature census, priority
assessment, public acceptance investigation, or exact catalog-page
status audit was commissioned or performed.

## Exact external artifact identities

The original source-access date was 15 September 2026. These are the
reviewer's reported pinned versions, not sources newly acquired or
visually inspected during native filing. The URLs, theorem locators,
specializations and actual reading depth are given in the preceding
source list.

| Source artifact | Bytes | PDF pages |
| --- | ---: | ---: |
| Erdős, admitted 1932 artifact | 502956 | 5 |
| Conrad, cyclicmodp | 375334 | 19 |
| Zagier, 1997 | 196309 | 5 |
| Durrett, version 5, 11 January 2019 | 2195717 | 490 |

The nine full-page visual inspections were Erdős PDF pages 4 and 5;
Conrad page 3; Zagier page 2; and Durrett pages 1, 37, 38, 61 and 76.
The source record additionally counted five Erdős and four Conrad
extracted-text page surfaces and one Durrett title-page text extraction:
nineteen page surfaces in that conservative count, not nineteen full
visual inspections. Some automatic web text was partial. Requested URLs
and successful responses were recorded, but redirect chains were not
separately logged.

## Resource and acceptance limits

The review used only the frozen mathematical subject and the narrow local
comparison described above. It acquired the four identified PDFs and
visually inspected the nine selected complete pages. Public source proof
coverage stops at the interfaces and displayed portions explicitly listed.
No mathematical code is required to reproduce the deductions. Source-view
rendering was a reading aid, not computational reproduction of the theorem.

The original source record measured 3,270,316 downloaded PDF bytes and
1,664,312 bytes of derived page images. Its conservative repeated-PDF
accounting charged 26,758,522 bytes; adding a text/metadata allowance gave
27,807,098 bytes. Raw web-tool transfer bytes were unavailable and were
not claimed as measured. Each web open was charged the subsequently pinned
artifact size instead. Repeated instruction reads and administrative
allowances were likewise conservatively accounted, not silently treated
as single reads. These are the original review's reported accounting
limitations, not measurements repeated during filing.

The report is a mathematical assessment of the pinned subject only.
Changing its mathematics or its consumed premises requires a new scope
assessment. This report does not grade its own independence or contract
compliance, confer a tier, or by itself establish ordinary-clone
integration. The distinct grade and this author-prepared native retention
remain separate from the historical mathematical verdict.
