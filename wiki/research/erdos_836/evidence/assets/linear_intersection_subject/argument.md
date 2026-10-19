[cut]

that for $r\ge2$ every $r$-uniform intersecting hypergraph $G$ with
$\chi(G)=3$ has two distinct edges $E,F$ with

$$
|E\cap F|\ge\left\lfloor\frac r2\right\rfloor,
$$

and that the same holds for every $r$-uniform intersecting hypergraph that is
not properly $2$-colorable. So some two edges meet in $\gg r$ vertices, and
the second question has the answer yes. The proof passes by compactness to a
finite subhypergraph $H$ that is not $2$-colorable and is minimal under edge
deletion, fixes an edge $A$, and takes a proper red–blue coloring of
$H\setminus\{A\}$ in which $A$ is red and the blue vertices are fewest.
Recoloring a vertex $x\in A$ blue then gives an edge $F_x$ that meets $A$ only
in $x$ and is otherwise blue, and recoloring a blue vertex $b$ red gives an
edge $G_b$ whose only blue vertex is $b$. With $t$ the largest intersection
of two edges of $H$, the intersecting property puts each such $b$ in at least
$r-t$ of the sets $F_x\setminus\{x\}$, and counting
$\sum_{y\in A\setminus\{x\}}|F_x\cap F_y|$ in two ways gives
$(r-1)t\ge(r-1)(r-t-1)$, so $2t\ge r-1$. The note also observes that a star
whose edges meet only at its center refutes the statement when the
parenthetical condition is read as $3$-colorability alone, the literal
reading that the problem page's Notes set aside.

[cut]

**Covers.** The second question of the modified Statement, with chromatic
number exactly $3$: some two edges meet in at least $\lfloor r/2\rfloor$
vertices, a linear bound in place of the $r/\log r$ of Erdős, Lovász and
Shelah.

[cut]

**Depends on.** No page of this wiki; the note proves the compactness lemma
it uses and is otherwise self-contained.

[cut]
