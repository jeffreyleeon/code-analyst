# Import python built-in libraries
import getopt
import os
import sys

# Import self-defined lib
base_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(base_dir, "./lib"))
from common.type_validator import ArrayValidator as array_validator
import common.constants as constants

config = {
    'operation_type': None,
    'github_url': None
}

def parse_config(opt_params):
    opts, args = getopt.getopt(opt_params, 'h', ['url=', 'operation-type='])
    for opt, arg in opts:
        arg = str(arg)
        if opt == '--url':
            if constants.GITHUB_BASE_URL not in arg:
                raise Exception('Expect url to include {}'.format(arg))
            config['github_url'] = arg
        elif opt == '--operation-type':
            if arg not in constants.CODE_ANALYST_OPT_TYPES.values():
                raise Exception('Unknown operation type: {}'.format(arg))
            config['operation_type'] = arg
        elif opt == '-h':
            usage()
            sys.exit()

def usage():
    print "python populate_throttle_devices.py --url github_https_url/--operation-type operation_type/-h"
    print "     -h                  Print this message"
    print "     --url               github url in https, e.g. https://github.com/jeffreyleeon/code-analyst"
    print "     --operation-type    operation types, one of {}".format(constants.CODE_ANALYST_OPT_TYPES.values())

def main(opt_params):
    try:
        parse_config(opt_params)
    except Exception as err:
        print('Failed when parsing params {}\n'.format(err))
        usage()
        sys.exit(2)
    print('===what is config {}'.format(config))
    pass

if __name__ == '__main__':
    arguments_array = sys.argv[1:]
    # Check number of params
    if array_validator.is_non_empty_array(arguments_array) is False:
        print('Error: Expect at least 1 argument, exit script.\n')
        usage()
        exit(0)
    print('Start of code analyst with arguments {}\n'.format(arguments_array))
    opt_params = arguments_array[:]
    main(opt_params)