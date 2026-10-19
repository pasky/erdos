---
name: research/small_maximal_sidon_attack/evidence
title: Finite checks of the carry lemmas
desc: |
  Check finite carry identities, anchored-lift residuals, a coupled
  completion witness, two- and three-translate block coverings, the retained
  consecutive-difference rulers, and multiple-height seeds and completions.
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# Finite checks of the carry lemmas

[[research/small_maximal_sidon_attack/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/research/small_maximal_sidon_attack/evidence/main.py
```

For each prime $p\in\{5,7,11,13,17,19\}$ the program builds a Singer set
$B\subset[0,q)$, $q=p^2+p+1$, from the trace-zero powers of a primitive
element of $\mathbb F_{p^3}$, and checks its perfect difference property.
It then checks the three lemmas of the
[integer transfer analysis](../integer_transfer.md) on these sets: the
half-set lemma for every $1\le d<q$; the pointer lemma for every pair of
residues $c\ne\rho$; and the coherence lemma for the progression of
residue $c$, the least residue outside $B$, over heights $1\le s\le p+1$,
which blocks every interior height and is not strong Sidon. Finally it
recomputes, for the anchored lifts with heights assigned in increasing and
decreasing order of the elements of $B$, the strong Sidon property, the
full blocking of the classes of $B$, and the exact number of unblocked
targets in $[1,(p+2)q]$. Those numbers are pinned to the table on the
analysis page, so a changed construction or count fails the run.

The ruler part searches, for $3\le m\le 9$, every Golomb ruler
$0=b_1<\dots<b_m\le m(m-1)$ and checks that the largest $L$ for which
every integer $1,\dots,L$ is a difference equals the value recorded on the
analysis page, and that the retained ruler for each $m$ attains it. It
also checks four retained Sidon rulers with 12, 14, 18 and 20 marks, whose
initial difference runs are 47, 55, 90 and 97; these are witnesses, not
claimed maxima.

The [finite template page](../finite_templates.md) has two further checks.
The exact integers in
[the retained witness](assets/projective_completion.json) give a 40-point
strong Sidon seed in $[1,8001]$ with exactly 399 misses, and a maximal
48-point completion. The program checks those cardinalities, the domain,
all pair sums and all blockers directly. It does not repeat the discovery
search or assert that the completion is smallest.

For $p\in\{5,7,11,19,31,43\}$ it also builds the specified Singer base,
checks its perfect difference property, and enumerates every pair
$0\le c<d\le q$ with $d-c\notin B-B$. Exact bit masks test whether
$(c+B-B)\cup(d+B-B)$ contains $[0,q]$. The pair counts and distinct-gap
counts must match the page, including the assertion that the last four
cases have only the pair $(0,q)$. These checks run in both modes.

For the last four primes it also enumerates every $0\le a<b<c\le q$
whose pairwise distances avoid $B-B$, with $b-a\ne c-b$ and
$(a,c)\ne(0,q)$. It counts those whose three translates cover $[0,q]$.
For each first pair, a bit mask initially gives every admissible third
point. Each target not covered by the first pair intersects that mask
with the third points that cover it. Thus every remaining bit is one
valid template and every excluded bit fails a required condition. The
four exact totals are pinned to the finite template page.

The [multiple-height page](../multiple_heights.md) is checked against
[26 retained seeds and completions](assets/multiple_height_completions.json).
The asset contains the exact base representatives, height columns and
added integers for the explicit columns with
$p\in\{3,5,7,11,13,17,19,23\}$ and Skolem columns with
$p\in\{3,7,11,19,23\}$, each in increasing and decreasing base order.
The program reconstructs the deterministic Singer base, verifies the
column formula or Skolem pair partition and all internal differences,
and enumerates the seed's pair sums and blockers. It checks the exact
residual size, residual classes and rows, and absence of misses in
occupied classes. For the supplied additions it checks the final pair
sums, the interval bounds and blocking of every interval point. It does
not rerun the discovery of the Skolem systems or greedy completions.
The domains have at most 53,088 points and 117 final marks. The pinned
26-case grid includes the empty-residual boundary case at $p=3$.

For $p\in\{5,7,11,13,17,19,23,29,31,37,43\}$ another census checks
the minimum misses of $(c+B-B)\cup(d+B-B)$ in $[0,q)$ over every
$0\le c<d<q$. It imposes no compatibility restriction. Integer bit
masks check the complete domain; for one fixed optimum per prime a
literal difference-membership loop separately checks the attained
minimum. The open right endpoint and admissible pairs differ from the
earlier template census. Both new families run in both modes. These
are exact finite observations and imply no asymptotic completion bound
or obstruction.

All arithmetic is exact. The program uses the repository's evidence harness
and the Python standard library. The full run takes about a minute and a
half, almost all of it the search for $m=9$; `--quick` stops that search at
$m=8$ and takes a few seconds. Any failed obligation gives a nonzero exit,
also under optimized Python. The checks cover these finite cases only; the
lemmas for every $q$ rest on their proofs, and the counts support no
asymptotic statement.
