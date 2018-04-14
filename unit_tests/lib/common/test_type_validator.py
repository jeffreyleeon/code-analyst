# Import system libraries
import os
import sys

# Import 3rd party libraries
import pytest

# Import custom libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
import lib.common.type_validator as type_validator


class TestBaseValidator(object):

    def test_base_validator_is_none(self):
        assert type_validator.BaseValidator.is_none(None) == True
        assert type_validator.BaseValidator.is_none(False) == False
        assert type_validator.BaseValidator.is_none(1) == False
        assert type_validator.BaseValidator.is_none('str') == False
        assert type_validator.BaseValidator.is_none([]) == False
        assert type_validator.BaseValidator.is_none({}) == False

    def test_base_validator_is_not_none(self):
        assert type_validator.BaseValidator.is_not_none(None) == False
        assert type_validator.BaseValidator.is_not_none(False) == True
        assert type_validator.BaseValidator.is_not_none(1) == True
        assert type_validator.BaseValidator.is_not_none('str') == True
        assert type_validator.BaseValidator.is_not_none([]) == True
        assert type_validator.BaseValidator.is_not_none({}) == True

class TestArrayValidator(object):

    def test_array_validator_is_array(self):
        assert type_validator.ArrayValidator.is_array(None) == False
        assert type_validator.ArrayValidator.is_array(False) == False
        assert type_validator.ArrayValidator.is_array(1) == False
        assert type_validator.ArrayValidator.is_array('str') == False
        assert type_validator.ArrayValidator.is_array([]) == True
        assert type_validator.ArrayValidator.is_array(['a', 'b']) == True
        assert type_validator.ArrayValidator.is_array({}) == False

    def test_array_validator_is_empty_array(self):
        assert type_validator.ArrayValidator.is_empty_array(None) == False
        assert type_validator.ArrayValidator.is_empty_array(False) == False
        assert type_validator.ArrayValidator.is_empty_array(1) == False
        assert type_validator.ArrayValidator.is_empty_array('str') == False
        assert type_validator.ArrayValidator.is_empty_array([]) == True
        assert type_validator.ArrayValidator.is_empty_array(['a', 'b']) == False
        assert type_validator.ArrayValidator.is_empty_array({}) == False

    def test_array_validator_is_empty_array(self):
        assert type_validator.ArrayValidator.is_non_empty_array(None) == False
        assert type_validator.ArrayValidator.is_non_empty_array(False) == False
        assert type_validator.ArrayValidator.is_non_empty_array(1) == False
        assert type_validator.ArrayValidator.is_non_empty_array('str') == False
        assert type_validator.ArrayValidator.is_non_empty_array([]) == False
        assert type_validator.ArrayValidator.is_non_empty_array(['a', 'b']) == True
        assert type_validator.ArrayValidator.is_non_empty_array({}) == False
