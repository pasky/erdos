[cut]

From the repository root run:

```sh
uv run --no-sync python wiki/theory/polynomials/L144_cubic_lemniscate_length/evidence/main.py
```

The program uses the repository's `tools.Checker` and python-flint arb and acb
balls at 64 bits. It takes about five minutes on one thread and reads no
input files. It implements Sections 5 to 7 of the
[[theory/polynomials/L144_cubic_lemniscate_length/_proof|proof]]: thirteen
parameter boxes of width $1/64$ on which the scaled integral $I(a)$ is
negative, an adaptive cover of $7/512\le\arcsin(2a^3)\le\pi/2$ by parameter
boxes on which the length is below $L_0-1/100$, the check that the two
regimes overlap, and the check that the boxes of the second regime tile its
range. Every bound is a sum of exact piece widths times ends of balls, so it
holds uniformly on its box; tolerances affect only how many pieces are used.
A control at $\arcsin(2a^3)=1/2$ computes upper and lower bounds and checks
that they differ by less than $0.05$. The upper integral ends at a dyadic
enclosure of $\pi$ from above; the lower integral ends at one from below and
omits the singular window. Each window is checked to lie inside $[0,\pi]$
and to contain the critical angle for the whole parameter box.

The arithmetic uses the enclosing endpoints and unions documented for
[python-flint arb](https://python-flint.readthedocs.io/en/latest/arb.html),
with root enclosures from
[python-flint acb](https://python-flint.readthedocs.io/en/latest/acb.html).
The proof explains why choosing either quadratic root or any cube root
preserves the sum. Integration uses real interval bounds, without assuming
that a complex integrand is analytic across a branch cut. A finite enclosure
at the depth limit is still a valid, possibly coarse bound; a nonfinite one
fails. No tolerance is accepted as an error estimate.

The program does not check the written reductions: the length integral, the
root identities, the comparison with $z^3-c$, the tail constant's derivation
and the reduction of all cubics to the family are proved on the proof page.
Every failed obligation, including a nonfinite enclosure in the first regime,

[cut]

causes a nonzero exit.
