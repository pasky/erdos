"""Small exact Farkas certificates for finite-dimensional linear inequalities.

A row is ``((a0, ..., a[d-1]), b)`` and means ``sum(a[j]*x[j]) <= b``.
Bounds on variables must be included explicitly as rows. Discovery uses SciPy;
the public checker uses only integers, strings, and ``fractions.Fraction``.

``infeasibility_certificate(rows)`` returns a JSON-serializable certificate or
None. None means that no certificate was found, not a proof of feasibility.
Certificate multipliers are positive rationals, sum to one, annihilate the
coefficient columns, and have a strictly negative weighted right side.
There are at most ``dimension + 1`` nonzero multipliers.
"""
from fractions import Fraction
import json



def _fraction(value):
    if isinstance(value, float):
        raise TypeError("Use exact integers, Fractions, or rational strings.")
    return Fraction(value)


def _rows(rows):
    result = []
    dimension = None
    for coefficients, rhs in rows:
        coefficients = tuple(_fraction(value) for value in coefficients)
        if dimension is None:
            dimension = len(coefficients)
            if dimension == 0:
                raise ValueError("An inequality must have at least one coefficient.")
        if len(coefficients) != dimension:
            raise ValueError("Every inequality must have the same number of coefficients.")
        result.append((coefficients, _fraction(rhs)))
    return result


def serialize_rows(rows):
    """Return rows in the same pair format, with all rationals as strings."""
    return [[[str(value) for value in coefficients], str(rhs)]
            for coefficients, rhs in _rows(rows)]


def verify_infeasibility_certificate(rows, certificate):
    """Verify a certificate exactly; malformed or false certificates return False.

    No floating arithmetic, optimizer, NumPy, or SymPy is used by this checker.
    Row indices refer to the input order, including explicit bound rows.
    """
    try:
        rows = _rows(rows)
        if not rows or not isinstance(certificate, dict):
            return False
        dimension = len(rows[0][0])
        if certificate.get("dimension") != dimension:
            return False
        support = certificate["support"]
        weights = tuple(_fraction(value) for value in certificate["multipliers"])
        if not 1 <= len(support) <= dimension + 1 or len(weights) != len(support):
            return False
        if any(type(index) is not int or not 0 <= index < len(rows) for index in support):
            return False
        if len(set(support)) != len(support):
            return False
        if any(weight <= 0 for weight in weights) or sum(weights) != 1:
            return False
        for column in range(dimension):
            if sum(weight*rows[index][0][column]
                   for index, weight in zip(support, weights)) != 0:
                return False
        rhs = sum(weight*rows[index][1] for index, weight in zip(support, weights))
        return rhs < 0 and rhs == _fraction(certificate["weighted_rhs"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError, OverflowError):
        return False


def _as_sympy(value):
    from sympy import Rational
    return Rational(value.numerator, value.denominator)


def _as_fraction(value):
    return Fraction(int(value.p), int(value.q))


def _reduce_support(matrix, costs, weights):
    """Exact nullspace pivots keep feasibility and never increase the cost."""
    from sympy import Matrix
    dimension = matrix.rows - 1
    active = [index for index, value in enumerate(weights) if value > 0]
    weights = list(weights)
    while len(active) > dimension + 1:
        submatrix = matrix[:, active]
        nullspace = submatrix.nullspace()
        if not nullspace:
            raise ArithmeticError("More independent columns than matrix rows.")
        direction = [_as_fraction(value) for value in nullspace[0]]
        assert any(value > 0 for value in direction)
        assert any(value < 0 for value in direction)
        lower = max(-weights[index]/value
                    for index, value in zip(active, direction) if value > 0)
        upper = min(-weights[index]/value
                    for index, value in zip(active, direction) if value < 0)
        slope = sum(costs[index]*value for index, value in zip(active, direction))
        step = lower if slope >= 0 else upper
        for index, value in zip(active, direction):
            weights[index] += step*value
            assert weights[index] >= 0
        active = [index for index in active if weights[index] > 0]
    assert matrix*Matrix([_as_sympy(value) for value in weights]) == Matrix([0]*dimension + [1])
    return weights


def _exact_weights(normalized_rows, support, guesses):
    """Reconstruct a rational dual on one discovered support, then compress it."""
    from sympy import Matrix
    from sympy.solvers.simplex import InfeasibleLPError, UnboundedLPError, linprog
    dimension = len(normalized_rows[0][0])
    matrix = Matrix([
        [_as_sympy(normalized_rows[index][0][column]) for index in support]
        for column in range(dimension)
    ] + [[1]*len(support)])
    target = Matrix([0]*dimension + [1])
    costs = [normalized_rows[index][1] for index in support]

    def acceptable(weights):
        return (len(weights) == len(support)
                and all(value >= 0 for value in weights)
                and matrix*Matrix([_as_sympy(value) for value in weights]) == target
                and sum(cost*value for cost, value in zip(costs, weights)) < 0)

    candidates = []
    try:
        solution, parameters, free_columns = matrix.gauss_jordan_solve(target, freevar=True)
        if not parameters.rows:
            candidates.append([_as_fraction(value) for value in solution])
        else:
            for denominator in (10**6, 10**12, 10**18):
                substitutions = {
                    parameter: _as_sympy(Fraction(float(guesses[column])).limit_denominator(denominator))
                    for parameter, column in zip(parameters, free_columns)
                }
                candidates.append([_as_fraction(value.subs(substitutions)) for value in solution])
    except (ValueError, ZeroDivisionError):
        pass
    for weights in candidates:
        if acceptable(weights):
            return _reduce_support(matrix, costs, weights)

    # This is unusual with a HiGHS simplex basis, but handles degenerate
    # floating supports and avoids selecting arbitrary free parameters.
    try:
        _, exact = linprog([_as_sympy(cost) for cost in costs],
                           A_eq=matrix, b_eq=target)
        weights = [_as_fraction(value) for value in exact]
        if acceptable(weights):
            return _reduce_support(matrix, costs, weights)
    except (InfeasibleLPError, UnboundedLPError, ValueError, ZeroDivisionError):
        pass
    return None


def _certificate_from_support(rows, scales, support, normalized_weights):
    dimension = len(rows[0][0])
    weights = [(index, weight/scales[index])
               for index, weight in zip(support, normalized_weights) if weight > 0]
    total = sum(value for _, value in weights)
    weights = [(index, value/total) for index, value in weights]
    certificate = {
        "dimension": dimension,
        "support": [index for index, _ in weights],
        "multipliers": [str(value) for _, value in weights],
        "weighted_rhs": str(sum(value*rows[index][1] for index, value in weights)),
    }
    if not verify_infeasibility_certificate(rows, certificate):
        raise ArithmeticError("Reconstructed Farkas certificate failed exact checking.")
    return certificate


def infeasibility_certificate(rows):
    """Discover and exactly certify infeasibility, or return None.

    Positive exact row rescaling keeps the float optimizer bounded. Its answer
    is only a support proposal; all feasibility and negativity claims are
    reconstructed and checked over the rationals before returning.
    """
    from scipy.optimize import linprog
    rows = _rows(rows)
    if not rows:
        return None
    dimension = len(rows[0][0])
    scales = [max(abs(value) for value in (*coefficients, rhs)) or Fraction(1)
              for coefficients, rhs in rows]
    normalized = [(tuple(value/scale for value in coefficients), rhs/scale)
                  for (coefficients, rhs), scale in zip(rows, scales)]
    matrix = [[float(coefficients[column]) for coefficients, _ in normalized]
              for column in range(dimension)] + [[1.0]*len(rows)]
    costs = [float(rhs) for _, rhs in normalized]
    result = linprog(costs, A_eq=matrix, b_eq=[0]*dimension + [1],
                     bounds=(0, None), method="highs-ds")
    if not result.success:
        return None
    seen = set()
    for threshold in (1e-9, 1e-14, 0.0):
        support = tuple(index for index, value in enumerate(result.x) if value > threshold)
        if not support or support in seen:
            continue
        seen.add(support)
        weights = _exact_weights(normalized, support, [result.x[index] for index in support])
        if weights is not None:
            return _certificate_from_support(rows, scales, support, weights)
    # A small exact fallback can recover a support lost by floating rounding.
    if len(rows) <= 32:
        support = tuple(range(len(rows)))
        weights = _exact_weights(normalized, support, list(result.x))
        if weights is not None:
            return _certificate_from_support(rows, scales, support, weights)
    return None


def self_test():
    """Exercise rational gaps, four-row witnesses, degeneracy, and tampering."""
    from sympy import Matrix
    rows = [((-1, 0, 0), 0), ((0, -1, 0), 0), ((0, 0, -1), 0),
            ((1, 1, 1), Fraction(-1, 7))]
    certificate = infeasibility_certificate(rows)
    assert verify_infeasibility_certificate(rows, certificate)
    assert len(certificate["support"]) == 4
    assert certificate["weighted_rhs"] == "-1/28"
    assert verify_infeasibility_certificate(serialize_rows(rows), certificate)
    tampered = {**certificate, "weighted_rhs": "-1/27"}
    assert not verify_infeasibility_certificate(rows, tampered)
    tampered = {**certificate, "multipliers": ["1/3"]*4}
    assert not verify_infeasibility_certificate(rows, tampered)

    feasible = [((-1, 0, 0), 0), ((1, 0, 0), 1),
                ((0, -1, 0), 0), ((0, 1, 0), 1),
                ((0, 0, -1), 0), ((0, 0, 1), 1)]
    assert infeasibility_certificate(feasible) is None
    degenerate = [(coefficients, Fraction(-1)) for coefficients, _ in feasible]
    weights = _exact_weights(_rows(degenerate), tuple(range(6)), [1/6]*6)
    assert weights is not None and sum(value > 0 for value in weights) <= 4
    reduced = _certificate_from_support(_rows(degenerate), [Fraction(1)]*6,
                                        tuple(range(6)), weights)
    assert verify_infeasibility_certificate(degenerate, reduced)
    four_dimensional = [
        (tuple(-int(column == index) for column in range(4)), 0)
        for index in range(4)
    ] + [((1, 1, 1, 1), Fraction(-1, 11))]
    four_dimensional_certificate = infeasibility_certificate(four_dimensional)
    assert verify_infeasibility_certificate(four_dimensional, four_dimensional_certificate)
    assert four_dimensional_certificate["dimension"] == 4
    assert len(four_dimensional_certificate["support"]) == 5
    assert four_dimensional_certificate["weighted_rhs"] == "-1/55"
    scaled = [(tuple(value*Fraction(10**20, 3) for value in coefficients),
               rhs*Fraction(10**20, 3)) for coefficients, rhs in _rows(rows)]
    assert verify_infeasibility_certificate(scaled, infeasibility_certificate(scaled))
    print(json.dumps({"self_test": "passed", "four_row_certificate": certificate,
                      "compressed_six_row_certificate": reduced,
                      "four_dimensional_certificate": four_dimensional_certificate}, indent=2))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        parser.error("Use --self-test, or import the generator and exact checker.")
