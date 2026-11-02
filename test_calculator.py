import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide_uneven():
    # Arrange
    a, b = 5, 2
    # Act
    result = divide(a, b)
    # Assert
    assert result == 2.5

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5), (-2, -3, -5), (0, 0, 0),
])
def test_add_many(a, b, expected):
    assert add(a, b) == expected

def test_divide_by_zero():
    assert divide (5, 0) == float("inf")
