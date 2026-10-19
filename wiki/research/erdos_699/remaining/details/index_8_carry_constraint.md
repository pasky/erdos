---
name: research/erdos_699/remaining/details/index_8_carry_constraint
title: "Erdős 699: a column restriction in the difficult index-eight region"
desc: "An exact prime-adic column identity and a small interpolation certificate exclude the low-residue Lucas branch in the difficult index-eight cofactor configuration. The whole index remains unresolved."
created: 2026-09-22T16:37:31Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a column restriction in the difficult index-eight region

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/other_approaches/index_8_next_obstruction|The remaining cofactor profile]] ·
[[research/erdos_699/methods/details/gcd_localization|Actual common-prime valuations]]

***

The difficult cofactor configuration can be restricted using the actual
column $j$. The following result is uniform in the row; it does not search
through finitely many rows.

**Proposition.** Suppose $(n,8,j)$ is bad, put $h=n-7$, and choose maximal
small-prime positions with

$$
(r_2,r_3,r_5,r_7)=(1,3,0,2).
$$

Write $P_p=p^{v_p(n-r_p)}$ and $u_p=(n-r_p)/P_p$. Assume

$$
u_2,u_3,u_5\ge h^{3/10}. \tag{1}
$$

There is no hypothesis on $u_7$. If $h\ge10^{850001}$, then

$$
\boxed{j\bmod P_7>2.} \tag{2}
$$

Moreover, writing $c=n-j$ and using $[a]_p=p^{v_p(a)}$,

$$
\left[\binom nj\right]_7>\sqrt h,
\qquad [j(j-1)(j-2)]_7<\sqrt h,
\qquad [c(c-1)(c-2)]_7<\sqrt h. \tag{3}
$$

Thus the low-residue Lucas branch cannot realize this cofactor region at
large height. The alternative in (2) remains possible; this proposition
does not make the whole index effective.

## An exact column valuation identity

Here is a general lemma independent of badness. Let $p$ be prime,
$0\le r<p$, $r<j\le n$, and write

$$
n-r=p^A u,\qquad A\ge1,\quad p\nmid u.
$$

Then

$$\boxed{
 p^{v_p\binom nj}\,[j(j-1)\cdots(j-r)]_p\le n-r.
} \tag{4}$$

To prove it, use

$$
(j)_{r+1}\binom nj
=(n)_{r+1}\binom{n-r-1}{j-r-1}.
$$

Exactly one numerator factor in $(n)_{r+1}$ is divisible by $p$, so its
valuation is $A$. The bottom $A$ base-$p$ digits of
$n-r-1=p^Au-1$ are all $p-1$. Kummer therefore gives

$$
v_p\binom{n-r-1}{j-r-1}
=v_p\binom{u-1}{\lfloor(j-r-1)/p^A\rfloor}
\le\lfloor\log_pu\rfloor.
$$

For $u=1$ the middle valuation is zero, as required. Taking valuations in
the displayed binomial identity proves (4). The same bound holds with
$j$ replaced by $n-j$ whenever that column exceeds $r$.

In particular, if $j\bmod p^A\le r$, the falling factorial on the left
contains a multiple of $p^A$. Hence $p^{v_p\binom nj}\le u$. For

$$
E_p=p^{\min\{A,v_p\binom nj\}},
$$

this implies

$$
E_p\le\min(p^A,u)\le\sqrt{n-r}. \tag{5}
$$

Equation (4) also retains information in the other Lucas branch, where
(5) need not hold.

## The interpolation certificate

Use coordinate factors

$$
H(X,Y)=\prod_{a=0}^7((X-a)(Y-a))^{h_a},
$$

with integer vectors

$$
(h_a)=(39,29,21,10,0,0,0,0),
$$
$$
(m_t)=(102,81,73,56,56,46,40,33).
$$

At a grid point $x+y=t<8$, prescribe residual multiplicity

$$
R_{xy}=\max\{0,m_t-h_x-h_y\}.
$$

The degree-84 symmetric jet matrix is $1845\times1849$ and has full row
rank modulo $251$. The
[nonvanishing interpolation lemma](../../methods/details/jet_nonvanishing.md)
therefore provides a finite integer family $G$ of degree at most 85 with
these residual multiplicities, at least one of which is nonzero at every
physical point $(j,c)$ with $j+c>7$. Coordinate factors cannot vanish
there, since $j,c\ge9$.

Consequently one of the corresponding $F=HG$ is nonzero, has degree at
most

$$
D=2\sum h_a+85=283,
$$

and has the row multiplicities $m_t$. The integer data and the exact rank
calculation are retained in the
[checker](../../computations/erdos_699_index_8_carry_constraint.py) and
[certificate](../../computations/erdos_699_index_8_carry_constraint.json).

Put $B=\binom nj$ and

$$
E_7=7^{\min\{v_7(n-2),v_7(B)\}}.
$$

The exact localization inequality, retaining this actual overlap, gives

$$
\prod_{t=0}^7(n-t)^{m_t}
\le (7!)^{102}|F(j,c)|\,
P_2^{81}P_3^{56}P_5^{102}E_7^{73}. \tag{6}
$$

The contribution of every nonmaximal small-prime power is covered by the
factor $(7!)^{102}$. The prime threshold remains the original $p\ge8$,
which here means primes at least 11.

The sum of the row multiplicities is 487. By (1), each of $P_2,P_3,P_5$
is at most $2h^{7/10}$. Also $n\le2h$. A deliberately generous coefficient
bound obtained from a nonzero maximal jet minor gives

$$
h^{367/10}\le10^{169000}E_7^{73}. \tag{7}
$$

For completeness, a jet entry is smaller than $2\cdot8^{84}$.
Hadamard, adjugates, and the generator construction bound the coefficient
norm of $G$ by $10^{1845(84+6)+50}$. The logarithmic bounds for $H$,
$(7!)^{102}$, and the replacements $n\le2h$ add respectively
$198$, $408$, and $283+239$. Their total is $167228<169000$.
The remaining height exponent in (6) is exactly

$$
487-283-\frac7{10}(81+56+102)=\frac{367}{10}.
$$

If the low-residue branch in (2) held, (5) would give
$E_7\le\sqrt{n-2}\le\sqrt{2h}$. Then (7) would imply

$$
h^{1/5}\le10^{169000}2^{73/2}<10^{170000},
$$

contrary to $h\ge10^{850001}$. This proves (2).

Finally, (7) gives

$$
E_7\ge10^{-169000/73}h^{367/730}.
$$

Combine this with (4), first at $j$ and then at $c$. Since
$7^{v_7(B)}\ge E_7$ and $n-2\le2h$,

$$
[(j)_3]_7,[(c)_3]_7
\le2\cdot10^{169000/73}h^{363/730}.
$$

At the stated height these quantities are strictly below $\sqrt h$;
the preceding lower bound for $E_7$ is strictly above $\sqrt h$.
This proves (3).
