---
name: research/leads/square_complement_repair_frontier/triadic_essential_bridge_interval
title: "A positive-density interval of essential ternary bridge points"
desc: |
  An author-recorded positive-density interval of essential bridge points
  in the specified ternary set, with deletion and replacement limits explicit.
problems:
- 33
review_status: unreviewed
created: 2026-09-15T18:23:11Z
updated: 2026-09-15T18:23:11Z
---

***

## Statement and significance

Let A be the explicit
[[theory/additive_bases/L3_square_complement_nine_halves/_index|L3]] set:
at each power s=3^k, retain residues
0,1,2 modulo 2s on [4s^2/9,4s^2], and residues 0,1,2 modulo s
on [5s^2/9,s^2]. This note concerns that specified set, not an optimum
over square complements.

Put

    beta_0 = 4891/900,       delta = 1/10000,
    I = [1/10-delta, 1/10+delta],       lambda=|I|=1/5000.

For every sufficiently large power q of 3, consider every integer b with

    b = r+3q (mod 6q),    r in {0,1,2},
    beta_0-delta <= b/q^2 <= beta_0+delta.

Each such b is essential in A: there is a positive integer t whose only
representation t=n^2+a with n>=0 and a in A uses a=b. In fact each b
has at least q/72000-o(q) such targets of the form b+h^2, uniformly
over the displayed b. The interval contains q/10000+O(1) bridge points
at scale q, counting all three centers.

This is an author-recorded proof. It blocks deletion of this particular
positive-density interval without adding replacement points. It does not
prove that all bridge points are essential, that A is optimal, or that
other deletions cannot improve its counting limit. The argument uses the
definition of A and elementary counts, not L3 as an established theorem.

## The hard targets and elimination of other centers

Write beta=b/q^2 and choose an integer h with h/q in I. The inequalities

    5+2(h/q) < beta < 9-6(h/q)

hold with room to spare throughout these intervals. Thus t=b+h^2 is an
actual hard target for the bridge b, with old bounded root q-h and
overshooting root 3q-h. In particular b is in A, via the inner annulus
at scale 3q.

Restrict h to four residue classes modulo 9. For r=0 or 1, use
h^2=4 or 7 (mod 9), namely h=2,4,5,7 (mod 9). For r=2, use
h^2=1 or 4 (mod 9), namely h=1,2,7,8 (mod 9).

For q divisible by 9, b=r (mod 9). These choices make t-r a unit
square modulo 9 and make t-r' a nonsquare modulo 9 for every other
r' in {0,1,2}. For example, when r=0 or 1, the adjacent center r+1
would require h^2-1=3 or 6 (mod 9), while the other center is already
excluded modulo 3. When r=2, center 0 would require h^2+2=3 or 6
(mod 9), and center 1 is excluded modulo 3. Thus only r can be used
by any annulus at scale at least 9.

There are (4/9)lambda*q+O(1) permitted h in qI.

## The current and larger scales

At scale 3q, an inner-annulus representation requires n^2=h^2 (mod
3q). Since 3 does not divide h, the roots are exactly +/-h modulo 3q.
We have sqrt(t)<2.34q and 3q-h>2.89q, so the only eligible
nonnegative root is h. It gives precisely a=b.

The outer congruence at 3q has the opposite parity. Its smallest
nonnegative root is 3q-h>sqrt(t), so it gives no representation.
All annuli from scale 9q onward start above t. It remains to exclude
annuli at scales s<=q.

## Exact geometry at a smaller scale

Write s=q/3^j. Because b-r is an odd multiple of 3q, an outer
representation at s uses

    n = c*q +/- h,       c=(2v+1)/3^j,

for some integer v. An inner representation at s uses the same formula
with c=v/3^j. The normalized residual is exactly

    (t-n^2)/q^2 = beta-c^2 +/- 2c(h/q).

For outer annuli we may overcount by allowing any residual in
(0,4/9^j]. For inner annuli we may overcount by allowing any residual
in (0,1/9^j]. The actual lower annular endpoints only remove cases.

At the central parameters beta=beta_0 and h/q=1/10, one has

    sqrt(beta+(h/q)^2)=7/3.

For j=0,1,2,3,4, none of the above residuals lies in its allowed
interval. Here are the distances from 7/3 to the nearest root grid on
either side, with the exceptional j=0 grids stated directly:

| j | Outer root distance | Inner root distance |
| --- | --- | --- |
| 0 | Largest lower root is 11/10 | Largest lower root is 21/10 |
| 1 | 1/10 | 1/10 |
| 2 | 1/10 | 1/90 |
| 3 | 7/270 | 1/90 |
| 4 | 1/810 | 1/810 |

These entries follow by measuring 3^j/10 from the even integers for
the outer grid, and from the integers for the inner grid. The relevant
positive residual is 2*(7/3)*d-d^2 for distance d. The smallest
margin from an allowed interval is greater than 1/200. For instance,
at outer j=1 the margin is 11/900, and at outer j=4 it is
3379/656100>1/200. The nearest upper roots have negative residual
of magnitude greater than 1/200 as well. At j=0, the two positive
margins are larger than 1/5 and 3/100, respectively.

For c between 1 and 3, perturbing beta and h/q by at most delta
changes the residual by at most 7*delta<1/200. Values c outside this
range are farther from the relevant intervals. Hence this exclusion
holds uniformly throughout the displayed beta interval and I, for all
five initial scales j=0,...,4.

## The remaining large scales cover too little of I

Consider j>=5 and temporarily allow y=h/q to be real. Any relevant
c lies between 2 and 5/2. Inverting the residual inequality gives

    c = sqrt(beta+y^2-u) +/- y,

where 0<u<=U. Its derivative in y has magnitude below 11/10 and
its derivative in u has magnitude below 1/4. Thus the two possible
c-ranges have total length at most (11/5)lambda+U/2.

For the outer grid, U=4/9^j and its spacing is 2/3^j. At most
(11/10)lambda*3^j+3 grid values can occur. Each covers a y-interval
of length at most U/(2c)<=1/9^j. Their total length is therefore
at most

    (11/10)lambda/3^j + 3/9^j.

For the inner grid, U=1/9^j and the spacing is 1/3^j. At most
(11/5)lambda*3^j+3 values occur, each covering length at most
1/(4*9^j). Its total is at most

    (11/20)lambda/3^j + 3/(4*9^j).

Summing both bounds over all j>=5 gives

    covered length <= (33/20)*lambda/162 + (15/4)/52488
                    < 3/40000.                          (1)

For the integer count, apply this only while s>=sqrt(q). An interval
of y-length L contains at most qL+2 possible h. The total number of
grid intervals in these scales is O(sqrt(q)), so (1) bounds their
covered integers by (3/40000)q+O(sqrt(q)), uniformly in beta.

## The small scales contribute only o(q) exceptions

All points contributed by scales s<sqrt(q) lie below 4q. Geometric
annular counting gives |A intersect [1,4q]|=O(sqrt(q)). For any such
point a, a representation b+h^2=n^2+a gives

    (n-h)(n+h)=b-a>0.

The number of possible h is at most the divisor count tau(b-a).
The elementary estimate tau(N)<=C_epsilon*N^epsilon gives
tau(b-a)=O(q^(1/4)) upon taking epsilon=1/8. Consequently these
small scales exclude only O(q^(3/4)) choices of h.

For completeness, the divisor estimate needs no external theorem. In the
prime factorization of N, use a+1<=2^a<=p^(epsilon*a) for every
prime p>=2^(1/epsilon). For each of the finitely many smaller primes,
sup_(a>=0) (a+1)/p^(epsilon*a) is finite. Multiplying those finite
constants proves the stated bound. The constants are independent of b
in the fixed interval, since b-a is uniformly O(q^2).

## Conclusion

The permitted residue classes leave (4/9)lambda*q+O(1) choices of h.
The initial five scales exclude none. The remaining large scales exclude
less than (3/40000)q+O(sqrt(q)), and the small scales exclude o(q).
Since

    (4/9)lambda - 3/40000 = 1/72000,

at least q/72000-o(q) choices remain. Every representation for any of
these targets uses b, by the earlier treatment of the current and larger
scales. This proves essentiality and the uniform target count.

Finally, the b interval has length q^2/5000 and each of its three
classes has spacing 6q. It therefore contains q/10000+O(1) points.
The result applies to each of them separately. A successful construction
may replace these points with different residuals; this proof only rules
out deleting them from A without replacement.

## Outstanding scrutiny

Independent scrutiny remains outstanding. The original author account identifies
the first-five-scale grid table and the passage from continuous interval lengths
to integer h counts, including the small-scale divisor bound, as useful focused
review targets. This identifies review scope; it supplies no independent verdict.
