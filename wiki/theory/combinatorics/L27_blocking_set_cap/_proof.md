---
name: theory/combinatorics/L27_blocking_set_cap/_proof
title: Incidence-moment proof
desc: Counting incidences and ordered pairs gives a quadratic obstruction to a blocking set with a prescribed maximum line intersection.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

A projective plane of order $q$ has $q^2+q+1$ points and lines, with $q+1$
lines through each point, and exactly one line through two distinct points.
For a set $S$ of size $s$, put $x_\ell=|S\cap\ell|$. Double counting gives

$$
\sum_\ell x_\ell=s(q+1),\qquad
\sum_\ell x_\ell(x_\ell-1)=s(s-1).
$$

If $1\le x_\ell\le C$, then
$x_\ell(x_\ell-1)\le C(x_\ell-1)$. Summing and rearranging proves

$$
s^2-[C(q+1)+1]s+C(q^2+q+1)\le0.
$$

Any cap at most three also satisfies the hypotheses with $C=3$. In that
case the discriminant is $-3q^2+12q+4$, which is negative at $q=5$ and
strictly decreasing for real $q\ge5$. The monic quadratic is positive for
every real $s$, a contradiction. The plane over the field of five elements
exists, so a cap working for every finite plane cannot be less than four:
a real bound below four permits at most three points on a line.

For $C=4$ the discriminant is $24q+9$, giving the interval on the claim
page. A necessary interval does not supply a point set attaining it.
