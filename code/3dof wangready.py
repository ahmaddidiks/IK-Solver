import math

l1 = 13.9
l2 = 14.6

def ik(koordinatx,koordinaty,koordinatz):
    x= koordinatx
    y= koordinaty
    z= koordinatz

    A = x**2 + y**2 + z**2 - (l1**2/(2*l1**2))
    B = math.sqrt(1-(A**2))
    tetha3 = math.atan2(B,A)
    buff1 = l2*math.cos(tetha3) + l1
    buff2 = math.sqrt(x**2 + y**2)
    buff3 = l2*math.sin(tetha3)

    C = z*buff1 - buff2*buff2
    D = buff1*buff2 + z*buff3
    tetha2 = math.atan2(C,D)
    tetha1 = math.atan2(x,y)

    print("x : %03f , y : %03f , z : %03f , tetha1 : %03f , tetha2 : %03f , tetha1 : %03f " % x,y,z,tetha1,tetha2,tetha3)

ik(1,3,-5)