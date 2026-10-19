"""Test the ``tools.core.problem_claims`` module."""

from __future__ import annotations

import pathlib

import pytest

import tools.core.problem_claims
from tools.core.problem_claims import derive, lint_problem_claims, write_derived

from .._helpers import write_page

__all__ = [
    'test_a_problem_with_consistent_claims_passes',
    'test_each_schema_defect_is_one_finding',
    'test_the_standing_is_derived_from_the_full_claims',
    'test_named_parts_settle_the_problem_together',
    'test_one_sided_results_settle_only_as_a_pair',
    'test_accepted_claims_differing_on_one_part_disagree',
    'test_parts_and_settles_are_checked',
    'test_a_provisional_standing_without_claims_is_debt_until_settled',
    'test_a_claim_page_without_authors_is_debt_until_settled',
    'test_an_empty_authors_list_records_an_unknown_name',
    'test_a_published_date_gives_only_what_is_known',
    'test_a_claim_not_yet_public_has_no_published_date',
    'test_a_null_submitted_records_an_unknown_date',
    'test_a_claim_id_names_one_claim_on_the_site',
    'test_same_day_pages_of_one_claimant_take_roman_suffixes',
    'test_a_pending_page_keeps_a_temporary_suffix_beside_a_public_page',
    'test_a_link_date_gives_only_what_is_known',
    'test_an_accepted_claim_rests_only_on_accepted_pages',
    'test_a_dependence_on_a_library_result_page_is_noted_with_its_read_status',
    'test_write_derived_sets_the_two_standing_lines_only',
    'test_write_derived_leaves_a_body_line_alone',
    'test_a_selection_scopes_the_check_and_the_write_to_named_folders',
    'test_only_index_pages_with_a_status_are_problems',
]

_AUTHORS = ('authors:', '- A. Claimant', '- B. Coauthor')
_CLAIM = (
    'title: A claimed proof',
    'desc: A synthetic claim.',
    *_AUTHORS,
    'status: accepted',
    'claim: proved',
    'scope: full',
    'evidence:',
    '- refereed',
    'published: 2026-01-02',
    'submitted: 2026-01-02',
    'links:',
    '- url: https://example.org/paper',
    '  kind: paper',
    '  date: 2026-01-02',
)
_BODY = (
    '***',
    '',
    'The claimant proves the statement; reviewed by the project on 2026-02-03.',
    '',
    '**Depends on.** Nothing beyond the cited paper.',
)


@pytest.fixture(autouse=True)
def open_tag_vocabulary(monkeypatch: pytest.MonkeyPatch) -> None:
    """Run the shared schema tests with the tag vocabulary open.

    The fixtures below carry synthetic tags; a
    repository that closes the vocabulary to its own list (PROBLEM_TAGS)
    covers that in a test of its own.
    """
    monkeypatch.setattr(tools.core.problem_claims, 'PROBLEM_TAGS', None)


def _problem(
    root: pathlib.Path,
    folder: str = 'alpha/p1',
    status: str = 'solved',
    claim: str = 'proved',
    tags: str = '[alpha, beta]',
    extra: tuple[str, ...] = (),
) -> pathlib.Path:
    """Write a problem index page under the fixture's problems tree."""
    return write_page(
        root / 'wiki/problems' / folder / '_index.md',
        '---',
        f'name: problems/{folder}',
        'title: A synthetic problem',
        'desc: A synthetic question.',
        f'status: {status}',
        f'claim: {claim}',
        f'tags: {tags}',
        *extra,
        '---',
        '',
        '***',
        '',
        '**Statement.** A synthetic question.',
    )


def _claim(
    root: pathlib.Path,
    name: str = '2026_01_02_claimant.md',
    folder: str = 'alpha/p1',
    *,
    frontmatter: tuple[str, ...] = _CLAIM,
    body: tuple[str, ...] = _BODY,
) -> pathlib.Path:
    """Write a claim page beside the fixture problem."""
    return write_page(
        root / 'wiki/problems' / folder / 'claims' / name,
        '---',
        *frontmatter,
        '---',
        '',
        *body,
    )


def _without(lines: tuple[str, ...], *prefixes: str) -> tuple[str, ...]:
    """Return ``lines`` without the lines starting with any of ``prefixes``."""
    return tuple(line for line in lines if not line.startswith(prefixes))


def _replace(lines: tuple[str, ...], prefix: str, *new: str) -> tuple[str, ...]:
    """Return ``lines`` with the line starting with ``prefix`` replaced by ``new``."""
    result = []
    for line in lines:
        if line.startswith(prefix):
            result.extend(new)
        else:
            result.append(line)
    return tuple(result)


def test_a_problem_with_consistent_claims_passes(tmp_path: pathlib.Path) -> None:
    """An accepted full claim with authors, evidence and links derives the recorded standing."""
    _problem(tmp_path)
    _claim(tmp_path)
    write_page(
        tmp_path / 'wiki/problems/alpha/_index.md', '---', 'desc: An area.', '---'
    )
    findings, notes = lint_problem_claims(tmp_path)
    assert findings == []
    assert notes[0] == (
        '1 problem(s); 1 claim page(s); 0 provisional standing(s) without a claim'
        ' page; 0 claim page(s) without authors'
    )


@pytest.mark.parametrize(
    ('frontmatter', 'body', 'name', 'message'),
    [
        (
            _replace(
                _without(_CLAIM, *_AUTHORS[1:]), 'authors:', 'authors: A. Claimant'
            ),
            _BODY,
            None,
            'authors must be a list of distinct nonempty strings',
        ),
        (
            _replace(_CLAIM, '- B. Coauthor', '- A. Claimant'),
            _BODY,
            None,
            'authors must be a list of distinct nonempty strings',
        ),
        (
            _replace(
                _without(_CLAIM, *_AUTHORS), 'status:', 'status: accepted', *_AUTHORS
            ),
            _BODY,
            None,
            'authors must come after desc and before status',
        ),
        (
            _replace(_CLAIM, 'status:', 'status: believed'),
            _BODY,
            None,
            "status 'believed' is not one of",
        ),
        (_without(_CLAIM, 'claim:'), _BODY, None, 'missing claim (one of'),
        (
            _replace(_CLAIM, 'claim:', 'claim: [proved]'),
            _BODY,
            None,
            "claim ['proved'] is not one of",
        ),
        (
            _replace(_CLAIM, 'claim:', 'claim: decidable'),
            _BODY,
            None,
            'scope must be partial',
        ),
        (
            _replace(_CLAIM, 'claim:', 'claim: not_provable'),
            _BODY,
            None,
            'one side of an independence result',
        ),
        (
            _replace(
                _replace(_CLAIM, 'claim:', 'claim: not_disprovable'),
                'scope:',
                'scope: conditional',
            ),
            _BODY,
            None,
            'one side of an independence result',
        ),
        (
            _replace(_CLAIM, 'scope:', 'scope: partial'),
            _BODY,
            None,
            'carries a **Covers.** paragraph',
        ),
        (
            (*_CLAIM[:9], '- formalized', '- refereed', *_CLAIM[10:]),
            _BODY,
            None,
            'in the order reviewed, refereed, formalized',
        ),
        (_without(_CLAIM, 'evidence:', '- refereed'), _BODY, None, 'missing evidence'),
        (_without(_CLAIM, 'published:'), _BODY, None, 'missing published'),
        (
            _replace(_CLAIM, 'published:', 'published: soon'),
            _BODY,
            None,
            'published must be a calendar date YYYY-MM-DD, or YYYY-MM or YYYY',
        ),
        (
            (*_without(_CLAIM, 'published:'), 'published: 2026-01-02'),
            _BODY,
            None,
            'published must come just before submitted',
        ),
        (
            _replace(_CLAIM, 'published:', 'published: 2026-01-03'),
            _BODY,
            None,
            "published 2026-01-03 does not match the page name's date 2026-01-02",
        ),
        (
            _replace(_CLAIM, 'published:', 'published: 2026-01'),
            _BODY,
            None,
            "published 2026-01 does not match the page name's date 2026-01-02",
        ),
        (
            _replace(
                _without(_CLAIM, '- url:', '  kind:', '  date:'), 'links:', 'links: []'
            ),
            _BODY,
            None,
            'links may be [] only while published is null',
        ),
        (_without(_CLAIM, 'submitted:'), _BODY, None, 'missing submitted'),
        (
            _replace(_CLAIM, 'submitted:', 'submitted: soon'),
            _BODY,
            None,
            'submitted must be a calendar date',
        ),
        (
            _replace(_CLAIM, 'submitted:', 'submitted: 2026-01-02', 'claim_id: null'),
            _BODY,
            None,
            'claim_id must be a nonempty string',
        ),
        (
            _replace(_CLAIM, 'submitted:', 'submitted: 2026-01-02', 'claim_id: 12345'),
            _BODY,
            None,
            'claim_id must be a nonempty string',
        ),
        (
            (*_CLAIM, 'claim_id: 01ABC'),
            _BODY,
            None,
            'claim_id must come just after submitted',
        ),
        (
            _replace(_CLAIM, 'status:', 'status: claimed'),
            _BODY,
            None,
            'a claimed page lists no evidence',
        ),
        (
            _replace(
                _CLAIM, '- url:', '- kind: paper', '  url: https://example.org/paper'
            ),
            _BODY,
            None,
            'must name url first',
        ),
        (
            _replace(_CLAIM, '  kind:', '  kind: blog'),
            _BODY,
            None,
            'kind must be one of',
        ),
        (
            _replace(_CLAIM, '  date:', '  date: 2026-01-02T00:00:00Z'),
            _BODY,
            None,
            'date must be a calendar date',
        ),
        (
            _replace(_CLAIM, '  date:', '  date: 1936-13'),
            _BODY,
            None,
            'date must be a calendar date',
        ),
        (
            _CLAIM,
            _replace(
                _BODY,
                '**Depends on.**',
                '**Depends on.** [[research/missing|a missing page]].',
            ),
            None,
            'is not a wiki page',
        ),
        (
            _CLAIM,
            _replace(
                _BODY,
                '**Depends on.**',
                '**Depends on.** [[problems/alpha/p1|the problem folder]].',
            ),
            None,
            'is not a wiki page',
        ),
        (
            _CLAIM,
            _replace(
                _BODY,
                '**Depends on.**',
                '**Depends on.** [[../library/first/missing|a missing result page]].',
            ),
            None,
            'is not a wiki page or a library result page',
        ),
        (_CLAIM, _BODY, 'claimant.md', 'claim page name must be'),
        (_CLAIM, _BODY, '2026_13_02_claimant.md', 'is not a calendar date'),
        (
            (*_CLAIM, '- url: https://example.org/paper', '  kind: discussion'),
            _BODY,
            None,
            'links list the same url twice',
        ),
    ],
)
def test_each_schema_defect_is_one_finding(
    tmp_path: pathlib.Path,
    frontmatter: tuple[str, ...],
    body: tuple[str, ...],
    name: str | None,
    message: str,
) -> None:
    """Every defect of a claim page is one finding naming the page."""
    _problem(tmp_path)
    page = _claim(
        tmp_path, name or '2026_01_02_claimant.md', frontmatter=frontmatter, body=body
    )
    findings, _ = lint_problem_claims(tmp_path)
    prefix = f'{page.relative_to(tmp_path).as_posix()}: '
    own = [finding for finding in findings if finding.startswith(prefix)]
    assert len(own) == 1, findings
    assert message in own[0]


@pytest.mark.parametrize(
    ('claims', 'expected', 'disagreement'),
    [
        ([('accepted', 'proved', 'full')], ('solved', 'proved'), None),
        (
            [('accepted', 'proved', 'full'), ('accepted', 'disproved', 'full')],
            ('solved', 'disproved'),
            'disagree',
        ),
        (
            [('claimed', 'proved', 'full'), ('rejected', 'disproved', 'full')],
            ('claimed', 'proved'),
            None,
        ),
        (
            [('claimed', 'proved', 'full'), ('claimed', 'disproved', 'full')],
            ('claimed', 'contested'),
            None,
        ),
        (
            [('accepted', 'decidable', 'partial'), ('withdrawn', 'proved', 'full')],
            ('open', 'none'),
            None,
        ),
        ([('claimed', 'proved', 'conditional')], ('open', 'none'), None),
    ],
)
def test_the_standing_is_derived_from_the_full_claims(
    tmp_path: pathlib.Path,
    claims: list[tuple[str, str, str]],
    expected: tuple[str, str],
    disagreement: str | None,
) -> None:
    """Accepted full claims settle, pending full claims claim, the rest derive nothing."""
    pages = [
        {'status': status, 'claim': claim, 'scope': scope}
        for status, claim, scope in claims
    ]
    derived, reason = derive(pages)
    assert derived == expected
    assert (reason is None) == (disagreement is None)
    # the recorded standing must match the derivation
    _problem(tmp_path, status='open', claim='none')
    for index, (status, claim, scope) in enumerate(claims):
        frontmatter = _replace(_CLAIM, 'status:', f'status: {status}')
        frontmatter = _replace(frontmatter, 'claim:', f'claim: {claim}')
        frontmatter = _replace(frontmatter, 'scope:', f'scope: {scope}')
        frontmatter = _replace(
            frontmatter, 'published:', f'published: 2026-01-0{index + 1}'
        )
        body = (
            _BODY
            if scope != 'partial'
            else (*_BODY, '', '**Covers.** The finite check.')
        )
        _claim(
            tmp_path,
            f'2026_01_0{index + 1}_claimant_{index}.md',
            frontmatter=frontmatter,
            body=body,
        )
    findings, _ = lint_problem_claims(tmp_path)
    mismatches = [finding for finding in findings if 'but the claims derive' in finding]
    assert len(mismatches) == (2 if expected != ('open', 'none') else 0), findings


def _partial(status: str, claim: str, *settles: str) -> dict[str, object]:
    """A partial claim's metadata as the derivation reads it."""
    return {
        'status': status,
        'claim': claim,
        'scope': 'partial',
        'settles': list(settles),
    }


@pytest.mark.parametrize(
    ('claims', 'expected'),
    [
        # every part settled by accepted claims that agree
        (
            [
                _partial('accepted', 'proved', 'lower'),
                _partial('accepted', 'proved', 'upper'),
            ],
            ('solved', 'proved'),
        ),
        # the settling claims differ, so the claim is answered
        (
            [
                _partial('accepted', 'proved', 'lower'),
                _partial('accepted', 'disproved', 'upper'),
            ],
            ('solved', 'answered'),
        ),
        # one part still rests on a pending claim
        (
            [
                _partial('accepted', 'proved', 'lower'),
                _partial('claimed', 'proved', 'upper'),
            ],
            ('claimed', 'proved'),
        ),
        # a part nobody names leaves the problem open
        ([_partial('accepted', 'proved', 'lower')], ('open', 'none')),
        # a partial claim naming no part derives nothing
        (
            [
                _partial('accepted', 'proved', 'lower'),
                {'status': 'accepted', 'claim': 'proved', 'scope': 'partial'},
            ],
            ('open', 'none'),
        ),
        # a reduction to a finite check settles no part
        (
            [
                _partial('accepted', 'proved', 'lower'),
                _partial('accepted', 'decidable', 'upper'),
            ],
            ('open', 'none'),
        ),
        # pending claims that differ on one part contest it
        (
            [
                _partial('accepted', 'proved', 'lower'),
                _partial('claimed', 'proved', 'upper'),
                _partial('claimed', 'disproved', 'upper'),
            ],
            ('claimed', 'contested'),
        ),
        # an accepted full claim settles regardless of the parts
        (
            [
                {'status': 'accepted', 'claim': 'disproved', 'scope': 'full'},
                _partial('claimed', 'proved', 'lower', 'upper'),
            ],
            ('solved', 'disproved'),
        ),
        # a claim without a claim value, a list claim, an empty claim and a
        # label that is not a string derive nothing, and do not stop the check
        (
            [
                {'status': 'accepted', 'scope': 'full'},
                {'status': 'accepted', 'claim': ['proved'], 'scope': 'full'},
                {'status': 'accepted', 'claim': '', 'scope': 'full'},
                _partial('accepted', 'proved', 'lower'),
                {
                    'status': 'accepted',
                    'claim': 'proved',
                    'scope': 'partial',
                    'settles': [{'upper': 'proved'}],
                },
            ],
            ('open', 'none'),
        ),
    ],
    ids=[
        'all_accepted',
        'values_differ',
        'one_pending',
        'one_unsettled',
        'no_settles',
        'decidable_settles_nothing',
        'pending_part_contested',
        'full_claim_wins',
        'malformed_claims_derive_nothing',
    ],
)
def test_named_parts_settle_the_problem_together(
    claims: list[dict[str, object]], expected: tuple[str, str]
) -> None:
    """Partial claims that name the problem's parts settle it together."""
    assert derive(claims, ('lower', 'upper')) == (expected, None)


@pytest.mark.parametrize(
    ('claims', 'parts', 'expected'),
    [
        # one side alone leaves the problem open
        ([_partial('accepted', 'not_provable')], (), ('open', 'none')),
        # one of each, accepted, settles it as independent
        (
            [
                _partial('accepted', 'not_provable'),
                _partial('accepted', 'not_disprovable'),
            ],
            (),
            ('solved', 'independent'),
        ),
        # with one of them pending, the problem is claimed
        (
            [
                _partial('accepted', 'not_provable'),
                _partial('claimed', 'not_disprovable'),
            ],
            (),
            ('claimed', 'independent'),
        ),
        # a part both sides name is settled as independent
        (
            [
                _partial('accepted', 'not_provable', 'lower'),
                _partial('accepted', 'not_disprovable', 'lower'),
                _partial('accepted', 'proved', 'upper'),
            ],
            ('lower', 'upper'),
            ('solved', 'answered'),
        ),
        # a part with one side alone stays open, and so does the problem
        (
            [
                _partial('accepted', 'not_provable', 'lower'),
                _partial('accepted', 'not_disprovable', 'lower'),
                _partial('accepted', 'not_disprovable', 'upper'),
            ],
            ('lower', 'upper'),
            ('open', 'none'),
        ),
        # a one-sided result beside an independence result on the same part agrees with it
        (
            [
                _partial('accepted', 'independent', 'lower'),
                _partial('accepted', 'not_provable', 'lower'),
                _partial('accepted', 'proved', 'upper'),
            ],
            ('lower', 'upper'),
            ('solved', 'answered'),
        ),
    ],
    ids=[
        'one_side',
        'both_sides',
        'one_side_pending',
        'part_independent',
        'part_one_side',
        'one_side_beside_independent',
    ],
)
def test_one_sided_results_settle_only_as_a_pair(
    claims: list[dict[str, object]], parts: tuple[str, ...], expected: tuple[str, str]
) -> None:
    """Not provable and not disprovable each leave a question open; together they settle it."""
    assert derive(claims, parts) == (expected, None)


def test_accepted_claims_differing_on_one_part_disagree() -> None:
    """Two accepted claims answering one part differently are a named disagreement."""
    claims = [
        _partial('accepted', 'proved', 'lower'),
        _partial('accepted', 'disproved', 'lower'),
        _partial('accepted', 'proved', 'upper'),
    ]
    assert derive(claims, ('lower', 'upper')) == (
        ('solved', 'answered'),
        "accepted claims settling part 'lower' disagree: disproved, proved",
    )


def test_parts_and_settles_are_checked(tmp_path: pathlib.Path) -> None:
    """Settles belongs to partial claims and names only the problem's parts; parts are short labels."""
    covers = ('**Covers.** One side of the question.', '', *_BODY)
    _problem(
        tmp_path,
        'alpha/p1',
        status='solved',
        claim='proved',
        extra=('parts: [lower, upper]',),
    )
    _claim(
        tmp_path,
        '2026_01_02_claimant.md',
        'alpha/p1',
        frontmatter=_replace(_CLAIM, 'scope:', 'scope: partial', 'settles: [lower]'),
        body=covers,
    )
    _claim(
        tmp_path,
        '2026_01_03_other.md',
        'alpha/p1',
        frontmatter=_replace(
            _replace(_CLAIM, 'published:', 'published: 2026-01-03'),
            'scope:',
            'scope: partial',
            'settles: [upper, middle]',
        ),
        body=covers,
    )
    _claim(
        tmp_path,
        '2026_01_04_third.md',
        'alpha/p1',
        frontmatter=_replace(
            _replace(_CLAIM, 'published:', 'published: 2026-01-04'),
            'scope:',
            'scope: full',
            'settles: [upper]',
        ),
    )
    _claim(
        tmp_path,
        '2026_01_05_fourth.md',
        'alpha/p1',
        frontmatter=_replace(
            _replace(
                _replace(_CLAIM, 'published:', 'published: 2026-01-05'),
                'scope:',
                'scope: partial',
                'settles: [upper]',
            ),
            'claim:',
            'claim: decidable',
        ),
        body=covers,
    )
    _problem(
        tmp_path,
        'alpha/p2',
        status='open',
        claim='none',
        extra=('parts: [Lower, lower]',),
    )
    _claim(
        tmp_path,
        '2026_01_02_claimant.md',
        'alpha/p2',
        frontmatter=_replace(_CLAIM, 'scope:', 'scope: partial', 'settles: [lower]'),
        body=covers,
    )
    findings, _ = lint_problem_claims(tmp_path)
    assert findings == [
        "wiki/problems/alpha/p1/claims/2026_01_03_other.md: settles names labels outside the problem's parts: middle",
        'wiki/problems/alpha/p1/claims/2026_01_04_third.md: settles is listed only on a partial claim',
        "wiki/problems/alpha/p1/claims/2026_01_05_fourth.md: claim 'decidable' is a reduction to a finite check; it settles no part",
        'wiki/problems/alpha/p2/_index.md: parts must be a nonempty list of distinct short labels (lowercase letters, digits, underscores)',
        'wiki/problems/alpha/p2/claims/2026_01_02_claimant.md: settles needs the problem page to list its parts',
    ]


def test_a_provisional_standing_without_claims_is_debt_until_settled(
    tmp_path: pathlib.Path,
) -> None:
    """A claimless problem keeps its provisional values, counted as debt; settled mode fails it."""
    _problem(tmp_path, 'alpha/p1', status='solved', claim='proved')
    _problem(tmp_path, 'alpha/p2', status='open', claim='none')
    findings, notes = lint_problem_claims(tmp_path)
    assert findings == []
    assert '1 provisional standing(s) without a claim page' in notes[0]
    findings, _ = lint_problem_claims(tmp_path, settled=True)
    assert findings == [
        "wiki/problems/alpha/p1/_index.md: provisional 'solved'/'proved' with no claim page"
    ]


# an outside claimant's page, and the project's own, which lists the project
@pytest.mark.parametrize('name', ['2026_01_02_claimant.md', '2026_01_02_corpus.md'])
def test_a_claim_page_without_authors_is_debt_until_settled(
    tmp_path: pathlib.Path, name: str
) -> None:
    """A claim page without authors is counted as debt; settled mode fails it."""
    _problem(tmp_path)
    _claim(tmp_path, name, frontmatter=_without(_CLAIM, *_AUTHORS))
    findings, notes = lint_problem_claims(tmp_path)
    assert findings == []
    assert notes[0].endswith('; 1 claim page(s) without authors')
    findings, _ = lint_problem_claims(tmp_path, settled=True)
    assert findings == [
        f'wiki/problems/alpha/p1/claims/{name}: missing authors'
        " (a list of the publication's authors as printed)"
    ]


def test_an_empty_authors_list_records_an_unknown_name(tmp_path: pathlib.Path) -> None:
    """A work whose author's real name is not known lists none; it is no debt even when settled."""
    _problem(tmp_path)
    _claim(
        tmp_path,
        frontmatter=_replace(
            _without(_CLAIM, *_AUTHORS[1:]), 'authors:', 'authors: []'
        ),
    )
    findings, notes = lint_problem_claims(tmp_path, settled=True)
    assert findings == []
    assert notes[0].endswith('; 0 claim page(s) without authors')


@pytest.mark.parametrize(
    ('name', 'date'),
    [
        ('1936_04_17_claimant.md', '1936-04-17'),
        ('1936_04_01_claimant.md', '1936-04'),
        ('1936_01_01_claimant.md', '1936'),
    ],
)
def test_a_published_date_gives_only_what_is_known(
    tmp_path: pathlib.Path, name: str, date: str
) -> None:
    """A claim known only to its month or year is dated by just that; its name fills the rest with 01."""
    _problem(tmp_path)
    _claim(
        tmp_path, name, frontmatter=_replace(_CLAIM, 'published:', f'published: {date}')
    )
    findings, _ = lint_problem_claims(tmp_path, settled=True)
    assert findings == []


@pytest.mark.parametrize(
    'links',
    [
        ('links: []',),
        ('links:', '- url: https://example.org/formalization', '  kind: formalization'),
    ],
    ids=['no_links', 'formalization'],
)
def test_a_claim_not_yet_public_has_no_published_date(
    tmp_path: pathlib.Path, links: tuple[str, ...]
) -> None:
    """An unreleased claim has published: null, no links or those due public by its release, and an unchecked filing-day name."""
    _problem(tmp_path, status='claimed', claim='proved')
    unreleased = _replace(
        _without(
            _replace(_CLAIM, 'status:', 'status: claimed'),
            'evidence:',
            '- refereed',
            '- url:',
            '  kind:',
            '  date:',
        ),
        'links:',
        *links,
    )
    unreleased = _replace(unreleased, 'published:', 'published: null')
    unreleased = _replace(unreleased, 'submitted:', 'submitted: null')
    _claim(tmp_path, '2026_03_04_claimant.md', frontmatter=unreleased)
    findings, _ = lint_problem_claims(tmp_path, settled=True)
    assert findings == []


def test_a_null_submitted_records_an_unknown_date(tmp_path: pathlib.Path) -> None:
    """A claim never submitted to the catalog's site or registry carries submitted: null."""
    _problem(tmp_path)
    _claim(tmp_path, frontmatter=_replace(_CLAIM, 'submitted:', 'submitted: null'))
    findings, _ = lint_problem_claims(tmp_path, settled=True)
    assert findings == []


def test_a_claim_id_names_one_claim_on_the_site(tmp_path: pathlib.Path) -> None:
    """A claim id is optional, and no two claim pages carry the same one, selected or not."""
    with_id = _replace(
        _CLAIM, 'submitted:', 'submitted: 2026-01-02', 'claim_id: 01M4FCNEMX'
    )
    for folder in ('alpha/p1', 'alpha/p2'):
        _problem(tmp_path, folder)
        _claim(tmp_path, folder=folder, frontmatter=with_id)
    _problem(tmp_path, 'alpha/p3')
    _claim(tmp_path, folder='alpha/p3')
    one = 'wiki/problems/alpha/p1/claims/2026_01_02_claimant.md'
    two = 'wiki/problems/alpha/p2/claims/2026_01_02_claimant.md'
    findings, _ = lint_problem_claims(tmp_path)
    assert findings == [
        f"{one}: claim_id '01M4FCNEMX' is also on {two}",
        f"{two}: claim_id '01M4FCNEMX' is also on {one}",
    ]
    findings, _ = lint_problem_claims(tmp_path, select=('p1', 'p3'))
    assert findings == [f"{one}: claim_id '01M4FCNEMX' is also on {two}"]
    _claim(tmp_path, folder='alpha/p2')
    assert lint_problem_claims(tmp_path)[0] == []


_SUFFIX = 'same-day claim pages by one claimant all take a roman suffix'
_LONE = 'a lone claim page keeps the plain name'
_GAP = 'same-day roman suffixes run _i, _ii, ... without a gap'


@pytest.mark.parametrize(
    ('names', 'expected'),
    [
        (('2026_01_02_claimant_i.md', '2026_01_02_claimant_ii.md'), []),
        (('2026_01_02_jiang_xi.md',), []),
        (('2026_01_02_claimant_i.md',), [('2026_01_02_claimant_i.md', _LONE)]),
        (
            (
                '2026_01_02_claimant.md',
                '2026_01_02_claimant_i.md',
                '2026_01_02_claimant_ii.md',
            ),
            [('2026_01_02_claimant.md', _SUFFIX)],
        ),
        (
            ('2026_01_02_claimant_i.md', '2026_01_02_claimant_iii.md'),
            [('2026_01_02_claimant_iii.md', _GAP)],
        ),
        (('2026_01_02_jiang.md', '2026_01_02_jiang_xi.md'), []),
        (
            (
                '2026_01_02_jiang_i.md',
                '2026_01_02_jiang_ii.md',
                '2026_01_02_jiang_xi.md',
            ),
            [],
        ),
    ],
)
def test_same_day_pages_of_one_claimant_take_roman_suffixes(
    tmp_path: pathlib.Path, names: tuple[str, ...], expected: list[tuple[str, str]]
) -> None:
    """One claimant's same-day pages all take roman suffixes from _i; a lone page does not."""
    _problem(tmp_path)
    for name in names:
        _claim(tmp_path, name)
    findings, _ = lint_problem_claims(tmp_path)
    folder = 'wiki/problems/alpha/p1/claims'
    assert len(findings) == len(expected), findings
    for finding, (name, message) in zip(sorted(findings), sorted(expected)):
        assert finding.startswith(f'{folder}/{name}: '), findings
        assert message in finding


def test_a_pending_page_keeps_a_temporary_suffix_beside_a_public_page(
    tmp_path: pathlib.Path,
) -> None:
    """A pending page filed on the day of its claimant's public page takes _i; the public page keeps its name."""
    _problem(tmp_path)
    _claim(tmp_path, '2026_01_02_claimant.md')
    pending = _replace(
        _without(
            _replace(_CLAIM, 'status:', 'status: claimed'),
            'evidence:',
            '- refereed',
            '- url:',
            '  kind:',
            '  date:',
        ),
        'links:',
        'links: []',
    )
    pending = _replace(pending, 'published:', 'published: null')
    pending = _replace(pending, 'submitted:', 'submitted: null')
    _claim(tmp_path, '2026_01_02_claimant_i.md', frontmatter=pending)
    findings, _ = lint_problem_claims(tmp_path)
    assert findings == []


@pytest.mark.parametrize('date', ['1936-04', '1936'])
def test_a_link_date_gives_only_what_is_known(
    tmp_path: pathlib.Path, date: str
) -> None:
    """A posting known only to its month or year is dated by just that, no day invented."""
    _problem(tmp_path)
    _claim(tmp_path, frontmatter=_replace(_CLAIM, '  date:', f'  date: {date}'))
    findings, _ = lint_problem_claims(tmp_path, settled=True)
    assert findings == []


def test_an_accepted_claim_rests_only_on_accepted_pages(tmp_path: pathlib.Path) -> None:
    """An accepted claim may depend on accepted claims, solved problems and proved cards, not on pending pages or stale cards."""
    _problem(tmp_path, 'alpha/p1', status='solved', claim='proved')
    _problem(tmp_path, 'alpha/p2', status='claimed', claim='proved')
    _problem(tmp_path, 'alpha/p3', status='solved', claim='proved')
    _claim(
        tmp_path,
        '2026_01_01_other.md',
        'alpha/p2',
        frontmatter=_without(
            _replace(
                _replace(_CLAIM, 'published:', 'published: 2026-01-01'),
                'status:',
                'status: claimed',
            ),
            'evidence:',
            '- refereed',
        ),
        body=_replace(_BODY, '**Depends on.**', '**Depends on.** Nothing.'),
    )
    write_page(
        tmp_path / 'wiki/theory/alpha/L1_card/_index.md',
        '---',
        'id: L1',
        'status: proved',
        '---',
    )
    write_page(
        tmp_path / 'wiki/theory/alpha/L2_stale/_index.md',
        '---',
        'id: L2',
        'status: proved',
        'standing: stale',
        '---',
    )
    write_page(tmp_path / 'wiki/research/note.md', '---', 'desc: A note.', '---')
    body = _replace(
        _BODY,
        '**Depends on.**',
        '**Depends on.** [[theory/alpha/L1_card/_index|L1]], [[research/note|a note]],',
        '[[theory/alpha/L2_stale/_index|a stale card]],',
        '[[problems/alpha/p3/_index|a solved problem]] and',
        '[[problems/alpha/p2/claims/2026_01_01_other|the pending claim]].',
    )
    _claim(tmp_path, body=body)
    findings, _ = lint_problem_claims(tmp_path)
    assert findings == [
        'wiki/problems/alpha/p1/claims/2026_01_02_claimant.md: an accepted claim depends on '
        "'theory/alpha/L2_stale/_index', whose status is 'proved (stale)'",
        'wiki/problems/alpha/p1/claims/2026_01_02_claimant.md: an accepted claim depends on '
        "'problems/alpha/p2/claims/2026_01_01_other', whose status is 'claimed'",
    ]


def test_a_dependence_on_a_library_result_page_is_noted_with_its_read_status(
    tmp_path: pathlib.Path,
) -> None:
    """A result page's read status is a note beside the entry and never enters the derivation."""
    _problem(tmp_path, 'alpha/p1', status='solved', claim='proved')
    write_page(
        tmp_path / 'library/first/_index.md', '---', 'name: first', '---', '', '***'
    )
    write_page(
        tmp_path / 'library/first/theorem_1.md',
        '---',
        'name: first/theorem_1',
        '---',
        '',
        '***',
        '',
        '**Read status: claims checked; proof not verified.** The statement was',
        'read on the page image.',
    )
    write_page(
        tmp_path / 'library/first/lemma_2.md',
        '---',
        'name: first/lemma_2',
        '---',
        '',
        '***',
        '',
        '**Read depth.** Claims checked: the statement (p. 3) and its hypotheses',
        '(pp. 3--4). The proof was not read.',
    )
    write_page(
        tmp_path / 'library/first/remark_3.md', '---', 'name: first/remark_3', '---'
    )
    body = _replace(
        _BODY,
        '**Depends on.**',
        '**Depends on.** [[../library/first/theorem_1|Theorem 1]],',
        '[[../library/first/lemma_2|Lemma 2]] and [[../library/first/remark_3|Remark 3]].',
    )
    _claim(tmp_path, body=body)
    findings, notes = lint_problem_claims(tmp_path)
    # an accepted claim with such dependences derives as one whose dependence is prose
    assert findings == []
    page = 'wiki/problems/alpha/p1/claims/2026_01_02_claimant.md'
    assert notes[:3] == [
        f"{page}: depends on '../library/first/theorem_1'"
        ' (read status: claims checked; proof not verified)',
        f"{page}: depends on '../library/first/lemma_2'"
        ' (read status: Claims checked: the statement (p. 3) and its hypotheses'
        ' (pp. 3--4))',
        f"{page}: depends on '../library/first/remark_3' (read status: not stated)",
    ]
    # a card is not a result page: name the result page the claim rests on
    _claim(
        tmp_path,
        body=_replace(
            _BODY,
            '**Depends on.**',
            '**Depends on.** [[../library/first/_index|the card]] and',
            '[[../library/first|the folder]].',
        ),
    )
    findings, notes = lint_problem_claims(tmp_path)
    assert findings == [
        f"{page}: Depends on names the library card '../library/first/_index'; name the"
        ' result page the claim rests on',
        f"{page}: Depends on names the library card '../library/first'; name the result"
        ' page the claim rests on',
    ]
    assert not any('depends on' in note for note in notes)


def test_write_derived_sets_the_two_standing_lines_only(tmp_path: pathlib.Path) -> None:
    """Writing the derivation changes the status and claim lines and nothing else."""
    page = _problem(tmp_path, status='open', claim='none')
    _claim(tmp_path)
    before = page.read_text(encoding='utf-8')
    assert write_derived(tmp_path) == ['wiki/problems/alpha/p1/_index.md']
    after = page.read_text(encoding='utf-8')
    assert after == before.replace('status: open', 'status: solved').replace(
        'claim: none', 'claim: proved'
    )
    assert write_derived(tmp_path) == []
    assert lint_problem_claims(tmp_path)[0] == []


def test_write_derived_leaves_a_body_line_alone(tmp_path: pathlib.Path) -> None:
    """A body line opening with a standing key stays as written when the frontmatter lacks the key."""
    page = _problem(tmp_path, status='open', claim='none')
    text = page.read_text(encoding='utf-8').replace('claim: none\n', '', 1)
    page.write_text(text + '\n```yaml\nclaim: none\n```\n', encoding='utf-8')
    _claim(tmp_path)
    before = page.read_text(encoding='utf-8')
    assert write_derived(tmp_path) == ['wiki/problems/alpha/p1/_index.md']
    after = page.read_text(encoding='utf-8')
    assert after == before.replace('status: open', 'status: solved')
    # the missing key is the check's to report
    findings, _ = lint_problem_claims(tmp_path)
    assert findings == [
        'wiki/problems/alpha/p1/_index.md: missing claim (one of none, proved,'
        ' disproved, answered, independent, contested)',
        "wiki/problems/alpha/p1/_index.md: claim None but the claims derive 'proved'",
    ]


def test_a_selection_scopes_the_check_and_the_write_to_named_folders(
    tmp_path: pathlib.Path,
) -> None:
    """Selected folders alone are written and checked; an unknown name is a finding."""
    _problem(tmp_path, 'alpha/p1', status='open', claim='none')
    _problem(tmp_path, 'alpha/p2', status='open', claim='none')
    _claim(tmp_path, folder='alpha/p1')
    _claim(tmp_path, folder='alpha/p2')
    assert write_derived(tmp_path, select=('p2',)) == [
        'wiki/problems/alpha/p2/_index.md'
    ]
    findings, notes = lint_problem_claims(tmp_path, select=('p2', 'p9'))
    assert findings == ['p9: no problem folder of that name']
    assert notes[0].startswith('1 problem(s); 1 claim page(s); 0 provisional')
    assert write_derived(tmp_path) == ['wiki/problems/alpha/p1/_index.md']


def test_only_index_pages_with_a_status_are_problems(tmp_path: pathlib.Path) -> None:
    """Area indexes, claims indexes and leaf pages are not problems; a missing tree is an error."""
    with pytest.raises(NotADirectoryError):
        lint_problem_claims(tmp_path)
    _problem(tmp_path, 'alpha/p1')
    _claim(tmp_path)
    write_page(tmp_path / 'wiki/problems/_index.md', '---', 'desc: Problems.', '---')
    write_page(
        tmp_path / 'wiki/problems/alpha/_index.md', '---', 'desc: An area.', '---'
    )
    write_page(
        tmp_path / 'wiki/problems/alpha/p1/claims/_index.md',
        '---',
        'desc: Claims.',
        '---',
    )
    write_page(
        tmp_path / 'wiki/problems/alpha/p1/notes.md', '---', 'status: open', '---'
    )
    findings, notes = lint_problem_claims(tmp_path)
    assert findings == []
    assert notes[0].startswith('1 problem(s); 1 claim page(s)')
