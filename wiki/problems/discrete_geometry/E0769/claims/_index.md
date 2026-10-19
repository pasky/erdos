---
name: problems/discrete_geometry/E0769/claims
desc: The 7 claim pages of Problem 769, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T07:56:38Z
updated: 2026-10-19T10:54:07Z
---

# problems/discrete_geometry/E0769/claims

[[problems/discrete_geometry/E0769/_index|..]]

[[problems/discrete_geometry/E0769/claims/1974_01_01_burgess_erdos|1974_01_01_burgess_erdos]]: Erdős (Math. Balkanica 4, 1974, a congress volume) proves with Burgess that
$c(n)\le(2^n-2)((n+1)^n-2)-1$ and says a theorem of Brauer gives
$c(n)<\alpha n^{n+1}$. The result is partial, and its status is claimed.

[[problems/discrete_geometry/E0769/claims/1998_02_01_hudelson|1998_02_01_hudelson]]: Hudelson (J. Combin. Theory Ser. A 81, 1998) proves $c(n)\ll(2n)^{n-1}$ for
every $n$, a bound below the one Burgess and Erdős proved. The paper is
refereed, and the result is partial.

[[problems/discrete_geometry/E0769/claims/2018_03_24_connor_marmorino|2018_03_24_connor_marmorino]]: Connor and Marmorino (J. Geom. 109, 2018) prove $c(n)\ge2^{n+1}-1$ for
$n\ge3$, $c(n)\le1.8\,n^{n+1}$ when $n+1$ is prime, and $c(n)\le e^2n^n$
otherwise. The paper is refereed, and the result is partial.

[[problems/discrete_geometry/E0769/claims/2026_07_14_snyder|2026_07_14_snyder]]: A Lean 4 theorem credited to Colin Snyder of Star Fleet Math states that
$c(n)\gg n^n$ fails, through an explicit $o(n^n)$ tiling threshold in odd
dimensions. The formal-conjectures catalog links it, and it has not been
audited here.

[[problems/discrete_geometry/E0769/claims/2026_07_24_zeng|2026_07_24_zeng]]: Jeffrey Zeng's proof-claim listing bounds the collective gcd threshold $h(n)$
by a square-root scale whenever $h(n)$ exceeds $P(n)$, and deduces
$c(n)=o(n^n)$ for odd $n$, so the uniform lower bound $c(n)\gg n^n$ fails. The
claim is partial and unreviewed.

[[problems/discrete_geometry/E0769/claims/2026_08_05_korsky|2026_08_05_korsky]]: Samuel Korsky's manuscript bounds $c(n)$ above by
$(C\max\{P(n),n^{1/(4\sqrt e)+\varepsilon}\})^n$, with $(\log n)^2$ in place
of the power under GRH, and below for even $n$ by about
$(1-1/\log_2 3)\,n2^n$. The claim is partial and unreviewed.

[[problems/discrete_geometry/E0769/claims/2026_10_19_plasma_ai|2026_10_19_plasma_ai]]: An author-recorded residue-path argument and an odd-dimensional gcd bound
show that every cube count from $1+(2^d-2)(M^d-1)$ on, with
$M=\lfloor\sqrt{3d}\rfloor+1$, is realized for odd $d\ge3$, so
$c(d)/d^d\to0$ along odd $d$ and $c(n)\gg n^n$ fails; tier 0, catalog
acceptance pending.

***
