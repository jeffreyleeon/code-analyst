'''
type_validator.py contains classes that validate variable types

'''

class BaseValidator:
    '''
    BaseValidator check trivial type such as None type.
    '''

    @staticmethod
    def is_none(arg):
        return arg is None

    @staticmethod
    def is_not_none(arg):
        return BaseValidator.is_none(arg) == False

class ArrayValidator:
    '''
    ArrayValidator validator arrays. 
    '''

    @staticmethod
    def is_array(arg):
        return \
            BaseValidator.is_not_none(arg) and \
            isinstance(arg, list)

    @staticmethod
    def is_empty_array(arg):
        return ArrayValidator.is_array(arg) and len(arg) == 0

    @staticmethod
    def is_non_empty_array(arg):
        return ArrayValidator.is_array(arg) and len(arg) > 0