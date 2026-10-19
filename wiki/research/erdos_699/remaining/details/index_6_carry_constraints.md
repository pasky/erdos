---
name: research/erdos_699/remaining/details/index_6_carry_constraints
title: "Erdős 699: simultaneous carry restrictions in the hard index-six region"
desc: "An explicit degree-twelve product and an exact valuation identity exclude the low-residue Lucas branches at 2,3,5 in a cofactor box around the remaining hard profile. No interpolation or rank computation is used."
created: 2026-09-22T17:37:40Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: simultaneous carry restrictions in the hard index-six region

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/index_8_carry_constraint|Column restrictions at index eight]] ·
[[research/erdos_699/methods/details/gcd_localization|Actual common-prime valuations]]

***

The hard index-six assignment is

$$
(r_2,r_3,r_5)=(2,1,0).
$$

The row cofactor profile alone does not settle this assignment. The actual
column can nevertheless be restricted without another interpolation
calculation.

**Proposition.** Let $(n,6,j)$ be bad, set $c=n-j$, $h=n-5$, and choose the
maximal small-prime positions as above. Put

$$
P_p=p^{v_p(n-r_p)},\qquad u_p=(n-r_p)/P_p.
$$

Assume

$$h^{31/100}\le u_2\le h^{2/5},\qquad
h^{9/25}\le u_3\le h^{2/5},\qquad
u_5\ge h^{31/100}. \tag{1}$$

For $h\ge10^{425}$, necessarily

$$\boxed{
 j\bmod P_2>2,\qquad j\bmod P_3>1,\qquad j\bmod P_5>0.
} \tag{2}$$

In particular, each selected prime produces a carry across its selected
prime-power boundary. There are also quantitative restrictions at 5:

$$
\left[\binom nj\right]_5>\sqrt h,
\qquad u_5<\sqrt h,
\qquad [j]_5,[c]_5<\sqrt h, \tag{3}
$$

where $[a]_p=p^{v_p(a)}$. In fact, (3) needs only the two lower bounds on
$u_2$ and $u_3$ in (1), without either upper bound or a lower bound on
$u_5$.

These are conditional restrictions on bad triples. The branches in (2)
are not excluded, so this proposition does not establish effectivity for
the entire index.

## A column identity allowing row labels at least the prime

The valuation identity from the index-eight argument extends to a row
label $r$ that may be at least $p$. Let

$$
n-r=P u,\qquad P=p^A>r,\qquad p\nmid u,\qquad r<j\le n.
$$

Then

$$\boxed{
\left[\binom nj\right]_p[(j)_{r+1}]_p
\le[r!]_p(n-r).
} \tag{4}$$

Indeed,

$$
(j)_{r+1}\binom nj=(n)_{r+1}\binom{n-r-1}{j-r-1}.
$$

Because $P>r$, the valuation of $(n)_{r+1}$ is $A+v_p(r!)$.
The bottom $A$ digits of $n-r-1=p^Au-1$ are all $p-1$, so

$$
v_p\binom{n-r-1}{j-r-1}
=v_p\binom{u-1}{\lfloor(j-r-1)/P\rfloor}
\le\lfloor\log_pu\rfloor.
$$

This proves (4). It also applies at the complementary column $c$.

If $b=j\bmod P\le r$, the $p$-valuation of the falling factorial is at
least $A+v_p(b!)+v_p((r-b)!)$. Thus, writing

$$
E_p=p^{\min\{A,v_p\binom nj\}},
$$

we obtain

$$
E_p\le\min\!\left(P,\left[\binom rb\right]_p u\right). \tag{5}
$$

For the three positions under consideration this gives

$$
\begin{array}{c|c}
\text{low-residue branch}&\text{overlap bound}\\ \hline
j\bmod P_2\le2&E_2\le2u_2\\
j\bmod P_3\le1&E_3\le u_3\\
j\bmod P_5=0&E_5\le\min(P_5,u_5)\le\sqrt n.
\end{array} \tag{6}
$$

The factor 2 in the first row is required: $\binom21=2$.
At the heights in the proposition, the upper bounds in (1) guarantee
$P_2,P_3\ge h^{3/5}>2$, so all uses of $P>r$ are justified.

## One explicit polynomial

Use

$$
F(X,Y)=(XY)^3((X-1)(Y-1))^2(X-2)(Y-2).
$$

Its degree is 12, and at every grid point $x+y=t<6$ it has multiplicity
at least $6-t$. It is positive at every admissible $(j,c)$.
The exact localization inequality therefore gives

$$
\prod_{t=0}^5(n-t)^{6-t}
\le (5!)^6 F(j,c)E_2^4E_3^5E_5^6. \tag{7}
$$

Each unselected small-prime contribution is covered by $(5!)^6$.
The large-prime hypothesis is precisely the original threshold $p\ge6$.

Since $jc\le n^2/4$ and $n\le2h$,

$$
F(j,c)\le(jc)^6\le h^{12}.
$$

The multiplicities in (7) sum to 21, giving

$$
\boxed{E_2^4E_3^5E_5^6\ge h^9/120^6.} \tag{8}
$$

The cofactor lower bounds imply

$$
P_2\le2h^{69/100},\quad P_3\le2h^{16/25},\quad P_5\le2h^{69/100}.
$$

Using $E_p\le P_p$ for the other two primes in turn yields

$$
\begin{aligned}
E_2^4&\ge\frac{h^{83/50}}{120^6 2^{11}},\\
E_3^5&\ge\frac{h^{21/10}}{120^6 2^{10}},\\
E_5^6&\ge\frac{h^{76/25}}{120^6 2^9}.
\end{aligned} \tag{9}
$$

Each row only needs the cofactor lower bounds at the other primes.
Their limiting overlap exponents are respectively $83/200$, $21/50$,
and $38/75$.

Now substitute the corresponding low-residue bound from (6) into (9).
The three conclusions would be

$$
h^{3/50}\le120^6 2^{15},\qquad
h^{1/10}\le120^6 2^{10},\qquad
h^{1/25}\le120^6 2^{12},
$$

respectively. But

$$
120^6 2^{15}<10^{17},\qquad 425/25=17.
$$

None is possible for $h\ge10^{425}$. This proves (2), without a matrix
rank calculation or an asymptotic analytic estimate.

To verify (3), put $C_5=120^6 2^9$. The third inequality in (9) gives
$E_5\ge C_5^{-1/6}h^{38/75}$. Both $u_5=n/P_5$ and the quantities
$[j]_5,[c]_5$ from (4) are at most

$$
2C_5^{1/6}h^{37/75}.
$$

The exact integer comparison

$$
\bigl(2^6C_5\bigr)^{25}<10^{425}
$$

shows these are below $\sqrt h$ at the stated height. The same comparison
also gives $E_5>\sqrt h$, proving all of (3).

The [checker](../../computations/erdos_699_index_6_carry_constraints.py)
and [record](../../computations/erdos_699_index_6_carry_constraints.json)
verify the multiplicities, rational exponent arithmetic, and numerical
thresholds. The proof uses only the explicit product $F$ and the column
valuation identity; it does not repeat an interpolation search.
