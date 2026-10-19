---
name: research/erdos_617/saturated_row_suppression
desc: Conditional clique-safe suppression and exact unit-row folding; folding preserves independence and any available budget, but may lose hereditary caps.
tags: [graph-theory, proved, private-cliques, reductions]
sources: []
created: 2026-09-22T05:15:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/saturated_row_suppression

***

**A proved conditional suppression theorem, not a proof that its hypotheses
can be forced.** Work in the normalized two-supported core from
[Two-support normalization](two_support_normalization.md):

$$
|H|=ar+1,\quad \alpha(H)=a<r,\quad \omega(H)\le r-1,
\quad |P_i|=r-d_i,\quad b=\sum_i d_i+1\le r.
$$

All $d_i\ge1$, and each support degree is at least $d_i+1$.

## 1. Saturation and outside-neighbor bounds

Choose a nonempty set $A$ of rows. For each $i\in A$, suppose a set
$S_i$ of $d_i$ incident exceptions each misses at most $h_i$ vertices
of $P_i$. Put

$$
Z_i=P_i\cup S_i,\quad
\mu_i=\binom r2-e(H[Z_i]),\quad
L_i=1+d_i h_i+\binom{d_i}{2}.
$$

Then $|Z_i|=r$ and $\mu_i\le L_i-1$. The local cap on
$Z_i\cup\{z\}$ gives

$$
e_H(z,Z_i)\le\mu_i+1\le L_i\qquad(z\notin Z_i). \tag{1}
$$

Assume $d_i\le k$ and $L_i\le L$ for $i\in A$, with

$$
r>k+3L. \tag{2}
$$


## 2. Unique clique-safe routing

If an exception $x$ is incident with $i\in A$ but is not in $S_i$,
route it to its other supporting row $j$. It is complete to $P_j$.
Indeed, its nonneighbors in $P_i$ number at least
$r-d_i-L_i>L_i$. If it missed $v\in P_j$, two-support augmentation
would force $v$ to be adjacent to all these vertices, contrary to (1).
If $j\in A$, completeness and $|P_j|>L_j$ force $x\in S_j$.
Consequently no exception is routed from both its endpoints.

Let $R_j$ consist of exceptions routed to $j$. Then

$$
P_j\cup R_j\text{ is a clique},\qquad
|R_j|\le d_j-1,\qquad c_j:=d_j-|R_j|\ge1. \tag{3}
$$

For pairwise adjacency, suppose $x,y\in R_j$ are nonadjacent.
If their sources coincide at $i$, their common nonneighbors in
$P_i$ have order at least $r-d_i-2L_i>0$ and augment $x,y$ with
the unused anchors. If their sources $i,\ell$ differ, their
common-nonneighbor lists in the two source rows have order greater
than $L$. They must be completely joined, by the same augmentation
argument. A private vertex of $P_i$ is outside $Z_\ell$, so (1)
makes this impossible. This proves the clique assertion; $K_r$-
freeness gives its capacity.

Writing $E=\sum_j(d_j-1)$, uniqueness gives

$$
\sum_{i\in A}(\deg_{\rm supp}(i)-d_i)=|R|\le E,
\qquad |A|\le E. \tag{4}
$$

Here $R$ is the union of the routed sets.

For the natural thresholds $h_i=\max(d_i,2)$ and $k\ge2$, one may
use

$$
L=L_k=\frac{3k^2-k+2}{2}.
$$

Thus $r\ge(9k^2-k+8)/2$ suffices for (2). Unit rows instead have
$k=1,L=3$, requiring $r\ge11$, exactly as in
[Unit-deficit propagation](unit_deficit_propagation.md).

## 3. The residual support identity

Remove the routed exceptions from the support multigraph. At each
$i\in A$ the remaining incident exceptions are precisely
$S_i\setminus R_i$, so its residual degree is $c_i$.
Put $U=[a]\setminus A$, $h=|U|$, and let $e_A,e_U$ count residual
support edges entirely inside $A,U$, respectively. The total residual
edge count is $\sum_jc_j+1$. Summing the residual degrees in $A$
therefore gives

$$
\boxed{e_U=\sum_{u\in U}c_u+1+e_A.} \tag{5}
$$

In particular $h\ge2$, since the support graph has no loops.

Consider the induced graph

$$
G_U=H\!\left[\bigcup_{u\in U}(P_u\cup R_u)
\ \cup\ (B\setminus R)_U\right].
$$

The last term contains only residual exceptions supported entirely
in $U$. Each enlarged private row $P_u\cup R_u$ is a clique;
relative to the retained anchors its vertices have singleton support.
Every other vertex has two retained anchor neighbors. Equation (5)
gives the exact order

$$
\boxed{|G_U|=hr+1+e_A>hr.} \tag{6}
$$

Counting alone does not give $\alpha(G_U)\le h$.

## 4. Safe simultaneous suppression

Set $s=h+\min(2,|A|)$. If

$$
r-d_i>sL_i\qquad(i\in A), \tag{7}
$$

then $\alpha(G_U)\le h$. This improves the earlier threshold
$h+\min(|A|,h)$ by using a minimal Hall-deficient subfamily.

Suppose $J\subseteq G_U$ is independent of order $h+1$. Give each
member its nonempty support list in $U$: a retained anchor and a
vertex of an enlarged private row have the corresponding singleton
list, and a residual exception has its two supporting anchors.
Choose an inclusion-minimal $C\subseteq J$ with more members than
indices in its union of lists. Put $V=\bigcup_{x\in C}L(x)$ and
$v=|V|$. Minimality implies $|C|=v+1$ and every index in $V$ occurs
at least twice: deleting a member containing a uniquely occurring
index would leave $v$ members on at most $v-1$ indices. If $\ell$
lists are singletons, then

$$
2v\le\sum_{x\in C}|L(x)|=2(v+1)-\ell,
\qquad \ell\le2.
$$

Only absorbed exceptions have original supporting anchors in $A$;
each has just one such source and has a singleton list in $U$.
Thus the set $T\subseteq A$ of original source anchors touched by
$C$ has size $t\le\min(2,|A|)$.

The set $C\cup(Q\setminus(V\cup T))$ is independent and has size
$a+1-t$. If $t=0$ this is already a contradiction. Otherwise replace
the $t$ touched anchors by greedy private representatives. Every
vertex of $G_U$ lies outside $Z_i$ for $i\in A$: a routed exception
retained in $U$ is outside the designation set of its unique source
and has no other support in $A$. Previously chosen private
representatives also lie outside $Z_i$. At each choice, $C$ and the
previous representatives form an independent avoiding set of size at
most $v+t\le h+\min(2,|A|)=s$, and forbid at most $sL_i$ vertices
of $P_i$. Retained anchors are automatically anticomplete to these
private representatives. Condition (7) therefore extends the set to
size $a+1$, a contradiction.

By (6), trim $G_U$ to $hr+1$ vertices while preserving the retained
anchors. Under (7) its independence is $h$; its singleton-support
classes remain cliques and its exceptional set is a subset of the
original $B$. This contradicts minimum-anchor normalization.
Consequently

$$
\boxed{r-k\le\bigl(h+\min(2,|A|)\bigr)L.} \tag{8}
$$

For a single saturated row, the exact necessary inequality is
$r-d_i\le aL_i$. In particular an active unit row requires
$3a\ge r-1$. If its designated exception misses only one vertex,
the stronger $2a\ge r-1$ holds.

## 5. An independent-set improvement

The already chosen outside vertices $T$ in the extension proof are
independent, disjoint from $Z_i$, and have order at most $s\le a<r$.
Since

$$
D_r(r+t)=\binom r2+\binom{t+1}{2}\quad(0\le t\le r),
$$

the hereditary cap on $Z_i\cup T$ yields

$$
e_H(Z_i,T)\le\mu_i+\binom{|T|+1}{2}.
$$

Thus the same suppression argument works under the weaker condition

$$
\boxed{r-d_i>
\min\!\left\{sL_i,\ \mu_i+\binom{s+1}{2}\right\}
\quad(i\in A).} \tag{9}
$$

This resolves the independence issue for the specified quantitative
range; it does not justify unrestricted deletion of saturated rows.
The routing, support identity, extension, trimming, and threshold
arithmetic were checked by the author against the written proof, as
were the minimal-Hall-subfamily improvement and its singleton-list
count; the argument is author-recorded.

## Remaining gap

The unsaturated remainder has not been forced into the range (7) or
(9). In particular, rows of deficit at least three may have fewer
than $d_i$ strongly incident exceptions while still accommodating
substantial support density. Neither (4) nor the residual identity
excludes this. No lower bound of order $\sqrt r$ on the average
deficit, and no resulting uniform or unrestricted infinite-family
proof, has been established.

## 6. Linear incidence bounds for independent outsiders

Let $|Z|=r$ and $e(H[Z])=\binom r2-\mu$. Define

$$
k=\max\{t\ge1:\binom t2\le\mu\},\qquad
\beta=\mu-\binom k2,\quad 0\le\beta<k.
$$

If $T$ is independent outside $Z$, with $k-1\le n=|T|\le r$, then

$$
\boxed{e(Z,T)\le kn+\beta.} \tag{10}
$$

Order the degrees into $Z$ as $d_1\ge\cdots\ge d_n$. The hereditary
cap on $Z$ and any first $t$ outsiders gives
$\sum_{j\le t}d_j\le\mu+\binom{t+1}{2}$. If $n\ge k$, this
forces $d_k\le k$: otherwise $\mu\ge\binom{k+1}{2}$.
Bound the first $k-1$ degrees by their cap and all subsequent degrees
by $k$. Their sum is at most $kn+\beta$. The same expression holds
for $n=k-1$; when $k=1$ the initial sum is empty.

Consequently, for $s\ge k-1$, every independent outsider set of size
at most $s\le r$ sends at most $ks+\beta$ edges into $Z$. For smaller
sets use the original quadratic cap and its monotonicity. Thus the
suppression criterion can use $k_i s+\beta_i$ in place of $sL_i$,
when $s\ge k_i-1$.

For an active unit block with two holes, $\mu=2$ gives
$e(Z,T)\le2|T|+1$ for nonempty independent $T$. Failure of single-row
suppression therefore requires $2a\ge r-2$, improving $3a\ge r-1$.
With only one hole it requires $2a\ge r-1$.

## 7. Sharper routing and clique safety

In Sections 1--3, the sufficient numerical condition (2) can be
replaced by

$$
\boxed{|P_i|>\mu_i+6\quad(i\in A).} \tag{11}
$$

Keep the original two-supported setup and $Z_i=P_i\cup S_i$.
Let $x\notin S_i$ be an exception incident with $i$, with other
endpoint $j$. If $z\in P_j$ misses $x$, the two-support argument
makes $z$ complete to $P_i\setminus N(x)$. The independent outsiders
$x,z$ therefore cover $P_i$ by their neighborhoods. The cap gives

$$
|P_i|\le e(Z_i,\{x,z\})\le\mu_i+3,
$$

a contradiction. Thus $x$ is complete to $P_j$. If $j\in A$, then
$x\in S_j$, since otherwise the one-outsider cap would give
$|P_j|\le\mu_j+1$. Routing is again unique.

Suppose two routed exceptions $x,y$ with common owner are nonadjacent.
If they have the same source $i$, their neighborhoods cover $P_i$;
otherwise a common private nonneighbor augments them and the unused
anchors. This contradicts the independent-pair cap just used.
For distinct sources $i,k$, the common nonneighbor sets

$$
A_i=P_i\setminus N(\{x,y\}),\qquad
A_k=P_k\setminus N(\{x,y\})
$$

are completely joined by augmentation. The independent-pair cap
ensures $A_k\ne\varnothing$. Choose $z\in A_k$. Now $x,y,z$ are
independent outsiders to $Z_i$, and their neighborhoods cover $P_i$.
Hence $|P_i|\le\mu_i+6$, again impossible. Thus all routed owner
groups are cliques, with the same capacities and support identity as
before. No independence-drop conclusion is implicit in (11).

## 8. Structural support peeling before the independence step

After routing from a fixed source set $A$, retain the rows in $U$,
the enlarged cliques $C_u=P_u\cup R_u$ of sizes $r-c_u$, and the
residual exceptions supported in $U$. Their support multigraph $M$
has excess

$$
\Delta=e(M)-\sum_{u\in U}c_u=1+e_A\ge1.
$$

If a retained row $v$ has $\deg_M(v)\le c_v$, delete its entire
enlarged clique and all incident residual exceptions. Then

$$
\Delta_{\rm new}=\Delta+c_v-\deg_M(v)\ge\Delta.
$$

Repeated deletion leaves a nonempty overloaded system, now with
support degrees at least $c_v+1$; it cannot become empty while
preserving positive excess.

A peeled original anchor is anticomplete to the final system.
Surviving private vertices belong to other rows; surviving absorbed
exceptions have a source in $A$ and their retained owner as original
supports; all residual exceptions incident to the peeled anchor were
deleted. Peeled anchors are also anticomplete to original private
representatives from source rows.

Thus the Hall suppression proof may use the **final** retained row
count $h$. Peeled rows are restored using their original anchors,
without additional avoidance cost. Performing this peeling asserts
no global independence bound on the residual; that bound still
requires the extension inequality.

## 9. A conditional weighted-greedy cancellation

Suppose source candidate cliques $C_1,\ldots,C_m$ have sizes $r-c_i$,
with $1\le c_i\le K$, and each is contained in an $r$-set $Z_i$
with missing-edge count at most $\binom{c_i}{2}$. Assume the residual
and all other candidate cliques lie outside $Z_i$. Suppose $h\ge K$
retained rows each have deficit at least $K+1$, and the total of all
source and retained deficits is at most $r-1$.

Then every independent residual $(h+1)$-set extends by one vertex
from every $C_i$. Order sources by decreasing $c_i$. Before choosing
from source $j$, there are $h+j$ independent outsiders. Applying
(10) with the upper missing count $\binom{c_j}{2}$ bounds their
forbidden vertices by $c_j(h+j)$. The deficit budget gives

$$
r-1\ge jc_j+h(c_j+1)\ge c_j(h+j+1),
$$

using $h\ge c_j$. Therefore $r-c_j>c_j(h+j)$, and the greedy
choice succeeds. All set sizes used are below $r$, since the positive
deficit budget bounds the number of rows by $r-1$.

Complete-owner completions meet this missing-edge hypothesis;
one-hole completions in general only give $\binom{c_i+1}{2}$ and
lose the exact cancellation. Sufficient complete-owner source blocks
have not been forced. Successive routing can also create dependencies
on earlier source rows, which this conditional lemma does not remove.

The independent-outsider bound, pair/triple routing proof, support
peeling, and conditional cancellation were separately checked. They
strengthen sufficient conditions, not unconditional suppression.

## Status of the attempted general low-deficit deletion

The subsequent attempt did not force the source blocks required above.
In particular, an inactive unit row can have every incident exception
complete to its **other** supporting row, without a proved near-full
completion at the source row. No existence of a counterexample with
this configuration is asserted; it is a case the deletion argument
does not exclude.

Routing such exceptions to their complete supporting rows is not enough:
the routed groups must be cliques, and the remaining graph must have
the required independence drop. Neither follows just from individual
completeness to a receiving row. After the established support peeling,
an unsaturated low-deficit row may still have too few strong incoming
incidences to fill its deficit and several outgoing incidences. The
global excess can remain supported on higher-deficit rows.

The [exact wedge identity](unit_deficit_propagation.md) forces many
nonadjacent incident pairs of exceptions. It does not make those pairs
simultaneously independent: their count alone does not yield an
independent support set with more edges than anchors. Thus this route
has not supplied an unconditional suppression or augmentation theorem.
The missing steps are clique-safe absorption for the unsaturated rows
and a justified independence drop, not another numerical cutoff.

## 10. Exact unit-row folding and its cap obstruction

The following operation avoids the independence-drop difficulty for a
specific row, but is **not** a valid induction in the capped class.
Let $H$ have order $ar+1$, maximum independent anchors
$Q=\{q_1,\ldots,q_a\}$, and one/two-support structure. Suppose a unit
private row $P=P_i$ has order $r-1$ and exactly two incident exceptions
$x,y$, which are nonadjacent. Thus $N_H[q_i]=P\cup\{x,y\}$.
Delete $P$ and identify $x,y$ to one vertex $z$, using the union of
their neighborhoods outside this deleted block. Call the simple graph
obtained $F$.

Then

$$
|F|=(a-1)r+1,\qquad \alpha(F)=a-1.
$$

An independent set avoiding $z$ extends in $H$ by $q_i$. One containing
$z$ lifts by replacing it with the independent pair $x,y$, also gaining
one vertex. The retained anchors attain the upper bound.

If the original supports are $\{i,j\}$ and $\{i,k\}$, the new support
of $z$ is $\{j,k\}$ when $j\ne k$, and $\{j\}$ otherwise. No other
vertex loses an anchor neighbor. The new singleton classes are cliques,
by augmentation of the retained maximum anchor set. The exception count
decreases by one in the first case and by two in the second. In
particular an available bound $b\le r$ survives. In the parallel case,
$x,y$ jointly dominate $P_j$, so its enlargement by $z$ is a clique.

### Exact budget calculation

Put $R=H-(P\cup\{x,y\})$ and

$$
S=\sum_{u\in P}(d_H(u)-r),\qquad
C=|N_H(x)\cap N_H(y)\cap R|.
$$

The edges incident with $P$ number
$r(r-1)+S-\binom{r-1}{2}$. Folding the remaining nonadjacent pair
loses exactly $C$ more edges. Thus

$$
\boxed{e(H)-e(F)=\binom r2+(r-1)+S+C.} \tag{12}
$$

If the private vertices of $P$ have degree at least $r$, then $S\ge0$.
If $H$ additionally has the least-core budget
$E_r(a)=a\binom r2+r(r+1)/2$, equation (12) gives

$$
e(F)\le E_r(a-1)-(r-1)-S-C.
$$

Equivalently, the change of the established potential is
$-2(r-1+S+C)$. This transfers a budget when it is present; it does not
give one to the separately normalized bounded-exception core.

### The exact missing cap inequality

Let $m_x,m_y$ count the respective nonneighbors of $x,y$ in $P$, and set

$$
\lambda=m_x+m_y-(r-2)\ge0.
$$

The nonnegativity follows from the cap on
$Z=P\cup\{x,y\}$, whose edge count is $D_r(r+1)-\lambda$.
For $T\subseteq R$ put

$$
A(T)=e_H(P,T),\qquad C(T)=|T\cap N_H(x)\cap N_H(y)|.
$$

The exact identity
$D_r(s+r)=D_r(s)+\binom r2+s$, applied to $Z\cup T$, gives

$$
\boxed{e_F(T\cup\{z\})\le
D_r(|T|+1)+|T|+\lambda-A(T)-C(T).} \tag{13}
$$

Sets not containing $z$ inherit their caps. The error in (13) is the
remaining issue.

For parallel supports, the nonneighbor sets of $x,y$ in $P$ are
disjoint: otherwise those three independent vertices replace the two
supporting anchors. They also exclude $q_i$, giving
$m_x+m_y\le r-2$ and hence $\lambda=0$.
The saturated $(r+1)$-set $Z$ then gives, for every outsider $v$,

$$
d_H(v,P)+\mathbf1_{vx\in E(H)}+\mathbf1_{vy\in E(H)}\le2.
$$

These facts do not prove $A(T)+C(T)\ge|T|$ for the sets that could
violate a new cap. Untouched anchors, for example, contribute zero.
No full-cap preservation or exclusion of newly created $K_r$'s has
been proved under the normalized-core hypotheses.

### Why caps and the deleted row's degree alone do not suffice

Here is a counterexample to a weaker folding rule, for every $r\ge5$.
It is **underloaded and contains full $K_r$'s**, so does not refute a
folding theorem using all the normalized-core assumptions.

Start with disjoint cliques $C_1,C_2$, each of order $r$.
Choose distinct $q_i,x\in C_1$ and distinct $y,q_j,t\in C_2$.
Between the cliques put a matching consisting of $q_i y$ and a
bijection from $C_1\setminus\{q_i,x\}$ to
$C_2\setminus\{y,q_j\}$. Add $w$ with precisely the neighbors $x,t$.
The anchors $\{q_i,q_j,w\}$ are maximum independent; each clique
contributes at most one vertex to any independent set. The exceptions
are exactly $x,y,t$, and $P_i=C_1\setminus\{x\}$ is a unit row whose
vertices all have degree $r$. Its only incident exceptions are the
nonadjacent pair $x,y$.

All hereditary caps hold. For a set with occupancies $u,v\le r$ in
the two cliques and without $w$, only $u+v>r$ is nontrivial.
The cap allows

$$
(r-u)(r-v)+(u+v-r)\ge\min(u,v)
$$

cross edges, enough for its matching.
For a set also containing $w$, with $r\le u+v\le2r-1$ and
$1\le u\le v$, put $A=r-u$, $B=r-v$. The permitted number of
edges beyond the two clique interiors is
$AB+2(u+v-r)+1$. This is at least $u+2$, because the difference is

$$
B(A-2)+u-1\ge0.
$$

For $A\ge2$ this is immediate; for $A=1$, use $B\le1$ and $r\ge5$.
If an occupancy is zero, the only nontrivial case is a whole clique
plus $w$, with only one incident edge from $w$. Finally the entire
$2r+1$-vertex graph has $r^2+1<D_r(2r+1)=r^2+2$ edges.

After folding $P_i,x,y$, the set
$(C_2\setminus\{y\})\cup\{z\}$ is a $K_r$, and $w$ has its two distinct
neighbors $z,t$ in it. Its union with $w$ violates the $(r+1)$-set cap.
Thus hereditary caps, one/two-support, and minimum degree $r$ on the
deleted row do not by themselves justify union folding. These weaker
hypotheses do not suffice; a valid repair must use additional assumptions.
The example does not show which of the omitted core hypotheses is decisive.

## 11. Parallel supports: induced deletion and a receiving-row charge

**Proved under the minimum-anchor normalized hypotheses.** In the unit
configuration of Section 10 suppose both exceptions have support
$\{i,j\}$. Write $m_x=|P_i\setminus N(x)|$ and similarly
$m_y$. As established there,

$$
m_x+m_y=r-2,\qquad
d(v,Z)\le2\quad(v\notin Z),\qquad
Z=P_i\cup\{x,y\}.
\tag{14}
$$

If $m_x\ge2a-2$, deleting $P_i\cup\{y\}$ reduces
independence to $a-1$. This is an ordinary induced deletion,
so all caps survive. For suppose the residual has an independent
$a$-set. It must have the form $\{x\}\cup J$, since a set
avoiding $x$ could be augmented by $q_i$. The set $J$
must dominate all $m_x$ holes of $x$ in $P_i$, and must
have a neighbor of $y$, as $x,y$ are nonadjacent. Therefore

$$
m_x+1\le e(J,Z)\le2|J|=2a-2,
$$

a contradiction. The other $a-1$ anchors remain maximum, and
one/two-support and any bound $b\le r$ persist. Minimum-anchor
normalization thus forces

$$
m_x,m_y\le2a-3,\qquad \boxed{r\le4a-4}. \tag{15}
$$


There is also an exact pointwise charge on the receiving row:

$$
\boxed{d(v,P_i)+\mathbf1_{\{vx,vy\in E(H)\}}=1
\quad(v\in P_j).} \tag{16}
$$

Both hole sets in (14) are nonempty, since completeness to the unit
row would create a forbidden $K_r$. Every $v\in P_j$ sees at
least one of $x,y$, or else $x,y,v$ and the unused anchors
are independent of order $a+1$. If it sees both, (14) forces
$d(v,P_i)=0$. If it sees only $y$, two-support augmentation
makes it complete to $P_i\setminus N(x)$; (14) then forces that
hole set and its neighborhood in $P_i$ both to have size one.
The remaining case is symmetric, proving (16).

In all cases $d(v,Z)=2$. The private-set expansion from
[Unit-deficit propagation](unit_deficit_propagation.md), applied to
the independent pair $q_i,v$, now gives

$$
2r+1\le|N[q_i]\cup N[v]|=(r+1)+(d(v)+1)-2,
$$

and consequently

$$
\boxed{d(v)\ge r+1\quad(v\in P_j),\qquad
\deg_{\rm supp}(j)\ge d_j+2.} \tag{17}
$$

If both hole sets have size at least two, the preceding proof also
shows that both exceptions are complete to $P_j$, while $P_i$
is anticomplete to $P_j$.

These conclusions localize the fold's possible cap error outside the
two supporting rows and give a whole row of positive private surplus.
They do not prove cap preservation for the fold or exclude every
parallel configuration.
