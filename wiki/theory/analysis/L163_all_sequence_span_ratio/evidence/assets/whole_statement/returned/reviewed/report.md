---
desc: |
  Adversarial review of the all-sequence circle-span ratio bound, including
  the multiset transfers, finite-list discrepancy bound, uniform constants,
  and extremal consequence.
---

# Whole-statement review of the all-sequence ratio bound

**Subject.** The ratio clause of the supplied composed theorem for Problem
1221, its complete supplied proof, and the consequence for $\mu_r$ in the
modified catalog formulation. The extraction was frozen on
2026-10-15 at 09:49:19.072889 UTC. The source paths and preserved excerpts are
listed below. Examination date: 2026-10-15 UTC.

**Reviewer and independence.** An independent mathematical reviewer, disclosed
model `gpt-6-astra`, examined the subject in a fresh context, without
participation in its construction or prior reliance on it. The assignment was
to find a counterexample, an essential proof defect, or a canonical failure
mode. The reviewer had neither the author's working context nor another
reviewer's verdict.

**Mathematical verdict: refutation-failed.** This verdict covers the stated
universal ratio inequality and its precise infimum and divergence consequences.
It does not assert a tier, acceptance, or problem status. Independent
derivations and failed attacks are retained in this report; no mathematical
computation is used. The grading decision belongs to a distinct fresh grader.

## Exact subject and reading boundary

All nine excerpts below were read in full. They are exact copies of the supplied
extraction, not extracts made from canonical pages during the examination.
Source ranges are locators supplied with the frozen extraction. The canonical
pages themselves were not opened.

| Preserved excerpt | Source path and supplied range |
| --- | --- |
| [Catalog formulations](subject/catalog_statement.md.txt) | `wiki/problems/analysis/E1221/_index.md`, lines 25–94, Statement through Statement (modified), excluding Notes. |
| [Model and theorem](subject/model_and_theorem.md.txt) | `wiki/research/erdos_1221/all_sequence_composition.md`, lines 31–85, Target through the composed theorem. Only the ratio clause and its consequence are assigned. |
| [Lemma 2.1](subject/lemma_2_1.md.txt) | `wiki/research/erdos_1221/ko26b_lemma_2_1_reconstruction.md`, lines 28–245, Definitions through Uniformity. |
| [All-sequence transfers](subject/all_sequence_transfer.md.txt) | `wiki/research/erdos_1221/all_sequence_composition.md`, lines 141–165; the passage starting “The least-distance step of Lemma 4.2” at line 189, column 24, through line 192; and Positivity, lines 193–196. |
| [Closing ratio comparison](subject/ratio_comparison.md.txt) | `wiki/research/erdos_1221/all_sequence_composition.md`, lines 197–248, The ratio part. |
| [Proposition 3.1](subject/proposition_3_1.md.txt) | `wiki/research/erdos_1221/ko26b_proposition_3_1_reconstruction.md`, lines 33–173, statement and proof. |
| [Proposition 1221.1](subject/proposition_1221_1.md.txt) | `wiki/research/erdos_1221/connections.md`, lines 425–476. The consumed conclusion is the finite-list extraction with $H\le B$. |
| [Proposition FP](subject/finite_list_bound.md.txt) | `wiki/research/erdos_1221/finite_list_prefix_bound.md`, lines 32–180, statement, proof, integer-rounding and repeated-entry remarks. |
| [Provenance and scope](subject/provenance_and_scope.md.txt) | The supplied bibliographic and scope map, read in full. |

The supplied extraction manifest was also read in full. Its scope, source
ranges, and payload identities agreed with the commission. The private pin and
byte checks are retained separately from this mathematical report. The
extraction's marker `[cut: outside this mathematical subject]` is an exclusion
marker, not an invitation to fill a cut from another source. The frozen inputs
were not changed.

The allowed mathematical reading was exactly that manifest and those nine
excerpts; actual mathematical reading stayed within it. Operating reading
included the full README, campaign instructions, and both verification
contracts; the Claims, Evidence, Tiers, and Project claims sections of anatomy;
the research guide's Reading section; and the full evidence, math-authoring,
and weaving guidance. The charter, steps, configuration and accepted-settings
records, command help, supplied scripts, and lifecycle, messaging, and memory
guidance were operating inputs. The template's source and pin fields were checked; its
duplicated commission was partly displayed and was fully read in the charter.
Root AGENTS was supplied as operating context. The operating manifests were
checked before direct reading. The remaining allowed operating pages and wiki
guidance were not substantively read.

The initial subscription table was empty, and the accepted settings specified
blind, sealed, local operation without synchronization or descendants. Those
facts support isolation; they are not a substitute for the reading account.
No inbox, feed, author plans or memory, prior verdict, canonical mathematical
page, ledger, original paper, live agent configuration, or outside search was
read. No excluded exposure or substantive steering was received. No subject
repair, merge, manual commit, repository battery, or Lean execution was
performed. The report concerns the frozen excerpts, not any later revision.

## Restatement with quantifiers and conventions

For every infinite sequence $X=(x_n)_{n\ge1}$ in
$\mathbb T=\mathbb R/\mathbb Z$, repetitions are permitted. Fix a positive
integer $r$. For each integer $n\ge r$, order the first $n$ labels by position
around the circumference-one circle, resolving coincident positions by their
arrival indices. Choose a real
lift $y_1\le\cdots\le y_n$ and extend it by $y_{i+n}=y_i+1$. Define

$$
s_i=y_{i+r}-y_i,\qquad
m_n^{(r)}=\min_{1\le i\le n}s_i,\qquad
M_n^{(r)}=\max_{1\le i\le n}s_i.
$$

These are lifted clockwise spans, not shortest unoriented circle distances.
The nonnegative gaps sum to one. Every gap occurs in exactly $r$ of the $n$
spans, including when $n=r$, so

$$
\sum_{i=1}^n s_i=r,\qquad nm_n^{(r)}\le r\le nM_n^{(r)}.
$$

Thus $M_n^{(r)}>0$. A zero minimum gives ratio $+\infty$, according to the
specified convention. Arc counts count labels with multiplicity, using
$(x,x+\ell]$ with $\ell<1$. Logarithms below are natural, except $\log_4$ and
$\log_2$ when explicitly written.

The assertion is that there exists an absolute $r_0$ such that, for every
integer $r\ge r_0$ and every such $X$,

$$
\limsup_{n\to\infty}\frac{M_n^{(r)}}{m_n^{(r)}}
\ge 1+\frac{\log r}{200r}.
\tag{R}
$$

For each fixed $r$, set

$$
\mu_r=\inf_X\limsup_{n\to\infty}
\frac{M_n^{(r)}}{m_n^{(r)}}.
$$

The assigned consequences, with the same absolute threshold, are

$$
r(\mu_r-1)\ge\frac{\log r}{200}\quad(r\ge r_0),
\qquad r(\mu_r-1)\longrightarrow+\infty.
\tag{E}
$$

The infimum and limits may be understood in the extended reals. No minimizing
sequence attaining the infimum is asserted. The limit in (E) takes $r$ through
the positive integers. The first two clauses of the shared theorem, their
growth expressions, and coefficient $1/100$ are outside this
verdict. The modified formulation is the target; its ratio definition is the
one above. The common model resolves the catalog display's index notation by
taking the maximum and minimum over the $n$ cyclic starting labels.

## Premises, interfaces, and reading depth

The premise census was derived from the frozen statement, proof, and
consequence sentences and checked on 2026-10-15 UTC. No native L-claim or ledger
row is consumed. Consequently there is no native premise standing or pending
grade to import, and no ledger read was made. The propositions in the following
table are deductions checked within this examination, not established premises
taken on trust.

| Internal interface | Exact role and hypotheses | Reading and examination |
| --- | --- | --- |
| Label model and mean identity | $n\ge r$, arbitrary repeated positions, nonnegative cyclic gaps summing to one. Supplies $nm\le r\le nM$ and $M>0$. | Full supplied definitions; identity rederived above. |
| Ratio failure to (2.1) | For a fixed $r$ and $A>0$, a strict limsup bound yields a $C<A$ and eventually positive minima. It must give nonnegative $a_t,b_t$ with sum at most $A$ for every sufficiently large real $t$. | Complete supplied deduction checked in Weakest step 3. The linked but unprovided Theorem 1.1 page is not needed. |
| Lemma 2.1 | Under (2.1), $D,E>0$, integer $k\ge1$, $q=E/(kr)<1$: upper and lower count comparisons at $(1\pm q)t$, with a threshold uniform for bounded $D$. | Full supplied proof verified, including the label extension, in Weakest step 1. |
| Terminal counts | Under (2.1), $r>A$ and late $t$: $U_t(r-A)\le r/(r-A)$ and $V_t(r+A)\ge r/(r+A)$. | Both multiset arguments verified in Weakest step 1. |
| Proposition 3.1 | Absolute $C_0,C_1$; $A\ge1$, $r\ge C_0A$, (2.1) eventually. With $\Lambda=\log(r/A)$ and $S=\sqrt{Ar}/\Lambda^2$, all late $t$ and all $x,0\le D\le S$ have count error at most $B=3A+C_1A/\Lambda$. | Entire supplied scale-chain and descent proof verified; absolute bounds exhibited in Weakest step 1. |
| Proposition 1221.1, extraction | $B\ge1$, $S\ge2$; the preceding bound at every integer $n\ge n_0$. For $L=\lfloor S\rfloor$, yields $L'\in[L-B,L+B]$ and a list in $(0,1)$ with $H_{L'}\le B$, repetitions permitted. | Full extraction proof verified in Weakest step 2. The final conditional paragraph was read but supplies no premise here. |
| Proposition FP | Every integer $L\ge1$ and every list in $[0,1)$, repetitions allowed: $H_L\ge\lfloor\log_4L\rfloor/16$. | Whole supplied proof verified, including the four-block range and potential inequalities, in Weakest step 2. |
| Closing comparison | $A=(\log r)/200$, eventual $L'\ge S/2$, and $3/200<1/(32\log4)$. | All large-parameter estimates and sequence-independent threshold verified in Weakest step 3. |
| Extremal consequence | (R) for every $X$ at each fixed $r\ge r_0$. | The infimum in ratio coordinates, multiplication by $r$, and divergence are checked separately in Weakest step 3. |

The dependency order is acyclic: the model and ratio reduction supply (2.1);
Lemma 2.1 and the terminal counts supply Proposition 3.1; that supplies the
finite list; Proposition FP is proved independently of those transfers; its
lower bound then contradicts the ratio hypothesis; finally the universal bound
passes to $\mu_r$. There is no separate batch acceptance order to presume.

The elementary background used is finite counting, finite sums and integrals,
the measure of an arc and a finite union bound, piecewise affine calculus,
Bernoulli's inequality, and elementary logarithmic and exponential estimates.
All specialized inequalities needed from the cited literature are proved in
the supplied subject and checked below.

The supplied provenance credits S. Korsky, *A resolution of the de
Bruijn–Erdős consecutive-gap problem*, arXiv:2609.07196v2, **unrefereed**,
Sections 2–3 and 6–8, for the span-to-count and closing arguments. Its stated
distinct-point hypothesis is not assumed to cover repeated points; that
extension is checked here. G. Larcher's *On the star discrepancy of sequences
in the unit interval*, arXiv:1407.2094v1, Lemma 2.1 and Section 3, is credited
for range splitting. Original project mathematics and the complete local
write-ups are credited to Plasma AI.

Actual original-paper reading depth for both cited papers is **unread**. The
verdict rests on the complete supplied local deductions, whose mathematical
proofs were verified, and asserts no original-paper or PDF fidelity. The
Halasz/Bilyk planar result mentioned in the provenance map is not consumed by
this ratio proof and was not inspected. Theorem 4.1 is unprovided and is not an
assumption here; no truth or proof-coverage claim about it follows from this
report. Proposition FP supplies the required lower bound directly.

## Weakest step 1: multiset transfer and uniform short-arc control

The first vulnerable link is transferring a proof written for distinct sets to
repeated positions without losing injectivity, endpoints, or uniformity. The
following rederivation also checks the surrounding Proposition 3.1.

### Label maps and averaging

Here hypothesis (2.1) means that $A\ge1$ is fixed and, for every sufficiently
large real $t$, there are $a_t,b_t\ge0$ with $a_t+b_t\le A$ such that every
$r$-span at time $\lfloor t\rfloor$ lies in
$[(r-a_t)/t,(r+b_t)/t]$. Let $N_t$ count those labels with multiplicity and,
for $D>0$, put

$$
U_t(D)=\frac1D\sup_x N_t((x,x+D/t]),\qquad
V_t(D)=\frac1D\inf_x N_t((x,x+D/t]).
$$

Times are taken large enough that these arcs have length less than one.

Regard $P_t$ as the labels $1,\ldots,\lfloor t\rfloor$ with their positions.
The inclusion of an earlier label set into a later one is injective even when
their position maps are not. Moving $kr$ places forward or backward in a cyclic
label order is a permutation; denote the two moves by $F_s$ and $B_s$,
respectively. For late $s$, the clockwise displacement of $F_s$ is a sum of
$k$ successive $r$-spans. The counterclockwise displacement magnitude of $B_s$
is such a sum based at its image. Both lie in

$$
\left[\frac{k(r-a_s)}s,\frac{k(r+b_s)}s\right].
$$

Composing a forward and a backward move uses the difference of these real
displacements. It is not replaced by its representative in $[0,1)$.
Membership in a counting arc is then taken modulo one. This supplies a valid
lift for each image, including when several image labels coincide.

For any fixed finite multiset $Q$, arc $J$ of length less than one, and
$0<\ell<1$, finite-sum integration gives

$$
\int_0^\ell N_Q(J+u)\,du
=\int_J N_Q((v,v+\ell])\,dv.
\tag{1}
$$

For each label this follows by matching the pairs $v=p-u$, using the integer
translates of a representative of $p$ that meet the real intervals. Only
finitely many translates contribute. Each label is counted separately, and
the differences at endpoints have measure zero. Thus (1) remains valid across
the cyclic cut and does not assume distinctness or a random distribution.

Fix $D,E>0$, an integer $k\ge1$, and $q=E/(kr)<1$.
For the upper comparison set $t_+=(1+q)t$, $\ell=E/t_+$, and
$s=t/(1-ut/(kr))$ for $0\le u\le\ell$. Then $t\le s\le t_+$ and
$kr/t-kr/s=u$. The map $B_sF_t$ is an injection from $P_t$ into $P_{t_+}$.
Writing its lifted displacement as $u+\eta$, one has

$$
-\frac{k(a_t+A)}t\le\eta\le\frac{k(b_t+A)}t.
$$

Enlarge $I=(x,x+D/t]$ by those two errors, obtaining $J$ with
$|J|\le(D+3kA)/t$. Every label in $I$ maps into $J+u$. The open left
endpoint remains strict, since a label of $I$ starts strictly to the right of
$x$. Integrating this injection inequality by (1) gives

$$
N_t(I)\le(D+3kA)(1+q)U_{t_+}(E).
\tag{2}
$$

For the lower comparison set $t_-=(1-q)t$, $\ell=E/t_-$, and
$s=t/(1+ut/(kr))$. Now $t_-\le s\le t$ and $kr/s-kr/t=u$.
The map $F_tB_s$ injects $P_{t_-}$ into $P_t$, with displacement
$-u+\eta$, where

$$
-\frac{ka_t}t-\frac{kA}{t_-}
\le\eta\le
\frac{kb_t}t+\frac{kA}{t_-}.
$$

Shrink the left endpoint of $I$ by the magnitude of the left error and its
right endpoint by the right error. Interpret a nonpositive remaining length
as an empty arc. The resulting $J+u$ maps into $I$, and (1) now gives

$$
N_t(I)\ge
\bigl(D(1-q)-kA(3-q)\bigr)_+V_{t_-}(E).
\tag{3}
$$

Dividing (2) and (3) by $D$ proves exactly both inequalities of Lemma 2.1.
No continuity or measurability of the choices $a_s,b_s$ is needed: their
bounds are used pointwise; the integrals are of translated counts of fixed
finite label sets.

For fixed $E,k$, every comparison time is a fixed positive multiple of $t$
or lies between two such multiples. Bounded $D$ makes all relevant arc
lengths bounded by a constant divided by $t$. One late-time threshold therefore
ensures the hypothesis, $kr<|P_s|$, and lengths less than one uniformly in
that range of $D$ and in the arc's starting point. The factors $1/D$ in the
normalized statement do not introduce a small-$D$ threshold.

### Terminal bounds and scale chains

For $r>A$, an arc of length $(r-A)/t$ containing at least $r+1$ labels
would contain a first label and the label $r$ places after it. Their lifted
separation is strictly less than the arc length, contradicting the lower span
bound. Coincident positions do not alter this strict inequality.

For the other terminal bound, lift all labels into $(x-1,x]$ and choose the
last label $p_0\le x$. Its next $r$ labels have positions strictly greater
than $x$. The last of those is at most
$p_0+(r+b_t)/t\le x+(r+A)/t$. Thus the longer arc contains at least $r$
labels. This proves the two terminal inequalities with multiplicity.

Write $\theta=\sqrt{A/r}$, $K=\sqrt{Ar}$, and
$\Lambda=\log(r/A)$. The doubling chains from $K$ to $r-A$ or $r+A$ have
at most $\Lambda/(2\log2)+2\le3\Lambda$ steps once $\Lambda\ge1$.
For adjacent scales $D<E\le2D$, take $k=\lceil D/K\rceil$. Then

$$
q\le2\theta,\qquad 3kA/D\le6\theta,\qquad kA/D\le2\theta.
$$

If $\theta\le1/12$, the upper multiplier in Lemma 2.1 is at most
$1+9\theta$, and the lower multiplier is at least $1-8\theta>0$.
Also $\theta+\theta^2<1$, so $K<r-A$ and both scale chains increase.
Successive comparison times are multiplied by positive factors $1\pm q_i$.
There are finitely many of them for each fixed $r,A$, so they can all be made
late enough. No uniform bound on their threshold across sequences is used.

Here is an explicit check that the implied constants are absolute. Put
$\varepsilon=\theta\Lambda$. Take $C_0$ large enough that

$$
\theta\le1/12,\quad \Lambda\ge1,\quad
\varepsilon\le1/120,\quad \theta\Lambda^2\le1
\qquad(r/A\ge C_0).
$$

For example $C_0=e^{32}$ suffices: $u e^{-u/2}$ and $u^2e^{-u/2}$ decrease
for $u\ge32$, and $e^{16}>2^{16}$. These are safe choices for checking the
supplied estimates, not additional hypotheses on the sequence. The terminal
bounds and chains yield

$$
U_t(K)\le(1+2\theta^2)e^{27\varepsilon}
\le1+60\varepsilon,
\qquad
V_t(K)\ge(1-\theta^2)(1-24\varepsilon)
\ge1-60\varepsilon.
\tag{4}
$$

For the exponential estimate, $27\varepsilon\le1/2$ and
$e^z\le1+2z$ on that interval. The lower estimate uses Bernoulli's
inequality with a nonnegative bound $1-24\varepsilon$.

In the descent to $0<D\le S=K/\Lambda^2$, use the unnormalized (2)–(3)
with $E=K,k=1$. The upper bound is at most
$(D+3A)(1+66\varepsilon)$. Put
$Q=D(1-\theta)-(3-\theta)A$. If $Q>0$, (4) gives
$N_t(I)\ge D-3A-61D\varepsilon$. If $Q\le0$, then
$D\le3A+3A\theta$, and $N_t(I)\ge0$ suffices. Hence, in every case,

$$
|N_t(I)-D|\le3A+200(D+A)\varepsilon.
$$

Since $D\varepsilon\le A/\Lambda$ and
$A\varepsilon\le A/\Lambda$, this is at most
$3A+400A/\Lambda$. Thus absolute constants in Proposition 3.1 really exist;
$C_1=400$ works with the safe $C_0$ above. The proof does not depend on these
particular choices. Its last comparison has fixed times $(1\pm\theta)t$;
the preceding uniform threshold applies to all $D\in(0,S]$. At $D=0$ the
arc is empty and the asserted count error is zero.

## Weakest step 2: finite-list extraction and the four-block lower bound

The second vulnerable link is the lower bound after entries collide. The
extraction is checked first to ensure that the list has the exact domain and
discrepancy convention that the lower bound requires.

For a list of length $L\ge1$, the quantity being bounded is

$$
H_L=\max_{1\le j\le L}\sup_{0\le u\le1}
\left|\#\{i\le j:z_i<u\}-ju\right|,
$$

with $H_0=0$ for the empty list.

### Extraction with constant $B$

Let the integer-time count estimate hold after $n_0$, let
$L=\lfloor S\rfloor$, and choose an integer $N$ sufficiently large that
$w=L/N<1$ and $n_0w<1$. Starting points $a$ for which $(a,a+w]$ contains a
position of one of the first $n_0$ terms form a set of measure at most
$n_0w$. Removing also the finitely many starts for which either endpoint is
one of the first $N$ positions still leaves a choice. This is an existence
argument for every finite initial multiset, not an almost-every-sequence
claim.

For such a choice, $J=(a,a+w]$ has $L'=N_N(J)$ with
$|L'-L|\le B$. List its labels in arrival order
$m_1<\cdots<m_{L'}$ and normalize their lifted positions to
$z_i=(x_{m_i}-a)/w$. Avoidance of both endpoints gives $z_i\in(0,1)$,
and avoidance of the early positions gives $m_i>n_0$.

Fix a nonempty prefix $j$ and $n=m_j$. Write
$C(u)=\#\{i\le j:z_i\le u\}$, and put

$$
f(u)=C(u)-nuw,\qquad
g(u)=j-C(u)-n(1-u)w.
$$

Both arcs involved have scaled lengths at most $nw\le Nw=L\le S$;
the two half-open arcs partition $J$ exactly, even at a repeated coordinate.
Therefore $|f(u)|,|g(u)|\le B$. Crucially,

$$
C(u)-ju=(1-u)f(u)-u g(u),\qquad 0\le u\le1,
$$

so its absolute value is at most $B$, not $2B$. Taking left limits gives the
same bound with $z_i<u$. At $u=0,1$ this is consistent because every entry
lies strictly between the endpoints. Thus $H_{L'}\le B$. An empty list
requires no prefix check; the later application ensures $L'>0$.

### Range splitting and jumps with multiplicity

For an arbitrary list of length $N$ in $[0,1)$, put

$$
D_j(x)=\#\{i\le j:z_i<x\}-jx,\qquad
P_N=\int_0^1\left(\max_{1\le j\le N}D_j(x)
-\min_{1\le j\le N}D_j(x)\right)dx.
$$

The elementary pointwise range bound gives $P_N\le2H_N$. For two nonempty
subsets of indices, writing their maxima as $M_0,M_2$ and minima as $m_0,m_2$,
the range on their union is

$$
\frac{(M_0-m_0)+(M_2-m_2)}2
+\frac{|M_2-M_0|+|m_2-m_0|}2.
$$

The full index set contains that union. This proves the supplied range
inequality exactly; it does not require the maxima and minima to occur at the
same index.

Now let $N=4m$. Use the early indices $1,\ldots,m$ and late indices
$3m+1,\ldots,4m$, with the middle $2m$ indices between them. Let $f$ be the
late maximum minus the early maximum, and $g$ the corresponding difference of
minima. Between entries, their derivatives almost everywhere are minus the
difference of an active late and early index. Consequently

$$
2m+1\le -f',-g'\le4m-1.
\tag{5}
$$

Changes of the active index only introduce continuous corners, of which there
are finitely many. They introduce no omitted jumps.

At a coordinate $v$, let $q_0,q_1,q_2$ be its multiplicities in the early,
middle, and late blocks. Every late $D_j$ jumps by at least $q_0+q_1$;
every early $D_j$ jumps by at most $q_0$. For either a maximum or a minimum,
an increment of each constituent between $a$ and $b$ increments the extremum
by a quantity between $a$ and $b$. Thus

$$
f(v+)-f(v)\ge q_1(v),\qquad
g(v+)-g(v)\ge q_1(v).
\tag{6}
$$

This argument permits arbitrary changes of which index is extremal. It also
allows early and late entries at the same coordinate. All jumps are
nonnegative. At $v=0$ the right jump is included; there is no entry at $1$.
Both functions equal zero at $0$ and $1$ under the strict-count convention.

For $F(s)=s|s|/2$, $F'(s)=|s|$. Integrating on all intervals of continuity
and then including the right jumps, with $h(v)=f(v+)-f(v)$, gives

$$
\int_0^1 |f|(-f')\,dx
=\sum_v\int_{f(v)}^{f(v)+h(v)}|s|\,ds
\ge\frac14\sum_v h(v)^2
\ge\frac14\sum_v q_1(v)=\frac m2.
\tag{7}
$$

The first lower bound follows by minimizing the integral of $|s|$ over an
interval of a fixed nonnegative length: the centered interval has value
$h^2/4$. The second uses (6) and the integer inequality $q_1^2\ge q_1$.
The endpoint terms telescope to zero; when entries are at zero, their jump is
one of the terms on the right. By (5), (7) implies
$\int_0^1|f|\,dx\ge1/8$. The identical reasoning for $g$ gives the other
$1/8$. No separation between entry coordinates is used.

### Recursion and every length

Integrating the range inequality yields

$$
P_{4m}\ge\tfrac12P_m(\text{early list})
+\tfrac12P_m(\text{late list})+\tfrac18.
$$

For a late index $3m+k$, its discrepancy is $D_{3m}+D'_k$, where $D'_k$
belongs to the late list considered from its own beginning. The common
$D_{3m}$ cancels from its maximum-minus-minimum range, justifying that term
of the recurrence. No independence between the two sublists is assumed.

Ordinary induction on $h$ gives $P_{4^h}\ge h/8$ for every list of that
length: $P_1=0$, and both smaller lists in the recurrence have length
$4^{h-1}$. Hence $H_{4^h}\ge h/16$. For every integer $L\ge1$, take its
initial $4^{\lfloor\log_4L\rfloor}$ entries. The maximum defining $H_L$
includes every prefix of this shorter list. Therefore

$$
H_L\ge\frac{\lfloor\log_4L\rfloor}{16}
\ge\frac{\log L}{16\log4}-\frac1{16}.
\tag{8}
$$

This proves the full Proposition FP used in the composition, including all
lengths and all repeated entries. The conditional smoothing paragraph of
Proposition 1221.1 is unnecessary for (8).

## Weakest step 3: ratio reduction, absolute threshold, and infimum

The third vulnerable link is uniformity: a time threshold depending on the
sequence must not become a sequence-dependent lower threshold on $r$.

Fix $r$, put $\alpha=1/200$ and $A=\alpha\log r$, and suppose (R) fails
strictly. The mean identity makes every finite ratio at least one. Choose
$0<C<A$ strictly above $r$ times the excess of the finite limsup over one.
Then, for all sufficiently large integers $n$, the ratio is finite and at most
$1+C/r$. In particular $m_n>0$, and

$$
n(M_n-m_n)
=\left(\frac{M_n}{m_n}-1\right)nm_n\le C,
\qquad nM_n\le r+C.
$$

For $n=\lfloor t\rfloor$, define $a_t=r-nm_n$ and $b_t=tM_n-r$.
Both are nonnegative. Also $(r-a_t)/t=nm_n/t\le m_n$ and
$(r+b_t)/t=M_n$, so every time-$t$ span has the required bounds. Finally,

$$
a_t+b_t=n(M_n-m_n)+(t-n)M_n
\le C+\frac{r+C}{n}<A
$$

for all sufficiently large $t$. This explicitly checks the floor-time error.
The possible closeness of $C$ to $A$ affects that time threshold only.

For all sufficiently large $r$, $A\ge1$ and $r\ge C_0A$. Apply the
verified Proposition 3.1 and restrict to integer times. Its parameters depend
only on $r$ and the absolute constants:

$$
\Lambda=\log(r/A),\qquad
S=\frac{\sqrt{Ar}}{\Lambda^2},\qquad
B=3A+\frac{C_1A}{\Lambda}.
$$

Set $u=\log r$. Then

$$
\Lambda=u-\log u-\log\alpha,\qquad
\frac{A}{\Lambda}\longrightarrow\alpha,
\qquad B=3\alpha u+O(1),
$$

and

$$
\log S=\tfrac12u-\tfrac32\log u+\tfrac12\log\alpha+o(1).
$$

In particular $S/u\to\infty$. Consequently $B\ge1$, $S\ge2$, and
$\lfloor S\rfloor-B\ge S/2>0$ for all sufficiently large $r$.
Proposition 1221.1 can be applied after whatever integer threshold the
sequence requires: its choice of $N$ has no upper restriction. It produces a
nonempty list with $L'\ge S/2$ and $H_{L'}\le B$.

Let $c_0=1/(16\log4)$. Applying (8) to that exact list gives

$$
3\alpha u+O(1)=B
\ge c_0\log(S/2)-\frac1{16}
=\frac{c_0}2u-\frac{3c_0}2\log u+O(1).
$$

The leading coefficients cannot satisfy this for arbitrarily large $u$, since

$$
3\alpha=\frac3{200}<\frac1{64}
<\frac1{32\log4}=\frac{c_0}{2}.
$$

The last strict inequality uses $\log4<2$. All error constants depend only
on $\alpha,C_0,C_1$. Thus one absolute $r_0$ excludes every strictly failing
sequence for every integer $r\ge r_0$. No time threshold uniform over those
sequences was required. Infinite limsup ratios satisfy (R) directly; finitely
many zero minima do not affect a finite limsup argument.

Now fix such an $r$. Every number over which the infimum defining $\mu_r$ is
taken is at least $1+\log r/(200r)$. The class of sequences is nonempty, and
the extended-real infimum therefore has the same lower bound. Subtracting one
and multiplying by positive $r$ proves (E). For every real $K$, eventually
$\log r/200>K$, so $r(\mu_r-1)>K$. This is the asserted divergence.
There is no exchange of infimum with limsup, no appeal to an attained optimum,
and no substitution of separate extremal values of $M_n$ and $m_n$.

## Strongest attempted refutation and other retained attacks

The strongest attempted refutation targeted (6)–(7): merge the middle entries
at one coordinate, put that coordinate at zero, and allow the maximizing or
minimizing indices to change at the jump. Such a configuration could defeat an
argument that counted distinct jump locations, assumed a fixed extremizing
index, or omitted the initial right jump.

It does not defeat the supplied proof. The general extremum-increment bound in
(6) holds through every active-index change. Coalescing $q$ middle entries
creates at least a jump of size $q$, whose contribution in (7) is at least
$q^2/4\ge q/4$. Thus collisions preserve the required total contribution
even when all middle entries coincide.

An exact endpoint diagnostic is the list $z_1=\cdots=z_{4m}=0$. For
$0<x\le1$, $D_j(x)=j(1-x)$, so

$$
f(x)=g(x)=3m(1-x),\qquad f(0)=g(0)=0.
$$

The right jump at zero has size $3m$, and

$$
\int_0^1|f|(-f')\,dx=\frac{9m^2}{2}
=F(3m)-F(0),\qquad \int_0^1|f|\,dx=\frac{3m}{2}.
$$

Omitting the zero-coordinate jump would incorrectly make the right side of
the potential identity vanish on this input. The frozen proof explicitly
includes it. This witness checks the suspected endpoint failure exactly; the
general argument above handles all locations and multiplicities, not just the
witness.

Other attacks and their disposition are retained here:

| Attempted failure | Finding |
| --- | --- |
| Replace an injection of points by a noninjective map after collisions. | At time four with $r=2$ and positions $(0,0,1/2,1/2)$, every span is $1/2$, so collisions cannot simply be dismissed as infinite ratios. Label permutations and label-set inclusion remain injective, and the arc counts retain all labels. Weakest step 1 proves the necessary transport. |
| Use a repeated finite-support sequence as a counterexample to (R). | Eventually some location has at least $r+1$ labels; thereafter a zero $r$-span persists. The maximum remains positive by the mean identity, so the ratio is eventually infinite. Infinite-support repetitions remain covered by the label argument. |
| Lose a full turn or an endpoint when an arc crosses the cyclic cut. | Displacements were kept as real lifts, and (1) was checked label by label using integer translates. The first endpoint is open in every injection or complement argument. No reduction to a shortest circle distance occurs. |
| Require $2B$ rather than $B$ in the finite-list extraction. | The two available errors are for complementary arcs. Their coefficients are $1-u$ and $-u$, whose absolute values sum to one. The exact formula in Weakest step 2 blocks this loss. |
| Produce a normalized entry at $1$, where the FP endpoint identity would fail. | The extraction excludes starts whose right endpoint is any of the first $N$ positions. The extracted list lies in $(0,1)$, strictly inside FP's domain. FP itself correctly includes possible entries at zero. |
| Fail near $D=0$, at empty lists, or at non-power-of-four lengths. | Lemma 2.1 is used in unnormalized form before sending $D$ small. The zero-length arc is empty. The extraction states $H_0=0$, and the application ensures $L'>0$. FP uses an integer power-of-four prefix and loses only the stated $1/16$. |
| Let $C$ approach $A$ and postpone the count threshold indefinitely across different sequences. | Each individual threshold stays finite; the extraction can choose an arbitrarily large $N$. All contradictory numerical parameters depend on $r$ and absolute constants only. No interchange of the sequence and time quantifiers is used. |
| Derive the extremal conclusion by combining separately optimized numerator and denominator bounds. | The proof instead starts with a bound on each actual ratio, controls $n(M_n-m_n)$ jointly, and takes the infimum only after proving the universal ratio statement. |

No attempted refutation produced a counterexample or an unsupported essential
deduction. The displayed derivations explain why the attacks failed rather than
appealing to the author's confidence, earlier review, or agreement of outputs.

## Checklist verdicts

### Canonical failure modes

| Failure mode in the verification contract | Verdict for this subject |
| --- | --- |
| “Almost all” upgraded to “all” | Not found. The finite measure exclusion selects one arc for each fixed sequence; it discards no sequences. Every transfer is labelwise. |
| Induction presupposes termination | Not found. FP uses ordinary induction on $h$, with smaller lists of length $4^{h-1}$ and base $P_1=0$. No algorithmic termination is assumed. |
| Probabilistic or averaging heuristics presented as proofs | Not found. Averaging is the exact finite-sum identity (1). Arc avoidance uses a strict measure upper bound, not a heuristic probability. |
| Circular use of an equivalent statement | Not found. FP is established from elementary discrepancy functions; neither the ratio theorem nor an equivalent sequence lower bound is assumed. |
| Exceptional sets dropped from density arguments | No density argument is used. The finite exclusions in choosing an arc are fully accounted for by positive remaining measure. |
| Finite verification cited beyond base-case coverage | Not found. There is no numerical verification. Finite-list lower bounds are proved for all lengths by induction and prefix restriction. |
| Convergence of a relaxed or averaged system substituted for the objects | Not found. The maps act on the actual labels of the nested sequence. The finite-list conversion is an exact extraction, with its discrepancy error proved. |

### Named patterns

| Named pattern in the verification contract | Verdict for this subject |
| --- | --- |
| Model-class transport instead of entailment | No axiom-system classification is asserted. The relevant model transfer, from distinct positions to label multisets, is justified by actual injections and counts in Weakest step 1. Similar notation is not used as the justification. |
| Uniformity over an infinite family asserted from finitely many instances | Not found. Absolute constants are derived in (4) and the descent. The final $r_0$ is independent of the sequence, while time thresholds may depend on it. |
| Extremal claims audited in the claim's own units | Satisfied. The argument controls the ratio itself, then bounds its infimum. There is no claimed exact extremum, optimal coefficient, or attained value to infer from other units. |
| Consequence sentences are claim surfaces | Satisfied. Both $r(\mu_r-1)\ge\log r/200$ and divergence are checked separately after (R). The shared theorem's other consequences are explicitly excluded. |
| Carry hypotheses actually used by a quantified argument | Satisfied. The proof keeps $A\ge1$, $r\ge C_0A$, positive time factors, short arcs, multiplicity, $B\ge1$, $S\ge2$, and $L'>0$ at their use sites. No bounded family of time thresholds is required. |
| A composition inherits its unproved premises | No missing consumed premise found. Lemma 2.1, Proposition 3.1, extraction, and FP are checked here. The unprovided Theorem 4.1 and planar bound are not substituted into the proof. |
| Reproducibility notes are claims | Satisfied at the mathematical level: the full subject and independent derivations are retained. No executable success count or rerun claim is made. The reconstruction instructions below use no unavailable input. |
| Verifier quotations are claims | Inapplicable. No prior verifier ruling or acceptance prose is supplied or relied on. Grading this report is a separate obligation. |
| Verdict words spelled in full | Satisfied. The mathematical verdict is written as refutation-failed, without an ambiguous abbreviation. |
| Certified-bracket functions fail loudly | Inapplicable. No numerical enclosure, iteration-capped routine, or sampled period is used. |
| A harness leg with no failing input is decoration | Inapplicable to executable evidence: none is used. The exact all-zero-list diagnostic exposes an omitted endpoint jump, and is not offered as universal computational coverage. |
| A gate that reads caches instead of rerunning is defective | Inapplicable. No gate, cached success output, or author computation supports the verdict. Identity checks only establish which text was read. |

### Erdős-specific checklist

| Checklist item | Explicit verdict |
| --- | --- |
| Quantifiers and scope | Satisfied. Every infinite sequence, repeated terms, every integer $r\ge r_0$, the limsup, and all eventual thresholds are preserved. Small $r$ is not claimed. Zero minima and $n\ge r$ are handled explicitly. |
| Circularity | No circularity found. The listed dependency order is acyclic, and the finite-list lower bound does not assume the target ratio claim. |
| Model and convention changes | All consumed changes checked: labels, real lifts, multiplicity, half-open arcs, real to integer times, arrival-order extraction, and strict versus weak prefix counts. |
| Finite and statistical overreach | None found. No statistical inference or independence of sampled cases is used. The finite arguments have universal symbolic proofs. |
| Uniformity | Satisfied. The count-estimate constants are absolute; its time threshold is uniform in $x,D$ at fixed $r,A$. The final asymptotics are sequence-independent. No infinite sum or extremum/limit interchange is used. |
| Extremal conclusions | Satisfied in ratio coordinates. The infimum is over a nonempty class of extended-real values all having the required lower bound. Neither finiteness nor attainment of the infimum is needed for the claimed lower bound and divergence. |
| Consequences and composition | All assigned consequences checked. Exact interfaces are supplied in the premise table. The finite list is nonempty when FP is used. |
| Computation | Inapplicable as an evidence mode. All arithmetic and inequalities are exposed symbolically; no numerical search, rounding assumption, program, or failure exit is a proof premise. |
| Reproduction | The exact nine mathematical inputs and this report suffice to reconstruct the assessment. No executable mathematical rerun is needed or claimed. The copies preserve the supplied extraction rather than a changing canonical page. |
| Source and verdict fidelity | Satisfied within the stated boundary: source credits and the unrefereed qualification are retained; original papers were not read, so their fidelity is not certified. No prior verdict is quoted or strengthened. |

The neighboring correlated-sample discipline is inapplicable because there is
no statistical inference. Evidence coverage follows the noncomputational
contract: the independent arguments, exact subjects, and useful failed attack
are retained. No artificial checker is offered in their place.
The structurally disjoint reproduction requirement for a computational batch
is inapplicable because no computation is used. No second-cycle comparison is
asserted, and no prior-cycle attack material was supplied or read.

## Reconstruction, verdict, and limitations

A reader can reconstruct this assessment using this report and the nine linked
files in `subject/`. Read the model and catalog formulations first, then Lemma
2.1 with its all-sequence transfer, Proposition 3.1, the extraction, FP, and the
closing comparison. The provenance map fixes the attribution and the excluded
conditional premise. The three independent derivations above expose every
consumed mathematical step and the exact endpoint diagnostic. They require no
private paths, original checkout, Git history, original-paper acquisition,
external program, or cached output. There is no mathematical code or executable
rerun command because this is a purely mathematical examination.

| Assigned conclusion | Mathematical verdict |
| --- | --- |
| Universal all-sequence ratio bound (R), including every supplied essential deduction | **refutation-failed** |
| Exact lower bound for $r(\mu_r-1)$ and its divergence (E) | **refutation-failed** |

No mathematical obligation within this assigned ratio proof remains unfinished.
The verdict is confined to the frozen extraction and coefficient $1/200$. It
does not verify the original papers, establish refereeing or community
acceptance, validate the unprovided Theorem 4.1, cover the one-sided clauses,
settle equality between all-sequence and distinct-sequence extremal constants,
or claim the coefficient is optimal. No Lean or computational certificate is
asserted. A distinct fresh grader must assess this report's contract and
independence; this report neither grades itself nor changes any tier or problem
status.
