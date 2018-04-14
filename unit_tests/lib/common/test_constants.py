# Import system libraries
import os
import sys

# Import 3rd party libraries
import pytest

# Import custom libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
import lib.common.constants as constants

def test_CODE_ANALYST_OPT_TYPES():
    assert constants.CODE_ANALYST_OPT_TYPES == {
        'ALL': 'all',
        'COMMIT_MSG': 'commit_msg'
    }

def test_GITHUB_BASE_URL():
    assert constants.GITHUB_BASE_URL == 'https://github.com/'
