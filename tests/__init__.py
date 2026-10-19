"""Tests for ``tools``."""

# The guard in conftest runs before the star imports load test modules that
# import corpus evidence at module level; pytest itself imports a conftest only
# after its package.
from . import conftest
from .test_claim_carry_forward import *
from .test_cli import *
from .test_core import *
from .test_corpus_layout import *
from .test_e0834_bitmask import *
from .test_e0834_evidence import *
from .test_fill_claim_authors import *
from .test_gate_boundaries import *
from .test_import import *
from .test_lean_comment_only import *
from .test_lean_coverage_pathspec import *
from .test_lean_workflow import *
from .test_owens_evidence import *
from .test_precommit_excludes import *
from .test_problem_library_links import *
from .test_root_namespace import *
from .test_tools_provider_loading import *
from .test_util import *
from .test_wiki_excludes import *
