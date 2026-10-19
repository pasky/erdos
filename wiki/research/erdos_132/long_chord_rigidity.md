---
name: research/erdos_132/long_chord_rigidity
title: Two consecutive long-diagonal families force regularity
desc: |
  An odd convex polygon with uniform lengths in its two longest
  cyclic separation classes is regular; richness has not forced this pattern.
sources: []
research_state: closed
created: 2026-09-22T23:35:00Z
updated: 2026-09-24T22:12:56Z
---


# Two consecutive long-diagonal families force regularity

***

**Lemma.** Let $n=2m+1\ge5$, and let $p_0,\ldots,p_{n-1}$ be
the vertices of a strictly convex polygon in counterclockwise order.
If, for every $i$,

$$|p_{i+m}-p_i|=a,\qquad |p_{i+m-1}-p_i|=b,$$

then the polygon is regular. Indices are modulo $n$.

These are the two largest **cyclic separations**, not an assumption
that they are already the two largest numerical distances.

**Proof.** Let $\varepsilon_i\in(0,\pi)$ be the angle at $p_i$
between the rays to $p_{i+m}$ and $p_{i+m+1}$. Consider the $n$
triangles $(p_i,p_{i+m},p_{i+m+1})$. At a given vertex, its two
appearances as a base vertex contribute its polygon interior
angle plus $\varepsilon_i$: their angular intervals cover the
interior angle and overlap precisely in $\varepsilon_i$.
Adding their angles, including the apex appearances, gives

$$n\pi=(n-2)\pi+2\sum_i\varepsilon_i,
\qquad\sum_i\varepsilon_i=\pi. \tag{1}$$

Reindex by $q_j=p_{mj}$. This visits every vertex because
$\gcd(m,n)=1$. Its consecutive edges all have length $a$, and
its three-step chords all have length $b$, since
$3m\equiv m-1\pmod n$. Its positive turns $\delta_j$ are the
numbers $\pi-\varepsilon_i$ in permuted order. Thus

$$0<\delta_j<\pi,\qquad \sum_j(\pi-\delta_j)=\pi. \tag{2}$$

Expanding the squared length of three successive edges gives

$$
F(\delta_j,\delta_{j+1})=b^2/a^2,
\quad F(x,y)=3+2\cos x+2\cos y+2\cos(x+y).
$$

Subtracting consecutive equations and dividing by
$4\cos(\delta_{j+1}/2)>0$ yields

$$
\cos(\delta_j+\delta_{j+1}/2)
=\cos(\delta_{j+2}+\delta_{j+1}/2).
$$

The angle ranges imply either $\delta_j=\delta_{j+2}$ or
$\delta_j+\delta_{j+1}+\delta_{j+2}=2\pi$. The latter would
make three of the positive quantities $\pi-\delta_j$ sum
to $\pi$, contradicting (2), since $n\ge5$ leaves other
positive terms. The turns are therefore two-periodic. Since
$n$ is odd, all turns are equal, necessarily $2\pi m/n$.
Equal edge lengths and equal turns make $q$ a regular star
polygon; its vertex set, and hence the original polygon, is
regular. $\square$

## Scope and remaining gap

The author checked the angle-sum identity, star orientation, the
cosine alternatives, and the odd-period argument; the argument is
author-recorded. No premise
here follows from merely having many rich distance classes.
In particular, richness has not supplied spanning cycles with
these prescribed cyclic separations. This lemma therefore does
not resolve either unrestricted question in
[Problem 132](../../problems/distance_problems/E0132/_index.md).

The [constant-width inverse theorem](constant_width_inverse.md)
uses a related local isometry-propagation mechanism, but obtains
its compatible rows only under a bounded distance-count excess
on a constant-width boundary.

The parity restriction cannot be removed. The
[even-order deformation construction](second_distance_extremality.md)
has both largest cyclic separation classes uniform, attains the exact
$3N/2$ second-distance bound after adding its inner points, and has no
five concyclic points. Thus extracting those two families at even order
would not prove circularity.
