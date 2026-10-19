---
name: research/leads/reciprocal_mersenne_greedy/evidence
title: Evidence
desc: |
  Exact finite checks of rational greedy prefixes, gaps, periodic supports,
  multiplier carry rules and finite seeds with doubling extensions. Explicit
  seeds refute nonnegative carry changes when a multiplier is added; every
  set containing 1 inside {1,...,12} has a half seed, while repeated
  multipliers and index-dependent sets can lose it. Every full Mersenne
  rational-membership conclusion stays open.
created: 2026-10-16T14:05:38Z
updated: 2026-10-16T14:05:38Z
---

# Evidence

[[research/leads/reciprocal_mersenne_greedy/_index|..]]

***

The [entry point](main.py) certifies the finite statements of the
[[research/leads/reciprocal_mersenne_greedy/proof_sketch|greedy-expansion sketch]],
section "Computations". It uses the Python standard library, the root Python
environment and the shared `Checker`, reads no data files and writes no files.
Run it from the repository root:

```sh
uv run --no-sync python wiki/research/leads/reciprocal_mersenne_greedy/evidence/main.py
```

The full run takes about two minutes, most of it in check 2, and well under
1 GiB of memory. `--quick` reduces check 1 to denominators at most 60 through
step 200, check 2 and the full-weight part of check 6 to 2000 steps, check 3
to denominators at most 60, and check 4 to periods at most 8, each with its
own pinned counts, and takes about ten seconds. The checks are:

1. every reduced fraction $p/Q\in(0,E)$ with $Q\le200$ is classified through
   step 1000 as a finite subsum (confirmed in exact rationals), a gap at a step
   $n$ (confirmed in exact rationals by $L_{n,J}+E_{n,J}<q-S_F<w_n$, Lemma 8 of
   the sketch) or passing step 1000 (the fraction lies in the level-1000
   cylinder of its greedy set, by interval enclosures); the counts, 41, 7395
   and 12218, and the number of gaps at each step are pinned, and no gap
   occurs after step 12; every finite subsum ends at a step that Lemma 9
   allows, and every passing run is past all such steps;
2. $\frac12$ and $\frac1{21}$ lie in the level-20000 cylinders of their greedy
   sets, every greedy decision being certified, and are past the steps at
   which Lemma 9 allows them to terminate; the selected counts and unique
   minimizing steps of $|2^nr_{n-1}-1|$ over $15\le n\le20000$ are pinned,
   and both minima are certified to lie strictly between $2^{-14}$ and
   $2^{-13}$; the decimal logarithms printed alongside are approximations;
3. for the 6830 reduced fractions with $Q\le150$ that pass step 400, the
   numbers of near misses $|2^nr_{n-1}-1|<2^{t-n}$ with $15\le n\le400$ and
   $n>t+2$, and the numbers of distinct pairs $(n,r_{n-1})$ among them (residual
   equality at a fixed step is decided exactly from the symmetric difference
   of the selected sets), are pinned for
   $t=2,4,6,8,10$; the uniform-position expectations are printed;
4. for each of the 1965 nonempty residue sets modulo $M\le10$ that are not
   periodic with a smaller period, the least-denominator fraction in the
   certified enclosure of the sum has denominator at least $2^{1000}$; a
   control finds $\frac13$ in a tiny interval around it. Every returned
   reduced fraction is also checked to lie inside its enclosure;
5. $4203/32768$ first meets a gap at step 17 after selecting
   $\{4,5,6,7,8,10,11,13,14,16\}$; the exact certificate uses
   $L_{17,2}+E_{17,2}$ as its upper tail bound. For the weights
   $v_n=\sum_{a\in\{1,2,3,4,6\}}2^{-an}$, the rule in
   [[research/leads/reciprocal_mersenne_greedy/multiplier_carries|the multiplier construction]]
   first proposes a non-Boolean digit, $-1$, at step 108, whereas the actual
   greedy prefix passes every step through 108. Its carry transitions at
   steps 106, 107 and 108 are $1\to2\to3\to1$, and the two prefixes first
   differ at step 106. This check runs unchanged in both modes;
6. the window rule of Lemma 12 of the sketch gives bits through the horizon
   of check 2 (20000 steps, 2000 in quick mode) and reproduces exactly the
   greedy digits of $\frac12$ that check 2 certifies. At every step $n\ge4$
   its digit equals the closed form
   $\lfloor(4k-2f_{2n-2}-f_{2n-1})2^{1-n}\rfloor$ of Lemma 12(b), computed
   separately from the integer $N_{n-1}$. With $f_m$ counting only the
   multipliers of $C$, the rule reproduces the exact greedy digits of the
   truncated weights for $C=\{1,2,3,4,6\}$ and $C=\{1,\ldots,8\}$ through
   step 400, every residual of which lies in its cylinder, and for the first
   set it uses the carries $1,2,3,1$ at steps 105 to 108, those of check 5.
   The truncated part runs unchanged in both modes. This is a finite check of
   the rule's agreement; it does not show that the rule never fails.
7. the finite seed equation of Lemma 13 is checked at
   $M=\max(2,\operatorname{lcm}(C))$ for
   $C=\{1\}$, $\{1,2\}$, $\{1,2,3\}$, $\{1,2,3,4,6\}$,
   $\{1,2,3,4,6,12\}$ and $\{1,\ldots,8\}$. The exact seed sizes are
   $1,1,3,5,5,411$, respectively. Four doubling blocks extend each seed through
   $16M$, after which every divisor contribution, bit, positive carry bound
   and boundary carry $c_{2^jM}=1$ is recomputed from the digits. Comparison
   with exact truncated greedy, starting at index 2, runs through
   $\min(400,16M)$. The $M=12$ seed $\{2,3,6,7,10\}$ and its carries
   $1,2,3,1$ at steps 105--108 are pinned. An altered seed is rejected. This
   check is unchanged in quick mode and uses only exact integers and rational
   tails. It does not supply seeds for unbounded multiplier sets.

8. the displayed $M=60$ seeds for $C_4$ and $C_5$ on the multiplier page
   are checked directly, without a seed search: both row sums equal
   $2^{59}-1$. Their carries, computed from every proper-divisor
   contribution, lie in $[1,|C|]$ and end at $1$. The complete transition
   table at positions $28$--$30$ is checked, including the decrease from
   $c_{29}=2$ to $c'_{29}=1$, as are the signed recurrence and row equation
   for their difference. This refutes a nonnegative-carry repair invariant,
   not Boolean seed extension. Both modes run this check unchanged.

9. every set $C=\{1\}\cup B$ with $B\subseteq\{2,\ldots,12\}$, 2048 sets,
   has the half seed of Lemma 13 at $M=\max(2,\operatorname{lcm}(C))$, and for the
   1542 of them with $M\le2520$ the extremal whole-word iteration (14) of
   the [[research/leads/reciprocal_mersenne_greedy/multiplier_carries|multiplier page]]
   stabilizes at that seed. For $C=\{1,2,3,4,6\}$ and $M=12$ the iteration
   is run at every target $t<2^{11}$; at 427 targets it stabilizes at a
   pair $\ell<u$. Each such pair satisfies the first assertion of the
   stable-pair proposition on that page, and at the 16 of these targets that
   have a row solution $x$, that solution lies in $[\ell,u]$ within
   $\frac{16}{9}2^{M-4k}$ of the dyadic point $Y$, as in the second.
   All 427 pairs satisfy the unit mixed-carry difference on the initial
   borrow block. The 169 with $k\ge3$ satisfy the mixed-carry rejoin at
   $2k$, the ordinary-carry offsets $+1,-1$, and both formulas for the
   next block's forcing in (22)--(23). Ordinary carries are independently
   recomputed from their coefficient sums. Their terminal mixed carries
   equal $2^{M-1}-t$; this different-target test does not verify the
   half-target bound (17) or exclude its two-cycles.
   The weights $2^{-n}+4^{-n}+3\cdot8^{-n}$, which dominate their tails,
   meet a gap at step 3 for the target $\frac12$, and the multiplicities
   $\lambda_3=3$, $\lambda_4=2$, $\lambda_5=1$ beside the unit channel meet
   one at step 4 after the forced prefix $\{2,3\}$, although their mass
   $\frac37+\frac2{15}+\frac1{31}$ is below $\sum_{a=2}^8(2^a-1)^{-1}$.
   Every decision is exact and every weight is checked to exceed its tail.
   For the index-dependent
   family displayed on that page, with pure binary weights after index 9,
   all $2^8$ subsets of $\{2,\ldots,9\}$ are enumerated and none leaves a
   remainder in $[0,2^{-9}]$. Both modes run this check unchanged. It is a
   finite check: it supplies no seed for an unbounded family of sets.

10. along the certified greedy prefix of $\frac12$ from check 2, at
    $H=2,4,\ldots,64$ and $N=2H$, the block word $W$ of the digits in
    $(H,N]$ satisfies $s_N=2^Hs_H-W-G(W)$ exactly, where
    $G(W)=\sum_d\epsilon_d2^{N-d}w_d$, with $0<2^Hs_H-W<\frac32$; the
    words $W+1$ and $W-1$ give scaled residuals below $0$ and above an upper
    bound for $\sigma_N$. For $2\le H\le7$ and every word $W\ge1$ whose
    last one is at $k$, $1+G(W)-G(W-1)=2^N(w_k-\sum_{k<d\le N}w_d)$, which
    is $2^Ng_k+\sigma_N$. The selections through 32 are pinned, the old
    pending mass $E_{16}=\frac{376801}{344043}$ exceeds $1$, and the carry
    $c_{32}=2$ equals $E_{16}+G(W)+s_{32}$. The explicit terminal carries
    $u_H=\lfloor E_H\rfloor+1$ and $u_H+1$ produce at most two words;
    exactly one passes and agrees with the certified word. The terminal
    carry is also recomputed from divisor coefficients; $E_{32}<1$ and
    $c_{64}=2$ require the larger candidate on the half orbit. The admissible
    prefixes $q=3/8$, $H=2$, $F=\{2\}$ and $q=155/256$, $H=4$,
    $F=\{2,3,4\}$ test the automatic boundary cases $W_H=0$ and
    $W_H=2^H$. The prefix from check 5, with $q=4203/32768$ and $H=16$,
    gives $u_H=1$, $W_H=32768$: its first candidate has negative
    residual and its second exceeds the tail. This refutes a selection
    guarantee based only on prefix admissibility and integer carries.
    Enumerating every subset at $L=2,6$ finds exactly the three renewal
    identities of Lemma 14. Its Bang–Zsigmondy argument excludes all
    other endpoints; the finite check alone does not. Both modes run
    this check unchanged. No later doubling block is decided.

Six controls run in both modes: a non-gap ($\frac{16}{125}$ at step 3, which
lies between $L_{3,1}$ and $T_3$) must not certify as a gap; the floor and
ceiling enclosures bracket $2^Pw_n$; the enclosure of $E$ meets an independent
one built from $\sum_m\tau(m)2^{-m}$; and the least-denominator routine of
check 4 agrees with a direct search on every interval between two fractions of
denominator at most 10 in $[0,2]$; window classification handles boundary points
and an enclosure spanning the entire window; and closest-approach bounds and
minimizing steps agree with exact rational calculations for the two targets
through step 40, including the zero first-step distance for $\frac12$.

Arithmetic is exact in rationals for the finite-subsum and gap certificates
and otherwise uses integers scaled by $2^P$ with floor and ceiling enclosures;
an enclosure that straddles a threshold is resolved in exact rationals when it
is an equality and otherwise fails the run.

The precision for an $N$-step run is $P=2N+64$. If $D=2^P$, each term is
enclosed by $\lfloor D/(2^n-1)\rfloor$ and $\lceil D/(2^n-1)\rceil$.
Summing through $n=P$ and adding $2$ to the upper endpoint encloses $DE$,
because $T_P<2^{1-P}$. Subtracting term enclosures yields residual and tail
enclosures. The final cylinder is checked again from the selected set.
The near-miss test accepts only an enclosure entirely inside the open window
or disjoint from it; any partial overlap fails the check. For the minimum
distance, integer bounds at a common scale isolate one step's upper bound
strictly below every other step's lower bound.

Check 4 uses $P=3200$, sums the selected terms through $P$, and adds the same
tail upper bound $2/D$. The routine `simplest_fraction` finds a rational of
least denominator in each resulting closed interval. Here is its arithmetic
justification. If the interval contains an integer, its least integer has
both numerator and denominator no larger than those of any reduced
nonnegative fraction in the interval. Otherwise both endpoints have the same
integer part $f$. Subtract $f$ and invert, reversing the endpoints; this
decreases the sum of their rational denominators, so the descent terminates.
If $p/q$ simultaneously minimizes numerator and denominator in the descended
interval, $(fp+q)/p$ does so in the original interval: the transformation
preserves coprimality and both coordinates are nondecreasing in $p,q$.
Induction back from the integer case proves the routine's minimum-denominator
property. The finite grid control checks its implementation; it does not
replace this argument.

For the truncated weights in check 5, the scale $2^{6\cdot108}$ represents
every weight through step 108 exactly as an integer. Every residual is
compared with the exact rational tail
$\sum_{a\in\{1,2,3,4,6\}}2^{-an}/(2^a-1)$. The proposed carry rule is
evaluated separately, using only indices below the current step. The finite
failure refutes the rule's extension; it does not refute half membership
for the truncated weights or for the full Mersenne weights.

These are finite statements. Passing $N$ steps leaves every later step open,
so no check proves that any rational with infinite support is a sum of
distinct $1/(2^n-1)$, and none proves an irrationality. Check 4 excludes only
denominators below $2^{1000}$ for nonempty purely periodic supports.
Check 3 compares counts with a model; the events are not independent, and the
check can detect only effects present at the computed steps.
