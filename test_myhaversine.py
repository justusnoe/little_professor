from myfunctions import mysqrt, mycos, myarcsin, mysin, get_decimal,deg2rad

# Define constants for Earth's radius
EARTH_RADIUS_KM = 6371  # Earth's mean radius in kilometers

def main():
    # Input coordinates from the user
    lat1 = get_decimal('Latitude 1st point in decimal degrees', -90, 90)
    lon1 = get_decimal('Longitude 1st point in decimal degrees', -180, 180)
    lat2 = get_decimal('Latitude 2nd point in decimal degrees', -90, 90)
    lon2 = get_decimal('Longitude 2nd point in decimal degrees', -180, 180)

    # Calculate the distance using the haversine formula
    haversine_distance = haversine((lat1, lon1), (lat2, lon2))
    
    print(f"The distance between points is {haversine_distance} km")

# Haversine formula for calculating great-circle distances between two points
def haversine(p1, p2):
    lat1, lon1 = p1  # degrees
    lat2, lon2 = p2

    # Convert degrees to radians for trigonometric calculations
    lat1, lon1, lat2, lon2 = map(deg2rad, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (mysin(dlat / 2) ** 2) + mycos(lat1) * mycos(lat2) * (mysin(dlon / 2) ** 2)
    c = 2 * myarcsin(min(1, mysqrt(a)))  # Compute angular distance
    distance = EARTH_RADIUS_KM * c  # Calculate distance in kilometers
    return distance

# Your updated auxiliary functions go here

if __name__ == "__main__":
    main()
