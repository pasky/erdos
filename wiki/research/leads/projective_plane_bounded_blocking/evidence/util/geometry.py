"""Exact arithmetic in GF(p^h) and incidence counts in PG(2, p^h).

Field elements are the integers 0, ..., q - 1, read as base-p digit vectors
of polynomials modulo a monic irreducible polynomial of degree h, found by
search. Points and lines of PG(2, q) are normalized homogeneous triples:
(x, y, 1), (x, 1, 0) and (1, 0, 0). A point (X, Y, Z) lies on the line
[a, b, c] exactly when aX + bY + cZ = 0.
"""

from __future__ import annotations

from collections import Counter

__all__ = [
    'Field',
    'line_loads',
    'normalize',
    'plane_points',
    'type_counts',
]


class Field:
    """Exact arithmetic in GF(p^h) by full addition and multiplication tables."""

    def __init__(self: Field, p: int, h: int) -> None:
        """Build the tables for GF(p^h)."""
        # store the parameters and find a modulus
        self.p, self.h, self.q = p, h, p**h
        self.modulus = self._irreducible()
        # tabulate the operations
        q = self.q
        self.add = [[self._add(a, b) for b in range(q)] for a in range(q)]
        self.mul = [[self._mul(a, b) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        self.inv = [0] + [next(b for b in range(q) if self.mul[a][b] == 1) for a in range(1, q)]

    def _digits(self: Field, a: int) -> list[int]:
        """Return the base-p digits of a, lowest first."""
        out = []
        for _ in range(self.h):
            out.append(a % self.p)
            a //= self.p
        return out

    def _value(self: Field, digits: list[int]) -> int:
        """Return the integer with the given base-p digits."""
        return sum(d * self.p**i for i, d in enumerate(digits))

    def _add(self: Field, a: int, b: int) -> int:
        """Add two elements digit by digit."""
        return self._value([(x + y) % self.p for x, y in zip(self._digits(a), self._digits(b), strict=True)])

    def _polymul(self: Field, a: int, b: int, modulus: list[int]) -> int:
        """Multiply two elements as polynomials modulo the monic modulus."""
        p, h = self.p, self.h
        prod = [0] * (2 * h - 1)
        for i, x in enumerate(self._digits(a)):
            for j, y in enumerate(self._digits(b)):
                prod[i + j] = (prod[i + j] + x * y) % p
        for d in range(2 * h - 2, h - 1, -1):
            c = prod[d]
            if c:
                for k in range(h + 1):
                    prod[d - h + k] = (prod[d - h + k] - c * modulus[k]) % p
        return self._value(prod[:h])

    def _mul(self: Field, a: int, b: int) -> int:
        """Multiply two elements modulo the chosen modulus."""
        return self._polymul(a, b, self.modulus)

    def _irreducible(self: Field) -> list[int]:
        """Return the first monic modulus for which every nonzero element is a unit."""
        p, h, q = self.p, self.h, self.p**self.h
        if h == 1:
            return [0, 1]
        for code in range(q):
            low = [(code // p**i) % p for i in range(h)]
            if low[0] == 0:
                continue
            modulus = [*low, 1]
            # x^(q-1) = 1 for every nonzero x holds exactly when the quotient ring is a field
            ok = True
            for x in range(1, q):
                r, base, e = 1, x, q - 1
                while e:
                    if e & 1:
                        r = self._polymul(r, base, modulus)
                    base = self._polymul(base, base, modulus)
                    e >>= 1
                if r != 1:
                    ok = False
                    break
            if ok:
                return modulus
        raise ValueError('no irreducible polynomial found')


def plane_points(field: Field) -> list[tuple[int, int, int]]:
    """Return the q^2 + q + 1 normalized points of PG(2, q)."""
    q = field.q
    pts = [(x, y, 1) for x in range(q) for y in range(q)]
    pts += [(x, 1, 0) for x in range(q)]
    pts.append((1, 0, 0))
    return pts


def normalize(field: Field, v: tuple[int, int, int]) -> tuple[int, int, int]:
    """Return the normalized representative of a nonzero vector."""
    for i in (2, 1, 0):
        if v[i]:
            s = field.inv[v[i]]
            return tuple(field.mul[s][c] for c in v)
    raise ValueError('zero vector')


def line_loads(field: Field, points: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
    """Return |S cap l| for every line l of PG(2, q), by direct incidence tests."""
    add, mul = field.add, field.mul
    loads = {}
    for a, b, c in plane_points(field):
        ma, mb, mc = mul[a], mul[b], mul[c]
        loads[(a, b, c)] = sum(1 for x, y, z in points if add[add[ma[x]][mb[y]]][mc[z]] == 0)
    return loads


def type_counts(loads: dict[tuple[int, int, int], int]) -> dict[int, int]:
    """Return the number of lines with each intersection size."""
    return dict(sorted(Counter(loads.values()).items()))
