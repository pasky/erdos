---
name: research/leads/aliquot_collision_density/evidence/verify/analytic_conclusions/review
title: Independent review of the analytic aliquot-collision results
desc: Adversarial examination of the collision obstruction, four-way equivalence and conditional density reduction, excluding the numerical census.
created: 2026-10-16T23:12:27Z
updated: 2026-10-16T23:12:27Z
---

# Independent review of the analytic aliquot-collision results

## Subject and independence

**Reviewer:** independent mathematical reviewer, commissioned model
GPT-6-astra, with no authorship of or collaboration on the assessed argument.
**Examination date:** 2026-10-16 UTC. **Freeze date:** 2026-10-16 UTC.
The local mathematics under examination is attributed to Plasma AI.

The native subject is
`wiki/research/leads/aliquot_collision_density/_index.md`, from **Target and
conventions**, through **The density-zero form is false** and **An equivalent
form of the problem**, ending with the semiprime separation inequality before
**Exact census**. The independently reconstructed supporting countermodel is
from `wiki/problems/arithmetic_functions/E0955/_index.md`, **Exact scope of the
arithmetic reduction**. Only the supplied frozen extractions were examined;
the full pages were not opened.

The retained subject is
`wiki/research/leads/aliquot_collision_density/evidence/assets/analytic_conclusions/subject.md`.
Its line numbers below refer to that extraction, not to the current native
page. The accompanying `countermodel.md` preserves the supplied countermodel
extraction, and `source_interfaces.md` records the exact mathematical interfaces
used from the supplied literature statements, with their provenance and reading
limits. The first two are unchanged copies of the supplied extractions;
`source_interfaces.md` is the reviewer's restatement, not an original-source
facsimile. All three belong in that same assets directory.

The charge was to find a counterexample, error, unsupported essential inference,
or canonical failure mode in every commissioned mathematical conclusion.
The finite census, later sieve route, and any assertion of a full solution of
E0955 are outside this examination. Condition (D) is reviewed as an antecedent
of implications, not as an established bound.

The review began in a fresh context separated from the subject's construction.
The allowed mathematical reading consisted of the subject extraction, its source
manifest, the PNT, Mertens and Pollack--Pomerance--Thompson excerpts, and the
countermodel extraction. All six were read completely. The governing corpus
and commissioned operating instructions were also read at their allowed scope.
No original mathematical page, source card, native claim ledger, prior review,
author working notes, inbox, live website or original PDF was opened. No broad
search or upstream update was performed. The supplied subject was kept fixed.
An empty subscription table was checked at the initial boundary and again on
resuming the examination; this supports channel isolation but is not itself
proof of what was read.

**Exposure requiring the grader's ruling.** General motivational advocacy
accompanied the assignment before mathematical reading: it listed unrelated
reported AI mathematical achievements and urged ambitious full solutions.
That is advocacy of the kind excluded by the verification standard. It was
disclosed when the exclusion was identified. It supplied no step of these
aliquot arguments, and none of its announcements is used as a premise or as
support for a favorable verdict. This disclosure does not adjudicate its
materiality. A separate grader must rule on that issue before treating this
report as an independent warrant.

This is a noncomputational examination. The independent derivations, exact
inequalities, countermodels used as attacks, and findings are contained below.
No executable evidence, finite census, statistical sample or cached output
supports a verdict, so there is no computational rerun command. The report
neither grades itself nor asserts a tier.

**Mathematical result:** refutation-failed for Theorems A and B and the scoped
analytic consequences. The literature-status characterization and the
independence exposure retain the qualifications stated below.

## Conventions, claim surfaces and external premises

Inputs are positive integers; $s(n)=\sigma(n)-n$ and $s(1)=0$.
For real $x\ge1$, $n\le x$ means positive integer inputs. The index m in a
fiber sum is a nonnegative integer, and $\sum_m r_x(m)=\lfloor x\rfloor$.
Here $r_x(m)=\#\{n\le x:s(n)=m\}$; $r_{S,x}(m)$ restricts that count to
$n\in S$, and $R_S(x)=\#(S\cap[1,x])$. The admitted set S may depend on x.
The only input of value zero is 1, since every $n>1$ has proper divisor 1.
Thus the two conventions about whether zero belongs to the target universe
change a preimage count by at most one.

For an admitted set S, the equality
$C_S(x)=\sum_m r_{S,x}(m)^2$ counts ordered pairs, including exactly $R_S(x)$
diagonal pairs. Interchanging coordinates pairs up the remaining pairs without
fixed points. Hence $C_S-R_S$ and $(C_S-R_S)/2$ have precisely the ordered and
unordered meanings stated in the extraction. A finite target B captures at most
$\sqrt{|B|C_S(x)}$ admitted inputs, by Cauchy--Schwarz. An infinite sparse
target needs the additional output-tail argument below.

The report separates five groups, with every subsidiary consequence recorded:

| Group | Assessed surface in the frozen extraction |
| --- | --- |
| A | Theorem A and its local construction and density estimates, lines 39--101 |
| A-epsilon | The semiprime example and density-order explanation, lines 34--37 and 103--108; the supremum and superpolynomial lower bounds, lines 108--119 |
| B | All four conditions and every implication of Theorem B, lines 129--196; the claimed equivalence of the corrected route, lines 124--127 and 206 |
| C | The PPT comparison and its obstruction, lines 198--204, with the entire supplied abstract countermodel |
| D | Complement estimate, conditional sufficiency, necessary growth of any admissible constant, and semiprime separation, lines 206--233 |

No native L-claim is consumed as an established premise. This was checked from
the frozen statements, proofs and consequence sentences on the examination
date. The local arithmetic assertions and countermodel are rederived here;
no author's tier is assumed and no live ledger reading was required or made.

The exact external interfaces are as follows. The fuller source identities and
formulas are retained in `source_interfaces.md` in the assets directory named
above.

| Source and locator | Consumed assertion and specialization | Reading depth and limit |
| --- | --- | --- |
| Johnston--Yang, *Some explicit estimates for the error term in the prime number theorem*, April 21, 2022 edition, Introduction and Corollary 1.3; canonical path `library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem.md` | $\pi(t)\sim t/\log t$, used for fixed-ratio prime intervals and prime density zero | Claims checked against the supplied statement; source proof and PDF fidelity not inspected. The explicit corollary implies the stated asymptotic, as shown in the retained interface. |
| Tao, *254A, Notes 1: Elementary multiplicative number theory* (2014), Theorem 26; supplied retrieval date 2026-10-16 | $m_t=(e^{-\gamma}+O(1/\log t))/\log t$; applied at $t=100/\delta$, at fixed roughness thresholds, and to bound the reciprocal-prime sum | Claims checked against the supplied statement. This is an expository source, not inspection of the original Mertens paper; no proof was supplied or reconstructed. |
| Pollack--Pomerance--Thompson, *Divisor-sum fibers*, 2017 author manuscript, Theorem 1.2, published in *Mathematika* (2018); canonical path `library/arithmetic_functions/pollack_2018_divisor_sum_fibers/pollack_2018_divisor_sum_fibers.md` | Uniform $o_h(x)$ capture for targets of size at most $x^{1/2+h(x)}$, for each fixed function $h(x)\to0$ | Claims checked against the supplied definition and statement. Proof not inspected. Used only in group C's comparison, never to prove B or E0955. |

These are identified external theorem interfaces, not local reconstructions of
the literature. Ordinary reliance on them is the commissioned boundary. The
PNT excerpt uses the conventional logarithmic integral; the singular integral
notation is understood as principal value. Changing its finite additive
normalization would not change the asymptotic used here. Nothing depends on the
other explicit estimates printed in that excerpt.

There is one unsupported characterization: the closed packet supplies no
literature-wide evidence for the sentence that (D) is **not known to be
equivalent**. The argument establishes sufficiency and does not establish
necessity. That mathematical limitation is checked; the separate assertion
about the state of knowledge is not certified. No disproof of equivalence is
inferred from absence of its proof here.

## A: removal of a density-zero family

### Restatement

For every family $E_x\subseteq\{1,\ldots,\lfloor x\rfloor\}$, with no
consistency or monotonicity assumed between different x, if $|E_x|/x\to0$,
then

$$
\frac{C_{[1,x]\setminus E_x}(x)}x\longrightarrow+\infty.
$$

The conclusion is eventual divergence for each such family, not a bound uniform
in all families' starting points or a prescribed rate of divergence.

### Weakest steps, independently rederived

**A1. The multiplicative class really has small outputs.** Fix
$0<\delta\le1/10$, put $z=1/\delta$, $Z=100z$, and let
$P_Z=\prod_{q\le Z}q$. For a positive integer $k$ coprime to $P_Z$, with
$f(k)=\sum_{q\mid k}1/(q-1)\le\delta/10$, unique factorization gives

$$
\frac{\sigma(k)}k
\le\prod_{q\mid k}(1-1/q)^{-1}
\le\exp\!\left(\sum_{q\mid k}\frac1{q-1}\right).
$$

The logarithmic bound follows from
$-\log(1-u)\le u/(1-u)$ for $0\le u<1$; prime powers cause no extra factor.
For $0\le t\le1/100$, the exponential series gives
$e^t\le(1-t)^{-1}$. Consequently
$e^{\delta/10}\le1+(10/99)\delta\le1+0.11\delta$.
If $z/1.8<p\le z/1.1$, then
$1.1\delta\le1/p<1.8\delta$. Since p is smaller than Z and k is
Z-rough, p does not divide k. Multiplicativity now yields

$$
\delta\le\frac{s(pk)}{pk}
\le1.91\delta+0.198\delta^2
\le1.9298\delta<2\delta.
$$

The prime p is the only prime divisor of pk at most Z, so two different
choices of p cannot produce the same input. The case $k=1$ gives a prime
input, with positive value 1, and satisfies the same ratio bounds. In
particular no value zero enters the pigeonhole count.

**A2. Weighted rough-number counting retains positive mass.** Every full
interval of length $P_Z$ contains $\varphi(P_Z)$ integers coprime to $P_Z$.
Finite inclusion--exclusion gives $\varphi(P_Z)/P_Z=m_Z$.
Thus, uniformly for real $t\ge0$,

$$
R_Z(t):=\#\{k\le t:(k,P_Z)=1\}=m_Zt+O_Z(1).
$$

For a prime $q>Z$, multiplication by q preserves coprimality with $P_Z$.
Counting each prime divisor once, including numbers divisible by its higher
powers, gives the exact finite identity

$$
\sum_{\substack{k\le y\\(k,P_Z)=1}}f(k)
=\sum_{Z<q\le y}\frac{R_Z(y/q)}{q-1}.
$$

The accumulated residue error is bounded by a constant depending only on Z
multiplied by $\sum_{q\le y}1/(q-1)$. The latter is $O(\log\log y)$ from
the supplied Mertens statement, since

$$
\sum_{q\le y}\frac1{q-1}
\le\sum_{q\le y}-\log(1-1/q)
   +\sum_{m=2}^{\infty}\frac1{m(m-1)}
=\log(1/m_y)+1.
$$

The main term is at most
$m_Zy\sum_{m>Z}1/[m(m-1)]=m_Zy/\lfloor Z\rfloor$.
For real $Z\ge1000$, $Z/\lfloor Z\rfloor\le1000/999<1.01$.
Markov's inequality at threshold $\delta/10$ therefore excludes at most

$$
0.101m_Zy+O_\delta(\log\log y)
\le0.11m_Zy+o_\delta(y)
$$

rough integers. The retained count is at least $0.89m_Zy-o_\delta(y)$.
There are finitely many allowed p for fixed delta. Summing this count at
$y=x/p$, using A1's uniqueness, proves exactly the stated lower bound
$(d_\delta-o_\delta(1))x$, with

$$
d_\delta=0.89m_Z\sum_{5z/9<p\le10z/11}\frac1p.
$$

The constants implicit in the error can be enormous as delta decreases. No
uniformity in delta was used in this calculation.

**A3. The prime-window constant and two successive limits.** For fixed
$0<a<b$, partial summation gives

$$
\sum_{az<p\le bz}\frac1p
=\frac{\pi(bz)}{bz}-\frac{\pi(az)}{az}
 +\int_{az}^{bz}\frac{\pi(t)}{t^2}\,dt.
$$

The PNT approximation is uniform on this fixed-ratio interval as $z\to\infty$,
simply because its relative error is eventually small for every $t\ge az$.
The endpoint difference is $o(1/\log z)$, whereas the integral is
$(\log(b/a)+o(1))/\log z$. Taking $(a,b)=(5/9,10/11)$ gives the
coefficient $\log(18/11)$. Also
$m_{100z}\sim e^{-\gamma}/\log z$ by Mertens, since
$\log(100z)/\log z\to1$. Hence

$$
d_\delta\log^2(1/\delta)
\longrightarrow0.89e^{-\gamma}\log(18/11)>0.24.
$$

For completeness, the numerical strict inequality needs no floating-point
calculation. Let $H_n=\sum_{j\le n}1/j$. From the definition of gamma,

$$
H_n-\log n-\gamma
=\sum_{k=n}^{\infty}\int_k^{k+1}
 \left(\frac1t-\frac1{k+1}\right)dt
>\frac1{2(n+1)}.
$$

For the last inequality, each integral is at least
$1/[2(k+1)^2]$, and the sum of these lower bounds exceeds
$\tfrac12\int_{n+1}^{\infty}t^{-2}dt$.

The four-term positive series for $2\operatorname{artanh}(2/3)=\log5$
is $122492/76545>8/5$. Taking $n=5$ in the preceding inequality gives
$\gamma<11/5-\log5<3/5$. The alternating exponential series through degree
5 gives $e^{-3/5}>0.548752>5487/10000$. Also

$$
\log(18/11)>2\left(\frac7{29}+\frac{(7/29)^3}{3}\right)
=\frac{36008}{73167}>\frac{123}{250}.
$$

Thus the coefficient exceeds
$ (89/100)(5487/10000)(123/250)=60066189/250000000>0.24$.
In particular $d_\delta\ge0.2/\log^2(1/\delta)$ for all sufficiently small
delta; no effective cutoff or all-delta version follows from this step.

For any one such fixed delta, removal of $o(x)$ inputs leaves at least
$(d_\delta-o(1))x$ members of $V_\delta$. Their values are positive integers
at most $2\delta x$. There are at most $\lfloor2\delta x\rfloor$ such
values, so Cauchy--Schwarz gives

$$
\liminf_{x\to\infty}\frac{C_{[1,x]\setminus E_x}(x)}x
\ge\frac{d_\delta^2}{2\delta}
\ge\frac{0.02}{\delta\log^4(1/\delta)}.
$$

This holds for every sufficiently small fixed delta. Given any finite M,
choose delta making the last expression larger than $2M$, then take x large
for that delta and the given exclusion family. Eventually the collision ratio
exceeds M. This proves actual divergence, without interchanging two limits.

### Strongest attacks and findings

The main attempted failure was to let the rough-number residue error grow with
delta while an adaptive exclusion follows $V_{\delta(x)}$. The proof defeats
that attack by retaining every fixed positive-density class eventually; the
residue error is sublinear at each fixed delta. It never takes a simultaneous
limit with delta depending on x.

An explicit boundary test shows why the asymptotic qualification matters. At
$\delta=1/10$, the prime window contains only 7, and
$d_{1/10}=0.89m_{1000}/7\le89/2625$. But
$\log10<12/5$ (the first six positive exponential-series terms at $12/5$
exceed 10), so $0.2/\log^2 10>5/144>89/2625$.
Thus the tempting bound for *every* delta in the displayed interval is false.
The frozen proof expressly excludes that reading, and the counterexample does
not refute it. Prime powers, the prime case $k=1$, real cutoffs, and the zero
output convention were also checked above.

**Premises:** the exact PNT and Mertens interfaces and the elementary
inequalities rederived in A1--A3. **Mathematical verdict: refutation-failed.**
The checklist below applies separately to A and its consequences.

## A-epsilon: density order and quantitative cost of exclusions

### Restatement

For sufficiently small fixed delta, the class $V_\delta$ has input proportions
bounded above and below by positive constant multiples of
$1/\log^2(1/\delta)$, after taking lower and upper limits in x. This
order-of-magnitude claim does not require an assertion that its exact natural
density exists. The distinct-semiprime example is a density-zero set.

For each fixed $\varepsilon>0$ and any family with
$|E_x|\le\varepsilon x$ eventually, the claimed collision lower bound is

$$
\liminf_x\frac{C_{[1,x]\setminus E_x}(x)}x
\ge\sup_{\substack{0<\delta\le1/10\\d_\delta>\varepsilon}}
       \frac{(d_\delta-\varepsilon)^2}{2\delta}.
$$

The range of delta is inherited from its definition in A. For all sufficiently
small positive epsilon this is at least
$F(\varepsilon)=(\varepsilon^2/2)\exp(\sqrt{0.1/\varepsilon})$.
If the indexing set is empty, the display carries no nontrivial lower bound;
the subsequent quantitative claims concern small epsilon, where it is nonempty.
Therefore any choice of admissible finite constants $K(\varepsilon)$ in
B(3), if such constants exist, must satisfy that lower bound and grow faster
than every fixed power of $1/\varepsilon$ as epsilon decreases to zero.
This is not a claim that the optimal constant is attained, equals F, or exists
unconditionally.

### Weakest steps and strongest attacks

**AE1. Upper and lower proportions.** A2 supplies the lower bound
$0.89m_Z\sum_p1/p$. Dropping the f restriction gives the upper bound
$m_Z\sum_p1/p$ for the upper limiting proportion, by the same finite residue
count. A3 makes both of order $1/\log^2(1/\delta)$ with absolute comparison
constants for sufficiently small delta. No exact density is silently assumed.
For semiprimes, fix w. Those with a prime factor $p\le w$ number at most
$\sum_{p\le w}\pi(x/p)=o_w(x)$; those with both factors above w are
w-rough and number at most $m_wx+O_w(1)$. Taking x first, then $w\to\infty$,
proves their density zero, including squares if desired.

**AE2. Supremum and constant dependence.** For each delta with
$d_\delta>\varepsilon$, at least
$(d_\delta-\varepsilon-o_\delta(1))x$ constructed inputs remain. Squaring
this eventually positive lower bound gives the stated term. A lower limit
bounded below by every term is bounded below by their supremum; no maximizing
delta, compactness or uniform x-threshold is assumed.
Take $\delta_\varepsilon=\exp(-\sqrt{0.1/\varepsilon})$. As epsilon tends
to zero this enters A3's valid range, and
$0.2/\log^2(1/\delta_\varepsilon)=2\varepsilon$. Thus
$(d_{\delta_\varepsilon}-\varepsilon)^2/(2\delta_\varepsilon)
\ge F(\varepsilon)$. Any eventual upper bound K must dominate this lower
limit. For every fixed $a\ge0$,

$$
\log\bigl(F(\varepsilon)\varepsilon^a\bigr)
=\sqrt{0.1/\varepsilon}+(a+2)\log\varepsilon-\log2
\longrightarrow+\infty.
$$

The strongest attack was to let the family $E_x$, its starting point, or
$K(\varepsilon)$ depend adversely on epsilon, or to demand a uniform bound
at delta equal to $1/10$. Each epsilon is fixed before x tends to infinity;
the construction then fixes a sufficiently small delta depending on it. These
dependences are allowed. The false all-delta extension exhibited above is not
used. The derived bound is in the claimed ratio $C/x$, not in an unrelated
absolute count, and supplies only a necessary lower bound on K.

**Premises:** A1--A3, elementary counting, and the PNT/Mertens specializations
explicitly used in AE1. **Mathematical verdict: refutation-failed** for the
density-zero example, the order statement, the supremum inequality, and the
superpolynomial consequence separately.

## B: the four equivalent formulations

### Restatement

Write $F_x(T)=x^{-1}\#\{n\le x:r_x(s(n))>T\}$. For this particular
proper-divisor-sum map, the following four assertions are equivalent:

1. Every fixed set A of natural density zero has a preimage of natural density
   zero.
2. $\lim_{T\to\infty}\limsup_{x\to\infty}F_x(T)=0$.
3. For each $\varepsilon>0$, some finite $K\ge0$ and $x_0$ work for every
   real $x\ge x_0$: one may remove at most $\varepsilon x$ inputs, with the
   chosen set depending on x, leaving ordered collision count at most Kx.
4. For each $\varepsilon>0$, some $\eta>0$ and $x_0$ work simultaneously
   for all $x\ge x_0$ and all nonnegative integer target sets B of cardinality
   at most $\eta x$: their input capture is at most $\varepsilon x$.

The constants may depend on epsilon. There is no bound on the locations of B's
values and no requirement that B stay fixed with x. These are equivalences;
none of the four assertions is declared true by the theorem.

### Weakest steps, independently rederived

**B1. Necessity of fiber tightness: lower-output control and one sparse union.**
For every prime $p\mid n$, the divisor $n/p$ is proper, so
$s(n)/n\ge1/p$. Let $L\ge4$. If $n>x/\sqrt L$ and $s(n)<x/L$, then
$s(n)/n<1/\sqrt L$, so n has no prime divisor at most $\sqrt L$.
The residue count in A2 therefore gives

$$
\#\{n\le x:s(n)<x/L\}
\le (L^{-1/2}+m_{\sqrt L})x+O_L(1).
$$

This is an arithmetic statement about s, not an assumption that outputs are
uniformly comparable to inputs. Mertens lets its coefficient be made
arbitrarily small by fixing L sufficiently large.

If (2) fails, the decreasing function
$H(T)=\limsup_x F_x(T)$ has a positive limit. Choose eta strictly below that
limit. For every T there are arbitrarily large x with $F_x(T)>\eta$.
Choose L with $L^{-1/2}+m_{\sqrt L}\le\eta/4$ and a nonnegative constant
$c_L$ bounding the residue error. Successively choose integers $x_k$ with

$$
F_{x_k}(k)>\eta,\qquad
x_k\ge k^2Lx_{k-1},\qquad c_L\le\eta x_k/4,
\qquad x_0=1.
$$

Arbitrarily large witnesses exist at each stage; this construction does not
assume its conclusion or a termination property. Real witness points could
also be replaced by their integer parts, where the numerator stays the same
and the ratio does not decrease.

Set $A_k=\{m\ge x_k/L:r_{x_k}(m)>k\}$ and $A=\bigcup_{k\ge1}A_k$.
At most $\eta x_k/2$ inputs lie below the output threshold. At least
$\eta x_k/2$ of the heavy-fiber inputs consequently have their value in
$A_k\subseteq A$. Thus $s^{-1}(A)$ has positive upper density.

Each $A_k$ is finite and $|A_k|<x_k/k$, because its fibers are disjoint and
each has more than k members. For any sufficiently large real y, choose the
largest k for which $x_k/L\le y$. No later $A_j$ has a value at most y.
Although values in earlier sets may be arbitrarily large, counting their
*entire* finite cardinalities is an upper bound. Hence

$$
\frac{|A\cap[1,y]|}{y}
\le\frac{L}{x_k}\left(\frac{x_k}{k}
                         +\sum_{j<k}x_j\right)
\le\frac Lk+\frac{Lk x_{k-1}}{x_k}
\le\frac Lk+\frac1k\longrightarrow0.
$$

Here $k\to\infty$ with y. This is a bound for all sufficiently large y,
not just the sequence $x_k$. Overlap between the $A_j$ only reduces their
union's cardinality. Since $x_1\ge L$, the union contains positive values,
so it is a valid target under either convention for zero. This contradicts
(1), proving (1) implies (2).

**B2. Sufficiency of trimmed second moments: upper-output control.** By
pairing complementary divisors and interchanging finite sums,

$$
\sum_{n\le x}\frac{\sigma(n)}n
=\sum_{n\le x}\sum_{d\mid n}\frac1d
=\sum_{d\le x}\frac1d\left\lfloor\frac xd\right\rfloor
\le x\sum_{d\ge1}\frac1{d^2}<2x.
$$

The last strict inequality follows by comparison of the tail with
$\int_1^\infty t^{-2}dt$; no evaluation of $\zeta(2)$ is needed. If
$s(n)>Lx$ and $n\le x$, then $\sigma(n)/n>1+L$, so these inputs number
at most $2x/(L+1)\le2x/L$.

For a fixed density-zero A, fix epsilon and its constant K from (3), then
fix $L\ge1$. Outside the removed inputs and the preceding upper tail,
Cauchy--Schwarz bounds the capture by
$\sqrt{Kx\,|A\cap[0,Lx]|}=o(x)$, because L is fixed. Therefore

$$
\limsup_x x^{-1}\#\{n\le x:s(n)\in A\}
\le\varepsilon+2/L.
$$

Letting L increase and epsilon decrease proves (1). The chosen exclusions may
vary arbitrarily with x; the estimate needs no nesting and no global excluded
set. Crucially K is fixed while x tends to infinity.

**B3. The finite-fiber implications and an independent cross-check.** From
(2), choose T with $\limsup_x F_x(T)<\varepsilon$, using strict slack, so
$F_x(T)\le\varepsilon$ eventually. Removing all heavy fibers leaves counts
at most T, and $\sum_m r_m^2\le T\sum_m r_m\le Tx$. This is (3).
To get (4), instead use eventual heavy input mass at most
$\varepsilon x/2$ and put $\eta=\varepsilon/(2T)$, taking $T\ge1$.
Every target B captures at most that heavy mass plus $T|B|$ other inputs.

Conversely, for (4), use its eta and set $T=1/\eta$. The heavy-value set
$B_x=\{m:r_x(m)>T\}$ has fewer than $x/T=\eta x$ elements and hence
captures at most $\varepsilon x$ inputs. Monotonicity in T gives (2).
This uses exactly the uniformity over target sets promised by (4).

As an independent check on the composition, (3) also directly implies (2)
without either arithmetic output-tail estimate. For its excluded set, let
$t_m$ denote surviving counts. Since $|B_x|<x/T$ and
$\sum_m t_m^2\le Kx$, Cauchy--Schwarz gives

$$
F_x(T)\le\varepsilon+\sqrt{K/T}\qquad(x\ge x_0).
$$

Take the upper limit in x, then let T grow with epsilon fixed, and finally
let epsilon decrease. This independently checks the connection between
arbitrary partial trimming and whole-fiber tightness.

### Strongest attacks and findings

The strongest attack on B1 was that the $A_k$ have no upper bound on their
values, so a sparse union estimate valid only at selected endpoints might
conceal dense intermediate intervals. The all-y calculation in B1 answers that
attack: later sets have a lower support cutoff, and the *total* cardinality of
each earlier set is included regardless of where its values lie.

Two explicit abstract maps tested whether the argument had silently transported
an equivalence that fails outside the arithmetic setting:

- For $g(n)=n^2$, every fiber has size at most 1 and the collision count is
  $\lfloor x\rfloor$, yet the density-zero set of squares captures every
  input. Thus tightness or (3) alone cannot imply (1) for an arbitrary map.
  This g fails B2's large-output estimate: for every fixed L, almost all
  $n\le x$ have $g(n)>Lx$.
- For $f(n)=\lfloor\sqrt n\rfloor$, every density-zero A still has a
  density-zero preimage: with $y=\lfloor\sqrt x\rfloor$, its capture is
  at most $(2y+1)|A\cap[1,y]|=o(x)$. But completed fibers have sizes
  $2m+1$, so for each fixed T all but $O_T(1)+O(\sqrt x)$ of the inputs
  lie in fibers larger than T. Tightness fails. This f fails B1's
  small-output estimate: for every fixed L, all outputs at scale x are
  smaller than $x/L$ once x is sufficiently large.

These are attack models, not counterexamples to any assertion about s. They
show that both arithmetic interfaces are consequential and cannot be omitted.
The supplied proof establishes them independently, so neither attack breaks
Theorem B. The zero fiber, limsup slack, unrestricted target locations and the
order of all limits were checked explicitly.

**Premises:** Mertens' limit $m_w\to0$, finite residue counting, the local
prime-divisor bound and mean identity, and elementary finite inequalities.
Neither Theorem A's divergence conclusion nor PPT is needed for B; A2's
residue-count derivation is merely reused as an elementary calculation.
**Mathematical verdict: refutation-failed** for the four-way equivalence and
the statement that its trimmed second-moment route loses no logical strength.

## C: comparison with the finite-target theorem and its countermodel

### Restatement

The supplied PPT theorem gives, for each fixed $h(x)\to0$, a uniform
$o_h(x)$ capture bound on positive targets of size at most $x^{1/2+h(x)}$.
Theorem B(4) instead asks that, for every capture tolerance epsilon, a fixed
positive fraction eta of x be an admissible target size eventually. The
small-target theorem, even combined with asymptotically linear output size,
does not imply density-zero preservation for arbitrary maps. This last
nonimplication concerns a class of abstract maps; it is not a disproof for s
or a prohibition on arguments using additional arithmetic information.

### Weakest steps and strongest attack

**C1. Exact interface and limit order.** For s, define the maximal capture
proportion $M_x(\eta)$ over sets of at most $\eta x$ target values. It is
nondecreasing in eta. Only finitely many values occur among inputs at scale x,
so this maximum exists. Condition B(4) is equivalent to

$$
\lim_{\eta\downarrow0}\limsup_{x\to\infty}M_x(\eta)=0,
$$

using strict slack when passing from a limsup to an eventual bound. PPT
instead controls $M_x(x^{-1/2+h(x)})$ along a scale depending on x. It gives
no uniform error rate over choices of h. Adding target value zero changes
capture by at most one. Thus the phrase about the same kind of uniform control
is faithful, but it does not exchange the two limiting operations.

**C2. Reconstruction with a uniform fiber constant.** Put
$a_j=\lfloor j^{3/2}\rfloor$ for $j\ge1$. These integers increase strictly
and $a_1=1$, so $T(n)=\max\{a_j:a_j\le n\}$ is defined for every positive
integer n. Its fiber over $a_j$ is the integer interval
$[a_j,a_{j+1}-1]$. The mean value theorem gives

$$
a_{j+1}-a_j\le\tfrac32\sqrt{j+1}+1.
$$

If $a_j\le x$, then $j<(x+1)^{2/3}$, and for $x\ge1$ the displayed gap
is at most $4x^{1/3}$. This also bounds the last, truncated fiber at x.
Consequently, for every target B with $|B|\le x^{1/2+h(x)}$,

$$
\#\{n\le x:T(n)\in B\}
\le4x^{5/6+h(x)}=o_h(x).
$$

For example, eventually $h(x)\le1/12$, so the right side is at most
$4x^{11/12}$. The bound is genuinely uniform over all B and needs no
independence assumption.

For $A=\{a_j:j\ge1\}$, its counting function is at most
$(x+1)^{2/3}$, hence A has density zero. The same gap estimate at x=n gives
$0\le n-T(n)\le4n^{1/3}$, so $T(n)/n\to1$. Nevertheless
$T^{-1}(A)$ is every positive integer. Indeed, for every fixed eta, the
whole image up to x has at most $(x+1)^{2/3}\le\eta x$ values eventually,
and it captures all inputs; thus its analogue of $M_x(\eta)$ tends to 1.

The strongest attempted challenge was that the example might fail uniformity
in B, the prescribed varying exponent, an endpoint fiber, or the promised
linear output behavior. The explicit uniform constant and the last-fiber bound
settle all four. The example meets the abstract hypotheses and violates the
conclusion, so it supplies a concrete obstruction to the proposed general
inference. Splitting a sparse target into a growing number of small sets
cannot remove this obstruction merely by multiplying unspecified little-o
errors.

**Premises:** the exact PPT statement only for the comparison; elementary
calculus and counting for the countermodel; B for the linear-target
equivalence. **Mathematical verdict: refutation-failed** for the comparison
and for the countermodel's stated nonimplication separately. The implication
that this countermodel defeats is not a claim of the frozen subject.

## D: the sufficient condition and its consequences

### Restatement

For every fixed $\delta>0$, set
$D(\delta)=\{n\text{ composite}:s(n)\ge\delta n\}$ and
$m_{1/\delta}=\prod_{p\le1/\delta}(1-1/p)$, with an empty product equal
to 1. The distinct claims are:

1. The complement has upper natural density at most $m_{1/\delta}$, which
   tends to zero as delta decreases to zero.
2. **If** for each fixed delta there is a finite $K_\delta$ with
   $C_{D(\delta)}(x)\le K_\delta x$ for all sufficiently large x, then
   B(3), and therefore density-zero preservation, follows.
3. Any constants satisfying that bound for sufficiently small delta must obey
   $K_\delta\ge0.02/[\delta\log^4(1/\delta)]$; thus any such family of
   constants tends to infinity as delta decreases to zero.
4. For fixed delta, the semiprimes in $D(\delta)$ have at most
   $M_\delta=\pi(3/\delta)+1$ representatives per value, and their own
   collision count is at most $M_\delta x$. Their interactions with the
   remaining inputs are separated using the stated factor-two inequality.

No assertion that condition (D) holds, or that it is necessary, is made or
verified. The literature-status sentence is subject to the explicit source
limitation above.

### Weakest steps, independently rederived

**D1. Complement and sufficiency.** If a composite n has a prime factor
$p\le1/\delta$, then $s(n)\ge n/p\ge\delta n$, so n belongs to
$D(\delta)$. In fact, every integer outside D is either $(1/\delta)$-rough
or one of the finitely many primes at most $1/\delta$; 1 is already rough.
This slightly sharper inclusion proves the asserted upper density bound by
finite residue counting alone. Alternatively the printed union with all
primes works because the PNT gives prime density zero.

For any epsilon choose delta so that $m_{1/\delta}<\varepsilon$. The strict
inequality supplies the slack needed to turn an upper-density bound into
$|[1,x]\setminus D(\delta)|\le\varepsilon x$ for every sufficiently large
x. Combine that threshold with the hypothesized collision threshold for this
fixed delta. The resulting exclusions and $K=K_\delta$ satisfy B(3).
There is no uniform bound in delta and no claim that the complement has density
zero for one fixed delta.

**D2. Necessary size of an admissible constant.** Every composite member of
$V_\delta$ satisfies $s(n)/n\ge\delta$ by A1. Its prime members arise only
from $k=1$ and belong to a finite prime window for fixed delta. Removing that
finite set preserves A2's lower input proportion and the positive-value range
$[1,2\delta x]$. A3's pigeonhole calculation therefore gives

$$
\liminf_x\frac{C_{D(\delta)}(x)}x
\ge\frac{d_\delta^2}{2\delta}
\ge\frac{0.02}{\delta\log^4(1/\delta)}
$$

for sufficiently small delta. Any eventual upper constant must dominate this
number. Its divergence proves exactly the asserted necessary growth; it says
nothing about the existence of those upper constants.

**D3. Semiprimes and mixed collisions.** For distinct primes $p<q$,

$$
\frac{s(pq)}{pq}=\frac1p+\frac1q+\frac1{pq}\le\frac3p.
$$

Membership in D therefore implies $p\le3/\delta$. Given a value m and
one such p, the other prime would have to be $q=m-p-1$, so there is at most
one distinct-prime semiprime for that p. A square contributes value $p+1$,
which determines p, and adds at most one more representative. Thus the
semiprime fiber count u satisfies $u(m)\le M_\delta$. It follows that

$$
\sum_m u(m)^2\le M_\delta\sum_m u(m)\le M_\delta x.
$$

Writing v for the remaining admitted fiber counts, the full count obeys

$$
\sum_m(u(m)+v(m))^2
\le2M_\delta x+2\sum_m v(m)^2.
$$

Thus the semiprimes can be separated when deciding whether the whole count is
$O_\delta(x)$: conversely, $\sum_m v(m)^2\le C_{D(\delta)}(x)$.
The bound $M_\delta x$ is for their *own* sum of squares;
it is not a separate bound on every mixed pair involving a semiprime. The
frozen sentence supplies precisely the inequality that accounts for those
mixed terms.

### Strongest attacks and findings

I tested whether an upper-density estimate was used without eventual slack,
whether the positive-density construction contained excluded primes, whether
prime squares shared the distinct-prime parametrization, and whether mixed
collisions were silently discarded. D1 uses the strict inequality
$m_{1/\delta}<\varepsilon$; D2 removes only finitely many primes; D3 counts
squares separately and retains the factor two. These attacks fail against the
stated implications. Treating (D) as proved or as necessary would strengthen
the subject and is not supported by this report.

**Premises:** elementary divisor inequalities and residue counting, Mertens'
limit, B for D1's final implication, and A1--A3 for D2; no external theorem is
needed for D3. **Mathematical verdict: refutation-failed** for each of the four
numbered claims in this section's restatement: the complement estimate,
conditional sufficiency, necessary growth, and semiprime separation.
The claim about what is known in the literature
remains an uncertified characterization, not a refuted mathematical statement.

## Checklist verdicts

The groups A, A-epsilon, B, C and D above include their individually stated
subsidiary conclusions. Each row below applies to **every group**: a universal
inapplicability is stated explicitly; otherwise the group-specific examination
or finding is given. These are mathematical checklist findings, not a grade of
this report. The source qualifications and independence exposure are retained
rather than converted into favorable checklist findings.

### Canonical failure modes

| Failure mode | Applicability and verdict |
| --- | --- |
| Almost all upgraded to all | No failure found. A gives eventual divergence for each exclusion family, with x-thresholds allowed to depend on it. A-epsilon keeps small-epsilon and fixed-delta qualifications. B concerns density-zero preimages and uniform eventual bounds, never an all-input fiber bound. C's countermodel conclusion is actually all inputs, because its image is contained in A by definition. D uses upper density and strict epsilon slack, not a fixed density-zero complement. |
| Induction presupposing termination | B1 is applicable: every stage has arbitrarily large witnesses from the negation of tightness, and only finitely many lower bounds are imposed at that stage; no failure found. A, A-epsilon, C and D contain no induction or termination assertion; inapplicable to them. |
| Probabilistic or averaging heuristics presented as proofs | No failure found in any group. A's Markov bound is an inequality for an exact finite weighted sum; B's divisor mean and Cauchy--Schwarz are exact deterministic bounds. A-epsilon, C and D use exact counting and limiting inequalities. No heuristic distribution or probabilistic independence is assumed. |
| Circular use of the target or an equivalent statement | No failure found in any group. A is independent of E0955. A-epsilon bounds constants only if they satisfy the stated property. B proves both output-tail interfaces without the target, and its contraposition explicitly produces a violating sparse set. C uses PPT only as a comparison. D assumes (D) openly and then uses the already derived B implication. |
| Exceptional sets dropped from density arguments | No failure found. A subtracts the full permitted exclusion from a fixed positive proportion. A-epsilon subtracts epsilon before squaring. B2 includes removed inputs, the upper output tail and the sparse bounded-value part; B1 removes the entire small-output exceptional mass. C treats the initial and last fibers. D includes prime exceptions and the finite primes in V, and keeps mixed collisions. |
| Finite verification cited beyond base-case coverage | Inapplicable to numerical verification in every group: none is used and the finite census is excluded. The finite inequalities and finite parametrizations in A, B, C and D are proved for their full stated ranges, not inferred from checked cases. A-epsilon's asymptotic bounds follow from those arguments. No failure found. |
| Convergence of a relaxed or averaged system substituted for actual objects | No failure found. A, A-epsilon, B and D count the actual integer fibers of s. B's two attack maps are explicitly not replacements for s. C uses an abstract map only to refute an abstract implication, with all its hypotheses checked. |

### Named canonical patterns

| Named pattern | Applicability and verdict |
| --- | --- |
| Model-class transport instead of entailment | Classification of axiom-system extensions is inapplicable to all groups. The relevant transport risk is checked in B and C: abstract equivalences fail for the displayed test maps, the s-specific interfaces are proved, and the countermodel defeats only the implication whose hypotheses it satisfies. A, A-epsilon and D remain in the original arithmetic model. No failure found. |
| Uniformity over an infinite family asserted from finitely many instances | No failure found. A fixes delta before x; only the subsequent PNT/Mertens limit ranges over delta. A-epsilon fixes epsilon and then delta before x. B has a single K or T for all sufficiently large x at each epsilon, and C's fiber bound is uniform in every target B for each fixed h. D allows both K and the x-threshold to depend on delta. |
| Extremal claims audited in the claim's own units | No failure found. A and D use collision count divided by x. A-epsilon's supremum is a lower bound in exactly those units, with no maximizing parameter or attained optimum claimed. B's limsup and C's maximal capture are normalized input proportions; C's gap constant is only an upper bound, not a sharp constant. |
| Consequence sentences are claim surfaces | Applied to all groups. The convention identities, semiprime density-zero example, two-sided order bounds, supremum, superpolynomial growth, corrected-route equivalence, PPT comparison, countermodel, D complement, conditional sufficiency, necessary growth and semiprime separation are each addressed. No mathematical failure found. The literature-status sentence about equivalence has insufficient source coverage and is not certified. |
| Carry hypotheses actually used by quantified arguments | No failure found. Fixed-parameter residue constants and nonempty positive-density classes are handled in A; A-epsilon squares only after positivity is ensured. B1 uses lower output support and bounds full finite cardinalities rather than assuming bounded values. B2 uses its independently established upper tail. C verifies both sparse-image size and linear output behavior. D retains its bound as a hypothesis. |
| A composition inherits its unproved premises | No failure found in the mathematical implications. All local supporting steps are rederived in an acyclic order below. The three external theorem statements are used only at their declared interfaces. D's antecedent remains unproved and explicit. The literature-wide characterization is not promoted to a premise or certified consequence. This qualification applies to every group using a source. |
| Reproducibility notes are claims | Inapplicable to computational reruns in all groups: the commissioned analytic subject contains no included runner or numerical coverage claim. Its mention of an exact computation points to the expressly excluded census. This report's reproduction evidence is the displayed derivation and retained mathematical inputs; it asserts no execution result. |
| Verifier quotations are claims | Inapplicable to all mathematical groups: no prior verifier ruling is present in the allowed subject or invoked here. The excluded standing and review text was not read. The grader's exposure ruling remains required and is not anticipated or quoted. |
| Verdict words spelled in full | Applicable to this report's verdict surfaces for all groups: refutation-failed is written in full. The opposite verdict, refuted-as-stated, is never used as an abbreviation or confused with it. No tier or self-grade is asserted. |
| Certified-bracket functions fail loudly | Inapplicable to all groups: no bracket routine, capped iteration or numerical enclosure is run or relied on. A's constants are justified by exact inequalities and series with known remainder signs. |
| A harness leg with no failing input is decoration | Inapplicable to all groups: there are no executable verification legs. The analytic attacks have explicit potential failure conditions, including incorrect limit order, missing tail bounds and discarded mixed terms; the test maps demonstrate actual failures when those hypotheses are removed. No tautological code is offered as evidence. |
| A gate reading caches instead of rerunning is defective | Inapplicable to all groups: no gate or cached success result was read, run or used. The verdict rests entirely on the retained reasoning and declared external theorem interfaces. |

### Erdos-specific checklist

| Item | Applicability and verdict |
| --- | --- |
| Quantifiers and scope | Checked for every group; no failure found. A allows arbitrary x-dependent o(x) exclusions; A-epsilon is eventual in small epsilon and its delta lies in the inherited range. B retains its four different quantifier orders, upper limits and fixed-target versus varying-target distinction. C fixes h before invoking uniformity. Every assertion of D has its fixed-delta or conditional scope. Boundary cases are covered in the derivations. |
| Circularity | Checked for every group; no failure found. The dependency order below has no cycle. B1 constructs a target violating (1) from failure of (2); it does not assume any sparse target property. A-epsilon's reference to the definition of an admissible K assumes no truth of B(3). D does not use its desired conclusion to justify its antecedent. |
| Model and convention changes | Checked for every group; no failure found. Ordered pairs and diagonals are consistent throughout A, A-epsilon, B and D. Value zero has one input. B's square and square-root maps test missing arithmetic interfaces, and C's abstract construction stays an abstract countermodel. No statement about s is refuted or proved by relabeling those maps. |
| Finite and statistical overreach | No failure found in any group. No sample, experiment or finite census is used. The deterministic mean bounds of A and B are not statistical inference. C's estimates hold for every integer input and every permitted target, and D's semiprime parametrization is exhaustive. |
| Uniformity | Checked for every group; no failure found. The fixed-Z residue bound holds for all real arguments but its constant depends on Z. All limiting operations are in the stated order. The finite sums over p in A are at fixed delta. B and C's bounds are uniform over target locations; PPT's error may depend on h. D asserts no uniform x-threshold as delta varies. |
| Extremal conclusions | Checked for every group; no failure found. The A-epsilon supremum is justified term by term and need not be attained. Its lower bound on K and D's lower bound on K-delta are in C/x units and do not assert sharpness or existence. A's divergence is distinguished from a mere subsequence. B and C use the correct upper-limit capture quantities. |
| Consequences and composition | Checked separately for all listed surfaces; no mathematical failure found. The external-source scope is preserved and local steps are proved before use. The D knowledge-status characterization remains unsupported by the available source coverage. No conclusion is inferred from an omitted finite census or later sieve route. |
| Computation | Inapplicable to all groups as a computational evidence requirement. No code, floating-point bound, finite search or numerical cap is involved. The decimal constants in A and A-epsilon denote exact rationals, with their required inequalities justified analytically. |
| Reproduction | For all groups, the noncomputational evidence consists of the unchanged subject and countermodel snapshots, retained source interfaces, and complete derivations in this report. No executable rerun or cached output claim is made. The ordinary-clone custody requirement applies to the stated assets and report paths. |
| Source and verdict fidelity | The source applications for A, A-epsilon, B, C and D were checked at exactly the supplied statement interfaces; their original proofs and PDF fidelity were not inspected. Mertens is supplied through Tao's exposition, so original-primary-proof coverage is not claimed. The D knowledge-status sentence is uncertified. No prior verification ruling is quoted, and the independence exposure requires a separate materiality ruling. These limitations are explicit; no broader source or acceptance coverage is asserted. |

The neighboring statistical discipline is inapplicable: there are no correlated
samples or statistical conclusions. Evidence coverage is matched to the actual
analytic derivations, statement-only external reading and excluded census as
required by the evidence standard.

## Premises and verification order

The following order records substantive mathematical consumption, not merely
shared notation:

1. Fix the conventions and the exact external PNT and Mertens statements.
   Establish finite rough-number residue counting, divisor-product bounds,
   Cauchy--Schwarz and Markov specializations, and the elementary inequalities
   used above.
2. Establish A1--A3 and Theorem A. Their conclusion does not consume B, PPT,
   D, or the countermodel.
3. Derive the A-epsilon consequences from the same construction. The definition
   of a constant admissible in B(3) is used, but B(3)'s truth is not assumed.
4. Establish B from its elementary finite-fiber arguments and its two arithmetic
   tail estimates. It consumes the residue-count calculation and the Mertens
   limit, not Theorem A's divergence conclusion.
5. Check C's comparison using the independently established B equivalence and
   PPT's exact supplied statement. Reconstruct its countermodel directly; its
   proof does not consume PPT.
6. Establish D's complement estimate, invoke B for the sufficient implication,
   use A's construction for necessary growth, and prove the semiprime estimate
   directly.

The source-owned statements are ordinary identified literature premises, with
reading depth and exact specializations recorded above. Their uninspected
proofs are not silently relabeled as local proof coverage. All remaining
support consists of elementary integer factorization, finite counting,
inequalities and calculus as displayed. No native L-claim, pending local grade,
unavailable local lemma, announcement or prior author's computation is used.
Accordingly there is no current or prospective native dependency-tier reading
to substitute for a live ledger check; the consumed-native-claim list is empty
on the examination date. The conditional theorem keeps (D) as an assumption,
not as an independently warranted result.

## Verdict and limits

| Assessed conclusion | Mathematical verdict |
| --- | --- |
| Ordered/diagonal collision conventions and their counting consequences | refutation-failed |
| Theorem A, including its construction and asymptotic estimates | refutation-failed |
| Semiprime density-zero example and the stated density order of V-delta | refutation-failed |
| Positive-density exclusion supremum and superpolynomial necessary growth of K(epsilon) | refutation-failed |
| Theorem B's four-way equivalence and corrected-route consequence | refutation-failed |
| Exact comparison to PPT Theorem 1.2 | refutation-failed |
| Supplied abstract countermodel and the scope of its nonimplication | refutation-failed |
| D complement density estimate and conditional sufficient implication | refutation-failed |
| Necessary growth of any admissible K-delta | refutation-failed |
| Semiprime fiber, self-collision and separation estimates in D | refutation-failed |

The strongest attempted failures were the nonuniform rough-number errors,
adaptively varying exclusions, loss of density control between diagonal
thresholds, transport to maps lacking the two arithmetic output bounds, an
invalid extension of small-target uniformity, and missing mixed collisions.
The retained arguments explain why each fails against the frozen mathematical
claims. No counterexample to those claims or unproved essential inference in
their supplied analytic proofs was found within the exact literature interfaces
authorized by the commission.

This is not an unqualified certification of every characterization in the
packet. The assertion about what is known concerning equivalence of (D) remains
unsupported by the closed source set. The distinction between an expository
Mertens statement and primary-proof inspection also remains explicit. These
limitations do not constitute a disproof of an analytic theorem or a proof of
an absent equivalence. Neither (D) nor a full resolution of E0955 is established
by this review. No numerical census, later sieve route, external theorem proof,
original-source transcription fidelity, or subsequently changed subject text is
covered.

The complete mathematical examination is retained at the stated scope. A
separate grader must judge the report contract and independence, including the
disclosed motivational exposure, before any acceptance or tier assertion.
