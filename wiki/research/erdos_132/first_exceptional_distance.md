---
name: research/erdos_132/first_exceptional_distance
title: First exceptional length and triangular-lattice propagation
desc: |
  A complete lattice patch propagates up to the first nonlattice length;
  in a one-rare sequence that length has unbounded rank from both ends.
sources: []
research_state: closed
created: 2026-09-23T04:40:00Z
updated: 2026-09-24T22:12:56Z
---


# First exceptional length and triangular-lattice propagation

***

**Subsequent strengthening.** The
[translated-triangle theorem](translated_triangles.md) shows that the
first exceptional length must eventually exist along any hypothetical
unbounded $R=1$ sequence. If every normalized squared distance were a
triangular-lattice norm, distances to a good equilateral triangle would
put all points in a common mesh-one lattice, contrary to the new
orientation bound. The finite propagation lemma below retains its
stated conditional hypothesis.

The first lemma is an exact finite statement. Its subsequent asymptotic
consequences assume the hypothetical $R=1$ sequence studied in
[one_rare_asymptotics](one_rare_asymptotics.md). Neither assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md) is resolved.

## Closed-ball propagation

Normalize the minimum distance to one, and put

$$\mathcal N=\{\sqrt{a^2+ab+b^2}:a,b\in\mathbb Z, (a,b)\ne(0,0)\}.$$

Suppose $d=\min(D(A)\setminus\mathcal N)$ exists. A point $p$ is a
patch center if $A$ contains the complete triangular-lattice graph ball
of radius two about $p$, in some mesh-one triangular lattice $\Lambda_p$.
Then

$$A\cap\overline B(p,d)\subseteq\Lambda_p. \tag{1}$$

Translate $p$ to zero. For $x\in A$ with $1<t=|x|\le d$, choose
adjacent unit lattice vectors $u,v$ bracketing its direction. They satisfy

$$x\cdot u,x\cdot v\ge t/2>1/2,
\qquad x\cdot(u+v)\ge3t/2>3/2.$$

Since $|u|=|v|=1$ and $|u+v|^2=3$, the distances from $x$ to
$u,v,u+v$ are all strictly less than $t$. They therefore have integer
squares $s_u,s_v,s_{u+v}$; a possible zero distance causes no problem.
The identity

$$|x|^2=s_u+s_v-s_{u+v}+1$$

makes $|x|^2$ an integer. It follows also that
$U=2x\cdot u$ and $V=2x\cdot v$ are integers. Now

$$3|x|^2=U^2-UV+V^2\equiv(U+V)^2\pmod3.$$

Consequently $U+V\equiv0\pmod3$, and

$$x=\frac{2U-V}{3}u+\frac{2V-U}{3}v\in\Lambda_p.$$

The cases $|x|=0,1$ follow from the patch, because minimum separation
one and its six unit neighbors exclude any other unit neighbor. There
are no distances in $(0,1)$. This proves (1), without a bounded-rank
hypothesis or a margin below $d$.

Two consequences will be useful if a global palette argument is found.
First, if $|x-y|=d$, then

$$\overline B(x,d)\cap\overline B(y,d)$$

contains no patch center. Otherwise (1) would put both endpoints in one
triangular lattice, contradicting $d\notin\mathcal N$.

Second, two patch centers $p,q$ with $|p-q|<d$ have the same lattice.
Choose a unit neighbor $z$ of $q$ pointing within $\pi/6$ toward $p$.
Minimum separation gives $|p-q|\ge1$, so

$$|z-p|^2\le |q-p|^2+1-\sqrt3|q-p|<|q-p|^2<d^2.$$

Both $q,z$ belong to $\Lambda_p$. Their unit difference determines
the orientation of a mesh-one triangular lattice, so
$\Lambda_q=\Lambda_p$. The point $z$ need not itself be a patch center.

## The first exceptional length is not near either end of the spectrum

Suppose $n\to\infty$ with $R(A)=1$, and let $d$ exist as above.
The established exact bounded-window spectrum already makes its
smallest-distance rank tend to infinity. Its **largest-distance rank
also tends to infinity**.

Fix $k$, write $r_k$ for the $k$-th largest distance, and let $B_k$
be the union of the first $k$ convex layers. The checked layer-depth
bound in [layers_and_obstructions](layers_and_obstructions.md) says that
every edge of length at least $r_k$ has both endpoints in $B_k$.
There is a unit equilateral triangle entirely outside $B_k$: almost
$n/3$ interior points are degree-six lattice vertices, while the fixed
layers after the second contain only $o(n)$ points, whose unit-distance
neighborhood also has only $o(n)$ points. For $k=1,2$ the same triangle
can be chosen outside $B_2$.

All distances incident with this triangle are strictly smaller than
$r_k$. If $d\ge r_k$, their squared values are integers. Integer
squared distances to a unit equilateral triangle force a point into
its triangular lattice: translate one vertex to zero and apply the
same $U,V$ calculation above, now using the integer squared distance
to zero directly. Thus every point of $A$ would belong to one lattice,
contradicting occurrence of $d$. Hence $d<r_k$ eventually for every
fixed $k$.

This conclusion is conditional on existence of a nonlattice distance;
it does not exclude a set lying entirely in a triangular lattice.

## A growing deficit in the global palette

Another consequence of the checked shell formula is

$$\frac n2-q(A)\longrightarrow\infty \qquad\text{if }R(A)=1, n\to\infty.
\tag{2}$$

Fix $M$. The $M$ distinct lattice lengths
$2^j\sqrt7$, $0\le j<M$, each have at least twelve lattice-vector
representations. At each of these fixed lengths the shell formula gives
at least $(2-o(1))n$ unordered pairs. These are not the diameter for
large $n$. Every other nondiameter class has at least $n+1$ pairs,
and the diameter has at least one. Consequently

$$\binom n2\ge1+(q(A)-1)(n+1)+M(n-o(n)),$$

and therefore $q(A)\le n/2-M+o(1)$. Since $M$ was arbitrary, (2)
follows. This is stronger than the elementary bound $q(A)\le n/2$,
but remains compatible with $q(A)$ of order $n$.

## What is not proved

The first exceptional graph avoids the large deep core but can still
have its edges on the approximately $2n/3$ outer points. Its empty
lenses alone do not bound its multiplicity by $n$. Even for a strictly
convex set, having an interior point outside all such lenses does not
force its length-$r$ graph to have at most as many edges as vertices.
The [minimum-graph construction](minimum_graph_obstruction.md) already
provides counterexamples to that proposed geometric shortcut.

For example, a universal estimate $m_A(r_2)\le2q(A)+C$ with an absolute
constant $C$ would contradict (2) along an $R=1$ sequence. No such
estimate is proved here. The tempting value $C=2$ is false: the odd
regular two-ring construction on ten points has $q=6$ and second-distance
multiplicity $15$. No inference from this suggested estimate, the
empty lenses, or the local lattices to either target assertion is made.

The author checked the closed-ball arithmetic, the nearby-center
argument, the two-sided rank conclusion, and the pair-budget deduction;
the argument is author-recorded. The underlying shell and layer results retain
their precise hypotheses in their linked notes.
