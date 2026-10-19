---
name: research/erdos_617/parabola_completion_criterion
desc: Exact completion criterion for complementary parabola components, with square-root lower and square-root-logarithmic upper bounds on omitted intercepts; independence is unproved.
tags: [graph-theory, constructions, finite-fields, proved]
sources: []
created: 2026-09-22T14:35:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/parabola_completion_criterion

***

**A component-preserving coloring construction, not an E617 counterexample.**
This differs from the
[shifted square-field template](semiregular_parabola_template.md). It gives an
exact criterion for retaining nearly all unshifted parabola components while
completing the edge coloring. It does not establish the required independence
bounds; the particular completion exhibited below fails them.

Let $F=\mathbb F_r$ have odd order, and take vertices $F^2\cup\{\infty\}$
and colors $F$. For $J\subseteq F$, prescribe

$$
P_{j,t}=\{(j+u^2,t+u):u\in F\}
$$

as full color-$t$ components for all $t\in F$ and $j\notin J$.
The star colors are not prescribed beforehand. Put

$$
S=\{u^2:u\in F\},\qquad D_d=J\cap(J-d).
$$


## Exact criterion

The prescribed components admit an equivariant complete edge coloring
if and only if

$$
\boxed{D_d+S=F\quad(d\in F\setminus\{0\}).} \tag{1}
$$

For necessity, a vertical edge $(a,x)(a+d,x)$ assigned color $t$
has both endpoints outside the prescribed color-$t$ components.
They cannot lie together in one such component, since that component
has exactly one point with second coordinate $x$. Therefore, with
$u=x-t$, both $a-u^2$ and $a+d-u^2$ belong to $J$. This is (1).

Conversely, two old points with distinct second coordinates lie on a
unique $P_{j,t}$: subtraction of their parabola equations determines
$t$ uniquely. Assign their edge color $t$.
For each unordered pair $a\ne b$, (1) supplies $u_{ab}$ with
$a-u_{ab}^2,b-u_{ab}^2\in J$. Assign $(a,x)(b,x)$ color $x-u_{ab}$.
Also choose $u_a$ with $a-u_a^2\in J$ and assign
$\infty(a,x)$ color $x-u_a$; existence follows from (1) by fixing
any $b\ne a$. No vertical or star edge touches a prescribed component
in its own color, and the nonvertical rule introduces no edge leaving
one. Translating second coordinates by $s$ translates all colors by $s$.
Thus the completion is equivariant and preserves the components.

## A lower bound on omitted intercepts

For $r\ge7$, two translates of $S$ do not cover $F$.
Indeed, for $d\ne0$ the quadratic-character identity gives

$$
|S\cap(S+d)|=rac{r+1+\chi(d)+\chi(-d)}4
\ge\frac{r-1}{4}>1.
$$

To verify the identity, use
$\mathbf1_S(x)=(1+\chi(x)+\mathbf1_{x=0})/2$ and
$\sum_x\chi(x(x-d))=-1$. The latter follows by completing the
square and counting solutions of $(z-y)(z+y)=d^2$.
Since $|S|=(r+1)/2$, the asserted failure to cover follows.

Consequently (1) requires $|D_d|\ge3$. Writing $k=|J|$,

$$
\boxed{k(k-1)=\sum_{d\ne0}|D_d|\ge3(r-1).} \tag{2}
$$

In particular $J=\theta\mathbb F_q\subset\mathbb F_{q^2}$, of
order $q$, cannot work: it would have $q(q-1)<3(q^2-1)$.
This excludes that complementary choice before any independence test.

## Existence with few omitted intercepts

For all sufficiently large odd prime powers $r$, some $J$ satisfying
(1) has

$$
\boxed{|J|<7\sqrt{r\log r}.} \tag{3}
$$

Include each field element independently with probability
$p=\sqrt{12\log r/(r+1)}$, which is at most one for sufficiently
large $r$.
For fixed $a\ne b$, the pairs $\{a-s,b-s\}$ for $s\in S$ are
distinct edges of a graph of maximum degree two. Distinctness follows
because a repeated unordered pair with swapped endpoints would imply
$2(a-b)=0$. Each component is a path or cycle, so a matching contains
at least one third of the $(r+1)/2$ edges. The probability that no
candidate pair is contained in $J$ is therefore at most

$$
(1-p^2)^{(r+1)/6}\le r^{-2}.
$$

The union bound over unordered pairs is strictly below $1/2$.
Markov's inequality gives $\Pr(|J|>2pr)\le1/2$. Hence both conditions
hold for some $J$, and
$2pr<\sqrt{48r\log r}<7\sqrt{r\log r}$.

This proves compatibility of $r-O(\sqrt{r\log r})$ prescribed full
components in every color. It proves no independence bound on the
remaining $|J|r+1$ vertices. In fact the baseline nonvertical rule
retains all $r$ disjoint parabola $K_r$'s of every color, including
the omitted intercepts. By the [full-resolution obstruction](packing_tools.md),
that particular completion is not a counterexample. Any successful
use of this component template would have to change unprescribed
nonvertical edges as well and separately prove residual independence
at most $|J|$. No such assignment or proof has been obtained.
