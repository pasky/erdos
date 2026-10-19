---
name: research/erdos_963/corank_one
title: 'The rational-rank defect at most one case'
desc: A proved maximum-volume argument establishing the target and its odd-slice strengthening when the intrinsic ternary-relation rank is at least the dissociation dimension minus one.
tags: []
sources: []
created: 2026-09-18T21:01:00Z
updated: 2026-09-18T21:01:00Z
---


# The rational-rank defect at most one case

***

## Statement

The following argument is proved. It extends the full-rational-rank case in
[[research/erdos_963/proof_sketch|the proof sketch]], but does not resolve the general problem.

Let $P$ be a finite nonempty set in a finite-dimensional rational vector
space. Assume that $0\notin P$ and that no two elements of $P$ are
opposites. Write $r=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}P$
and let $d=d(P)$ be the maximum size of a dissociated subset. If
$d\le r+1$, then

$$
 |P|\le 2^d-1. \tag{1}
$$

If, additionally, the additive group $L=\langle P\rangle_{\mathbb Z}$
admits a homomorphism

$$
 \chi:L\longrightarrow\mathbb F_2,
 \qquad \chi(p)=1\quad(p\in P),
 \tag{2}
$$

then

$$
 |P|\le 2^{d-1}. \tag{3}
$$

Positive sets satisfy the no-opposites hypothesis. Positive odd integer sets
satisfy (2), using reduction modulo two. The intrinsic lift below makes these
claims applicable beyond the original rational rank.

## Maximum-volume coordinates and the integral columns

Choose a rational basis $B=\{b_1,\ldots,b_r\}\subseteq P$ whose
determinant has maximum absolute value among all bases chosen from $P$.
Use $B$ as coordinate basis. Every coordinate of every $p\in P$
lies in $[-1,1]$: replacing $b_i$ by $p$ multiplies the basis
determinant by the $i$-th coordinate of $p$.
Likewise, the absolute determinant of any $r$ coordinate columns from
$P$ is at most one.

Let $I$ be the elements with integral coordinates. Their coordinates
belong to $\{-1,0,1\}^r$. Reduction modulo two is injective on
$I$. Indeed, two nonzero proportional ternary vectors are equal or
opposite. Thus two distinct columns $x,y\in I$ are rationally
independent. If their reductions modulo two were equal, extend $x,y$
to a rational basis using columns of $B$. The resulting matrix is
integral and has nonzero even determinant, contrary to the determinant bound.
No nonzero ternary vector reduces to zero modulo two. Hence

$$
 |I|\le 2^r-1. \tag{4}
$$

Under (2), an integral-coordinate vector satisfies
$\chi(\sum_i z_i b_i)=\sum_i z_i\pmod2$. Every column in $I$
therefore reduces to an odd-weight binary vector, giving

$$
 |I|\le 2^{r-1}. \tag{5}
$$


If $d=r$, every $p\in P\setminus B$ has ternary coordinates:
the dependence of $B\cup\{p\}$ must use $p$, since $B$ is
rationally independent. Thus $P=I$, and (4)--(5) prove both claims in
this case. It remains to consider $d=r+1$.

## A single signed nonintegral residue class

Put $N=P\setminus I$. If $N$ is empty, (4)--(5) already give the
required bounds. Suppose that $N\ne\varnothing$.

For distinct $x,y\in N$, the set $B\cup\{x,y\}$ has
$r+2>d$ elements and is not dissociated. Any ternary relation must use
both $x$ and $y$: a relation using just one of them would make that
column integral, and a relation using neither contradicts the independence of
$B$. Consequently

$$
 x-y\in\{-1,0,1\}^r
 \quad\hbox{or}\quad
 x+y\in\{-1,0,1\}^r. \tag{6}
$$

In particular, the residues of all columns of $N$ in
$\mathbb Q^r/\mathbb Z^r$ belong to a single pair $\{g,-g\}$,
where $g\ne0$.

Individual changes of sign preserve dissociation, preserve (2), and do not
identify two of the columns because the original set has no opposites. Thus
we may orient the columns of $N$ as convenient. The determinant bounds
and (6) remain valid after these sign changes.

### The case $2g\ne0$

Orient every nonintegral column to have residue $g$. For two such
columns, their sum is not integral. Thus (6) says that all their differences
are ternary. In each coordinate, all values have the same fractional part
and any two differ by at most one. There are at most two values in each
coordinate, so

$$
 |N|\le2^r. \tag{7}
$$

Combining (4) and (7) gives
$|P|\le2^{r+1}-1=2^d-1$.

Under (2), fix $x_0\in N$. For every $x\in N$, the integral
coordinate vector $x-x_0$ has

$$
 \sum_i(x_i-(x_0)_i)\equiv\chi(x)-\chi(x_0)=0\pmod2. \tag{8}
$$

Embed the available coordinate choices in a product of $r$ pairs of
consecutive values. If a coordinate is constant, add an artificial second
value differing by one. Exactly half of the $2^r$ vertices of this
product satisfy (8). Therefore $|N|\le2^{r-1}$. Together with (5),
this proves $|P|\le2^r=2^{d-1}$.

### The case $2g=0$

There are $s\ge1$ coordinates where the residue is $1/2$, and
$z=r-s$ coordinates where the residue is zero. The first coordinates
have values $\pm1/2$; the latter have values in $\{-1,0,1\}$.
Orient each column so that its first half-integral coordinate is $+1/2$.

Fix a support $S$ among the $z$ integral coordinates. If two sign
patterns on $S$ are neither equal nor opposite, they agree at a nonzero
coordinate and disagree at another. Their column sum then has a coordinate
$\pm2$, and their column difference also has a coordinate $\pm2$.
This contradicts (6). Thus at most two opposite sign patterns occur for a
nonempty support, and one occurs for the empty support. Each fixed integral
pattern has at most $2^{s-1}$ half-integral patterns. Consequently

$$
 |N|\le2^{s-1}\bigl(1+2(2^z-1)\bigr)
       =2^r-2^{s-1}<2^r. \tag{9}
$$

Together with (4), this proves (1); in this subcase it gives the slightly
stronger bound $|P|\le2^{r+1}-2$.

Now assume (2). Since $2x$ is an integral-coordinate vector and
$\chi(2x)=0$, its coordinate sum is even. Modulo two, this sum is
$s$, so $s$ is even and hence $s\ge2$. The total coordinate
sum

$$
 t(x)=\sum_{i=1}^r x_i
$$

is therefore an integer. For any two columns, their difference is integral,
and (2) gives $t(x)-t(y)\equiv0\pmod2$. Thus all these total sums
have the same parity. For a fixed integral-coordinate pattern, exactly half
of the $2^{s-1}$ possible half-integral patterns have the required total
parity: flipping any one of the remaining $s-1$ half-integral signs
changes the total by one. It follows that

$$
 |N|\le2^{s-2}\bigl(1+2(2^z-1)\bigr)
       =2^{r-1}-2^{s-2}<2^{r-1}. \tag{10}
$$

Combining this with (5) proves (3).

## Intrinsic ternary-relation rank

The rank hypothesis can be strengthened without changing any ternary
relations. For a finite positive real set $P$, take the vector space
$\mathbb Q^P$ with coordinate vectors $e_p$. Let

$$
 T=\operatorname{span}_{\mathbb Q}
 \left\{(\varepsilon_p)_{p\in P}\in\{-1,0,1\}^P:
              \sum_{p\in P}\varepsilon_p p=0\right\},
 \qquad V=\mathbb Q^P/T,
 \qquad \rho=\dim_{\mathbb Q}V.
$$

Call $\rho$ the intrinsic ternary-relation rank in this note. The
lifted configuration is $\widetilde P=\{e_p+T:p\in P\}\subseteq V$.

The original evaluation functional descends to a rational-linear map
$f:V\to\mathbb R$, with $f(e_p+T)=p>0$. In particular, the
lifted columns are distinct, nonzero, and have no antipodal pair. A ternary
vector vanishes in $V$ if and only if it gives a zero relation on the
original set. One direction holds because every original ternary relation
was included in the definition of $T$; the reverse holds because
$T$ is contained in the kernel of the original evaluation. Hence

$$
 d(\widetilde P)=d(P). \tag{11}
$$


For a maximum dissociated $D\subseteq P$, every $p\in P\setminus D$
has a ternary representation on $D$. These relations show that the
images of $D$ span $V$. Thus

$$
 \dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}P
 \le\rho\le d(P). \tag{12}
$$

Applying the proved vector-space theorem to $\widetilde P$ establishes
the target whenever

$$
 \rho\ge d(P)-1. \tag{13}
$$


If the original elements are odd integers, the parity homomorphism also
survives this lift. Indeed, an integral vector $(z_p)\in T\cap\mathbb Z^P$
has $\sum_p z_p p=0$, and reduction modulo two gives
$\sum_p z_p\equiv0\pmod2$. Therefore the map sending every lifted
generator to one descends to
$\langle\widetilde P\rangle_{\mathbb Z}\to\mathbb F_2$.
Under (13), the odd-slice bound follows:

$$
 |P|\le2^{d(P)-1}.
$$


## Remaining limitation

For rank defect $d-r=t\ge2$, the residue configuration in
$\mathbb Q^r/\mathbb Z^r$ has dissociation dimension at most $t$:
a dissociated set of $t+1$ residues, together with $B$, would give
$d+1$ dissociated columns. However, a dependence among $t+1$
nonintegral columns need not imply any pair relation of the form (6).
The coordinate counting above depends essentially on that pair relation.
No general rank-defect induction, and no proof for intrinsic defect at least
two, is established here.
