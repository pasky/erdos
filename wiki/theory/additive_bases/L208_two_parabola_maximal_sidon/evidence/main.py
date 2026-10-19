"""Exhaustive finite check of the two-parabola maximal Sidon sets in F_q^3.

For every odd prime power q in {3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 49}
and every non-square mu of F_q, the set
A = {(t, t^2, 0)} u {(0, mu u^2, u)} of F_q^3 is checked to have 2q - 1
elements, to be strong Sidon (all unordered pair sums, doubles included,
distinct), and to be maximal (every x outside A equals a + b - c with
a, b, c in A and c not in {a, b}); the explicit witnesses of the proof are
also checked for every x outside A. As a control, for every non-zero square
mu the predicted repeated sum P(t) + P(-t) = C(u) + C(-u) with t^2 = mu u^2
is found. Exact finite-field arithmetic from explicit irreducible
polynomials, verified irreducible here; standard library and the repository
evidence harness only. Expected runtime about half a minute. Finite cases
only: the theorem for every odd q rests on the proof, not on this check.
"""
import sys
from itertools import product
from tools import Checker, evidence_parser

# q -> (p, monic modulus coefficients from constant term up, degree k)
FIELDS = {3: (3, [0, 1]), 5: (5, [0, 1]), 7: (7, [0, 1]), 11: (11, [0, 1]),
          13: (13, [0, 1]), 17: (17, [0, 1]), 19: (19, [0, 1]),
          23: (23, [0, 1]), 9: (3, [1, 0, 1]), 25: (5, [3, 0, 1]),
          27: (3, [2, 2, 0, 1]), 49: (7, [1, 0, 1])}


def field(q):
    """Return addition, negation and multiplication tables of F_q."""
    p, modulus = FIELDS[q]
    k = len(modulus) - 1
    vectors = list(product(range(p), repeat=k))
    index = {v: i for i, v in enumerate(vectors)}

    def multiply(u, v):
        coefficients = [0] * (2 * k - 1)
        for i in range(k):
            for j in range(k):
                coefficients[i + j] += u[i] * v[j]
        for degree in range(2 * k - 2, k - 1, -1):
            lead = coefficients[degree] % p
            for t in range(k + 1):
                coefficients[degree - k + t] -= lead * modulus[t]
        return tuple(c % p for c in coefficients[:k])

    add = [[index[tuple((a + b) % p for a, b in zip(u, v))] for v in vectors]
           for u in vectors]
    mul = [[index[multiply(u, v)] for v in vectors] for u in vectors]
    neg = [index[tuple((-a) % p for a in u)] for u in vectors]
    return p, k, vectors, add, mul, neg


def irreducible(p, modulus):
    """Degree at most three: irreducible exactly when it has no root."""
    k = len(modulus) - 1
    return k == 1 or all(sum(c * x ** i for i, c in enumerate(modulus)) % p
                         for x in range(p))


def check_field(checker, q):
    p, k, vectors, add, mul, neg = field(q)
    checker.check(f'q={q}: modulus irreducible over F_{p}',
                  irreducible(p, FIELDS[q][1]))
    zero = 0
    one = vectors.index(tuple([1] + [0] * (k - 1)))
    checker.check(f'q={q}: multiplicative identity and inverses',
                  all(mul[one][x] == x for x in range(q))
                  and all(any(mul[x][y] == one for y in range(q))
                          for x in range(1, q)))
    squares = {mul[x][x] for x in range(1, q)}
    nonsquares = [x for x in range(1, q) if x not in squares]
    checker.check(f'q={q}: half the non-zero elements are squares',
                  len(squares) == len(nonsquares) == (q - 1) // 2)
    two = add[one][one]
    half = next(y for y in range(q) if mul[two][y] == one)
    inverse = {x: next(y for y in range(q) if mul[x][y] == one)
               for x in range(1, q)}

    def vadd(a, b):
        return tuple(add[x][y] for x, y in zip(a, b))

    def vsub(a, b):
        return tuple(add[x][neg[y]] for x, y in zip(a, b))

    for mu in sorted(squares):
        # control: a square mu gives the predicted repeated sum
        u = one
        t = next(s for s in range(q) if mul[s][s] == mu)
        lhs = vadd((t, mul[t][t], zero), (neg[t], mul[t][t], zero))
        rhs = vadd((zero, mul[mu][mul[u][u]], u),
                   (zero, mul[mu][mul[u][u]], neg[u]))
        checker.check(f'q={q}, square mu={mu}: P(t)+P(-t) = C(u)+C(-u)',
                      lhs == rhs and t != zero)
    for mu in nonsquares:
        P = [(t, mul[t][t], zero) for t in range(q)]
        C = [(zero, mul[mu][mul[u][u]], u) for u in range(q)]
        A = sorted(set(P) | set(C))
        Aset = set(A)
        checker.check(f'q={q}, mu={mu}: |A| = 2q-1', len(A) == 2 * q - 1)
        sums = set()
        sidon = True
        for i in range(len(A)):
            for j in range(i, len(A)):
                s = vadd(A[i], A[j])
                if s in sums:
                    sidon = False
                sums.add(s)
        checker.check(f'q={q}, mu={mu}: strong Sidon', sidon)
        blocked = set(Aset)
        for i in range(len(A)):
            for j in range(i, len(A)):
                s = vadd(A[i], A[j])
                for c in A:
                    if c != A[i] and c != A[j]:
                        blocked.add(vsub(s, c))
        maximal = all((x, y, z) in blocked
                      for x in range(q) for y in range(q) for z in range(q))
        checker.check(f'q={q}, mu={mu}: maximal (every x outside A blocked)',
                      maximal)
        witnesses = True
        for x1, x2, x3 in product(range(q), repeat=3):
            x = (x1, x2, x3)
            if x in Aset:
                continue
            if x1 != zero:
                # a = C(x3), b = P(t), c = P(w), t - w = x1, t + w = sigma
                sigma = mul[add[x2][neg[mul[mu][mul[x3][x3]]]]][inverse[x1]]
                t = mul[add[sigma][x1]][half]
                w = mul[add[sigma][neg[x1]]][half]
                a, b, c = C[x3], P[t], P[w]
            elif x3 != zero:
                # a = P(0), b = C(u), c = C(v), u - v = x3, u + v = sigma
                sigma = mul[x2][inverse[mul[mu][x3]]]
                u = mul[add[sigma][x3]][half]
                v = mul[add[sigma][neg[x3]]][half]
                a, b, c = P[zero], C[u], C[v]
            else:
                # a = P(1), b = P(t'), c = P(1 + t') with t' = -x2/2
                tp = neg[mul[x2][half]]
                a, b, c = P[one], P[tp], P[add[one][tp]]
            witnesses &= (vsub(vadd(a, b), c) == x and c not in (a, b)
                          and {a, b, c} <= Aset)
        checker.check(f'q={q}, mu={mu}: explicit proof witnesses valid',
                      witnesses)


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    for q in sorted(FIELDS):
        check_field(checker, q)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
