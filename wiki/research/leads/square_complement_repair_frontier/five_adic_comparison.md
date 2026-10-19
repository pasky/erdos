---
name: research/leads/square_complement_repair_frontier/five_adic_comparison
title: "A complete five-adic comparison construction"
desc: |
  A complete author-recorded five-adic comparison with upper limit 99/20,
  whose coverage and real-prefix proofs do not improve the 9/2 target.
problems:
- 33
review_status: unreviewed
created: 2026-09-15T18:23:11Z
updated: 2026-09-15T18:23:11Z
---

***

## Outcome

The two-parity construction below represents every positive integer and has
upper counting limit 99/20. It therefore does not improve the comparison
target 9/2. Its value here is a complete alternative repair mechanism: all
five lift positions are handled by one opposite-parity family, with an exact
prefix calculation. The proof is author-recorded and consumes no external
theorem or native claim.

For M>=1 let R_M consist of the positive integers congruent to 0,1,2
modulo M, identifying repetitions. For q=5^k, k>=0, set

    O_q = R_(2q) intersect [4q^2/25,4q^2],
    P_q = {a>0 : a = r+q (mod 2q), r=0,1,2}
          intersect [q^2/25,q^2],
    B = union_q (O_q union P_q).

## Root lifting and descent

The identity {0,1,2}+{1,4}=Z/5Z lets us choose r in {0,1,2} so
that t-r is a nonzero square modulo 5. At each power q>=5, it has two
sign roots modulo 2q and a unique representative 0<m_q<q. Elementary
lifting works because 2m is invertible modulo 5. At the next scale,

    m_(5q) is one of m, 2q-m, 2q+m, 4q-m, 4q+m.

At q=1 choose the root 0 or 1 according to parity; the same inclusive
list gives every possible bounded root at q=5.

Every positive residual a<=4q^2 with a=r (mod 2q) belongs to an
outer annulus at a scale <=q. Every positive residual b<=q^2 with
b=r+q (mod 2q) belongs to an opposite-parity annulus at a scale <=q.
In both cases the radial annuli are consecutive and their congruences
descend. For the second case, q/s is odd, so r+q = r+s (mod 2s).

## Coverage

The initial outer annulus contains 1,2,3,4 and 5=1^2+4. Fix t>=6.
At q=1 its chosen residual exceeds 4. Let Q=5q be the first scale at
which a_Q=t-m_Q^2<=4Q^2. If a_Q>0 the preceding descent catches it.
Assume a_Q<=0 and put a=t-m^2>4q^2, M=m_Q.

The cases M=m and M=2q-m are impossible: in the latter,
a_Q=a-4q^2+4qm>0. It remains to produce a positive residual for the
opposite-parity root N=Q-M. Such a residual is congruent to r+Q modulo
2Q, because M^2-N^2=2QM-Q^2=Q (mod 2Q).

If M=2q+m, first consider e=t-(2q-m)^2=a-4q^2+4qm>0. If
e<=4q^2, outer descent catches it. Otherwise a>8q^2-4qm. Combining
this with a<=4q^2+4qm, from a_Q<=0, gives m>q/2. Now

    t-(3q-m)^2 = a-9q^2+6qm > -q^2+2qm > 0.

This is the residual at N=Q-M. Its upper bound is
M^2-N^2=-5q^2+10qm<=5q^2<Q^2.

If M=4q-m, then N=q+m and

    t-N^2 = a-q^2-2qm > 3q^2-2qm >= q^2 >0,
    t-N^2 <= M^2-N^2 =15q^2-10qm<=15q^2<Q^2.

If M=4q+m, then N=q-m>=0 and

    t-N^2 = a-q^2+2qm>0,
    t-N^2 <= M^2-N^2 =15q^2+10qm<=25q^2=Q^2.

Opposite-parity descent catches the residual in all three cases. The
argument includes a_Q=0 and every annular seam. This proves coverage.

## Counting every real prefix

At large scales the two parity families do not overlap, including across
scales. An opposite-parity class at a larger scale reduces to r+s modulo
2s, whereas the outer family at s uses residues 0,1,2. The opposite
family at a smaller scale ends before an outer family at a larger scale
can start. Small repeated classes change the count by O(1).

At q=5^k, ordinary residue counts and geometric summation give

    O(q^2) = (27/10)q+O(k),
    P(q^2) = (9/5)q+O(k),
    B(q^2) = (9/2)q+O(k).

For example, the outer annulus at s has count (144/25)s+O(1).
Summing through s=q/5 gives (36/25)q+O(k), and the remainder through
q^2 has length 21q^2/25 and density 3/(2q), giving (63/50)q+O(1).
Their sum is (27/10)q+O(k). The opposite annulus at s has count
(36/25)s+O(1), so summation through q gives (9/5)q+O(k).

For x=X/q^2 in [1,25], the complete leading profile is

    B(X) = q F(x)+O(k), uniformly in x,

    F(x) = 27/10 + (9/5)x,       1<=x<=4,
         = 15/2 + (3/5)x,        4<=x<=25.

On (q^2,4q^2), the densities are 3/(2q) from O_q and 3/(10q)
from P_(5q). On (4q^2,25q^2), both active densities are 3/(10q).
There are only two interval pieces, so periodic counting errors are
uniform; after division by sqrt(X)>=q they vanish as k grows.

Each F(x)/sqrt(x) has the form a/sqrt(x)+b*sqrt(x), whose interior
critical point is a minimum. The boundary values are 9/2 at x=1 and
x=25, and 99/20 at x=4. Thus

    limsup B(X)/sqrt(X) = 99/20,

witnessed by X=4*5^(2k). In fact the lower limit is 3*sqrt(2), at
x=25/2 in the second piece. The upper limit, not the favorable values
at q^2, determines why this construction fails the intended improvement.
