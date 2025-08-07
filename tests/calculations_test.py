# System Modules
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0

def test_area_of_circle_negative_radius(self):
   """Test with a negative radius to raise ValueError."""
   # Arrange
   radius = -1

   # Act & Assert
   with self.assertRaises(ValueError):
      area_of_circle(radius)


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1

def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55

def test_get_nth_fibonacci_negative(self):
   """Test with a negative number to raise ValueError."""
   # Arrange
   n = -1

   # Act & Assert
   with self.assertRaises(ValueError):
      get_nth_fibonacci(n)


def test_area_of_circle_large_radius(self):
    """Test with a very large radius."""
    radius = 1e6
    result = area_of_circle(radius)
    expected = 3.14159 * (radius ** 2)
    self.assertAlmostEqual(result, expected, places=5)

def test_area_of_circle_small_positive_radius(self):
    """Test with a very small positive radius."""
    radius = 1e-6
    result = area_of_circle(radius)
    expected = 3.14159 * (radius ** 2)
    self.assertAlmostEqual(result, expected, places=5)

def test_area_of_circle_non_numeric_input(self):
    """Test with a non-numeric input to raise TypeError."""
    with self.assertRaises(TypeError):
        area_of_circle("string")
    with self.assertRaises(TypeError):
        area_of_circle(None)

def test_get_nth_fibonacci_two(self):
    """Test with n=2."""
    n = 2
    result = get_nth_fibonacci(n)
    self.assertEqual(result, 1)

def test_get_nth_fibonacci_three(self):
    """Test with n=3."""
    n = 3
    result = get_nth_fibonacci(n)
    self.assertEqual(result, 2)

def test_get_nth_fibonacci_large_n(self):
    """Test with a very large n."""
    n = 50
    result = get_nth_fibonacci(n)
    self.assertEqual(result, 12586269025)  # Fibonacci(50)

def test_get_nth_fibonacci_non_integer_input(self):
    """Test with a non-integer input to raise TypeError."""
    with self.assertRaises(TypeError):
        get_nth_fibonacci(3.5)
    with self.assertRaises(TypeError):
        get_nth_fibonacci("string")
    with self.assertRaises(TypeError):
        get_nth_fibonacci(None)


