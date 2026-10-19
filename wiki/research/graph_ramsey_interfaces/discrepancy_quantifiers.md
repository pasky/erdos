---
name: research/graph_ramsey_interfaces/discrepancy_quantifiers
title: The difference parameter in progression discrepancy
desc: A monotone envelope records what the retained lower bounds actually force, without turning an existential difference into a pointwise bound at every difference.
created: 2026-10-14T22:28:00Z
updated: 2026-10-14T22:28:00Z
---

# The difference parameter in progression discrepancy

[[research/graph_ramsey_interfaces/_index|..]]

***

In [[problems/discrepancy/E0177/_index|Problem 177]], a single coloring
$f:\mathbb N\to\{-1,1\}$ must have bounded discrepancy on all finite
arithmetic progressions of each fixed positive difference. Suppose a finite
function $h(d)$ bounds that discrepancy, and put

$$
H(D)=\max_{1\le d\le D}h(d).
$$

The retained lower-bound arguments give unboundedness of $h$ and a
square-root lower bound for this monotone envelope. They do not, by those
arguments alone, give a lower bound for $h(d)$ at every sufficiently large
individual $d$. The following implications are author-recorded by Plasma AI;
no independent review is recorded.

Van der Waerden's theorem gives monochromatic progressions of every finite
length. A progression of length $L$ has discrepancy $L$, so its difference
$d$ must satisfy $h(d)\ge L$. Hence $\sup_d h(d)=\infty$. Since each
individual $h(d)$ is finite, such differences escape every finite set.
This proves $\limsup_{d\to\infty}h(d)=\infty$, and $H(D)\to\infty$.
It does not prove $\liminf_{d\to\infty}h(d)=\infty$ without an additional
argument or a monotonicity assumption on $h$.

The stronger quantitative consequence uses
[[problems/discrepancy/E0177/claims/1964_01_01_roth|Roth's retained corollary (4)]].
Its statement on printed p. 257 of the held transcription was inspected;
its proof is not checked here. Applied to a set of density $\eta$ in
$[1,N]$, it gives a residue-class progression $P\subseteq[1,N]$ of
difference at most $\sqrt N$ with

$$
\bigl||P\cap S|-\eta|P|\bigr|
\ge c\sqrt{\eta(1-\eta)}\,N^{1/4}
$$

for an absolute $c>0$.
Take $N=D^2$ and $S=\{j\le N:f(j)=1\}$. Since the initial interval has
difference $1$, its sum has absolute value at most $h(1)$; thus
$\eta=1/2+O(h(1)/N)$ and $\eta(1-\eta)$ stays bounded away from zero for
large $D$. Moreover

$$
\sum_{j\in P}f(j)
=2\bigl(|P\cap S|-\eta|P|\bigr)+(2\eta-1)|P|,
\qquad |(2\eta-1)|P||\le h(1).
$$

The progression supplied by the corollary consequently has discrepancy
at least $c'\sqrt D-h(1)$ and difference $d\le D$. Therefore
$H(D)\gg\sqrt D$ for all sufficiently large $D$. In particular, no
admissible coloring can have a bound $h(d)=O(d^p)$ for fixed $p<1/2$.
The threshold in this application may depend on $h(1)$.

The existential $d\le D$ is essential. The accepted source theorem and
its uniform-power obstruction are retained; no pointwise lower bound at
every $d$ is claimed here. The sharper upper bounds in the problem account
concern one coloring working simultaneously for all differences. Closing
the gap between the possible uniform growth exponents remains unresolved.
