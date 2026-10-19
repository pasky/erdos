---
name: research/leads/odd_covering_distortion/support_concentration
title: A residue configuration that defeats the 138.877 interface
desc: |
  A valuation form of Harrington's repeated-3 construction gives a distinct
  odd family whose survivors have one fixed first 3-digit. At depth 16
  through 73, every supported measure has point-kernel value above 152.14.
  Thus the universal 138.877 small-prime certificate is false, independently
  of its digit order, class-mass recursion, or initial block.
created: 2026-10-17T08:24:44Z
updated: 2026-10-17T08:24:44Z
---

***

This is author-recorded work by Plasma AI, without independent review. It
refutes the universal Step 3 and Step 3* of the
[[research/leads/odd_covering_distortion/sketch|odd-covering sketch]], at
their stated threshold and definitions. It does not resolve Problem 7. The
counterexample is a distinct family that leaves an explicitly described point
uncovered; its purpose is to test the proposed measure certificate.

The construction is a valuation presentation of Section 3 of Joshua
Harrington, *Two questions concerning covering systems*, International Journal
of Number Theory 11 (2015), 1739–1750, printed pp. 1741–1743. The
[[../library/covering_systems/harrington_2015_two_questions_covering_systems/question_1_6|source's
repeated-modulus variant]] allows modulus 3 twice. Below, only one of those
two classes is retained. The argument is given explicitly, so the conclusion
does not rely on a coverage assertion taken from the source without a proof.
No pending outside claim is used.

## A family covering the multiples of 3

For coprime prime powers, a displayed conjunction specifies one congruence
class by the Chinese remainder theorem. Repeated occurrences of the same
conjunction in the following formulas mean one class, not repeated moduli.

For $1\le n\le15$, $0\le s\le11$, and $0\le u\le9$, write

$$
A_n:\quad x\equiv2\cdot3^n\pmod{3^{n+1}},\qquad
B_s:\quad x\equiv4\cdot5^s\pmod{5^{s+1}}.
$$

Take the following classes, called $\mathcal H$:

- $x\equiv3^n\pmod{3^{n+1}}$ for every $n$.
- For every $s$, the classes $x\equiv5^s\pmod{5^{s+1}}$ and
  $x\equiv0\pmod3$, $x\equiv2\cdot5^s\pmod{5^{s+1}}$; for every $(n,s)$,
  the class $A_n$, $x\equiv3\cdot5^s\pmod{5^{s+1}}$.
- For every $u$, the class $x\equiv7^u\pmod{7^{u+1}}$ and the class
  $x\equiv0\pmod3$, $x\equiv2\cdot7^u\pmod{7^{u+1}}$.
- For every $(s,u)$, the classes $B_s$,
  $x\equiv3\cdot7^u\pmod{7^{u+1}}$ and $x\equiv0\pmod3$, $B_s$,
  $x\equiv4\cdot7^u\pmod{7^{u+1}}$.
- For every $(n,u)$, the class $A_n$,
  $x\equiv5\cdot7^u\pmod{7^{u+1}}$; for every $(n,s,u)$, the class
  $A_n$, $B_s$, $x\equiv6\cdot7^u\pmod{7^{u+1}}$.
- For $(p,q,D)=(7,11,10),(5,13,12),(3,17,16)$, the class
  $x\equiv0\pmod q$ and, for $1\le j\le D$, the class
  $x\equiv0\pmod{p^j}$, $x\equiv j\pmod q$.

There are $2470$ classes. All their moduli are odd and greater than 3, and
all are distinct. For the classes supported on $3,5,7$, the 3-exponent is
$0$, $1$, or $n+1\in\{2,\ldots,16\}$; within each of these cases the
presence and exponents of 5 and 7 identify the formula uniquely. The three
closing families are distinguished by their auxiliary prime $11$, $13$, or
$17$. Thus unique factorization verifies distinctness, including every
boundary value of the parameters.

**Coverage.** Suppose $3\mid x$. If $3^{16}\mid x$, the closing family
$(3,17,16)$ covers $x$: its residue modulo 17 is either zero or a number
$j\in\{1,\ldots,16\}$, in which case $3^j\mid x$. Otherwise
$v_3(x)=n\in\{1,\ldots,15\}$. A first nonzero 3-digit of 1 is covered by
the first family; a digit of 2 satisfies $A_n$.

In the latter case, if $5^{12}\mid x$, use the closing family $(5,13,12)$.
Otherwise let $v_5(x)=s\in\{0,\ldots,11\}$. The first nonzero 5-digits
$1,2,3$ are covered by the second family. Digit 4 satisfies $B_s$.
If then $7^{10}\mid x$, use $(7,11,10)$. Otherwise
$v_7(x)=u\in\{0,\ldots,9\}$, and its six possible nonzero digits are
covered, in order, by the six classes involving $7^{u+1}$. This exhausts
every multiple of 3, including zero via the first closing case.

Consequently $\mathcal H\cup\{1\pmod3,2\pmod3\}$ covers the integers with
only modulus 3 repeated. The distinct family

$$
\mathcal C=\mathcal H\cup\{1\pmod3\}
$$

has every uncovered integer in $2\pmod3$.

## A finite period with all small-prime depths

Put

$$
\mathcal P=\{p:3\le p\le73,\ p\text{ prime}\},\qquad
N=\prod_{p\in\mathcal P}p^{16}.
$$

Let $x_0\pmod N$ be the CRT point with coordinate 2 modulo $p^{16}$ for
$p=3,5,7$ and coordinate 1 modulo $p^{16}$ for all other $p\in\mathcal P$.
It avoids every class of $\mathcal C$: a condition involving a positive
3-power in $\mathcal H$ has first digit zero; the remaining pure 5- and
7-power conditions have first digit 1 or zero; the mixed 5-and-7 conditions
have first 5-digit 4 or zero; and the closing families either require an
auxiliary coordinate zero or one of $3,5,7$ to have first digit zero.

Complete the missing prime-modulus classes by taking $x_0+1\pmod p$, and add
$x_0+1\pmod N$. These additions have new distinct moduli, avoid $x_0$, and
make the least common multiple exactly $N$. The resulting $2486$ classes
still have all survivors in $2\pmod3$. If a complete divisor inventory is
required, add $x_0+1\pmod d$ for each remaining divisor $d>1$ of $N$; the
same conclusions hold.

Delete the prime-modulus classes to form the reduced box $Q_s$ of the
[[research/leads/odd_covering_distortion/point_kernel|point-kernel page]]. At
3 the deleted first digit is 1, so its first-digit alphabet is $\{0,2\}$.
The uncovered set $R$ is nonempty, contains $x_0$, and lies wholly in its
first-digit branch 2.

## The forced kernel value

Let $P$ be any probability measure supported on $R$. Independently choose the
centre $y$ uniformly from the part of $Q_s$ whose first 3-digit is 2. For
fixed $x\in R$, its agreement depth $a_3(x,y)$ satisfies

$$
\Pr(a_3(x,y)\ge t)=3^{-(t-1)}\qquad(1\le t\le16).
$$

At each other prime the corresponding probability is
$1/((p-1)p^{t-1})$, independently across primes. Expanding
$(a+1)^2=1+\sum_{t=1}^a(2t+1)$ and averaging the point kernel gives

$$
\mathbb E_y K(x,y)=C_{16}:=
\left(1+\sum_{t=1}^{16}\frac{2t+1}{3^{t-1}}\right)
\prod_{\substack{p\in\mathcal P\\p>3}}
\left(1+\sum_{t=1}^{16}\frac{2t+1}{(p-1)p^{t-1}}\right).
$$

The value is independent of $x\in R$, so averaging over $P$ and taking the
maximum over $y$ proves

$$
\sigma(P)\ \ge\ k(P)\ \ge\ C_{16}>152.14>138.877.
$$

The first inequality is the point-kernel page's elementary concentrated-system
bound. The strict numerical comparisons above are rational. Truncating every
prime to four digits already gives a lower bound in $(146.80,146.81)$;
retaining sixteen digits at 3 and four elsewhere gives one in
$(151.62,151.63)$. No infinite-depth limit is needed.

Thus Step 3* is false. The stronger Step 3 is false too, regardless of its
initial block, digit order, or loss rule: a successful certificate there
would condition its final measure on $R$ and yield
$\sigma(P)\le\kappa/\mu_{21}\le138.877$, as proved on the point-kernel
page. That contradicts the displayed lower bound.

## Testing the replacement tail

For the $2486$-class family above, let $U$ be uniform on $Q_s$. Its
survivors have the quantitative lower bound

$$
U(R)\ge\frac{773}{1920}>\frac14.
$$

To see this, condition on first 3-digit 2, an event of $U$-probability
$1/2$. Every class of $\mathcal H$ with a 3-factor is then disjoint from
this branch, as is the added class modulo $N$. The prime-modulus classes
have already been deleted. The remaining pure 5-power classes have total
conditional mass at most $1/16$, the pure 7-power classes at most $1/36$.
Their union has mass at most $1/16+1/36-1/(16\cdot36)$. The mixed
5-and-7 classes are disjoint from this union and have total mass at most

$$
\left(\sum_{s\ge0}\frac1{4\cdot5^s}\right)
\left(\sum_{u\ge0}\frac1{6\cdot7^u}\right)=\frac{35}{576}.
$$

Together these three collections have mass at most $43/288$. The closing
classes with auxiliary primes 11 and 13 contribute at most $7/360$ and
$5/192$. The 17-closure is disjoint from the branch. Hence the uncovered
conditional mass is at least
$1-43/288-7/360-5/192=773/960$, giving the stated bound.

Corollary E of the
[[research/leads/odd_covering_distortion/exact_loss_tail|exact-loss tail]]
therefore handles this configuration: $P=U(\,\cdot\mid R)$ satisfies
Corollary D. In fact no addition of distinct odd classes having a prime
greater than 73 can complete it to a cover. This confirms that the failure
of the $138.877$ threshold does not refute the exact-loss replacement.

The density hypothesis alone cannot settle every configuration. Add, to the
same $2486$-class family, the 16 classes

$$
x\equiv2\pmod3,\qquad x\equiv1\pmod q,
\quad q\in J:=\{11,13,19,23,29,31,37,41,43,47,53,59,61,67,71,73\}.
$$

Their moduli $3q$ are absent from the old family and distinct. The enlarged
family still misses a CRT point: take coordinates 2 at 3, 5, 7, 11 and 13,
coordinate 1 at 17, and coordinate 3 at all primes from 19 through 73,
at the same depth 16. Every displayed class misses this point.

Put

$$
u_5=\frac{1-5^{-11}}{16},\quad u_7=\frac{1-7^{-9}}{36},\quad
v_5=\frac{5(1-5^{-12})}{16},\quad
v_7=\frac{7(1-7^{-10})}{36}.
$$

On the first-3-digit-2 branch, the old pure 5- and 7-power classes and
mixed 5-and-7 classes have union mass exactly
$u_5+u_7-u_5u_7+v_5v_7$. This event is independent of every $q$-coordinate
with $q\in J$. The new classes remove one further allowed value there.
Ignoring the closing classes only increases the uncovered set, so its
uniform density $d'$ obeys the strict rational bound

$$
0<d'\le\frac12(1-u_5-u_7+u_5u_7-v_5v_7)
\prod_{q\in J}\frac{q-2}{q-1}<\frac14.
$$

This does not refute Corollary D; it shows that its measure cannot always be
justified by Corollary E's uniform-density hypothesis. For this extension,
an adapted product measure does suffice. Let $V$ be uniform on the product
subset with first 3-digit 2 and, at each $q\in J$, the additional value 1
removed. Its first-digit sizes are $r_3=1$, $r_q=q-2$ for $q\in J$, and
$r_p=p-1$ otherwise; later digits remain unrestricted.

Under $V$ the pure and mixed 5-and-7 classes still have mass at most
$43/288$. In the 11- and 13-closures, the $j=1$ classes are now disjoint
from the product subset. The other closing classes have total masses at
most $1/(9\cdot36)=1/324$ and $1/(11\cdot16)=1/176$. All classes with a
3-factor in $\mathcal H$, and the class modulo $N$, are disjoint. Hence

$$
d_V:=V(R)\ge1-\frac{43}{288}-\frac1{324}-\frac1{176}
=\frac{24005}{28512}>\frac{841}{1000}.
$$

Apply the product-measure form of the exact-loss bound, then condition on
$R$. Part 7 of the evidence program certifies unconditioned loss below
$417/1000$ through prime $19997$, and $f_{2262}<21000$ after conditioning,
below the same termination threshold. Thus this extension also satisfies
Corollary D, although its uniform density is below $1/4$.
The full argument still needs a measure construction for arbitrary
configurations; these two explicit constructions do not supply one.

## Effect on the full argument

This defeats a universal small-prime certificate with the retained threshold
and the stated class-mass or system constants. It goes beyond a restriction
on the complete-prefix moment model: the obstruction is the geometry of an
actual uncovered set, and survives arbitrary compatibility-sensitive
optimization of a measure on that set.

It does not refute the source's large-prime theorem, the actual-system
interface for a particular full family, or the
[[research/leads/odd_covering_distortion/exact_loss_tail|exact-loss tail's
Corollary D]]. The last condition uses more than $\sigma(P)$ and might allow
this larger forced value. The full-solution obligation is to construct
supported measures meeting that condition for every small-prime family, or to
replace the interface. Reopening Step 3 at $138.877$ with the same definitions
is impossible; changing its hypotheses or its constant is necessary.

## Evidence and reading scope

Part 6 of the lead's [evidence program](evidence/main.py), implemented in
[the concentration helper](evidence/util/concentration.py), builds the
congruence catalogue and a separate recursive partition of $3\mathbb Z$ into
$13547$ cylinders. It checks every leaf's inclusion in a catalogue class,
the total leaf density $1/3$, distinctness, the explicit surviving CRT point,
the finite period extension, and the three strict rational kernel bounds.
It also checks distinctness and a surviving point for the 16-class density
extension, and the strict rational upper bound on its surviving density.
Deleting the pure class modulo 17 breaks the partition certificate, a negative
control. The recursive partition and the kernel averaging reduction are proved
above; this is not enumeration of the enormous period.

The source was read in its published edition, Section 2's CRT notation and
Section 3, with the printed pages 1741–1743 inspected. Its printed display
(3.8) has superfluous ranges and its accompanying covering sentence does not
match the six displayed nonzero digits. The valuation argument here only needs
$0\le u\le9$, with the six digits $1,\ldots,6$; the closing family covers
$7^{10}\mid x$. This is an explicit reconstruction, not a claim that those
printed indices have been changed by the source.
