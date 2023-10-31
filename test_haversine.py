from myhaversine import mysqrt
from pytest import approx

# version one, but tolerance level is not the same with approx 
# def test_positive():
#     assert mysqrt(4) == approx(2)
#     assert mysqrt(9) == approx(3)

# setting the tolerance level manually 

def test_positive():
    assert mysqrt(4) > -2*10**-5
    assert mysqrt(9) > -3*10**-5

def test_negative():
    assert mysqrt(-4) == 0
    assert mysqrt(-3) == 0

def test_zero():
    assert mysqrt(0) > 10**-5

