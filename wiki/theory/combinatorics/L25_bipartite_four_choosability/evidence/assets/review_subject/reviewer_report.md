---
title: L25 whole-statement examination
desc: |
  Independent adversarial examination of the frozen L25 statement and proof,
  with exact palette arithmetic, convention checks, dependency findings, and
  the verdict refutation-failed.
---

# L25 whole-statement examination

***

## Subject and independence

This is a whole-statement mathematical examination under a charge to find a
counterexample, false inference, missing hypothesis, unsupported essential
step, or applicable canonical failure mode. The examination date is
2026-10-14 UTC. The subject was frozen on
2026-10-14 at 16:42:51.414936 UTC. The reviewer is an independent mathematical
reviewer, neither author nor collaborator on the frozen argument. The disclosed
reviewer model is gpt-6-astra, with reasoning effort max. Mathematical work in
this record is attributed to Plasma AI.

The subject comprises the assertion that every finite simple bipartite graph
on at most 25 vertices is colorable from every assignment of four distinct
colors to each vertex, its entire supplied mathematical argument, the finite
arithmetic it uses, and the consequence about the least order $n(4)$.

The preserved snapshots are under
`wiki/theory/combinatorics/L25_bipartite_four_choosability/evidence/assets/review_subject/`.
They are exact copies of the supplied extraction, including its uniform
`[cut]` markers. Their relation to the original repository subjects is:

| Preserved snapshot | Original subject and examined portion |
| --- | --- |
| [statement.md](../assets/review_subject/statement.md), lines 5–8 | `wiki/theory/combinatorics/L25_bipartite_four_choosability/_index.md`, statement field |
| [proof.md](../assets/review_subject/proof.md), lines 3–57 | `wiki/theory/combinatorics/L25_bipartite_four_choosability/_proof.md`, complete mathematical proof body |
| [checker_excerpt.txt](../assets/review_subject/checker_excerpt.txt), entire supplied text | `wiki/research/finite_graph_coloring_obstructions/evidence/main.py`, imports, `choose`, and the supplied part of `palette_checks` through the pair-coverage exclusion |

The [snapshot manifest](../assets/review_subject/manifest.json) records the
original paths, freeze time, and cut marker. These snapshots identify the
assessed text even if an original page subsequently changes. The original
cards and the complete original program were not read. The checker excerpt is
documentary source text, expressly supplied without a runnable entry point.

The reviewer began without prior exposure to this argument or its author's
working context. The subscription table was checked empty before mathematical
reading and remained empty at the attack boundary. No inbox or other message
channel was opened, no mathematical steering was received, and no web, history,
other mathematical file, author account, prior examination, or sibling result
was consulted. Only this examination's own continuation was carried between
its stages. No excluded material was encountered. Identity checks against the
commissioned manifests established that the operating inputs and mathematical
packet matched their specified versions and that the subject copies remained
unchanged. These facts support isolation; an empty subscription table alone
would not establish independence.

The allowed mathematical read set was exactly the supplied manifest,
statement, proof, and checker excerpt; all four were actually read in full.
No other mathematical supporting read was authorized. Operating instructions
were separately permitted. The required operating reading was
`README.md`; `docs/anatomy.md`, “Claims”, “Evidence”, “Tiers”, and “Project
claims”, including “Claim scrutiny”; `docs/verification.md` in full;
`campaign/AGENTS.md`; `campaign/guides/verification.md` in full; and
`campaign/guides/research.md`, “Reading”. Root `AGENTS.md` was supplied as
instructions. Additional operating reading comprised `docs/math_authoring.md`,
`docs/weaving.md`, and `docs/evidence.md` in full, together with the checked
commission, its three steps, effective configuration, template values, the
radio and memory operating instructions, and the applicable leaf, resource,
and isolation portions of the installed execution instructions. Their examples
and links were not followed. Other permitted guidance was not needed.

All mathematical evidence is retained in the derivations, arithmetic tables,
and attacks below. No mathematical program was run or is needed to reproduce
them. File-identity and package-format checks are administrative checks, not
mathematical evidence. The report makes no execution or exit-status claim
about the omitted program or its imported harness.

## Restatement and conventions

Let $G=(V,E)$ be any finite simple graph with $|V|\le25$ and a bipartition
$V=A\mathbin{\dot\cup}B$. For every assignment $L$ with $L(x)$ a set of exactly
four colors for each $x\in V$, there exists a function $f$ such that
$f(x)\in L(x)$ for all vertices and $f(x)\ne f(y)$ for every edge $xy$.
The coloring may depend on both the graph and the assignment. The four colors
are distinct within each list; lists at different vertices may coincide.
The color universe is unrestricted, and need not consist of only four colors.

The empty graph has its empty coloring. Either part of a bipartition may be
empty. Isolated vertices, disconnected graphs, and unequal part sizes are
included. Simplicity excludes loops; no connectivity or regularity hypothesis
is used. Since only finitely many finite lists occur, their union $C$ is finite,
with $|C|\le4|V|$, regardless of how the colors were originally named.

Write $\chi_\ell(G)$ for the least nonnegative integer $k$ such that every
assignment of $k$ distinct colors per vertex permits a proper list coloring.
Using lists of
at least $k$ gives the same property: select a $k$-element sublist at each
vertex. The assertion implies $\chi_\ell(G)\le4$ throughout the stated graph
class. Consequently, with $n(4)$ the least order of a finite simple bipartite
graph having $\chi_\ell>4$, it asserts $n(4)\ge26$. The existence implicit in
this least-order notation is checked separately below.

## Weakest step 1: completion, minimization, and color identification

This examines proof lines 3–17. Suppose a bad assignment exists on an allowed
graph. Keep a fixed bipartition and add all missing cross-edges. A coloring of
the resulting $K_{a,c}$ would also color the original graph, so the same
assignment remains bad. No implication in the reverse direction is needed.
The vertex set and all lists are unchanged.

For this fixed complete bipartite graph the collection of bad assignments is
therefore nonempty. Their palette sizes are nonnegative integers bounded by
$4v$, where $v=a+c$. Choose a smallest attained size $N$. This uses only
well-ordering of a nonempty set of integers. It does not assume termination of
a coloring procedure. Arbitrary color labels cause no difficulty: a finite
palette can be relabeled bijectively without changing any equality or coloring.

To attack the identification step, let distinct colors $p,q\in C$ occur in
no common list. Let $\pi:C\longrightarrow C'$ identify just $p$ and $q$.
On each list $\pi$ is injective, so $L'(x)=\pi(L(x))$ still has four elements.
Both colors belong to the palette, hence the new palette has exactly $N-1$
elements. If $f'$ colors the merged assignment, there is a unique
$f(x)\in L(x)$ with $\pi(f(x))=f'(x)$. If an edge had $f(x)=f(y)$, applying
$\pi$ would give $f'(x)=f'(y)$, contradicting propriety. Thus the lift is proper.
In particular, using different original preimages at different vertices cannot
create the feared conflict across an edge.

The merged assignment would therefore still be bad, since a merged coloring
would lift to the prohibited original coloring. Its smaller palette contradicts
minimality. Consequently every unordered pair of distinct palette colors occurs
together in at least one list. The hypothesis that the merged pair never
cooccurs is essential for preserving four-element lists: merging two elements
of the list $\{p,q,r,s\}$ would leave only three.

Each four-element list contains $\binom42=6$ pairs. Counting pairs with
multiplicity over vertices, even when different vertices have the same list,
gives

$$
\binom N2\le6v.
$$

For each color $x$, let $t_x$ be the number of vertex lists containing it.
Each such occurrence supplies three possible partners. Repeated partners
reduce the number of distinct partners, so pair coverage implies
$N-1\le3t_x$. Since $t_x$ is an integer,

$$
t_x\ge\left\lceil\frac{N-1}{3}\right\rceil,
\qquad
4v=\sum_{x\in C}t_x
\ge N\left\lceil\frac{N-1}{3}\right\rceil.
$$

These are precisely the two claimed inequalities. Neither distinct lists
across vertices nor a distributional assumption on their overlaps is needed.

## Weakest step 2: covering all palette subsets

This examines proof lines 20–34. Fix an integer $0\le\ell\le N$ and an
$\ell$-element subset $T\subseteq C$. If every left list meets $T$, choose a
color in that intersection at each left vertex. If no right list is contained
in $T$, choose a color outside $T$ at each right vertex. Choices exist by the
two stated conditions. There are no edges within either part, and colors used
on opposite parts belong to disjoint palettes, so this gives a proper coloring.
Only this sufficient condition is needed; the argument does not assume that
every coloring uses an arbitrary prescribed palette size.

For a bad assignment, therefore, every such $T$ has at least one obstruction:
a left list disjoint from $T$, or a right list contained in $T$. A particular
left four-list is missed by exactly $\binom{N-4}{\ell}$ subsets. A particular
right four-list is contained in exactly $\binom{N-4}{\ell-4}$ subsets. Count
ordered pairs consisting of a subset and an obstructing vertex. Every subset
contributes at least once, while repeated lists or multiple obstructions may
contribute more than once. Hence the direction of the inequality is

$$
a\binom{N-4}{\ell}+c\binom{N-4}{\ell-4}
\ge\binom N\ell.
$$

For a nonempty graph the palette has at least four elements. Binomial
coefficients have nonnegative upper entries here and are zero when the lower
entry is negative or exceeds the upper entry. This convention exactly counts
impossible containment or avoidance events.

Write $X=\binom{N-4}{\ell}$ and $Y=\binom{N-4}{\ell-4}$. Replacing
$\ell$ by $N-\ell$ interchanges $X,Y$, since

$$
\binom{N-4}{N-\ell}=\binom{N-4}{\ell-4},
\qquad
\binom{N-4}{N-\ell-4}=\binom{N-4}{\ell},
\qquad
\binom N{N-\ell}=\binom N\ell.
$$

The zero conventions preserve these identities at the endpoints. Adding
$aX+cY\ge\binom N\ell$ and $aY+cX\ge\binom N\ell$ gives

$$
v(X+Y)\ge2\binom N\ell.
$$

This step does not assume $a=c$. If $N$ is even and $\ell=N/2$, it adds an
inequality to itself, which is valid; no independence of the two counts is
claimed. For $N=7,\ell=3$, the right containment count is zero. The two
unsymmetrized inequalities then give $a\ge35$ and $c\ge35$, confirming both
the zero convention and the factor two in this boundary case.

## Weakest step 3: exhaustive palette cases and the integer endpoint

This examines proof lines 42–57. An empty graph or a graph with one empty
part is edgeless and colorable directly. In any remaining bad assignment,
if $N\le6$, split $C$ into two parts of size at most three. A four-element
list cannot lie wholly in either part, so it meets both. Using one part on
each side colors the graph. Thus a bad assignment has $N\ge7$.

At the other end,

$$
\binom{18}{2}=\frac{18\cdot17}{2}=153>150=6\cdot25.
$$

Also $\binom{N+1}{2}-\binom N2=N>0$ for $N\ge1$. Pair counting therefore
excludes every $N\ge18$, not just the single value 18. This proves the
exhaustive reduction $7\le N\le17$ before the midpoint table is used.

Set $\ell=\lfloor N/2\rfloor$ and define

$$
R_N=\frac{2\binom N\ell}
{\binom{N-4}{\ell}+\binom{N-4}{\ell-4}},
\qquad
d_N=\left\lceil\frac{N-1}{3}\right\rceil,
\qquad
I_N=\left\lceil\frac{Nd_N}{4}\right\rceil.
$$

All denominators in this range are positive, as the following full calculation
shows. The necessary conditions are $v\ge R_N$ and $v\ge I_N$.

### Exact arithmetic reproduction

The binomial entries below are obtained by integer products, or equivalently
by $\binom n0=1$ and
$\binom n{k+1}=\binom nk(n-k)/(k+1)$, with symmetry in $k,n-k$ and the
specified zero convention. The midpoint totals can also be built from
$\binom73=35$: the successive multipliers from $N=7$ through $N=17$ are
$2,9/5,2,11/6,2,13/7,2,15/8,2,17/9$. Thus every integer used in the quotient
is exposed, rather than taken from the excerpt's expected array.

| $N$ | $\ell$ | $\binom N\ell$ | $\binom{N-4}{\ell}$ | $\binom{N-4}{\ell-4}$ | denominator | $R_N$ |
| --- | --- | --- | --- | --- | --- | --- |
| 7 | 3 | 35 | 1 | 0 | 1 | 70 |
| 8 | 4 | 70 | 1 | 1 | 2 | 70 |
| 9 | 4 | 126 | 5 | 1 | 6 | 42 |
| 10 | 5 | 252 | 6 | 6 | 12 | 42 |
| 11 | 5 | 462 | 21 | 7 | 28 | 33 |
| 12 | 6 | 924 | 28 | 28 | 56 | 33 |
| 13 | 6 | 1716 | 84 | 36 | 120 | $143/5$ |
| 14 | 7 | 3432 | 120 | 120 | 240 | $143/5$ |
| 15 | 7 | 6435 | 330 | 165 | 495 | 26 |
| 16 | 8 | 12870 | 495 | 495 | 990 | 26 |
| 17 | 8 | 24310 | 1287 | 715 | 2002 | $170/7$ |

A second algebraic derivation checks the quotients and the adjacent equal
values without using these binomial integers. Let
$(s)_4=s(s-1)(s-2)(s-3)$. Dividing the avoidance and containment counts by
$\binom N\ell$ gives $(N-\ell)_4/(N)_4$ and $(\ell)_4/(N)_4$ respectively.
Thus

$$
R_N=\frac{2(N)_4}{(N-\ell)_4+(\ell)_4}.
$$

For $N=2m$ this is $(2m)_4/(m)_4$. For $N=2m-1$ it is
$2(2m-1)_4/((m)_4+(m-1)_4)$. Since

$$
(m)_4+(m-1)_4
=2(m-1)(m-2)^2(m-3),
$$

both simplify, for $m\ge4$, to

$$
R_{2m-1}=R_{2m}
=\frac{4(2m-1)(2m-3)}{(m-2)(m-3)}.
$$

For $m=4,5,6,7,8,9$ the numerator and denominator pairs are respectively
$(140,2),(252,6),(396,12),(572,20),(780,30),(1020,42)$. They give
$70,42,33,143/5,26,170/7$. Only $N=17$ from the last pair is needed after the
palette reduction. At $m=4$ the term $(m-1)_4$ is zero, so this derivation also
checks the boundary rather than assuming all containment counts positive.

Here is the complete integer incidence calculation appearing in the excerpt:

| $N$ | $d_N$ | $Nd_N$ | $I_N$ |
| --- | --- | --- | --- |
| 7 | 2 | 14 | 4 |
| 8 | 3 | 24 | 6 |
| 9 | 3 | 27 | 7 |
| 10 | 3 | 30 | 8 |
| 11 | 4 | 44 | 11 |
| 12 | 4 | 48 | 12 |
| 13 | 4 | 52 | 13 |
| 14 | 5 | 70 | 18 |
| 15 | 5 | 75 | 19 |
| 16 | 5 | 80 | 20 |
| 17 | 6 | 102 | 26 |

For $7\le N\le16$, every $R_N$ exceeds 25, including $143/5>25$ because
$143>125$, and the exact value 26 at $N=15,16$. At $N=17$, $170/7<25$,
because $170<175$, so the covering inequality alone cannot finish the proof.
The incidence bound instead gives $4v\ge102$, hence
$v\ge\lceil102/4\rceil=26$. This eliminates the last case and contradicts
$v\le25$.

### What the documentary checker text establishes

The supplied loop has exactly the range $N=7,\ldots,17$ and uses
$\ell=\lfloor N/2\rfloor$. Its `choose` implements the required zero
convention on the inputs that occur here. Its quotient is the displayed $R_N$.
For integers, $(N-1+2)\mathbin{//}3$ equals $d_N$, and
$(Nd_N+3)\mathbin{//}4$ equals $I_N$. The two tables therefore reproduce
every bound in the visible loop and its expected midpoint array. The final
pair comparison is exactly $153>150$.

The comparisons are mathematically nonvacuous. Substituting 69 for the first
expected table entry would disagree with 70. Replacing the final upward
division of 102 by truncation would give 25 and make the $N=17$ exclusion
comparison fail. Replacing 18 by 17 in the pair comparison gives
$\binom{17}{2}=136\le150$ and fails it. These are explicit failure controls
for the inspected expressions, not claims of executed harness tests.

No conclusion is drawn about whether the full original driver calls this
function, propagates failures, or runs in a particular environment. The excerpt
is not claimed to be independently executable. The mathematical derivations
above supply all arithmetic used by this examination without that runtime
interface, cached outputs, or a separate program.

## Strongest attempted refutation and other attacks

The strongest attack targets a 17-color minimal bad assignment on 25 vertices,
where the two coarser counts leave numerical room. In particular, the abstract
parameter choice $(a,c,N)=(12,13,17)$ satisfies pair counting,
$136\le150$, and both midpoint covering inequalities:

$$
12\cdot1287+13\cdot715=24739\ge24310,
\qquad
12\cdot715+13\cdot1287=25311\ge24310.
$$

Their sum is $50050=25\cdot2002$, exceeding $48620=2\cdot24310$.
These numbers describe a feasible candidate for those necessary inequalities,
not a constructed assignment. They show why agreement with the midpoint table
and global pair count would be insufficient: the last exclusion
depends on the local incidence argument.

Attempt to realize this candidate by distributing the $4\cdot25=100$ color
incidences among 17 colors. If every color appeared at least six times, at least
$17\cdot6=102$ incidences would be required. Hence some color appears at most
five times. Its occurrences provide at most $5\cdot3=15$ distinct partners,
fewer than the other 16 colors. At least one pair is absent. Repeating lists
or partners only worsens this deficit. Identifying the absent pair preserves
badness and contradicts minimality by the lifting argument already checked.
The attempted endpoint escape therefore fails for an explicit integer reason;
no rounding approximation or external covering theorem closes it.

Other attacks and their outcomes are retained here:

| Attack surface | Exact test and finding |
| --- | --- |
| Empty graph and empty parts | The empty function colors zero vertices. If one part is empty, choose any color at each vertex; there are no edges. No minimal bad assignment exists in either case. |
| Isolated vertices and disconnected graphs | Completion adds only cross-edges on the same vertex set. Any coloring after completion restricts to a coloring before it. Connectivity and positive minimum degree are unused. |
| Arbitrary labels and a very large initial palette | The union of the lists has at most $4v$ colors. Minimization is over bad assignments on a fixed graph, and a bijective relabeling preserves all constraints. The bound $N\le17$ is derived for a minimum palette, not assumed for the input. |
| A conflict created by lifting a merged color | An alleged equal original color on an edge has equal images, contradicting the quotient coloring. The required four-element condition survives because the merged colors never share a list. |
| Repeated lists or overlapping obstruction events | Vertex occurrences are counted with multiplicity. Covering only requires at least one obstruction per subset; overlaps increase the count. No disjointness or statistical independence is used. |
| Unbalanced parts and complementing the subset size | The two inequalities have coefficients $(a,c)$ and $(c,a)$ after binomial symmetry; their sum depends only on $a+c$. No balance assumption enters. |
| The odd lower endpoint and the even midpoint | At $N=7$, the zero containment count gives $a,c\ge35$. At an even midpoint, adding the same inequality twice is legitimate and gives the same ratio as the single inequality. |
| Dropping distinctness within a list | A single edge with four copies of the same color at each endpoint is uncolorable. This violates the actual set-of-four-distinct-colors hypothesis and explains why it must be retained. |
| Graphs outside the domain | $K_5$ with the same four-color list at every vertex is an excluded nonbipartite counterexample. A vertex with a loop is uncolorable but violates simplicity and cannot respect a bipartition. Neither belongs to the statement's domain. |

No counterexample or unsupported essential deduction was found in the frozen
mathematical argument. The attacks did not require a replacement proof.

## The consequence about the least order

This checks statement lines 7–8 separately. For a finite simple graph, list
chromatic number is defined: if there are $r>0$ vertices, process them in an
arbitrary order from lists of size $r$, choosing a color different from all
previously chosen colors. At most $r-1$ colors are forbidden, so a choice
remains. This even gives distinct colors to all vertices, and thus proves
$\chi_\ell\le r$. Either usual empty-graph convention also gives
$\chi_\ell\le4$ there.

Four-choosability implies colorability from all larger lists by taking
four-element sublists. Thus a finite simple bipartite graph with
$\chi_\ell>4$ must admit a bad four-list assignment. The proved assertion
excludes all its orders $0,1,\ldots,25$. Orders are integers, so every such
graph has order at least 26. No assertion of an example at order 26 follows.

The frozen text leaves the existence underlying the phrase “least order”
implicit. The following elementary convention check establishes that the set
being minimized is nonempty. Give the four left vertices of $K_{4,256}$
pairwise disjoint four-color lists $U_1,U_2,U_3,U_4$. For each of the
$4^4=256$ tuples $(u_1,u_2,u_3,u_4)\in U_1\times\cdots\times U_4$, give
one right vertex the list $\{u_1,u_2,u_3,u_4\}$. Its colors are distinct
because the $U_i$ are disjoint. Whatever colors the four left vertices choose,
the right vertex indexed by that tuple has all four of its colors used by its
neighbors and cannot be colored. This is a finite simple bipartite graph with
a bad four-list assignment. The set of possible orders is therefore nonempty,
so well-ordering supplies its minimum.

This last construction is additional elementary well-definedness reasoning,
not text present in the frozen proof. The lower-bound implication already
follows from the exclusion of orders at most 25; the construction verifies
that its least-order notation denotes a finite integer. It supplies no part
of the palette argument and makes no claim about order-26 feasibility or the
exact value of $n(4)$.

## Premises and disclosed reconstruction

The dependency reading at verdict filing on 2026-10-14 UTC is of the supplied
statement and full proof, including the consequence sentence. No native
L-claim is consumed as an established premise, and no live native dependency
standing was consumed or read. No dependency promotion, pending grade,
conditional tier, or batch acceptance order is involved.

The bibliographic attribution in proof lines 37–40 names the
Hanson–MacGillivray–Toft method and source locators. The proof also explicitly
claims to derive its needed specializations. The deductions above check those
specializations from the frozen text itself. The named publication and its
library card were unread; no source theorem is imported on their authority.
Bibliographic fidelity, priority, and the source's own proof coverage are
outside this examination. This record does not certify those locators or
attribute to the source any independently inspected result.

The mathematical foundations used are finite sets, elementary graph and
list-coloring definitions, well-ordering of nonnegative integers, finite
choice, counting with multiplicity, binomial identities, and exact integer and
rational arithmetic. Each specialized combinatorial inequality is derived
above. There is no unresolved external theorem interface.

Routine inference reconstruction is disclosed explicitly: the treatment of
empty parts; finiteness and attainment of the minimum palette; the formal
quotient-map lift; the per-color union count and summation of incidences; the
binomial identities behind symmetrization; monotonicity beyond $N=18$;
coefficient positivity and every table calculation; integer rounding at
$N=17$; and the definitions, monotonicity, and elementary existence underlying
$n(4)$. The existence construction is expressly identified as absent from the
frozen text. These elaborations expose the stated argument and its conventions;
no substantive missing lemma in the exclusion of 25-vertex graphs was found
or silently replaced.

## Checklist verdicts

“Survives” below is a mathematical finding within the stated reading scope,
not a grade of this report or a tier assertion. An inapplicable or unexamined
item states its reason and does not receive an implied favorable ruling.

### Erdos audit checklist

| Item | Verdict and basis |
| --- | --- |
| Quantifiers and scope | Survives. The proof begins with an arbitrary bad assignment on an arbitrary allowed graph. Empty graphs, empty parts, repeated lists, arbitrary color labels, and every integer order through 25 are covered. The coloring depends on the assignment. |
| Circularity | Survives. A minimum palette is chosen only after assuming a counterexample. Its attainment uses integer well-ordering, not the desired colorability assertion or assumed algorithmic termination. |
| Model and convention changes | Survives. Completion preserves badness in the needed direction. The quotient preserves four distinct colors per list and a quotient coloring lifts. A separated-palette coloring is proved sufficient before it is used contrapositively. |
| Finite and statistical overreach | Survives. The exact reduction establishes $7\le N\le17$ for every minimal bad assignment. All eleven cases are calculated. No samples or heuristic averages occur. |
| Uniformity | Survives for the asserted finite-order domain. All constants depend only on list size four and the order bound 25. Relabeling and the finite-palette argument cover arbitrary color universes. No limit or infinite sum is exchanged. |
| Extremal conclusions | Survives. Palette minimality is attained in integers; the least graph order is checked in vertex units, with nonemptiness established explicitly. No equality $n(4)=26$ or sharpness conclusion is asserted. |
| Consequences and composition | Survives. Both counting inequalities follow from the same minimal bad assignment. Palette splitting excludes $N\le6$, covering excludes $7\le N\le16$, and integer incidences exclude 17. The $n(4)$ consequence is separately justified, with its implicit existence convention disclosed. |
| Computation | Exact arithmetic survives. All necessary entries, ranges, zero conventions, denominator positivity, ceilings, and strict comparisons are reproduced above. Runtime failure propagation of the unsupplied harness is unexamined and is not a premise. No numerical enclosure or exhausted search is used. |
| Reproduction | Satisfied mathematically by the retained derivations and two explicit arithmetic routes. The excerpt is documentary and supplies no runnable command. No cached success or unretained mathematical program supports the verdict. Execution of the original driver is outside the examined scope. |
| Source and verdict fidelity | The mathematical interpretation of the supplied statement, argument, and visible arithmetic is checked. Bibliographic fidelity is excluded and no external theorem is consumed. Prior verdicts were not supplied or read; none is characterized or strengthened. |

### Canonical failure modes

| Failure mode | Verdict and basis |
| --- | --- |
| “Almost all” upgraded to “all” | Absent. The initial counterexample is arbitrary and all resulting palette sizes are eliminated. There is no density or exceptional-family statement. |
| Induction presupposing termination | Absent. No induction or iterative stopping claim is used. Palette minimization is a single well-ordering argument. |
| Probabilistic or averaging heuristics presented as proof | Absent. The covering counts and incidence pigeonhole argument are exact inequalities. No probabilistic heuristic is invoked. |
| Circular use of an equivalent statement | Absent. No form of four-choosability is assumed to establish the quotient lift or the separated-palette sufficient condition. Both transfers are proved directly. |
| Exceptional sets dropped from density arguments | Inapplicable: there is no density argument. Boundary cases are handled explicitly rather than discarded. |
| Finite verification cited beyond base-case coverage | Absent. Exhaustiveness is proved by palette minimization and pair counting before the table is applied. No table is extrapolated to larger orders or other list sizes. |
| Relaxed or averaged convergence substituted for actual objects | Absent. No convergence is involved. The necessary counts alone are not treated as sufficient for realizability; the 17-color attack explicitly distinguishes a numerical candidate from an assignment. |

### Named canonical patterns

| Pattern | Verdict and basis |
| --- | --- |
| Model-class transport instead of entailment | No classification of axiom systems is asserted. The applicable transport checks survive: graph completion and color identification have explicit implications, and subset covering follows from a proved coloring condition. |
| Uniformity over an infinite family inferred from finite instances | Absent. The argument works for each arbitrary graph and arbitrary color labels; its finite palette range follows from universal counting deductions. No finite sampling stands in for that reduction. |
| Extremal claims audited in their own units | Satisfied. The minimum palette is measured in distinct colors, incidences count list membership, and $n(4)$ is bounded in integer numbers of vertices. The conversion $102/4$ to order at least 26 is explicit. |
| Consequence sentences are claim surfaces | Satisfied. The least-order consequence is examined separately, including the existence implicit in its notation. No statement about exact $n(4)$ is inferred. |
| Hypotheses actually used by a quantified argument are carried | Satisfied. Finiteness, a bipartition, four distinct colors in each list, and palette minimality are all available where used. Pair coverage is derived for a minimum-palette bad assignment, not asserted for arbitrary assignments. |
| A composition inherits its unproved premises | No missing premise found. Both inequalities and every required transfer are derived. The source attribution contributes no uninspected theorem. No native claim standing is borrowed. |
| Reproducibility notes are claims | The mathematical reproduction route is fully retained. The visible source expressions match the reproduced numbers. There is no claim that the excerpt executes or that the complete original driver has been rerun. |
| Verifier quotations are claims | Inapplicable. No earlier verifier report was read or quoted, and no claim-card standing prose was supplied. |
| Verdict words spelled in full | Satisfied. The mathematical verdict is refutation-failed. It is neither an abbreviated opposite verdict nor a grade or tier. |
| Certified-bracket functions fail loudly | Inapplicable. There are no numerical brackets, floating-point estimates, period windows, iteration caps, or enclosure routines. |
| A harness leg without a failing input is decoration | No executable leg carries this review. The documentary predicates have the explicit arithmetic failure controls given above. Actual harness behavior remains unexamined. |
| A gate reading caches instead of rerunning is defective | Inapplicable to the mathematical warrant. No gate, cache, success summary, or stored execution result is used; the required arithmetic is derived explicitly. |

The neighboring correlated-sample discipline is inapplicable because no
statistical inference occurs. Evidence coverage is matched to the actual
subject: a mathematical proof examination with exact arithmetic, not a test
of the omitted runtime or a bibliography audit. This is one claim in one
independent review cycle, not a computational batch or a second-cycle review.

## Verdict and limits

**refutation-failed.** The frozen whole statement and its mathematical proof
survive the commissioned attacks. Every required finite arithmetic entry is
reproduced, the palette cases are exhaustive, the 17-color endpoint is excluded
by integral incidence counts, and the stated lower bound on $n(4)$ follows.
No substantive proof defect, false hypothesis transfer, or counterexample was
found. Routine reconstruction and the additional check of least-order
well-definedness are identified above.

This verdict covers only the preserved subject. It does not determine the
exact value of $n(4)$, the general-list-size problem, novelty, bibliographic
source fidelity, or order-26 feasibility. It does not certify execution of the
complete source program, its harness, or a Lean formalization. Those exclusions
leave no missing mathematical input in the assessed argument.

The reviewer neither grades this report nor changes claim standing. Acceptance
of its independence and complete report contract, and any resulting standing
decision, belong to a distinct eligible grader and the authorized integrator.
