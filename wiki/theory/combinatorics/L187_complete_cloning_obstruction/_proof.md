---
name: theory/combinatorics/L187_complete_cloning_obstruction/_proof
desc: The transversal product formula, seven Fano-cap spectra and seven distinct parity rows prove the complete-cloning obstruction.
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# theory/combinatorics/L187_complete_cloning_obstruction/_proof

***

Use the conventions of [[theory/combinatorics/L187_complete_cloning_obstruction/_index|L187]].
Write $k'=ks$, $\tau=\tau(\mathcal H)$ and $\tau'=\tau(\mathcal C(\mathcal H))$.
A selected set of clone points covers every expanded edge if and only if
the original points whose classes contain at least $N-s+1$ selected
clones form a transversal of $\mathcal H$. If these original points miss
an edge, choose an $s$-subset avoiding the selection in each of that edge's
classes. Conversely, an edge meeting one of the specified classes cannot
avoid the selection. Therefore

$$
k'=ks,\qquad \tau'=(N-s+1)\tau.
$$

## A repeated-edge obstruction for each individual seed

Consider the complete clone-class operation defined on the claim card. If the seed is
nonempty and has no empty edge, then

$$
N\ge7\lceil s/4\rceil
\quad\Longrightarrow\quad
\text{its complete clone-class expansion fails }P_7. \tag{*}
$$

To prove this, index seven rows by the points of the Fano plane. The
complements of its seven lines are four-point caps. Each row index belongs
to four caps, and two caps never cover all seven row indices, since two
lines intersect. Put $h=\lceil s/4\rceil$. In each clone class, take $h$
copies of each cap as the incidence spectra of $7h$ clone points; any
remaining clone points have empty spectrum. Every row initially has $4h$
points in the class. Delete memberships until each row has exactly $s$
points. Every surviving spectrum is a subset of a cap, so no two spectra
cover all seven rows, even when the points come from different classes.

Fix one nonempty seed edge $E$ and make these same choices in every class
indexed by $E$. The resulting seven rows are edges of the expanded family.
No two clone points meet them all. If some rows coincide, delete duplicates;
covering the distinct rows is equivalent to covering the original list.
Thus a subfamily of at most seven distinct edges has no two-point
transversal, proving (*). Under an exactly-seven convention, this also
witnesses failure whenever the expanded family has at least seven edges,
by extending that subfamily. In (*) it does have at least seven: already
the choices in one nonempty class give $\binom Ns\ge7$.

Consequently a $P_7$ expansion must have $N<7\lceil s/4\rceil$. Combining
this with the exact transversal formula above gives the necessary bound

$$
\frac{\tau'}{k'}
\le\frac\tau k\left(\frac34+\frac{21}{4s}\right). \tag{**}
$$

Here $N,s$ are integers, so $N-s+1\le7\lceil s/4\rceil-s$, and
$\lceil s/4\rceil\le(s+3)/4$. Unlike the universal preservation criterion,
(*) applies to each fixed seed individually.

For the parity family on the claim card, $k=4q$ and $\tau\le3q+1$:
$V\setminus X$ is a transversal, since every edge meets $X$ oddly and
has even size $4q$. Thus $\tau/k\le31/40$ for $q\ge10$.
Already (**), for every $P_7$ complete clone-class expansion with $s\ge25$,
gives

$$
\frac{\tau'}{k'}\le
\frac{31}{40}\left(\frac34+\frac{21}{4s}\right)<\frac34.
$$

There is a stronger parity-specific obstruction covering the small clone
sizes too:

$$
3N\ge4s
\quad\Longrightarrow\quad
\text{the parity seed's complete clone-class expansion fails }P_7. \tag{***}
$$

Construct seven seed edges indexed by $\mathbb Z/7\mathbb Z$. Start with
$q$ vertices of each of seven types $j$, whose incidence spectra are
$C_j=\{j,j+1,j+2,j+3\}$ modulo seven, and one extra vertex. Every row
initially has $4q$ vertices. Choose a set $X$ of $4q$ of the typed vertices
as follows: choose one vertex each of types $0$ and $4$, and an even number
of vertices of each other type. This is possible because the remaining
$4q-2$ is even and
$4q-2\le10\lfloor q/2\rfloor$ for $q\ge3$; each of the five even counts
can range from zero to $2\lfloor q/2\rfloor$.

Before further modification, row zero has even intersection with $X$, and
the other six rows have odd intersection: modulo two the selected spectra
are $C_0$ and $C_4$, whose symmetric difference consists of those six rows.
Remove row zero from the spectrum of the chosen type-zero vertex, and give
the extra vertex spectrum $\{0\}$. Row sizes remain $4q$, and now every
row meets $X$ oddly. These are seven distinct edges of the parity family on
$7q+1$ vertices. Every vertex occurs in at most four of them. The chosen
$X$ has the prescribed size, so relabeling realizes
the same tuple for any specified set $X$ of that size.

If $3N\ge4s$, four $s$-subsets of an $N$-point class can have empty
intersection: their four complements have size $N-s$ and can cover the
class because $4(N-s)\ge N$. To construct them, partition the class into
four parts of size at most $N-s$, and enlarge each part to that size.
At every vertex appearing in four of the seed rows, use these four
$s$-subsets for the four corresponding expanded rows. At the other vertices
use arbitrary $s$-subsets. Every clone point then occurs in at most three
of the seven expanded rows. Two points cover at most six rows. This proves
(***), and the seven rows remain distinct because their projections are
the seven distinct seed edges.

Thus any $P_7$ complete clone-class expansion of this parity seed must have
$N<4s/3$, and its ratio obeys

$$
\frac{\tau'}{k'}\le
\frac{3q+1}{4q}\frac{\lceil s/3\rceil}{s}.
$$

For $s\ge2$, $\lceil s/3\rceil/s\le1/2$, so this ratio is at most
$31/80<3/4$. For $s=1$, the necessary condition forces $N=1$, the unchanged
seed. Hence no nontrivial complete clone-class substitution of a parity seed
preserves both $P_7$ and its ratio above $3/4$.
