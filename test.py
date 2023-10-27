# return square root

def mysqrt(x):
    xmin = 0
    xmax = x
    tol = 0.000001
    mid = (xmin+xmax)/2
    while abs(mid*mid-x)>tol:
        if mid*mid>x:
            xmax=mid
        else: 
            xmin=mid 
        mid = (xmin+xmax)/2
    return mid

print(mysqrt(9))