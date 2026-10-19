---
name: research/erdos_864/second_order_construction
desc: An endpoint-compression construction giving a positive N-to-the-one-quarter term above the reflected lower bound along an unbounded sequence.
tags: [proved, constructions, bounds]
sources: []
created: 2026-09-23T20:44:47Z
updated: 2026-09-24T22:12:55Z
---


# research/erdos_864/second_order_construction

***

## Statement and scope

There is an unbounded sequence of integers $N$ for which

$$
 M(N)\ge \frac{2}{\sqrt3}\sqrt N+
 \left(\frac{2\sqrt2}{9\,3^{1/4}}-o(1)\right)N^{1/4}. \tag{1}
$$

Equivalently,

$$
 \limsup_{N\to\infty}
 \frac{M(N)-(2/\sqrt3)\sqrt N}{N^{1/4}}
 \ge \frac{2\sqrt2}{9\,3^{1/4}}.
$$

The construction includes diagonal pair sums and has only one possible
exceptional integer sum. This does **not** improve the leading constant
or settle the proposed upper bound.

The idea is to compress the
[reflected construction](established_bounds.md) by an amount of order
$N^{3/4}$, while deleting only order $N^{1/4}$ points to eliminate
the new collisions. Averaging over the compression parameter reduces
the required relation count to an ordinary Cartesian-product count;
no sparse four-variable counting lemma is assumed.

## A cyclic Sidon set and its translate variance

For a prime power $q$, put $v=q^2+q+1$. There is a set
$D_0\subset\mathbb Z_v$, of size $q+1$, in which every nonzero
ordered difference occurs exactly once.

Here is a self-contained verification of the standard Singer
construction used below. Let $K=\mathbb F_{q^3}$, and let $U$ be a
two-dimensional $\mathbb F_q$-subspace of $K$. The projective points
of $U$ give $q+1$ elements of the cyclic group
$K^*/\mathbb F_q^*$, which has order $v$. For
$x\in K^*\setminus\mathbb F_q^*$, the subspaces $U$ and $xU$
intersect in exactly one dimension. They cannot coincide: otherwise
for $0\ne u\in U$, the three elements $u,xu,x^2u$ would belong to
$U$, contradicting the degree-three minimal polynomial of $x$.
Their unique common projective point gives exactly one representation
of the quotient class of $x$ as a quotient of two points of $D_0$.
Under a cyclic identification, this is the required difference
property. It implies ordinary modular Sidonicity, including diagonal
pairs.

For comparison, see §3.4 and entry [4] of
[source record](../../../library/additive_bases/obryant_2004_complete_annotated_bibliography_work_related_sidon/_index.md).
The proof above supplies all properties used here.

For any set $I\subset\mathbb Z_v$ of $\ell$ residues, and a uniformly
random translate $\tau$, let

$$
 X_I(\tau)=|(D_0+\tau)\cap I|.
$$

The perfect-difference property gives

$$
 \sum_\tau X_I(\tau)=(q+1)\ell,\qquad
 \sum_\tau X_I(\tau)(X_I(\tau)-1)=\ell(\ell-1).
$$

Since $(q+1)^2=v+q$, it follows that

$$
 \mathbb E X_I=\frac{(q+1)\ell}{v},\qquad
 \operatorname{Var}X_I=\frac{q\ell(v-\ell)}{v^2}. \tag{2}
$$


## Simultaneous distribution in two short endpoint intervals

Fix $c>0$, and put $W=\lfloor c q^{3/2}\rfloor$. For every
sufficiently large $q$, one can choose a translate of $D_0$,
represented by $D\subset[0,v-1]$, so that both measures

$$
 \mu_L=\frac qW\sum_{\substack{d\in D\\0\le d\le W}}\delta_{d/W},
 \qquad
 \mu_R=\frac qW\sum_{\substack{d\in D\\v-1-W\le d\le v-1}}
                      \delta_{(v-1-d)/W} \tag{3}
$$

converge weakly to Lebesgue measure on $[0,1]$, as $q$ tends to
infinity through prime powers.

For completeness, apply (2) to the endpoint prefixes of relative
length $j/J$, where $J=\lfloor q^{1/8}\rfloor$. Their normalized
counts have expectation $j/J+o(1)$, uniformly in $j$, and variance
$O(q/W)=O(q^{-1/2})$. Chebyshev's inequality, with normalized
tolerance $q^{-1/8}$, bounds each failure probability by
$O(q^{-1/4})$. There are $O(J)$ prefixes in both windows, so the
probability of any failure is $O(q^{-1/8})$. A good translate exists.
Monotonicity fills the gaps between grid points and gives simultaneous
uniform convergence of the two distribution functions. In particular,
both endpoint intervals contain $O(W/q)$ elements of $D$.

No independence between the two endpoint measures is asserted or
needed. For this deterministic good translate, their Cartesian
products converge to the corresponding products of Lebesgue measure.

## Averaging the new forbidden relations

Fix also $a\in(0,1)$. For each integer
$\lceil aW\rceil\le w\le W$, let $E_w$ count pairs
$(\{d_1,d_2,d_3\},d_4)$, with an unordered multiset of three inputs
and $d_i\in D$, satisfying

$$
 d_1+d_2+d_3=d_4-(v-1)+w. \tag{4}
$$

Every input belongs to $[0,W]$, and every output to
$[v-1-W,v-1]$. On writing

$$
 x_i=d_i/W\quad(1\le i\le3),\qquad
 x_4=(v-1-d_4)/W,
$$

equation (4) is equivalent to $\sum_i x_i=w/W$.
Thus the sum over these $w$ of the **ordered** relation counts
equals the number of endpoint quadruples in the simplex shell

$$
 a\le x_1+x_2+x_3+x_4\le1,
$$

with the lower boundary adjusted by $O(W^{-1})$ for rounding.
The limiting product measure assigns the boundary measure zero.
By (3), this count is

$$
 \left(\frac{1-a^4}{24}+o(1)\right)\left(\frac Wq\right)^4. \tag{5}
$$

Indeed the simplex of nonnegative quadruples with sum at most $t\le1$
has volume $t^4/24$.

Quadruples with a repeated input contribute only

$$
 O\!\left((W/q)^3\right)=O(q^{3/2}):
$$

choose which two input positions coincide, their common value, the
remaining input, and the output. For all other tuples there are exactly
six input orderings. Consequently

$$
 \sum_{w=\lceil aW\rceil}^{W}E_w
 =\left(\frac{1-a^4}{144}+o(1)\right)\left(\frac Wq\right)^4
  +O(q^{3/2}).
$$

There are $(1-a)W+O(1)$ parameters. With
$S_a=1+a+a^2+a^3$, some $w$ therefore satisfies

$$
 E_w\le
 \left(\frac{S_a c^3}{144}+o(1)\right)\sqrt q. \tag{6}
$$

The repeated-input error becomes $O(1)$ after averaging. Here and
below all errors tend to zero with $q$ for fixed $a,c$.

## Deletion, reflection, and the unique exception

Delete from $D$ every output $d_4$ participating in (4), and call
the remaining set $D'$. At most $E_w$ elements are deleted.
Put

$$
 t=\frac{v-1-w}{2},\qquad B=t+D'.
$$

For large $q$, $t>0$. The set $B$ is ordinary Sidon because
$D'$ is, and (4) is precisely the condition that an element of $B$
be a sum of three elements of $B$. Hence

$$
 B\cap(B+B+B)=\varnothing.
$$

The [positive-half characterization](symmetric_reformulations.md)
now shows that $\pm B$ has unique unordered pair sums away from
zero. Explicitly, positive sums are either sums of two elements of
$B$ or positive differences of two elements of $B$. Each type is
unique by Sidonicity; a collision between the types would give the
excluded three-to-one relation. Negative sums follow by reflection.
This checks diagonal pairs as well.

A translation gives the integer set

$$
 A=(v-D')\ \cup\ (2v-1-w+D')
       \subset[1,N],\qquad N=3v-2-w. \tag{7}
$$

This avoids any parity restriction on $w$. The two copies are
disjoint for large $q$, and

$$
 |A|\ge2q+2-2E_w.
$$

Their exceptional sum is $3v-1-w=N+1$; it is the only integer
sum that can repeat.

## Optimizing the gain

Uniformly for $w=O(q^{3/2})$,

$$
 \frac2{\sqrt3}\sqrt{3v-2-w}
   =2q-\frac{w}{3q}+O(1).
$$

Using $w\ge aW$ and (6) in (7) yields

$$
 |A|-\frac2{\sqrt3}\sqrt N
 \ge
 \left(\frac{ac}{3}-\frac{S_a c^3}{72}+o(1)\right)\sqrt q. \tag{8}
$$

For fixed $a$, this expression is maximized by

$$
 c^2=\frac{8a}{S_a},
$$

and its coefficient becomes

$$
 F(a)=\frac{4\sqrt2\,a^{3/2}}{9\sqrt{S_a}}
       \longrightarrow\frac{2\sqrt2}{9}
       \qquad(a\uparrow1).
$$

Choose a sequence $a_j\uparrow1$, take the corresponding $c_j$,
and then choose increasing prime powers $q_j$ large enough that
the normalized error in (8) is at most $1/j$.
Since $N_j\sim3q_j^2$, this proves (1).

The diagonal choice proves an unbounded sequence statement, not the
same second-order inequality for every sufficiently large $N$.
The established leading bounds remain those on the
[bounds page](established_bounds.md).
