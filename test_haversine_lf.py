import pytest
from myfunctions import mysqrt, mycos, myarcsin, mysin
from myhaversine import myhaversine

# Test the mysqrt function
def test_mysqrt():
    # Test for a perfect square
    assert mysqrt(25) == 5

    # Test for a larger perfect square
    assert mysqrt(100) == 10

    # Test for the square root of 0
    assert mysqrt(0) == 0

    # Test for an arbitrary positive number
    assert mysqrt(2) == pytest.approx(1.41421, abs=1e-5)

    # Test for a very small number
    assert mysqrt(1e-10) == pytest.approx(1e-5, abs=1e-5)

# Test the mycos function
def test_mycos():
    # Test for an acute angle (30 degrees)
    assert mycos(30) == pytest.approx(0.86603, abs=1e-5)

    # Test for a right angle (45 degrees)
    assert mycos(45) == pytest.approx(0.70711, abs=1e-5)

    # Test for an obtuse angle (60 degrees)
    assert mycos(60) == pytest.approx(0.5, abs=1e-5)

    # Test for cosine of 0 degrees (should be 1)
    assert mycos(0) == 1

    # Test for cosine of 90 degrees (should be 0)
    assert mycos(90) == 0

    # Test for cosine of 180 degrees (should be -1)
    assert mycos(180) == -1

# Test the myarcsin function
def test_myarcsin():
    # Test for arcsin of 0 (should be 0)
    assert myarcsin(0) == 0

    # Test for arcsin of 0.5 (should be 30 degrees)
    assert myarcsin(0.5) == pytest.approx(30, abs=1e-5)

    # Test for arcsin of 1 (should be 90 degrees)
    assert myarcsin(1) == 90

    # Test for arcsin of -1 (should be -90 degrees)
    assert myarcsin(-1) == -90

    # Test for arcsin of cosine value (should reverse the angle)
    assert myarcsin(0.86603) == pytest.approx(30, abs=1e-5)

# Test the mysin function
def test_mysin():
    # Test for sine of 30 degrees (should be 0.5)
    assert mysin(30) == pytest.approx(0.5, abs=1e-5)

    # Test for sine of 45 degrees (should be 0.70711)
    assert mysin(45) == pytest.approx(0.70711, abs=1e-5)

    # Test for sine of 60 degrees (should be 0.86603)
    assert mysin(60) == pytest.approx(0.86603, abs=1e-5)

    # Test for sine of 0 degrees (should be 0)
    assert mysin(0) == 0

    # Test for sine of 90 degrees (should be 1)
    assert mysin(90) == 1

    # Test for sine of 180 degrees (should be 0)
    assert mysin(180) == 0

# Test the myhaversine function
def test_haversine():
    # Test the haversine function with known coordinates and distances

    # Coordinates of two points: (lat1, lon1) to (lat2, lon2)
    # Use known distances for testing

    # Example 1: Two points with the same coordinates (distance should be 0)
    assert myhaversine((0, 0), (0, 0)) == 0

    # Example 2: Two points 1 degree apart (should be around 111.32 km)
    assert myhaversine((0, 0), (0, 1)) == pytest.approx(111.32, abs=0.01)

    # Example 3: Two points 180 degrees apart (should be around 20,000 km)
    assert myhaversine((0, 0), (0, 180)) == pytest.approx(20000, abs=100)

    # Add more test cases as needed


if __name__ == "__main__":
    pytest.main()
