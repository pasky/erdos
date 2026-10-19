[cut]

The imported theorem is the exact statement on
`library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/target.md`:
if u,v > 0 and u/v is irrational, every sufficiently large integer is

\[
 \sum_{r\in R}\lfloor u2^r\rfloor+
 \sum_{s\in S}\lfloor v2^s\rfloor
\]

for finite R,S contained in the nonnegative integers.

[cut]

Fix m >= 2, gamma = 2^(1/m), and t > 0. The number gamma is irrational: a
rational mth root of the integer 2 would be an integer, and no integer has
mth power 2. In particular 1 < gamma < 2. Let L be any prescribed first
index, and let F be any finite set of deleted values. Choose an integer j >= L
large enough that, for every n >= j,

\[
 t\gamma^n(\gamma-1)>1,
 \qquad \lfloor t\gamma^j\rfloor>\max(F\cup\{0\}).
\]

Thus the values floor(t gamma^n), n >= j, are positive, strictly increasing,
and avoid F. Take u=t gamma^j and v=t gamma^(j+1). Their ratio 1/gamma is
irrational. Since gamma^m=2, the two sequences in the imported theorem are
exactly the subsequences with indices

\[
 j+mr\quad\hbox{and}\quad j+1+ms\qquad(r,s\ge0).
\]

These index classes are disjoint because m >= 2. Each representation from
the theorem therefore uses distinct indices of the original tail, and strict
increase makes them distinct integer values as well. Consequently there is
an H=H(t,m,j) such that every integer N >= H is a sum of distinct values of
the original sequence outside F. This proves strong completeness, under
either the indexed or distinct-value convention and with either first index
0 or 1. It gives no numerical H uniform in t, m or F.

For E0354(ii), take gamma=sqrt(2) and apply this to the alpha ray alone.
Adding the beta ray preserves completeness, so the conclusion holds for all
alpha,beta > 0, even without the irrational-ratio restriction. This is a
positive answer to the existential reading.

[cut]
