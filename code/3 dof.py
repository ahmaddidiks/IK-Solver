import math
#import numpy as np
#from uncertainties import ufloat

x = 10
y = 0.00
z = 10.00
l1 = 13.9
l2 = 14.6

#perhitungan Tetha2
hit = (pow(y,2) + pow(z,2) - pow(l1,2) - pow(l2,2))/2*l1*l2
cosTetha2 = math.cos(hit)
sinTetha2 = math.sqrt(1-cosTetha2**2)
Tetha2 = math.degrees(math.atan2(sinTetha2,cosTetha2))

#perhitungan Tetha1
k1 = l1+l2*cosTetha2
k2 = l2*sinTetha2
Tetha1 = math.degrees(math.atan2(z,y) - math.atan2(k2,k1))

#perhitungan sudut x
xDeg = math.degree(math.atan2(x, y))
print(Tetha1)
print(Tetha2)
print(xDeg)





