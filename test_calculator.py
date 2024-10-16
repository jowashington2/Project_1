import pytest
from src.main import roman_to_int, int_to_roman, calculate, evaluate_expression

def test_roman_to_int():
    assert roman_to_int("X") == 10
    assert roman_to_int("IV") == 4
    assert roman_to_int("MCMXCIV") == 1994

def test_int_to_roman():
    assert int_to_roman(10) == "X"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(1994) == "MCMXCIV"

def test_calculate():
    assert calculate("+", 5, 10) == 15
    assert calculate("-", 10, 5) == 5
    assert calculate("*", 6, 7) == 42
    assert calculate("/", 9, 3) == 3

def test_evaluate_expression():
    assert evaluate_expression("VII + V") == "XII"
    assert evaluate_expression("(X + V) * II") == "XXX"
    assert evaluate_expression("II * (VI + II)") == "XVI"
    assert evaluate_expression("0") == "0 does not exist in Roman numerals."
    assert evaluate_expression("-I") == "Negative numbers can't be represented in Roman numerals."
