---
name: research/leads/two_colour_triples_stepping_up/bounded_query_obstruction
title: Bounded-query two-colour lifts of graphs to triples
desc: |
  Every red/blue colouring of the triples of {0,1}^M that reads the two
  deltas, bits at boundedly many positions fixed by those deltas, and the
  common prefix has red and blue sets whose sizes multiply to more than M'.
  Such lifts avoiding a monochromatic n-set have order at most 2^{O(n^4)}.
tags: []
sources: []
created: 2026-10-16T14:25:13Z
updated: 2026-10-16T14:25:13Z
---

# Bounded-query two-colour lifts of graphs to triples

***

This page records an obstruction proved by Plasma AI for the route of
[[research/leads/two_colour_triples_stepping_up/_index|two-colour stepping-up for triples]],
whose target is [[problems/ramsey_theory/E0564/_index|Problem 564]]. The proof
is author-recorded and has not been independently reviewed. It refutes the
family of two-colour lifts whose extra query positions are fixed by the
ordered delta pair. The prefix may affect the output, but not the query
positions. This distinction matters for
[[research/leads/two_colour_triples_stepping_up/prefix_routing|prefix-selected queries]],
which are not covered with a dimension-independent query bound.

## Setting

Write the words of $\{0,1\}^M$ as $x=(x_{M-1},\dots,x_0)$ and order them as
binary integers, position $i$ having weight $2^i$. For distinct words put

$$
\delta(x,y)=\max\{i:x_i\ne y_i\}.
$$

If $x<y$ then $x_{\delta(x,y)}=0$ and $y_{\delta(x,y)}=1$. For $x<y<z$ put
$a=\delta(x,y)$ and $b=\delta(y,z)$; then $a\ne b$ and
$\delta(x,z)=\max(a,b)$. The four-colour stepping-up construction that the
Problem 564 page attributes to Erdős, Hajnal, Máté and Rado colours
$\{x<y<z\}$ by the colour of the pair $\{a,b\}$ in a graph colouring
$\varphi$ together with the bit $[a<b]$; every monochromatic set then has
monotone deltas forming a $\varphi$-clique. The question of this route is
whether some two-colour rule of the same kind can work.

**Definition.** Fix $w\ge0$ and, for each ordered pair $(a,b)$ of distinct
positions, a set $W(a,b)$ of at most $w$ positions. A red/blue colouring
$\chi$ of the triples of $\{0,1\}^M$ is a *$w$-query rule* if
$\chi(\{x<y<z\})$ is determined by $a$, $b$ and the bit triples
$(x_i,y_i,z_i)$ for $i\in W(a,b)\cup\{a,b\}$.

Here $W(a,b)$ is chosen before the words are given. In particular it cannot
depend on their common prefix. A bounded-depth adaptive bit procedure is
covered if the union of its possible query positions, for each fixed
$(a,b)$, has bounded size; a bound on queries along one execution alone is
not the definition.

Every merger of the four stepping-up colours into two is a $0$-query rule,
and so is every colouring $\psi(a,b)$ of the ordered pairs of deltas. The
*outsider bit* of $x<y<z$ is $z_a$ when $a<b$ and $x_b$ when $a>b$: the bit of
the third word at the lower delta. Rules reading it are $0$-query rules too.
A rule reading the bits within distance $\rho$ of $a$ and of $b$ is a
$4\rho$-query rule.

## Theorem

**Theorem.** Let $\chi$ be a $w$-query rule on $\{0,1\}^M$, with $w=0$ or
$M\ge3w$. Put $M'=M$ if $w=0$, and
$M'=\lceil\frac23\sqrt{M/(3w)}\rceil$ if $w\ge1$.
Then $\chi$ has a red set of $R$ words and a blue set of $B$ words with

$$
R\cdot B\ge M'+1 .
$$

In particular some monochromatic set has at least $\sqrt{M'+1}$ words.

**Corollary.** If a $w$-query rule on $\{0,1\}^M$ has no monochromatic set
of $n\ge2$ words, then $M'+1\le(n-1)^2$ in the theorem's range. For $w=0$
this gives
$M\le n^2-2n$, so the colouring certifies at most $R_3(n)>2^{n^2-2n}$: a
$0$-query lift never beats the shape $2^{cn^2}$ of the random bound. These
are bounds on the size of a witness in this class, not upper bounds on
$R_3(n)$ itself. For
$w\ge1$ and $M\ge3w$ it gives
$M\le\frac{27w}4M'^2<\frac{27w}4n^4$; the final bound is immediate also
when $M<3w$. For a rule reading the
bits within distance $\rho$ of the two deltas, the positions divisible by
$2\rho+1$ already form a spread set (defined below), so $M<(2\rho+1)n^2$. No
bounded-query lift certifies a double-exponential bound.

## Proof

**Spread labels.** Call $\Lambda$ a set of positions *spread* if
$W(p,q)\cap\Lambda\subseteq\{p,q\}$ for all distinct $p,q\in\Lambda$. All
positions form a spread set when $w=0$. For $w\ge1$ keep each position
independently with probability $\pi=(3wM)^{-1/2}$, and then delete one kept
position from each triple $(p,q,r)$ of kept positions with
$r\in W(p,q)\setminus\{p,q\}$. There are fewer than $wM^2$ such triples, so
the expected size of the result is at least

$$
\pi M-wM^2\pi^3=\tfrac23\sqrt{M/(3w)},
$$

and some spread set has at least $M'$ positions. Fix such a $\Lambda$.

**Labelled trees.** A *labelled tree* is a finite rooted tree in which every
internal node has a left and a right child and carries a label in $\Lambda$,
the labels strictly decreasing along every path from the root; a label may
recur in different branches. A *realization* assigns to each leaf a word
whose bit at the label of each ancestor is $0$ when the leaf lies in that
ancestor's left subtree and $1$ when it lies in the right one, with the
remaining bits chosen so that any two leaves agree at every position above
the label of their lowest common ancestor. In a realization $\delta(x,y)$ is
the label of the lowest common ancestor of $x$ and $y$, and $x<y$ exactly
when $x$ lies in its left subtree. So for three leaves $x<y<z$ with lowest
common ancestor $u$ there is a second node $v$: either $v$ is the lowest
common ancestor of $x,y$, in the left subtree of $u$ (side $L$, $a<b$,
outsider $z$), or $v$ is that of $y,z$, in the right subtree of $u$ (side
$R$, $a>b$, outsider $x$). In both cases $\{a,b\}=\{\ell(u),\ell(v)\}$ and the
outsider bit is the outsider's bit at $\ell(v)$.

**The canonical table.** Write $e_i$ for the word whose only $1$ is at
position $i$. For $p>q$ in $\Lambda$, a side $\sigma$ and $\eta\in\{0,1\}$,
let $F(p,q,\sigma,\eta)$ be the colour of the triple $0<e_q<e_p+\eta e_q$
when $\sigma=L$ and of $\eta e_q<e_p<e_p+e_q$ when $\sigma=R$.

*Lemma 1.* In a realization whose words have no $1$ outside $\Lambda$, a
triple with nodes $u,v$, labels $p=\ell(u)>q=\ell(v)$, side $\sigma$ and
outsider bit $\eta$ has colour $F(p,q,\sigma,\eta)$.

*Proof.* The rule reads $W(a,b)\cup\{p,q\}$. Positions of
$W(a,b)\setminus\{p,q\}$ lie outside $\Lambda$, because $\Lambda$ is spread,
so all three words have $0$ there, as the canonical words do. At $p$ and $q$
the bits are forced by the tree. On side $L$: $x_q=0$, $y_q=1$, $z_q=\eta$,
$x_p=y_p=0$, $z_p=1$. On side $R$: $x_p=0$, $y_p=z_p=1$, $y_q=0$, $z_q=1$,
$x_q=\eta$. These are the bits of the canonical triple. $\square$

**Coloured trees.** For $p>q$ in $\Lambda$, a colour $c$ and a side
$\sigma$, call $q$ *$c$-possible on side $\sigma$ below $p$* if
$F(p,q,\sigma,\eta)=c$ for some $\eta$, and *$c$-robust* there if it holds for
both values of $\eta$. A *$c$-tree on $S\subseteq\Lambda$* is a labelled tree
with labels in $S$ such that for every internal node $u$ and every internal
node $v$ below it, on side $\sigma$ of $u$, the label $\ell(v)$ is $c$-possible
on side $\sigma$ below $\ell(u)$, and $c$-robust there whenever $\ell(v)$ also
labels a node on the other side of $u$.

*Lemma 2.* Every $c$-tree has a realization with no $1$ outside $\Lambda$
whose words form a $c$-coloured set, one word per leaf.

*Proof.* Give each leaf $x$ its forced bits, and $0$ at every position that
labels no node of the tree. Let $q$ be a label in the tree that does not label
a node on the path of $x$. Each node $v$ labelled $q$ then lies off that path;
with $u$ the lowest common ancestor of $v$ and $x$, the triples with nodes
$u,v$ and outsider $x$ *demand* a value of $x_q$ making
$F(\ell(u),q,\sigma,x_q)=c$, unless $q$ is $c$-robust there. Two demands never
conflict. If they come from the same $u$, the nodes $v$ lie on the same side of
$u$ and the demands are equal. If they come from $u_1$ above $u_2$, the node
$v_2$ demanding at $u_2$ lies on the side of $u_1$ containing $x$, so $q$
labels nodes on both sides of $u_1$, and the tree condition makes $q$
$c$-robust at $u_1$: no demand there. Set $x_q$ to the demand, or to $0$ if
there is none. Two leaves below a common node $w$ see the same nodes labelled
$q>\ell(w)$ off their paths, with the same lowest common ancestors and sides,
so they receive equal bits above $\ell(w)$: this is a realization. In a triple
with nodes $u,v$ the outsider's bit at $\ell(v)$ is either forced by a node
labelled $\ell(v)$ on the outsider's path, on the other side of $u$, where the
tree condition gives robustness, or set by the demand; in both cases Lemma 1
gives colour $c$.
$\square$

*Lemma 3.* Let $g_c(S)$ be the largest number of leaves of a $c$-tree on $S$,
with $g_c(\emptyset)=1$. For nonempty $A\subseteq\Lambda$ with $r=\max A$, and
$S_1,S_2\subseteq A\setminus\{r\}$ such that every label of $S_1$ is
$c$-possible on side $L$ below $r$, every label of $S_2$ is $c$-possible on
side $R$, and every label of $S_1\cap S_2$ is $c$-robust on both sides,

$$
g_c(A)\ge g_c(S_1)+g_c(S_2).
$$

Also $g_c$ is monotone under inclusion.

*Proof.* Put optimal $c$-trees on $S_1$ and $S_2$ below a root labelled $r$.
Pairs inside a subtree keep their conditions, and the conditions at the root
are the hypotheses. $\square$

**The product inequality.** Write $\rho(S)=g_{\mathrm{red}}(S)$ and
$\beta(S)=g_{\mathrm{blue}}(S)$. We show $\rho(A)\beta(A)\ge|A|+1$ for every
$A\subseteq\Lambda$ by induction on $|A|$; $A=\emptyset$ gives $1\ge1$. For
nonempty $A$ with $r=\max A$, classify each $q\in A\setminus\{r\}$ on each side
as type $\mathrm R$ (both values of $F$ red), $\mathrm B$ (both blue) or
$\mathrm M$ (one of each). Place $q$ in two of four sets:

- type $(\mathrm R,\mathrm R)$ on the sides $(L,R)$: in $S_1^{\mathrm{red}}$
  and $S_2^{\mathrm{red}}$;
- type $(\mathrm B,\mathrm B)$: in $S_1^{\mathrm{blue}}$ and
  $S_2^{\mathrm{blue}}$;
- otherwise, if red is possible on side $L$ and blue on side $R$: in
  $S_1^{\mathrm{red}}$ and $S_2^{\mathrm{blue}}$;
- otherwise: in $S_2^{\mathrm{red}}$ and $S_1^{\mathrm{blue}}$, where red is
  then possible on side $R$ and blue on side $L$.

The pairs $(S_1^{\mathrm{red}},S_2^{\mathrm{red}})$ and
$(S_1^{\mathrm{blue}},S_2^{\mathrm{blue}})$ satisfy Lemma 3, since only the
types $(\mathrm R,\mathrm R)$ and $(\mathrm B,\mathrm B)$ enter both sets of a
colour. By induction and monotonicity,

$$
|S_1^{\mathrm{red}}|+1\le\rho(S_1^{\mathrm{red}})\beta(A),\qquad
|S_2^{\mathrm{red}}|+1\le\rho(S_2^{\mathrm{red}})\beta(A),
$$

and adding them with Lemma 3 bounds their sum by $\rho(A)\beta(A)$. The same
holds for the blue sets. Each $q$ lies in exactly two of the four sets, so

$$
2(|A|-1)+4\le2\rho(A)\beta(A),
$$

which is $\rho(A)\beta(A)\ge|A|+1$. With $A=\Lambda$ and Lemma 2 this is the
theorem. $\square$

Two extreme cases show the shape of the argument. If every pair of a set
$J\subseteq\Lambda$ is of type $(\mathrm R,\mathrm R)$, the $2^{|J|}$ words
supported on $J$ form a red set: the complete tree with one label per level.
If no pair of $A\subseteq\Lambda$ has all four values red, the blue tree with
root $\max A$ that sends each label to a side where blue is possible, and
recurses, uses every label once and has $|A|+1$ leaves.

## Rules that also read the common prefix

The three words of a triple agree at every position above $\max(a,b)$; call
these bits its *common prefix*. Call $\chi$ a *$w$-query prefix rule* if
$\chi(\{x<y<z\})$ is determined by $a$, $b$, the bit triples at
$W(a,b)\cup\{a,b\}$ and the common prefix, in any way. Such a rule may
depend on unboundedly many bits.

**Theorem (prefix rules).** The theorem and its corollary hold, with the same
$M'$, for every $w$-query prefix rule.

*Proof.* Keep the spread set $\Lambda$, and build only words supported on
$\Lambda$. A *context* $\kappa$ fixes the bits at a set $D(\kappa)$ of
positions of $\Lambda$. For $S\subseteq\Lambda\setminus D(\kappa)$ let
$g_c(S,\kappa)$ be the largest size of a $c$-coloured set of words supported
on $\Lambda$, agreeing with $\kappa$, whose delta tree has all its labels in
$S$, with $g_c(\emptyset,\kappa)=1$. It can only decrease when $S$ shrinks or
$\kappa$ is extended. For nonempty $A$ with $r=\max A$, let $\kappa^+$ extend
$\kappa$ by $0$ at the positions of $\Lambda$ above $r$ outside $D(\kappa)$.
Every set counted by $g_c(A,\kappa^+)$ has the same bits $P$ above $r$, and
$P$ is the common prefix of every triple whose upper delta is $r$. Define
$F$ at $r$ as before, after adding $P$ to the three canonical words; by the
argument of Lemma 1, a triple of such a set with labels $r>q$, side
$\sigma$ and outsider bit $\eta$ has colour $F(r,q,\sigma,\eta)$. Split
$A\setminus\{r\}$ into the four sets by this table. For the red pair, let
$\kappa_L$ extend $\kappa^+$ by $0$ at $r$ and, at each
$q\in S_2^{\mathrm{red}}\setminus S_1^{\mathrm{red}}$, by a bit $\eta$ with
$F(r,q,R,\eta)$ red; let $\kappa_R$ extend $\kappa^+$ by $1$ at $r$ and, at
each $q\in S_1^{\mathrm{red}}\setminus S_2^{\mathrm{red}}$, by a bit $\eta$
with $F(r,q,L,\eta)$ red. A red set for $(S_1^{\mathrm{red}},\kappa_L)$ and a
red set for $(S_2^{\mathrm{red}},\kappa_R)$ together form a red set for
$(A,\kappa^+)$: their words agree above $r$ and split at $r$; in a triple
with upper delta $r$ the outsider's bit at the lower label is fixed by the
context, or the label lies in both sets and is robust; triples inside one
part keep their colours. Hence

$$
g_{\mathrm{red}}(A,\kappa^+)\ge g_{\mathrm{red}}(S_1^{\mathrm{red}},\kappa_L)
+g_{\mathrm{red}}(S_2^{\mathrm{red}},\kappa_R),
$$

and likewise for blue with its own contexts. The induction of the product
inequality now runs over pairs $(A,\kappa)$: it proves
$\rho(A,\kappa^+)\beta(A,\kappa^+)\ge|A|+1$ exactly as before, using the
children's contexts and the monotonicity
$\beta(S_1^{\mathrm{red}},\kappa_L)\le\beta(A,\kappa^+)$, and monotonicity
passes the bound to $(A,\kappa)$. With $A=\Lambda$ and the empty context
this is the theorem. $\square$

The extension does not cover unbounded dependence on bits between or below
the deltas. It also does not cover a bounded number of queries whose
positions depend on the prefix, unless their union over prefixes fits the
fixed sets $W(a,b)$ with a uniform bound. In the latter case a spread set
must avoid all those positions simultaneously. Merely fixing the prefix at
one root does not produce the common spread set used throughout the proof.

The inequality also limits off-diagonal uses of these lifts. A $0$-query
lift with no blue set of $s$ words and no red set of $n$ words has
$M+1\le(s-1)(n-1)$, so it certifies at most $r_3(s,n)>2^{(s-1)(n-1)}$. For
each fixed $s\ge4$ and all large $n$ this is weaker than the bound
$\log r_3(s,n)\ge c_1sn\log(n/s)$ of
[[../library/ramsey_theory/conlon_2008_hypergraph_ramsey_numbers/theorem_1_3|Conlon, Fox and Sudakov, Theorem 1.3]],
so constructions reaching that bound are not $0$-query lifts.

**Relation to pair constructions.** Conlon, Fox, Gunby, He, Mubayi, Suk
and Verstraëte call a colouring
$\chi(\{i<j<k\})=g(f(i,j),f(j,k),f(k,i))$ a pair construction of complexity
$p$ when $f$ takes $p$ values, and note that stepping-up constructions are the
pair constructions with $f=\delta$ (*On off-diagonal hypergraph Ramsey
numbers*, arXiv:2404.02021v1, 2 April 2024, Section 4.1, read in the text
layer of the PDF). A pair construction with $f=\delta$ is exactly a
$0$-query rule that ignores the outsider bit. So with two colours the
stepping-up pair function certifies at most $R_3(n)>2^{n^2-2n}$, although
with four colours it gives a double-exponential bound. When $f$ also records
the bits of the two words at boundedly many positions determined by
$\delta$, the colouring is a $w$-query rule and the bound
$2^{(27w/4)n^4}$ of the corollary applies. Their Proposition 4.2,
on monochromatic copies of $K^{(3)}_{n,n,n}$ in pair constructions of
complexity $p$, concerns a different target. Web searches on 2026-10-16
found no published statement of the theorem above; they were brief and do
not establish novelty.

## The prepared candidates

Two narrower families of candidate lifts fall under the theorem; for them
direct arguments give larger monochromatic sets.

- **The sixteen mergers.** A merger is a table $T(e,o)$ of the stepping-up
  colour $e=\varphi(\{a,b\})$ and the orientation $o=[a<b]$. Some colour is
  achievable on every pair unless $T(0,\cdot)$ and $T(1,\cdot)$ are constant
  with different values; in the first case the tree of the second extreme
  case on all positions has $M+1$ words, and in the second the subcube on the
  larger $\varphi$-clique has $2^{\lfloor\log_4M\rfloor+1}>\sqrt M$ words,
  since $R(k+1,k+1)\le\binom{2k}{k}<4^k$ for $k\ge1$; $M<4$ is immediate.
- **The 256 outsider-bit tables.** A table $T(e,o,\eta)$ reading also the
  outsider bit $\eta$ is a $0$-query rule whose canonical values on a pair
  depend only on its colour $e$. The same two cases apply word for word, so
  every table has a monochromatic set of more than $\sqrt M$ words, and of
  $M+1$ words when some colour is achievable for both values of $e$.

The second item refutes the candidate lemma that some fixed table, with a
graph seed on $M=\lfloor2^{t/4}\rfloor$ positions and no monochromatic
$t$-set, has no monochromatic $(Ct+1)$-set: the table's colouring contains a
monochromatic set of more than $\sqrt M\ge2^{t/8-1/2}$ words, which exceeds
$Ct+1$ for all large $t$, whatever the seed.

## Scope

The theorem uses only the full cube and words supported on a spread set
$\Lambda$. It does not exclude:

- rules that read unboundedly many positions below the upper delta, such as
  the parity of the pair's bits between the two deltas, or the outsider's
  bits below the upper delta;
- rules that use the common prefix to select query positions whose union
  over prefixes is unbounded, even if each triple makes only one query;
- colourings of a proper subset of the cube that avoids the words the proof
  builds;
- constructions not of this lift form, such as product or squaring
  recursions, or lifts over larger alphabets.

The inequality $R\cdot B>M'$ fails for general two-colourings, so the
restriction on what a rule reads is essential. The colouring behind
[[../library/ramsey_theory/conlon_2008_hypergraph_ramsey_numbers/theorem_1_3|Theorem 1.3 of Conlon, Fox and Sudakov]]
(their Theorem 3.1, in the transcription of the paper) is a random pair
construction: a random labelling of the pairs and a graph colouring of the
labels, read at the two pairs through the smallest vertex of a triple. For
fixed $s\ge4$ it has no red set of $s$ points and no blue set of $n$ points on
$2^M$ points with $M$ of order $sn\log n$, so $R\cdot B<sn$ is far below $M$.

Any bijection between a $2^M$-element set and $\{0,1\}^M$ turns a colouring
of its triples into a colouring of the triples of the cube. So a two-colouring
of the triples of a $2^M$-element set with no monochromatic set of more than
$K$ points, where $K^2\le M$, is a $0$-query rule under no such bijection: a
double-exponential two-colouring is not a bounded-query lift in any
identification of its vertex set with a cube.

The target requires two output colours. The finite checks in
[evidence/main.py](evidence/main.py) build, for 40 bounded-query rules, the
red and blue trees of the product inequality (labels repeated where the
proof allows), check that their sizes multiply to more than $|\Lambda|$, that
no two demands on a bit disagree, and that every triple of the resulting
words has the claimed colour; they do the same with contexts for 12 prefix
rules, where the construction without contexts fails, and rebuild both
extreme cases and the sets for all 256 outsider tables over two seeds. They
do not check the universal statement.
