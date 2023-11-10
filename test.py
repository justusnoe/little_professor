from myhaversine import myhaversine 

lat1 = 0
lon1 = 0
lat2 = 0
lon2 = 1

expected_distance = 111.32

p1 = lat1,lon1
p2 = lat2,lon2

print(myhaversine(p1,p2))
# actual distance: 112.08399740493165
