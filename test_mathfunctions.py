import math
import myfunctions

#using other tests! improve this functions with a loop.  

# test mysqrt function by comparing with the math function 
print("First test mysqrt: 9")
print(math.sqrt(9))
print(myfunctions.mysqrt(9))

print("Second test mysqrt: 0")
print(math.sqrt(0))
print(myfunctions.mysqrt(0))

print("Third test mysqrt: -9")
try:
    print(math.sqrt(-9))
    print(myfunctions.mysqrt(-9))
except ValueError:
    print("ValueError")

# test mysin function by comparing with the math function 
print("First test mysin: 90")
print(math.sin(90))
print(myfunctions.mysin(90))

print("Second test mysin: 0")
print(math.sin(0))
print(myfunctions.mysin(0))

print("Third test mysin: -90")
print(math.sin(-90))
print(myfunctions.mysin(-90))

# test mycos function by comparing with the math function 
print("First test mycos: 90")
print(math.cos(90))
print(myfunctions.mycos(90))

print("Second test mycos: 0")
print(math.cos(0))
print(myfunctions.mycos(0))

print("Third test mycos: -90")
print(math.cos(-90))
print(myfunctions.mycos(-90))


