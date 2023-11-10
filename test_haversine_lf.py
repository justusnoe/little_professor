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
def test_myhaversine():
    # Replace these with actual latitude and longitude values
    lat1 = 0
    lon1 = 0
    lat2 = 0
    lon2 = 1

    # Expected distance using the haversine formula
    expected_distance = 111.32  # Approximately 111.32 km for a 1-degree difference in longitude

    # Calculate the distance using myhaversine
    distance = myhaversine((lat1, lon1), (lat2, lon2))

    # Check if the distance is within 100 meters of the expected distance
    assert abs(distance - expected_distance) < 0.1  # 100 meters in kilometers

if __name__ == "__main__":
    pytest.main()
