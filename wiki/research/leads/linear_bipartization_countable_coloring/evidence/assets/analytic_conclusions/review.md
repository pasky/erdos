# Adversarial examination of Proposition B and its auxiliary conclusions

## Subject and independence

**Examination date:** 2026-10-16 UTC.

**Subject:** the mathematical extraction of
`wiki/research/leads/linear_bipartization_countable_coloring/_index.md`,
frozen on 2026-10-16: “Target and conventions,” editable proof sketch Steps 1–3,
“Barely superlinear budgets allow chromatic number $\aleph_1$,” Proposition B,
and all five consequence bullets. The [accompanying frozen extraction](../../assets/analytic_conclusions/subject.md)
identifies the actual text examined. It is an extraction of those sections,
not the entire lead page. The project argument is credited to Plasma AI.
Propositions A, C, D, PV, and a full solution of Problem 111 are outside this
examination.

**Role:** independent mathematical reviewer, charged to find a counterexample,
missing hypothesis, unsupported essential inference, or canonical failure mode.
The disclosed reviewer model is GPT-6 Astra.
The reviewer neither authored nor collaborated on the subject and had not
previously built on it. The examination used a fresh context, the frozen
extraction, its source manifest, the two supplied source transcriptions, and
the two specifically permitted primary PDFs. The required operating guidance
was also read. No author memory, prior review, source card, live claim ledger,
original lead page, unrelated research, inbox, or network source was read.
The subscription table was empty at both checked examination boundaries.
The frozen subject was not modified.

The commission itself included motivational assertions about unrelated AI
mathematical achievements. They were received with the assignment, were not
verified, and were used neither as mathematical premises nor as reasons to
agree. Their presence was disclosed for a separate grader's materiality ruling.
No ruling on that exposure is asserted here. No other excluded communication
or search exposure is known.

**Actual mathematical reading:** the frozen subject and manifest in full;
Lambie-Hanson's supplied transcription in full, with the dependency examination
concentrated on Sections 1–5; the Erdős excerpt in full. Lambie-Hanson's primary PDF pages
1–9 were visually checked at 300 dpi, including the definitions, Section 4
construction, Claim 4.1, its chromatic argument, and Section 5. The closing
sentence of the Section 5 proof on page 10 was read in the transcription; the
contradictory coloring equality itself was checked on page 9. In the Erdős PDF,
the relevant Part VII paragraph on page 16 was visually checked at 300 dpi;
bibliography pages 17 and 19 were seen while locating it. Adjacent material in
these page images supplied no premise.

This is a noncomputational examination. Its independent reasoning, including
the exact counterexample to the signed-budget reading, is retained below.
There is no mathematical program, finite search, cached success result, or
computer-generated certificate on which a verdict depends. Reconstruction
requires the frozen subject, the source interfaces identified below, and the
arguments in this report. Routine PDF rendering is source inspection, not a
mathematical verification leg.

## Conclusions of the examination

| Surface | Mathematical verdict |
| --- | --- |
| Definitions, countable deletion, packing, and the conditional equivalence in Steps 1–3 | **refutation-failed** within the stated chromatic-number scope. Lemma CC itself is not proved or accepted as a premise. |
| Proposition B, including the ZFC cardinality and the diamond Hajnal–Máté clause | **refutation-failed**, relying on the identified published source interfaces. |
| First consequence: the strict upper bound and the simultaneous bounds for every positive exponent | **refutation-failed**. The constants in the simultaneous asymptotic bounds may depend on the exponent. |
| Second consequence: no uniform rate | **refutation-failed**, with its eventual quantifier and its conditional statement about a positive answer to Problem 111 preserved. |
| Third consequence: “any integer-valued” budget tending to infinity | **refuted-as-stated on the literal signed-integer reading**: $g(n)=n-2$ is an exact witness. Under the nonnegative, natural-valued convention introduced in Proposition B, the narrower claim is **refutation-failed**. The distinction is substantive for an all-order hypothesis. |
| Fourth consequence: blow-ups and the hypothetical obligatory-blow-up route | **refutation-failed**, with the base graph fixed while its blow-up factor grows. |
| Fifth consequence: each finite label tail has chromatic number $\aleph_1$ | **refutation-failed**. No conclusion about an intersection of all tails is included. |

Thus the principal mathematical construction survives these attacks. A blanket
favorable verdict on every standalone consequence requires deciding whether the
third bullet inherits $g:\mathbb N\to\mathbb N$ or quantifies over
$\mathbb Z$-valued functions. This report does not silently make that decision
by changing the frozen wording. No grade or claim tier is asserted.

## Restatement and conventions

Write $\mathbb N_0=\{0,1,2,\ldots\}$; positive orders are $n\geq1$.
Lambie-Hanson explicitly includes zero among the natural numbers. Graphs are
simple undirected set-sized graphs. Subgraphs need not be induced.
For finite $F$, $\beta(F)$ is the minimum number of edges removed to obtain
a bipartite graph. For infinite $G$,

$$
 h_G(n)=\max\{\beta(F):F\subseteq G,\ |V(F)|=n\}.
$$

The use of $h_G$ is restricted to infinite graphs, as in its definition.
The finite graphs allowed in the statement of CC already have countable
chromatic number and require no extension of $h_G$ beyond that domain.

The principal statement is: for each nondecreasing unbounded
$g:\mathbb N_0\to\mathbb N_0$, there exists one graph $G_g$ such that

$$
 |V(G_g)|=2^{\aleph_1},\qquad \chi(G_g)=\aleph_1,\qquad
 \forall n\geq1,\quad h_{G_g}(n)\leq(n-1)g(n).
$$

The graph may depend on the entire function $g$, but not on $n$.
Under $\diamondsuit$, there is instead such a graph with vertex set of
cardinality $\aleph_1$, order-isomorphic to a graph on $\omega_1$ whose
lower neighbors at each vertex are finite or form an increasing sequence
cofinal in that vertex. This is the source's Hajnal–Máté convention.

The five bullets additionally assert, respectively: an all-order strict power
upper bound and a single graph with all positive-exponent asymptotic bounds;
an eventual upper bound below every prescribed divergent rate; failure of the
countable-coloring conclusion for every divergent budget in the asserted
integer-valued class; exclusion of arbitrarily large blow-ups of each fixed
finite non-bipartite graph from one example; and uncountable chromatic number
at every finite label cutoff. Their precise quantifiers and limitations are
examined separately below.

## Premises and source fidelity

The dependency census was made from the frozen statement and proof, including
the consequence sentences, on 2026-10-16 UTC. No native L-claim is consumed as
an established premise. No live ledger reading was authorized or needed for
that empty census. CC is the antecedent of an implication being examined, not
an imported theorem. All local supporting graph arguments are rederived here.
The reasoning order is acyclic: definitions and deletion/packing first;
the conditional CC equivalence second; the external labelled construction and
its checked interface next; Proposition B; then its five consequences. The
hypothetical blow-up route also uses the CC equivalence.

### Lambie-Hanson

The identified edition is Chris Lambie-Hanson, *On the growth rate of chromatic
numbers of finite subgraphs*, [arXiv:1902.08177v2](https://arxiv.org/abs/1902.08177v2),
with manuscript date February 26, 2019. The arXiv version identifier and
manuscript date are visible on its first page; the version margin says
February 25. This date distinction does not change the identified edition.
The canonical source paths supplied with the examination are

- `library/graph_coloring/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs.pdf`;
- `library/graph_coloring/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs.md`.

The following are the consumed interfaces, not a claim to have independently
reconstructed all original literature proofs.

| Source locator | Exact interface and specialization | Reading and reliance |
| --- | --- | --- |
| Section 1.1 and Definitions 2.1–2.3, pp. 2–3 | Natural numbers include zero; finite increasing ladder blocks have merge types; $t_s^d=0^s(01)^{d-s}1^s$; the Specker graph on $d$-subsets joins disjoint sets with this type in either orientation. | Definitions and their use checked against print, with the index slips disclosed below. |
| Theorem 2.4(2), p. 4 | For an ordinal $\alpha$, $1\leq s\leq d-1$, and $d\geq2s^2+1$, the Specker graph $G(\alpha,t_s^d)$ has no odd cycle of length at most $2s+1$. Used for $\alpha=\omega_2$ and $\omega_1$. | Exact statement checked; relied on as a published external result. The original Erdős–Hajnal proof cited there was not read. Part (1), about its chromatic number, is not needed. |
| Propositions 2.6–2.8, p. 4 | Finite products of colorings color unions; an odd closed walk contains a no-longer odd cycle; homomorphisms therefore preserve exclusion of short odd cycles. | Statements and proofs checked; the required arguments are also given below. |
| Definition 3.1 and Theorem 3.2, pp. 4–5 | Club-guessing ladders exist on $S^\lambda_\kappa$ when $\kappa,\lambda$ are regular and $\kappa^+<\lambda$. Used with $\kappa=\omega,\lambda=\omega_2$. | Statement checked; ordinary reliance on the theorem stated in this source. The original Shelah proof was not read. This ZFC theorem is not applied at $\omega_1$. |
| Proposition 3.3, p. 5 | A partition of a club-guessing domain into fewer than $\lambda$ parts has a part on which the ladders still guess clubs. | Statement and proof read; the countable-partition argument is justified below. |
| Lemma 3.4, pp. 5–6 | For uncountable regular $\lambda$, on a stationary club-guessing subset of $S^\lambda_\omega$, any prescribed finite disjoint type is realized by initial ladder segments at some $\alpha<\beta$. Used with a finite concatenation of the types for labels $0,\ldots,k$. | Exact statement and application checked; proof read, but no independent full reconstruction of the elementary-submodel argument is asserted. It is a published external premise. |
| Section 4, pp. 6–8; Claim 4.1, p. 7 | For each input $f:\mathbb N_0\to\mathbb N_0$, the constructed graph has size $2^{\aleph_1}$, chromatic number exactly $\aleph_1$, forest label classes, and a label-$\geq k$ tail with no odd cycle of length $\leq f(k)$, simultaneously for all $k$. | Construction and chromatic proof inspected, and this full interface rederived below from the identified premises. The displayed finite-chromatic-growth theorem alone would be insufficient. |
| Definitions 5.1–5.2, p. 8; Section 5, p. 9 | Diamond supplies a joint ladder/color prediction sequence; the ordinal-vertex construction has size and chromatic number $\aleph_1$, the Hajnal–Máté property, and the same two label properties. | Definitions, construction and chromatic argument checked. The omitted analogue of Claim 4.1 is filled in below; it is not inferred solely from the theorem's title. |

There are printed index slips. Definition 2.1(2) on page 3 has $t(n)$
where the varying merge position is $i$; the surrounding word description
and example identify the intended merge type. The proof of Proposition 2.6
on page 4 has $h(k)$ where its coordinate is $j<k$. These slips are
also in the supplied transcription. This examination defines a merge type
directly by membership in the increasing union and defines product colorings
coordinatewise; it does not rely on those literally erroneous formulas.

There are also differences between print and the frozen transcription inside
the proof of Lemma 3.4. On page 5, the initial segment next to the newly chosen
$\beta$ is printed with subscript $\gamma$, whereas the transcription
uses $\delta$. On page 6, two bounds in the recursive choice are printed
with $C_\gamma$, whereas the transcription uses $C_\delta$. This report
records those as source/transcription differences, not as an author-issued
erratum. They do not change the lemma's checked statement, and the review
consumes that statement as a published premise rather than claiming an
independent certification of every line of its printed proof. No transcription
or source file was changed.

### Erdős

The other identified source is Paul Erdős, *Combinatorial problems which I
would most like to see solved* (1981), Part VII, final paragraph, page 16 of
the supplied PDF. Its canonical source paths are

- `library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/erdos_1981_combinatorial_problems_which_i_would_most.pdf`;
- `library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/erdos_1981_combinatorial_problems_which_i_would_most.md`.

The paragraph really asks the finite-density question for graphs with
chromatic number at least $\aleph_1$, and then proposes the strict upper
bound for a graph of chromatic number exactly $\aleph_1$, for each
positive $\varepsilon$. The excerpt preserves both distinctions. The native
Steps 1–3 concern the exactly-$\aleph_1$ scope and verify the corresponding
restriction of the finite-density formulation. They do not establish a
reduction for arbitrary larger chromatic numbers. The sentence identifying the
finite-density *form* is supported; it must not be read as an unproved
identification of these two entire graph classes.

This source is used to check the characterization of the 1981 question and
upper-bound belief, not as a theorem or as evidence that the present argument
solves Problem 111. No current catalog or broader literature-status claim was
examined.

## The local prerequisites

### Restatement

For a graph with $\chi(G)=\aleph_1$, deleting countably many vertices leaves
chromatic number $\aleph_1$. Infinitely many vertex-disjoint copies of one
finite graph with $v$ vertices and $\beta=b>2Kv$, where $K>0$, imply
$h_G(n)>Kn$ for every $n\geq2v$. An uncountable disjoint family of finite
violators contains infinitely many copies of one such finite type.

CC asserts that every graph with $\chi\leq\aleph_1$ satisfying
$\beta(F)\leq C|V(F)|$ on every finite subgraph, for a fixed $C\geq0$,
is countably colorable. The reviewed assertion is the equivalence of CC with
the positive limit statement, together with the countable-deletion remainder
when $h_G(n)\leq Kn$ at infinitely many orders.

### Weakest steps and derivation

First, if $F\subseteq H$, the intersection with $E(F)$ of any bipartizing
edge set for $H$ bipartizes $F$. This proves monotonicity. For infinite
$G$, the set defining $h_G(n)$ is nonempty and consists of integers in
$[0,\binom n2]$; its maximum therefore exists and is attained. Adding
vertices and taking an induced supergraph cannot reduce the lower bound
obtained from any chosen subgraphs.

Second, a countable coloring of $G-S$ extends to $G$ using a disjoint
countable palette of distinct colors for $S$. Edges between the two parts
then cause no conflict. Thus $G-S$ is not countably colorable, while a
coloring of $G$ restricts to it. Its chromatic number is exactly
$\aleph_1$, regardless of $|V(G)|$.

For the packing assertion, choose $q=\lfloor n/v\rfloor$ disjoint copies
and pad their union to $n$ vertices. A bipartizing set must contain at least
$b$ edges of each copy, and those edge sets are disjoint. Cross-edges cannot
undo these restrictions. Consequently

$$
 h_G(n)\geq qb\geq \frac b v(n-v)
       >2K(n-v)\geq Kn\qquad(n\geq2v).
$$

The strict inequality uses $n-v>0$. Countably many finite isomorphism types
cannot partition an uncountable family into countable parts. The repeated
type has exactly the same $v$ and $\beta=b$, so this is a justified
passage to a fixed witness, not a uniform-size assumption.

Third, assume CC. For each fixed $K>0$, choose a finite $2K$-linear
violator after each countable stage of a recursion of length $\omega_1$.
The already used vertices at stage $\xi<\omega_1$ are countable. Deletion
preserves chromatic number $\aleph_1$, and CC supplies the next violator
by contraposition. A well-order of the finite subgraphs makes the choices
within ordinary ZFC transfinite recursion. Packing yields an eventual bound
$h_G(n)>Kn$. Its threshold may depend on $G,K$, which is exactly what
the limit requires.

Conversely, failure of divergence to infinity gives a finite $K>0$ and
unboundedly many orders with $h_G(n)\leq Kn$. By Zorn's lemma, take a
maximal vertex-disjoint family of finite graphs with
$\beta(F)>2K|V(F)|$. Uncountability of that family contradicts the packing
bound on those unboundedly many orders. Its vertex union is countable, and
maximality makes its complement $2K$-linear. The complement still has
chromatic number $\aleph_1$. A $C$-linear graph of that chromatic number
also directly prevents divergence. These are both directions of the claimed
equivalence. If the “moreover” hypothesis is allowed $K<0$, it is impossible;
if $K=0$, padding any odd cycle contradicts it, so the graph would be
bipartite and the hypothesis is again impossible for $\chi(G)=\aleph_1$.

### Strongest attack, dependencies, and verdict

The principal attempted failure was loss of uniformity: witness sizes can
grow without bound, and adding edges between witnesses might invalidate
additivity. The restriction of a bipartizing set to each disjoint copy gives
the needed inequality even with arbitrary cross-edges; the uncountable
family and countability of finite types produce a fixed size only after the
recursion. No uniform bound on all chosen witnesses is needed.

A single finite witness alone is insufficient: a disjoint union of that
finite graph and infinitely many isolated vertices has bounded $h_G(n)$
for large $n$. This example illustrates why the proof needs disjoint
replication; it is not offered as an instance of Problem 111.

Dependencies are the definitions, elementary coloring arguments, countable
unions of finite sets, and ZFC choice/maximality. The Erdős characterization
has the scope qualification stated above. The local mathematical verdict is
**refutation-failed**. This verdict concerns the equivalence, not the truth
of its unresolved CC antecedent.

## Proposition B: the source construction and the deletion bound

### Weakest step 1: the source properties must hold on one correctly sized graph

Fix any $f:\mathbb N_0\to\mathbb N_0$. Choose

$$
 s_k=\min\{s\geq1:2s+1\geq f(k)\},\qquad d_k=2s_k^2+1,
$$

and consecutive disjoint index intervals $I_k$ of lengths $d_k$.
These are valid Specker parameters: $1\leq s_k\leq d_k-1$.
Let $S=S^{\omega_2}_\omega$ and take the club-guessing sequence supplied
by Theorem 3.2. Its stationary-set hypothesis holds: inside any club choose
a strictly increasing sequence of length $\omega$; its supremum remains
below the regular cardinal $\omega_2$, belongs to the club, and has
cofinality $\omega$. The vertices at rank $\beta\in S$ are all functions
$\tau:S\cap\beta\to\mathbb N_0$. The domains distinguish the ranks:
if $\alpha<\beta$ belong to $S$, then $\alpha$ belongs to $S\cap\beta$
but not to $S\cap\alpha$.

Each domain has size at most $\aleph_1$, and some have size exactly
$\aleph_1$, for example at $\beta=\omega_1+\omega$. Thus the vertex
union $\Sigma$ satisfies

$$
 2^{\aleph_1}=\aleph_0^{\aleph_1}
 \leq |\Sigma|
 \leq \aleph_2\cdot\aleph_0^{\aleph_1}
 =2^{\aleph_1}.
$$

Here $\aleph_0^{\aleph_1}=2^{\aleph_1}$ follows by bounding $\aleph_0$
between $2$ and $2^{\aleph_0}$; and $2^{\aleph_1}\geq\aleph_2$ is
Cantor's inequality. No continuum hypothesis or prescribed value of
$2^{\aleph_1}$ is used.

For a rank-$\beta$ vertex $\tau$ and label $k$, the construction
chooses the least eligible $\alpha\in S\cap\beta$, if one exists, with
$\tau(\alpha)=k$ and the required disjoint types in every block
$I_j,\ j\leq k$. It adds the edge from $\tau$ to its restriction at
$\alpha$. Therefore every edge joins different ranks, every vertex has
at most one lower neighbor per label, and it has at most countably many lower
neighbors in total. Coloring by rank, each vertex avoids only countably many
previously used colors; a color below $\omega_1$ remains available.
Vertices of one rank are nonadjacent. Hence $\chi(G)\leq\aleph_1$.

To check the lower bound, suppose $c:\Sigma\to\mathbb N_0$ is proper and
define recursively

$$
 \rho(\alpha)=c(\rho\restriction(S\cap\alpha)).
$$

Some color class $S_k=\{\alpha:\rho(\alpha)=k\}$ retains club guessing.
For completeness, if each color class failed, choose a club $D_k$ whose
guessers in that class are nonstationary, and intersect it with a club
avoiding those guessers. No ladder indexed in that class is contained in
the resulting club: containment would put its supremum there too. The
intersection over all $k$ is still club, contradicting the original
club-guessing property. This proves the specialization of Proposition 3.3
actually used.

Apply Lemma 3.4 to the concatenation of the types for $I_0,\ldots,I_k$.
Each concatenated block has exactly $d_j$ entries of each kind, so its
realization gives the required type on each individual interval. It supplies
$\alpha^*<\beta^*$ in $S_k$ witnessing eligibility at label $k$ for
the vertex $\rho\restriction(S\cap\beta^*)$. The least eligible neighbor
may differ from $\alpha^*$, but its eligibility still forces
$\rho(\alpha)=k$. Both endpoints therefore have color $k$, a
contradiction. This point prevents an erroneous reliance on the particular
witness being the one selected. Hence $\chi(G)=\aleph_1$.

### Weakest step 2: forests and tail odd girth give an edge bound, not just a coloring bound

A finite cycle in the label-$k$ graph has a vertex of greatest rank. Its
two distinct cycle neighbors have smaller rank and the same label, contrary
to the one-lower-neighbor property. Thus each label class is a forest. The
rank hypothesis matters: an arbitrary orientation with outdegree one could
contain a directed cycle.

For a tail edge with label at least $k$, its endpoints have disjoint
$I_k$-blocks of type $t_{s_k}^{d_k}$. The map

$$
 \sigma\longmapsto C_{\alpha_\sigma}[I_k]
$$

is therefore a graph homomorphism into the specified Specker graph. Its
images on adjacent vertices are distinct, because the blocks are nonempty
and disjoint. An odd cycle could map to a closed walk with repeated vertices,
but cutting at a repetition leaves a shorter odd closed walk. Repetition of
this finite descent yields an odd cycle of no greater length. Consequently
the Specker odd-girth bound gives the exact tail bound $\leq f(k)$, even
without injectivity of the homomorphism.

Now let $g$ have Proposition B's stated domain and hypotheses. For each
$k$, monotonicity and unboundedness of $g$ make

$$
 f(k)=\max\bigl(\{0\}\cup\{m\geq1:g(m)\leq k\}\bigr)
$$

finite. For every positive $n$, the set defining $f(g(n))$ contains
$n$. Thus $n\leq f(g(n))$, with no inverse-function assumption and
no strict-monotonicity requirement.

Fix an arbitrary $n$-vertex subgraph $F$, set $k=g(n)$, and retain
its tail edges. Any odd cycle there would have length at most $n$, which
the tail exclusion forbids. The retained graph is bipartite: in each
component, parity of finite paths from a chosen root defines a two-coloring;
inconsistent parities would give an odd closed walk and hence an odd cycle.
Each discarded label class, restricted to $V(F)$, is a forest with at
most $n-1$ edges. One can count them directly: charge each edge to its
higher-rank endpoint; each vertex is charged at most once, and a vertex of
minimum rank is charged zero times. Summing over the $k$ labels below $k$ proves

$$
 \beta(F)\leq\sum_{j<k}|E(F)\cap E_j|\leq k(n-1).
$$

This applies to every $F$ and every $n$ in one graph. For $k=0$, no
edges are discarded. For $n=1$, both sides are zero. Arbitrarily long
finite plateaus of $g$ do not affect the argument.

### Weakest step 3: the diamond construction really has the same interface

Section 5 supplies, under diamond, ladders $C_\alpha$ and predictions
$p_\alpha:S\cap\alpha\to\mathbb N_0$ on
$S=S^{\omega_1}_\omega$ such that every global coloring is predicted
correctly on stationarily many indices whose ladders also guess any given
club. The direction from diamond needed here follows by fixing coding maps
for a pair consisting of a subset of $\omega_1$ and the graph of a
coloring. Decode the diamond guess at each $\alpha\in S$. If it yields
a cofinal set $D_\alpha\subseteq\alpha$ and a function on $S\cap\alpha$,
take that function as $p_\alpha$ and choose an $\omega$-sequence
$C_\alpha$ cofinal in $D_\alpha$. Otherwise use fixed default choices.
These choices depend only on the local guess, not on knowledge of whether it
is correct. For any given global club $D$ and coloring $c$, intersect
the stationary set of correct guesses with the club of ordinals closed
under the coding maps and the club of limit points of $D$. At these
indices the decoded pair is exactly $(D\cap\alpha,c\restriction(S\cap\alpha))$,
so the chosen ladder is contained in $D$ and the prediction is correct.
This gives the joint property used by the source. It does not invoke the ZFC
club-guessing theorem at the forbidden no-gap parameters.

Vertices are now the ordinals in $S$. At $\beta$, one least eligible
$\alpha<\beta$ per label is selected, with $p_\beta(\alpha)=k$ and the
same block requirements. A finite cycle again has an ordinal maximum, so
its fixed-label graph is a forest. The tail homomorphism is now
$\alpha\mapsto C_\alpha[I_k]$ into the Specker graph on $\omega_1$.
The entire preceding deletion argument therefore transfers, not merely a
bound on the finite chromatic number.

The Hajnal–Máté condition also follows from the actual parameters. Since
$d_k-s_k\geq2$, the last zero in $t_{s_k}^{d_k}$ occurs after its first
one. If the label-$k$ neighbor $\alpha_k^\beta$ is selected, then

$$
 \alpha_k^\beta>
 \max C_{\alpha_k^\beta}[I_k]>
 \min C_\beta[I_k]>
 C_\beta(\max I_{k-1})\qquad(k\geq1).
$$

For every $\gamma<\beta$, only finitely many labels can produce a
neighbor at most $\gamma$. Hence an infinite lower-neighbor set has order
type $\omega$ and is cofinal in $\beta$, even though the selection
order of the neighbors need not be increasing. The order isomorphism from
$S$ onto $\omega_1$ preserves this condition: cofinality of a subset
below $\beta$ gives cofinality of its image below the image of $\beta$.
The vertex set has cardinality $\aleph_1$.

For a purported proper countable coloring $c$, restrict to indices where
$p_\alpha=c\restriction(S\cap\alpha)$. Their ladders retain club
guessing. A color class retains it too, and Lemma 3.4 again supplies an
eligible label-$k$ neighbor at a correctly predicting vertex $\beta^*$
with $c(\beta^*)=k$. The selected neighbor $\alpha$, whether or not it
is itself a correctly predicting index, satisfies
$c(\alpha)=p_{\beta^*}(\alpha)=k$. This contradicts propriety. Together
with the cardinality upper bound, it proves $\chi(G)=\aleph_1$.

### Strongest attacks, dependencies, and verdict

The most consequential attempted refutation was that the source's displayed
theorem supplies only finite chromatic bounds, which do not by themselves
bound the number of edges needing deletion. The actual construction supplies
the stronger simultaneous labelled interface on the same graph, and the
forest count proves the required deletion estimate. This attack fails for
the frozen proof because it explicitly invokes Claim 4.1.

Further attacks checked a collapsed homomorphic odd cycle, equal-rank
neighbors, a selected neighbor different from the chromatic proof's witness,
zero labels, the first vertex order, long plateaus, a hidden continuum
hypothesis, and the transfer of the Hajnal–Máté ordering. The derivations
above address each at its exact use. The graph cardinality is exact, not
merely an upper bound. The diamond hypothesis remains explicit.

The external premises and their limits are those listed in the source table;
the other steps are rederived here. The verdict for both clauses of
Proposition B is **refutation-failed** under that ordinary external-theorem
reliance. This is not a reconstruction of all original proofs behind the
Specker, club-guessing, or type-realization results.

## First consequence: the strict upper bound

### Restatement, weakest step, and derivation

For each real $\varepsilon>0$, a graph of chromatic number exactly
$\aleph_1$ has $h_G(m)<m^{1+\varepsilon}$ at every positive integer
$m$. Its cardinality can be $2^{\aleph_1}$ in ZFC and $\aleph_1$
under diamond. There is also one such graph with
$h_G(n)=O_\varepsilon(n^{1+\varepsilon})$ for every positive
$\varepsilon$, with the graph independent of $\varepsilon$.

The weakest endpoint is strictness when $m^\varepsilon$ is an integer,
and especially $m=1$. The choice $g(m)=\lfloor m^\varepsilon\rfloor$
is natural-valued, nondecreasing, and unbounded. Proposition B gives

$$
 h_G(m)\leq(m-1)\lfloor m^\varepsilon\rfloor
 \leq(m-1)m^\varepsilon<m^{1+\varepsilon}
 \qquad(m\geq1).
$$

Strictness comes from $m-1<m$, not from rounding. At $m=1$, it reads
$0<1$.

For $g(n)=\lceil\log_2(n+1)\rceil$, the same graph works for every
exponent. For example,

$$
 g(n)\leq 2+\frac{\ln n}{\ln2}
 \leq \left(2+\frac1{e\varepsilon\ln2}\right)n^\varepsilon
 \qquad(n\geq1),
$$

where the second inequality follows by maximizing
$t e^{-\varepsilon t}$ for $t\geq0$. Thus the implicit constant may
depend on $\varepsilon$. A constant uniform as $\varepsilon\downarrow0$
is not asserted or supplied.

### Strongest attack, premises, and verdict

The attacks were an all-order failure at the first order, equality at an
integer power, an exchanged graph/exponent quantifier, and an implicit
uniform constant. The displayed estimates settle the first three and expose
the permitted dependence in the fourth. The primary Erdős paragraph confirms
the strict inequality and the exactly-$\aleph_1$ chromatic requirement.
It puts no $\aleph_1$ bound on the vertex set.

Dependencies are Proposition B and elementary estimates just shown; the
historical characterization uses the checked Erdős paragraph. The verdict
is **refutation-failed**. The argument establishes upper bounds only. The
sentence saying that it does not answer the limit or unboundedness question
is retained as a limitation of this deduction, not as a claim of
independence in set theory or a survey of all current knowledge about these
graphs. This review asserts neither divergence nor boundedness of their
bipartization ratio.

## Second consequence: no uniform rate

### Restatement, weakest step, and derivation

For each real-valued sequence $r(n)\to+\infty$, there is a graph
with chromatic number $\aleph_1$ such that $h_G(n)<n r(n)$ for every
sufficiently large $n$. If all such graphs in fact have divergent
$h_G(n)/n$, no divergent eventual lower rate can hold for all of them.

The weakest step is existence and usefulness of a minimum over an infinite
tail when $r$ need not be monotone. Define

$$
 a(n)=\min_{m\geq n}\lfloor r(m)\rfloor,
 \qquad g(n)=\max(1,a(n)).
$$

Every tail of the integer sequence is bounded below: its sufficiently late
terms are positive, and only finitely many earlier terms remain. A nonempty
bounded-below set of integers has a minimum. Removing initial terms cannot
lower that minimum, so $g$ is nondecreasing. For every integer $M$,
eventually all terms of the tail have floor at least $M$; hence
$g(n)\to+\infty$.

For all sufficiently large $n$, $a(n)\geq1$ and
$1\leq g(n)\leq\lfloor r(n)\rfloor\leq r(n)$. Applying Proposition B,

$$
 h_G(n)\leq(n-1)g(n)<n g(n)\leq n r(n).
$$

No claim is made at early indices with $r(n)\leq0$. The graph depends on
$r$, and its eventual threshold may depend on $r$ as well.

### Strongest attack, premises, and verdict

An oscillating rate could have defeated a naïve pointwise floor or a
nonexistent tail minimum. Convergence to infinity, as opposed to mere
unboundedness, supplies both the lower boundedness and divergence of the
minorant. If a common divergent eventual lower rate $R$ existed for all
graphs, applying the result with $r=R$ would contradict it in the selected
graph. The conditional phrasing does not assert that the graphs' ratios
actually diverge.

The conclusion also rules out a common rate up to graph-dependent positive
multiplicative constants. Given any proposed divergent rate $R$, apply the
construction with $r(n)=\sqrt{\max(1,R(n))}$. The resulting graph satisfies
$h_G(n)/(nR(n))\to0$, so its ratio cannot eventually dominate any positive
constant multiple of $R$. This is a consequence of the all-rates quantifier,
not a claim of a uniform threshold across graphs.

Dependencies are Proposition B and the tail argument above. The verdict is
**refutation-failed**. In particular, the early-sign issue that defeats the
literal next bullet does not defeat this eventually quantified statement.

## Third consequence: sharpness at the linear scale

### Restatement and range distinction

The bullet states that, for any integer-valued $g(n)\to+\infty$, replacing
$C|V(F)|$ in CC by $|V(F)|g(|V(F)|)$ makes the lemma false. On its
standalone signed-integer reading, this means that every such
$g:\mathbb N_0\to\mathbb Z$ admits a graph $G$ with
$\chi(G)=\aleph_1$ and

$$
 \forall F\subseteq G\text{ finite},\qquad
 \beta(F)\leq |V(F)|g(|V(F)|).
$$

On the narrower reading inherited from Proposition B, the codomain is
$\mathbb N_0$, and only monotonicity of $g$ is relaxed.

### Strongest attack: an exact witness against the signed-integer quantifier

Take

$$
 g(n)=n-2.
$$

It is integer-valued, nondecreasing, and tends to infinity. Every nonempty
simple graph has a one-vertex subgraph $F$, for which

$$
 \beta(F)=0>-1=|V(F)|g(|V(F)|).
$$

Consequently no nonempty graph satisfies the modified all-order hypothesis.
The empty graph, if admitted, is countably colorable. The modified lemma is
therefore true for this $g$, rather than false. This disproves the
standalone universal signed-integer assertion; it is not merely a failure
of the proposed proof. Its proposed minorant equals $g$ and does not
have Proposition B's nonnegative codomain.

This is a boundary defect in an all-order universal claim. Discarding a
finite initial segment or replacing negative values by zero changes the
hypothesis being asserted; neither change has been made to the subject here.

### Weakest step and derivation for the nonnegative reading

If $g:\mathbb N_0\to\mathbb N_0$ and $g(n)\to+\infty$, then

$$
 u(n)=\min_{m\geq n}g(m)
$$

exists, is nonnegative and nondecreasing, tends to infinity, and is at most
$g(n)$. Proposition B supplies a graph of chromatic number $\aleph_1$
with

$$
 \beta(F)\leq (n-1)u(n)\leq n g(n),\qquad n=|V(F)|\geq1.
$$

The empty finite subgraph satisfies its zero bound too. Initial zeros and
nonmonotone positive terms cause no failure. This proves precisely the
nonnegative version and explains the intended linear-scale contrast.

The weaker “subquadratic” and “$n^{1+o(1)}$” hypotheses alone do not
force countable colorability. The logarithmic-budget graph already has
$h_G(n)\leq n\lceil\log_2(n+1)\rceil=o(n^2)$. Even if
$n^{1+o(1)}$ is read as equality of exponents rather than only an upper
bound, the conclusion follows. After any countable deletion the graph still
has chromatic number $\aleph_1$, so it is not bipartite and contains a
finite odd cycle. Recursion gives uncountably many disjoint odd cycles, and
some fixed odd length $\ell$ repeats infinitely. Packing those cycles,
whose bipartization number is one, gives

$$
 h_G(n)\geq\lfloor n/\ell\rfloor\geq n/(2\ell)
 \qquad(n\geq2\ell).
$$

The lower and logarithmic upper bounds imply
$\log h_G(n)/\log n\to1$. The phrase that a proof “must use” linearity
is justified in this mathematical sense: replacing linearity by either of
those two weaker growth hypotheses cannot establish the same coloring
conclusion. It does not impose a syntactic requirement on every possible
future proof of CC.

### Premises and verdict

The counterexample to the signed reading uses only the one-vertex definition
of $\beta$. The nonnegative reading uses Proposition B, while the
$n^{1+o(1)}$ example also uses countable deletion and packing. The literal
signed-integer assertion is **refuted-as-stated**. If the original
$g:\mathbb N\to\mathbb N$ convention is determined to govern this bullet,
that narrower assertion and its two growth examples are
**refutation-failed**. This report preserves both readings for adjudication
rather than relabelling a changed statement as the frozen one.

## Fourth consequence: blow-ups

### Restatement and weakest steps

For a finite non-bipartite graph $H$ and positive integer $s$, replace
each vertex by an independent class of $s$ vertices and every edge by a
complete bipartite graph between the corresponding classes. The asserted
lower bound is $\beta(H[s])\geq s^2$. A single logarithmic-budget graph
of chromatic number $\aleph_1$ contains $H[s]$ for only finitely many
positive $s$, for each fixed finite non-bipartite $H$. The upper
threshold may depend on $H$.

Choose an odd cycle $C_\ell\subseteq H$. Its transversal cycles in
$C_\ell[s]$ are indexed by one choice from each of the $\ell$ classes,
so there are $s^\ell$ of them. Each edge of $C_\ell[s]$ belongs to
exactly $s^{\ell-2}$ such cycles. A bipartizing set $D$ must meet every
one, and hence

$$
 s^\ell\leq
 \sum_{e\in D\cap E(C_\ell[s])}s^{\ell-2}
 \leq |D|s^{\ell-2}.
$$

This proves the bound, including $s=1$. Edges of $H[s]$ outside this
cycle blow-up lie in zero of these selected cycles; the claimed uniform
incidence count is used only on $C_\ell[s]$, exactly where it is valid.

For $v=|V(H)|$, an embedding of $H[s]$ into the logarithmic-budget
example would give, with $n=sv$,

$$
 s^2\leq\beta(H[s])\leq h_G(sv)
 \leq(sv-1)g(sv)\leq sv\,g(sv).
$$

Thus $s\leq v g(sv)$ is necessary. But
$v\lceil\log_2(sv+1)\rceil/s\to0$ for each fixed $v$.
It fails for every sufficiently large $s$. This is a statement about
subgraph embeddings, so extra ambient edges and inducedness cannot invalidate
it. The same graph works for all finite non-bipartite $H$; only the
exclusion threshold depends on $H$.

### Strongest attack: audit the $s^2$ bound by a different argument

A possible failure was overcounting transversal cycles or treating fractional
weights as an integral deletion set. There is a separate cut argument that
checks the bound in its actual units. For any two-coloring of $C_\ell[s]$,
let $x_i\in[0,1]$ be the fraction of vertices of class $i$ receiving
the first color. Its number of monochromatic edges is

$$
 s^2\sum_{i\bmod\ell}
 \bigl(x_i x_{i+1}+(1-x_i)(1-x_{i+1})\bigr).
$$

The sum is affine in each coordinate separately. Moving each coordinate to
an endpoint that minimizes the current value cannot increase it, so its
minimum on the cube is attained at a vertex of the cube. Such a vertex is
a two-coloring of an odd cycle and has at least one monochromatic base edge.
The displayed sum is therefore at least one for every choice of the
fractions. A bipartizing deletion set must include all monochromatic edges
of a bipartition of its remainder, so its size is at least $s^2$.
This independently confirms the lower bound; no statistical heuristic is
being substituted for a proof.

### The conditional obligatory-blow-up sentence

A sufficient precise formulation of the hypothetical premise is: every graph
$J$ with $\chi(J)=\aleph_1$ contains $H_J[s]$ for arbitrarily large
$s$, for some fixed finite non-bipartite $H_J$. The base graph may
depend on $J$; it must not change with $s$ in this statement.
For any $C$, choosing $s>C|V(H_J)|$ violates $C$-linearity.
Consequently this hypothetical premise implies CC and then the limit through
Steps 1–3, applying the premise anew to every countable-deletion remainder.
The conventional stronger assertion that a fixed non-bipartite $H$ and all
its blow-ups are obligatory also suffices. A premise that merely allowed
$|V(H)|$ to grow arbitrarily with $s$ would not supply this inference.

Dependencies are Proposition B for the logarithmic graph, the finite-cycle
argument, and Steps 1–3 for the hypothetical route. The verdict is
**refutation-failed** under these fixed-base quantifiers. This conditional
route is not claimed to occur, and the example disproves its obligatory
premise.

## Fifth consequence: each finite label tail

### Restatement, weakest step, and derivation

For the constructed graph and each fixed $k\in\mathbb N_0$, the spanning
graph formed by edges with labels at least $k$ has chromatic number
exactly $\aleph_1$, even though its subgraphs of order at most $f(k)$
are bipartite.

Choose a two-coloring of each of the $k$ forests below $k$. Their
coordinate tuple colors the union with at most $2^k$ colors. If the tail
had a countable coloring, pairing it with that finite tuple would give a
countable coloring of the full graph. An edge is distinguished in whichever
part contains it, so this is a genuine proper coloring. This contradicts
$\chi(G)=\aleph_1$. Conversely the tail is a subgraph of $G$, giving
the upper bound $\aleph_1$. The case $k=0$ uses the one empty tuple
and simply returns the full graph.

### Strongest attack, premises, and verdict

The strongest attack was to mistake a finite product for an infinite product
or to pass chromatic number through the intersection of all tails. Neither
is justified or needed. Indeed every edge has a finite label, so the
intersection of the edge sets of all tails is empty, although every finite
cutoff has chromatic number $\aleph_1$. This exhibits the exact limit
operation that would fail. The claim stays at each finite $k$.

The dependencies are the forest property and the exact chromatic number of
the same construction, with product colorings independently established here.
The verdict is **refutation-failed**.

## Audit checklist

The following tables apply to every reviewed surface. A row naming particular
surfaces records their distinct application; a row marked inapplicable to all
applies individually to the prerequisites, Proposition B, and all five
consequences. The claim-specific sections above supply the restatement,
weakest-step derivation, strongest attack, premises, and mathematical verdict
for each surface.

### Canonical failure modes

| Item | Applicability and finding |
| --- | --- |
| Almost-all upgraded to all | Signed sharpness reading: refuted-as-stated; otherwise no failure found. Checked: B and the strict power bound hold at every positive order, including $1$; the rate statement is expressly eventual; the sharpness hypothesis is all-order and exposes the signed-budget defect; blow-up exclusion is eventual for each fixed $H$; tails concern every finite $k$. Steps 1–3 correctly turn a subsequence obstruction into a linear remainder. |
| Induction presupposing termination | No failure found. Checked: the $\omega_1$ recursions have witnesses at every countable stage, by their stated conditional hypotheses or odd-cycle existence. Rank colorings and $\rho$ use well-founded ordinal recursion. Splitting a repeated odd walk strictly decreases its finite length. No other consequence uses an unproved termination assertion. |
| Probabilistic or averaging heuristic presented as proof | No failure: the graph constructions and deductions are deterministic or nonconstructive ZFC arguments. The blow-up incidence count and the separate affine-minimization argument are exact finite inequalities, not empirical averages. No probabilistic estimate is consumed by another surface. |
| Circular use of an equivalent claim | No failure found. Checked: CC is assumed only in one direction of an equivalence and recovered from a failed limit in the other. B uses published construction properties, not CC, the target limit, or an inferred bipartization theorem. Consequences depend on B in one direction only. |
| Exceptional sets dropped from density arguments | Signed sharpness reading: refuted-as-stated; otherwise no failure found. No density exceptional set is used. Countable deleted sets and stationary/club restrictions are retained explicitly. The rate proof discards only a stated finite initial segment. The sharpness bullet cannot discard one under its all-order wording; its signed reading fails there. |
| Finite verification overreach | Inapplicable as evidence: no enumerated sample is used. Finite cycle and forest arguments are symbolic for arbitrary parameters; they are not extrapolations from checked orders. |
| Relaxed or averaged system substituted for actual objects | No failure found. Checked: forest deletion constructs an actual bipartite remainder; the homomorphism argument handles collapsed walks; the diamond order transfer preserves the exact neighborhood condition; the blow-up cube argument proves a lower bound for every actual cut. No relaxed limit is used. |

### Named canonical patterns

| Pattern | Applicability and finding |
| --- | --- |
| Model-class transport instead of entailment | No failure found. Checked where relevant: the diamond graph's actual construction is inspected, rather than inferred from similar theorem wording. Its extra set-theoretic hypothesis is not transported to ZFC or vice versa. The “must use linearity” sentence is tested as a non-implication between graph hypotheses, not as a restriction on proof syntax. No novelty or axiom-extension classification is claimed. |
| Infinite-family uniformity inferred from finitely many instances | No such inference: the same input function determines all labels simultaneously. Bounds are derived symbolically. The power constant may depend on $\varepsilon$, the rate threshold on $r$, and the blow-up threshold on $H$. The third bullet's range qualification is explicit. |
| Extremal claims checked in their own units | Signed sharpness reading: refuted-as-stated; otherwise no failure found. Checked: $h_G(n)$ is an attained integer maximum; the deletion budget is an edge count; strictness uses $(n-1)g(n)$; blow-up costs are compared as $s^2/(s\lvert V(H)\rvert)=s/\lvert V(H)\rvert$. No sharp optimality of B's upper bound is asserted. |
| Consequence sentences are independent claim surfaces | Applied: all five bullets and the explanatory statements about rates, growth classes, hypothetical blow-ups, and finite scales are separately examined. The literal signed sharpness reading is not covered by B's favorable verdict. |
| Carry the hypotheses of a quantified argument | Signed sharpness reading: refuted-as-stated; otherwise no failure found. Applied: nonnegativity and convergence to infinity of budgets, finiteness and fixedness of $H$, fixed finite $k$, and the exactly-$\aleph_1$ scope are tracked. The signed-integer sharpness wording is the failure found; the nonnegative reading is recorded separately. |
| Composition inherits unproved premises | No uncovered essential inference found within the stated external-premise boundary. Applied: the exact published source interfaces and their proof-reading limits remain explicit. No native L-claim or pending grade is presumed. CC and obligatory blow-ups remain conditional. The diamond analogue is actually derived. |
| Reproducibility notes are claims | Inapplicable to executable evidence. No computational rerun or pass-count claim occurs in the frozen subject. This examination makes no computational evidence claim. Its frozen text and mathematical derivations are retained. |
| Verifier quotations are claims | Inapplicable to the frozen mathematical extraction: prior-review and standing text was excluded, and no earlier verifier verdict is characterized. Source characterizations are checked separately. |
| Verdict words spelled in full | Satisfied throughout this report: refutation-failed and refuted-as-stated are not abbreviated. The signed-budget finding is a disproof on the specified reading, not merely a failed proof. |
| Certified-bracket functions fail loudly | Inapplicable to every surface: no numerical enclosure, iteration cap, or periodic numerical estimate is used. |
| A checking leg must have a failing input | Inapplicable to executable legs, since none is used. The mathematical boundary tests are substantive: a one-vertex graph with $g(1)=-1$, a same-label cycle, a countable tail coloring, or an oversized fixed-$H$ blow-up would respectively violate the explicitly checked obligations. |
| A gate must rerun rather than read caches | Inapplicable: no repository gate or cached output is used to support any mathematical verdict. |

### Erdős-specific checklist

| Item | Applicability and finding |
| --- | --- |
| Quantifiers and scope | Signed sharpness reading: refuted-as-stated; otherwise no failure found. B: one graph per whole $g$, all positive orders. Strict bound: one graph per exponent, and a separate one graph for all exponents with exponent-dependent constants. Rate: one graph per rate, eventual bound. Sharpness: nonnegative and signed readings distinguished by an exact witness. Blow-ups: one graph excludes large factors for every fixed non-bipartite $H$. Tails: every finite cutoff. Prerequisites: exactly $\aleph_1$, arbitrary vertex cardinality, and the whole limit. |
| Circularity | No circularity found on any surface. The verification order is acyclic, and the unresolved equivalence antecedent is never treated as a theorem. |
| Model and convention changes | Signed sharpness reading: refuted-as-stated; otherwise no failure found. Simple graphs and edge deletion are preserved. Non-induced copies are sufficient. The source's ordinal rank and diamond assumptions are retained. The only adverse domain finding is the signed reading of the third consequence. |
| Finite and statistical overreach | No finite search, statistical sample, or heuristic inference is used on any surface. No correlation discipline is needed. |
| Uniformity | No failure found. Checked at each stated parameter dependence. Infinite tail minima are justified by convergence to infinity; no finite sample substitutes for this fact. No assertion interchanges an infinite product or intersection with chromatic number. |
| Extremal conclusions | Signed sharpness reading: refuted-as-stated; otherwise no failure found. The maximum defining $h_G$, the strict all-order power inequality, the ratio $s/\lvert V(H)\rvert$, and the one-vertex signed-budget failure are all checked in their own coordinates. “Linear-scale sharpness” is not interpreted as optimality of a numerical constant. |
| Consequences and composition | Signed sharpness reading: refuted-as-stated; otherwise no failure found. Each consequence has its own derivation and verdict. Source statements are not strengthened from chromatic bounds to deletion counts without the forest/tail argument. Negative initial budgets are not silently modified. |
| Computation | Inapplicable to mathematical evidence for every surface. The report uses exact symbolic arguments and no numerical certification. |
| Reproduction | No computational reproduction leg is required for this noncomputational examination. The independent arguments and frozen subject suffice to repeat the deductions; the identified literature remains the explicit external boundary. |
| Source and verdict fidelity | No unsupported characterization found at the explicitly qualified scope. Primary images confirm Claim 4.1, the two constructions, the cardinality/chromatic clauses, and Erdős's strict upper-bound wording. Printed slips and transcription differences are disclosed. The original proofs behind external source theorems are not claimed as reviewed. No full Problem 111 solution, grade, or tier is asserted. |

The adjacent evidence discipline is satisfied by retaining mathematical
arguments rather than manufacturing a program. Correlated-sample guidance is
inapplicable because there are no statistical samples or statistical inferences.

## Final verdict and limits

The frozen proof of Proposition B survives the commissioned attacks, including
its exact ZFC cardinality, its chromatic number, and the diamond Hajnal–Máté
clause: **refutation-failed** under the stated published external premises.
The local prerequisites and the first, second, fourth, and fifth consequences
also have verdict **refutation-failed**, with the quantifier and source-scope
qualifications above.

The third consequence has an exact one-vertex refutation if “integer-valued”
allows negative integers: **refuted-as-stated** on that literal reading.
Its natural-valued version, suggested by Proposition B's preceding convention,
is **refutation-failed**. This is a range distinction in the asserted
all-order hypothesis; it does not refute Proposition B or the nonnegative
linear-scale example. It should be resolved explicitly when the frozen
wording is assessed, rather than hidden by a favorable verdict on the main
proposition.

This report does not establish CC, settle the growth of $h_G(n)/n$ for
these examples, verify a full solution of Problem 111, reconstruct the
original proofs of the external set-theoretic theorems, or cover later
revisions of the subject. The source/transcription differences and the
motivational-preamble exposure remain disclosed. A distinct grader owns the
report's contract, independence and materiality assessment; no self-grade or
tier assertion accompanies this examination.
