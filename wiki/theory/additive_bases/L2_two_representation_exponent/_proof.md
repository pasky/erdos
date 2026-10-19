---
name: theory/additive_bases/L2_two_representation_exponent/_proof
title: Proof of the two-representation exponent
desc: |
  A uniform divisor count for fiber triples and simultaneous shell selection
  give one set with lower exponent 3/7 and an encoding-specific zero ratio.
tags: []
sources: []
created: 2026-09-08T22:30:28Z
updated: 2026-09-08T22:43:22Z
---

***

We prove [L2](_index.md) and its restricted-encoding consequence. Put
$\gamma=3/7$. All logarithms in estimates below have base two unless
written $\ln$; the ratio in the theorem is independent of that choice.

## External interfaces and elementary divisor control

We use the following three external theorems at precisely these strengths:

- Bertrand's postulate: for every integer $m\ge1$, there is a prime $q$
  with $m<q\le2m$. We use $m\ge2$, when $2m$ is composite, so the
  upper inequality is strict. See P. Erdős,
  [*Beweis eines Satzes von Tschebyschef*](https://users.renyi.hu/~p_erdos/1932-01.pdf),
  *Acta Litt. Sci. Szeged* 5 (1932), 194–198, §5, printed pp. 197–198
  (PDF pp. 4–5).
- For every prime $q$, the multiplicative group of nonzero residues modulo
  $q$ is cyclic of order $q-1$. See Keith Conrad,
  [*Cyclicity of (Z/(p))^×*](https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf),
  undated author exposition, Theorem 2.6, printed/PDF p. 3.
- The prime number theorem: if $\pi(t)$ counts the primes at most the real
  number $t$, then $\pi(t)\sim t/\ln t$ as $t\to\infty$. See D. Zagier,
  [*Newman's Short Proof of the Prime Number Theorem*](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf),
  *American Mathematical Monthly* 104(8) (1997), 705–708, the named Prime
  Number Theorem on printed p. 705 (PDF p. 2, following the cover).

These selected PDFs were accessed. Reading scope
for the three external inputs is claims checked: their statements and
inequality conventions were checked visually, without a full proof audit.

Bertrand supplies one auxiliary prime in each specified interval; cyclicity
supplies the digit encodings; the prime number theorem supplies the number
of available labels in each shell. No theorem about the density of Sidon
sets is a premise.

Here is the divisor estimate needed later, with its uniformity included.
Write $\tau(m)$ for the number of positive divisors of a positive integer
$m$. For every fixed $C>0$,

$$
\max_{1\le m\le 2^{CK^2}}2\tau(m)
\le 2^{O_C(K^2/\log_2 K)}\qquad(K\to\infty).
\tag{1}
$$

To prove this, take a real $H\ge e^4$, put $t=\ln H$, and factor an
arbitrary $1\le m\le H$ as $m=\prod_p p^{e_p}$. The case $m=1$ has
an empty product and $\tau(1)=1$. Every exponent is at most $t/\ln2$.
The primes at most $\sqrt t$ are at most $\sqrt t$ in number, so their
contribution to $\ln\tau(m)$ is at most

$$
\sqrt t\,\ln(1+t/\ln2).
$$

For primes $p>\sqrt t$, use $e_p+1\le2^{e_p}$ and

$$
\sum_{p>\sqrt t}e_p\le\frac{2t}{\ln t}.
$$

Their contribution is at most $2(\ln2)t/\ln t$. The first contribution
is also $O(t/\ln t)$, since $(\ln t)^2/\sqrt t\to0$. These bounds
hold for every $m\le H$ with constants independent of $m$. Taking
$H=2^{CK^2}$ proves (1). For a nonzero integer $F$, its ordered signed
factor pairs $(u,v)$ with $uv=F$ number exactly $2\tau(|F|)$: choose a
positive divisor $|u|$ and either sign of $u$, after which $v$ is fixed.

## The label set and its digits

Fix primes and generators

$$
2^{2j-1}<q_j<2^{2j},\qquad
g_j\text{ generates }(\mathbb Z/q_j\mathbb Z)^\times
\quad(j\ge1).
$$

Bertrand applies with $m=2^{2j-1}$. The intervals are disjoint, so the
primes $q_j$ are pairwise distinct. Define

$$
b_j=4q_j,\quad Q_k=\prod_{j=1}^kq_j,\quad
B_k=\prod_{j=1}^kb_j=4^kQ_k,\quad B_0=1.
$$

Summing the exponents in the prime bounds gives

$$
2^{k^2}<Q_k<2^{k^2+k},\qquad
2^{k^2+2k}<B_k<2^{k^2+3k}.
\tag{2}
$$

Choose a fixed integer $k_0$ sufficiently large for
$\gamma(k-1)^2>2k$ whenever $k\ge k_0$, and for the explicit uniform
comparisons below. All these requirements have finite thresholds. Only the
label shells below $k_0$ are omitted; the auxiliary primes and radices remain
fixed starting at $j=1$.

For $k\ge k_0$, let

$$
\mathcal P_k=
\{p\text{ prime}:2^{\gamma(k-1)^2}<p\le2^{\gamma k^2}\}.
\tag{3}
$$

These shells are disjoint. If $p\in\mathcal P_k$ and $j\le k$, then
$p>2^{2k}>q_j$. There is a unique integer $x_j(p)$ with

$$
q_j+1\le x_j(p)\le2q_j-1,\qquad
g_j^{x_j(p)}\equiv p\pmod{q_j}.
\tag{4}
$$

Indeed, the interval in (4) has exactly $q_j-1$ consecutive integers,
and hence represents every exponent class modulo $q_j-1$ once. Put
$x_j(p)=0$ for $j>k$, and define the positive integer

$$
a_p=\sum_{j=1}^k x_j(p)B_{j-1}.
\tag{5}
$$

A finite mixed-radix expansion with digits $0\le d_j<b_j$ is unique:
reduce equality of two expansions modulo $b_1$ to identify the first digit,
subtract it and divide by $b_1$, and continue. Formula (5) has such digits,
its top digit is positive, and telescoping gives

$$
1\le a_p\le\sum_{j=1}^k(b_j-1)B_{j-1}=B_k-1.
\tag{6}
$$

Adding any two labels creates no carries, because each digit sum is at most
$4q_j-2<b_j$. Thus equality of label sums implies equality of their digit
sums at every position.

The map $p\mapsto a_p$ is injective. Its last nonzero digit determines
the shell $k$. Within one shell, equal labels give equal digits, and (4)
gives $p\equiv p'\pmod{q_j}$ for every $j\le k$. Distinctness of the
auxiliary primes implies $Q_k\mid p-p'$: the product of distinct primes
dividing an integer divides it, by repeated application of Euclid's lemma.
But $p,p'\le2^{\gamma k^2}<Q_k$, so $p=p'$.

Write $n_k=|\mathcal P_k|$ and $X_k=2^{\gamma k^2}$. The prime number
theorem gives

$$
n_k\sim\frac{X_k}{\ln X_k},\qquad
\log_2 n_k=\gamma k^2-O(\log_2 k)
\quad(k\to\infty).
\tag{7}
$$

For the subtraction of the lower endpoint, it is enough that
$\pi(X_{k-1})\le X_{k-1}$ and

$$
\frac{X_{k-1}\ln X_k}{X_k}
=\gamma k^2\ln2\,2^{-\gamma(2k-1)}\longrightarrow0.
$$

In particular, the shells are nonempty eventually. No logarithm of a shell
size is needed for the finitely many shells where its size might be zero.

## Recovering the shells and the congruence fibers

In a sum with shell indices $K\ge L$, the digit at position $j$ lies in
one of the following disjoint ranges:

$$
\begin{array}{c|c}
j\le L &[2q_j+2,4q_j-2]\\
L<j\le K &[q_j+1,2q_j-1]\\
j>K &\{0\}.
\end{array}
\tag{8}
$$

The last nonzero position recovers $K$, and the last position in the
two-active-digit range recovers $L$. This also covers $K=L$, when the
middle range never occurs. Therefore all representations of a given integer
use the same unordered pair of shells.

For a same-shell equality $a_p+a_r=a_{p'}+a_{r'}$, exponentiating digit
equality gives $pr\equiv p'r'\pmod{Q_K}$. Both products are at most
$2^{2\gamma K^2}<Q_K$, so they are equal as integers. A prime $p$ then
divides $p'$ or $r'$, hence equals that prime; cancellation identifies the
other prime. Thus the unordered pair is unique, including when $p=r$.

For $K>L\ge k_0$, put

$$
M=Q_L,\quad N=Q_K/Q_L,\quad
X=2^{\gamma K^2},\quad Y=2^{\gamma L^2}.
$$

Then $\gcd(M,N)=1$, $MN=Q_K$, and direct multiplication of the prime
bounds gives

$$
2^{L^2}<M<2^{L^2+L},\qquad
2^{K^2-L^2}<N<2^{K^2-L^2+K-L}.
\tag{9}
$$

The relevant map on the full shells is

$$
\Phi_{K,L}:\mathcal P_K\times\mathcal P_L
\longrightarrow(\mathbb Z/N\mathbb Z)\times(\mathbb Z/M\mathbb Z),
\qquad
(P,R)\longmapsto(P\bmod N,PR\bmod M).
\tag{10}
$$

Equal integer sums $a_P+a_R=a_{P'}+a_{R'}$ imply equal images in
(10): the single active digits above $L$ yield $P\equiv P'\pmod N$,
and the two active digits through $L$ yield $PR\equiv P'R'\pmod M$.
Only this implication is used; membership in a common fiber is not asserted
to imply equality of integer sums.

Each coordinate projection is injective on any one fiber. If $P=P'$, then
cancellation modulo $M$ gives $R\equiv R'\pmod M$, and $R,R'\le Y<M$
gives $R=R'$. Cancellation is legitimate because an upper-shell prime exceeds
every $q_j$ dividing $M$. If instead $R=R'$, cancellation modulo $M$
gives $P\equiv P'\pmod M$, while the first coordinate gives the same
congruence modulo $N$. Coprimality implies $MN\mid P-P'$, and
$P,P'\le X<MN$ gives $P=P'$. The lower prime is coprime to $M$ by (3).

A fiber with at least two points forces the strict band

$$
\frac47<\frac{L^2}{K^2}<\frac34.
\tag{11}
$$

To see this, two distinct upper coordinates have a nonzero difference divisible
by $N$ and of absolute value less than $X$, so $N<X$. The two products
$PR,P'R'$ are distinct: prime divisibility and disjointness of the shells
would otherwise identify both coordinates. Their nonzero difference is
divisible by $M$ and has absolute value less than $XY$, so $M<XY$.
Using (9) gives respectively

$$
K^2-L^2<\gamma K^2,\qquad
L^2<\gamma(K^2+L^2),
$$

which are (11).

## A uniform count of triples in the fibers

Let $T_{K,L}$ count the three-element subsets of
$\mathcal P_K\times\mathcal P_L$ that lie in one fiber of (10). Set

$$
U=X/N,\qquad Z=XY/M,\qquad W=2XY^2/(MN).
\tag{12}
$$

We will prove, with an absolute constant $C$ and every sufficiently large
$K$, uniformly over $k_0\le L<K$,

$$
T_{K,L}\le C U^2Z^2W\,2^{CK^2/\log_2 K}.
\tag{13}
$$

If $T_{K,L}=0$, the inequality holds without further conditions. Assume
there is a triple, and order its upper primes as $P_1<P_2<P_3$. Projection
injectivity makes the corresponding lower primes $R_1,R_2,R_3$ distinct.
The fiber congruences give uniquely determined integers $a,b,s,t$ with

$$
\begin{aligned}
P_2-P_1&=Na,& P_3-P_1&=Nb,&0<a<b<U,\\
P_2R_2-P_1R_1&=Ms,& P_3R_3-P_1R_1&=Mt,
&0<|s|,|t|<Z.
\end{aligned}
\tag{14}
$$

The product differences are nonzero by the prime argument just used, and
$s\ne t$ because otherwise $P_2R_2=P_3R_3$. Rewriting the two product
equations yields

$$
\begin{aligned}
P_1(R_2-R_1)+NaR_2&=Ms,\\
P_1(R_3-R_1)+NbR_3&=Mt.
\end{aligned}
\tag{15}
$$

Eliminating $P_1$ gives $N E=M F_0$, where

$$
\begin{aligned}
E&=aR_2(R_3-R_1)-bR_3(R_2-R_1),\\
F_0&=s(R_3-R_1)-t(R_2-R_1).
\end{aligned}
$$

Since $M$ and $N$ are coprime, $M\mid E$. For the integer $d=E/M$,
the same equality gives

$$
\begin{aligned}
aR_2(R_3-R_1)-bR_3(R_2-R_1)&=dM,\\
s(R_3-R_1)-t(R_2-R_1)&=dN.
\end{aligned}
\tag{16}
$$

The bound $|E|<2UY^2$ implies $|d|<W$.

All further size comparisons are uniform over the band (11). The shell
lower bounds and (9) give, for every coordinate of the triple,

$$
\begin{aligned}
\log_2(U/R_i)
&<-(1-\gamma)(K^2-L^2)+2\gamma L-\gamma\\
&<-K^2/7+6K/7,\\
\log_2(U/P_i)
&<-(K^2-L^2)+2\gamma K-\gamma\\
&<-K^2/4+6K/7.
\end{aligned}
\tag{17}
$$

Thus $U<R_i$ and $U<P_i$ for all sufficiently large $K$, independently
of $L$. If $d=0$, reduction of the first equation in (16) modulo $R_2$
would give $R_2\mid bR_3R_1$. The three lower primes are distinct, so
$R_2\mid b$, contradicting $0<b<U<R_2$. We have proved

$$
0<|d|<W.
\tag{18}
$$

There is also a strict margin for the later nonvanishing argument. In fact,
(9), (11), and (12) imply

$$
\begin{aligned}
\log_2(WU^3/M)
&<1+(4\gamma-4)K^2+(2\gamma+2)L^2\\
&<1-K^2/7.
\end{aligned}
\tag{19}
$$

After enlarging $k_0$ if necessary, this proves $|d|U^3<M$. The inequalities
(17) and (19) depend only on $K$, so this single choice works for every
lower shell.

Fix the five integers $(a,b,s,t,d)$ and set $\Delta=at-bs$. We count
how many triples can have these parameters.

### The case $\Delta\ne0$

Define

$$
\rho=R_2-R_3,\qquad \sigma=atR_2-bsR_3.
$$

Eliminating $R_1$ from (16) gives

$$
\rho\sigma=d\{M(s-t)-NaR_2+NbR_3\}.
\tag{20}
$$

For clarity, multiply the first equation in (16) by $s-t$ and substitute
$(s-t)R_1=sR_3-tR_2-dN$ from the second. The quadratic part becomes
$atR_2^2-(at+bs)R_2R_3+bsR_3^2=\rho\sigma$, giving (20).
Also,

$$
R_2=\frac{\sigma-bs\rho}{\Delta},\qquad
R_3=\frac{\sigma-at\rho}{\Delta}.
\tag{21}
$$

Substituting (21) in (20) and multiplying by $\Delta$ yields

$$
\Delta\rho\sigma
=d\Delta M(s-t)+dN(b-a)\sigma+dNab(s-t)\rho.
$$

Multiply again by $\Delta$ and complete the product to obtain

$$
\begin{aligned}
&(\Delta\rho-dN(b-a))(\Delta\sigma-dNab(s-t))\\
&\qquad=d(s-t)\{\Delta^2M+dN^2ab(b-a)\}.
\end{aligned}
\tag{22}
$$

Call the integer on the right $F$. It is nonzero. We already know
$d\ne0$ and $s\ne t$. If the braces vanished, coprimality of $M$ and
$N$ would give $M\mid dab(b-a)$. This is impossible because

$$
0<|dab(b-a)|<|d|U^3<M.
$$

The integer $F$ is uniformly of bounded exponential size. For example,
$X,Y\le2^{K^2}$, $M,N\le2^{2K^2}$,
$U\le2^{K^2}$, $Z\le2^{2K^2}$, and $W\le2^{4K^2}$ imply
$|\Delta|<2^{4K^2}$ and then $1\le|F|\le2^{20K^2}$.
These deliberately loose bounds use no constant depending on $L$.
By (1), equation (22) therefore has at most
$2^{O(K^2/\log_2 K)}$ ordered signed factor pairs.

Each such factor pair determines $\rho$ and $\sigma$, since
$\Delta\ne0$, and then determines $R_2,R_3$ by (21). The second
equation of (16) determines $R_1$, since $s-t\ne0$. Finally the first
equation of (15) determines $P_1$, since $R_2-R_1\ne0$, and (14)
determines $P_2,P_3$. Some factor pairs need not yield integers or primes
in the required intervals; discarding them can only reduce the count. There
is no additional choice of a fiber or of a prime after the factor pair.

### The case $\Delta=0$

Write $e=\gcd(a,b)$, $a=ea'$, $b=eb'$, with
$1\le a'<b'$ and $\gcd(a',b')=1$. From $a't=b's$, there is a
nonzero integer $f$ such that $s=fa'$ and $t=fb'$. Put

$$
C_0=fM-NeR_1.
$$

Equations (14)–(15) now give

$$
a'C_0=P_2(R_2-R_1),\qquad
b'C_0=P_3(R_3-R_1).
\tag{23}
$$

For instance, replace $P_1$ by $P_2-Nea'$ in the first equation of
(15), and cancel the resulting $Nea'R_2$ terms. By (17),
$a'<P_2$ and $b'<P_3$. Hence the distinct primes $P_2,P_3$ both
divide $C_0$, so their product divides it. On the other hand,
$|f|<Z$, $e<U$, and $R_1\le Y$ give

$$
|C_0|<ZM+NUY=2XY.
$$

Uniformly over (11), the shell lower endpoints give

$$
\begin{aligned}
\log_2\frac{2XY}{P_2P_3}
&<1-\gamma(K^2-L^2)+4\gamma K-2\gamma\\
&<-3K^2/28+12K/7+1/7.
\end{aligned}
\tag{24}
$$

This is negative for all sufficiently large $K$, so $|C_0|<P_2P_3$.
Divisibility forces $C_0=0$, and (23) gives $R_2=R_1$, a contradiction.
Thus the singular case contributes no triples.

### Summing the parameters

A triple forces $U>1$, $Z>1$, and $W>1$ by (14) and (18). There are
at most $U^2$ choices of $(a,b)$, at most $4Z^2$ choices of $(s,t)$,
and at most $2W$ choices of $d$. The nonsingular factor-pair estimate is
uniform over all these choices. Multiplying proves (13). The zero-triple
case was handled first; in particular no logarithm of $T_{K,L}=0$ has
been used.

For a nonzero triple count, (11) and $MN>2^{K^2}$ imply

$$
\begin{aligned}
U^2Z^2W
&=\frac{2X^5Y^4}{(MN)^3}\\
&<2^{1+(5\gamma-3)K^2+4\gamma L^2}
\le2^{1+\gamma K^2}.
\end{aligned}
\tag{25}
$$

The last inequality uses $5\gamma-3+3\gamma=\gamma$ at
$\gamma=3/7$. Combining (13) and (25), and restoring the zero case,
gives a common bound

$$
T_{K,L}\le2^{\gamma K^2+O(K^2/\log_2 K)}
\tag{26}
$$

for every retained pair of shells. Every implied constant and the lower
threshold for $K$ in (26) are independent of the lower index $L$.

## Choosing one set through all shells

We first prove the finite selection bound we use. A simple three-uniform
hypergraph consists of a finite vertex set and a set of three-element edges.
For $n>0$ vertices and $m\ge0$ edges, it has an independent subset of
size at least

$$
c\frac{n}{\sqrt{1+m/n}},\qquad c=\frac{2}{3\sqrt3}.
\tag{27}
$$

Retain each vertex independently with probability
$p=1/\sqrt{3(1+m/n)}$. The expected number of retained vertices minus
retained edges is $pn-p^3m\ge(2/3)pn$. In each outcome, delete a vertex
from each edge whose three vertices were retained. Removing the union of
these choices deletes at most the number of retained edges and leaves an
independent subset. Some outcome therefore has at least the stated expected
lower bound. If $m=0$, retaining the whole vertex set also proves (27).
If $n=0$, use the empty independent subset without dividing by $n$.

For every $K\ge k_0$, define a simple three-uniform hypergraph on the
entire shell $\mathcal P_K$. Declare an upper-prime three-set an edge
if it is the projection of a triple in one fiber of $\Phi_{K,L}$ for
at least one $k_0\le L<K$, using the full lower shell $\mathcal P_L$.
Let $m_K$ be its number of edges. Different triples and lower shells can
give the same edge, so the appropriate bounds are

$$
m_K\le\sum_{L=k_0}^{K-1}T_{K,L}
\le2^{\gamma K^2+O(K^2/\log_2 K)}.
\tag{28}
$$

The sum has fewer than $K$ terms and the error in (26) is uniform; its
extra factor $K$ is absorbed in the displayed error. An empty sum is zero.
Together with (7), this gives $m_K/n_K\le2^{O(K^2/\log_2 K)}$ for
all sufficiently large $K$. Thus (27) gives an independent subset
$I_K\subseteq\mathcal P_K$ with

$$
|I_K|\ge2^{\gamma K^2-O(K^2/\log_2 K)}.
\tag{29}
$$

Make one choice for every shell, independent of all density exponents: for
example, order each finite prime shell increasingly and take the
lexicographically first maximum independent subset. For an empty shell take
$I_K=\varnothing$. Finitely many initial shells cause no density issue;
their independent subsets are still selected by this same rule. Define

$$
A=\{a_p:p\in\bigcup_{K\ge k_0}I_K\}.
\tag{30}
$$

This fixes a single set. It is a set of positive integers by (6), and is
infinite by (29) and injectivity of the labeling map.

Every fiber of every $\Phi_{K,L}$ contains at most two selected pairs.
Indeed, three selected pairs would have three distinct upper primes by
projection injectivity. Those primes form an edge by the definition of
$m_K$, contradicting independence of $I_K$. This argument already allowed
every prime in the lower shell, so choices of the lower subsets cannot
introduce an unaccounted triple.

Now fix an integer $n$ with a representation in $A$. Equation (8) forces
all its representations to use one shell pair. The same-shell case has one
unordered representation at most. In the unequal-shell case, each unordered
representation corresponds to exactly one ordered pair $(P,R)$ with the
upper-shell prime first, and all such pairs lie in a single fiber of (10).
There are at most two. Integers with no representation, including nonpositive
integers, satisfy the same bound. This proves $r_A(n)\le2$ for every
integer $n$, with diagonal representations included in the same-shell case.

## Passing to every real cutoff

The strictly increasing sequence $B_K$ tends to infinity. For every large
real $x$, choose the unique $K$ with $B_K\le x<B_{K+1}$. Every selected
label from shell $K$ is below $B_K$, by (6), so

$$
\log_2 A(x)\ge\gamma K^2-O(K^2/\log_2 K).
\tag{31}
$$

The quantity on the right is positive eventually, and (2) gives

$$
0<\log_2 x<(K+1)^2+3(K+1)=K^2+5K+4.
$$

Dividing (31) by this upper bound for the positive denominator yields

$$
\frac{\log_2 A(x)}{\log_2 x}
\ge\frac{\gamma K^2-O(K^2/\log_2 K)}{K^2+5K+4}
\longrightarrow\gamma
$$

as a lower bound when $x\to\infty$. Hence the limit inferior is at least
$\gamma=3/7$. For any fixed $\alpha<\gamma$, the displayed lower bound
is greater than $\alpha$ for all sufficiently large $K$. Exponentiating
gives $A(x)\ge x^\alpha$ for all sufficiently large real $x$. The set
(30) has not changed with $\alpha$.

## Restricted-encoding zero endpoint ratio

Define the unselected ambient set

$$
A_0=\{a_p:p\in\bigcup_{k\ge k_0}\mathcal P_k\},\qquad
x_K=(q_{K+1}+1)B_K-1\quad(K\ge k_0).
$$

Every label from shell $K+1$ or higher has its $(K+1)$st digit at least
$q_{K+1}+1$, and all its other digits are nonnegative. It is therefore
strictly larger than $x_K$. All shell primes through $K$ are distinct
positive integers at most $2^{\gamma K^2}$, so

$$
A_0(x_K)\le\sum_{k=k_0}^K|\mathcal P_k|
\le2^{\gamma K^2}.
$$

Since $B_K>1$, the prime bounds and (2) give

$$
x_K>q_{K+1}B_K>2^{2K+1}2^{K^2+2K}
=2^{K^2+4K+1}.
$$

Thus $x_K\to\infty$ and

$$
0\le\frac{A_0(x_K)}{x_K^{3/7}}
\le2^{-(3/7)(4K+1)}\longrightarrow0.
$$

For any subset $S\subseteq A_0$, its counting function is nonnegative
and at most $A_0(x)$, so its ratio to $x^{3/7}$ also tends to zero along
these cutoffs and has limit inferior zero. This proves the named consequence.
It rules out an eventual positive constant times $x^{3/7}$ only among
subsets of this encoding. It makes no assertion about that endpoint for
other two-representation sets or about the square-root scale of E0158.
