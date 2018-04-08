# Import python built-in libraries
import getopt
import os
import sys

# Import self-defined lib
base_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(base_dir, "./lib"))
from common.type_validator import ArrayValidator as array_validator
import common.constants as constants

def main(opt_type, opt_params):
    pass

if __name__ == '__main__':
    arguments_array = sys.argv[1:]
    # Check number of params
    if array_validator.is_non_empty_array(arguments_array) is False:
        print('Error: Expect at least 1 argument, exit script.')
        exit(0)
    print('Start of code analyst with arguments {}'.format(arguments_array))
    opt_type = arguments_array[0]
    opt_params = arguments_array[1:]
    # Check operation type
    if opt_type not in constants.CODE_ANALYST_OPT_TYPES.values():
        print('Error: Unsupported operation type: {}'.format(opt_type))
        exit(0)
    main(opt_type, opt_params)