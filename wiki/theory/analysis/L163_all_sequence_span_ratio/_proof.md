---
name: theory/analysis/L163_all_sequence_span_ratio/_proof
title: Proof of the all-sequence consecutive-span ratio bound
desc: Converts a putative small ratio into uniformly small short-arc count errors, extracts a finite list, and contradicts its explicit prefix discrepancy lower bound.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Proof of the all-sequence consecutive-span ratio bound

***

Use the conventions of
[[theory/analysis/L163_all_sequence_span_ratio/_index|L163]]. The complete
supporting deductions are the canonical research pages linked below; their
exact examined portions also survive in the
[[theory/analysis/L163_all_sequence_span_ratio/evidence/verify/whole_statement/_index|whole-statement record]].
No distinct-point theorem is used to infer the repeated-point assertion.

Fix $\alpha=1/200$, let $r$ be large and put $A=\alpha\log r$.
If a sequence violated the proposed limsup bound, then for some $0<C<A$,
eventually $M_n/m_n\le1+C/r$. The mean identity gives
$n(M_n-m_n)\le C$ and $nM_n\le r+C$. For $n=\lfloor t\rfloor$ set
$a_t=r-nm_n$ and $b_t=tM_n-r$. These are nonnegative; all $r$-spans lie in
$[(r-a_t)/t,(r+b_t)/t]$ and

$$
a_t+b_t\le C+(r+C)/n<A
$$

at every sufficiently large real $t$.

The two label injections in
[[research/erdos_1221/ko26b_lemma_2_1_reconstruction|Lemma 2.1]] and the
[[research/erdos_1221/all_sequence_composition|label, terminal-count and real-lift transfers]]
apply to this hypothesis, with every coincident term counted separately.
The finite scale iteration of
[[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]]
therefore supplies absolute $C_0,C_1$ such that, when $r\ge C_0A$, all late
integer $n$, all $x$ and all $0\le D\le S$ satisfy

$$
\left|N_n((x,x+D/n])-D\right|\le B,\qquad
S=\frac{\sqrt{Ar}}{\log^2(r/A)},\quad
B=3A+\frac{C_1A}{\log(r/A)}.
$$

One time threshold covers the entire range of $D$. Proposition 1221.1 of
[[research/erdos_1221/connections|the extraction argument]] chooses a short
arc avoiding the early terms and reads later terms in arrival order. For
$B\ge1$ and $S\ge2$ it yields a list of length
$L'\ge\lfloor S\rfloor-B$ in $(0,1)$, with repetitions allowed, whose
maximum prefix star discrepancy $H_{L'}$ is at most $B$. The complementary
arc errors have coefficients $1-u$ and $-u$, so this is $B$, not $2B$.

The complete
[[research/erdos_1221/finite_list_prefix_bound|four-block finite-list proof]]
gives, for every nonempty list,

$$
H_{L'}\ge\frac{\lfloor\log_4L'\rfloor}{16}
\ge\frac{\log L'}{16\log4}-\frac1{16}.
$$

Its range and jump argument includes repeated entries and the right jump at
zero; it consumes no optimized discrepancy theorem from an unprovided source.
Now $B=3\alpha\log r+O(1)$ and
$\log S=\frac12\log r-\frac32\log\log r+O(1)$. Thus $L'\ge S/2>0$
for all sufficiently large $r$, and the two discrepancy bounds imply

$$
3\alpha\log r+O(1)\ge
\frac{\log r}{32\log4}-O(\log\log r).
$$

This is impossible eventually, since $3/200<1/64<1/(32\log4)$.
All constants in this comparison are absolute. The sequence-dependent time
threshold only changes how late the extraction is made. Hence one absolute
$r_0$ gives the claimed inequality for every sequence. Infinite limsup
ratios satisfy it directly.

For fixed $r\ge r_0$, every value in the infimum defining $\mu_r$ is at
least $1+\log r/(200r)$. Taking that infimum, then subtracting one and
multiplying by $r$, proves the quantitative consequence. Its lower bound
$\log r/200$ tends to infinity. No limit and extremum are interchanged.
