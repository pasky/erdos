"""Exact 2-adic divisibility for the multipoint seed (10,9,8).

The proof is the integer beta expansion below. Its coefficient is a product
of two multinomial coefficients. The finite examples compare it with direct
integration and illustrate the two distinct powers of 2 usable in a cross
product. They do not certify a whole-index exclusion.
"""
from fractions import Fraction
from functools import reduce
from math import comb, factorial, gcd
from pathlib import Path
import json


def integer_beta(a, b, c, d, u, v, w, z):
    """N times integral t^a(1-t)^d(u+vt)^b(w+zt)^c dt on [0,1]."""
    assert min(a, b, c, d) >= 0
    length = a+b+c+d
    total = 0
    for r in range(b+1):
        for s in range(c+1):
            first = comb(a+r+s, a)*comb(r+s, r)
            second = comb(length+1, b-r)*comb(length+1-b+r, c-s)
            total += first*second*u**(b-r)*v**r*w**(c-s)*z**s
    return total


def raw_row(m, k, directions=(2, 2, 2, 1)):
    A0, A1, A2, D = directions
    a, b, c, d = A0*m+k, A1*m+k, A2*m+k, D*m-1-k
    assert min(a, b, c, d) >= 0
    sign = (-1)**d
    return [
        sign*2**(a+c+d+1)*integer_beta(a, b, c, d, -1, 10, -1, 5),
        sign*integer_beta(b, a, c, d, 1, 9, -1, 9),
        sign*2**a*integer_beta(c, a, b, d, 1, 4, 1, 8),
    ]


def direct_row(m, k, directions):
    """Independent rational integration of the original four-root polynomial."""
    A0, A1, A2, D = directions
    powers = [A0*m+k, A1*m+k, A2*m+k, D*m-1-k]
    coefficients = [1]
    for root, power in zip((0, 1, 2, 10), powers):
        for _ in range(power):
            next_coefficients = [0]*(len(coefficients)+1)
            for j, coefficient in enumerate(coefficients):
                next_coefficients[j] -= root*coefficient
                next_coefficients[j+1] += coefficient
            coefficients = next_coefficients
    length = sum(powers)
    normalizer = Fraction(factorial(length+1),
                          factorial(powers[0])*factorial(powers[1])
                          *factorial(powers[2])*factorial(powers[3]))
    assert normalizer.denominator == 1
    result = []
    for i, (root, base) in enumerate(zip((0, 1, 2), (5, 9, 8))):
        integral = sum((Fraction(coefficient*(10**(j+1)-root**(j+1)), j+1)
                        for j, coefficient in enumerate(coefficients)), Fraction(0))
        value = normalizer*integral/base**(powers[i]+powers[3]+1)
        assert value.denominator == 1
        result.append(value.numerator)
    return result


def valuation_two(value):
    if value == 0:
        return None
    value = abs(value)
    return (value & -value).bit_length()-1


def odd_primitive(row):
    content = reduce(gcd, row)
    assert content > 0
    odd_content = content >> valuation_two(content)
    return [value//odd_content for value in row]


def cross(left, right):
    return [left[1]*right[2]-left[2]*right[1],
            left[2]*right[0]-left[0]*right[2],
            left[0]*right[1]-left[1]*right[0]]


def divisible(value, power):
    assert power >= 0
    return value % 2**power == 0


def report():
    records = []
    choices = ((2, 2, 2, 1), (1, 1, 1, 1), (3, 2, 1, 2), (1, 3, 4, 2))
    for directions in choices:
        A0, A1, A2, D = directions
        for m in (2, 3, 4, 6):
            rows = [raw_row(m, k, directions) for k in (0, 1)]
            if m <= 3:
                assert rows == [direct_row(m, k, directions) for k in (0, 1)]
            a0, E = A0*m, (A0+A2+D)*m
            for k, row in enumerate(rows):
                assert divisible(row[0], E+k)
                assert divisible(row[2], a0+k)
            primitive_rows = [odd_primitive(row) for row in rows]
            minors = cross(*primitive_rows)
            lower_bounds = [a0, a0+E+1, E]
            assert all(divisible(value, bound) for value, bound in zip(minors, lower_bounds))
            divided = [value//2**a0 for value in minors]
            assert divisible(divided[2], (A2+D)*m)
            records.append({
                'directions': list(directions), 'm': m,
                'odd_normalized_row_valuations': [[valuation_two(x) for x in row]
                                                for row in primitive_rows],
                'cross_valuations': [valuation_two(x) for x in minors],
                'proved_cross_lower_bounds': lower_bounds,
                'chosen_common_power_of_two': a0,
                'third_coefficient_remaining_power_of_two': (A2+D)*m,
                'after_chosen_division_valuations': [valuation_two(x) for x in divided],
            })
    return {
        'scope': 'Exact divisibility identities for explicitly odd-normalized rows; no full primitive-gcd or whole-index assertion.',
        'seed': [10, 9, 8], 'prime_power_bases': [5, 9, 8],
        'records': records,
    }


if __name__ == '__main__':
    result = report()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'exact_examples': len(result['records']),
                      'direct_integration_examples': 8,
                      'row_and_minor_divisibilities': 'verified'}))
