from myfunctions import mysqrt, mycos, myarcsin, mysin
from myhaversine import myhaversine
from pytest import approx


# testing mysqrt  
# tolerance level can be set with approx
def test_mysqrt_positive():
    assert mysqrt(4) == approx(2, abs=10**-10)
    assert mysqrt(9) == approx(3, abs=10**-10)

def test_mysqrt_negative():
    assert mysqrt(-4) == ValueError
    assert mysqrt(-3) == ValueError

def test_mysqrt_zero():
    assert mysqrt(0) == 0


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

# test myhaversine with the distance from pole to equator 

lat1 = 0
lon1 = 0

lat2 =90
lon2 = 0

p1 = lat1,lon1
p2 = lat2,lon2

expected_value = 10007.55722101796 #haversine function 

def test_myhaversine(): 
    assert myhaversine(p1,p2) == approx(expected_value, abs = 0.1)


    