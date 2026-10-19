"""Finite check of the greedy Singer-level construction in Z_q x H.

For prime p, q = p^2 + p + 1, a Singer perfect difference set B in Z_q is
built from the trace-zero elements of F_(p^3) and its perfect difference
property is checked directly. For each listed abelian group H of odd order
h <= p/4 (cyclic, and one non-cyclic case), the greedy rule of the proof
assigns c(0) = min B and then c(x), c(-x) for each pair {x, -x}, always
taking the least residue allowed by conditions S1-S3 against the values
already assigned. The check confirms that the greedy never runs out of
values, and then verifies by brute force that
A = {(b, 0) : b in B} u {(c(x), x) : x in H} has p + h elements, is strong
Sidon in Z_q x H (all unordered pair sums, doubles included, distinct), and
is maximal (every element outside A is a + b - c with c not in {a, b}).
The same brute force is run on two controls: the Singer set alone in Z_q
(maximal) and a constant level map (not Sidon). It also checks two retained
level maps outside the proved range, for (p, h) = (5, 7) and (11, 13), found
earlier by a randomized backtracking search; they record finite observations
only. Exact integer arithmetic;
standard library and the repository evidence harness only. Expected runtime
under a minute. Finite cases only: every larger case rests on the proof.
"""
import sys
from itertools import product
from tools import Checker, evidence_parser

# (p, H as a tuple of cyclic factor orders)
CASES = [(13, (3,)), (17, (3,)), (19, (3,)), (23, (5,)), (29, (7,)),
         (31, (7,)), (37, (9,)), (37, (3, 3)), (41, (9,)), (43, (9,)),
         (47, (11,)), (53, (13,))]

# retained level maps beyond h <= p/4, listed as c(0), c(1), ..., c(h-1)
WITNESSES = {(5, (7,)): [15, 0, 21, 7, 14, 23, 12],
             (11, (13,)): [11, 47, 16, 64, 42, 72, 6, 14, 48, 114, 118, 32,
                           52]}


def factor(n):
    primes, d = [], 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            while n % d == 0:
                n //= d
        d += 1
    return primes + ([n] if n > 1 else [])


def singer(p):
    """Perfect difference set modulo p^2+p+1 from trace-zero powers."""
    a, b = next((a, b) for a in range(p) for b in range(1, p)
                if all((x ** 3 + a * x + b) % p for x in range(p)))

    def mul(u, v):
        c = [0] * 5
        for i in range(3):
            for j in range(3):
                c[i + j] += u[i] * v[j]
        for d in (4, 3):
            c[d - 2] -= a * c[d]
            c[d - 3] -= b * c[d]
        return tuple(x % p for x in c[:3])

    def power(u, e):
        r = (1, 0, 0)
        while e:
            if e & 1:
                r = mul(r, u)
            u = mul(u, u)
            e >>= 1
        return r

    order = p ** 3 - 1
    primes = factor(order)
    g = next(v for v in ((n % p, n // p % p, n // p // p)
                         for n in range(2, p ** 3))
             if all(power(v, order // f) != (1, 0, 0) for f in primes))
    q = p * p + p + 1
    B, v = [], (1, 0, 0)
    for e in range(q):
        v1 = power(v, p)
        v2 = power(v1, p)
        if all((v[i] + v1[i] + v2[i]) % p == 0 for i in range(3)):
            B.append(e)
        v = mul(v, g)
    return q, B


def greedy(q, B, H):
    """The assignment of the proof; returns None if some step has no value."""
    elements = list(product(*[range(n) for n in H]))
    zero = tuple(0 for _ in H)

    def hadd(x, y):
        return tuple((a + b) % n for a, b, n in zip(x, y, H))

    def hneg(x):
        return tuple((-a) % n for a, n in zip(x, H))

    Bset = set(B)
    BB = {(x + y) % q for x in B for y in B}
    c = {zero: min(B)}
    order, seen = [], {zero}
    for x in elements:
        if x not in seen:
            order += [x, hneg(x)]
            seen |= {x, hneg(x)}
    for x in order:
        forbidden = set()
        S = list(c)
        # S1: new pair sums avoid existing pair sums at the same level
        for y in S + [x]:
            level = hadd(x, y)
            existing = {(c[z] + c[w]) % q for i, z in enumerate(S)
                        for w in S[i:] if hadd(z, w) == level}
            if y == x:
                half = pow(2, -1, q)
                forbidden |= {s * half % q for s in existing}
            else:
                forbidden |= {(s - c[y]) % q for s in existing}
        # S2: c(x) + c(-x) not in B + B
        if hneg(x) in c:
            forbidden |= {(s - c[hneg(x)]) % q for s in BB}
        # S3: c(v) + c(w) - c(v + w) not in B for v, w, v + w non-zero
        for w in S:
            if w != zero and hadd(x, w) in c and hadd(x, w) != zero:
                forbidden |= {(b - c[w] + c[hadd(x, w)]) % q for b in B}
        if hadd(x, x) in c and hadd(x, x) != zero:
            half = pow(2, -1, q)
            forbidden |= {(b + c[hadd(x, x)]) * half % q for b in B}
        for i, v in enumerate(S):
            for w in S[i:]:
                if v != zero and w != zero and hadd(v, w) == x:
                    forbidden |= {(c[v] + c[w] - b) % q for b in B}
        free = [r for r in range(q) if r not in forbidden]
        if not free:
            return None
        c[x] = free[0]
    return c


def audit(q, H, A):
    """Brute-force strong Sidon and maximality of A in Z_q x H."""
    moduli = (q,) + tuple(H)

    def add(x, y):
        return tuple((a + b) % n for a, b, n in zip(x, y, moduli))

    def sub(x, y):
        return tuple((a - b) % n for a, b, n in zip(x, y, moduli))

    sums, sidon = set(), True
    for i in range(len(A)):
        for j in range(i, len(A)):
            s = add(A[i], A[j])
            sidon &= s not in sums
            sums.add(s)
    blocked = set(A)
    for i in range(len(A)):
        for j in range(i, len(A)):
            s = add(A[i], A[j])
            for c in A:
                if c != A[i] and c != A[j]:
                    blocked.add(sub(s, c))
    size = 1
    for n in moduli:
        size *= n
    return sidon, len(blocked) == size


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    for p in sorted({p for p, _ in CASES}):
        q, B = singer(p)
        diffs = sorted((x - y) % q for x in B for y in B if x != y)
        checker.check(f'p={p}: B is a perfect difference set modulo {q}',
                      len(B) == p + 1 and diffs == list(range(1, q)))
        sidon, maximal = audit(q, (), [(b,) for b in B])
        checker.check(f'p={p}: control, B alone is maximal Sidon in Z_q',
                      sidon and maximal)
    for p, H in CASES:
        h = 1
        for n in H:
            h *= n
        checker.check(f'p={p}, H={H}: odd order h <= p/4',
                      h % 2 == 1 and 4 * h <= p)
        q, B = singer(p)
        c = greedy(q, B, H)
        checker.check(f'p={p}, H={H}: greedy assignment completes',
                      c is not None)
        if c is None:
            continue
        zero = tuple(0 for _ in H)
        A = sorted({(b,) + zero for b in B} | {(c[x],) + x for x in c})
        sidon, maximal = audit(q, H, A)
        checker.check(f'p={p}, H={H}: |A| = p + h', len(A) == p + h)
        checker.check(f'p={p}, H={H}: strong Sidon in Z_q x H', sidon)
        checker.check(f'p={p}, H={H}: maximal in Z_q x H', maximal)
        if (p, H) == CASES[0]:
            constant = sorted({(b,) + zero for b in B}
                              | {(min(B),) + x for x in c})
            checker.check(f'p={p}, H={H}: control, constant map not Sidon',
                          not audit(q, H, constant)[0])
    for (p, H), values in sorted(WITNESSES.items()):
        q, B = singer(p)
        c = {(x,): v for x, v in enumerate(values)}
        A = sorted({(b, 0) for b in B} | {(c[x],) + x for x in c})
        sidon, maximal = audit(q, H, A)
        checker.check(f'witness p={p}, H={H}: c(0) in B and |A| = p + h',
                      c[(0,)] in B and len(A) == p + len(values))
        checker.check(f'witness p={p}, H={H}: strong Sidon and maximal',
                      sidon and maximal)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
