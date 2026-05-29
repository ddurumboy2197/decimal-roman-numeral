# test_decimal_to_roman.py
import pytest
from decimal_to_roman import decimal_to_roman

def test_decimal_to_roman():
    assert decimal_to_roman(1) == 'I'
    assert decimal_to_roman(4) == 'IV'
    assert decimal_to_roman(5) == 'V'
    assert decimal_to_roman(9) == 'IX'
    assert decimal_to_roman(13) == 'XIII'
    assert decimal_to_roman(44) == 'XLIV'
    assert decimal_to_roman(1000) == 'M'

def test_decimal_to_roman_zero():
    assert decimal_to_roman(0) == ''

def test_decimal_to_roman_negative():
    with pytest.raises(ValueError):
        decimal_to_roman(-1)

def test_decimal_to_roman_non_integer():
    with pytest.raises(TypeError):
        decimal_to_roman(1.5)
