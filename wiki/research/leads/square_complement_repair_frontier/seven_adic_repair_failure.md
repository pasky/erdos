---
name: research/leads/square_complement_repair_frontier/seven_adic_repair_failure
title: "Failure of a concrete seven-adic residue repair"
desc: |
  A coverage counterexample and excessive intermediate prefix for one
  specified seven-adic repair, with both failures author-recorded.
problems:
- 33
review_status: unreviewed
created: 2026-09-15T18:23:11Z
updated: 2026-09-15T18:23:11Z
---

***

## Proposed set and outcome

Put R={0,1,5}. Start with the seven-adic outer skeleton A7, using
residues r modulo 2q on [4q^2/49,4q^2], for q=7^k and r in R.
Add the following sets at each q:

    common repair: a = r+7q (mod 14q), 5q^2<a<=49q^2;
    even repair:   a = r+jq (mod 14q), 4q^2<a<=8q^2,
                   j in {4,6,8,10}.

Call the resulting union C. This attempted rule was motivated by the
common reflected root 7q-M, and by selecting four of the six nonzero
even lift classes for the small-root gap. It fails coverage, with the
exact witness 26522 below. Independently, its own prefix count has upper
limit at least 195/(28*sqrt(2))>9/2. Neither its boundary count nor the
four-class choice supplies a repaired complement.

All calculations are author-recorded, without independent acceptance.

## A middle lift omitted by the proposed routing

Take q=49, m=29, r=5, M=4q-m=167, and

    t=M^2+r-2*(14q)=26522.

The old root 2q+m=127 gives residual 10393. This lies in (4q^2,8q^2]
but has class r+2q modulo 14q, which the even repair omits. The next
smaller same-parity roots 2q-m=69 and m=29 give residuals 21761 and
25681, both exceeding 8q^2=19208. The common reflected root is
7q-M=176>sqrt(t), so its residual is nonpositive.

This is a middle-gap failure: m/q lies between 1/2 and 2/3. The two
old roots that were both available in the smaller gap no longer both
have residual <=8q^2. A subclass argument that checked only the small
gap cannot be applied here.

## All other scales and centers are excluded

We have t=6 (mod 7), so among R only r=5 is possible: t-0=6 and
t-1=5 are nonresidues modulo 7, while t-5=1 is a nonzero square.
This applies to every scale >=7 in C.

At scale 1, all points of the proposed set contributed by that scale are
at most 49. But floor(sqrt(t))=162 and t-162^2=278>49.

At scale 7, the outer annulus ends at 196, so even the nearest square
leaves too large a residual. The common repair is at most 2401 and
requires n^2=8 (mod 98). Its roots are 20 and 78 modulo 98. The
largest eligible n below sqrt(t) is 118, leaving residual 12598>2401.
For the even repair, a residual in (196,392] permits only n=162.
Its residual 278 is 82 modulo 98, whereas the allowed center-5
classes are 33,47,61,75.

At scale 49, the outer class requires n=29 or 69 (mod 98). The
largest eligible root below sqrt(t) is 127, leaving 10393>9604.
For the even repair, parity restricts the eligible roots modulo 49 to
29,69,127. The first two residuals exceed 19208; the last has the
omitted class r+2q. The common class has bounded root 176 and fails
as above.

At scale 343, the outer bounded root is 167>sqrt(t). By the
[fixed-center monotonicity argument](proof_sketch.md#a-fixed-center-lift-cannot-return-after-overshooting),
every later bounded root for the same center is at least 167. All repairs from
scale 343 onward start above 4*343^2=470596>t. Outer annuli from
scale 2401 onward also start at least at 470596. This exhausts all
scales and proves that t is not a square plus an element of C.

## The count also fails between the boundaries

For large q, the common repair contributes (66/7)q+O(1) points and
the even repair (24/7)q+O(1). Their classes are distinct. The repair
supports at different scales are disjoint, and none overlaps the outer
skeleton except for bounded initial exceptions.

Through 4q^2 the outer skeleton contributes (48/7)q+O(log q), and
the earlier repairs contribute (15/7)q+O(log q). Thus

    C(4q^2)=9q+O(log q).

On (4q^2,5q^2], the next outer annulus and the four even repair
classes give density 15/(14q). On (5q^2,8q^2], the common repair
raises the density to 18/(14q). Consequently

    C(8q^2) = [9 + 15/14 + 3*(18/14)]q+O(log q)
             = (195/14)q+O(log q),

and hence

    limsup C(X)/sqrt(X) >= 195/(28*sqrt(2)) > 9/2.

The inequality is strict because 195^2=38025 is greater than
(126*sqrt(2))^2=31752. This count failure does not depend on whether
the proposed routing could be repaired. It concerns C as a set.

## What changes the next attempt

The two defects require different repairs. Coverage needs an option for
middle lift positions where only one old residual is short enough.
The counting target requires less mass near the first added bands, or a
proved sharing rule with smaller scales. Enlarging the present intervals
would not correct its already excessive prefix count.
