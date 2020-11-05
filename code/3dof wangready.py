import math

l1 = 13.9
l2 = 14.6

def ik(koordinatx,koordinaty,koordinatz):
    x= koordinatx
    y= koordinaty
    z= koordinatz

    A = (x**2 + y**2 + z**2 - l1**2 - l2**2) /(2*l1*l2)
    B = math.sqrt(1-(A**2))
    tetha3 = math.degrees(math.acos(A))
    
    buff1 = l2*math.cos(tetha3) + l1
    buff2 = math.sqrt(x**2 + y**2)
    buff3 = l2*math.sin(tetha3)

    C = math.degrees(math.atan2(buff2,z))      #z*buff1 + buff2*buff3
    D = math.degrees(math.atan2(buff3,buff1))  #buff1*buff2 - z*buff3
    tetha2 = C - D   #math.degrees(math.atan2(C,D))
    tetha1 = math.degrees(math.atan2(x,y))
    print(tetha1)
    print(tetha2)
    print(tetha3)

ik(5,20,0) #x;z;y