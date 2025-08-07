# System Modules
import sys
import os
import unittest

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

class TestCalculations(unittest.TestCase):

    def test_area_of_circle_positive_radius(self):
        """Test with a positive radius."""
        # Arrange
        radius = 1

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertAlmostEqual(result, 3.14159, places=5)

    def test_area_of_circle_zero_radius(self):
        """Test with a radius of zero."""
        # Arrange
        radius = 0

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertEqual(result, 0)

    def test_area_of_circle_negative_radius(self):
        """Test with a negative radius to raise ValueError."""
        # Arrange
        radius = -1

        # Act & Assert
        with self.assertRaises(ValueError):
            area_of_circle(radius)

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

    def test_get_nth_fibonacci_zero(self):
        """Test with n=0."""
        n = 0
        result = get_nth_fibonacci(n)
        self.assertEqual(result, 0)

    def test_get_nth_fibonacci_one(self):
        """Test with n=1."""
        n = 1
        result = get_nth_fibonacci(n)
        self.assertEqual(result, 1)

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

    def test_get_nth_fibonacci_ten(self):
        """Test with n=10."""
        n = 10
        result = get_nth_fibonacci(n)
        self.assertEqual(result, 55)

    def test_get_nth_fibonacci_large_n(self):
        """Test with a very large n."""
        n = 50
        result = get_nth_fibonacci(n)
        self.assertEqual(result, 12586269025)  # Fibonacci(50)

    def test_get_nth_fibonacci_negative(self):
        """Test with a negative number to raise ValueError."""
        n = -1
        with self.assertRaises(ValueError):
            get_nth_fibonacci(n)

    def test_get_nth_fibonacci_non_integer_input(self):
        """Test with a non-integer input to raise TypeError."""
        with self.assertRaises(TypeError):
            get_nth_fibonacci(3.5)
        with self.assertRaises(TypeError):
            get_nth_fibonacci("string")
        with self.assertRaises(TypeError):
            get_nth_fibonacci(None)

if __name__ == '__main__':
    unittest.main()