---
name: problems/extremal_graph_theory/E1157
title: Problem 1157
desc: |
  Asks for the most edges an $r$-graph on $n$ vertices can have with no $k$
  vertices spanning $s$ edges, the Brown–Erdős–Sós problem. The associated
  conjecture is proved for $s=3$ and, in its linear form, for large uniformity,
  but open for $3$-graphs with $k=s+3$ and $s\ge4$. A 2026 preprint claims the
  asymptotics whenever $(rs-k)/(s-1)$ is an integer $t$ with $2\le t<r$, except
  for $3$-graphs with even $s$.
tags:
- Hypergraphs
- Turán numbers
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-13T10:25:58Z
---

# Problem 1157

[[problems/extremal_graph_theory/_index|..]]

[[problems/extremal_graph_theory/E1157/claims/_index|claims/]]: The 1 claim page of Problem 1157, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $t,k,r\geq 2$. Let $\mathcal{F}$ be the family of all
$r$-uniform hypergraphs with $k$ vertices and $s$ edges. Determine

$$
\mathrm{ex}_r(n,\mathcal{F}).
$$

**Formulation.** The site's wording as accessed 2026-09-18T10:47Z
(page last edited 24 January 2026). The wording binds $t$, $k$ and $r$ and
then uses an unbound $s$ and no $t$; $s$ is a fourth parameter, the number
of edges, and $t$ is used only in the commentary's conjecture. With $s$ read
as a parameter the question is well defined: since a hypergraph contains a
member of $\mathcal F$ as a subgraph exactly when some $k$ of its vertices
span at least $s$ edges, $\mathrm{ex}_r(n,\mathcal F)$ is the largest number
of edges of an $r$-graph on $n$ vertices in which every $k$ vertices span
fewer than $s$ edges. This is the function of Brown, Erdős and Sós
([BES73], p. 55): "we shall denote $\mathrm{ex}(n;G^{(r)}(k,h))$
[sic; $s$ is meant] by $f^{(r)}(n;k,s)-1$. Thus $f^{(r)}(n;k,s)$ denotes the
smallest $t$ for which every $G^{(r)}(n,t)$ contains at least one
$G^{(r)}(k,s)$", so the site's $\mathrm{ex}_r(n,\mathcal F)$ is their
$f^{(r)}(n;k,s)-1$; later
papers write $f_r(n,v,e)$ or $f^{(r)}(n;s,k)$ with the vertex and edge
counts in various orders, and this page keeps the site's letters ($r$ the
uniformity, $k$ vertices, $s$ edges, $t$ the exponent). The question is
"Determine" and the site labeled it OPEN, so the wording is a notation
defect, not a degenerate statement, and the field describes the question as
written. The 1999 booklet [Va99] states the same question as its item 3.64
in yet other letters (quoted below).

**Status.** Open. The problem is a whole family of Turán-type questions. No
cited source determines $\mathrm{ex}_r(n,\mathcal F)$ in general.

The cited sources prove the following. The Theorem of Section 4 of [BES73]
([[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/theorem_section_4|result page]])
gives the general lower bound
$\mathrm{ex}_r(n,\mathcal F)>c_{k,s}n^{(rs-k)/(s-1)}$ for $k>r$ and $s>1$. The
authors remark, without proof, that it is sharp in the exponent when $s-1$
divides $rs-k$. When the quotient is an integer $t$ with $2\le t<r$, that is
$k=(r-t)s+t$, the order is $n^t$: the lower bound above has exponent $t$, and
$s$ edges through one $t$-set span at most $k$ vertices, so
$\mathrm{ex}_r(n,\mathcal F)\le(s-1)\binom nt/\binom rt$ (an observation made
here). The 2026 preprint [CHL26] claims the leading constant:
$\mathrm{ex}_r(n,\mathcal F)=(\pi+o(1))n^t$ with $\pi=2/(t!(2\binom rt-1))$ for
odd $s$ and $\pi=1/(t!\binom rt)$ for even $s$ and $r\ge4$, and $\pi>1/6$ for
$3$-graphs with even $s\ge4$
([[problems/extremal_graph_theory/E1157/claims/2026_09_29_chao_huang_liu|Chao, Huang and Liu 2026]]).
It is unrefereed, and as a partial result it leaves the problem open. The
Brown--Erdős--Sós conjecture states that
$\mathrm{ex}_r(n,\mathcal F)=o(n^t)$ once $k\ge(r-t)s+t+1$. It is proved for
$s=3$ and every $r>t\ge2$, with a matching $n^{t-o(1)}$ lower bound (Theorem 1
of [AlSh06],
[[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/theorem_1|result page]]).
This extends the Ruzsa--Szemerédi $(6,3)$-theorem and the Erdős--Frankl--Rödl
case $t=2$. In its linear form with $t=2$, the conjecture is proved for every
uniformity $r$ large enough in terms of the density (Theorem 3 of [KeLo20],
[[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/theorem_3|result page]]).
For 3-graphs and $t=2$, the sources give approximate versions. They show
$\mathrm{ex}_3(n,\mathcal F)=o(n^2)$ for $k=s+\lfloor\log_2s\rfloor+2$ (Sárközy
and Selkow, quoted) and for $k=s+O(\log s/\log\log s)$ (Conlon, Gishboliner,
Levanzov and Shapira, quoted). They also give the power saving
$\mathrm{ex}_3(n,\mathcal F)=O(n^{2-\varepsilon})$ for
$k=s+\lfloor\log_2s\rfloor+38$ (Theorem 1.3 of [JMMS25],
[[../library/extremal_graph_theory/janzer_2025_power_saving_brown_erdos_sos_problem/theorem_1_3|result page]]).
Finally, Theorem 1.4 of [ShTy23]
([[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/theorem_1_4|result page]])
gives a conditional reduction of the constant-deficiency form to a Turán
conjecture on 2-degenerate bipartite graphs.

The conjecture itself, $\mathrm{ex}_3(n,\mathcal F)=o(n^2)$ for $k=s+3$, is open
for every $s\ge4$ in every cited source, including the $(7,4)$ case. No
resolution and no proof claim was found in the search dated 2026-09-18 UTC whose
scope the Current assessment records. This is a bounded negative finding, not a
certificate of openness.

**Source.** [erdosproblems.com/1157](https://www.erdosproblems.com/1157),
accessed 2026-09-18 at 10:47 UTC: the problem page (OPEN, with
the site's note that no finite computation can settle it; last edited 24
January 2026; source keys [BES73], [Va99, 3.64]; commentary citing [1178],
[716] and [1076]), its empty discussion thread and its empty proof-claim
tab. Cite as: T. F. Bloom, Erdős Problem #1157,
https://www.erdosproblems.com/1157, accessed 2026-09-18.

**References.**

- [BES73] Brown, W. G., Erdős, P. and Sós, V. T., Some extremal problems on
  $r$-graphs. New Directions in the Theory of Graphs (Proc. Third Ann Arbor
  Conf., Univ. Michigan, 1971), Academic Press (1973), 53--63 (the venue
  from the running head of the Rényi archive scan and from the arXiv
  abstract of Glock, Kim, Lichev, Pikhurko and Sun, arXiv:2403.04474; the
  site's reference text gives "(1973), 53--63"); the definition, p. 55; the
  Theorem of Section 4 and the remark after it, p. 59. Cited from the Rényi
  archive copy (https://users.renyi.hu/~p_erdos/), an eleven-page typescript
  scan of printed pp. 53--63. Library home:
  [[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/_index|brown_1973_extremal_problems_graphs]].
- [Va99] Various, Some of Paul's favorite problems. Booklet produced for
  the conference "Paul Erdős and his mathematics", Budapest, July 1999;
  item 3.64 in Section 3.5, Set-systems. Library home:
  [[../library/number_theory/various_1999_some_pauls_favorite_problems/_index|various_1999_some_pauls_favorite_problems]]
  (the booklet's scan is image-only, in paired pages, and the item's leaf
  carries no legible printed page number).
- [AlSh06] Alon, N. and Shapira, A., On an extremal hypergraph problem of
  Brown, Erdős and Sós. Combinatorica 26 (2006), no. 6, 627--645,
  doi:10.1007/s00493-006-0035-9; Theorem 1, p. 2 of the authors' public
  preprint (https://www.cs.tau.ac.il/~nogaa/PDFS/asaferdos4.pdf, 15 pages,
  dated 2004). Not cited by the site.
  Library home:
  [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/_index|alon_2006_extremal_hypergraph_problem_brown_erdos_sos]].
- [KeLo20] Keevash, P. and Long, J., The Brown--Erdős--Sós conjecture for
  hypergraphs of large uniformity. arXiv:2007.14824v1 (29 July 2020);
  Proc. Amer. Math. Soc., doi:10.1090/proc/15487 (2021); Conjectures 1--2
  and Theorem 3, pp. 1--2 of the arXiv version. Not cited by the site. Library home:
  [[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/_index|keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large]].
- [ShTy23] Shapira, A. and Tyomkyn, M., A new approach for the
  Brown--Erdős--Sós problem. arXiv:2301.07758v1 (18 January 2023);
  EuroComb 2023 proceedings, doi:10.5817/cz.muni.eurocomb23-112, 812--818;
  Israel J. Math. 267 (2025), no. 2, 717--728, doi:10.1007/s11856-025-2714-5;
  Conjectures 1.1--1.3, p. 2; Theorem 1.4, p. 3 of the arXiv version. Not
  cited by the site. Library home:
  [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/_index|shapira_2023_new_approach_brown_erdos_sos_problem]].
- [JMMS25] Janzer, O., Methuku, A., Milojević, A. and Sudakov, B., Power
  saving for the Brown--Erdős--Sós problem. Discrete Analysis 2025:5, 16 pp.,
  doi:10.19086/da.138191 (published 10 July 2025; arXiv:2311.12765v2 is the
  journal typesetting); Conjecture 1.1 and Theorem 1.2, p. 2; Theorem 1.3,
  p. 3. Not cited by the site.
  Library home:
  [[../library/extremal_graph_theory/janzer_2025_power_saving_brown_erdos_sos_problem/_index|janzer_2025_power_saving_brown_erdos_sos_problem]].
- [Er74c] Erdős, Paul, Extremal problems on graphs and hypergraphs.
  Hypergraph Seminar, Lecture Notes in Math. 411 (1974), 75--84; pp. 80--81.
  Not cited by the site. Library home:
  [[../library/extremal_graph_theory/erdos_1974_extremal_problems_graphs_hypergraphs/_index|erdos_1974_extremal_problems_graphs_hypergraphs]];
  cited from the Rényi archive copy (https://users.renyi.hu/~p_erdos/), a
  ten-page typescript scan of printed pp. 75--84.
- [GiSo26] Gishboliner, L. and Solymosi, J., A simple counting argument for
  dense linear hypergraphs. arXiv:2606.25931 (24 June 2026, 7 pages), a
  preprint; Theorem 1.1 and Corollary 1.4, pp. 1--2; not held; a lead,
  recorded below. [SaTy25] Santos, G. and Tyomkyn, M., The Brown--Erdős--Sós
  conjecture in dense triple systems. arXiv:2508.09841 (13 August 2025); a
  lead, cited from its abstract. The $(k+2,k)$-problem papers named below
  are cited from their arXiv abstracts, except [BPSWZ26].
- [CHL26] Chao, T.-W., Huang, X. and Liu, H., Asymptotics of the
  Brown--Erdős--Sós problem at integer exponents. arXiv:2609.38115v1 (29
  September 2026, 22 pages); Theorems 1.1 and 1.2, p. 2; Theorems 2.3, 2.4
  and 2.6, pp. 5--7; Lemma 3.4, p. 12; Section 5, p. 20. A preprint, not
  cited by the site and not held in the library; its claim page is
  [[problems/extremal_graph_theory/E1157/claims/2026_09_29_chao_huang_liu|2026_09_29_chao_huang_liu]].
- [BPSWZ26] Bodnár, L., Pikhurko, O., Sun, S., Wang, Y. and Zeng, J., The
  quadratic Brown--Erdős--Sós problem for 3-uniform hypergraphs with 8 and 9
  edges. arXiv:2610.03323v1 (2 October 2026, 16 pages); Theorem 1.1, p. 2;
  Theorem 1.2, p. 3. A preprint, not cited by the site and not held; read for
  its statements and its lower-bound construction (pp. 1--7).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/83397bad317ac2cf180ffd418f791b8613d1a78f/FormalConjectures/ErdosProblems/1157.lean),
file `ErdosProblems/1157.lean`, added on 2026-10-07 (no file existed on
2026-09-18; the tree's `FormalConjectures/OEIS/1157.lean` is an OEIS
sequence file, not this problem). At the pinned commit it declares `erdos_1157` under `category research open, AMS 5` with proof
`sorry` and no `formal_proof` attribute: for all $r,k,s\ge2$ and all $n$,
`Hypergraph.configurationExtremalNumber n r k s` equals an `answer(sorry)`
function of $n$, $r$, $k$ and $s$; its docstring binds $s$, $k$ and $r$,
reading the site's unbound $s$ as the Formulation note does. The site's
indicator and the community database record a formalized statement since
2026-10-07 (on 2026-09-18 both recorded none), and the
database records the problem open (last update 23 January 2026), with no
formal proof and OEIS "possible".

## Current assessment

**The question (site formulation of 2026-09-18T10:47Z).** The statement
above; OPEN, with the site's note that no finite computation can settle it;
last edited 24 January 2026. The site's commentary, in this page's words:
the question is broad and hard, with many partial results, several of them
in [BES73] itself; it displays that paper's lower bound
$\mathrm{ex}_r(n,\mathcal F)\gg_{k,s}n^{\frac{rs-k}{s-1}}$, valid whenever
$k>r$ and $s>1$, and the Brown--Erdős--Sós conjecture that for all
$r>t\ge2$ and $s\ge3$ the Turán number is $o(n^t)$ whenever
$k\ge(r-t)s+t+1$; and it routes the case $t=2$ to Problem 1178, the case
$s=r=3$, $k=6$ to Problem 716, and the case $r=3$, $k=s+2$ to Problem 1076.
(The conjecture's display writes $\mathrm{ex}_t$ where the uniformity is
$r$; the letters are read as in the Formulation note.) The thread and the
proof-claim tab are empty. The cross-referenced pages are
[[problems/set_systems/E1178/_index|Problem 1178]], [[problems/set_systems/E0716/_index|Problem 716]]
and [[problems/set_systems/E1076/_index|Problem 1076]], whose accounts are their
own. The question is read as the general determination of
$\mathrm{ex}_r(n,\mathcal F)$ for all $r$, $k$ and $s$. A theorem that
determines it, exactly or to first order, on a range of the parameters
answers part of that question and is a partial claim here, as
[[problems/extremal_graph_theory/E1157/claims/2026_09_29_chao_huang_liu|Chao, Huang and Liu's integer-exponent asymptotics]]
are. Problems 716 and 1076 carry as claims the earlier results on the cases
the site routes to them, such as the refereed limits for 3-graphs at $k=s+2$
recorded below. The 2026 preprints on that case, the 3-graph part of [CHL26]
and [BPSWZ26], are recorded on Problem 1076 as
[[problems/set_systems/E1076/claims/2026_09_29_chao_huang_liu|Chao, Huang and Liu's]]
and
[[problems/set_systems/E1076/claims/2026_10_02_bodnar_pikhurko_sun_wang_zeng|Bodnár, Pikhurko, Sun, Wang and Zeng's]]
claim pages, rejected there because they answer the site's wording. The other
earlier determinations for particular parameters, such as the graph values in
Sections 2--3 of [BES73], have no claim pages here (Remaining gaps).

**The general lower bound.**
[[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/theorem_section_4|The Theorem of Section 4 of [BES73]]]
(p. 59): "For integers $k>r$ and $s>1$ there exists a positive
constant $c_{k,s}$ such that $f^{(r)}(n;k,s)>c_{k,s}n^{(rs-k)/(s-1)}$", by
the deletion method; the remark after it: "the exponent of $n$ in the above
inequality is not always best possible. It can, however, be shown to be
best possible when $s-1$ divides $rs-k$. For example, when $k=5$ and $s=4$
we know that $f^{(3)}(n;5,4)=O(n^{5/2})$, but here we obtain only
$f^{(3)}(n;5,4)>cn^{7/3}$." This is the site's displayed bound. Read depth:
claims checked for the theorem, the remark and the definitions (pp. 53--55,
59); the proof (pp. 59--61) is unchecked. The paper is a proceedings
article; the Rényi archive copy is a typescript scan.

**The conjecture and its proved cases.** In the site's letters the
conjecture asks for $\mathrm{ex}_r(n,\mathcal F)=o(n^t)$ when
$k\ge(r-t)s+t+1$, which [KeLo20] states as Conjecture 1 (p. 1): "For any
$r>t\ge2$ and $k\ge3$ any $r$-graph on $n$ vertices with no
$((r-t)k+t+1,k)$-configuration has $o(n^t)$ edges" (their $k$ is the
site's $s$). Against the lower bound above, whose exponent at $k=(r-t)s+t+1$
is $t-1/(s-1)$, the conjecture asks only for the upper bound $o(n^t)$; for
$s=3$, Theorem 1 of [AlSh06] gives
$n^{t-o(1)}<\mathrm{ex}_r(n,\mathcal F)=o(n^t)$.

- $s=3$, every $r>t\ge2$:
  [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/theorem_1|Theorem 1 of [AlSh06]]]
  (p. 2 of the preprint): "For any fixed $2\le k<r$ we have,
  $n^{k-o(1)}<f_r(n,3(r-k)+k+1,3)=o(n^k)$" (their $k$ is the site's $t$,
  their $v=3(r-t)+t+1$ the site's $k$, three edges). It extends the
  Ruzsa--Szemerédi $(6,3)$-theorem ($n^{2-o(1)}<f_3(n,6,3)=o(n^2)$, their
  (2)) and Erdős, Frankl and Rödl's $n^{2-o(1)}<f_r(n,3r-3,3)=o(n^2)$ for
  every $r\ge3$ (their (3), the case $e=3$, $k=2$ of their (1), so
  $3(r-2)+3=3r-3$ vertices; the preprint's display prints the vertex count
  as $3(r-3)+3$, a misprint, since on $3r-6$ vertices the statement fails
  for every $r\ge3$; [KeLo20], p. 2, states the same theorem as the case
  $k=3$ of $((r-2)k+3,k)$-configurations); those two papers are not held and
  are cited second-hand from [AlSh06] and [KeLo20]. Acceptance evidence:
  Combinatorica 26 (2006), refereed. Read depth: claims checked for Theorem
  1 in the authors' preprint; the journal text may differ from it; the proof
  (Sections 2--4) is unchecked.
- Large uniformity, $t=2$:
  [[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/theorem_3|Theorem 3 of [KeLo20]]]
  (p. 2): "For any $\varepsilon>0$ there is $r_0=r_0(\varepsilon)$
  such that for all $r\ge r_0$ and for all $k\ge3$ there exists $n_0=n_0(r,k)$
  such that any linear $r$-graph $G$ on $n\ge n_0$ vertices with no
  $((r-2)k+3,k)$-configuration has $d_{\mathrm{lin}}(G)<\varepsilon$", where
  $d_{\mathrm{lin}}(G)=e(G)\binom r2/\binom n2$; the paper says (p. 1) that
  Conjecture 1 "would follow from the case $t=2$", which reduces to this
  linear form, its Conjecture 2. Acceptance evidence: Proc. Amer. Math.
  Soc., refereed; cited from the arXiv v1, from which the journal text may
  differ; claims checked for the theorem and the conjectures, the
  bow-tie-graph proof unchecked. [GiSo26] (a 2026
  preprint; Theorem 1.1 and Corollary 1.4, pp. 1--2) gives, by a counting argument, an explicit density threshold
  $\frac{r-1}r\cdot\frac{k-2}{(r-2)(k-2)+1}+o(1)$ for linear $r$-graphs and
  derives the large-uniformity theorem from it; a preprint, recorded as a
  lead.
- Approximate versions for 3-graphs ($t=2$). Sárközy and Selkow, quoted as
  Theorem 1.2 of [JMMS25] (p. 2): $f(n,e+\lfloor\log_2e\rfloor+2,e)=o(n^2)$
  for every $e\ge3$; Solymosi and Solymosi's $f(n,14,10)=o(n^2)$ and Conlon,
  Gishboliner, Levanzov and Shapira's $f(n,e+O(\log e/\log\log e),e)=o(n^2)$
  (quoted on the same page; the last is arXiv:1912.08834), all by
  regularity, "barely below quadratic".
  [[../library/extremal_graph_theory/janzer_2025_power_saving_brown_erdos_sos_problem/theorem_1_3|Theorem 1.3 of [JMMS25]]]
  (p. 3): "For every $e\ge3$, there exists some $\varepsilon>0$
  such that $f(n,e+\lfloor\log_2e\rfloor+38,e)=O(n^{2-\varepsilon})$", the
  first power saving near the Sárközy--Selkow threshold, toward the
  Gowers--Long conjecture $f(n,e+4,e)=O(n^{2-\varepsilon})$; the paper
  notes that an additive constant is unavoidable at $e=3$ because the
  Ruzsa--Szemerédi construction gives $f(n,6,3)\ge n^{2-o(1)}$, and that
  $f(n,7,4)$ and $f(n,8,5)$ are also $n^{2-o(1)}$. Acceptance evidence:
  Discrete Analysis 2025:5, refereed; cited from the journal typesetting
  (arXiv v2); claims checked for the theorem and the introduction's account,
  the proof unchecked.
- Conditional:
  [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/theorem_1_4|Theorem 1.4 of [ShTy23]]]
  (p. 3): "Conjecture 1.3 implies Conjecture 1.1", where
  [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/conjecture_1_1|Conjecture 1.1]]
  asks for an absolute $d$ with $(e+d,e)$-configurations in every 3-graph
  with $\Omega(n^2)$ edges and Conjecture 1.3 asks that every graph with
  $\Omega(n^{3/2})$ edges contain some 2-degenerate graph on $k$ vertices
  with $2k-t$ edges; a route, not a bound. Refereed (Israel J. Math. 267
  (2025)); cited from the arXiv v1.

**The integer-exponent threshold.** When $k=(r-t)s+t$ for an integer
$2\le t<r$, one vertex below the conjecture's range, the order of
$\mathrm{ex}_r(n,\mathcal F)$ is $n^t$ (Status above), and the question becomes
the limit $\pi(r,t,s)=\lim_{n\to\infty}n^{-t}\mathrm{ex}_r(n,\mathcal F)$.
[[problems/extremal_graph_theory/E1157/claims/2026_09_29_chao_huang_liu|Theorem 1.1 of [CHL26]]]
(p. 2) states that for all $r>t\ge2$ and $s\ge2$ the limit equals
$2/(t!(2\binom rt-1))$ for odd $s$, and $1/(t!\binom rt)$ for even $s$ when
$r\ge4$. It does not cover $3$-graphs with even $s$, where the limit exists by
Delcourt and Postle's theorem and $\pi(3,2,2)=1/6$ is Rödl's packing value;
with that theorem it gives the existence of the limit for all $r>t\ge2$ and
$s\ge2$ (p. 2). Theorem 1.2 (p. 2) gives $\pi(3,2,s)>1/6$ for every even
$s\ge4$, and Section 5 (p. 20) adds $\pi(3,2,s)\le1/5$. The paper's
$f^{(r)}(n;s,k)$ has $s$ vertices and $k$ edges, the site's $k$ and $s$. The
even-$s$ value is the packing coefficient of a high-girth partial Steiner
system. The odd-$s$ value is larger and comes from packing pairs of edges that
meet in $t$ vertices, with their extra $t$-sets shared among many pairs. The
paper cites as earlier values Rödl's case $s=2$ and Glock, Joos, Kim, Kühn,
Lichev and Pikhurko's cases $s\in\{3,4\}$ for every $r>t\ge2$, and for
3-graphs the cases $2\le s\le7$; at $r=3$ its odd value $1/5$ agrees with the
limits at $s=3$, $5$ and $7$ below. Acceptance evidence: none, an unrefereed
preprint (v1 of 29 September 2026, the only version). Read depth: the
statements checked, the proof of Theorem 2.3 and the closing count of Theorem
2.4 checked, and the rest read through or for structure, as the claim page
states.

**The quadratic regime (leads).** For $r=3$ and $k=s+2$, where [BES73] gives
$\Theta(n^2)$, the question becomes the value
of $\lim f^{(3)}(n;s+2,s)/n^2$, whose existence Brown, Erdős and Sós
conjectured: Delcourt and Postle (arXiv:2210.01105) proved the limit exists
for all $s\ge2$, and Shangguan (arXiv:2210.11338, SIAM J. Discrete Math. 37
(2023) 1920--1929 per Crossref) extended this to every uniformity. For
3-graphs the limit is known for $2\le s\le7$: $s=4$ is $7/36$ (Glock, Joos,
Kim, Kühn, Lichev and Pikhurko, arXiv:2209.14177,
$f^{(3)}(n;6,4)=(\frac7{36}+o(1))n^2$), and $s=5$, $6$ and $7$ are due to
Glock, Kim, Lichev, Pikhurko and Sun (arXiv:2403.04474). [CHL26] claims the
limit $1/5$ for every odd $s$ (above), and Theorem 1.1 of [BPSWZ26] (p. 2)
claims the value $1/5$ at $s=9$ independently, by a finite-field construction
for the lower bound and computer-solved linear programs for the upper bound.
For $s=8$, Pikhurko and Sun (arXiv:2506.01739) determine the limit for every
uniformity at least 4 and give for 3-graphs only the lower bound $3/16$, which
they conjecture to be sharp; Theorem 1.2 of [BPSWZ26] (p. 3) gives the upper
bound $5053/26544=0.19036\ldots$, below the bound $1/5$ of [CHL26]. Letzter
and Sgueglia (arXiv:2312.03856) and Wang and Zeng (arXiv:2603.19345) treat even
$s$ at large uniformity (abstracts). This regime is
[[problems/set_systems/E1076/_index|Problem 1076]]'s and is recorded here from
the papers' abstracts, except [CHL26] and [BPSWZ26], read in the preprints.
[SaTy25] proves the $(k+3,k)$ statement for linear triple systems of linear
density above $4/5$ (abstract).

**Erdős's statements.** [Er74c], pp. 80--81, announces the two forthcoming
papers with Brown and Sós as the beginning of an organized treatment of extremal
questions for $r$-graphs and singles out, as "the most attractive unsolved
problem" (p. 80), the question (9) whether $f(n;G_3(6,3))/n^2\to0$; it records
the authors' lower bound $f(n;G_3(6;3))>cn^{3/2}$, their guess that the truth is
below $n^{2-\epsilon}$, which they could not prove even in the weaker form (9),
and Szemerédi's then-recent announcement of a proof of (9). Then, for 3-graphs,
$\lim f(n;G_3(4,2))/n^2=\frac16$; display (10),
$c_1n^{5/2}<f(n;G_3(5;4))<c_2n^{5/2}$; display (11),
$f(n;G_3(k,k-1))>n^{2+\varepsilon_k}$, with the exact value of $\varepsilon_k$
known to Erdős only for $k=5$; display (12),
$c_1^{(k)}n^2<f(n;G_3(k,k-2))<c_2^{(k)}n^2$ for every $k>3$; the guess (13) that
$\lim_{n=\infty}\frac1{n^2}f(n;G_3(k,k-2))=\frac16$ for every $k$; and the
"Theorem. Every $G_3(n;[\frac13\binom n2]+1)$ contains either a $G_3(5;3)$ or a
$G_3(6;4)$" (p. 81). [Va99], item 3.64 (Section 3.5): "Find the maximum number
of edges in a $t$-uniform hypergraph in which every $k$ vertices span at most
$r$ edges. This very difficult question contains the existence problem of block
designs, the Ruzsa--Szemerédi Theorem etc." (the booklet's $t$ and $r$ are the
site's $r$ and $s-1$).

**Search scope (2026-09-18 UTC).** None of the routes below found a
determination of $\mathrm{ex}_r(n,\mathcal F)$ in general, a proof of the
conjecture for any $s\ge4$ at small uniformity, or a proof claim.

- The site: problem page and discussion thread, as accessed 2026-09-18 and
  again on 2026-10-13 (the page last edited 24 January 2026, no comment), and
  the proof-claim tab (no proof claim); the formal-conjectures tree and the
  community database on 2026-09-18 and 2026-10-07 (the Formalization paragraph
  records what each held on each date).
- The primary sources, at the pages cited: [BES73] pp. 53--55 and 59, [Va99]
  item 3.64, [Er74c] pp. 80--81, [AlSh06] pp. 1--2, [KeLo20] pp. 1--2,
  [ShTy23] pp. 1--3, [JMMS25] pp. 1--3, [GiSo26] pp. 1--2, [CHL26] Sections
  1--3 and 5 (pp. 1--20), [BPSWZ26] pp. 1--7.
- arXiv: an all-fields advanced search for "Erdős", "Erdos" and "Erdös" over
  submissions from 2026-09-25 to 2026-10-13, which found [CHL26] and
  [BPSWZ26], and their abstract pages, accessed 2026-10-13 (one version
  each).
- Crossref: the records of [JMMS25] (doi:10.19086/da.138191) and
  bibliographic queries for [AlSh06], [KeLo20], [ShTy23] and [BES73] (the
  last returned no record for the proceedings article).
- arXiv API: the records of 2007.14824, 2301.07758, 2311.12765, 2606.25931,
  2508.09841, 1912.08834, 2210.11338, 2210.01105, 2209.14177, 2403.04474,
  2506.01739, 2312.03856 and 2603.19345; the search `abs:"Brown-Erdős-Sós"
  OR abs:"Brown-Erdos-Sos" OR abs:"Brown, Erdős and Sós" OR abs:"Brown,
  Erdos and Sos"` sorted by date (26 records: the papers named above,
  group-structure papers, coding-theory applications and a Ramsey variant;
  none claims the conjecture for $s\ge4$ at small uniformity).
- Semantic Scholar: the citation lists of [AlSh06] by DOI (47 records) and
  of [KeLo20] and [JMMS25] by arXiv identifier (none indexed), by title.

Not searched: MathSciNet, zbMATH, Google Scholar, X. Cited second-hand:
Ruzsa and Szemerédi 1978, Erdős, Frankl and Rödl 1986 and Sárközy and Selkow
2005, from the introductions of [AlSh06], [KeLo20] and [JMMS25]; the
$(k+2,k)$-problem papers other than [CHL26] and [BPSWZ26], from their
abstracts; the earlier values that [CHL26] cites, from its introduction.
[AlSh06], [KeLo20] and [ShTy23] are cited from the public preprints named in
the References; their journal texts may differ.

**Remaining gaps.** (1) The Ruzsa--Szemerédi and Erdős--Frankl--Rödl
theorems are cited second-hand from the introductions of [AlSh06] and
[KeLo20]. (2) Proof coverage is statements only on every source except
[CHL26], of which two steps of the upper bound are checked; no proof is
reviewed. (3) [AlSh06], [KeLo20] and [ShTy23] are cited from the preprints;
the journal texts may differ. (4) The quadratic regime and
the dense-linear results are recorded from abstracts, except [CHL26] and
[BPSWZ26]; the regime is Problem 1076's. (5) The site's notation defect is
recorded above and not resolved with the site. (6) The integer-exponent
asymptotics rest on the unrefereed preprint [CHL26]. (7) The earlier
determinations for particular parameters outside the cases routed to
Problems 716 and 1076 have no claim pages here: the graph values of [BES73],
the values at $s\le4$ for every $r>t\ge2$ that [CHL26] cites, Glock, Kim,
Lichev, Pikhurko and Sun's limits at $s=5$ and $s=7$ and Pikhurko and Sun's
at $s=8$ for every uniformity $r\ge4$, and the linear case $t=1$, which
[CHL26] (p. 2) calls elementary and completely understood.

## Known results

- [[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/theorem_section_4|Brown--Erdős--Sós, Theorem of Section 4]]
  (1973): $\mathrm{ex}_r(n,\mathcal F)>c_{k,s}n^{(rs-k)/(s-1)}$ for $k>r$,
  $s>1$; sharp in the exponent when $s-1\mid rs-k$, as the authors remark
  without proof.
- [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/theorem_1|Alon--Shapira, Theorem 1]]
  (2006): the conjecture for $s=3$ and every $r>t\ge2$, with the matching
  $n^{t-o(1)}$ lower bound.
- [[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/theorem_3|Keevash--Long, Theorem 3]]
  (2020; PAMS 2021): the $t=2$ linear form for every $r\ge r_0(\varepsilon)$.
- [[../library/extremal_graph_theory/janzer_2025_power_saving_brown_erdos_sos_problem/theorem_1_3|Janzer--Methuku--Milojević--Sudakov, Theorem 1.3]]
  (2025): $\mathrm{ex}_3(n,\mathcal F)=O(n^{2-\varepsilon})$ for
  $k=s+\lfloor\log_2s\rfloor+38$; Sárközy--Selkow's $o(n^2)$ at
  $k=s+\lfloor\log_2s\rfloor+2$ quoted there.
- [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/theorem_1_4|Shapira--Tyomkyn, Theorem 1.4]]
  (2023; Israel J. Math. 2025): Conjecture 1.3 implies the
  constant-deficiency
  [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/conjecture_1_1|Conjecture 1.1]].
- [Er74c] pp. 80--81 (1974): the program as Erdős stated it, displays
  (9)--(13).
- [[problems/extremal_graph_theory/E1157/claims/2026_09_29_chao_huang_liu|Chao--Huang--Liu, Theorems 1.1 and 1.2]]
  (2026 preprint, unrefereed): $\lim n^{-t}\mathrm{ex}_r(n,\mathcal F)$ at
  $k=(r-t)s+t$ for every $r>t\ge2$ and $s\ge2$, except $3$-graphs with even
  $s$, where for $s\ge4$ it shows that the limit lies in $(1/6,1/5]$.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/_index|alon_2006_extremal_hypergraph_problem_brown_erdos_sos]]
- [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/conjecture_1|alon_2006_extremal_hypergraph_problem_brown_erdos_sos / conjecture_1]]
- [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/proposition_5_1|alon_2006_extremal_hypergraph_problem_brown_erdos_sos / proposition_5_1]]
- [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/proposition_5_2|alon_2006_extremal_hypergraph_problem_brown_erdos_sos / proposition_5_2]]
- [[../library/extremal_graph_theory/alon_2006_extremal_hypergraph_problem_brown_erdos_sos/theorem_1|alon_2006_extremal_hypergraph_problem_brown_erdos_sos / theorem_1]]
- [[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/_index|brown_1973_extremal_problems_graphs]]
- [[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/conjecture_p62|brown_1973_extremal_problems_graphs / conjecture_p62]]
- [[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/theorem_p62|brown_1973_extremal_problems_graphs / theorem_p62]]
- [[../library/extremal_graph_theory/brown_1973_extremal_problems_graphs/theorem_section_4|brown_1973_extremal_problems_graphs / theorem_section_4]]
- [[../library/extremal_graph_theory/erdos_1974_extremal_problems_graphs_hypergraphs/_index|erdos_1974_extremal_problems_graphs_hypergraphs]]
- [[../library/extremal_graph_theory/janzer_2025_power_saving_brown_erdos_sos_problem/_index|janzer_2025_power_saving_brown_erdos_sos_problem]]
- [[../library/extremal_graph_theory/janzer_2025_power_saving_brown_erdos_sos_problem/theorem_1_3|janzer_2025_power_saving_brown_erdos_sos_problem / theorem_1_3]]
- [[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/_index|keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large]]
- [[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/theorem_12|keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large / theorem_12]]
- [[../library/extremal_graph_theory/keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large/theorem_3|keevash_2020_brown_erdos_sos_conjecture_hypergraphs_large / theorem_3]]
- [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/_index|shapira_2023_new_approach_brown_erdos_sos_problem]]
- [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/conjecture_1_1|shapira_2023_new_approach_brown_erdos_sos_problem / conjecture_1_1]]
- [[../library/extremal_graph_theory/shapira_2023_new_approach_brown_erdos_sos_problem/theorem_1_4|shapira_2023_new_approach_brown_erdos_sos_problem / theorem_1_4]]
- [[../library/number_theory/various_1999_some_pauls_favorite_problems/_index|various_1999_some_pauls_favorite_problems]]

<!-- END problem library links -->
