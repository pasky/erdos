---
name: research/erdos_25/independent/harmonic_capacity_and_narrow_windows
title: Independent investigation of Erdős Problem 25
desc: Unverified independent input; the checked two-class result, moment certificate, and superseded targets are recorded in the topical notes.
tags: []
sources: []
created: 2026-09-22T15:19:56Z
updated: 2026-10-13T05:28:09Z
---

# Independent investigation of Erdős Problem 25

***

## Status and scope

**This investigation did not resolve the problem.** No proof of existence of
logarithmic density in full generality, and no counterexample satisfying the
distinct-modulus hypothesis, was obtained.

Only the supplied local problem and sources were used. No supplied problem
page or source was edited. The claims below are separated into proved facts,
explicit calculations, unsuccessful constructions, and unproved targets.
Computational searches are not used as proofs of a general assertion.

The main useful results of this investigation are a self-contained periodic
compression argument, a sharp bound for one or finitely many early hits per
distinct modulus, a two-class Dirichlet inequality, and explicit examples
showing that several tempting harmonic compression assertions are false.

## 1. Exact problem, conventions, and elementary cases

Let

$$
1\le q_1<q_2<\cdots,\qquad 0\le a_i<q_i,
$$

and put

$$
B_i=\{n\ge q_i:n\equiv a_i\pmod{q_i}\}
    =\{q_i t+a_i:t\ge1\},\qquad
B=\bigcup_i B_i,\qquad A=\mathbb N\setminus B.
$$

In particular, the first eligible point is (q_i+a_i), including (q_i)
when (a_i=0). The smaller representative (a_i>0) is not removed by this
congruence. This convention is maintained throughout these notes.

For a set (S\subseteq\mathbb N), natural density, when it exists, is

$$
d(S)=\lim_{X\to\infty}\frac{\#(S\cap[1,X])}{X}.
$$

Write

$$
L_S(X)=\frac1{\log X}\sum_{\substack{n\le X\\n\in S}}\frac1n,
\quad
\underline{\operatorname{ld}}(S)=\liminf L_S(X),
\quad
\overline{\operatorname{ld}}(S)=\limsup L_S(X).
$$

Logarithmic density exists precisely when the latter two quantities agree.
Natural density implies logarithmic density with the same value; the
converse is not asserted. Set (H_N=\sum_{n\le N}1/n).

For a finite initial segment, define (A^{(k)}=\mathbb N\setminus
\bigcup_{i\le k}B_i). Beyond (q_k), this set is periodic modulo

$$
L_k=\operatorname{lcm}(q_1,\ldots,q_k).
$$

Thus its natural and logarithmic densities agree; denote the common value
by $\delta_k$. These decrease to $\delta\in[0,1]$, and

$$
\overline d(A)\le\delta,
\qquad \overline{\operatorname{ld}}(A)\le\delta.
$$

Consequently $\delta=0$ already implies natural density zero. The difficult
case necessarily has $\delta>0$.

The following standard positive cases were checked against Chojecki's full
source, Sections 2–3, and have elementary proofs:

* If $\sum_i1/q_i<\infty$, then (A) has natural density $\delta$.
  Indeed, the activation convention gives
  $\#(B_i\cap[1,X])\le\lfloor X/q_i\rfloor$, so the infinite tail has
  upper natural density at most $\sum_{i>k}1/q_i$. This justifies the
  infinite union bound, rather than merely citing finite additivity.
* If the moduli are pairwise coprime, then
  $\delta_k=\prod_{i\le k}(1-1/q_i)$. A convergent reciprocal sum is the
  previous case; a divergent sum gives $\delta=0$.
* For zero residues, the Davenport–Erdős theorem gives logarithmic density
  for the union of multiples and its complement. Natural density can fail.
  The relevant full 1936 and 1951 source passages were examined. Their
  divisibility closure and smooth-factor identities cannot simply be
  transferred to arbitrary residues.

## 2. Periodic union compression: proved

For a finite family of full residue classes let

$$
U=\bigcup_i[a_i]_{q_i},\qquad
U_0=\bigcup_i[0]_{q_i}.
$$

Their densities are proportions in the cyclic group modulo the least common
multiple. Equivalently, use Haar measure $\mu$ on the profinite integers.
Then

$$
\boxed{\mu(U)\ge\mu(U_0).} \tag{2.1}
$$

Here is a complete finite proof. Write the cyclic group, by CRT, as a
product of prime-power groups. Each congruence class is a product of cosets
of subgroups in these coordinates. In one coordinate replace every coset
by the subgroup of the same cardinality containing zero. Fix the other
coordinates. The participating old fibers have union cardinality at least
their largest cardinality. The replacement fibers are nested subgroups,
so their union has exactly that largest cardinality. The union therefore
cannot increase under this replacement. Repeat for every prime coordinate.
The resulting union is exactly (U_0), proving (2.1).

This argument also allows repeated moduli. Distinctness enters the later
capacity bounds, not (2.1).

The supplied Filaseta–Ford–Konyagin–Pomerance–Yu full source, Introduction,
paragraph beginning “Similar to the definition of $\delta^-(S)$,” explicitly
attributes the equivalent maximum-uncovered-density statement to Rogers.
Thus (2.1) is not claimed as a new theorem.

**Limitation:** (2.1) compares completed periodic unions. It does not compare
their delayed finite harmonic sums. Section 6 gives exact counterexamples
to two stronger comparisons that were considered.

## 3. Sharp harmonic capacity for moduli and early hits: proved

### 3.1 Harmonic inequality for a finite set of multiples

Let (D\subseteq[1,X]\cap\mathbb N) be finite, let

$$
M(D)=\bigcup_{q\in D}q\mathbb N,
\qquad d_0=d(M(D)),\qquad N=\lfloor X\rfloor.
$$

Then

$$
\sum_{\substack{n\le X\\n\in M(D)}}\frac1n\le d_0 H_N. \tag{3.1}
$$

Proof: for each prime (p\le N), independently choose a nonnegative integer

$$
\mathbb P(V_p=j)=(1-1/p)p^{-j},
$$

and set (Z=\prod_{p\le N}p^{V_p}). Every positive integer (n\le N) has
probability (c/n), where (c=\prod_{p\le N}(1-1/p)). Thus conditioning

on (Z\le N) gives exactly the probability weights (1/(nH_N)).

The event (Z\in M(D)) is increasing in all the valuations, whereas

(Z\le N) is decreasing. Independent-coordinate association therefore gives

$$
\mathbb P(Z\in M(D)\mid Z\le N)
\le\mathbb P(Z\in M(D))=d_0.
$$

For completeness, the association used here follows in one coordinate from

$$
\operatorname{Cov}(f(V),g(V))
=\tfrac12\mathbb E[(f(V)-f(V'))(g(V)-g(V'))]\ge0
$$

for increasing (f,g), with (V') an independent copy; induction gives the
product version. Apply this to the increasing event and the complement of
the decreasing event. The equality with (d_0) is the usual independent
Haar valuation distribution. This proves (3.1).

### 3.2 One modulus supplies only one reciprocal term

If (U) consists of one selected class for each distinct (q\in D\subseteq
[1,X]), and (u=\mu(U)), then (2.1) and (3.1) give

$$
\boxed{\sum_{q\in D}\frac1q\le u H_{\lfloor X\rfloor}.} \tag{3.2}
$$

Indeed, (D\subseteq M(D)), and distinctness permits counting each (q)
only once. This is a uniform finite-family inequality.

In particular, if at most one endpoint (x_q\in[q,X]) is selected per
modulus, then

$$
\sum_q\frac1{x_q}\le u H_{\lfloor X\rfloor}. \tag{3.3}
$$

The endpoint need not even satisfy its selected congruence for (3.3).

For the first (K) eligible representatives of every class, the union bound
and (q t+a\ge qt) give

$$
\boxed{
\sum_{\substack{n\le X\\
 n=q t+a_q\text{ for some }q,\ 1\le t\le K}}\frac1n
\le H_K\,u H_{\lfloor X\rfloor}.
} \tag{3.4}
$$

Only moduli (q\le X) need be included in (U) here. With at most (s)
classes per modulus the corresponding bound has an extra factor (s).

**Precise limitation:** (3.4) controls boundedly many early hits of a family
whose *whole* periodic union has small measure. It does not control the
unshadowed tail relative to a previous family. It also has the factor
(H_K). It would be an overstatement to conclude from it alone that every
possible counterexample must use unbounded quotients. What it rules out is
a small-whole-footprint construction obtaining a fixed positive fraction
of $\log X$ from a fixed number of hits per modulus.

### 3.3 Dirichlet version

For $s>1$, the distribution (n^{-s}/\zeta(s)) has independent prime
valuations with tails (p^{-as}\), coordinatewise dominated by Haar
valuation tails (p^{-a}\). The same increasing-event argument gives

$$
\sum_{n\in M(D)}n^{-s}\le d_0\zeta(s).
$$

Consequently, for distinct moduli and endpoints (x_q\ge q),

$$
\sum_q x_q^{-s}
\le\sum_q q^{-s}
\le\sum_{n\in M(D)}n^{-s}
\le\mu(U)\zeta(s). \tag{3.5}
$$

This also agrees with the finite Dirichlet inequality in the checked
Davenport–Erdős 1936 source.

## 4. Why the supplied multi-residue counterexample does not transfer

Wang's full source, particularly Lemmas 4–7 and Section 4, was inspected.
Its finite block at (Q=2^j) has at least (3Q/8) endpoints in

$$
[11Q/10,19Q/10],
$$

with assigned moduli in $[19Q/20,21Q/20]$, all strictly smaller than
their endpoints, and completed union measure at most

$$
\eta_j=\exp(-k_j/100),\qquad
k_j=2\lfloor\sqrt j/8\rfloor.
$$

The same modulus is used for many different residues. Thus this is not a
distinct-singleton block for Problem 25.

There is a rigorous obstruction stronger than merely observing these
repetitions. If such a block were singleton, each modulus could witness at
most one of these endpoints: the endpoint interval has diameter (4Q/5),
smaller than every assigned modulus. Thus (3.3) would give

$$
\frac{15}{76}
\le\sum_{m\in E_j}\frac1m
\le\mu(U_j)H_{\lfloor19Q/10\rfloor}.
$$

Thus its footprint would have to be $\gg1/\log Q$, whereas Wang's
$\eta_j$ is (o(1/\log Q)). A direct singleton analog with those
parameters is impossible. This does not rule out a construction whose
different-scale footprints overlap substantially.

Two attempted repairs failed more concretely:

1. Wang's label sets (S) have $|S|=k/2+O(\sqrt k)$, and a modulus with
   label (S) must be divisible by
   $d_S=\prod_{i\in S}p_i$, with (p_i>4^{k+1}). The number of available
   distinct moduli in a fixed-ratio interval of size (Q) with these
   incidences is at most
   $$
   O\!\left(Q\sum_S\frac1{d_S}+2^k\right)
   \le O\!\left(Q,2^k4^{-(k+1)(k/2-\sqrt k)}+2^k\right)=o(Q).
   $$
   Retaining the incidence skeleton cannot supply a positive fraction of
   (Q) different moduli.
2. Refining each old class to a class modulo a distinct multiple of its
   modulus keeps the new full class inside the old one, but loses capacity.
   The available modulus density is at most $\sum_S1/q_S=O(2^k/Q)$.
   Accumulating enough reciprocal mass over an enormous multiplier range
   also pushes the endpoint range beyond the old finite periodic structure,
   destroying the desired local anomaly. No successful refinement was found.

A further attempted repair used sparse labels of probability (1/p), so
that endpoint label patterns occur in the same proportions as prime
divisibility patterns of moduli. With one marked residue modulo each prime,
these labels are just divisibility of a common translate (n-R). This fixes
the counting mismatch but returns to divisor-window behavior rather than
Wang's rapidly decaying footprint. No adequate multi-scale construction
was obtained from this idea.

Wang's recovery-and-epoch mechanism itself is sound for its stated
multi-residue blocks: a fixed finite past is eventually periodic, later
moduli can be chosen larger than a recovery cutoff, and long epochs collect
harmonic deletion. For Problem 25, such an argument would still need legal
singleton blocks and separation of their modulus ranges. No infinite
singleton construction was specified here, so none is claimed to satisfy
those obligations.

## 5. Candidate finite domination inequalities and a two-class result

For a finite distinct-singleton family let (U_{\rm tr}\) denote its delayed
union, and (U) its full periodic union. Two strong possible targets are

$$
\sum_{\substack{n\le X\\n\in U_{\rm tr}}}\frac1n
\le\mu(U)H_{\lfloor X\rfloor}, \tag{H}
$$

and

$$
\sum_{n\in U_{\rm tr}}n^{-s}\le\mu(U)\zeta(s)
\qquad(s>1). \tag{D}
$$

**Neither (H) nor (D) was proved or refuted in general.** The direct
one-endpoint inequality is not a proof of either statement for all hits.
Splitting by the quotient (t) loses an additional harmonic or zeta factor.

(H) would settle the problem: apply it at cutoff (X) to all moduli at most
(X), and combine the resulting upper bound for (B) with the lower bound
from every fixed finite initial union. A general proof of (D) would give
the analogous Dirichlet limit; a nonnegative Tauberian step would then be
needed to state the logarithmic-density conclusion.

Both assertions are false if arbitrary multiplicity is permitted. Wang's
finite blocks have eligible harmonic mass bounded below by (15/76), but
$\mu(U_j)H_{2Q}\to0$. For (D), take (s=1+1/\log Q). Their Dirichlet
mass stays bounded below absolutely, while
$\mu(U_j)\zeta(s)\to0$. Thus an argument ignoring denominator multiplicity
cannot prove the required result.

### A proof of (D) for two classes

For $s>1$, define the shift loss

$$
\ell_s(q,a)=\sum_{t\ge1}\bigl((qt)^{-s}-(qt+a)^{-s}\bigr)\ge0.
$$

A single delayed class has Dirichlet mass
$q^{-s}\zeta(s)-\ell_s(q,a)$, so (D) holds for one class.

Consider distinct moduli (m<n). If the classes are incompatible, their
union has density (1/m+1/n), and the single-class bounds suffice.
Otherwise let (L=\operatorname{lcm}(m,n)), and let (b\in[0,L)) be the
common CRT representative. The union density is the same as for the two
zero classes.

If (b=0), the intersection mass is (L^{-s}\zeta(s)). If (b\ge n),
the first intersection point is eligible, and

$$
\sum_{t\ge0}(b+tL)^{-s}\ge L^{-s}\zeta(s).
$$

In both cases inclusion–exclusion bounds the union mass by that of the
two zero classes. If (0<b<n), then (b=a_n), and the intersection mass is

$$
L^{-s}\zeta(s)-\ell_s(L,b).
$$

Since (L\ge n),

$$
\ell_s(L,b)\le\ell_s(n,b)
$$

term by term: (x^{-s}-(x+b)^{-s}) decreases with (x). Hence the
intersection's shift loss is absorbed by the (n)-class shift loss. Again
the union mass is no larger than the zero-class union mass. The increasing
valuation argument in Section 3.3 bounds the latter by its density times
$\zeta(s)$. This proves (D) for two classes.

For three or more classes, alternating higher intersections obstruct this
simple absorption. No conserving extension was found.

## 6. Exact counterexamples to stronger compression ideas

These calculations were independently recomputed with rational arithmetic
before this record was written. They do **not** disprove (H).

### 6.1 Normalized harmonic mass is not maximized by zero residues

At (X=100), compare moduli $4,7,9,10,18$, first with all residues zero,
then with only the residue modulo 18 changed to 4. Let the eligible harmonic
sums be (h_0,h_1), and periodic union densities (u_0,u_1). Exact
enumeration in one common period and through (X=100) gives

$$
u_0=\frac7{15},\quad u_1=\frac{17}{35},
\quad h_0=\frac{12037863923159}{6746328388800},
\quad h_1=\frac{17081934714855317}{9195245593934400}.
$$

In particular,

$$
u_0h_1-u_1h_0
=\frac{113383068679483}{482750393681556000}>0.
$$

Thus (h_1/u_1>h_0/u_0). Periodic compression is not monotone for this
normalized harmonic ratio.

### 6.2 Even at equal periodic density, shifting can increase harmonic mass

At (X=1000), compare

$$
0\pmod4,\quad0\pmod9,\quad0\pmod{11},\quad a\pmod{210}
$$

for (a=0) and (a=48). Both full unions have density (274/693).
Outside the first three classes, the last class adds only (210) in the
first system, and adds (258,678) in the second. All three displayed points
respect activation (n\ge210\). Therefore

$$
h_{48}-h_0
=\frac1{258}+\frac1{678}-\frac1{210}
=\frac{601}{1020390}>0.
$$

This also refutes a proposed comparison of the additive harmonic deficit
against the all-zero system.

Targeted exhaustive or stochastic finite searches found no counterexample
to (H), including families of divisors of several moderately large common
periods. These searches cover only finite cases, have no established
extremal completeness, and are not evidence on which any theorem here
depends. The scripts and detailed search notes are not retained.

## 7. A uniform obstruction to common-translate narrow-window blocks

The following partial result was proved during the investigation. It rules
out a particular proposed construction, not all compatible-residue systems.

**Proposition.** Fix (K,C>1). Uniformly over integers (R=R_N),

$$
\sum_{\substack{N\le n\le N^C\\
\exists q\in[N,KN]\cap\mathbb N:\ q\mid n-R}}\frac1n
=o(\log N). \tag{7.1}
$$

Discarding ineligible points (n<q), or taking only a subset of the moduli,
can only decrease the left side.

Here are the details. For fixed $\alpha>0$, first consider an integer
interval of length (H\ge N^{1+\alpha}). Choose
$z=N^\epsilon$, where (2\epsilon<\min(1,\alpha)), and put

$$
s_z(v)=\sum_{p\le z}1_{p\mid v},\qquad
\lambda=\sum_{p\le z}\frac1p=\log\log N+O_\epsilon(1).
$$

For any interval (J) of (T) integers, expansion of the square and CRT
give

$$
\sum_{v\in J}(s_z(v)-\lambda)^2\ll T\lambda+z^2. \tag{7.2}
$$

Each one-prime or two-prime count has error (O(1)); the same estimate
holds with any subset of the primes omitted and its own reciprocal mean.
The prime reciprocal asymptotic used here is the classical one also used
in the supplied sieve literature.

Only (O_K(N/\lambda)) moduli (q\in[N,KN]) have
(s_z(q)<3\lambda/4). Their progressions cover (O_K(H/\lambda)) points.
Only (O(H/\lambda)) points of the translated interval have
(s_z(n-R)\ge3\lambda/2).

For a remaining modulus and point write (n-R=qt), and set

$$
X_q(t)=\sum_{\substack{p\le z\\p\nmid q}}1_{p\mid t},
\qquad \lambda_q=\sum_{\substack{p\le z\\p\nmid q}}\frac1p.
$$

Uniformly for (q\le KN), $\lambda_q=(1-o(1))\lambda$. Indeed,
splitting prime divisors of (q) at $\log N$ gives

$$
\sum_{p\mid q}\frac1p
\le\sum_{p\le\log N}\frac1p
 +\frac{\log(KN)}{(\log N)(\log\log N)}
=O(\log\log\log N)=o(\lambda).
$$

Since (s_z(n-R)=s_z(q)+X_q(t)), the remaining points have
(X_q(t)<3\lambda/4). Their (t)'s occupy an interval of length
(H/q+O(1)), so (7.2) bounds their number by

$$
O\!\left(\frac{H}{q\lambda}+\frac{z^2}{\lambda^2}\right).
$$

Summing over (q\in[N,KN]) gives (O_K(H/\lambda)), since
(Nz^2=o(H)). All these estimates are uniform in the translate (R).

The initial range $[N,N^{1+\alpha}]$ has harmonic mass at most
$\alpha\log N+O(1)$. Split the rest through (N^C) into dyadic
intervals. Each contributes (O_{K,\alpha}(1/\lambda)), and there are
(O_C(\log N)) intervals. First let (N\to\infty), then
$\alpha\downarrow0$, proving (7.1).

This shows why simply translating the zero classes from a fixed-ratio
modulus window does not create a sufficiently long logarithmic deletion
epoch. It does not handle arbitrary independently chosen residues, growing
window ratios, or the general conditioned-tail problem.

## 8. Conditional tails: exact reduction and a quantifier gap

An initially attractive proposal was to prove only a uniform continuity
bound for families with a small full periodic union, then apply it to the
unshadowed tail after conditioning on a finite prefix. The conditioning
step has a nontrivial loss.

Fix a prefix of period (L), with allowed residue representatives
(r\in R\subseteq\{1,\ldots,L\}). Write

$$
n=L(u-1)+r,\qquad u\ge1.
$$

For a later modulus (q), put (g=(q,L)) and (m=q/g). The class meets
this fiber iff (a\equiv r\pmod g); if compatible it pulls back to one
class modulo (m), since $(m,L/g)=1$.

The activation condition remains exactly

$$
gm\le L(u-1)+r. \tag{8.1}
$$

It implies only (m\le Lu), not the original-form condition (m\le u).

Moreover, distinct original moduli may produce the same quotient modulus.
For a fixed (m), the possible (g\mid L) satisfy $(m,L/g)=1$, giving
the exact upper multiplicity

$$
\prod_{\substack{p^\ell\parallel L\\p\nmid m}}(\ell+1)
\le\tau(L). \tag{8.2}
$$

If (\nu_r) is the full tail-union measure inside the pulled-back fiber,
then

$$
\frac1L\sum_{r\in R}\nu_r
=\mu(U_{\rm tail}\setminus U_{\rm prefix}). \tag{8.3}
$$

The harmonic change of variables has bounded error:

$$
0\le\sum_{u\in S}\left(\frac1{L(u-1)+r}-\frac1{Lu}\right)
\le\frac1r
$$

for every subset (S) and cutoff. Separate (u=1), and for (u\ge2)
bound the difference by $(L-r)/(L^2u(u-1))$. Summing over fibers costs
at most (H_L). The finitely many discrepancies of the initial delayed
prefix also have bounded harmonic mass.

These formulas rigorously account for distinctness, multiplicity, and
activation. They do **not** give the hoped-for tail estimate. For example,
a hypothetical singleton estimate with coefficient (f(\mu(U))\to0)
typically becomes one with factors depending on (L\), such as
$\tau(L)f(L\epsilon)+O(L\tau(L)\epsilon)$, where $\epsilon$ is the
unshadowed tail measure. Although $\epsilon_k\to0$ as the prefix grows,
its periods (L_k\) may grow much faster. One cannot infer that

$$
L_k\epsilon_k\to0\quad\text{or}\quad
\tau(L_k)f(L_k\epsilon_k)\to0.
$$

Thus weak unconditioned continuity was not shown sufficient. This is an
identified gap, not an established local-to-global reduction. Further
formulas were recorded in a companion note that is not retained.

## 9. First-kill decomposition and unproved charging ideas

Let

$$
E_i=B_i\setminus\bigcup_{j<i}B_j.
$$

They are disjoint, eventually periodic, and their densities satisfy

$$
e_i=d(E_i)=\delta_{i-1}-\delta_i,\qquad
\sum_i e_i=1-\delta.
$$

For (j<i), compatibility is
(a_i\equiv a_j\pmod{(q_i,q_j)}\). A compatible earlier class induces
one forbidden residue on (t\) modulo

$$
r_{ij}=\frac{q_j}{(q_i,q_j)}
$$

in the representation (n=a_i+q_i t\), (t\ge1). Thus (E_i) is a
translate-dilate of a finite periodic quotient sieve of density (q_i e_i).
There is no extra activation condition from earlier moduli here, since
(n\ge q_i>q_j).

Chojecki's full source, Sections 4–6, was checked for this representation
and its tower example. In that example, with $(u,6)=1$,

$$
m_j=u2^{r-j}3^j\quad(0\le j\le r),
$$

and residues

$$
a_r=0,\qquad
a_j\equiv u3^r(1+2^{r-j-1})\pmod{m_j}\quad(j<r),
$$

the top first-kill set is

$$
E_{m_r}=\{u3^r(1+2^r t):t\ge0\}.
$$

Its density is (1/(u6^r)), but its first point contributes (1/(u3^r)).
This disproves a naive individual bound using only the first-kill density
and an entropy-sized error. It does not disprove a global bound: the
preceding scaffold has reciprocal scale (O(1/(u2^r))), larger than that
first spike by a factor of order $(3/2)^r$. Disjoint copies of this
gadget do not provide the missing amplification.

One weaker sufficient global target considered was

$$
\sum_{\substack{n\le X\\n\in B}}\frac1n
\le \left(\sum_{q_i\le X}e_i\right)\log X
 +O\!\left(\sum_{q_i\le X}e_i\log q_i\right)+o(\log X). \tag{9.1}
$$

This is **unproved**. Its attraction is that for every fixed infinite
system,

$$
\frac1{\log X}\sum_{q_i\le X}e_i\log q_i\longrightarrow0
$$

by dominated convergence, since $\sum e_i\le1$. If (9.1) were proved,
the finite-prefix lower bound would give logarithmic density (1-\delta)
for (B), hence $\delta$ for (A).

A possible backward charge uses compatible (m<q). Write

$$
r=\frac m{(m,q)},\qquad s=\frac q{(m,q)}>r.
$$

If (r=1), the earlier class contains the later class, so the later class
has no first kills. Otherwise (r\ge2), and

$$
\frac1r\le2\log(s/r)=2\log(q/m).
$$

Indeed (s\ge r+1) and $\log(1+1/r)\ge1/(r+1)\ge1/(2r)$.
This compares the relative size of a quotient restriction to a decrease
in logarithmic modulus. No conserving charge scheme was found. Naively
summing intersections with later classes charges the same earlier class
repeatedly, potentially on logarithmically many scales.

Other unfinished ideas included a second-moment capacity argument, entropy
of the least killing modulus, and prime-coordinate martingale
approximation. None supplied the required global estimate. In particular,
the elementary second-moment choice (h_q=\sum_{n\le X,\,n\in E_q}1/n)
and

$$
V(\omega)=\sum_q qh_q1_{[a_q]_q}(\omega)
$$

has $\mathbb EV=\sum_qh_q$, but its second moment involves

$$
\sum_{q,r}(q,r)\,1_{a_q\equiv a_r\pmod{(q,r)}}h_qh_r.
$$

The hoped-for upper bound by $H_X\sum_qh_q$ is false already for the
zero classes modulo (2,3,5,7) at (X=10). Here

$$
(h_2,h_3,h_5,h_7)
=\left(\frac{137}{120},\frac49,\frac15,\frac17\right),
$$

and exact calculation gives

$$
\mathbb EV^2-H_{10}\sum_qh_q
=\frac{329873}{6350400}>0.
$$

Consequently that direct Cauchy–Schwarz route is not a proof of (H).

## 10. Remaining mathematical uncertainty

There is no established control here of all large-quotient hits from a
distinct-modulus family, nor of their unshadowed part after a finite
prefix. There is also no construction making those hits produce a fixed
logarithmic oscillation while the periodic survivor densities remain
bounded away from zero.

In particular, none of the following has been established:

* the sharp finite inequality (H) or its general Dirichlet counterpart (D);
* Chojecki's global charge condition or the weaker target (9.1);
* a valid singleton replacement for Wang's multi-residue blocks;
* an infinite legal congruence system with unequal upper and lower
  logarithmic densities.

The auxiliary notes with more detailed calculations and failed attempts
(compression, early-hit capacity, and the common-translate narrow-window
proposition; Dirichlet approaches and their multiplicity obstruction; exact
finite examples and searches; quotient and activation formulas; label and
matching attempts) are not retained.

Where such a note used informal language suggesting that bounded-hit
capacity alone forces every possible counterexample to use unbounded
quotients, the qualification in Section 3.2 of this consolidated record is
the intended precise statement. The obstruction is proved for
small-whole-footprint bounded-hit blocks; the general conditioned setting
remains unresolved.

**Final status: incomplete investigation, not a solution of Problem 25.**
