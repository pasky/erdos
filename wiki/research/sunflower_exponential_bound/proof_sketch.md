---
name: research/sunflower_exponential_bound/proof_sketch
title: "Sunflower exponential bound: current argument"
desc: |
  Problem 20 is equivalent to a sunflower statement for spread families; L214
  refutes the constant-spread matching route and L215 any bounded-core
  variant. Maximal-rate link chains can fail; a linear Hall argument bounds
  affine linear word families, and slice rank handles links on few points.
  A counting extension gives Fourier criteria allowing arbitrary cores.
  The general structural inverse remains open.
created: 2026-10-15T17:54:12Z
updated: 2026-10-15T17:54:12Z
---

***

## Target and standing

The target is
[[problems/set_systems/E0020/_index|Problem 20, which the catalog records as open; nothing here changes that]].
Let $f(n,k)$ be the least number such that every family of at least $f(n,k)$
distinct $n$-element sets contains a $k$-sunflower: $k$ distinct members whose
pairwise intersections all equal one set, the core, which may be empty. The
question is whether $f(n,k)<c_k^n$ for each fixed $k\ge3$, with $c_k$
independent of $n$ and of the ground set. The case $k=2$ is immediate. A
disproof needs one $k$ and $k$-sunflower-free families of $n$-sets whose size
to the power $1/n$ is unbounded; a bound exponential in the size of the ground
set does not suffice when that size is unrestricted. The general upper bound
used for comparison here, for $n\ge2$, is
$f(n,k)\le(Ck\log n)^n$, from
[[../library/set_systems/bell_2021_note_sunflowers/theorem_1|Bell–Chueluecha–Warnke's Theorem 1]].

**Problem 20 is not solved.** Every result recorded for this attack is
author-recorded by Plasma AI and carries at most tier 0. The claims
[[theory/set_systems/L214_spread_intersecting_families/_index|L214]] and
[[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215]]
record the spread obstructions; the structured positive theorem is
[[theory/set_systems/L268_linear_word_sunflowers/_index|L268]]. An
outside preprint, Fukuyama's arXiv:2212.13609v3, announces a proof of the
conjecture with base $Ck^4$. The
[[research/sunflower_exponential_bound/fukuyama_sequence_gap|explicit product-family test]]
contradicts its Lemma 2.1 and shows that its core-selection inequality (2.4)
need not have any solution under the stated hypotheses. This is an
author-recorded failure of intermediate assertions, not a disproof of the
conjecture. The preprint is not used as a premise.

## Conventions

A family of $n$-sets is *absolutely $R$-spread* if every nonempty $T$ lies in
at most $R^{n-|T|}$ members (the convention of Bell–Chueluecha–Warnke and of
Rao), and *normalized $R$-spread* if every nonempty $T$ lies in at most
$R^{-|T|}|\mathcal F|$ members, which forces $|\mathcal F|\ge R^n$ (the
convention of Alweiss, Lovett, Wu and Zhang and of Tao). Normalized $R$-spread
implies normalized $R'$-spread for $R'\le R$. The
[[research/sunflower_exponential_bound/refined_spread_obstructions|thinning lemma]]
converts normalized $Q$-spread to an absolute $r$-spread subfamily larger
than $r^n$ when $r\ge2$, $n\ge2$ and
$Q\ge4er(8r)^{2/(r-1)}$; $Q\ge32r$ suffices for $r\ge16$. It has no
upper bound on the original family size. The narrower thinning statement
in L214 remains sufficient for that claim.

## Held links

1. **Link reduction (elementary, author-recorded).** If $|\mathcal F|>R^n$,
   choose an inclusion-maximal $T$ with $|\mathcal F_T|>R^{n-|T|}$. The empty
   set qualifies and $|T|<n$. The link $\{S\setminus T:S\in\mathcal F_T\}$ is
   absolutely $R$-spread with more than $R^{n-|T|}$ members, and a
   $k$-sunflower in it lifts to a $k$-sunflower of $\mathcal F$ whose core
   contains $T$. The argument is spelled out in
   [[research/sunflower_exponential_bound/spread_matching_obstruction|the obstruction note]].
2. **Spread form (equivalence, elementary).** By link 1, Problem 20 holds,
   after a harmless enlargement of the base to handle strict endpoints, if

   > **SF($k$):** every absolutely $R_k$-spread family of $n$-sets with more
   > than $R_k^n$ members contains a $k$-sunflower, for every $n$.

   Conversely Problem 20 with constant $c_k$ gives SF($k$) for every
   $R_k\ge c_k$, since such a family has more than $c_k^n$ members. In the
   forward direction SF($k$) gives $f(n,k)\le\lfloor R_k^n\rfloor+1$,
   and, for example, $c_k=R_k+2$ meets the target's strict inequality.
   Thus SF($k$) is equivalent to the target; it changes the vocabulary and supplies the
   spread hypothesis, but not the difficulty.
3. **The matching route is closed.** The sufficient condition $M(k)$, that
   absolutely $R_k$-spread families with more than $R_k^n$ members contain $k$
   pairwise disjoint members, is false for every $k\ge3$. For $R_k\ge16$,
   [[theory/set_systems/L214_spread_intersecting_families/_index|L214]]
   supplies the counterexamples. The general thinning argument above
   supplies them for every $R_k\ge2$; when $R_k<k-1$, a family of $k-1$
   singletons already refutes the assertion. For $k=2$, every $R_k\ge2$
   fails, but $R_k=1$ must be excluded: absolute $1$-spread forces
   disjointness. These distinctions do not affect the target $k\ge3$.
   This also refutes the proposed asymptotic strengthening beside
   [[../library/set_systems/rao_2020_coding_sunflowers/lemma_2|Rao's Lemma 2]]
   that the lemma might hold with $r(p,k)=O(p)$. Varying the substitution
   scales in the
   [[research/sunflower_exponential_bound/refined_spread_obstructions|refined obstruction]]
   gives a lower obstruction of order $\log n/\log\log n$ along its
   uniformities. This normalized order was already recorded by ALWZ,
   Section 4 after Theorem 4.2, with attribution to
   Lovett–Solomon–Zhang (2019); no new asymptotic lower bound is claimed.
   The upper bound $C\log n$ is
   [[../library/set_systems/bell_2021_note_sunflowers/lemma_2|Bell–Chueluecha–Warnke's Lemma 2]],
   in the absolute convention. The normalized comparison is stated with
   its source qualifications in the obstruction note.
4. **Two obstructions at their scope.** The product of $n$ blocks of size $s$
   obstructs the random-hitting lemma at constant spread but has $s$
   disjoint members
   ([[research/methods/finite_set_thresholds|finite-set threshold note]]).
   The families of L214 obstruct the matching lemma and are intersecting, so
   every sunflower they contain has a nonempty core. A proof of SF($k$) must
   therefore find sunflowers with nonempty cores in some spread families.
5. **Cores must be allowed to grow.**
   [[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215, which substitutes sunflower-free triangle powers into the block families]]
   gives, for every $R\ge3$ and every $s$, an intersecting family with
   $R$-spread uniform measure in which every $k$-sunflower, $k\ge3$, has a
   core of at least $s$ points. So no lemma "spread at least $R_k$ forces a
   $k$-sunflower with a core of at most $s_k$ points", with $R_k$ and $s_k$
   independent of $n$, holds. At fixed $R>3$ the forced cores have about
   $\log_2\log_2n/\log_2(R/3)$ points. The general thinning lemma gives
   the corresponding obstruction for absolute $r$-spread families with
   more than $r^n$ members, for every $r\ge2$.
6. **Threshold for three petals.** Powers of a ten-triple intersecting seed
   on six points, recorded in the obstruction note, are intersecting, have no
   $3$-sunflower, and have normalized spread approaching $\sqrt{10}$. So
   $R_3\ge\sqrt{10}$ in the normalized form of SF($3$), above the value $2$ of
   the Erdős–Rado product.
7. **A maximal-rate chain need not find the core.** The
   [[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|chain obstruction]]
   gives, for every $A>5$, an $n$-uniform family larger than $A^n$ with
   matching number two, whose unique maximal-rate choices lead to a
   three-sunflower-free terminal family. An explicit sunflower is discarded
   along the way. Its proof uses the thinning lemma, the triangle powers,
   and an elementary union-and-cone recurrence, all at author standing.
   Favorable tie-breaking does not repair the procedure.
8. **Affine linear words satisfy an exponential bound.**
   [[theory/set_systems/L268_linear_word_sunflowers/_index|L268]]
   proves that a linear subspace $C\le A_1\oplus\cdots\oplus A_n$ over
   $\mathbb F_q$, of dimension at least $sn$, contains an $s$-dimensional
   subspace on which every coordinate is zero or injective. Its $q^s$
   words form a sunflower. Thus affine linear word families without a
   $k$-sunflower have fewer than $k^{2n}$ members, uniformly over the field
   and coordinate alphabet dimensions. The
   [[research/sunflower_exponential_bound/linear_word_families|coset argument]]
   gives an exponential bound for dense subsets of such a linear family,
   with dependence on the density.
   The proof includes the independent-representative lemma it uses. This
   structured result has author standing and no established novelty claim.
9. **Bounded additive growth also suffices.** In the binary encoding,
   the
   [[research/sunflower_exponential_bound/additive_word_families|covering argument]]
   shows that a sunflower-free family with growth ratios
   $K_2=|2F|/|F|$ and $K_4=|4F|/|F|$ has
   $|F|<(2(k-1)K_2 2^{K_4})^n$. Thus fixed fourfold growth gives an
   exponential bound. With the explicitly cited Plünnecke estimate,
   doubling at most $K$ gives base $2(k-1)K2^{K^4}$. This extends the
   positive result beyond linear families, but arbitrary words need not
   satisfy the growth hypothesis. An explicit binary Sidon family shows
   that extracting a bounded-doubling subfamily can require exponential
   loss even when the original family is sunflower-free.
10. **Links on few points, sections, and an intersecting normal form.**
    The
    [[research/sunflower_exponential_bound/slice_rank_spread_links|slice-rank note]]
    records, for $k=3$, a routine projection form of Naslund–Sawin's
    slice-rank bound for words and its consequence for set families: more
    than $\rho^m$ sets of size $m$ on at most $A\rho m$ points contain a
    $3$-sunflower once $\rho\ge e^3(27/4)A^2$, about $135.6A^2$, whatever
    the cores. So every link that link 1 produces from a counterexample at
    base $\rho$ covers more than $m\rho^{3/2}/11.65$ points. The note also
    proves that the target for $k=3$ is equivalent to the statement that,
    for some $c>1$, intersecting, absolutely $c$-spread families of
    $j$-sets without a $3$-sunflower have at most $(c-1)^j$ members. The
    slice-rank bound finds $3$-sunflowers in the families behind the
    Alweiss–Lovett–Wu–Zhang lower bound for robust sunflowers, and
    sections, whose sunflowers lift exactly, reach the unthinned families
    of L214 and L215. For the L214 thinning, a matching in a projected
    link finds a sunflower with a one-part core. The displayed section
    count tests can simultaneously fail after thinning, even with adaptive
    section choice; other links and sections are not excluded. These
    arguments are author-recorded; no novelty is claimed for the
    slice-rank inputs.
11. **Counting in affine spaces and a Fourier criterion.** The
    [[research/sunflower_exponential_bound/agreement_statistics|agreement-statistics note]]
    extends the Hall selection in the proof of L268: $k$ independent
    uniform words in any binary affine word space satisfy the coordinate
    sunflower pattern, allowing the all-equal tuple, with probability
    at least $2^{-(k-1)^2n}$. The homogeneous indicator has Fourier norm
    at most $(k!+1)^n$, including after restriction to the affine space.
    Therefore a family $F$ in a binary affine space $a+C$ contains a
    $k$-sunflower if
    $|F|>2^{(k-1)n+1/(k-1)}$ and its uniform measure has squared bias at
    most $1/(2((k!+1)2^{(k-1)^2})^n)$ on every nontrivial character of
    $C$. For $k=3$ the thresholds are $\sqrt2\,4^n$ and
    $1/(2\cdot112^n)$. The bias condition is not deduced from cardinality
    or spread. The note also proves that uniformly sampled families of
    $\lfloor\rho^n\rfloor$ words in $[B]^n$ have a $k$-matching with
    probability tending to one precisely above the exponential rate
    $\gamma_k(B)=B/((B)_k)^{1/k}$, for fixed $B\ge k$, away from
    equality. These are author-recorded statements. They neither bound
    the largest adversarial family nor confer independent standing.

## The open gap

The whole difficulty is SF($k$) itself: a way to produce a $k$-sunflower from
spread alone, with a nonempty core when the family has no $k$ disjoint
members, and with a core that may need to grow like $\log\log n$.

**Where the core must be found (author-recorded observation).** For a family
$\mathcal F$ of $m$-sets and a rate $R$, call
$\Pr[T\subseteq S]\,R^{|T|}$ the weight of a nonempty set $T$; a member has
weight $R^m/|\mathcal F|$. If a set of largest weight among all nonempty sets
is not a member, its link is again normalized $R$-spread, because no superset
is heavier.
Every member has largest weight exactly when
$|\mathcal F_T|\le R^{m-|T|}$ for all nonempty $T$, that is, when
$\mathcal F$ is absolutely $R$-spread. So following the heaviest sets, a form
of the link reduction of link 1, moves to a spread link while some proper
subset outweighs the members. It stops exactly at absolutely spread families,
where no proper subset outweighs a member. There the sunflower has to be found
with a light core, a set $T$ with $|\mathcal F_T|\le R^{m-|T|}$. The families
of L214 keep their properties in the absolute form, by L214's Lemma 4, so such
a light core must sometimes be nonempty. L215 and the general thinning
lemma show that it must sometimes be large in either spread convention.

No general candidate below is proved. Each is a statement to test against three kinds
of family. The L214 families have one-point cores. The L215 families have only
large cores. The powers of the ten-triple seed have no $3$-sunflower and
spread just below $\sqrt{10}$.

- **Core-finding through light links, recursively.** In an intersecting
  family every member meets a fixed member $S_0$, so some point $v\in S_0$ lies
  in at least a fraction $1/n$ of the members, and passing to such links loses
  a factor up to $n/R$ at every step, the loss behind the Erdős–Rado bound. A
  heavy point does not exist in general: by the remark on light core points in
  the obstruction note, the L214 families with more levels are still
  $\rho$-spread while every point lies in at most a fraction $2^{-h}$ of the
  members. There the sunflower's core point is light, but its link, with its
  own uniform measure, is again $\rho$-spread. A useful lemma would find a
  possibly light point or set whose link is again spread relative to its own
  size, and would continue in that link. By L215 it cannot always use a
  bounded-size core; a single step with a large core remains possible.
  The degenerate case is the one isolated above, an absolutely spread
  family in which no proper subset is relatively heavy.
- **Structure of spread families without $k$ disjoint members.** The
  proposition of the obstruction note shows that substitution powers behave
  like their seeds. A stability statement would reduce SF($k$) to the
  links. It would say that every spread family without $k$ disjoint members
  decomposes, like a seed, into a few heavy points and spread links.
- **Words over unbounded alphabets.** By
  [[../library/set_systems/alon_2013_sunflowers_matrix_multiplication/theorem_2_6|Alon–Shpilka–Umans' Theorem 2.6]],
  the target is equivalent, up to a factor $e$ in the base, to a bound for
  words over an arbitrary alphabet. The slice-rank bound of
  [[../library/set_systems/naslund_2017_upper_bounds_sunflower_free_sets/theorem_5|Naslund–Sawin's Theorem 5]]
  grows with the alphabet; its projection form in link 10 depends on the
  family's projections to two thirds of the coordinates instead, but a
  family whose such projections are nearly injective escapes it. The
  linear subclass in link 8 admits a bound independent of the alphabet
  without compressing it. A general family need not contain the linear
  structures supplied by that argument; no reduction of general words to
  the linear subclass is given here.
- **A dichotomy for unbalanced links.** By link 10, a counterexample to
  SF($3$) at rate $\rho\ge137$ yields an intersecting, absolutely
  $\rho$-spread family of $m$-sets with more than $(\rho-1)^m$ members on
  more than $m(\rho-1)^{3/2}/11.65$ points, with no section certificate in
  any link. A proof could split such families into a pseudorandom case,
  where counting in some link gives three pairwise disjoint members
  uniformly in the alphabet, and a structured case, where a passage to a
  link, section or projection gains in an explicit invariant. Link 11
  gives concrete sufficient Fourier conditions for the counting case,
  also allowing arbitrary cores, but only an exponentially small
  character bias when they fail. Converting that bias into a useful
  restriction with controlled total loss is unproved. Any such
  statement must handle random families, the unthinned and thinned
  substitution powers, and the two-part chain obstruction of link 7 at
  once. No such dichotomy is proved; since a sunflower is a matching in
  the link at its core, stating the residual this way is a reformulation
  of SF($3$), not a reduction of it.

## Source interfaces and their standing

- Bell–Chueluecha–Warnke, arXiv:2009.09327v2: Theorem 1, Lemma 2 and the
  quoted Theorem 3 of Rao and Tao, read on the library cards; their proofs are
  source readings, not independently reviewed here. The comparison in link 3
  uses Lemma 2 as stated, in the absolute convention with at least $r^n$
  members.
- Rao, *Coding for sunflowers*, arXiv:1909.04774v2: the primary proof,
  including the encoding argument in Section 4, was read. Lemma 2 and the
  remark on p. 2 are used at source standing. The remark is refuted only as
  far as the explicit constructions state: L214 covers $r\ge16$, and
  the general thinning lemma extends the counterexamples to $r\ge2$.
- Alweiss–Lovett–Wu–Zhang, arXiv:1908.08483v3: Theorem 2.5 in the weighted
  convention, used only for the normalized upper bound in the obstruction
  note; Rao's sharper bound is used only as they record it. Section 4's
  Theorem 4.2, its proof, and the immediately following comparison to
  Lovett–Solomon–Zhang were read in the primary transcription. The original
  cited lower-bound construction has not been checked here. Lemma 3.1, the
  lower bound for robust sunflowers, and its proof were read in the primary
  transcription, with the statement and the start of the construction
  checked on the page images of pp. 11–12. This construction supplies the
  comparison family tested in link 10; the general slice-rank estimate does
  not depend on it.
- Fukuyama, arXiv:2212.13609v3: Section 2's four-step proof was read,
  including the definitions and the interfaces from Lemma 2.1 through
  Proposition 2.3. The exact source test and page-image receipt are in
  the linked gap analysis. This is a failed-argument comparison, not a
  premise or an accepted solution.
- Alon–Shpilka–Umans: Definition 2.5 and Theorem 2.6, including its proof,
  were read in the primary transcription, pp. 5–6, with the relevant
  definition checked on the p. 5 image. The theorem supplies the word
  formulation comparison, and its colouring step is reused in link 10.
  Naslund–Sawin's arXiv:1606.09575v1, Lemma 6 and the Section 3 proof of
  Theorem 5 were read in the primary transcription. Lemma 6's statement was
  also checked on the p. 2 image; Section 3 was read as text. Link 10 proves
  the bound it uses in full, with one external input
  at source standing: Tao's lemma that a diagonal tensor with nonzero
  diagonal entries has slice rank equal to the size of its support, as
  stated in Naslund and Sawin's Lemma 6. Link 11 uses elementary Fourier
  orthogonality and the proved linear representative lemma from L268;
  no additional external theorem is its premise.
- Petridis, arXiv:1101.3507v3: Theorem 1.1 at $A=B$, $h=4$, supplies
  $|4A|\le K^4|A|$ from $|2A|\le K|A|$. Proposition 2.1 and Theorem 3.1
  were read as primary proof text, without page-image inspection. This
  premise is used only in the doubling corollary of link 9. The fourfold
  version is self-contained given link 8.

## Maximal-rate links: exact successes and a general obstruction

**A canonical chain (author-recorded).** For a family $\mathcal F$ of $m$-sets,
$m\ge2$, let

$$
R_a(\mathcal F)=\max_{0<|T|<m}|\mathcal F_T|^{1/(m-|T|)},
$$

the least rate at which $\mathcal F$ is absolutely spread, and let $T^*$
attain it. The link at $T^*$ has exactly $R_a^{m-|T^*|}$ members and is
absolutely $R_a$-spread: for nonempty $U$ disjoint from $T^*$,
$|\mathcal F_{T^*\cup U}|\le R_a^{m-|T^*|-|U|}$, by the choice of $R_a$ when
$|T^*\cup U|<m$ and trivially otherwise. Hence $R_a$ of the link is at most
$R_a(\mathcal F)$. Iterating gives a chain of links whose rates never increase.
At each step either the current link has $k$ disjoint members, which gives a
$k$-sunflower whose core is the union of the sets $T^*$ chosen so far, or the
chain continues. When a step reaches uniformity $1$, its size is the
preceding selected rate, and its members are distinct singletons. So the
chain ends in a $k$-sunflower unless its rate falls below
$k$. Without $k$ disjoint members, a cover of at most $(k-1)m$ points gives a
point of degree at least $|\mathcal F|/((k-1)m)$. That bounds the loss of
rate per step by the factor $((k-1)m/R)^{1/(m-1)}$, the loss behind the
Erdős–Rado bound.

The
[[research/sunflower_exponential_bound/maximal_rate_links|exact calculation on L214 and L215]]
shows that a whole inner member over the first center of the top block
seed attains $R_a$, and that its link has $\rho$ disjoint members. Hence
for $k\le\rho$ a suitable maximizer succeeds at the first step on these
families. This does not prove that every maximizer succeeds.

The general decay bound is false, even when the maximizing set is unique
at every step before a sunflower-free family is reached. The
[[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|full construction]]
starts with a low-rate sunflower-free family $G$. It forms a new family
by adjoining one new point to every member of $G$, then adding an
intersecting absolutely spread family on a disjoint ground set. The
selected link always returns $G$. The added family nevertheless increases
the size enough that iteration makes the initial exponential rate
arbitrarily large. All visited families have matching number two. One
added part can contain an explicit three-sunflower that the chain misses.

## Remaining obligation

The equivalent assertion SF($k$) is still open. A new core-finding
argument must handle both the selected link and the members it discards,
or use a different invariant. Merely bounding the density loss along a
single maximal-rate chain cannot work. The obstruction uses two
intersecting parts at each stage, so a recursion that retains the other
part remains a possible route, but it needs a bound on the combined
recursion. No such bound is established here.

One precise question is whether the absence of a $k$-sunflower bounds the
total mass of a tree of links, even though the largest individual link can
lose all useful structure. Any proposed weight must accommodate disjoint
unions and coning, as in the chain obstruction, as well as substitution,
as in L214 and L215. The algebraic result in link 8 supplies a uniform
dimension bound for linear words, and its coset partition also handles
subsets of fixed positive density in a linear family. Extending that
argument requires a structural reduction that retains words of the
original family. No such reduction or general alphabet compression is
proved here. One sufficient, unproved extraction statement is the
following: for each fixed $k$, constants $B_k,K_k$ exist such that every
$k$-sunflower-free word family $F$ of length $n$ has a subfamily $F'$ of
at least $|F|/B_k^n$ members, with injective binary vector encodings of
its coordinate alphabets satisfying $|F'+F'|\le K_k|F'|$. Link 9 would
then bound word families with exponential base
$2B_k(k-1)K_k2^{K_k^4}$. The Alon–Shpilka–Umans reduction costs a further
factor $e$ for arbitrary set families, with harmless endpoint slack.
No such extraction theorem is established.
In fact, with no further requirements on $B_k,K_k$ or the extraction,
this statement is equivalent to the target: an exponential bound for
sunflower-free word families permits taking $F'$ to be a singleton,
with $K_k=1$ and $B_k$ at least the bound's base. The proposed extraction
is therefore a reformulation, not a reduction to a known weaker problem.
A useful advance along it would need a structural extraction argument
independent of the desired cardinality bound.
The binary Sidon example
rules out a loss that is always subexponential, or always retains a
fixed positive power of the original cardinality. It does not rule out
the exponential loss that would suffice. Establishing such an extraction
in the sunflower-free case, or using large growth in a different way,
remains unproved.

Link 10 narrows where a counterexample at rate $\rho\ge137$ for $k=3$
can live: an intersecting trace uses more points than its uniformity times
$(\rho-1)^{3/2}/11.65$, with no section certificate in any link. The random
thinnings of substitution powers considered there contain a sunflower with
the explicit high probabilities in Corollary 9. Link 11 proves that random
word families at sufficiently large constant rates have matchings with probability
tending to one. A candidate must have correlations that evade the
recorded section, projection and counting criteria.

The core-allowing Fourier criterion in link 11 supplies a more concrete
inverse question. A sunflower-free family above its size threshold has
nontrivial Fourier bias, in every binary encoding and relative to its
affine span. The guaranteed bias is exponentially small in $n$.
Selecting the larger fiber of one such character can lose almost half
the words and need not fix a coordinate. There is no bound here on the
number or cumulative cost of those restrictions, and the affine
dimension is unrestricted. A useful inverse must retain original words,
control that total cost in terms of $n$, and handle the discarded mass
when necessary. The dichotomy described under the open gap would do
this. It is not established.
