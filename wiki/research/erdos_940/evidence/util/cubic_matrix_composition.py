"""Exact finite verification of the cubic matrix identities; requires SymPy."""

import sympy as s

z, a, b = s.symbols("z a b")
x = s.symbols("x1:4")
y = s.symbols("y1:4")


def red(f):
    return s.rem(s.expand(f), z * z + z + 1, z)


def mul(A, B):
    C = {}
    for (i, j), v in A.items():
        for (k, l), w in B.items():
            I, J = i + k, j + l
            key = (I % 3, J % 3)
            C[key] = C.get(key, 0) + v * w * z ** (j * k) * a ** (I // 3) * b ** (J // 3)
    return {key: red(v) for key, v in C.items()}


def trace(A):
    return red(3 * A.get((0, 0), 0))


def assert_scalar(A, f):
    assert red(A.get((0, 0), 0) - f) == 0
    assert all(v == 0 for key, v in A.items() if key != (0, 0))


c = [a, b, a * a * b]
F = sum(c[i] * x[i] ** 3 for i in range(3))
X = {(1, 0): x[0], (0, 1): x[1], (2, 1): x[2]}
Y = {(1, 0): y[0], (0, 1): y[1], (2, 1): y[2]}
XX = mul(X, X)
assert trace(X) == 0 and trace(XX) == 0
assert_scalar(mul(XX, X), F)
XY = mul(X, Y)
assert trace(XY) == 0
expected = 6 * a * b * (1 + z) * (x[0] * y[1] - x[1] * y[0]) * (x[1] * y[2] - x[2] * y[1])
assert red(trace(mul(XY, XY)) - expected) == 0
assert red(trace(mul(XX, Y)) - 3 * sum(c[i] * x[i] ** 2 * y[i] for i in range(3))) == 0

D = {
    (2, 0): x[0] * y[0],
    (1, 1): -z * z * x[0] * y[1],
    (0, 1): -a * z * z * x[0] * y[2],
    (0, 2): x[1] * y[1],
    (2, 2): -z * x[1] * y[2],
    (1, 2): a * z * z * x[2] * y[2],
}
YX = mul(Y, X)
assert all(red((1 - z) * D.get(key, 0) - XY.get(key, 0) + z * YX.get(key, 0)) == 0
           for key in set(D) | set(XY) | set(YX))
H = sum(c[i] ** 2 * x[i] ** 3 * y[i] ** 3 for i in range(3))
H += sum(c[i] * c[j] * (3 * x[i] ** 2 * x[j] * y[i] * y[j] ** 2 - x[i] ** 3 * y[j] ** 3)
         for i in range(3) for j in range(i + 1, 3))
DD = mul(D, D)
assert trace(D) == 0 and trace(DD) == 0
assert_scalar(mul(DD, D), H)
print("All cubic matrix identities verified exactly.")
