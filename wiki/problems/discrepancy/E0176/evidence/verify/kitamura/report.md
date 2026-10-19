---
name: problems/discrepancy/E0176/evidence/verify/kitamura/report
title: "Arithmetic-progression discrepancy: whole-proof examination"
desc: Independent adversarial examination of two arithmetic-progression discrepancy bounds, their finite bases and exponential consequences.
created: 2026-10-15T23:59:17Z
updated: 2026-10-16T00:10:49Z
---

# Arithmetic-progression discrepancy: whole-proof examination

## Subject and independence

**Examination date:** 2026-10-15 UTC. **Role:** independent whole-proof
reviewer, in a fresh isolated context, with disclosed model profile
gpt-6-astra. The reviewer neither authored nor collaborated on the subject,
had not previously built on it, and received no prior verdict or author
advocacy. This is a mathematical examination of static source text and
finite computations. It makes no Lean elaboration, kernel, tier, acceptance
or problem-status claim.

**Frozen subject:** the extraction frozen on 2026-10-15 at 13:17:10 UTC,
preserved byte-for-byte under [subject/manifest.json](../../assets/kitamura/reviewed/subject/manifest.json).
All paths below are relative to this report's repository directory.
The preserved subject consists of the
[exact statement](../../assets/kitamura/reviewed/subject/statement.md.txt),
[candidate proof](../../assets/kitamura/reviewed/subject/proof.md.txt),
[exponential deductions](../../assets/kitamura/reviewed/subject/exponential_consequences.md.txt),
[Basic source slice](../../assets/kitamura/reviewed/subject/source/nk2_basic.lean.txt),
[Sqrt source slice](../../assets/kitamura/reviewed/subject/source/nksqrtk_sqrt.lean.txt),
[small-case definitions](../../assets/kitamura/reviewed/subject/source/SmallKCommon.lean.txt),
[source one-term argument](../../assets/kitamura/reviewed/subject/source/K1.lean.txt),
[case 2](../../assets/kitamura/reviewed/subject/source/K2.lean.txt),
[case 3](../../assets/kitamura/reviewed/subject/source/K3.lean.txt),
[case 4](../../assets/kitamura/reviewed/subject/source/K4.lean.txt),
[finite checker](../../assets/kitamura/reviewed/subject/finite/small_cases.py.txt),
[its finite fixture](../../assets/kitamura/reviewed/subject/finite/small_cases_results.json),
the 17 individually listed runtime files in the manifest, and
[source provenance and scope](../../assets/kitamura/reviewed/subject/provenance_and_scope.md.txt).
The snapshot is the supplied extraction, including its uniform cut markers;
it is not a reconstruction from canonical pages. Its mathematical bytes
remained unchanged throughout this examination.

**Reading depth:** every statement, deduction, supplied analytic source
slice, small-case source file, checker and complete finite fixture above was
read in full. The two analytic slices contain 1702 and 964 lines,
respectively. Their essential mathematical deductions are examined below.
All 17 supplied runtime files were read in full, including their import and
initialization surfaces. Their uncalled repository utilities are not
mathematical premises and were not verified as repository tools. Only the
unchanged finite-checker route used this package.

The operating instructions were separately frozen and checked against their
manifest before use. The required portions of anatomy, the complete neutral
and campaign verification contracts, README, campaign guidance, the permitted
research-reading section, evidence, mathematical authoring and weaving were
read. These instructions did not expand the mathematical read set. No
canonical mathematical page, live ledger, full source archive, source README,
author inspection account, previous examination, external paper or website
was read. No inbox, feed, sibling context or substantive steering was
consumed. The subscription tables checked at the examination boundaries were
empty; the accepted settings recorded blind, sealed, no-sync operation.
These are supporting isolation facts, not a claim that those settings impose
a filesystem sandbox. No excluded exposure occurred.

**Independent evidence:** the mathematical derivations in this report and
the [independent finite program](../../assets/kitamura/reviewed/finite/independent.py), its
[exact inputs](../../assets/kitamura/reviewed/finite/claims.json),
[counts and certificates](../../assets/kitamura/reviewed/finite/results.json),
[false-minimum controls](../../assets/kitamura/reviewed/finite/negative_claims.json), and
[control witnesses](../../assets/kitamura/reviewed/finite/negative_results.json).
The [rerun driver](../../assets/kitamura/reviewed/rerun.py) freshly executes the unchanged author checker,
the independent program and the negative controls. Concrete commands appear
under “Reproduction.” This is one examination with a disjoint computational
route, not a claim to two independent review cycles.

**Credits and source limits:** Kenta Kitamura / KitaKen1 owns the original
source mechanism. The supplied provenance preserves preparation-assistance
credits to Codex 5.5 and ChatGPT 5.5 Pro. The analytic extraction, finite Python
probe and exponential deductions are original Plasma AI work. The independent
derivations and reproduction retained in this report are also Plasma AI work.
The source
locators are KitaKen1/erdos176-nk2-polynomial-bound-lean at external revision
88be9174c1b85548fa48d2498ba907a9e80f04c7 and
KitaKen1/erdos176-nksqrtk-polynomial-bound-lean at external revision
19b2ad31c81207613f7cfdaa68467d3dca98b3b7. The supplied provenance records
Apache 2.0 for both archives. Archive identity and license texts were not
separately inspected. The proof examined is the supplied common Basic
mathematics together with the supplied Sqrt extension; the claimed equality
with the second archive's unlisted Basic file was not independently compared.
No conclusion below relies on that unperformed comparison or on a reported
source build.

## Restatement with all quantifiers

For integers $k\geq1$, real $\ell>0$ and integers $N\geq1$, let $P(k,\ell,N)$
mean the following:

For **every** map $f:\{0,\ldots,N-1\}\to\{-1,1\}$, there **exist** integers
$a\geq0$ and $d\geq1$ such that
$a+(k-1)d<N$ and
$$
\left|\sum_{j=0}^{k-1}f(a+jd)\right|\geq\ell.
$$

The terms form an ordinary progression with positive difference.
The final discrepancy comparison includes equality.
If the set of positive integers satisfying $P(k,\ell,N)$ is nonempty,
$N(k,\ell)$ denotes its least element. It is undefined otherwise.

The separately examined conclusions are:

| Conclusion | Exact assertion |
| --- | --- |
| Polynomial bound for 2 | For every integer $k\geq5$, the minimum exists and $N(k,2)\leq \lfloor T_2(k)\rfloor+1$, where $T_2(k)=2(k^2-1)(k-1)(2k+1)/(k-3)$. |
| Polynomial bound for $\sqrt{k}$ | For every integer $k\geq2$, the minimum exists and $N(k,\sqrt{k})\leq\lfloor T_s(k)\rfloor+1$, where $T_s(k)=\frac43(k^2-k+1)(k-1)(k(k-1)+1)$. |
| Finite minimum at 2 | $P(2,2,3)$ holds, while $P(2,2,M)$ fails for every positive integer $M<3$; hence $N(2,2)=3$. |
| Finite minimum at 3 | $P(3,2,9)$ holds, while $P(3,2,M)$ fails for every positive integer $M<9$; hence $N(3,2)=9$. |
| Finite minimum at 4 | $P(4,2,13)$ holds, while $P(4,2,M)$ fails for every positive integer $M<13$; hence $N(4,2)=13$. |
| One-term target 2 | For every positive integer $N$, $P(1,2,N)$ fails; $N(1,2)$ does not exist. |
| One-term target 1 | $P(1,1,1)$ holds and the least positive length is $N(1,1)=1$. |
| Exponential bound for 2 | For every integer $k\geq2$, $N(k,2)$ exists and is at most $16^k$. The one-term target 2 is expressly excluded. |
| Exponential bound for $\sqrt{k}$ | For every integer $k\geq1$, $N(k,\sqrt{k})$ exists and is at most $64^k$, including the actual one-term minimum. |

All divisions defining $T_2,T_s$ are real divisions before applying the
ordinary integer floor. No natural-number division is substituted. Translating
every index by one gives exactly the same minima for $\{1,\ldots,N\}$.
Cyclic progressions used below do not themselves establish any final assertion.

## Common derivations: finite Fourier and Fejér identities

Fix a positive integer $N$ and a sign coloring $f$, extended periodically to
the integers. Write
$$
S_d(a)=\sum_{j=0}^{k-1}f((a+jd)\bmod N),\qquad
M_d=\frac1N\sum_{a=0}^{N-1}S_d(a)^2.
$$

### Finite Fourier normalization

Take $\omega=\exp(2\pi i/N)$. For $t,u\in\{0,\ldots,N-1\}$, put
$q=\omega^{t-u}$. If $t=u$, the sum of $q^a$ is $N$.
Otherwise $N$ cannot divide the nonzero integer $t-u$ in this range, so
$q\neq1$, while $q^N=1$. Multiplying the finite geometric sum by
$1-q$ gives $1-q^N=0$. Thus
$$
\frac1N\sum_{a=0}^{N-1}\omega^{(t-u)a}=\mathbf1_{\{t=u\}}.
\tag{1}
$$
For $N=1$ only the first case occurs.

Define
$$
\widehat f(t)=\frac1N\sum_{a=0}^{N-1}f(a)\omega^{-ta}.
$$
Interchanging two finite sums and applying the same geometric identity with
the roles of index and frequency exchanged gives
$f(x)=\sum_t\widehat f(t)\omega^{tx}$.
For arbitrary complex coefficients $c_t$, direct multiplication gives
$$
\frac1N\sum_a\left|\sum_t c_t\omega^{ta}\right|^2
 =\sum_{t,u}c_t\overline{c_u}
   \frac1N\sum_a\omega^{(t-u)a}
 =\sum_t|c_t|^2.
\tag{2}
$$
In particular $\sum_t|\widehat f(t)|^2=1$.

With $G_d(z)=\sum_{j=0}^{k-1}z^{jd}$, the periodic expansion of $f$ yields
$$
S_d(a)=\sum_t\widehat f(t)\omega^{ta}G_d(\omega^t),\qquad
M_d=\sum_t|\widehat f(t)|^2|G_d(\omega^t)|^2.
\tag{3}
$$
This independently supplies the normalization and finite basis/Parseval
content used in the source. It holds for every positive $N$ and every natural
$d$, with no primality, coprimality or distinct-residue assumption.

### Fejér expansion and the factor two

For a unit complex number $z$, integers $k,D\geq0$, and $1\leq d\leq D$,
let $w_d=1-d/(D+1)$. Consider
$$
Q=\frac1{D+1}\sum_{p,q=0}^{k-1}
 \left|\sum_{r=0}^{D}(z^p\overline{z^q})^r\right|^2.
$$
Every summand is nonnegative. When $p=q$, its value after division by $D+1$
is $D+1$, since $z^p\overline{z^p}=1$. Therefore
$Q\geq k(D+1)$, even when different powers $z^p$ coincide.

Expand the square and interchange the four finite sums. For fixed $r,s$,
the sum over $p,q$ is
$$
\left|\sum_{p=0}^{k-1}z^{p(r-s)}\right|^2.
$$
Negative exponents are well-defined because $z\neq0$. Their sums are the
conjugates of the positive-exponent sums, and have the same squared modulus.
There are $D+1$ pairs with $r=s$. For a positive difference $d$, the pairs
$(r,s)=(s+d,s)$ number exactly $D+1-d$, and there are equally many pairs of
difference $-d$. It follows that
$$
Q=k^2+2\sum_{d=1}^{D}w_d|G_d(z)|^2.
\tag{4}
$$
Consequently
$$
\sum_{d=1}^{D}w_d|G_d(z)|^2
 \geq \frac{k(D+1)-k^2}{2}.
\tag{5}
$$
Since $0\leq w_d\leq1$, the same lower bound holds for
$\sum_{d=1}^{D}|G_d(z)|^2$.

This includes the empty $D=0$ case: the identity gives $Q=k^2$, while
the lower bound becomes $0\geq(k-k^2)/2$ for natural $k$.
No limiting argument is involved.

As an exact normalization attack, take $k=2,D=4,z=-1$.
Then $G_1=G_3=0$ and $G_2=G_4=2$, so the weighted energy is $16/5$.
Directly, the two diagonal pair terms total $10$, and each off-diagonal term
is $1/5$, giving $Q=52/5=4+2(16/5)$. This tests the normalization, diagonal
contribution and factor two away from the all-ones case. The general proof
above, rather than this example, establishes (4)–(5).

Multiplying (5) by the nonnegative masses $|\widehat f(t)|^2$ and summing
over $t$ gives
$$
\sum_{d=1}^{D}w_dM_d\geq\frac{k(D+1)-k^2}{2},\qquad
\sum_{d=1}^{D}M_d\geq\frac{k(D+1)-k^2}{2}.
\tag{6}
$$
The masses sum to exactly one, not $N$ or $1/N$.

The source's conditional helpers with a scalar Cassels hypothesis are
discharged by its own scalar proof. In the supplied Basic slice,
the nonnegative pair terms, expansion and bounds lead to
casselsGeomLowerClaim_true, then to the unconditional moment bound.
The Sqrt slice retains the exact weighted identity. No Cassels or Turán
literature result is imported into this examination.

## Common derivations: ordinary progressions, wrapping and minima

### Wrap loss and target conventions

Let $m=(k-1)d$. Among $a=0,\ldots,N-1$, exactly $\min(N,m)$ satisfy
$a+m\geq N$: if $m<N$, they are $N-m,\ldots,N-1$; if $m\geq N$, all starts
qualify. In particular their number is at most $m$. Equality at the endpoint
$a+m=N$ belongs to the wrapping set.

For every cyclic start, the triangle inequality gives $|S_d(a)|\leq k$,
even if residues repeat. If every non-wrapping start has $S_d(a)^2\leq b$,
then, for $k^2-b\geq0$,
$$
M_d\leq b+(k^2-b)\frac{\min(N,(k-1)d)}N
 \leq b+(k^2-b)\frac{(k-1)d}{N}.
\tag{7}
$$
The second estimate remains valid when its right side exceeds $k^2$.
No implicit assumption $(k-1)d<N$ was used to count wrapping starts.

For discrepancy 2, failure of the non-strict target means integer
$|S_d(a)|<2$, hence $S_d(a)^2\leq1$.
For the other target, both $\sqrt{k}$ and $|S_d(a)|$ are nonnegative, and
squaring preserves their order. Thus
$$
\sqrt{k}\leq|S_d(a)|\quad\Longleftrightarrow\quad k\leq S_d(a)^2.
\tag{8}
$$
Failure gives the integer inequality $S_d(a)^2\leq k-1$.
The caps in (7) are therefore $b=1$ and $b=k-1$, respectively.
Equality in (8) remains admissible, including square $k$.
For example a four-term sum $1+1+1-1=2$ reaches $\sqrt4$; replacing the
final comparison by a strict one would change the subject.

If $a+(k-1)d<N$ and $j<k$, then
$a+jd\leq a+(k-1)d<N$. Every cyclic index equals its ordinary index.
For $d\geq1$ the indices are distinct. The canonical representatives of
$\mathbb Z/N\mathbb Z$ are in bijection with $\{0,\ldots,N-1\}$, so transport
through Fin and ZMod changes neither the sum nor its normalization.
An integer embedded in $\mathbb C$ has squared norm equal to its integer
square embedded in $\mathbb R$. These observations supply every model bridge
used in (3), (6) and (7).

### Polynomial bound for discrepancy 2

Assume $k\geq5$ and that every ordinary $k$-term AP misses target 2.
Put $D=2k$. Summing (7) with $b=1$ and dividing by $D$ gives
$$
\frac1D\sum_{d=1}^D M_d
 \leq 1+\frac{(k^2-1)(k-1)(D+1)}{2N}
 =:U_2.
$$
The unweighted half of (6) gives
$$
\frac1D\sum_{d=1}^D M_d\geq\frac{k+1}{4}=:L_2.
$$
Writing $A_2=(k^2-1)(k-1)(2k+1)$, subtraction gives the exact gap
$$
L_2-U_2
 =\frac{N(k-3)-2A_2}{4N}
 =\frac{k-3}{4}\left(1-\frac{T_2(k)}N\right).
\tag{9}
$$
Both $N$ and $k-3$ are positive. Therefore $N>T_2(k)$ makes the gap
strictly positive, a contradiction. The conclusion is an ordinary AP with
$1\leq d\leq2k$ and non-strict discrepancy at least 2.

A floor boundary attack is decisive about the needed strictness:
$T_2(5)=1056$. At $N=1056$, (9) is zero and this contradiction is unavailable.
The stated choice is $N=1057$, where the gap is exactly $1/2114>0$.
Thus the added one is doing necessary work in the argument; it was not lost
when passing between real and integer bounds.

### Polynomial bound for discrepancy $\sqrt{k}$

Assume $k\geq2$ and every ordinary AP fails (8).
The exact finite sums, obtained from $\sum d=D(D+1)/2$ and
$\sum d^2=D(D+1)(2D+1)/6$, are
$$
\sum_{d=1}^D w_d=\frac D2,\qquad
\sum_{d=1}^D d\,w_d=\frac{D(D+2)}6.
\tag{10}
$$
Nonnegativity of every weight permits summing (7). Set
$A=(k^2-k+1)(k-1)$ and $K=k(k-1)>0$, and take $D=2K$.
The weighted bounds become
$$
U_s=(k-1)\frac D2+\frac{A D(D+2)}{6N},\qquad
L_s=\frac{k(D+1)-k^2}{2}.
$$
Before inserting the error term, the difference is
$L_s-(k-1)D/2=(D-K)/2=K/2$. Hence
$$
L_s-U_s
 =\frac K2-\frac{2AK(K+1)}{3N}
 =\frac K2\left(1-\frac{T_s(k)}N\right).
\tag{11}
$$
For $N>T_s(k)$ this is strictly positive, again a contradiction.
It produces a positive difference at most $2k(k-1)$ and a non-wrapping
ordinary AP satisfying (8).

At the smallest allowed $k=2$, the threshold is the integer $12$.
At $N=12$ the gap is zero, while at the stated integer choice $13$ it is
$1/13$. The proof uses the exact weighted estimate and the integer cap
$k-1$; replacing either by a heuristic average would not prove (11).

### Existence, floors and least values

On their stated domains, both thresholds are positive real numbers.
For either threshold $T$, let $B=\lfloor T\rfloor+1$.
Then $B\geq1$ and $T<B$, including integral $T$.
The preceding contradiction proves the universal property at $B$ before
selecting a minimum. The nonempty set of positive successful lengths
therefore has a least element, and that element is at most $B$.

The source properties explicitly require positive length. Consequently their
Nat.find selections over natural numbers are these same positive minima.
On the positive threshold domains, Nat.floor agrees with the ordinary floor.
No default value supplies existence. N176 is guarded by $k\geq5$, and
N176Sqrt by $k\geq2$; their default zero values outside those guards are
different definitions from the mathematical minima.

For completeness, if the property holds at $M$ and $N\geq M$, restricting a
coloring of length $N$ to its first $M$ entries supplies an AP still contained
in the larger interval. Translation by one is also bijective: set
$g(x)=f(x-1)$, send $(a,d)$ to $(a+1,d)$, and reverse by subtraction.
Both successful-length sets, and hence their minima, are unchanged.

## Finite bases: exact independent reproduction

### Boolean codes and sign colorings

For any $N\geq0$, encode a sign coloring by
$$
c=\sum_{\{x:f(x)=1\}}2^x.
$$
Then $0\leq c<2^N$ since $\sum_{x=0}^{N-1}2^x=2^N-1$.
For a fixed $x$, split the sum as
$c=c_{<x}+\epsilon_x2^x+2^{x+1}t$, where $0\leq c_{<x}<2^x$ and
$\epsilon_x$ is one or zero according as $f(x)=1$ or $-1$.
Then $(c\mathbin{\mathrm{div}}2^x)\bmod2=\epsilon_x$.
Conversely repeated Euclidean division by two gives each $0\leq c<2^N$
exactly $N$ binary digits, padded with zeros; their reconstruction gives $c$.
Thus these codes and sign colorings are bijective. This includes the empty
coloring and the sole code zero at $N=0$.

For $k\geq2$, an admissible positive difference satisfies
$d\leq(k-1)d\leq a+(k-1)d<N$. Also $a<N$.
Thus the source loops over $a,d<N$, with the positive-difference guard,
exhaust all ordinary APs. Its endpoint guard implies every $j<k$ is in range,
so the fold skips no term on an accepted candidate.
The Boolean predicate goodCode is exactly the universal coloring property
on these finite domains. allBeforeFalse rejects every smaller length.
At $N=0$, one empty coloring exists but there is no start, so the property
fails. The mathematical bridge is proved here; no claim is made that the
source has formalized this bridge.

The author checker enumerates sign tuples and equal-gap subsets, then
compares with its start/difference inventory. Its integer arithmetic,
positive endpoint conditions, empty cases, target comparison and failure exit
were inspected. The unchanged script was freshly run through the supplied
runtime, producing 12 passing checks and exactly the retained 28 data rows.
Actual script-file import tracing identified all 17 runtime files at the
supplied paths. Neither a stored success message nor native_decide was used
as a premise.

### Independent inclusion-exclusion for $k=2,3$

For $k=2$, a sum reaches absolute value 2 exactly when the two signs agree.
For $k=3$, its absolute value is 1 or 3, so reaching 2 is equivalent to all
three signs agreeing. Avoidance is therefore absence of monochromatic AP
edges in both cases.

Generate an AP by its endpoints $x<y$: it exists precisely when $k-1$
divides $y-x$, with points $x+j(y-x)/(k-1)$.
This is separate from both author generators.
For any selected subset $J$ of AP edges, requiring every edge of $J$ to be
monochromatic identifies its vertices into $c(J)$ equivalence classes.
There are exactly $2^{c(J)}$ sign assignments satisfying those equalities.
Inclusion-exclusion gives the number of avoiding colorings:
$$
A_{k,N}=\sum_{J\subseteq E}(-1)^{|J|}2^{c(J)}.
\tag{12}
$$

The independent implementation starts with the discrete partition and
coefficient one. For each edge it keeps each current term, and subtracts
the same coefficient on the partition obtained by merging that edge's
classes. Induction on the number of processed edges proves that the resulting
coefficient of each partition is exactly the sum of the inclusion-exclusion
signs producing it. Equal partitions can therefore be combined without
enumerating sign tuples. This is a terminating expansion over a finite edge
list, not an assumption that all colorings have been visited.

For prescribed prefix signs, a partition contributes zero if a class receives
both signs. Otherwise each unfixed class has two choices. Using these
conditional counts, the program selects sign $-1$ whenever that branch has
a completion, and sign $+1$ otherwise. The two branch counts sum to the parent
count. This constructs the lexicographically first avoiding coloring and
records its exact branch counts. No author witness is supplied to this
construction.

At $(k,N)=(2,3)$ the resulting coefficient polynomial is
$q^3-3q^2+2q$, whose value at $q=2$ is zero.
At $(3,9)$ it is
$$
q^9-16q^7+21q^6+42q^5-101q^4+58q^3+5q^2-10q.
\tag{13}
$$
Its value at 2 is
$512-2048+1344+1344-1616+464+20-20=0$.
The retained data supplies the endpoint edges and coefficient polynomial
for every checked length; rerunning reconstructs the partition expansion.

There is also a direct independent proof at $k=2$: among three signs two
agree, and any pair of distinct indices is a positive-difference two-term AP.
The opposite signs at length two show the lower bound.

### Independent recurrence for $k=4$

A four-term signed sum misses absolute value 2 exactly when it is zero.
In particular every consecutive block of four must sum to zero.
Subtracting neighboring block equations gives $f(i+4)=f(i)$ whenever both
indices occur.

For $4\leq N\leq6$, the first four entries must be a balanced seed with
two signs of each kind, of which there are six. The recurrence determines
any remaining entries, and only difference one is possible, so all six work.

For $7\leq N\leq12$, the AP $0,2,4,6$ has sum
$2(f(0)+f(2))$. It must vanish, so $f(2)=-f(0)$.
The balanced seed then forces $f(3)=-f(1)$.
Every avoiding coloring is therefore the restriction of
$$
(u,v,-u,-v,u,v,-u,-v,\ldots),\qquad u,v\in\{-1,1\}.
\tag{14}
$$
Conversely all four choices work through length 12.
Every admissible difference is at most 3. An odd difference visits each
residue class modulo four once; difference two alternates opposite signs.
Both sums are zero.

At length 13, the positive-difference AP $0,4,8,12$ lies in the interval and
has sum $4u$, eliminating all four possibilities. At length 12 its last
point is outside the interval, so it cannot be used early. For $N<4$, there
are no four-term APs and all $2^N$ colorings avoid.

This proves the count formula used by the independent program. The
zero at 13 follows from the exhibited obstruction to all recurrence seeds;
it is not inferred from a hard-coded assertion of the desired minimum.
The program retains the allowable seeds and checks its first witnesses
against the endpoint-generated APs.

### Complete count and witness coverage

| $k$ | Lengths, in order | Numbers of avoiding colorings, in that order |
| --- | --- | --- |
| 2 | $0,\ldots,3$ | $1,2,2,0$ |
| 3 | $0,\ldots,9$ | $1,2,4,6,10,14,20,16,6,0$ |
| 4 | $0,\ldots,13$ | $1,2,4,8,6,6,6,4,4,4,4,4,4,0$ |

Every AP count, coloring-domain size, avoiding count and first avoiding
coloring agrees between the fresh author route and the independent route,
in all 28 rows. The independent route represents 17,421 assignments;
it does not enumerate 17,421 sign tuples.
The separate AP count formula is
$mN-(k-1)m(m+1)/2$, with
$m=\max(0,\lfloor(N-1)/(k-1)\rfloor)$.
Indeed, each $1\leq d\leq m$ permits exactly $N-(k-1)d$ starts, and no
larger difference permits a start. Summing these counts gives the formula;
each AP has a unique start and positive difference.

The first avoiding witnesses at one below each minimum are, respectively,
$(-1,1)$,
$(-1,-1,1,1,-1,-1,1,1)$, and
$(-1,-1,1,1,-1,-1,1,1,-1,-1,1,1)$.
All earlier lengths have positive counts, and the claimed upper lengths
have count zero. This establishes each exact positive minimum.

The negative input asks for minima 2, 8 and 12 at $k=2,3,4$.
It was executed under Python -O and exited 1, with respective avoiding
counts 2, 6 and 4 and concrete witnesses. Thus each computational case has
an observed failing input at the relevant boundary.
For the author's separate predicates, an omitted AP such as $(0,1)$ at
$k=2,N=2$ would fail inventory agreement; reporting $(-1,-1)$ there as an
avoider would fail witness validation; the false upper lengths above fail
universality; a proposed minimum of 4 at $k=2$ fails its smaller-length
test because length 3 already has zero avoiders. These describe failure
conditions, not modifications made to the
frozen author program.

The independent route changes both the counted objects and the arithmetic
primitive. A sign-loop stopping or bit-coverage error cannot silently remove
the same assignments from the partition inclusion-exclusion calculation.
The four-term recurrence avoids a full assignment census altogether.
Their endpoint inventory and the closed AP-count formula also differ from
the author's subset and bounded-start inventories. Agreement alone is not
the warrant: equations (12), the partition induction, the conditional-count
argument and the proof of (14) provide the mathematical reductions.

## One-term cases and exponential consequences

For $k=1$, every admissible sum is a single sign, of absolute value one.
Thus for every positive $N$ no coloring has a one-term AP of discrepancy 2,
and the universal property for target 2 fails. There is no $N(1,2)$.

For target $\sqrt1=1$, at length one take $a=0,d=1$.
Its endpoint is zero and its absolute sum is one, including equality.
Since every positive length is at least one, the minimum is $N(1,1)=1$.
The source default N176Sqrt 1 = 0 has no role in this argument.

For integers $k\geq5$, the positive factors satisfy
$k-3\geq k/3$, $k^2-1\leq k^2$, $k-1\leq k$ and $2k+1\leq3k$.
Therefore
$$
T_2(k)\leq18k^3,\qquad
\lfloor T_2(k)\rfloor+1\leq18k^3+1\leq19k^3.
\tag{15}
$$
For every integer $k\geq1$, $k\leq2^k$: start at one and use
$k+1\leq2k\leq2^{k+1}$ in the induction step.
For $k\geq5$, also $19\leq2^k$, since $19\leq32$ and powers of two increase.
Hence
$$
19k^3\leq 2^k(2^k)^3=16^k.
$$
At $k=2,3,4$, the independently established minima are
$3\leq256$, $9\leq4096$, and $13\leq65536$.
These cover exactly the remaining domain of the exponential bound for 2.
No assertion for $k=1$ is imported.

For $k\geq2$, the three factors in $T_s$ satisfy
$k^2-k+1\leq k^2$, $k-1\leq k$, and $k(k-1)+1\leq k^2$.
Thus
$$
T_s(k)\leq\frac43 k^5,\qquad
\lfloor T_s(k)\rfloor+1\leq\frac43k^5+1\leq3k^5.
\tag{16}
$$
Now $3\leq2^k$ and $k\leq2^k$, so
$3k^5\leq2^k(2^k)^5=64^k$.
The remaining $k=1$ case is the actual minimum $1\leq64$ just proved.
These are uniform inequalities for every parameter in the stated ranges,
not extrapolations from finite tests.

## Weakest steps and strongest attempted refutations

The following table identifies at most three weakest links for each conclusion.
The derivations above supply the links; the last column states their composition
and the attempted break, rather than relying on agreement with source output.

| Conclusion | Weakest steps independently rederived | Strongest attack and result |
| --- | --- | --- |
| Polynomial bound for 2 | (1) Geometric orthogonality and the normalized Fourier moment, (1)–(3); (2) the pair-energy diagonal and both difference multiplicities, (4)–(6); (3) wrap loss, positive gap (9), and the strict floor/minimum bridge. | Try to concentrate all large cyclic sums on wrapping progressions. The alternating six-point example below shows why this is a real threat. Exact wrap counting and the gap in (9) defeat it whenever the stated threshold is exceeded, for every coloring. The integral threshold at $k=5$ also tests the required strict inequality. No defect found. |
| Polynomial bound for $\sqrt{k}$ | (1) The exact weighted identity and nonnegative Fourier masses; (2) integer-square cap $k-1$, exact weight sums (10), and gap (11); (3) non-wrapping transport, equality in the square-root target, and the floor/minimum bridge. | Try to use a square $k$ to reverse a strict/non-strict comparison, or lose an endpoint in the wrap estimate. Equation (8) includes equality, and a last point equal to $N$ is counted as wrapping. The period-four example below fails only after its obstructing AP enters the interval. The smallest-domain gap is positive at $k=2,N=13$. No defect found. |
| $N(2,2)=3$ | (1) All sign colorings are represented by codes; (2) any pair is an ordinary two-term AP, so pigeonhole gives the upper value; (3) opposite signs give the lower value and (12) reproduces all counts. | Try to advance the minimum to 2. The retained witness $(-1,1)$ defeats it, and the negative control detects two avoiders. Try to leave an avoider at 3: pigeonhole and the zero partition count separately rule it out. No defect in the stated minimum found. |
| $N(3,2)=9$ | (1) Missing discrepancy 2 is precisely a nonmonochromatic coloring of the triple constraints; (2) partition inclusion-exclusion counts every assignment with its exact sign; (3) the zero in (13), positive smaller counts and constructed witnesses imply the minimum. | Try to extend an avoiding length-eight pattern to a length-nine counterexample, or miss one through the author's sign enumeration. The independent constraint expansion gives zero at 9 without that enumeration, while the false minimum 8 is rejected with six avoiders. All nine-point endpoint constraints and the polynomial coefficients are retained. No defect found. |
| $N(4,2)=13$ | (1) Zero sums of neighboring four-blocks force period four; (2) the difference-two AP reduces the six balanced seeds to four; (3) difference four at length 13 eliminates every seed, whereas every allowed difference through length 12 gives sum zero. | Try to keep a balanced period-four sequence forever, or use $0,4,8,12$ at length 12. It is excluded from length 12 and included at 13, where its sum is $4u$. The false minimum 12 leaves four witnesses; the obstruction proves none survives at 13. No defect found. |
| Nonexistence of $N(1,2)$ | The one-term sum has absolute value one for every start and coloring; positive length always has at least one coloring. | Try to make a very large interval or positive difference change a one-term sum. Neither changes its single value. The target 2 is impossible at every positive length. No defect found. |
| $N(1,1)=1$ | The admissible choice $a=0,d=1$ works at length one for both signs; one is the smallest positive integer. | Try to substitute the source's default N176Sqrt 1 = 0 or to demand two distinct indices from a one-term AP. Neither matches the statement. Its actual endpoint is $a+0d=0$, and equality at discrepancy one is allowed. No defect found. |
| Exponential bound $16^k$ | (1) The polynomial conclusion supplies existence for $k\geq5$; (2) the rounding estimate (15) and induction $k\leq2^k$ prove the uniform comparison; (3) the three separately verified finite minima cover exactly $k=2,3,4$. | Try to leave a gap before the polynomial domain or extend the conclusion to the nonexistent $k=1$ case. The three bases fill the former and the statement explicitly excludes the latter. The constant $19$ is absorbed only from $k=5$, where $2^k\geq32$. No defect found. |
| Exponential bound $64^k$ | (1) The square-root polynomial conclusion supplies existence for $k\geq2$; (2) (16) and $3\leq2^k$, $k\leq2^k$ prove the uniform comparison; (3) the actual $N(1,1)=1$ covers the remaining parameter. | Try to use the guarded zero fallback as the base or apply $3\leq2^k$ at $k=1$. Neither is used: the separate one-term proof supplies that case. No defect found. |

The most consequential attempted refutation was the cyclic-to-ordinary
passage. For $k=5,N=6$, the alternating coloring
$f(a)=(-1)^a$ has only difference-one ordinary five-term APs, each of absolute
sum one. On the cycle, every even difference gives absolute sum five.
Thus a large cyclic moment alone cannot entail the ordinary conclusion.
This is an exact counterexample to that shortcut, not to the commissioned
bound. Extending the alternating coloring to any interval of length at least
9 already supplies the ordinary AP $0,2,4,6,8$ of absolute sum five.
More generally, (7) accounts for every possible wrapping start, and (9) leaves
a strictly positive gap at every stated polynomial length, including
$1/2114$ at $k=5,N=1057$.

The same failure mechanism is visible for $k=4$ and the coloring with period
$(-1,-1,1,1)$: at length four the ordinary sum is zero, while cyclic
difference four has absolute sum four. The exact recurrence analysis shows
that it avoids target 2, which equals $\sqrt4$, through length 12 and fails
at length 13. It therefore checks the model and endpoint obstruction without
purporting to refute the much larger square-root polynomial bound.
These examples test a mechanism the proof must control; merely finding
large cyclic sums would have missed it.

Additional attacks covered composite $N$, non-coprime and repeated cyclic
steps, $N=1$, empty $D=0$, saturated wrap sets, the nonnegative coefficient
$k^2-b$, natural subtraction before real coercion, and integral thresholds.
The Fourier proof requires only $N>0$. Natural subtractions used in the public
ranges agree with their integer differences: $k-1\geq0$, $k-3>0$, and
$k^2-(k-1)=k^2-k+1>0$. No discarded exceptional coloring or unstated
arithmetic restriction survived these checks.

## Premises, interfaces and actual reading depth

The premise list was derived from the frozen statement, proof, source slices
and every consequence sentence. There is no consumed native L-claim and no
accepted external Cassels, Turán, van der Waerden or other source theorem
being taken as a black box. The elementary finite identities, integer
inequalities and well-ordering used here are stated and derived at their
points of use. The exact external source versions are identified in the
subject block. The following table distinguishes the source interfaces from
any claim of formal execution.

| Input interface and locator in the preserved subject | Hypotheses and consumed content | Reading and verification scope |
| --- | --- | --- |
| Basic, lines 12–244: cyclicIndex, cyclicAPSum, wraps, ordinaryAPSum, card_wrapStarts_le and moment upper estimates | Positive $N$; integer signs; $d\geq1$ when returning an AP. Pointwise bound $k^2$, endpoint guard and count of wrapping starts. | Whole text read; mathematical deductions rederived in (7) and the ordinary-index argument. No coprimality restriction is added. |
| Basic, lines 246–739: fejerPairEnergy through casselsGeomLowerClaim_true | Unit $z$, natural $k,D$. Pair terms are nonnegative; diagonal contribution and finite triangle sums yield the scalar lower bound. | Whole text read; full finite four-sum expansion and difference counts rederived in (4)–(5). Conditional scalar helpers are discharged, not assumed. |
| Basic, lines 741–1108: fourierCoeff, expansions, orthogonality and unconditional moment lower bounds | Positive finite cyclic group; signs give unit squared mass. | Whole text read; normalized geometric orthogonality, inversion, Parseval and moment expansion rederived in (1)–(3),(6). No unread Fourier theorem is an external premise. |
| Basic, lines 1110–1324: finZModEquiv, zmodColoringOfFin and cyclic moments | Canonical representatives and integer-to-complex coercion preserve every sum, norm square and average. | Whole text read; the explicit bijection and normalization are checked above. |
| Basic, lines 1326–1702: real threshold, ordinary existence, htmlBoundNat, erdos176Good, erdos176Number, N176_le_report_bound_explicit | $k\geq5$, real threshold, positive length, every sign map. Establish a successful length before the least element. N176's zero branch is outside the theorem's range. | Whole text read; gap (9), positivity, real floor, existence and least-value interface verified. The final declaration has no outstanding Cassels hypothesis. |
| Sqrt, lines 12–260: fejerWeight, its two sums, triangle multiplicities and fejerPairEnergy_eq_sq_add_two_weighted | Natural $D$, $1\leq d\leq D$, unit $z$. Nonnegative weights and exact weighted scalar bound. | Whole text read; (4)–(5),(10) rederive every required finite identity. |
| Sqrt, lines 262–766: weighted cyclic lower bound, sqrtLargeSq, moment upper estimates and ordinary existence | Positive $N$, $k\geq2$, squared integer target. Common Basic identities plus integer cap $k-1$ and weighted wrap loss. | Whole text read; (6)–(8),(10)–(11) establish the complete interface, including the non-strict square-root comparison. |
| Sqrt, lines 768–964: sqrtHtmlBoundNat, erdos176SqrtGood, least number and N176Sqrt_le_report_bound_explicit | $k\geq2$; successful positive length before Nat.find. Default zero below two is not a minimum assertion. | Whole text read; floors, positivity and the guarded abbreviation checked separately from the actual one-term minimum. |
| SmallKCommon, lines 1–45; K2, K3, K4, each lines 1–23 | Boolean sign codes, bounded positive differences, exactAtCode = goodCode together with allBeforeFalse. | Whole text read. The ordinary-sign bridge is supplied above. The native_decide invocations were neither run nor used as warrants; the exact finite claims were freshly re-established by both computational routes. |
| K1, lines 1–27; exponential deductions, lines 1–15 | A single signed value has magnitude one; positive minimum and polynomial comparisons on the stated domains. | Whole text read; both one-term claims and both infinite consequences proved above with every base. |
| Candidate proof, lines 1–148; statement, lines 1–24 | Ordinary APs, non-strict targets, real division, positive minima, translation, both polynomial and exponential conclusions. | Whole text read, including every supplied consequence and cut marker. No omitted standing or author assurance is consumed. |
| Finite checker, lines 1–93; fixture, lines 1–359 | Exact inputs $(2,3),(3,9),(4,13)$ and all lengths from zero to each bound. | Whole text and fixture read. Unchanged checker rerun; every concrete data row independently reproduced. Scope is exactly those finite cases. |
| Supplied runtime closure | Checker, evidence_parser and their import closure needed by the unchanged script. | All 17 files read whole, including import/initialization behavior. Only the named checker route executed. No claim about uncalled gate, ledger, audit or corpus utilities. |
| Manifest and provenance, whole | Extraction identity, cut, source versions, credits and stated licensing limits. | Whole read. These identify material; they do not establish a theorem, a source build or equality with an unlisted archive file. |

**Dependency reading at verdict filing, 2026-10-15 UTC:** the consumed-native-claim set is empty. A live ledger read is therefore inapplicable and was
excluded by the commission; no stale or pending native premise is silently
being relied on. No pending source grade is assumed. All substantive
mathematical interfaces in the table are within this examination.

The acyclic order for the batch is: common finite identities and model
bridges; the two polynomial conclusions separately; the three finite minima
and both one-term conclusions independently; then the exponential bound for 2
using its polynomial conclusion and the three finite minima, and the
square-root exponential bound using its polynomial conclusion and the
one-term minimum. The square-root polynomial proof uses common Basic
identities, not the discrepancy-2 polynomial conclusion. The finite proofs
use neither polynomial bound. Any grading of the consequences must preserve
these dependencies and cannot substitute agreement on the last arithmetic
line for acceptance of a consumed premise.

## Checklist

Each row below applies to all nine restated conclusions. Where a failure mode
has no corresponding mathematical operation, the inapplicability is stated
explicitly. The claim-specific derivations and attacks in the preceding table
supply the evidence for the shared verdicts.

### Canonical failure modes

| Failure mode | Verdict and coverage |
| --- | --- |
| “Almost all” quietly upgraded to “all” | Not found. The Fourier identities hold for each fixed coloring and every positive $N$; no exceptional coloring is removed. The finite counts cover every assignment in each declared domain. Both one-term assertions quantify over all relevant signs and lengths. Exponential comparisons hold for every integer in their stated ranges. |
| Induction that presupposes termination | Not found. Inclusion-exclusion inducts over a finite, explicitly generated edge list; the witness construction runs through $N$ vertices. The only infinite-parameter induction proves $k\leq2^k$ with its base and successor step. The remaining proofs do not require iterative termination. |
| Probabilistic or averaging heuristics presented as proofs | Not found. Equations (1)–(6) and (10) are exact finite sums. Nonnegative masses sum to one and wrap upper bounds are pointwise before averaging. There is no sampled probability estimate. Finite minima and one-term cases do not rely on a heuristic average. |
| Circular use of an equivalent target | Not found. The scalar pair estimate follows from nonnegative squares; successful lengths precede minimum selection. The finite independent counts do not assume the proposed minima, and the four-term zero at 13 follows from an explicit obstruction. The exponential consequences use the acyclic order stated above. |
| Exceptional sets dropped from density arguments | Inapplicable: there is no density or asymptotic exceptional-set argument. The possible finite exceptional set of wrapping starts is instead counted exactly and paid for in (7); none is discarded. |
| Finite verification cited beyond base-case coverage | Not found. The executable domain is exactly the 28 listed rows. Infinite polynomial and exponential families have symbolic proofs. The one-term universal claims are proved directly, not inferred from those rows. |
| Convergence of a relaxed or averaged system substituted for actual objects | No convergence claim occurs, so its limit form is inapplicable. Its relevant model-transfer risk was attacked explicitly: (7) and the strict gaps force a non-wrapping ordinary AP, and the Boolean/sign and translation bridges preserve the exact target. |

### Named patterns

| Pattern | Verdict and coverage |
| --- | --- |
| Model-class transport instead of entailment | The classification/axiom-extension form is inapplicable: no new axiom system is classified. The related transfer question is discharged explicitly for Fin, cyclic representatives, ordinary indices, Boolean signs and translated intervals. The finite and one-term claims are in the original model. |
| Uniformity over an infinite family asserted from finitely many instances | Not found. Both polynomial gaps and both exponential comparisons are symbolic in $k$ with the displayed parameter dependence. No finite checks are used to infer these uniform bounds. The exact minima have finite, expressly bounded scope; one-term nonexistence is a direct formula for every $N$. |
| Extremal claims audited in the claim's own units | Satisfied. The exact minima are lengths in the ordinary AP model: positive lower witnesses and zero avoider counts at the upper lengths. Least positive values for the polynomials are formed only after existence. No optimality of polynomial or exponential constants is asserted; a zero source fallback is never counted as an attained minimum. |
| Consequence sentences are claim surfaces | Satisfied. Both exponentials, all three finite minima, nonexistence at $(1,2)$, the value at $(1,1)$, translation and least-value deductions receive explicit arguments and separate conclusion verdicts. No stronger domain is inferred from neighboring statements. |
| Carry hypotheses actually used by a quantified argument | Satisfied. $N>0$, $k\geq5$ or $k\geq2$, sign-valued colorings, positive ordinary difference, real divisions and non-strict targets are retained. All averages are finite. The $k=1$ cases have separate proofs and do not enter formulas requiring $k-3>0$ or $k(k-1)>0$. |
| A composition inherits its unproved premises | No missing consumed clause found. Every interface is in the premise table, including Fourier normalization, wraps, integer caps, code surjectivity, floors, minima and bases. No unexecuted native_decide result or uninspected external theorem supplies a premise. The grading order for the consequences is explicit. |
| Reproducibility notes are claims | Satisfied for this examination's executable claims: the driver and exact inputs were freshly run, and actual script imports checked. All 28 rows and first witnesses agree. The unchanged checker's historical docstring path is expressly obsolete; it was not silently claimed runnable. The supplied runtime and current package-relative route below are the assessed rerun path. |
| Verifier quotations are claims | Inapplicable to this blind subject. Prior reports and standing characterizations were excluded and unread; no earlier verifier ruling is quoted as evidence. This examination's own verdict words and coverage statements are given in full. |
| Verdict words spelled in full | Satisfied. Every conclusion below carries refutation-failed in full. No abbreviation merges it with the opposite verdict, refuted-as-stated; proof defective; statement unresolved is not used to mean a disproof. |
| Certified-bracket functions fail loudly | Inapplicable: no approximate enclosure, numerical integration, iterative certificate or period-sensitive numerical window is used. All finite arithmetic is integral. Unsupported finite domains and malformed input raise an error with nonzero exit; no exhausted cap is returned as a certificate. |
| A harness leg with no failing input is decoration | Satisfied for each finite case: the retained false minima 2, 8 and 12 fail with exact counts and witnesses, including under Python -O. Inventory disagreement and invalid-witness inputs are specified above; the driver's comparison rejects unequal data or wrong import origins. Analytic claims are derivations, not decorative executable legs. |
| A gate that reads caches instead of rerunning is defective | No gate is used as a mathematical warrant. The rerun driver executes both routes and controls first, then compares fresh data with the retained fixtures. The original fixture is concrete mathematical data, not an accepted success receipt. |

Correlated-sample inference is inapplicable: no random sample, statistical
confidence statement or repeated-run independence estimate appears.
The evidence-coverage discipline is applied throughout: static mathematical
proof coverage is separated from Lean execution, the exact finite rows from
infinite families, and the independent route from both author algorithms.
This is a first examination; the distinct-attack requirement for a second
independent review cycle is inapplicable. Structural disjointness for the
computational batch is supplied and justified.

### Erdős whole-claim checklist

| Item | Verdict and evidence |
| --- | --- |
| Quantifiers and scope | Satisfied for all nine conclusions. The restatement specifies every parameter range, every coloring, positive length, positive difference and non-strict target. Empty intervals occur only in the finite lower-bound checks; no positive minimum is zero. |
| Circularity | No circular step found. The pair-energy argument, finite expansion and recurrence supply foundations independent of the target; the batch composition is acyclic and existence precedes Nat.find. |
| Model and convention changes | No unsupported change found. The cyclic and Boolean models are connected explicitly to ordinary progressions; the translation to $[1,N]$ is bijective. The alternating and period-four attacks test the failure of omitting this bridge. |
| Finite and statistical overreach | Not found. Finite checks establish only the stated finite census and minima. Infinite bounds and one-term nonexistence are proved symbolically. Statistical inference is inapplicable. |
| Uniformity | Satisfied. All sum exchanges are finite. The exact gaps carry their full $k,N$ dependence, and (15)–(16) give uniform comparisons on explicit domains. Finite census assertions are not promoted to uniform claims. |
| Extremal conclusions | Satisfied in interval-length units. Every exact minimum has an upper proof and lower witnesses; the other minima exist by well-ordering a nonempty positive set. Sharpness of the displayed general bounds is not claimed. |
| Consequences and composition | Satisfied subject to the stated acyclic grading order. Every consequence is individually attacked, including floors, both exponentials and all bases. No default abbreviation or source build supplies a missing link. |
| Computation | Satisfied for the finite claims: exact integer arithmetic, explicit bounded inputs, all 28 rows, concrete witnesses and polynomial/recurrence certificates, and observed nonzero negative controls. This item is otherwise inapplicable as proof support for the analytic and one-term results. |
| Reproduction | Satisfied for the computational batch by fresh unchanged execution plus a structurally disjoint partition/recurrence route. The retained driver regenerates its outputs, checks actual script imports and compares all data. Noncomputational conclusions retain complete derivations and attacks. |
| Source and verdict fidelity | Satisfied within the supplied extraction. Credits, exact external versions and source limits are preserved. Static proof reading is not described as a kernel check; unlisted archives and prior rulings are not represented as examined. The nine verdicts below cover only the frozen subject. |

## Reproduction

The retained package is self-contained for the checks, with the repository's
already prepared Python environment. It requires no installation, synchronization,
Lean, network, corpus scan, gate or ledger command. The independent program uses
only the Python standard library. The unchanged author program additionally
uses the supplied 17-file runtime closure.

From the directory containing this report, set REVIEW_SCRATCH to an absolute
writable scratch directory and run the following. The output directory is
explicitly selected; no result is written into the subject snapshot.

~~~sh
test -n "$REVIEW_SCRATCH" &&
nice -n 10 env \
  -u VIRTUAL_ENV -u UV_PROJECT -u UV_PROJECT_ENVIRONMENT \
  -u UV_WORKING_DIR -u UV_NO_PROJECT -u PYTHONPATH \
  PYTHONDONTWRITEBYTECODE=1 \
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 BLIS_NUM_THREADS=1 \
  uv run --no-sync python -B rerun.py --output "$REVIEW_SCRATCH"
~~~

The driver runs sequentially, using the interpreter selected by this command.
For the author invocation it sets PYTHONPATH to the absolute
subject/tools_runtime directory and invokes
subject/finite/small_cases.py.txt as an actual script file, with --output
under the selected scratch directory. It verifies the loaded tools source
paths from that invocation's import trace. The original historical docstring
command is left unchanged in the snapshot and is not the current path.
The driver then runs finite/independent.py on finite/claims.json and on
finite/negative_claims.json, the latter under Python -O.

Expected successful driver result: exit zero; all 28 count/witness rows
equal; 17 supplied tools origins confirmed; the positive independent run exits
zero and the three-case negative run exits one. The driver writes fresh
author_results.json, independent_results.json, negative_results.json and
verification.json plus disposable subprocess diagnostics into scratch.
Ordinary runtime is under one minute on one thread; the bounded inputs here
completed within that scope. A failure in a constituent run, comparison or
import-origin obligation makes the driver exit nonzero. No cached success is
an input to its decision.

For a direct independent run from the same directory:

~~~sh
test -n "$REVIEW_SCRATCH" &&
nice -n 10 env \
  -u VIRTUAL_ENV -u UV_PROJECT -u UV_PROJECT_ENVIRONMENT \
  -u UV_WORKING_DIR -u UV_NO_PROJECT -u PYTHONPATH \
  PYTHONDONTWRITEBYTECODE=1 \
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 BLIS_NUM_THREADS=1 \
  uv run --no-sync python -B finite/independent.py \
  --input finite/claims.json --output "$REVIEW_SCRATCH/direct.json"
~~~

The scratch directory must already exist for this direct invocation.
Replacing the input by finite/negative_claims.json, adding Python's -O
flag and choosing another output filename must return exit one, not zero.
The full driver performs that control automatically. These instructions use
package-relative inputs so moving the complete report directory does not
alter a mathematical check.

Retained artifacts are the unchanged subject snapshot, the independent source,
the two exact input files, the complete fresh author data, the independent
counts/certificates and the failed-control counts/witnesses. In particular
[finite/author_results.json](../../assets/kitamura/reviewed/finite/author_results.json) is the concrete
fresh count/witness data, not a terminal success summary. The independent
outputs retain endpoint AP inventories, partition polynomials and conditional
witness counts, or the allowable recurrence seeds. The prose derivation is
essential to interpreting the four-term recurrence computation.

## Verdict and limitations

| Conclusion | Mathematical verdict |
| --- | --- |
| Polynomial bound for 2, every integer $k\geq5$ | **refutation-failed** |
| Polynomial bound for $\sqrt{k}$, every integer $k\geq2$ | **refutation-failed** |
| $N(2,2)=3$ | **refutation-failed** |
| $N(3,2)=9$ | **refutation-failed** |
| $N(4,2)=13$ | **refutation-failed** |
| Nonexistence of $N(1,2)$ | **refutation-failed** |
| Actual minimum $N(1,1)=1$ | **refutation-failed** |
| $N(k,2)\leq16^k$ for every integer $k\geq2$ | **refutation-failed** |
| $N(k,\sqrt{k})\leq64^k$ for every integer $k\geq1$ | **refutation-failed** |

The frozen argument survived the stated attacks. No missing essential
mathematical premise, counterexample or unfinished mathematical coverage
obligation was found within the commissioned read set. This includes the
complete finite Fourier/Fejér and wrapping chain, all model and minimum
bridges, exact finite rerun and disjoint reproduction, and every base and
exponential consequence.

The scope is mathematical proof inspection plus the specified exact finite
computations. No Lean elaboration, native_decide execution, compiler trust
audit or kernel replay was performed. The report does not establish fidelity
of an unlisted source file, the complete archives, their license texts, any
reported source build, or later changed bytes. The finite data says nothing
about other parameter values without the displayed mathematical reductions.
No optimality of the general bounds is asserted.

A distinct fresh grader must assess this unchanged report, its independence
and its keeper evidence, preserving the premise order for the two
consequences. This report awards no tier, problem status or acceptance.
