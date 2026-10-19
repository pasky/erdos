---
name: research/erdos_940/independent/canonical_decomposition_and_quartic_zero_target
title: 'Independent record: Erdős Problem 940'
desc: Unverified independent record; selected claims were checked separately in the current topical notes.
tags: []
sources: []
created: 2026-09-22T16:39:33Z
updated: 2026-09-22T16:39:33Z
---


# Independent record: Erdős Problem 940

***

## 1. Scope, sources, and outcome

This record collects the proofs, calculations, failed approaches, and gaps of
this investigation; it does not report a solution of an open case.

Write $\mathcal F_r$ for the positive $r$-powerful integers, including 1,
and

$$
S_r=\bigcup_{1\le j\le r}j\mathcal F_r.
$$

The questions must remain separate:

* For $r=3$, positive lower density of $\mathbb N\setminus S_3$ is
  established background from the supplied Beyer de Ryke manuscript. It was not
  re-audited or claimed as a new result.
* Whether $S_3$ has density zero was not resolved.
* For every $r\ge4$, neither infinitude of $\mathbb N\setminus S_r$ nor the
  density-zero question was resolved.
* No unconditional positive-density result for any $S_r$ was obtained.

Only the supplied files were used; there was no browsing. The full Markdown of
Beyer de Ryke was read before using its canonical decomposition and counting
framework. No theorem from Wang or Browning–Verzobio is invoked as an
unconditional input below. In particular, no conditional six-cube energy bound,
and no estimate for primitive ternary equations with powerful output, has been
promoted to an estimate for $S_r$.

The strongest completed arguments are:

1. An exact equivalence between density zero for $S_r$ and density zero for
   every fixed positive integer-coefficient diagonal degree-$r$ form in $r$
   variables.
2. Exact quartic zero-target local counts, including both a harmonic saving and
   coefficient patterns with the opposite behavior.
3. A global upper-density bound below $1/4$, and an upper relative-density
   bound below $1/200$ in $15\pmod{16}$, for a specified paired-coefficient
   subfamily of $S_4$, not for $S_4$ itself.
4. An exact finite certificate showing that one specified 32-assignment quartic
   upper-bound construction cannot prove the desired deficit.

The polished account is `solution.md`. The present record includes additional
unsuccessful mechanisms and the status of the numerical work.

## 2. Canonical decomposition and what it actually reduces

Define

$$
\mathcal C_r=\left\{\prod_{s=1}^{r-1}b_s^{r+s}:
 b_s\text{ squarefree and pairwise coprime}\right\}.
$$

Every $n\in\mathcal F_r$ is uniquely $dx^r$, with $d\in\mathcal C_r$,
$x\ge1$. Indeed, for a positive prime exponent $e\ge r$, use canonical
exponent 0 if $e\equiv0\pmod r$, and canonical exponent $r+s$ if
$e\equiv s\pmod r$, $1\le s<r$. The remainder is a nonnegative multiple of
$r$.

For $\sigma>1/(r+1)$,

$$
\sum_{d\in\mathcal C_r}d^{-\sigma}
=\prod_p\left(1+\sum_{s=1}^{r-1}p^{-(r+s)\sigma}\right)<\infty.
$$

In particular, put

$$
W_r=\sum_{d\in\mathcal C_r}d^{-1/r}.
$$

Then

$$
\#(\mathcal F_r\cap[1,X])\le W_rX^{1/r}.
$$

Sums with fewer than $r$ summands therefore contribute only $O_r(X^{1-1/r})$
integers.

For a coefficient tuple $\mathbf d$, let

$$
A_{\mathbf d}=\{d_1x_1^r+\cdots+d_rx_r^r:x_i\ge1\}.
$$

For finite $E\subset\mathcal C_r$, put
$U_E=\bigcup_{\mathbf d\in E^r}A_{\mathbf d}$ and
$W_E=\sum_{d\in E}d^{-1/r}$. The uniform estimate is

$$
\#((S_r\setminus U_E)\cap[1,X])
\le O_r(X^{1-1/r})+X(W_r^r-W_E^r).                    \tag{2.1}
$$

Proof: for each tuple $\mathbf d$, dropping the sum condition in favor of the
individual conditions $d_ix_i^r\le X$ bounds its representations by
$X\prod_i d_i^{-1/r}$. Sum over tuples outside $E^r$.

This has a quantitative version. If $0<\eta<1/[r(r+1)]$, then

$$
\sum_{d>D}d^{-1/r}
\le D^{-\eta}\sum_d d^{-1/r+\eta}
=O_{r,\eta}(D^{-\eta}).
$$

Thus taking $E=\mathcal C_r\cap[1,D]$ makes the error in (2.1)
$O_r(X^{1-1/r})+O_{r,\eta}(XD^{-\eta})$.

### Exact density-zero equivalence

For fixed $r$, the following are equivalent:

* $d(S_r)=0$.
* Every $A_{\mathbf d}$, $\mathbf d\in\mathcal C_r^r$, has density zero.
* Every positive integer-coefficient form $\sum_{i=1}^r c_ix_i^r$ has a
  density-zero positive value set.

The first implication is containment. The second implies the first by the finite
union $U_E$ and (2.1), followed by exhaustion of $\mathcal C_r$. For the
arbitrary coefficients, set $L=\operatorname{rad}(c_1\cdots c_r)$. Each
$L^rc_i$, and hence each $L^rc_ix_i^r$, is $r$-powerful. Therefore

$$
L^rA_{\mathbf c}\subseteq S_r.
$$

Density zero of $S_r$ implies density zero of $A_{\mathbf c}$, since $L$
is fixed. The converse includes the canonical coefficient tuples.

This is a genuine equivalence, but not a solution of the resulting fixed-form
problem. It prevents an argument from attributing positive density exclusively
to canonical coefficients tending to infinity. If $S_r$ has positive upper
density, some single fixed canonical form has positive upper density: choose a
finite core with smaller tail, then use the finite union bound.

There is no proved upgrade to positive *lower* density for that one form.
Homogeneity alone cannot supply it. To see this, partition the positive integers
into alternating intervals $[M_j,M_{j+1})$, with $M_j/M_{j+1}^{1-1/r}\to0$,
and close the two alternating unions under multiplication by positive $r$-th
powers. The resulting two homogeneous sets cover $\mathbb N$, but each has
lower density zero. At the end of a band of the opposite parity, all
contributing bases are below $M_j$, giving at most $M_jX^{1/r}=o(X)$
elements. This is not an example of diagonal-form images; it disproves only the
proposed inference from homogeneity.

### First-moment counting is critical, not subcritical

Let $V_r=\operatorname{vol}\{\mathbf t\ge0:\sum t_i^r\le1\}=\Gamma(1+1/r)^r$.
Riemann sums for a fixed coefficient tuple, dominated by its summable weight,
give

$$
\#\{(n_1,\ldots,n_r)\in\mathcal F_r^r:\sum n_i\le X\}
\sim V_rW_r^rX.
$$

The unordered count is asymptotic to $V_rW_r^rX/r!$, since tuples with a
repeated actual summand number $O_r(X^{1-1/r})$. This cannot yield $o(X)$
merely by counting tuples. Early finite Euler-product computations through
primes below 200,000 gave unordered constants approximately 11.88 for $r=3$
and 233.82 for $r=4$; these were truncated products, not certified values of
the infinite constants.

## 3. Exact congruence obstructions do not exist for the full sumset

For every modulus $M$, every residue class contains a sum of two positive
$r$-powerful integers.

Choose $e\ge r$ coprime to $\varphi(M)$. At an odd prime power dividing
$M$, any target is a sum of two units: the first unit need only avoid 0 and
the target modulo the prime. At a power of 2, an even target is a sum of two
units; an odd target is zero plus a unit. The $e$-th power map permutes units
modulo each prime power, and zero is an $e$-th power. CRT gives positive
$x,y$ with $x^e+y^e$ in the prescribed class. Both powers are
$r$-powerful.

Thus the useful congruence strategy must count representations sparsely within a
class. It cannot produce an empty class for the entire $S_r$. Closure under
perfect $r$-th-power multiplication also does not contradict cofiniteness, and
the critical first moment supplies no such contradiction.

## 4. General local estimates and the distinction between zero and nonzero targets

For a prime $p$, unit coefficients $a_i$, and $u\in\mathbb F_p$, set

$$
N_p(u;\mathbf a)=\#\{\mathbf x\in\mathbb F_p^r:\sum a_ix_i^r=u\},
\qquad \rho_p=p^{1-r}N_p.
$$

With $C_r=(r-1)^r$, elementary character expansion gives

$$
|\rho_p(u;\mathbf a)-1|\le
\begin{cases}
C_rp^{-(r-1)/2},&u\ne0,\\
C_rp^{-(r-2)/2},&u=0.
\end{cases}                                                   \tag{4.1}
$$

To prove this, put $g=\gcd(r,p-1)$. For nonzero additive frequency $s$, the
power sum is a sum of $g-1$ Gauss sums of magnitude $\sqrt p$. Expanding the
product over $r$ coordinates leaves at most $(g-1)^r$ terms. The remaining
sum over $s\ne0$ has magnitude at most $\sqrt p$ for nonzero target, whereas
for target zero it is either zero or $p-1$. Including the orthogonality factor
$1/p$ gives (4.1).

For $r\ge5$, these errors are summable over primes. For a fixed coefficient
tuple, adding sufficiently large good primes cannot make the product of local
factors arbitrarily small: once the errors are at most $1/2$,

$$
\prod_{p\in\mathcal Q}\rho_p
\ge \exp\left(-2C_r\sum_{p\ge Q}p^{-(r-2)/2}\right)>0.
$$

This statement concerns the specified large-good-prime mechanism, not the
density of $S_r$.

Prime powers do not improve that mechanism. If $p\nmid ra_1\cdots a_r$, all
nonzero solution vectors modulo $p$ are nonsingular and each lifts to exactly
$p^{(k-1)(r-1)}$ solutions for each prescribed target lift. Hence

$$
\rho_{p^k}(u;\mathbf a)\ge
\begin{cases}
\rho_p(u;\mathbf a),&p\nmid u,\\
\rho_p(0;\mathbf a)-p^{1-r},&p\mid u.
\end{cases}
$$

The first line is equality. The additional error is again summable. Small or bad
primes are not covered by this conclusion.

## 5. Quartic zero-target calculation

Let $p$ be odd and not divide the four coefficients. If $p\equiv3\pmod4$,
the square and fourth-power maps have equal fiber cardinalities over each
target. Quadratic Gauss sums give

$$
\rho_p(0;\mathbf d)
=1+\frac{p-1}{p^2}\left(\frac{d_1d_2d_3d_4}{p}\right).       \tag{5.1}
$$

For $p\equiv1\pmod4$, choose a quartic character $\chi$, and put

$$
z_i=\chi(d_i),\quad D=\prod_i z_i,\quad
\epsilon=\chi(-1),\quad J=J(\chi,\chi).
$$

Then $|J|=\sqrt p$, and the exact formula is

$$
\rho_p(0;\mathbf d)
=1+\frac{p-1}{p^2}\left(B+2\Re\frac{J^2}{pD}\right),         \tag{5.2}
$$

where

$$
B=D^2\left[1+\epsilon\left(\left|\sum_i z_i\right|^2-4\right)\right]
 +D\sum_{i<j}z_i^2z_j^2.                                  \tag{5.3}
$$

In particular $B$ is an integer and the harmonic trace differs from it by at
most 2.

Derivation: if $G_j=\tau(\chi^j)$, the nonzero-frequency power sum is
$\sum_{j=1}^3\chi^{-j}(sd)G_j$. Orthogonality retains exactly the exponent
patterns 1111, 3333, 1133, 2222, 1223, with multiplicities 1, 1, 6, 1, 12. Use

$$
G_1G_3=\epsilon p,\quad G_2^2=p,\quad
G_1^2=JG_2,\quad G_3^2=\overline JG_2.
$$

These give (5.2)–(5.3).

Writing the digit $a$ for $i^a$, the complete table up to permutation,
common multiplication, and conjugation is

| Pattern | $B$, $\epsilon=1$ | $B$, $\epsilon=-1$ |
|---|---:|---:|
| 0000 | 19 | -5 |
| 0001 | -7 | 5 |
| 0002 | -5 | -5 |
| 0011 | 7 | -1 |
| 0012 | 1 | -3 |
| 0013 | -1 | -1 |
| 0022 | 3 | 11 |
| 0123 | -1 | 7 |

If every coefficient is a fourth power and $p\equiv5\pmod8$, then $B=-5$, so

$$
\rho_p(0;\mathbf d)\le1-3(p-1)/p^2\le1-2/p.              \tag{5.4}
$$

This is a harmonic-size saving and initially looked capable of extending the
cubic argument.

The immediate obstruction is canonical coefficient $64=2^6$. At
$p\equiv5\pmod8$, $\chi(64)=-1$; one cannot make all canonical coefficients
fourth powers while preserving this prime class. More decisively, the canonical
tuple $(1,1,64,64)$ satisfies $\rho_p(0)>1$ at **every odd prime**. At
$p\equiv3\pmod4$ its factor is $1+(p-1)/p^2$. At $p\equiv1\pmod8$ its
trace lies in $[17,21]$, and at $p\equiv5\pmod8$ in $[9,13]$.

An important correction made during the investigation: replacing canonical
coefficients $(1,1,64,64)$ by $(1,1,4,4)$ absorbs a factor $2^4$ into the
last variables, which must then be even. The forms are equivalent at odd primes,
but not as unrestricted integral or 2-adic value sets. A preliminary
universality argument involving normalized $(1,2,4,8)$ and canonical
$(1,32,64,128)$ was discarded for the same reason. The latter has odd values
only in $1\pmod{16}$.

## 6. The paired quartic family: rigorous bounds, limited scope

Consider tuples equivalent, by permutation, a common positive rational factor,
and individual rational fourth-power factors, to

$$
(1,4,a,4a),\qquad a>0.                                  \tag{6.1}
$$

Their zero-target factor exceeds 1 at every good odd prime. Their coefficient
product is a square, handling (5.1). For (5.2), use
$\chi(4)=\chi(-1)=\epsilon$, which follows from $(1+i)^4=-4$. The character
pattern becomes $(1,\epsilon,z,\epsilon z)$. Its $B$-values are 19, 7, 3
when $\epsilon=1$, and 11 or 7 when $\epsilon=-1$. Thus the trace in (5.2)
is always at least 1.

For canonical coefficients, (6.1) has an elementary exact description. A paired
coefficient pair has equal odd parts and dyadic exponents either $(0,6)$ or
$(5,7)$, in either order. A tuple belongs to the family if one of its three
pair partitions consists of two such pairs. Let $\mathcal P\subseteq S_4$ be
the values represented by this family.

Set

$$
V=\Gamma(5/4)^4\le1,\quad
L=1/\sqrt2+1/4,
$$


$$
W=\prod_{p\text{ odd}}(1+p^{-5/2}+p^{-3}+p^{-7/2}),\quad
Z=\prod_{p\text{ odd}}(1+p^{-5}+p^{-6}+p^{-7}).
$$

The total ordered coefficient weight is exactly

$$
\sum_{\mathbf d\text{ paired}}(d_1d_2d_3d_4)^{-1/4}
=3L^2W^2-\frac{27}{32}Z.                                \tag{6.2}
$$

For one pairing, each odd-prime pair contributes $1+p^{-5/2}+p^{-3}+p^{-7/2}$;
the dyadic ordered pair contributes $L$. Intersections of two pairing
conditions have weight $(9/32)Z$. The triple intersection is empty, since
three pairwise differences cannot all be 2 modulo 4. Inclusion–exclusion proves
(6.2).

For fixed $\mathbf d$, lattice counting gives $VX\prod_i d_i^{-1/4}+o(X)$;
the summable weights justify passage to the entire family. Repeated actual
summands contribute $O(X^{3/4})$, and all other permutation orbits have size
24. Consequently

$$
\overline d(\mathcal P)
\le\frac V{24}\left(3L^2W^2-\frac{27}{32}Z\right)
\le\frac V8L^2W^2<\frac14.                              \tag{6.3}
$$

For the last strict inequality, with $f(t)=t^{-5/2}+t^{-3}+t^{-7/2}$,

$$
\log W\le\sum_{n\ge3,\ n\text{ odd}}f(n)
\le f(3)+\tfrac12\int_3^\infty f(t)dt<1/4.
$$

Thus $W^2<\sqrt e<2$, and $L<1$. The sharper expression in (6.3) is
numerically about 0.08378684, but that decimal is not needed for the proof.

### A stronger dyadic-relative bound

Put

$$
C_{15}=\sum_{t\in\mathcal C_4,\ t\equiv15\ (16)}t^{-1/2},
\quad h=2^{-3/2},\quad K=2(h+1/8)W=LW.
$$

Then

$$
\limsup_{X\to\infty}\frac{16}{X}
\#\{n\le X:n\in\mathcal P,\ n\equiv15\pmod{16}\}
\le4VhC_{15}K<1/200.                                    \tag{6.4}
$$

Reason: a paired tuple has at most two odd coefficients. For an odd target,
exactly one variable attached to an odd coefficient must be odd. Odd fourth
powers are 1 modulo 16, so that coefficient must be 15 modulo 16. If there are
$k$ such positions, the normalized local factor is at most $8k$. For a fixed
pairing and a designated such position, its pair has weight $hC_{15}$, and the
other pair has weight $K$. Sum over four positions and three pairings to
obtain $96hC_{15}K$, then multiply by $V/24$.

`check_higher_r_bounds.py` is an exact rational certificate for

$$
W<1.182,\qquad C_{15}<0.003,
$$

and hence (6.4). It convolves local masses in the residue classes modulo 16 for
odd primes through 97. The finite total is below 1.181 and the finite mass at 15
below 0.00206. Upper bounds for $1/\sqrt p$ are obtained by rational ceilings
with denominator $10^{12}$. The logarithm of the omitted product is at most

$$
U=\int_{100}^\infty(t^{-5/2}+t^{-3}+t^{-7/2})dt
=1081/1500000.
$$

Using $e^U\le(1-U)^{-1}$ certifies the displayed bounds. Finally
$h<177/500$, $V\le1$, and direct rational substitution gives
$4VhC_{15}K<1/200$. The certificate was run successfully.

Neither (6.3) nor (6.4) bounds all of $S_4$. No reduction was proved forcing
arbitrary representations into this family.

### Finite-character classification and an additional angular uncertainty

A stronger algebraic calculation, recorded in `notes_quartic_trace.md`,
classifies the square-product rational tuples for which $B\ge3$ for every
allowable finite quartic-character assignment: they are precisely (6.1), up to
the indicated equivalences. This is a classification robust to **every**
Jacobi-sum angle, not a claimed classification of all actual prime behavior.

The finite group calculation is as follows. Normalize the first coefficient to
1. Valuation columns lie in
$\{(x_1,x_2,x_3)\in(\mathbb Z/4)^3:x_1+x_2+x_3\text{ even}\}$. Let $H$ be
generated by the odd-prime columns, let $v$ be the column at 2, and set
$G=H+\langle2v\rangle$. The $\epsilon=1$ allowed set $B\ge3$ is the union
of the three cyclic lines generated by $(0,1,1),(1,0,1),(1,1,0)$. A subgroup
in this union is contained in one line or is the Klein four group of the three
doubled generators. The latter is incompatible with the $\epsilon=-1$ allowed
coset, whose elements are the three doubled generators and the six permutations
of $(1,2,3)$. The surviving line-and-coset alternatives give the valuation
pattern of $(1,4,a,4a)$.

Translating freely prescribed prime characters into positive-density prime
classes uses finite Kummer theory and Chebotarev. For square-product tuples
outside (6.1), the algebraic result only guarantees an assignment with
$B\le-1$. If $B\le-3$, the trace is negative regardless of angle. If
$B=-1$, it is not. The tuple $(1,1,2,2)$ illustrates this: for
$p\equiv5\pmod8$, its trace is $-1-2\Re(J^2/p)$, positive at 5 and negative
at 13. A suitable angular prime-distribution theorem would be additional input;
none was proved or invoked to resolve the problem. Also, individual
suppressibility would not automatically produce a common progression suppressing
the weighted union.

## 7. Exact missing progression estimate and the repaired tail bound

For fixed $M$, define

$$
\rho_M(a;\mathbf d)=M^{-3}
\#\{\mathbf x\pmod M:\sum_i d_ix_i^4\equiv a\pmod M\}.
$$

Lattice counting in residue classes and dominated convergence give the ordered
representation count, after division by $X$, tending to

$$
\frac V M\sum_{\mathbf d\in\mathcal C_4^4}
\left(\prod_i d_i^{-1/4}\right)\rho_M(a;\mathbf d).       \tag{7.1}
$$

Domination for fixed $M$ comes from the unrestricted bound
$X\prod_i d_i^{-1/4}$. A sufficient condition for a positive-density
complement of $S_4$ would be

$$
\frac V{24}\sum_{\mathbf d\in\mathcal C_4^4}
\left(\prod_i d_i^{-1/4}\right)\rho_M(a;\mathbf d)<1.     \tag{7.2}
$$

Repeated summands and shorter sums are $o(X)$. No modulus satisfying (7.2) was
established.

The central failure of the straightforward quartic extension is now explicit:
zero-target restrictions suppress some coefficient patterns but amplify every
good-prime local factor of (6.1). Small global density of that family does not
bound its relative density in a much sparser progression. Even its small
relative density in $15\pmod{16}$ cannot simply be retained after adding many
homogeneous odd-prime restrictions.

A technical tail issue was identified and repaired. For zero target, if all four
coefficients vanish modulo $p$, then $\rho_p=p$, so the cubic-style product
of bounded prime-divisor weights is insufficient. Use instead

$$
H(\mathbf d)=4^{\sum_i\omega(d_i)}
\operatorname{rad}(\gcd(d_1,d_2,d_3,d_4))\prod_i d_i^{-1/4}.
$$

Its sum is finite: if $u_p=p^{-5/4}+p^{-3/2}+p^{-7/4}$, its Euler factor is

$$
(1+4u_p)^4+(p-1)(4u_p)^4=1+O(p^{-5/4})+O(p^{-4}).
$$

For odd $p$, character expansion for unit coefficients, and fixing all but one
active variable otherwise, give

$$
\rho_p(0;\mathbf d)\le(1+81/p)
4^{\sum_i\mathbf1_{p\mid d_i}}
 p^{\mathbf1_{p\mid\gcd(d_1,d_2,d_3,d_4)}}.
$$

Thus for squarefree odd $M$ with $\sum_{p\mid M}1/p\le T$, the weighted
product is bounded by $e^{81T}H(\mathbf d)$. Tail control is uniform for a
**fixed reciprocal-prime budget**, not for unrestricted $T$. The unsolved part
is the main-term saving, not this technical summability issue.

## 8. A concrete finite quartic optimization: rigorous failure of one version

The attempted restriction was

$$
\chi(\ell)=\psi(\ell\bmod16)\quad(\ell\text{ odd prime}),
\qquad\chi(2)=i^t,
$$

where $\psi$ ranges over the eight characters of $(\mathbb Z/16)^\times$ and
$t=0,1,2,3$. These give 32 finite-character prescriptions. For canonical
$d=2^eu$, its type is $(e\bmod4,u\bmod16)$, also one of 32 possibilities.

Let $Z_v=\sum_{u\text{ odd canonical},\ u\equiv v(16)}u^{-1/4}$, and let
$a_0=1,a_1=2^{-5/4},a_2=2^{-6/4},a_3=2^{-7/4}$. The coefficient weight of type
$(E,v)$ is $a_EZ_v$. For a multiset of four types, let $m_s$ be its
multiplicities, and let $P$ be the probability that the active odd-coefficient
subset sums to 15 modulo 16. Explicitly, $P$ is its number of successful
subsets divided by $2^k$, where $k$ is the number of odd coefficients. Its
contribution to relative unordered tuple counting is

$$
w=16VP\prod_s(a_EZ_v)^{m_s}/\prod_s m_s!.
$$

Bounding the unknown Jacobi term by 2 gives the convex exponential objective

$$
F(\boldsymbol\lambda)=\sum_{\text{type multisets}}w
\exp\left(\sum_g\lambda_g(B_g+2)\right),
\qquad\lambda_g\ge0.                                   \tag{8.1}
$$

The $\lambda_g$ represent reciprocal-prime budgets; starting primes
sufficiently far out makes the quadratic errors small. A successful bound below
1 would have supplied the required main-term target for this construction, with
the tail argument handled separately.

There is an **exact finite obstruction** to (8.1), not just an optimizer
failure. There are 364 type multisets with $P>0$ for which $B_g+2\ge0$ for
all 32 prescriptions. Their weights cannot decrease. Using only odd canonical
coefficients supported on primes through 251, and replacing $V$ by the lower
bound $1/4$, their total weight exceeds

$$
\frac{4167280525630629767083012259181277616191488}
{3840000000000000000000000000000000000000000}>1.08.
$$

The lower bound $V\ge1/4$ follows from the cube $[0,1/\sqrt2]^4$ inside the
quartic unit ball. `check_quartic_residue_obstruction.py` verifies the finite
inequality using integer arithmetic, downward-rounded coefficient weights, and
exact traces. It was run successfully. Therefore (8.1) exceeds 1.08 for every
nonnegative $\boldsymbol\lambda$.

This does **not** rule out other character prescriptions, sharper phase use,
small-prime effects, or bounds for distinct values better than tuple counting.

Exploratory, non-certified optimization used odd-prime Euler factors through
2,000,000 and obtained type masses approximately

$$
(1.401040,.578255,.431980,.400121,.640903,.489147,.383298,.315425)
$$

in residues $1,3,5,7,9,11,13,15$. The associated truncated objective started
near 130.1292. The safe objective had its numerical minimum at zero budgets.
Allowing independently selectable Jacobi phases on a 16-angle grid produced
about 130.0506, and setting their average to zero gave about 130.0835. These are
truncated Euler-product experiments with hypothetical phase freedom, not
certified infinite-product optima or statements about actual prime distribution.

A separate bounded search allowed free quartic characters on the first 50 odd
primes, set the remaining characters to 1, and optimized the initial gradient
with the most favorable possible phase. Thirty random coordinate-descent starts
found approximately -22.9245, with no substantially better direction than the
residue-character family. This was not an exhaustive search or a global minimum
proof. The scripts and arrays are preserved; no open statement follows from
these computations.

## 9. Positive density: exact sufficient estimate and unsuccessful constructions

For fixed positive coefficients $\mathbf c$, put
$F(\mathbf x)=\sum_i c_ix_i^r$ and

$$
E_F(N)=\#\{\mathbf x,\mathbf y\in[1,N]^r\cap\mathbb Z^r:F(\mathbf x)=F(\mathbf y)\}.
$$

If $E_F(N)\ll_F N^r$, Cauchy–Schwarz gives $\gg_F N^r$ distinct values below
$(\sum c_i)N^r$. Choosing $N$ from arbitrary $X$, then multiplying by the
fixed $L^r$ of Section 2, gives positive lower density for $S_r$. No form
with this bound was obtained. An $N^{r+\varepsilon}$ estimate is not enough;
nor is a form whose coefficients change with $N$.

For cubics, the collision problem becomes a precise average of ternary quadratic
equations. Put $h_i=x_i-y_i$, $z_i=x_i+y_i$. The box and parity conditions
are

$$
|h_i|\le N-1,\quad |h_i|+2\le z_i\le2N-|h_i|,
\quad z_i\equiv h_i\pmod2,
$$

and the equation is

$$
3\sum_{i=1}^3c_ih_iz_i^2=-\sum_{i=1}^3c_ih_i^3,          \tag{9.1}
$$

since $x_i^3-y_i^3=h_i(3z_i^2+h_i^2)/4$. The transformation is bijective under
these conditions. A log-free $O(N^3)$ total for (9.1) would suffice, but was
not proved. Primitive ternary powerful relations do not estimate these
arbitrary-target, nonprimitive fibers.

### Why enlarging the kernels did not simplify the energy problem

The energy for all powerful summands includes the pure-power self-energy as a
nonnegative subcount. Thus an $O(X)$ energy bound for the full family would
already prove the corresponding critical pure-power bound. Finite unions of
coefficient families also retain each self-energy. Canonical truncation prevents
unbounded kernels alone from supplying positive upper density. A selected
special subfamily could still work, but no such construction was found.

### Widely separated p-adic coefficients do not give mixed-radix injectivity

For $p\nmid r$, take coefficients $p^{e_i}u_i$, $u_i$ units, with
$e_0<e_1$. Set all $y_i=1$, and all $x_i=1$ except $x_0,x_1$. Equality
becomes

$$
x_0^r=1-p^{e_1-e_0}(u_1/u_0)(x_1^r-1).
$$

For any $x_1\in\mathbb Z_p$, the right side is 1 modulo $p$, so Hensel
lifting gives a unique $x_0\in1+p\mathbb Z_p$. If $x_1^r-1$ is a unit, then
$v_p(x_0-1)=e_1-e_0$, although $x_1\not\equiv1\pmod p$. Carries are possible
with arbitrarily large finite coefficient spacing. These are p-adic collisions,
not asserted integer collisions in the box; they invalidate the proposed
coordinatewise congruence recursion, not every global energy approach.

### Independent polynomial summands do not evade the diagonal problem

If a nonconstant $f\in\mathbb Z[x]$ is eventually positive and $f(n)$ is
$r$-powerful for all sufficiently large integers, every irreducible factor of
$f$ has multiplicity at least $r$. Proof: an irreducible factor has
infinitely many prime divisors of its values (Schur's elementary argument).
Exclude finitely many primes dividing coefficients, discriminants, or pairwise
resultants. At a remaining simple root modulo $p$, choose a lift modulo
$p^2$ that is not a root. The valuation of $f(n)$ equals that factor's
multiplicity on an infinite progression, forcing it to be at least $r$.

Consequently $\deg f\ge r$. If $\deg f=r$, then $f=c(ax+b)^r$, with
$\gcd(a,b)=1$, $a>0$, and $c$ a positive $r$-powerful integer. The last
assertion follows by choosing $ax+b$ nonzero modulo each prime dividing $c$.

For at most $r$ independent univariate-polynomial summands, the number of
candidate values is $O(X^{\sum 1/\deg f_i})$, after omitting constants. It is
$o(X)$ unless there are exactly $r$ nonconstant degree-$r$ polynomials.
That remaining case is a fixed diagonal form on arithmetic progressions. This
only limits this construction mechanism; it is not a density-zero theorem for
$S_r$.

### Norm identities and linear symmetries did not supply special forms

A nondegenerate diagonal form $\sum a_ix_i^d$, in at least three variables and
degree $d\ge3$, is absolutely irreducible: its projective hypersurface is
smooth, whereas two positive-degree projective factors would intersect in
singular points. It cannot become a product or a field norm under an invertible
linear change.

Its invertible linear automorphisms are monomial. The Hessian determinant is a
nonzero constant times $\prod_i x_i^{d-2}$. The Hessian transformation rule
forces every transformed coordinate linear form to be proportional to a
coordinate, by unique factorization. Over $\mathbb Q$, only finitely many such
rescalings preserve the fixed coefficients. This excludes the proposed infinite
linear norm-unit symmetry, not nonlinear methods.

Concrete tempting identities were checked:

$$
N_{\mathbb Q(\sqrt[3]2)/\mathbb Q}(x+y\sqrt[3]2+z\sqrt[3]4)
=x^3+2y^3+4z^3-6xyz.
$$

The mixed term cannot be discarded; forcing it to vanish loses a variable and
positive-density scale. Also

$$
x^4+4y^4=(x^2-2xy+2y^2)(x^2+2xy+2y^2)
$$

factors the binary pieces of $x^4+4y^4+a z^4+4a w^4$, not the full
four-variable form. No resulting critical energy bound was obtained.

## 10. Remaining uncertainties and record of artifacts

The principal unresolved alternatives are:

* Prove density zero for every fixed positive diagonal form in the equivalence
  of Section 2.
* Prove positive lower density for one fixed form, for example by the log-free
  energy estimate in Section 9.
* For $r=4$, construct a modulus and class satisfying (7.2), controlling the
  paired family's contribution in that same class.
* For $r\ge5$, find an argument beyond the summable large-good-prime local
  fluctuations. Their summability does not settle either original question.

No claim was made that these sufficient conditions are necessary, apart from the
explicitly proved density-zero equivalence. No conclusion about natural density
existence was obtained. Positive upper density and positive lower density were
kept distinct. The angular prime-distribution input discussed in Section 6
remains additional, unproved input here. Neither the finite method obstruction
nor the failed numerical searches is evidence of a theorem about the full
$S_4$.

The working files this record cites by name (a polished partial account,
eight topical notes, two certificate scripts and three exploratory scripts
with their data) were not retained; the retained re-derivations are the
topical notes and the [evidence scripts](../evidence/_index.md) of this
folder. The names, kept so the citations above stay readable:

* `solution.md`: polished partial account, with the main proofs and exact gaps.
* `notes_reductions.md`: canonical tails, exact reformulation, quantitative
  extraction, homogeneity counterexample.
* `notes_quartic_trace.md`: Gauss/Jacobi formula, character table,
  finite-character classification, paired-family weight.
* `notes_higher_r.md`: general local and prime-power estimates, quartic
  obstruction, dyadic-relative paired bound.
* `notes_quartic_mix.md`: the 32-assignment construction and its certified
  limitation.
* `notes_positive_density.md`: polynomial restriction, p-adic carries,
  quadratic-fiber energy reduction.
* `notes_special_forms.md`: special-coefficient energy criterion, Hessian
  argument, checked norm identities.
* `notes_basis.md`: congruence coverage and limits of counting/scaling
  arguments.
* `check_higher_r_bounds.py`: exact rational certificate for (6.4).
* `check_quartic_residue_obstruction.py`: exact integer certificate for the
  obstruction to (8.1).
* `quartic_residue_mix.py`, `quartic_residue_phase_mix.py`,
  `quartic_gradient_search.py`, and their `.npz` data: exploratory computations,
  not proofs of a global optimum.

The unconditional results in `solution.md`, including the quartic
normalizations, pairing weights, division by 24, relative-density calculation,
and tail Euler factor, were checked independently within this investigation. The
qualification about bounded reciprocal-prime budget and the distinction between
equal fiber cardinalities and equal fibers were incorporated. No open part of
Erdős Problem 940 is claimed resolved.
