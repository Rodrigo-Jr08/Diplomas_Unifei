import pytest

from diploma_mec.business_rules import exactly_one
from diploma_mec.errors import BusinessRuleError


def test_exactly_one_accepts_one_value():
    assert exactly_one(object(), None) == 1


def test_exactly_one_rejects_zero():
    with pytest.raises(BusinessRuleError):
        exactly_one(None, None)


def test_exactly_one_rejects_two():
    with pytest.raises(BusinessRuleError):
        exactly_one(object(), object())
