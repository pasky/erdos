---
name: research/diophantine_representation_interfaces/mobius_split
title: "The limitation of a pointwise Mobius split"
desc: "A pointwise Mertens exponent theta gives squarefree error exponent one over three minus theta through this absolute-value split, leaving the quarter-power target."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E0969/_index|E0969]].

## E0969: the reach of the elementary Mobius split

The target is the order of the signed squarefree error; an Omega bound holds
along a sequence, not at every x. The pointwise Mertens estimate below is an
explicit hypothesis. Any proposed source for it retains its own recorded
standing.

Assume |M(t)|<=Ct^theta for t>=1 and 0<=theta<1, where M(t)=sum_(d<=t)mu(d). For
1<=D<=sqrt(x), split Q(x)=sum_(d<=sqrt(x))mu(d)floor(x/d^2). The part d<=D
equals x sum_(d<=D)mu(d)/d^2+O(D). Partial summation bounds the omitted infinite
main-term tail by O(xD^(theta-2)). Interchanging the finite sums in d>D gives

$$
\sum_{m\le x/D^2}\left(M(\sqrt{x/m})-M(D)\right),
$$

with a zero boundary term if endpoints coincide. Its absolute value is at most a
constant times x^(theta/2)(x/D^2)^(1-theta/2)+(x/D^2)D^theta, hence
O(xD^(theta-2)). Balancing at D=x^(1/(3-theta)) proves

$$
E(x)=O(D+xD^{\theta-2})=O(x^{1/(3-\theta)}).
$$

An epsilon loss in the M bound gives the corresponding epsilon loss here. This
reproduces 8/17 and 12/25 from the two claimed theta values without endorsing
their premises. Even theta=1/2 yields only 2/5 in this estimate; for theta>=0
this absolute-value split cannot produce an exponent below 1/3. This is a
limitation of the estimate, not a lower bound for E(x). It does not determine
the expected 1/4 order. Next test: cancellation in fractional parts or the
hyperbola tail beyond this pointwise M input. Stop if only theta is changed in
the same balance.
