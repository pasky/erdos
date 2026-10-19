---
name: research/erdos_699/archive/other_approaches/index_6_overlap_obstruction
title: "Erdős 699: full small-prime overlap in the remaining index-six position pattern"
desc: "In the pattern r2=2, r3=1, r5=0, four column residue classes realize the entire selected prime powers as common-prime overlap. The forced valuation gap at row zero does not itself improve the polynomial capacities."
created: 2026-09-22T08:28:03Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: full small-prime overlap in the remaining index-six position pattern

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

The [exact localization lemma](../../methods/details/gcd_localization.md)
permits replacing a selected small-prime power $P_p$ by

$$
E_p=p^{\min\{v_p(n-r_p),v_p\binom nj\}}.
$$

This can strengthen a polynomial certificate when the column binomial has
few carries at one of the selected primes. In the unresolved position
pattern

$$
(r_2,r_3,r_5)=(2,1,0),
$$

the already proved row-zero restriction leaves column residue classes
where all three overlaps equal the original prime powers.

**Proposition.** Suppose $(n,6,j)$ is bad and the selected positions are
$(2,1,0)$. Put

$$
A_2=v_2(n-2),\qquad A_3=v_3(n-1),\qquad A_5=v_5(n).
$$

Then

$$
n\equiv250\pmod{300}.
$$

For any integer column $j$ with

$$
j\equiv11,23,47,\text{ or }59\pmod{60},
$$

one has

$$v_p\binom nj\ge A_p\quad(p=2,3,5),\qquad
  E_2=2^{A_2},\quad E_3=3^{A_3},\quad E_5=5^{A_5}.$$

Here the column must lie in $0\le j\le n$ for the binomial assertion.
The overlap conclusion itself only needs the displayed conditions on the
row and its three prime-power factors; it does not require badness.

**Proof.** Maximality at $r_2=2$ forces $A_2\ge2$, hence
$n\equiv2\pmod4$. The selected factor at $r_3=1$ is divisible by three,
so $n\equiv1\pmod3$. Therefore neither $8\mid n$ nor $9\mid n$.
The [forced valuation-gap proposition](low_crt_row_zero.md)
then supplies $25\mid n$, giving $n\equiv250\pmod{300}$.

Each listed column has $j\equiv3\pmod4$, $j\equiv2\pmod3$, and
$5\nmid j$. In Kummer's formula

$$v_p\binom nj=\sum_{k\ge1}
 \mathbf1_{\{j\bmod p^k>n\bmod p^k\}},$$

the first $A_2$ summands at two are all one: at level one the residues
are $1>0$, and at every level $2\le k\le A_2$ the row residue is two
while the column residue is at least three. At three, every level
$1\le k\le A_3$ has row residue one and column residue at least two.
At five, every level $1\le k\le A_5$ has row residue zero and nonzero
column residue. This proves all three valuation bounds and hence all
three equalities for $E_p$. $\square$

These column classes also satisfy the forced row-zero gap in its strongest
simple form: $v_5(j)=0$ and $v_5(n)\ge2$. They are closed under column
reflection, because $n\equiv10\pmod{60}$ interchanges $11$ with $59$
and $23$ with $47$.

Whether such columns also avoid every common prime at least seven remains
unresolved. An argument using the actual overlaps must obtain an additional
restriction from those large primes; the selected-position pattern and the
known row-zero valuation gap alone provide no power saving in $E_p/P_p$.
