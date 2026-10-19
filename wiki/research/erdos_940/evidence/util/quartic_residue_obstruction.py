#!/usr/bin/env python3
"""Exact obstruction to one restricted quartic first-moment upper bound.

Scope.  This checks only the following 32-prescription construction, with
target 15 modulo 16 and the Jacobi-sum contribution bounded above by 2.
It does not obstruct other progressions, other character prescriptions,
valuation-one restrictions modulo p**2, or distinct-value estimates.  In
particular it does not challenge the quartic complement theorem.

A prescription consists of a character psi of (Z/16Z)^* and t in {0,1,2,3}:
chi(ell) = psi(ell mod 16) for odd coefficient primes ell, and chi(2) = i**t.
For a quartic character at a split odd prime, chi(-1) = chi(2)**2 = (-1)**t:
this follows because -4 = (1+i)**4 is a fourth power.  The sign is NOT in
general psi(15); psi prescribes positive odd primes, not the rational -1.

Canonical coefficient types are (E,v), where E = 0,1,2,3 represents dyadic
exponent e = 0,5,6,7, respectively, and v is the odd part modulo 16.  If
Z_v is the total d**(-1/4) mass of odd canonical d in residue v, the type
mass is a_E Z_v, with a_E = 2**(-e/4).  For a multiset of four types, let
k count the odd coefficients and let P be the probability that the sum
of the active odd coefficients is 15 modulo 16.  Each of the k odd
coefficients is active with probability 1/2.  If m_s are type
multiplicities, its relative unordered representation weight is

    w = 16 V P * product_s (a_E Z_v)**m_s / product_s m_s!,

where V = Gamma(5/4)**4.  This is the local factor rho_16 = 16P times the
lattice volume, with the type permutation count 4!/product m_s! and
division by 4!.  The cube [0,1/sqrt(2)]**4 lies in sum x_i**4 <= 1, so
V >= 1/4.  Thus 16V may be replaced by 4 for a rigorous lower bound.

For each prescription g the zero-target harmonic trace has the form
B_g + theta_g, with |theta_g| <= 2.  The proposed upper-bound objective is

    sum_type_multisets w * exp(sum_g lambda_g * (B_g + 2)), lambda_g >= 0.

The script finds 364 type multisets with P > 0 and B_g + 2 >= 0 for all
32 prescriptions.  Their weights cannot decrease in this objective.
Only coefficients supported on odd primes <= 251 are used to lower-bound
their weights.  Every computation and comparison below is exact.

Rounding scheme.  All masses are represented by integer multiples of
1/SCALE.  For a local weight p**(-e/4),

    floor(SCALE * p**(-e/4))
      = isqrt(isqrt(SCALE**4 // p**e)).

Local weights, every residue convolution, and final products of a
dyadic mass with an odd mass are rounded down.  All operations have
nonnegative coefficients, so the resulting type masses are rigorous
lower bounds.  The final sum is accumulated as an exact Fraction.

Run: uv run --no-sync python wiki/research/erdos_940/evidence/util/quartic_residue_obstruction.py
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial, isqrt


SCALE = 10**12
PRIME_CUTOFF = 251
UNITS = tuple(range(1, 16, 2))
DYADIC_EXPONENTS = (0, 5, 6, 7)
TYPES = tuple((exponent_class, residue)
              for exponent_class in range(4) for residue in UNITS)

# Every odd residue is uniquely (-1)**a * 3**b modulo 16,
# with a modulo 2 and b modulo 4.  Characters have value i**(2*l*a+k*b).
UNIT_LOG = {
    ((-1)**a * pow(3, b, 16)) % 16: (a, b)
    for a in range(2) for b in range(4)
}
assert set(UNIT_LOG) == set(UNITS)

PRESCRIPTIONS = tuple((k, l, t)
                      for k in range(4) for l in range(2) for t in range(4))
CHARACTER_DIGITS = tuple(
    tuple((t * exponent_class + k * UNIT_LOG[residue][1]
           + 2 * l * UNIT_LOG[residue][0]) % 4
          for exponent_class, residue in TYPES)
    for k, l, t in PRESCRIPTIONS
)

REAL = (1, 0, -1, 0)
IMAGINARY = (0, 1, 0, -1)


def integer_trace(digits, epsilon):
    """Compute B exactly for z_j=i**digits[j] and epsilon=chi(-1).

    B = D**2 * (1 + epsilon*(|sum z_j|**2 - 4))
        + D * sum_{j<k} z_j**2*z_k**2,  D=product z_j.

    The second symmetric sum is (q*q-4)/2 for q=sum z_j**2.
    If D is imaginary, this symmetric sum is zero.  Therefore taking
    the real part of D in the integer formula loses nothing.
    """
    total_digit = sum(digits)
    norm = sum(REAL[d] for d in digits)**2
    norm += sum(IMAGINARY[d] for d in digits)**2
    q = sum((-1)**d for d in digits)
    symmetric_sum = (q*q - 4) // 2
    assert total_digit % 2 == 0 or symmetric_sum == 0
    return ((-1)**total_digit * (1 + epsilon * (norm - 4))
            + REAL[total_digit % 4] * symmetric_sum)


def find_immutable_multisets():
    result = []
    # Exactly binomial(35,4) = 52360 multisets; no unbounded search.
    visited = 0
    for indices in combinations_with_replacement(range(len(TYPES)), 4):
        visited += 1
        odd_residues = [TYPES[index][1] for index in indices
                        if TYPES[index][0] == 0]
        k = len(odd_residues)
        successful_subsets = sum(
            sum(odd_residues[j] for j in range(k) if mask >> j & 1) % 16 == 15
            for mask in range(1 << k)
        )
        if successful_subsets == 0:
            continue
        if all(integer_trace(tuple(digits[index] for index in indices),
                             (-1)**t) + 2 >= 0
               for digits, (_, _, t) in zip(CHARACTER_DIGITS, PRESCRIPTIONS)):
            result.append((indices, successful_subsets, k))
    assert visited == 52360
    assert len(result) == 364
    return result


def rounded_local_mass(prime, exponent):
    """Return floor(SCALE * prime**(-exponent/4)), exactly."""
    result = isqrt(isqrt(SCALE**4 // prime**exponent))
    assert result**4 * prime**exponent <= SCALE**4
    assert (result + 1)**4 * prime**exponent > SCALE**4
    return result


def rounded_type_masses():
    primes = tuple(p for p in range(3, PRIME_CUTOFF + 1, 2)
                   if all(p % q for q in range(2, isqrt(p) + 1)))
    assert len(primes) == 53 and primes[-1] == PRIME_CUTOFF

    odd_masses = {residue: 0 for residue in UNITS}
    odd_masses[1] = SCALE
    for prime in primes:
        local = [(1, SCALE)] + [
            (pow(prime, exponent, 16), rounded_local_mass(prime, exponent))
            for exponent in (5, 6, 7)
        ]
        convolution = {residue: 0 for residue in UNITS}
        for residue, mass in odd_masses.items():
            for local_residue, local_mass in local:
                convolution[residue * local_residue % 16] += mass * local_mass
        odd_masses = {residue: mass // SCALE
                      for residue, mass in convolution.items()}

    dyadic_masses = (SCALE,) + tuple(rounded_local_mass(2, exponent)
                                    for exponent in DYADIC_EXPONENTS[1:])
    return tuple(dyadic_masses[exponent_class] * odd_masses[residue] // SCALE
                 for exponent_class, residue in TYPES)


def main():
    immutable = find_immutable_multisets()
    type_masses = rounded_type_masses()
    lower_bound = Fraction(0)
    for indices, successful_subsets, k in immutable:
        product = 1
        for index in indices:
            product *= type_masses[index]
        permutation_denominator = 1
        for multiplicity in Counter(indices).values():
            permutation_denominator *= factorial(multiplicity)
        lower_bound += Fraction(
            4 * successful_subsets * product,
            (1 << k) * permutation_denominator * SCALE**4,
        )

    expected = Fraction(
        67826836205251839956626671887649519872177425279,
        62500000000000000000000000000000000000000000000,
    )
    assert lower_bound == expected
    assert lower_bound > Fraction(27, 25)
    print(f"Immutable type multisets: {len(immutable)}")
    print(f"Exact finite lower bound: {lower_bound}")
    print("Verified: lower bound > 27/25 = 1.08.")
    print("Scope: only the specified 32-prescription, target-15 safe objective.")


if __name__ == "__main__":
    main()
