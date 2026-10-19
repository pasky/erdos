---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/theorem_1_1
title: "Theorem 1.1: f(n) has normal order alpha log n with variance x(log x)^2/(log log x)^5"
desc: |
  The number $f(n)$ of iterations of Euler's function needed to reach $1$ has
  normal order $\alpha\log n$ for a constant $\alpha\in[1/\log3,1/\log2]$:
  the variance about $\alpha\log n$ up to $x$ is
  $O(x(\log x)^2/(\log\log x)^5)$, so $f(n)/\log n\to\alpha$ on a set of
  natural density one; its Lean formalization is rebuilt and kernel-replayed
  here.
created: 2026-10-14T20:20:13Z
updated: 2026-10-19T06:24:13Z
---

***

## Statement

Let $\varphi_0(n)=n$, $\varphi_{k+1}=\varphi\circ\varphi_k$, and
$f(n)=\min\{k:\varphi_k(n)=1\}$ for $n\ge1$. **Theorem 1.1.** There is a
constant $\alpha$ with $1/\log3\le\alpha\le1/\log2$ such that, for all
sufficiently large $x$,

$$
\sum_{n\le x}\bigl(f(n)-\alpha\log n\bigr)^2\ll\frac{x(\log x)^2}{(\log\log x)^5},
$$

and

$$
\#\Bigl\{3\le n\le x:\ |f(n)-\alpha\log n|>\frac{\log n}{\log\log n}\Bigr\}
\ll\frac{x}{(\log\log x)^3}+\sqrt x.
$$

In particular, $f(n)/\log n\to\alpha$ on a set of natural density one, which
answers the first two questions of
[[../wiki/problems/arithmetic_functions/E0408/_index|Problem 408]].

The paper's $f$ counts from $\varphi_0$, so $f(1)=0$; Problem 408 and the
formalization count from $\varphi_1=\varphi$, so $f(1)=1$. The two agree for
$n\ge2$, and no density changes.

**Source.** Plasma AI, *The normal order of the number of iterations of
Euler's function*, preprint (2026), `paper/totient_iterates.tex`, label
`thm:main`, Section 1, in
[plasma-ai/erdos-408 at 4ea44bf](https://github.com/plasma-ai/erdos-408/tree/4ea44bf911f8668aec10ec25c4b309e8ed476666).
The formalization states the two bounds as `Erdos408.normal_order_rate` in
`Challenge.lean`, with the exceptional count taken over $1\le n\le x$ and
$\log n/\log\log n<|f(n)-\alpha\log n|$, and proves it in `Solution.lean`.

**Read depth.** Claims checked: the statement was read clause by clause in the
TeX source and compared with `Challenge.lean`. The paper's proof was not read.
The formalization's proof of `normal_order_rate` was rebuilt, checked with
Comparator and replayed in the kernel
([[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt|the replay receipt]]), and the
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]
found the statement faithful to this theorem, graded on 2026-10-14.
