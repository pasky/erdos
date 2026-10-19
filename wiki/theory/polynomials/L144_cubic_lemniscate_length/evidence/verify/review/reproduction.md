---
name: theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/reproduction
desc: Exact inputs, execution substitutions, rerun commands, and the successful and failed computation outcomes for the frozen cubic examination.
created: 2026-10-15T23:40:25Z
updated: 2026-10-15T23:40:25Z
---

# theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/reproduction

***

Reading: the complete frozen checker and evidence description, the copied
runtime interface, the supplied installed API reference, and the independently
written diagnostic. These instructions accompany the [report](report.md) and
[derivations](derivations.md); they do not turn a stored output into a check.

## Retained inputs

`assets/subject/` contains exact copies of the supplied statement, proof,
evidence description, checker, and individually supplied runtime files. The
copyrighted source excerpt is identified by its exact bibliographic locator
instead of reproduced. No executable mathematical input was changed. The runtime lockfile is
named `uv.lock.txt`, preserving its delivered safe name and original bytes.
It is not an installation target.

The independent finite diagnostic is [independent_check.py](independent_check.py).
Its exact Gaussian-rational cases and rejection inputs are
[assets/diagnostic_inputs.json](assets/diagnostic_inputs.json). It reads the
retained checker as a module to test its functions; it does not run the
checker's `main()` a second time. Its reference density comes from a prescribed
root and quadratic division, not Cardano. The mathematical rationale and scope
are in derivation 3.

The operating wrapper
[assets/operating/run_frozen_evidence.py](assets/operating/run_frozen_evidence.py)
is preserved exactly as executed. It prints and checks environment identities,
sets the original single-script argument list, and executes the unchanged
checker through `runpy.run_path`. It introduces no mathematical check or
changed constant. The supplied installed API text is retained as
[assets/operating/flint_api_reference.txt](assets/operating/flint_api_reference.txt);
no example from it was executed.

## Environment and path substitution

The observed mathematical runs used the checkout-local `.venv`, CPython
3.14.6, python-flint 0.9.0, the supplied runtime's `tools` package, and the
interpreter's standard-library `typing`. Each running process printed the
four commissioned identities: `sys.prefix`, `tools.__file__`,
`typing.__file__`, and python-flint version. Both used Python safe-path mode.
The author's checker sets `ctx.prec=64` and `ctx.threads=1`; the independent
diagnostic uses one thread with 64-bit tested boxes and 128-bit reference
calculations.

The original documented command, from the repository root, is:

```sh
uv run --no-sync python wiki/theory/polynomials/L144_cubic_lemniscate_length/evidence/main.py
```

The closed examination authorized replacing that live mathematical path by
the supplied frozen copy and replacing the package import by its supplied
runtime. The original live path was not executed. The commands below apply
that same substitution to the retained copies, plus the transparent identity
wrapper used in the observed full run. Set `review_dir` to the directory
containing this report; after filing at the commissioned home it is as shown.
Use an already installed repository environment. Do not install or synchronize
from the copied runtime project or lockfile.

## Full frozen checker

From the repository root:

```sh
review_dir=wiki/theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review
env -u VIRTUAL_ENV -u UV_PROJECT -u UV_PROJECT_ENVIRONMENT \
  -u UV_WORKING_DIR -u UV_NO_PROJECT \
  PYTHONPATH="$PWD/$review_dir/assets/subject/runtime" \
  PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
  uv run --no-sync python -P -u \
  "$review_dir/assets/operating/run_frozen_evidence.py" \
  "$review_dir/assets/subject/evidence/main.py"
```

This is a full mathematical rerun, not an output parser. The observed run
exited 0 with 22 successful obligations in approximately 288 seconds. It
reproduced all thirteen small-parameter boxes and 591 accepted larger-parameter
boxes. Detailed numerical findings are in the report. The identity prefix is
operating information, not a mathematical check. A rerun must inspect its own
outputs and exit status; the recorded result is not a substitute.

The driver has no input data file and exposes no quick-mode argument. Its
failure interfaces are its fixed constants, computed candidate bounds, and
parameterized helper functions. The following are concrete negative witnesses
for its obligation types, established by reading their predicates; they are
not additional executed tests or edits to the retained source.

| Obligation type | Input at that interface that fails |
| --- | --- |
| Small-parameter tiling | `A_BOXES=12` with `A_END=13/64`. |
| Near arc is a graph | `A_END=1`, `Y_CUT=50`, giving $a^6Y^2=2500$. |
| Far branch beyond the cutoff | `A_END=1/2`, `Y_CUT=50`, giving $c/a^3=\sqrt{60}<50$. |
| Gamma/beta consistency | A zero ball in place of `L0`, disjoint from the positive beta expression. |
| Each negative-integral obligation | A candidate returned upper bound of zero; strict negativity fails. |
| Both regime-join obligations | `BETA_START=1` with `A_END=13/64`; this creates a gap in both parameterizations. |
| Successful full parameter cover | `cover_b(0,2^(-41))`, which fails its window and cannot resolve before its width cutoff; this case was also executed by the diagnostic. |
| Accepted length margin | A candidate upper length bound equal to $L_0$, or a candidate margin exactly $1/100$, fails the respective strict test. |
| Control ordering and width | Candidate lower/upper values $(9,8)$ fail ordering; $(8,81/10)$ fail the $0.05$ width requirement. |

## Independent diagnostic and its retained failures

From the same repository root, with `review_dir` set as above:

```sh
env -u VIRTUAL_ENV -u UV_PROJECT -u UV_PROJECT_ENVIRONMENT \
  -u UV_WORKING_DIR -u UV_NO_PROJECT \
  PYTHONPATH="$PWD/$review_dir/assets/subject/runtime" \
  PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
  uv run --no-sync python -P -u "$review_dir/independent_check.py"
```

The observed run completed in less than a second and **exited 1**, with
44 checks passing and these four of 48 failing:

- `finite depth cap retains rectangle bounds [2,4]`;
- `negative rectangle bound uses correct width endpoints`;
- `positive rectangle bound uses correct width endpoints`;
- `sign-changing rectangle bound contains both extremes`.

Despite their labels, their predicates require exact equalities to ideal
endpoints. The ball-constructor contract permits outward radius rounding, so
these predicates are stronger than the required enclosing inequalities.
The actual endpoint values were not printed. The driver is retained unchanged
and is not a successful whole certificate. Its observed root-comparison and
rejection-case results have the finite scope stated in the report. The
analytical signed-rectangle argument does not rely on the four failed tests.

Meaningful failing inputs include the wrong origin density $4/3$, an
indeterminate integrand at depth zero, the invalid critical window at
$\beta=0$, and an unresolved cover of $[0,2^{-41}]$. Their exact forms are
in the JSON and code. The failure to reject any one of them would make the
corresponding diagnostic check fail. Replacing an enclosing constant interval
by its midpoint would fail for the endpoint members of that constant family;
the retained exact-equality tests did not properly encode that weaker
requirement.

The diagnostic has not been repaired, rerun, or retroactively relabeled as a
pass. If the four calibration assertions are corrected and instrumented, the
result must be retained as a new diagnostic record. Only the two described
mathematical executions were performed. Further execution is not claimed by
this record.

## Coverage and limitations

The full checker verifies the uniform integral bounds and their parameter
cover. The written reductions, gamma identity, source interfaces, and equality
classification are checked mathematically in the report and derivations.
The independent root route can detect branch, coefficient, or normalization
mistakes on its exact cases, but shares the arb/acb implementation and makes
no statistical or universal inference from those cases.

The supplied source is cited by locator and the operating references are retained for
the assessment; they do not imply PDF inspection or reconstruction of the
underlying external books. Raw environment receipts, process transcripts,
subscription outputs, and communication receipts remain private operating
records. They are not mathematical inputs to either program. The earlier
excluded-package import is disclosed in the report and still requires the
distinct grader's materiality ruling.
