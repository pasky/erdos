# The claim under acceptance

The first two paragraphs of the **Claim.** section of `wiki/problems/set_theory/E0111/claims/2026_10_17_plasma_ai.md` as it stood on 2026-10-18: the limit the claim asserts and the countable-coloring theorem it goes through. Links are shown as they appear in the source.

**Claim.** For every simple graph $G$ with $\chi(G)=\aleph_1$, whatever
the cardinality of its vertex set,

$$
\forall K>0\ \exists N\ \forall n\ge N:\qquad h_G(n)>Kn,
$$

so $h_G(n)/n\to\infty$. Here $h_G(n)$ is the least bound in the Statement
of [[problems/set_theory/E0111/_index|Problem 111]], the largest number of
edge deletions that an $n$-vertex subgraph of $G$ needs to become
bipartite; every admissible bound is at least this one. The threshold $N$
may depend on $G$ and $K$. The second question of the Statement therefore
has a positive answer.

The proof goes through a countable-coloring theorem: for every finite
$C\ge0$, every graph each of whose finite subgraphs $F$ can be made
bipartite by deleting at most $C|V(F)|$ edges has countable chromatic
number, at every vertex cardinality, singular cardinals included.
Deleting countably many vertices from a graph of chromatic number
$\aleph_1$ leaves chromatic number $\aleph_1$, so the theorem yields
$\aleph_1$ pairwise vertex-disjoint finite subgraphs $F$ each needing more
than $2K|V(F)|$ deletions. One isomorphism type recurs uncountably often,
and packing its copies gives $h_G(n)>Kn$ for every large $n$.

