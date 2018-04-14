# Import system libraries
import getopt
import os
import sys

# Import 3rd party libraries
import pytest

# Import custom libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import code_analyst
import lib.common.constants as constants

class TestParseConfig(object):

    def test_unknow_params(self):
        opt_params = ['-a', 1, '-b', 2]
        with pytest.raises(getopt.GetoptError):
            code_analyst.parse_config(opt_params)

    def test_valid_url_param(self):
        opt_params = ['--url', 'https://github.com/jeffreyleeon/code-analyst']
        code_analyst.parse_config(opt_params)
        assert code_analyst.config['github_url'] == 'https://github.com/jeffreyleeon/code-analyst'

    def test_invalid_url_param(self):
        opt_params = ['--url', 'https://google.com']
        with pytest.raises(Exception):
            code_analyst.parse_config(opt_params)

    def test_valid_operation_types(self):
        for op_type in constants.CODE_ANALYST_OPT_TYPES.values():
            opt_params = ['--operation-type', op_type]
            code_analyst.parse_config(opt_params)
            assert code_analyst.config['operation_type'] == op_type

    def test_invalid_operation_types(self):
        opt_params = ['--operation-type', 'random_op_type']
        with pytest.raises(Exception):
            code_analyst.parse_config(opt_params)
