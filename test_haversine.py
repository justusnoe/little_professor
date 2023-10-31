from myhaversine import mysqrt, mycos
from pytest import approx

# testing mysqrt function 
# tolerance level can set with approx
def test_positive():
    assert mysqrt(4) == approx(2, abs=10**-5)
    assert mysqrt(9) == approx(3, abs=10**-5)

def test_negative():
    assert mysqrt(-4) == 0
    assert mysqrt(-3) == 0

def test_zero():
    assert mysqrt(0) > 10**-5


# testing mycos 
def test_mycos(): 
    assert mycos(0) == 1
    assert mycos(90) == 0
    assert mycos(180) == -1
    assert mycos(360) == 1  


