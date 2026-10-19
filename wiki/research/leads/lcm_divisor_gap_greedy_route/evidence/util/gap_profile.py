"""Exploratory gap profile of the divisors of L_x = lcm(1, ..., x).

Retained by the lead lcm_divisor_gap_greedy_route as an exploratory
computation, not as evidence for any claim. For each consecutive pair d < b
of divisors of L_x with geometric mean g = sqrt(d b) in [x, sqrt(L_x)] it
computes

    kappa(d, b) = (log x) * log(1 / log(b/d)) / log g,

the largest c for which log(b/d) <= g^(-c / log x) holds at that pair. It
prints, per x: tau(L_x), log L_x, the minimum of kappa over the lower half,
the same minimum restricted to g >= x^2, and the largest log(b/d) in each
tenth of the range of log g / log sqrt(L_x). Usage:

    python3 gap_profile.py 20 30 40 50 60 64
"""
import math
import sys


def primes_upto(x):
    sieve = bytearray([1]) * (x + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(x + 1) if sieve[i]]


def divisors_of_lcm(x):
    divs = [1]
    for p in primes_upto(x):
        e = 1
        while p ** (e + 1) <= x:
            e += 1
        powers = [p ** k for k in range(e + 1)]
        divs = [d * q for d in divs for q in powers]
    divs.sort()
    return divs


def main(xs):
    print("x tau log_L min_kappa min_kappa_g_ge_x2 | max log(b/d) per tenth of log g / log sqrt L")
    for x in xs:
        divs = divisors_of_lcm(x)
        L = divs[-1]
        log_x = math.log(x)
        half = 0.5 * math.log(L)
        best = float("inf")
        best_far = float("inf")
        band = [0.0] * 10
        for d, b in zip(divs, divs[1:]):
            log_d = math.log(d)
            log_b = math.log(b)
            log_g = 0.5 * (log_d + log_b)
            if log_g < log_x or log_g > half:
                continue
            r = log_b - log_d
            kappa = log_x * math.log(1.0 / r) / log_g
            best = min(best, kappa)
            if log_g >= 2 * log_x:
                best_far = min(best_far, kappa)
            k = min(9, int(10 * log_g / half))
            band[k] = max(band[k], r)
        print(f"{x} {len(divs)} {math.log(L):.2f} {best:.3f} {best_far:.3f} |",
              " ".join(f"{v:.2e}" for v in band))


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]])
