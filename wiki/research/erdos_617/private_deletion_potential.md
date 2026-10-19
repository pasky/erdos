---
name: research/erdos_617/private_deletion_potential
desc: All-deficit potential-safe private deletion, with full private minimum degree through square-root deficits when exceptions are bounded.
tags: [graph-theory, proved, potential, private-cliques]
sources: []
created: 2026-09-22T14:00:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/private_deletion_potential

***

**A proved partial normalization rule, not a full normalization theorem.**
The common budgeted two-supported residue in
[Critical components](critical_component_reduction.md) cannot use
low-private-degree deletion directly: its exceptions may have still
smaller degrees. The following argument closes this issue for rows of
deficit at most three without imposing any lower degree on exceptions.
The all-deficit refinement below incorporates the potential gained in
trimming: it gives a degree lower bound in every row, and, when $b\le r$,
full private minimum degree through deficits of order $\sqrt{2a}$.

Suppose $J$ is $K_r$-free, $r\ge4$, with

$$
|J|=ar+1,\qquad \alpha(J)=a,
$$

and a maximum independent anchor set $I=\{q_1,\ldots,q_a\}$ such that
every outside vertex has one or two anchor neighbors. Write its private
cliques as $P_i$, with $|P_i|=r-d_i$, and let $b$ count the two-supported
exceptions. Then $b=1+\sum_i d_i$. A bound $b\le r$, if available,
is retained by the operation below.

Use the usual potential

$$
\Phi(J,a)=2e(J)-(2r-1)|J|+r^2a.
$$

Choose a vertex $v$ of minimum degree **within its private row** $P_i$.
Put

$$
|P_i|=r-k=:p,\qquad d_J(v)=r-t-1\le r-1.
$$

Since $v$ sees its entire row, $0\le t\le k$. Let

$$
X=N_J[v]\setminus P_i,\qquad |X|=k-t=:f.
$$

Then deletion of $N[v]$, together with lowering the independence
parameter by one, changes the potential by at most

$$
\boxed{\Delta\Phi\le-
\bigl[k(3-k)+t(2k-3)+2e(J[X])\bigr].} \tag{1}
$$

In particular it does not increase the potential when $k\le3$.

## Incident-edge count

The closed neighborhood contains no anchor other than $q_i$:
$v$ is private to that anchor. Every $x\in X$ has a neighbor among
the other anchors, all of which are outside $N[v]$. This is true
whether $x$ is an exception or a private vertex of another row.
Writing $E_{\rm inc}$ for the number of edges with at least one
endpoint in $N[v]$, minimum degree within $P_i$ gives

$$
\begin{aligned}
\sum_{z\in N[v]}d_J(z)
&\ge p(r-t-1)+e(P_i,X)+2e(X)+f,\\
E_{\rm inc}
&=\sum_{z\in N[v]}d_J(z)-e(J[N[v]])\\
&\ge p(r-t-1)-\binom p2+f+e(X).
\end{aligned} \tag{2}
$$

No degree lower bound on $X$ other than its displayed incident edges
is used. Since $|N[v]|=r-t$, the potential change is

$$
-2E_{\rm inc}+(2r-1)(r-t)-r^2.
$$

Substituting (2) and $p=r-k$, $f=k-t$ gives exactly (1).
For $k=1,2,3$, the bracket is respectively

$$
2-t+2e(X),\qquad 2+t+2e(X),\qquad 3t+2e(X),
$$

all nonnegative in $0\le t\le k$.

## Preserving supports and trimming the surplus

The remaining graph has order $r(a-1)+t+1$, independence at most
$a-1$, and retains the other $a-1$ anchors. Thus its independence
number is exactly $a-1$. Every survivor retains one or two anchor
neighbors. A private vertex from row $i$ cannot survive, and an
exception losing $q_i$ retains its other anchor. Singleton-support
classes are cliques by maximum-set augmentation. The new two-supported
exception set is a subset of the old one.

If $t>0$, trim to $r(a-1)+1$ while retaining these anchors. The
anchor-preserving trimming lemma in
[Critical components, Section 7](critical_component_reduction.md)
applies because the graph is $K_r$-free: whenever its order exceeds
$r(a-1)+1$, some nonanchor vertex has degree at least $r+1$.
Deleting it lowers $\Phi$ by at least three. For completeness, if
all nonanchor degrees were at most $r$, their induced graph would
have maximum degree at most $r-1$ and contain no $K_r$. Brooks's
theorem would make it $(r-1)$-colorable, contradicting its order
greater than $(a-1)(r-1)$ and independence at most $a-1$.

Thus a low-degree private vertex in a row of deficit at most three
can be deleted with a decrease in the anchor parameter while retaining
the original potential upper bound, hereditary caps, and any original
bound $b\le r$.

## Consequence and precise limitation

Choose a minimum-anchor member within a nonempty class satisfying these
hypotheses and a fixed potential upper bound. Every private vertex in a row of
deficit at most three then has degree at least $r$. In particular its unit-row
anchors have degree at least $r$. For $r\ge12$, the strengthened scope of
[Maximum-set surplus](maximum_set_surplus.md) therefore applies, even if
higher-deficit rows still contain low-degree vertices. If $b\le r$, then
two-support gives $\sigma=E+2$, where $E=b-a-1$, and the surplus inequality
yields

$$
9a\le7r-5.
$$

Unlike unrestricted minimum-anchor normalization, this partial
normalization retains the potential bound as well.

The general sign in (1) is not always favorable. For example $k=4$,
$t=0$ requires additional incident-edge cost. The refinements below
partially address this, but do not establish minimum degree $r$ on
every private row or supply the still-missing $b\le r$ in an arbitrary
least-budget residue.

The incident-edge count, polynomial identity, support preservation,
and trimming hypotheses were checked by the author and are
author-recorded. No computation is used.

## All-deficit normalization using the trimming gain

Retain $k,p,t,X,f$ above, and put $R=J-N[v]$ and

$$
S=\sum_{z\in P_i}(d_J(z)-d_J(v)),\qquad U=e(X,R)-f.
$$

Both are nonnegative: rowwise minimality gives $S\ge0$, and every
$x\in X$ retains an anchor neighbor in $R$, giving $U\ge0$.
The incident-edge count is exactly

$$
E_{\rm inc}=\binom p2+pf+S+e(X)+e(X,R),
$$

since the total degree from $P_i$ to its outside is $pf+S$.
The $t$ anchor-preserving trimming deletions each gain at least three
in the potential. Incorporating them in (1) gives

$$
\boxed{\Delta\Phi_{\rm final}\le-
[k(3-k)+2kt+2e(X)+2S+2U].} \tag{3}
$$

In particular deletion is safe whenever

$$
t\ge\max\{0,\lceil(k-3)/2\rceil\}. \tag{4}
$$

The support, cap, and exception-count preservation proof is unchanged. If
connectedness and criticality are wanted, prune and extract an overloaded
component as in [Critical components](critical_component_reduction.md); this
cannot restore the deleted anchor parameter.

Consequently a minimum-anchor member of the common budgeted class can
be assumed to satisfy, for every private vertex,

$$
\boxed{d_J(v)\ge r-\theta(d_i),\qquad
\theta(k)=\max\{0,\lfloor(k-2)/2\rfloor\},\quad v\in P_i.} \tag{5}
$$

Indeed, a smaller row minimum would have $t\ge\theta(k)$, exactly
the integer threshold in (4), permitting another reduction.
For deficits $1,2,3,4,5,6,7,\ldots$, the bounds are
$r,r,r,r-1,r-1,r-2,r-2,\ldots$.
The corresponding anchor degrees in the exception support multigraph
are at least two for deficit one, and at least
$\lceil d_i/2\rceil+2$ for $d_i\ge2$.

## Stronger deletion with a bounded exception set

**Additional hypothesis: $b\le r$.** Put

$$
K=\frac{k(k-3-2t)}2,\qquad L=S+e(X)+U.
$$

Equation (3) says $\Delta\Phi_{\rm final}\le2(K-L)$.
We claim deletion is safe whenever

$$
\boxed{a+t-2\ge K.} \tag{6}
$$

Only $K>0$ needs proof. Suppose $L<K$. All deficits are positive
and sum to at most $r-1$, so for $j,\ell\ne i$, $j\ne\ell$,

$$
|P_j|\ge a+k-1,\qquad
|P_j|+|P_\ell|\ge r+a+k-2. \tag{7}
$$


Every member of $X$ must be an exception incident with $i$.
If $x\in X\cap P_j$, then
$d_R(x)\ge|P_j|-f\ge a+t-1$. This implies
$U\ge d_R(x)-1\ge a+t-2\ge K$, a contradiction.
If instead $x$ is an exception supported on $j,\ell\ne i$, its
nonneighbor sets in those two private rows form a clique, by the
two-support augmentation argument. That clique has at most $r-1$
vertices. Therefore (7) gives at least $a+k-1$ neighbors in the two
rows, and at least $a+t-1$ remaining in $R$, the same contradiction.

Every $x\in X$ is complete to $P_i$. To see this, write
$d_R(x)=1+u_x$, so $\sum_xu_x=U$, and suppose $x$, supported on
$i,j$, misses $z\in P_i$. Then $z$ is complete to
$P_j\setminus N(x)$. All of $P_j$ is now in $R$, since $X$
consists entirely of exceptions. Put $s_z=d(z)-d(v)$. The number
of neighbors of $z$ outside $P_i$ is $f+s_z$, so

$$
|P_j|-1-u_x\le f+s_z,
\qquad a+t-2\le u_x+s_z\le U+S\le L<K,
$$

contradicting (6).

Finally $X$ is a clique. Suppose $x,y\in X$ are nonadjacent.
If their other support is the same row $j$, they jointly dominate
$P_j$, since a common nonneighbor would augment them and the unused
anchors. Thus

$$
|P_j|\le d_R(x)+d_R(y)\le2+U\le2+L.
$$

This contradicts (7) and (6): $K>0$ implies $f=k-t\ge4$, so
$a+k-3>a+t-2>L$.
If their other supports are distinct $j,\ell$, their common
nonneighbor sets in $P_j,P_\ell$ form a clique, again by augmentation.
Its order is at least

$$
|P_j|+|P_\ell|-d_R(x)-d_R(y)
\ge r+a+k-4-L>r-1,
$$

the same contradiction. Therefore

$$
L\ge\binom f2>K,
\qquad \binom{k-t}{2}-K=\frac{t^2+t+2k}{2}>0.
$$

This proves (6).

In a minimum-anchor bounded-exception member, it follows that

$$
\boxed{d_J(v)\ge r\text{ on every row of deficit }k
\text{ with }k(k-3)\le2a-4.} \tag{8}
$$

Under that condition, (6) holds for every $t\ge0$. This is a
uniform extension of the fixed small-deficit rule, but it is conditional
on $b\le r$. Neither (5) nor (8) establishes that missing hypothesis
or resolves the surviving cores.
