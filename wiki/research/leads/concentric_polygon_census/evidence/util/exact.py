"""Exact cyclotomic fields and certified ordering of quadratic real roots.

Equalities use Q[z]/Phi_N. Arb is used only for strict inequalities in the
embedding z=exp(2*pi*i/N); exhausted precision raises, never guesses.
"""

from functools import cmp_to_key

from flint import arb, ctx, fmpq, fmpq_poly
from sympy import Poly, Symbol, cyclotomic_poly


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def rational_bound(value):
    mantissa, exponent = value.man_exp()
    if exponent >= 0:
        return fmpq(mantissa * (2 ** int(exponent)))
    return fmpq(mantissa, 2 ** int(-exponent))


class Element:
    __slots__ = ("field", "poly", "key")

    def __init__(self, field, poly):
        self.field = field
        self.poly = poly % field.modulus
        self.key = tuple(self.poly.coeffs())

    def coerce(self, other):
        if isinstance(other, Element):
            require(other.field is self.field, "mixed cyclotomic fields")
            return other
        return self.field(other)

    def __add__(self, other):
        return Element(self.field, self.poly + self.coerce(other).poly)

    __radd__ = __add__

    def __neg__(self):
        return Element(self.field, -self.poly)

    def __sub__(self, other):
        return Element(self.field, self.poly - self.coerce(other).poly)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        return Element(self.field, self.poly * self.coerce(other).poly)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        require(bool(other), "division by zero")
        gcd, inverse, _ = other.poly.xgcd(self.field.modulus)
        require(gcd == 1, "noninvertible field element")
        return Element(self.field, self.poly * inverse)

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, power):
        require(isinstance(power, int) and power >= 0, "invalid exponent")
        result = self.field(1)
        base = self
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def __bool__(self):
        return bool(self.poly)

    def __eq__(self, other):
        other = self.coerce(other)
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Field:
    def __init__(self, order):
        self.order = order
        z = Symbol("z")
        coefficients = list(reversed(Poly(cyclotomic_poly(order, z), z).all_coeffs()))
        self.modulus = fmpq_poly([int(c) for c in coefficients])
        self.powers = []
        power = self(1)
        generator = Element(self, fmpq_poly([0, 1]))
        for _ in range(order):
            self.powers.append(power)
            power = power * generator
        require(power == 1, "cyclotomic generator order identity failed")
        self._balls = {}
        self._cosines = {}
        self._signs = {}
        self._real = set()

    def __call__(self, value):
        if isinstance(value, Element):
            require(value.field is self, "mixed cyclotomic fields")
            return value
        return Element(self, fmpq_poly([fmpq(value)]))

    def cos(self, k):
        return (self.powers[k % self.order] + self.powers[-k % self.order]) / 2

    def conjugate(self, element):
        return sum(
            (c * self.powers[-i % self.order] for i, c in enumerate(element.key)),
            self(0),
        )

    def ball(self, element, bits=128):
        element = self(element)
        key = element.key, bits
        if key in self._balls:
            return self._balls[key]
        if element.key not in self._real:
            require(self.conjugate(element) == element, "ordering a nonreal element")
            self._real.add(element.key)
        with ctx.workprec(bits):
            if bits not in self._cosines:
                self._cosines[bits] = [
                    arb(fmpq(2 * i, self.order)).cos_pi()
                    for i in range(self.modulus.degree())
                ]
            result = sum(
                (arb(c) * self._cosines[bits][i] for i, c in enumerate(element.key)),
                arb(0),
            )
        self._balls[key] = result
        return result

    def sign(self, element):
        element = self(element)
        if not element:
            return 0
        if element.key not in self._signs:
            for bits in (128, 256, 512, 1024, 2048, 4096):
                ball = self.ball(element, bits)
                if ball > 0:
                    self._signs[element.key] = 1
                    break
                if ball < 0:
                    self._signs[element.key] = -1
                    break
            else:
                raise ArithmeticError("real field sign unresolved at 4096 bits")
        return self._signs[element.key]


class Root:
    """A field value, or one branch of x^2+b*x+c with positive discriminant."""

    def __init__(self, field, *, value=None, b=None, c=None, branch=0):
        self.field = field
        self.value = value
        self.b = b
        self.c = c
        self.branch = branch
        self._intervals = {}

    def interval(self, bits=128):
        if bits not in self._intervals:
            with ctx.workprec(bits):
                if self.value is not None:
                    ball = self.field.ball(self.value, bits)
                else:
                    discriminant = self.field.ball(self.b * self.b - 4 * self.c, bits)
                    require(discriminant > 0, "quadratic discriminant enclosure unresolved")
                    ball = (
                        -self.field.ball(self.b, bits) + self.branch * discriminant.sqrt()
                    ) / 2
                self._intervals[bits] = (
                    rational_bound(ball.lower()), rational_bound(ball.upper())
                )
        return self._intervals[bits]

    def is_value(self, value):
        value = self.field(value)
        if self.value is not None:
            return self.value == value
        if value * value + self.b * value + self.c:
            return False
        return self.field.sign(2 * value + self.b) == self.branch

    def equal(self, other):
        if self.value is not None:
            return other.is_value(self.value)
        if other.value is not None:
            return self.is_value(other.value)
        if self.b == other.b:
            return self.c == other.c and self.branch == other.branch
        candidate = (other.c - self.c) / (self.b - other.b)
        return self.is_value(candidate) and other.is_value(candidate)

    def compare(self, other):
        for bits in (128, 256, 512, 1024, 2048, 4096):
            left, right = self.interval(bits), other.interval(bits)
            if left[1] < right[0]:
                return -1
            if right[1] < left[0]:
                return 1
            if bits == 128 and self.equal(other):
                return 0
        raise ArithmeticError("distinct real roots not separated at 4096 bits")

    def compare_value(self, value):
        return self.compare(Root(self.field, value=self.field(value)))

    def vanishes(self, a, b, c):
        a, b, c = (self.field(v) for v in (a, b, c))
        if self.value is not None:
            return not (a * self.value * self.value + b * self.value + c)
        linear = b - a * self.b
        constant = c - a * self.c
        if not linear:
            return not constant
        return self.is_value(-constant / linear)


def real_roots(field, a, b, c):
    """All distinct real roots, with branch 0 for a linear or repeated root."""
    a, b, c = (field(v) for v in (a, b, c))
    if not a:
        require(bool(b) or bool(c), "identically zero critical equation")
        return [] if not b else [Root(field, value=-c / b)]
    b, c = b / a, c / a
    sign = field.sign(b * b - 4 * c)
    if sign < 0:
        return []
    if sign == 0:
        return [Root(field, value=-b / 2)]
    return [Root(field, b=b, c=c, branch=branch) for branch in (-1, 1)]


def root_groups(labeled_roots):
    """Sort by certified real order; merge only after an exact common-root test."""
    ordered = sorted(labeled_roots, key=cmp_to_key(lambda a, b: a[0].compare(b[0])))
    groups = []
    for root, label in ordered:
        if groups and groups[-1][0].compare(root) == 0:
            groups[-1][1].append(label)
        else:
            groups.append((root, [label]))
    return groups
