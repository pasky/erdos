---
name: research/leads/two_colour_triples_stepping_up/prefix_routing
title: An obstruction to prefix-selected one-bit lifts
desc: |
  Every lift colouring a triple by the XOR of its seed colour, orientation
  and one prefix-selected outsider bit has a monochromatic set of at least
  M^(1/3)/4+1 words in dimension M >= 8. Its sufficient routing lemma fails.
tags: []
sources: []
created: 2026-10-16T15:39:01Z
updated: 2026-10-16T15:39:01Z
---

# An obstruction to prefix-selected one-bit lifts

***

This records a refuted construction for the
[[research/leads/two_colour_triples_stepping_up/_index|two-colour triple route]].
The finite routing assertion below would imply
[[problems/ramsey_theory/E0564/_index|Problem 564]], but the polynomial-clique
obstruction proves it false within the specified rule family. The conditional
implication, constraint reduction and obstruction are author-recorded
arguments by Plasma AI, without independent review. The target remains open.

## The two-colour rule

Here $[M]=\{0,\ldots,M-1\}$. Use these positions, increasing binary order, and
$\delta(x,y)=\max\{i:x_i\ne y_i\}$. Fix a graph colouring
$\varphi:\binom{[M]}2\to\{0,1\}$. A *routing table* chooses

$$
h(P,p,q)\in\{0,\ldots,p-1\}
\quad(0\le q<p<M,\quad 0\le P<2^{M-p-1}).
$$

For $x<y<z$, put $a=\delta(x,y)$, $b=\delta(y,z)$,
$p=\max(a,b)$, $q=\min(a,b)$, and $P=\lfloor x/2^{p+1}\rfloor$.
The outsider is $w=z$ if $a<b$ and $w=x$ if $a>b$. Define

$$
\chi_{\varphi,h}(x,y,z)
=\varphi(\{p,q\})\mathbin\oplus[a<b]
 \mathbin\oplus w_{h(P,p,q)}. \tag{1}
$$

Every triple has exactly one colour in $\{0,1\}$. The common prefix is
used to choose one position below the upper delta, and only the outsider's
bit at that position is queried. The position is allowed to depend on the
whole prefix. No third output colour is hidden in the routing table.

This does not fall under the
[[research/leads/two_colour_triples_stepping_up/bounded_query_obstruction|fixed-query product theorem]]
with $w=1$: its sets $W(a,b)$ must work for every prefix. The union of
$h(P,p,q)$ over $P$ can have size growing with $M$. In any one finite
dimension a bound $w\le M$ is trivial; the issue is a uniform bound as the
dimension grows.

## Exact sufficient finite assertion and its failure

**Routing assertion, refuted within (1).** There are fixed integers $C\ge1$, $D\ge0$ and
$t_0\ge4$ such that for every $t\ge t_0$, with
$M=\lfloor2^{t/4}\rfloor$, there are a graph colouring $\varphi$ with no
monochromatic $t$-set and a routing table $h$ for which (1) has no
monochromatic $(Ct+D)$-set.

The assertion is finite at each parameter, and the output rule is fully
specified. Its uniform existence assertion is false by the obstruction
below, not merely unproved. The stronger statement that *every* seed
$\varphi$ with the stated property admits such a table would also suffice,
and is also excluded. The graph seeds alone exist by
$2\binom Mt2^{-\binom t2}<1$ for $t\ge4$.

If the lemma holds, (1) is a colouring on $2^M$ vertices, so
$R_3(Ct+D)>2^M$. For $t\ge8$, $M\ge2^{t/8}$. Given a sufficiently large
$n$, put $t=\lfloor(n-D)/C\rfloor$. Then $Ct+D\le n$ and
$t\ge n/(2C)$ once $n\ge2(D+C)$; also require
$n\ge D+C\max(t_0,8)$. Hence

$$
R_3(n)>2^{2^{n/(16C)}}.
$$

Decreasing the constant covers the remaining $n\ge3$. The
[[research/leads/two_colour_triples_stepping_up/higher_uniformity_transfer|two-colour higher-uniformity transfer]]
then gives Problem 562. This is a conditional implication with a false
premise within (1), not a construction.

## The constraint system for every potential clique

A finite set of distinct words has a full binary tree obtained by splitting
at its largest differing position and recursing. Each internal node $u$
has a label $p_u$; labels strictly decrease along a path, but may repeat in
different branches. Every leaf $w$ has its forced branch bits at ancestor
labels. Two leaves must agree above the label of their lowest common
ancestor. Write $P_u$ for their common prefix above $p_u$ inside the subtree
of $u$. Bits off a leaf's own path are variables too, not implicitly zero.

Fix a desired clique colour $c$. For every ancestor--descendant pair of
internal nodes $u,v$, with $v$ on side $\sigma\in\{L,R\}$ of $u$, and
every leaf $w$ on the other side of $u$, impose

$$
w_{h(P_u,p_u,p_v)}
=c\mathbin\oplus\varphi(\{p_u,p_v\})
 \mathbin\oplus[\sigma=L]. \tag{2}
$$

Together with the branch bits and prefix agreement, (2) is necessary and
sufficient for the realized leaves to form a $c$-clique. Indeed, a triple's
upper branching node is $u$; the two leaves in one side have lowest common
ancestor $v$; the other leaf is $w$. Equation (1) is then exactly (2).
Conversely every constraint in (2) is witnessed by a triple, by taking one
leaf from each child of $v$ and the leaf $w$.

Thus all tree shapes, repeated labels, and all allowed off-path bits must
be controlled. Checking only increasing delta sequences, distinct labels,
or a preferred realization would omit potential monochromatic sets.
The intended task is to choose $\varphi,h$ so that no tree with $Ct+D$
leaves admits these constraints and a realization, for either $c$. The
obstruction below proves that task impossible within (1). A conflict may
be two opposite demands on the same bit, a
demand contradicting a forced branch bit, or demands incompatible with
prefix agreement. The query address itself depends on the chosen prefixes;
it must be evaluated at those prefixes, not at zero.

## Finite discrimination

There is a particularly small checked instance. Take $M=4$,
$\varphi(\{p,q\})=1$ except $\varphi(\{3,2\})=0$. Set all query positions
to zero except

$$
h(0,2,0)=h(1,2,0)=1,\qquad h(1,2,1)=1.
$$

Both colours have largest monochromatic set of size four on the sixteen
words: examples are $\{0,1,2,4\}$ in colour zero and
$\{0,1,3,7\}$ in colour one. The exact table and these witnesses are held
in [prefix_selector_16.json](evidence/assets/prefix_selector_16.json).
[evidence/main.py](evidence/main.py) recomputes all 560 triple colours and
examines all 4,368 five-sets; none is monochromatic. It also verifies both
displayed four-sets. The instance was found by Boolean/integer constraint
search; its verification does not require that search or its solver.

This refutes the extension of the simple $M+1$-vertex tree obstruction to
all rules (1). It does **not** refute the fixed-query product inequality,
prove the routing lemma, or establish a useful growth rate. In particular
four vertices is compatible with all its quantitative lower bounds here.

The same finite bound is attainable without using the prefix: keep
$\varphi$ and set $h(P,p,q)=q$ for $p\le2$, while
$h(0,3,0)=2$ and $h(0,3,1)=h(0,3,2)=0$. The checker verifies all five-sets
and the same two four-set witnesses for this control too. Thus the
sixteen-point example provides no evidence of an advantage over fixed-query
rules. Prefix-dependent positions escape that theorem's hypotheses, but
the separate obstruction below applies to (1).

The optional synthesis program [produce.py](evidence/produce.py) implements
the finite search over all seed edges and routing entries, in dense and
counterexample-guided modes. With its Boolean/bit-vector encoding, the
instances $(M,k)=(3,4),(5,5),(6,6)$ return UNSAT: no table in this exact
family avoids a monochromatic $k$-set at those parameters. These are
solver-dependent finite findings; no independently checked UNSAT certificate
is retained, and the default evidence check does not replay the synthesis.
The six-dimensional instance takes about two minutes; a time cap can instead
return unknown, which establishes nothing. These cases alone neither prove
a linear obstruction in $M$ nor refute an eventual $C\log M$ bound; the
parameter-uniform obstruction is mathematical, not inferred from the search.

## Polynomial cliques for every routing table

**Proposition.** Let $M\ge8$. For every graph colouring $\varphi$, every
routing table $h$ in (1), and each $c\in\{0,1\}$, there is a
$c$-monochromatic set of at least $M^{1/3}/4+1$ words. The routing table
is arbitrary and deterministic; no distributional hypothesis on it is used.

*Proof.* For a label set $J\subseteq[M]$, construct a full binary tree by
inserting the labels of $J$ in decreasing order. To insert $q$, start at
the root. At an existing node labelled $p>q$, go left when
$\varphi(\{p,q\})\oplus1=c$, and right otherwise. On reaching a leaf,
replace it by a node labelled $q$ with two leaf children. Each label is
used once, so the final tree has $|J|+1$ leaves. Realize a leaf as the
word with ones precisely at the labels where its path turns right, and
zeros at every other position. These words are distinct, their delta
tree is exactly the constructed tree, and for every triple

$$
\varphi(\{p,q\})\oplus[a<b]=c. \tag{3}
$$

For every $p\in[M]$, whether or not $p\in J$, define $P_p$ as follows.
Construct the tree on $J\cap\{p+1,\ldots,M-1\}$, follow the insertion
path for $p$, put a one at its right-turn ancestor labels and zero at all
other positions above $p$, and take that binary prefix above $p$.
Crucially, $P_p$ depends only on the membership indicators of labels
strictly greater than $p$. If $p\in J$, it is the actual common prefix
at the node labelled $p$: later insertions have labels below $p$ and
cannot change it.

Select each label independently with probability
$\alpha=1/(2M^{2/3})$, leaving $\varphi,h,c$ fixed. For each fixed $p>q$,
condition on all membership indicators strictly above $p$. The position

$$
r=h(P_p,p,q)<p
$$

is now fixed. If $r\ne q$, the three indicators at $p,q,r$ are distinct,
independent of that conditioning, and each has probability $\alpha$.
Therefore the probability of the event

$$
p,q\in J,\qquad h(P_p,p,q)\in J\setminus\{q\}
$$

is at most $\alpha^3$. Call this a bad pair. The bound is imposed for
all label pairs, so it includes every ancestor--descendant pair that will
actually occur; it does not condition on that descendant relation. A
union bound gives

$$
\Pr(\text{some bad pair})
\le\binom M2\alpha^3<\frac1{16}. \tag{4}
$$

Let $X=|J|$ and $\mu=\mathbb E X=M^{1/3}/2\ge1$. Since
$\mathbb E X^2\le\mu^2+\mu$, Cauchy--Schwarz gives

$$
\Pr(X\ge\mu/2)\ge
\frac{\mu^2}{4\mathbb E X^2}
\ge\frac{\mu}{4(\mu+1)}\ge\frac18. \tag{5}
$$

For completeness, $\mathbb E[X\mathbf1_{X\ge\mu/2}]\ge\mu/2$, and
applying Cauchy--Schwarz to this expectation proves the first inequality.
Equations (4)--(5) show that some $J$ has no bad pair and has at least
$M^{1/3}/4$ labels.

For this $J$, consider any triple of its tree words, with upper label
$p$, lower label $q$, and outsider $w$. Its query position is either
outside $J$, where all the words have bit zero, or is $q$ itself. In the
latter case, the node labelled $q$ lies on the opposite side of the
$p$-node from $w$. Since labels are used only once, $q$ is not on the
outsider's path, and again $w_q=0$. Thus every queried outsider bit is
zero. Equation (3) shows that every triple has colour $c$. The tree has
$|J|+1\ge M^{1/3}/4+1$ leaves, as required. $\square$

**Consequence.** If (1) has no monochromatic $n$-set, $n\ge3$, then

$$
M\le64(n-2)^3.
$$

For $M\ge8$, compare the proposition with a maximum monochromatic size
of at most $n-1$; for $M<8$ the bound is immediate. Thus a lift in this
family avoiding $n$ points has order at most $2^{64(n-2)^3}$. This is an
upper bound on what this construction family can certify, not an upper
bound on $R_3(n)$. For $M=\lfloor2^{t/4}\rfloor$ and $n=Ct+D$, the
inequality fails for all sufficiently large $t$, for any fixed $C,D$.
The sufficient routing assertion is therefore false in this family.

The same proof also rules out XORing any fixed number $w\ge1$ of
prefix-selected outsider bits. Let their positions be
$h_j(P,p,q)<p$, $1\le j\le w$. With
$\alpha=1/(2(wM^2)^{1/3})$, the union bound for a bad pair has at most
$w$ terms, so (4) is unchanged. When $M\ge8w$, the mean is
$\mu=(M/w)^{1/3}/2\ge1$, and each colour has at least
$(M/w)^{1/3}/4+1$ vertices. Thus avoiding an $n$-set requires
$M\le64w(n-2)^3$, also when $M<8w$. In particular merely adding a
bounded number of outsider bits with the same XOR output cannot repair
this mechanism.

The proof permits arbitrary dependence of the queried position on the
whole common prefix. Its two essential restrictions are the output form
(1), whose zero-query answer has complementary colours on the two
orientations, and that the query lies strictly below $p$. Prefix
information cannot predict which smaller labels the random set will
contain. This obstruction is separate from the fixed-query product
theorem: it does not require a fixed spread set that works at every prefix.

The finite driver constructs these trees for deterministic sample label
sets and routing rules, recomputes every triple from the actual words, and
checks the prefix dependence directly. These examples are consistency
checks of the construction; the probability argument, not a finite test,
proves the proposition for every routing table.

## Failure account and reopening condition

The finite attack has variables for $\varphi(p,q)$ and $h(P,p,q)$ and uses
(1) to colour each triple. A counterexample-guided search proposes a table,
searches exactly for a monochromatic set, and adds the clause that this set
must receive both colours. The sixteen-point witness shows that this
finite search can succeed, but the proposition proves that no sequence of
such successes can have the growth needed by the routing assertion.

The failed step is uniform exclusion of the demand systems (2). The
missing input is false for (1): the random-label construction supplies
large consistent systems for every choice of the tables, in both colours.
Choosing nonuniform or correlated routing entries, or merely extending
the finite search, cannot fix this. The all-clique reduction and the
conditional higher-uniformity transfer remain valid; they do not supply
a triple construction.

Reopening requires a different output rule, a growing amount or different
kind of bit information, or a restriction to a subset of the cube that
excludes the displayed trees while retaining the required number of
vertices. None is constructed here. The proposition does not rule out
every prefix-dependent two-colour lift, every finite-state construction,
or a squaring recursion.
