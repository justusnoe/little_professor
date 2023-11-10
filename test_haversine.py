from myfunctions import mysqrt, mycos, myarcsin, mysin
from myhaversine import myhaversine
from pytest import approx


# testing mysqrt  
# tolerance level can be set with approx
def test_mysqrt_positive():
    assert mysqrt(4) == approx(2, abs=10**-5)
    assert mysqrt(9) == approx(3, abs=10**-5)

def test_mysqrt_negative():
    assert mysqrt(-4) == 0
    assert mysqrt(-3) == 0

def test_mysqrt_zero():
    assert mysqrt(0) > 10**-5


# testing mycos 
def test_mycos_positve(): 
    assert mycos(90) == 0
    assert mycos(180) == -1
    assert mycos(360) == 1  

def test_mycos_negative():
    assert mycos(-90) == 0
    assert mycos(-180) == -1
    assert mycos(-360) == 1

def test_mycos_zero():
    assert mycos(0) == 1

# testing myarcsin 
def test_myarcsin():
    assert myarcsin(0) == 0
    assert myarcsin(1) == 90
    assert myarcsin(-1) == -90

# testing mysin 
def test_mysin_positive():
    assert mysin(90) == 1 
    assert mysin(180) == 0
    assert mysin(360) == 0  

def test_mysin_negative():
    assert mysin(-90) == -1 
    assert mysin(-180) == 0
    assert mysin(-360) == 0

def test_mysin_zero():
    assert mysin(0) == 0

# test myhaversine
# Q: how to test corner cases? pole - equator 
# Q: how to adapt 

lat1 = 45.7597
lon1 = 4.8422

lat2 = 48.8567
lon2 = 2.3508

p1 = lat1,lon1
p2 = lat2,lon2

def test_myhaversine(): 
    assert myhaversine(p1,p2) == approx(392.446, abs=0.1)


    