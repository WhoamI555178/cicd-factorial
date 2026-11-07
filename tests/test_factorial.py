import pytest
from app.factorial import calculate_factorial

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_positive():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError):
        calculate_factorial(-1)