"""Complete event enumeration for the two domains in the owning sketch."""

from itertools import combinations

from .exact import Field, Root, real_roots, require, root_groups


def concentric_position(root, boundary):
    low, high = root.compare_value(boundary), root.compare_value(1 / boundary)
    if low < 0:
        return "below"
    if low == 0:
        return "lower_boundary"
    if high < 0:
        return "inside"
    if high == 0:
        return "upper_boundary"
    return "above"


def concentric_counts_direct(m, field, root):
    """All 2m-1 labels at each orbit, grouped by exact polynomial evaluation."""
    result = []
    for orbit in ("A", "B"):
        distances = []
        for k in range(1, m):
            length = 2 - 2 * field.cos(2 * k)
            distances.append((0, 0, length) if orbit == "A" else (length, 0, 0))
        distances.extend((1, -2 * field.cos(2 * k + 1), 1) for k in range(m))
        groups = []
        for distance in distances:
            for representative in groups:
                if root.vanishes(*(x - y for x, y in zip(distance, representative))):
                    break
            else:
                groups.append(distance)
        result.append(len(groups))
    return result


def concentric(m):
    field = Field(2 * m)
    h, q = m // 2, (m + 1) // 2
    lengths = [2 - 2 * field.cos(2 * i) for i in range(1, h + 1)]
    cosines = [field.cos(2 * j + 1) for j in range(q)]
    require(len(set(lengths)) == h and len(set(cosines)) == q, "reflection quotient")
    labeled = []
    root_tallies = {"negative": 0, "zero": 0, "positive": 0}
    for i, length in enumerate(lengths, 1):
        for j, cosine in enumerate(cosines):
            for kind, coefficients in (
                ("P", (1, -2 * cosine, 1 - length)),
                ("Q", (1 - length, -2 * cosine, 1)),
            ):
                for root in real_roots(field, *coefficients):
                    sign = root.compare_value(0)
                    root_tallies[{-1: "negative", 0: "zero", 1: "positive"}[sign]] += 1
                    if sign > 0:
                        labeled.append((root, [kind, i, j, root.branch]))
    boundary = field.cos(1)
    records = []
    for root, labels in root_groups(labeled):
        labels.sort()
        position = concentric_position(root, boundary)
        u = sum(label[0] == "P" for label in labels)
        v = sum(label[0] == "Q" for label in labels)
        counts = [m - u, m - v]
        require(u <= h and v <= h, "injective-list matching count")
        # Direct full-label partitions on every admissible event and every
        # event that reduces both orbits, plus all small orders.
        if position == "inside" or (u and v) or m <= 5:
            require(concentric_counts_direct(m, field, root) == counts, "orbit partition")
        records.append({"events": labels, "position": position, "counts": counts})
    # P(r)=r^2 Q(1/r): a positive class has the reciprocal event class with
    # its orbit counts swapped. This checks multiplicities as well as coverage.
    for left, right in zip(records, reversed(records)):
        require(left["counts"] == list(reversed(right["counts"])), "reciprocal counts")
        require(
            {(1 if e[0] == "P" else 0, e[1], e[2]) for e in left["events"]}
            == {(0 if e[0] == "P" else 1, e[1], e[2]) for e in right["events"]},
            "reciprocal event labels",
        )
    if m == 4:
        # The positive root of r^2-sqrt(2)*r-1 is (1+sqrt(3))/sqrt(2).
        control = [
            row for row in records if ["P", 1, 0, 1] in row["events"]
        ]
        require(len(control) == 1, "H8 event exists uniquely")
        require(control[0]["counts"] == [3, 3], "H8 pinned counts")
        require(control[0]["position"] == "above", "H8 convexity rejection")
    return {
        "family": "half_step_concentric",
        "order": m,
        "field_order": 2 * m,
        "threshold": m,
        "generic_counts": [m, m],
        "equations": 2 * h * q,
        "real_root_events": root_tallies,
        "critical": records,
    }


def controls():
    """Root identities, degeneracies, strict endpoints and near inequalities."""
    field = Field(8)
    sqrt_two = 2 * field.cos(1)
    require(sqrt_two * sqrt_two == 2, "cyclotomic sqrt(2)")
    roots = real_roots(field, 1, 0, -2)
    require(len(roots) == 2, "two quadratic branches")
    require(roots[0].is_value(-sqrt_two) and roots[1].is_value(sqrt_two), "branch choice")
    alternate = real_roots(field, 1, -sqrt_two - 1, sqrt_two)
    require(roots[1].equal(alternate[1]), "common root of distinct quadratics")
    require(not roots[0].equal(alternate[0]), "unequal quadratic roots")
    require(len(real_roots(field, 1, 0, 1)) == 0, "no real roots")
    repeated = real_roots(field, 1, -2, 1)
    require(len(repeated) == 1 and repeated[0].is_value(1), "repeated root")
    linear = real_roots(field, 0, 2, -1)
    require(len(linear) == 1 and linear[0].is_value(field(1) / 2), "linear equation")
    zero = real_roots(field, 1, -1, 0)
    require([root.compare_value(0) for root in zero] == [0, 1], "zero-root exclusion")
    one = Root(field, value=field(1))
    near = Root(field, value=field(1) + field(1) / (2 ** 300))
    require(not one.equal(near) and one.compare(near) == -1, "no tolerance equality")
    for m in (3, 4, 5, 32):
        current = Field(2 * m)
        boundary = current.cos(1)
        lower, upper = Root(current, value=boundary), Root(current, value=1 / boundary)
        require(concentric_position(lower, boundary) == "lower_boundary", "open lower endpoint")
        require(concentric_position(upper, boundary) == "upper_boundary", "open upper endpoint")
        require(concentric_position(Root(current, value=current(1)), boundary) == "inside", "interior")


def affine_lines(n, field):
    lines = []
    for i in range(n):
        row = {}
        for j in range(n):
            if i == j:
                continue
            sum_double = (field.cos(2 * i) + field.cos(2 * j)) / 2
            difference, total = field.cos(i - j), field.cos(i + j)
            x = 1 + sum_double - difference - total
            y = 1 - sum_double - difference + total
            # Separate coordinate-difference construction checks the formulas.
            horizontal = field.cos(i) - field.cos(j)
            vertical_imag = (
                field.powers[i] - field.powers[-i % n]
                - field.powers[j] + field.powers[-j % n]
            ) / 2
            require(x == horizontal * horizontal, "horizontal squared distance")
            require(y == -vertical_imag * vertical_imag, "vertical squared distance")
            row[j] = x, y
        lines.append(row)
    return lines


def affine(n):
    field = Field(n)
    lines = affine_lines(n, field)
    generic = [len(set(row.values())) for row in lines]
    require(min(generic) >= n // 2, "generic affine count")
    parameters = {}
    tallies = {"persistent": 0, "parallel": 0, "negative": 0, "zero": 0, "positive": 0}
    for i, row in enumerate(lines):
        for j, k in combinations(row, 2):
            xj, yj = row[j]
            xk, yk = row[k]
            if yj == yk:
                tallies["persistent" if xj == xk else "parallel"] += 1
                continue
            parameter = (xk - xj) / (yj - yk)
            sign = field.sign(parameter)
            tallies[{-1: "negative", 0: "zero", 1: "positive"}[sign]] += 1
            if sign > 0:
                parameters.setdefault(parameter, []).append([i, j, k])
    require(sum(tallies.values()) == n * (n - 1) * (n - 2) // 2, "affine pair coverage")
    roots = [(Root(field, value=s), s) for s in parameters]
    records = []
    for root, values in root_groups(roots):
        require(len(values) == 1, "field keys deduplicate affine parameters")
        parameter = values[0]
        events = parameters[parameter]
        counts = []
        # Direct evaluation of all vertices, independently of event merging.
        for i, row in enumerate(lines):
            partition = {}
            for j, (x, y) in row.items():
                partition.setdefault(x + parameter * y, []).append(j)
            counts.append(len(partition))
            # Check all event edges against the resulting partition, and that
            # every new equality is represented by its event (or persistent).
            expected = {
                (a, b) for pin, a, b in events if pin == i
            }
            actual = set()
            for block in partition.values():
                for a, b in combinations(block, 2):
                    if row[a] != row[b]:
                        actual.add((a, b))
            require(actual == expected, "affine equality-event completeness")
        circle = parameter == 1
        if circle:
            require(counts == [n // 2] * n, "regular polygon circle control")
        if n == 8 and parameter == 1 + 4 * field.cos(1):
            require(counts == [3, 6, 4, 6, 3, 6, 4, 6], "affine every-vertex control")
        records.append({"events": events, "circle": circle, "counts": counts})
    if n == 8:
        require(1 + 4 * field.cos(1) in parameters, "affine control parameter present")
    return {
        "family": "affine_regular",
        "order": n,
        "field_order": n,
        "threshold": n // 2,
        "generic_counts": generic,
        "pair_events": tallies,
        "critical": records,
    }
