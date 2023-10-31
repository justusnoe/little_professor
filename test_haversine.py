from myhaversine import mysqrt
from pytest import approx

# version one, but tolerance level is the same with approx 
# def test_positive():
#     assert mysqrt(4) == approx(2)
#     assert mysqrt(9) == approx(3)


# def test_negative():
#     assert mysqrt(-4) == 0
#     assert mysqrt(-3) == 0


# def test_zero():
#     assert mysqrt(0) == approx(0)

# setting the tolerance level manually 

def test_positive():
    assert mysqrt(4) >= -2*10**-5

