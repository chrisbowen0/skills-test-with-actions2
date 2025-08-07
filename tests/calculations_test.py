# System Modules
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_large_radius():
    """Test with a very large radius."""
    radius = 1e6
    result = area_of_circle(radius)
    expected = 3.14159 * (radius ** 2)
    assert abs(result - expected) < 1e-5

def test_area_of_circle_small_positive_radius():
    """Test with a very small positive radius."""
    radius = 1e-6
    result = area_of_circle(radius)
    expected = 3.14159 * (radius ** 2)
    assert abs(result - expected) < 1e-5

def test_area_of_circle_non_numeric_input():
    """Test with a non-numeric input to raise TypeError."""
    with pytest.raises(TypeError):
        area_of_circle("string")
    with pytest.raises(TypeError):
        area_of_circle(None)

def test_get_nth_fibonacci_two():
    """Test with n=2."""
    n = 2
    result = get_nth_fibonacci(n)
    assert result == 1

def test_get_nth_fibonacci_three():
    """Test with n=3."""
    n = 3
    result = get_nth_fibonacci(n)
    assert result == 2

def test_get_nth_fibonacci_large_n():
    """Test with a very large n."""
    n = 50
    result = get_nth_fibonacci(n)
    assert result == 12586269025  # Fibonacci(50)

def test_get_nth_fibonacci_non_integer_input():
    """Test with a non-integer input to raise TypeError."""
    with pytest.raises(TypeError):
        get_nth_fibonacci(3.5)
    with pytest.raises(TypeError):
        get_nth_fibonacci("string")
    with pytest.raises(TypeError):
        get_nth_fibonacci(None)
