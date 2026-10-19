---
name: theory/combinatorics/L238_normalized_core_near_clique_bound/_proof
desc: Hereditary caps bound outsider degrees; anchor incidence and a safe induced deletion force the near-clique inequality.
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# theory/combinatorics/L238_normalized_core_near_clique_bound/_proof

***

Use the hypotheses and notation of [[theory/combinatorics/L238_normalized_core_near_clique_bound/_index|L238]].
Fix an $r$-set $T$ with $h\le a-2$ missing edges. Every vertex outside $T$
has at most $h+1$ neighbors in $T$, because

$$
D_r(r+1)=\binom r2+1.
$$

Put $c=|T\cap Q|$. If $c\ge3$, the missing anchor pairs and the fact that
every nonanchor sees at most two anchors give at least

$$
\binom c2+(c-2)(r-c)
=r+(c-3)(r-c/2)\ge r
$$

missing edges, contrary to $h\le a-2<r$.
If $c=2$, write the anchors as $q_l,q_m$. Their nonedge uses one of the
$h$ missing pairs, so at least $r-h-1$ other vertices of $T$ see both and
belong to $B_{lm}$. But the positive other deficits and their sum give

$$
|B_{lm}|\le d_l+d_m-1\le r-a,
\qquad r-h-1\ge r-a+1,
$$

a contradiction. Thus $c\le1$, proving also the last assertion.

If $c=0$, count incidences between $T$ and the $a$ outside anchors.
Every vertex of $T$ supplies at least one; each anchor supplies at most
$h+1$. Consequently $r\le a(h+1)$.

Suppose $c=1$, with anchor $q_l$, and let $p=|T\cap P_l|$.
Every vertex of $T\setminus P_l$ has a neighbor among the other anchors:
if it sees $q_l$, it is two-supported, and otherwise all its anchor support
lies outside $l$. Thus

$$
r-p\le(a-1)(h+1).
$$

If $p\le h+1$, this proves the result. Otherwise any omitted vertex of
$P_l$ would see more than $h+1$ vertices of $T$, so $P_l\subseteq T$.
Assume for contradiction $r>a(h+1)$. An independent $a$-set in $H-T$
has at most $a(h+1)<r$ neighbors in $T$, so could be augmented by a
vertex of $T$. Hence $\alpha(H-T)\le a-1$. The other $a-1$ anchors
remain, giving equality.

The induced graph $H-T$ has order $(a-1)r+1$. Every remaining vertex has
one or two neighbors among those anchors: the whole private row of the
removed anchor was deleted, and a surviving exception loses at most one
support endpoint. At most $b\le r$ two-supported vertices remain.
This contradicts the stated minimum-anchor property with $k=a-1$.
All caps are inherited. For comparison with the normalized-core language,
singleton-support classes are cliques, since a nonadjacent pair in one
class would augment the remaining maximum anchor set; their deficits
satisfy the usual counting identity automatically. No least-color budget
or exception-degree bound is needed.

This proves $r\le a(h+1)$. Taking $h=1$ gives the $K_r-e$ assertion.
Finally suppose $r\le4a-4$. Then $\lceil r/a\rceil-1\le3$.
If an $r$-set has fewer than this many missing edges, their number is at
most two, hence at most $a-2$. The proved bound gives
$h+1\ge r/a$, so $h\ge\lceil r/a\rceil-1$, a contradiction.
$\square$
