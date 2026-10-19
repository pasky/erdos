---
name: research/methods/private_progression_discounts
title: Private progressions and discounted reciprocal budgets
desc: |
  Extracts minimum private progressions from irredundant covers and derives
  a discounted reciprocal budget through nonuniform set pairs and digit
  averaging.
problems: [7]
review_status: unreviewed
created: 2026-09-09T02:22:43Z
updated: 2026-10-19T04:19:07Z
---

# Private progressions and discounted reciprocal budgets

[[research/methods/_index|..]]

***

This page's notes that cite no source are author-recorded research, not claims.

This account gives complete author-recorded deductions for finite irredundant
coverings: a disjoint family of private progressions, a pointwise inequality
for cylinders with different coordinate alphabets and support sizes, and an
averaged reciprocal budget. Simpson's minimum-modulus theorem supplies an
additional bound in terms of the number of classes. These conclusions do not
provide an owner-payment argument or a resolution of
[[problems/covering_systems/E0007/_index|Problem 7]].

## Minimum private progressions

Let

$$
\mathcal C=(C_i)_{i=1}^k,
\qquad C_i=a_i+n_i\mathbb Z,
\qquad k\ge1,\quad n_i\in\mathbb Z_{>0},
\qquad \bigcup_{i=1}^k C_i=\mathbb Z
$$

be an indexed irredundant cover. Thus each class has a nonempty private set

$$
W_i=C_i\setminus\bigcup_{j\ne i}C_j
   =\mathbb Z\setminus\bigcup_{j\ne i}C_j.
$$

The second equality uses coverage. Put
$L=\operatorname{lcm}_i n_i$ and
$L_{-i}=\operatorname{lcm}_{j\ne i}n_j$, with empty lcm equal to $1$.
The set $W_i$ is periodic modulo $L_{-i}$. Any $w\in W_i$ therefore gives
$w+L_{-i}\mathbb Z\subseteq W_i$, so the following minimum exists:

$$
P_i=\min\{d\in\mathbb Z_{>0}:\exists b\in\mathbb Z,
                      \ b+d\mathbb Z\subseteq W_i\}.
$$

Choose a minimizing progression $Q_i=b_i+P_i\mathbb Z$. The minimum is over
all residues as well as all positive moduli. It is not defined by fixing a
private point first, or by asking for the least period of the whole set $W_i$.

Containment $Q_i\subseteq C_i$ gives $b_i\equiv a_i\pmod{n_i}$ and
$n_i\mid P_i$, by subtracting two consecutive elements of $Q_i$. To obtain
the other divisibility, observe that whenever $b+d\mathbb Z$ lies in an
$M$-periodic set $W$, closure under positive and negative shifts by $M$ gives

$$
b+\gcd(d,M)\mathbb Z=b+d\mathbb Z+M\mathbb Z\subseteq W.
$$

For $d=P_i$ and $M=L_{-i}$, minimality forces
$\gcd(P_i,L_{-i})=P_i$. Consequently

$$
n_i\mid P_i\mid L_{-i}\mid L.
$$

Different private sets are disjoint. Hence the $Q_i$ are pairwise disjoint,
and each occupies exactly $L/P_i$ residues modulo $L$. Counting these residues
proves

$$
\sum_{i=1}^k\frac1{P_i}\le1.
$$

Repeated moduli are allowed. Identical classes cannot occur in an irredundant
cover. Pruning a cover to an irredundant subcover supplies these private sets
only for the retained classes; it supplies none for discarded classes.
If $k=1$, coverage forces $n_1=1$, and $W_1=Q_1=\mathbb Z$, $P_1=1$.

## Simpson's minimum-modulus bound

For a positive integer $m$, define

$$
g_{\mathrm S}(m)
=\sum_{p^\alpha\parallel m}\bigl((\alpha-1)(p-1)+1\bigr),
\qquad g_{\mathrm S}(1)=0.
$$

The subscript distinguishes Simpson's arithmetic function from the
rigidity-defect notation used elsewhere. In
[[../library/covering_systems/simpson_1997_crittenden_vanden_eynden_coverings/_index|Simpson's 1997 paper]],
Theorem 1, printed p. 397, says that if a finite collection $\mathcal A$ of
arithmetic progressions does not cover $\mathbb Z$, and $P$ is the least
positive modulus for which some progression is disjoint from its union, then
$|\mathcal A|\ge g_{\mathrm S}(P)$. Its hypotheses do not require distinct
moduli, pairwise disjointness, or irredundancy of $\mathcal A$.

Apply this theorem to $\mathcal A_i=(C_j)_{j\ne i}$. Its omitted set is
exactly $W_i$, and its minimum omitted-progression modulus is exactly $P_i$.
It follows that

$$
g_{\mathrm S}(P_i)\le k-1.
$$

An arbitrary private progression does not meet this minimum hypothesis. For
example, the even and odd classes form an irredundant two-class cover, while
$0+2^r\mathbb Z$ is private for the even class for every $r\ge1$ and has
$g_{\mathrm S}(2^r)=r$. The theorem also does not supply this bound merely
from a least step through a preselected private point.

Write

$$
s_i=\sum_p v_p(n_i),\qquad t_i=\sum_p v_p(P_i).
$$

Divisibility gives $s_i\le t_i$. For every prime $p$ and integer $\alpha\ge1$,

$$
(\alpha-1)(p-1)+1-\alpha=(\alpha-1)(p-2)\ge0.
$$

Thus the source theorem also gives

$$
0\le s_i\le t_i\le g_{\mathrm S}(P_i)\le k-1.
$$

## Nonuniform set pairs and private points

The finite-set inequality needed below allows each pair to have different
sizes. If $(A_i,D_i)_{i=1}^N$ are finite sets satisfying

$$
A_i\cap D_i=\varnothing,
\qquad A_i\cap D_j\ne\varnothing\quad(i\ne j),
$$

where the second condition holds for every ordered pair of distinct indices,
then

$$
\sum_{i=1}^N\binom{|A_i|+|D_i|}{|D_i|}^{-1}\le1.
$$

This is the Bollobás inequality stated in
[[../library/set_systems/ellis_2010_irredundant_families_subcubes/_index|Ellis's arXiv:1003.2960v1]],
Theorem 3, p. 6. Ellis attributes it to Bollobás (1965) and refers its proof
to reference [3], Bollobás's 1986 book. The following permutation proof is a
local reconstruction, not a report of reading that book's proof.

Uniformly order the finite ground set $\bigcup_i(A_i\cup D_i)$. Let $E_i$
be the event that every element of $A_i$ precedes every element of $D_i$.
Because the two sets are disjoint, their relative order is uniform and

$$
\Pr(E_i)=\frac{|A_i|!\,|D_i|!}{(|A_i|+|D_i|)!}
        =\binom{|A_i|+|D_i|}{|D_i|}^{-1}.
$$

For $i\ne j$, choose $u\in A_i\cap D_j$ and $v\in A_j\cap D_i$.
They are distinct, since equality would put their common element in
$A_i\cap D_i$. Event $E_i$ requires $u$ before $v$, and $E_j$ requires $v$
before $u$. The events are therefore pairwise disjoint, proving the inequality
by summing their probabilities. This also handles an empty family and a
single pair with an empty side. With at least two pairs, the cross-intersection
conditions force every side to be nonempty.

Now let $\Omega=\prod_{j\in V}\Omega_j$ be a finite product of finite nonempty
domains, with $V$ finite. An atomic cylinder $B$ fixes one value in each
coordinate of its specified support $I_B\subseteq V$, leaving the other
coordinates unrestricted. Take a finite indexed irredundant cover by such
cylinders, and choose a private point $z_B$ for each cylinder.

Fix $x\in\Omega$ and consider only the cylinders containing $x$. For each,
put

$$
A_B(x)=\{j\in V:(z_B)_j\ne x_j\},
\qquad h_B(x)=|A_B(x)|.
$$

Since $x,z_B\in B$, they agree on $I_B$, so $A_B(x)\cap I_B=\varnothing$.
For distinct $B,B'$ containing $x$, privacy gives $z_B\notin B'$. Thus some
coordinate of $I_{B'}$ differs between $z_B$ and $x$, because $x$ satisfies
all the fixed coordinates of $B'$. This proves
$A_B(x)\cap I_{B'}\ne\varnothing$ for both orders of each pair. Applying the
set-pair inequality to $(A_B(x),I_B)$ gives

$$
\sum_{B\ni x}\binom{|I_B|+h_B(x)}{|I_B|}^{-1}\le1.
$$

The proof uses neither a binary alphabet nor a common support size. Moreover,
the private points can be chosen separately for each $x$: the argument is
pointwise and imposes no relation between choices at different frame points.

## Digitization and the discounted budget

Return to the congruence cover and its selected private progressions. Write
$L=\prod_{p\mid L}p^{e_p}$. The Chinese remainder correspondence and unique
base-$p$ expansions identify residues modulo $L$ with

$$
\Omega=\prod_{p\mid L}\prod_{r=0}^{e_p-1}\{0,\ldots,p-1\}.
$$

For $L=1$, this empty product has one point.
Coordinate $(p,r)$ is the coefficient of $p^r$ in the residue modulo
$p^{e_p}$. Each class $C_i$ becomes one cylinder fixing the lowest
$\alpha_{i,p}=v_p(n_i)$ digits at each prime. Its support is

$$
I_i=\{(p,r):0\le r<\alpha_{i,p}\},\qquad |I_i|=s_i.
$$

No owner is split into additional classes. The same correspondence turns
$Q_i$ into a cylinder with support

$$
J_i=\{(p,r):0\le r<\beta_{i,p}\},
\qquad \beta_{i,p}=v_p(P_i).
$$

Here $I_i\subseteq J_i$, since $n_i\mid P_i$, and $\beta_{i,p}\le e_p$,
since $P_i\mid L$. The fixed digits on $I_i$ agree with those of $C_i$.
Every point of the $Q_i$ cylinder is private to $C_i$.

For each fixed $x\in\Omega$, choose $z_i(x)$ by using $b_i$'s fixed digits
on $J_i$ and $x$'s digits on its complement. This point lies in $Q_i$ and is
therefore private to $C_i$. If $x\in C_i$, the two points agree on $I_i$ and
outside $J_i$. Their differing coordinates are exactly the extra constrained
digits in $J_i\setminus I_i$ at which $x$ differs from $b_i$.

Under uniform $x\in\Omega$, conditioned on $x\in C_i$, all coordinates
outside $I_i$ remain independent and uniform in their respective alphabets.
Define

$$
\delta_{i,p}=\beta_{i,p}-\alpha_{i,p}\ge0,
\qquad R_i=\sum_{p\mid L}R_{i,p},
\qquad R_{i,p}\sim\operatorname{Binomial}
          \left(\delta_{i,p},\frac{p-1}{p}\right),
$$

with independent $R_{i,p}$. Each extra $p$-digit differs from the fixed digit
with probability $(p-1)/p$. Hence $h_i(x)$, conditionally on $x\in C_i$, has
exactly the law of $R_i$. Set

$$
K_i=\mathbb E\binom{s_i+R_i}{s_i}^{-1}.
$$

Apply the pointwise cylinder inequality using the choices $z_i(x)$, and then
average over the finite frame. Since $\Pr(x\in C_i)=1/n_i$, finite
linearity of expectation gives

$$
\sum_{i=1}^k\frac{K_i}{n_i}\le1.
$$

For $s_i\ge1$, an equivalent exact expression is

$$
K_i=s_i\int_0^1 t^{s_i-1}
       \prod_{p\mid L}\left(1-\left(1-\frac1p\right)t\right)^{\delta_{i,p}}
       \,dt.
$$

Indeed, integration by parts gives, for integers $s\ge1$ and $r\ge0$,

$$
s\int_0^1 t^{s-1}(1-t)^r\,dt
=\frac{s!\,r!}{(s+r)!}=\binom{s+r}{s}^{-1}.
$$

Taking the finite expectation inside the integral and using independence
replaces $(1-t)^{R_i}$ by the displayed product. If $s_i=0$, then $n_i=1$;
irredundancy forces the one-class case. In that case $P_i=1$, $R_i=0$ and
$K_i=1$ directly. The integral formula is not used with $s_i=0$.

Finally, $0\le R_i\le t_i-s_i$ and the binomial coefficient
$\binom{s_i+r}{s_i}$ is nondecreasing in $r$. Therefore

$$
K_i\ge\binom{t_i}{s_i}^{-1}
     \ge\binom{k-1}{s_i}^{-1},
\qquad
\sum_{i=1}^k\frac1{n_i\binom{k-1}{s_i}}\le1.
$$

The second comparison uses Simpson's theorem through $t_i\le k-1$.
All denominators are defined because $0\le s_i\le t_i\le k-1$; for the
one-class case the binomial coefficient is $\binom00=1$.

## Missing transfers and source-reading limits

The weights satisfy $0<K_i\le1$. Dropping them from the reciprocal budget
would strengthen its conclusion and is not justified by this proof. Nor is a
uniform strict bound obtained that contradicts every hypothetical cover by
distinct odd moduli greater than one. The argument establishes necessary
inequalities, but supplies no strict slack sufficient to settle Problem 7.

The moduli $P_i$ belong to private subprogressions, not to replacement owners.
In particular, $n_i\mid P_i$ does not transfer a lower bound on
$\gcd(P_i,P_j)$ to a lower bound on $\gcd(n_i,n_j)$. Likewise, the disjoint
ordering events are attached to owners at one fixed point $x$. They do not
provide a simultaneous allocation of owner capacity to several projected
arithmetic rows. A charging map with a justified nonreuse or capacity rule
remains missing. Neither private-progression density nor pointwise set-pair
weights supply that row-resource bridge.

The deductions use no local L-claim. The arithmetic correspondence, the gcd
replacement, the permutation proof and the averaging argument are supplied
here. Simpson's Theorem 1 is the external premise for the bounds involving
$k-1$. Its definition and statement on printed pp. 396-397 and complete proof
on pp. 398-399 were inspected visually in the retained 1997 publisher PDF.
That proof's cited CRT reference was not read; ordinary CRT and the elementary
gcd intersection criterion are the arithmetic interfaces used here. This
focused reading does not claim independently accepted source-proof coverage.

For Ellis, the retained source is arXiv:1003.2960v1, dated 15 March 2010, not
the later published article. Its identity on p. 1, nonuniform inequality and
proof referral on p. 6, and reference [3] on p. 23 were inspected visually.
Reference [3] is B. Bollobás, *Combinatorics: Set systems, hypergraphs,
families of vectors, and combinatorial probability*, Cambridge University
Press, 1986. Neither that book nor the original 1965 paper was read. No
equality characterization or complete Meshulam-bound proof is used. The local
permutation proof supplies the finite-set argument needed for this account.

The composition remains author-recorded and unreviewed. It carries no
independent mathematical acceptance, formal verification, novelty claim, or
new assessment of the erdosproblems.com problem's status.
