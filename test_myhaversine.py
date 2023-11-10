from myfunctions import mysqrt, mycos, mysin, get_decimal, deg2rad

def main():
    lat1 = get_decimal('Latitude 1st point in decimal degrees', -90, 90)
    lon1 = get_decimal('Longitude 1st point in decimal degrees', -180, 180)
    lat2 = get_decimal('Latitude 2nd point in decimal degrees', -90, 90)
    lon2 = get_decimal('Longitude 2nd point in decimal degrees', -180, 180)
    print(f"The distance between points is {myhaversine((lat1, lon1), (lat2, lon2))} km")

def myhaversine(p1, p2):
    R = 6371
    lat1, lon1 = p1
    lat2, lon2 = p2
    A = mysin((lat2 - lat1) / 2)
    B = mysin((lon2 - lon1) / 2)
    C = 2 * A**2 * mycos(lat1) * mycos(lat2) * B**2  # Simplify the expression
    C = max(0, C)  # Ensure C is non-negative
    H = mysqrt(C)
    H = max(-1, min(1, H))  # Ensure H is between -1 and 1
    return 2 * R * deg2rad(myarcsin(H))

if __name__ == "__main":
    main()
