from myhaversine import myhaversine 
from haversine import haversine


lat1 = 0
lon1 = 0
lat2 =90
lon2 = 0

p1 = lat1,lon1
p2 = lat2,lon2

print(myhaversine(p1,p2))
# actual distance: 112.08399740493165
print(haversine(p1,p2))
