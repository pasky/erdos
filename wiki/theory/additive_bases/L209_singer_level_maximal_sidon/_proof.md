---
name: theory/additive_bases/L209_singer_level_maximal_sidon/_proof
desc: |
  Maximality follows from the perfect difference property at every level;
  the strong Sidon property reduces to three families of conditions on the
  level map, and a greedy count satisfies them when h <= p/4.
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# theory/additive_bases/L209_singer_level_maximal_sidon/_proof

[[theory/additive_bases/L209_singer_level_maximal_sidon/_index|..]]

***

Write $G=\mathbb Z_q\times H$, $\bar b=(b,0)$ for $b\in B$ and
$\gamma(x)=(c(x),x)$ for $x\in H$. Since $q=p^2+p+1$ and $h$ are odd, $G$
has odd order, so $2$ is invertible in $\mathbb Z_q$ and $x\ne-x$ for
$x\ne0$ in $H$. The set $B$ is strong Sidon in $\mathbb Z_q$: if
$b_1+b_2=b_3+b_4$ then $b_1-b_3=b_4-b_2$, and uniqueness of differences
forces $\{b_1,b_2\}=\{b_3,b_4\}$. Hence $|B+B|=(p+1)(p+2)/2$.

**Conditions on $c$.** We require

- (S0) $c(0)\in B$, so that $\gamma(0)=\overline{c(0)}$ and $|A|=p+h$;
- (S1) for every $\lambda\in H$, the values $c(y)+c(y')$ over unordered
  pairs $\{y,y'\}$ with $y+y'=\lambda$, $y=y'$ allowed, are distinct;
- (S2) $c(x)+c(-x)\notin B+B$ for $x\ne0$;
- (S3) $c(v)+c(w)-c(v+w)\notin B$ for $v,w\ne0$ with $v+w\ne0$, $v=w$
  allowed.

**These conditions give the strong Sidon property.** A sum of two elements
of $A$ has one of the forms $(b+b',0)$, $(b+c(x),x)$ or
$(c(y)+c(y'),y+y')$. Two sums of the first form coincide only for the same
pair, because $B$ is strong Sidon, and the same holds for the second form
by comparing levels and then residues. Two sums of the third form coincide
only for the same pair by (S1). A sum of the first form equals one of the
second only at level $x=0$, where $\gamma(0)=\overline{c(0)}$ makes both
the same pair of points of $B\times\{0\}$. A sum of the first form equals
one of the third only if $y+y'=0$; for $y\ne0$ this is excluded by (S2),
and $y=y'=0$ is again a pair inside $B\times\{0\}$. A sum of the second
form equals one of the third only if $x=y+y'$ and
$b=c(y)+c(y')-c(y+y')$. If $y=0$ or $y'=0$ the two pairs coincide, as
$\gamma(0)=\overline{c(0)}$; if $y+y'=0$ we are in the previous case; and
otherwise (S3) excludes it.

**Maximality.** Let $g=(\rho,s)\notin A$. If $s\ne0$ then
$\rho\ne c(s)$, and there are $b,b'\in B$ with $b-b'=\rho-c(s)$; then
$g=\gamma(s)+\bar b-\bar b'$, where $\bar b'\ne\bar b$ and
$\bar b'\ne\gamma(s)$ because their levels differ. If $s=0$ then
$\rho\notin B$, so $\rho\ne c(0)$, and there are $b,b'\in B$ with
$b-b'=\rho-c(0)$; then $g=\overline{c(0)}+\bar b-\bar b'$, where
$b'\ne b$, and $b'=c(0)$ would give $\rho=b\in B$. In both cases
$a+b=g+c$ with $\{a,b\}\ne\{g,c\}$, so $A\cup\{g\}$ is not strong Sidon.

**Existence of $c$.** Put $c(0)=\min B$, list the non-zero elements of $H$
in pairs $\{x,-x\}$, and assign the values one at a time, $c(x)$ before
$c(-x)$, each time choosing any residue that violates none of (S1)--(S3)
among the already assigned values. If such a residue always exists, the
final map satisfies (S0)--(S3), since every condition involves finitely
many points and is checked when its last value is assigned.

Let $S$ be the set of points already assigned when $c(x)$ is chosen, so
$0\in S$, $x\notin S$ and $|S|\le h-1$. The residues excluded for $c(x)$
are at most the following.

- (S1): for each $y\in S\cup\{x\}$, the new sum at level $x+y$ must avoid
  the sums of the pairs inside $S$ at that level. There are at most
  $\lceil |S|/2\rceil\le h/2$ such pairs, and $c(x)$ is determined by the
  sum it would equal (for $y=x$ through $2c(x)$). This excludes at most
  $h\cdot h/2$ residues.
- (S2): if $-x\in S$, the residues $(B+B)-c(-x)$, at most $(p+1)(p+2)/2$.
- (S3) with $x=v$: for each $w\in S\setminus\{0\}$ with
  $x+w\in S\setminus\{0\}$, the $p+1$ residues $B-c(w)+c(x+w)$, at most
  $(h-2)(p+1)$ in all; with $v=w=x$ and $2x\in S\setminus\{0\}$, the $p+1$
  residues $(B+c(2x))/2$.
- (S3) with $x=v+w$: for each unordered pair $\{v,w\}$ in
  $S\setminus\{0\}$ with $v+w=x$, at most $(h-1)/2$ pairs, the $p+1$
  residues $c(v)+c(w)-B$.

The total is at most

$$
\frac{(p+1)(p+2)}2+(p+1)\frac{3h-3}2+\frac{h^2}2 .
$$

A residue remains whenever this is less than $q=p^2+p+1$, which holds when
$h^2+3h(p+1)\le(p+1)^2$. For $h\le p/4$,

$$
h^2+3h(p+1)\le\frac{p^2}{16}+\frac{3p(p+1)}4
=\frac{13p^2+12p}{16}<(p+1)^2 .
$$

So the greedy assignment never stops, and the map $c$ exists.

**Cyclic case.** If $H\cong\mathbb Z_h$ and $\gcd(h,q)=1$, then
$\mathbb Z_q\times\mathbb Z_h\cong\mathbb Z_{qh}$ by the Chinese remainder
theorem. $\blacksquare$

**Admissible cyclic orders.** For every large prime power $p$ some prime
$h\in[p/8,p/4]$ does not divide $q$: by the prime number theorem the
interval contains more than two primes, while three distinct prime factors
of size at least $p/8$ would have product at least $(p/8)^3>q$. Such an $h$
is odd, the group $\mathbb Z_{qh}$ has order between $qp/8$ and $qp/4$, and
$|A|=p+h\le5p/4\le\frac52|\mathbb Z_{qh}|^{1/3}$.

**Remark.** The same count works with any finite abelian group $K$ of odd
order carrying a set $B$ whose differences cover $K\setminus\{0\}$
exactly once, in place of $\mathbb Z_q$. The threshold from the count is
$h\le\frac{\sqrt{13}-3}2(p+1)\approx0.30(p+1)$.
