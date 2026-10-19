"""Fully numerical off-diagonal pair thresholds, including all finite constants.

The supplied coefficient-gcd certificate must hold for both adjacent
rectangles at every integer m>=m0. Multinomial bounds and elementary
integral estimates give explicit prefactors; no asymptotic O(1) is used.
"""

from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_off_diagonal_pade import growth_parameters, rational
from erdos_699_off_diagonal_pairs import normalized_edge

iv.dps = 80


def interval_min(values):
    return iv.mpf([min(x.a for x in values), min(x.b for x in values)])


def interval_max(values):
    return iv.mpf([max(x.a for x in values), max(x.b for x in values)])


def pair_threshold(source, edge, m0, *, gap=11, maximum_shift=11,
                   separate_terms=False, integral_trim=None,
                   near_limit=False):
    """Return a directed numerical cap for one specified rational pair OR."""
    p, q, ep, eq = edge
    targets = {p: Fraction(ep, 10000), q: Fraction(eq, 10000)}
    seed = source['seed']
    P, Q, a, b = (seed[k] for k in ('P', 'Q', 'a', 'b'))
    delta = a*P-b*Q
    assert delta > 0 and gap > 0 and maximum_shift > 0
    A, B, C = source['directions']
    assert m0 >= 2 and B*m0 >= 2
    ell = Fraction(source['gcd_log_rate'])
    c0, k0, growth = growth_parameters(
        P, Q, a, b, A, B, C, ell, terms=source['gcd_terms'],
        sum_scale=source.get('gcd_sum_rounding_denominator'))
    H, left_block, right_block = A+B+C, A+B, B+C
    entropy = (H*iv.log(H)-A*iv.log(A)-B*iv.log(B)-C*iv.log(C))
    T = a*P
    q_rate = (left_block*iv.log(P)-right_block*iv.log(b)
              - A*iv.log(T)+rational(ell)-c0)
    e_rate = (left_block*iv.log(P)+right_block*iv.log(Q)
              - B*iv.log(T)-(A+C)*iv.log(delta)+rational(ell)-k0)
    log_mq, log_me = q_rate-entropy, e_rate-entropy
    assert log_mq < 0 and log_me < 0
    # Both factorial prefactors are <= F*m*exp(entropy*m).
    F = max(Fraction(B), Fraction((H+1)*B*B, A*C))
    trim = Fraction(2) if integral_trim is None else Fraction(integral_trim)
    # Splitting off base^(m-trim) leaves all exponents nonnegative.
    assert trim >= Fraction(2, B) and trim <= m0
    log_q_prefactor = iv.log(rational(F))-rational(trim)*log_mq
    log_e_prefactor = iv.log(rational(F))-rational(trim)*log_me
    log_first_prefactor = iv.log(gap*T)+log_q_prefactor
    log_second_prefactor = 3*iv.log(delta)-iv.log(T)+log_e_prefactor

    prime_left, prime_right = source['primes']
    assert {prime_left, prime_right} == {p, q}
    rho = interval_min([
        (1-rational(targets[prime_left]))/(left_block*iv.log(P)),
        (1-rational(targets[prime_right]))/(right_block*iv.log(Q)),
    ])
    assert rho*k0 > 1
    proposal = rho*rational(Fraction(999999, 1000000)) if near_limit else (rho+1/k0)/2
    block = Fraction(str(float(proposal.mid))).limit_denominator(10**12)
    tau = rational(block)
    assert 0 < tau < rho and tau*k0 > 1
    first_gain, second_gain = tau*c0, tau*k0-1
    gain = interval_min([first_gain, second_gain])
    assert gain > 0
    log_coefficient = (iv.log(tau)+iv.log(2)+interval_max([
        log_first_prefactor+c0,
        iv.log(2)+log_second_prefactor+k0,
    ]))
    first_log_coefficient = iv.log(2*tau)+log_first_prefactor+c0
    second_log_coefficient = iv.log(4*tau)+log_second_prefactor+k0

    def holds(cap):
        if cap <= 0:
            return False
        x = cap*iv.log(10)
        decay_holds = (first_log_coefficient+iv.log(x)-first_gain*x < 0
                       and second_log_coefficient+iv.log(x)-second_gain*x < 0
                       if separate_terms else
                       log_coefficient+iv.log(x)-gain*x < 0)
        return (tau*x >= m0+1 and x >= iv.log(maximum_shift+1)
                and gain*x > 1 and decay_holds)

    upper = 1
    while not holds(upper):
        upper *= 2
    lower = 0
    while upper-lower > 1:
        middle = (lower+upper)//2
        if holds(middle):
            upper = middle
        else:
            lower = middle
    assert holds(upper)
    x = upper*iv.log(10)
    threshold_bound = (interval_max([
        first_log_coefficient+iv.log(x)-first_gain*x,
        second_log_coefficient+iv.log(x)-second_gain*x,
    ]) if separate_terms else log_coefficient+iv.log(x)-gain*x)
    result = {
        'edge': list(edge), 'seed': seed, 'directions': [A, B, C],
        'gcd_log_rate': str(ell), 'gcd_m0': m0,
        'gap_bound': gap, 'maximum_shift': maximum_shift,
        'block_parameter': str(block), 'factorial_prefactor_F': str(F),
        'left_block': left_block, 'right_block': right_block,
        'threshold_power_of_ten': upper,
        'intervals': {name: iv.nstr(value, 40) for name, value in {
            'first_decay_rate': c0, 'second_decay_rate': k0,
            'log_Q_integrand_maximum': log_mq,
            'log_E_integrand_maximum': log_me,
            'log_Q_prefactor': log_q_prefactor,
            'log_E_prefactor': log_e_prefactor,
            'log_first_prefactor': log_first_prefactor,
            'log_second_prefactor': log_second_prefactor,
            'available_block_per_log_height': rho,
            'first_gain': first_gain, 'second_gain': second_gain,
            'log_coefficient': log_coefficient,
            'threshold_log_upper_bound': threshold_bound,
            'threshold_block_lower_bound': tau*x,
        }.items()},
        'conclusion': 'For every h>=10^K, the two listed cofactor upper bounds cannot both hold.',
    }
    if separate_terms:
        result['threshold_bound_method'] = 'Each of the two integer-bound terms is below one half.'
        result['intervals'].update({
            'first_doubled_log_coefficient': iv.nstr(first_log_coefficient, 40),
            'second_doubled_log_coefficient': iv.nstr(second_log_coefficient, 40),
            'threshold_first_doubled_log_upper_bound': iv.nstr(
                first_log_coefficient+iv.log(x)-first_gain*x, 40),
            'threshold_second_doubled_log_upper_bound': iv.nstr(
                second_log_coefficient+iv.log(x)-second_gain*x, 40),
        })
    if integral_trim is not None:
        result['integral_trim'] = str(trim)
    if near_limit:
        result['block_selection'] = 'Within one part per million of the available integral-block limit.'
    return result


def main():
    directory = Path(__file__).parent
    ramp_path = directory/'erdos_699_index_12_ramp.json'
    gcd_path = directory/'erdos_699_off_diagonal_gcd_numeric.json'
    bootstrap_path = directory/'erdos_699_off_diagonal_gcd_bootstrap.json'
    ramp = json.loads(ramp_path.read_text())
    source_path = directory/ramp['source_file']
    sources = json.loads(source_path.read_text())
    gcd_data = json.loads(gcd_path.read_text())
    bootstrap = json.loads(bootstrap_path.read_text())
    assert len(bootstrap['records']) == len(ramp['source_bindings']) == 20
    by_edge = {normalized_edge(row): row for row in sources['records']}
    gcd_by_edge = {tuple(row['edge']): row for row in gcd_data['records']}
    bootstrap_by_edge = {tuple(row['edge']): row for row in bootstrap['records']}
    rows = []
    for binding in ramp['source_bindings']:
        edge = tuple(binding['edge'])
        source = by_edge[tuple(binding['source_edge'])]
        certificate = gcd_by_edge[edge]
        assert certificate['directions'] == source['directions']
        assert Fraction(certificate['ell_lower']) > Fraction(source['gcd_log_rate'])
        finite = bootstrap_by_edge[edge]
        assert finite['analytic_gcd_certificate'] == certificate
        assert Fraction(finite['requested_log_rate']) == Fraction(source['gcd_log_rate'])
        assert finite['finite_interval_end'] == certificate['m0']-1
        assert finite['finite_interval_start'] <= finite['finite_interval_end']
        assert Fraction(finite['minimum_margin']) > 0
        uniform = pair_threshold(source, edge, certificate['m0'])
        row = pair_threshold(source, edge, finite['finite_interval_start'])
        row['gcd_certificate_edge'] = certificate['edge']
        row['uniform_gcd_m0'] = certificate['m0']
        row['uniform_threshold_power_of_ten'] = uniform['threshold_power_of_ten']
        rows.append(row)
    cap = max(row['threshold_power_of_ten'] for row in rows)
    result = {
        'scope': 'Twenty fully numerical off-diagonal pair thresholds for the index-twelve ramp proof.',
        'index': 12, 'height_variable': 'h=n-11',
        'ramp_file': ramp_path.name,
        'source_file': source_path.name,
        'gcd_file': gcd_path.name,
        'bootstrap_file': bootstrap_path.name,
        'records': rows, 'maximum_pair_threshold_power_of_ten': cap,
        'ramp_algebraic_power_of_ten': 845,
        'complete_row_cap_power_of_ten': max(845, cap+1),
        'uniform_only_complete_row_cap_power_of_ten': max(
            845, 1+max(row['uniform_threshold_power_of_ten'] for row in rows)),
        'conclusion': 'Every bad triple at index twelve has n below the displayed complete row cap.',
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(output),
                      'maximum_pair_threshold_power_of_ten': cap,
                      'complete_row_cap_power_of_ten': result['complete_row_cap_power_of_ten'],
                      'pair_caps': [[row['edge'], row['threshold_power_of_ten']] for row in rows]}, indent=2))


if __name__ == '__main__':
    main()
