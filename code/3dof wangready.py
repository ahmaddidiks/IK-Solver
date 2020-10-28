import math

l1 = 13.9
l2 = 14.6

def ik(koordinatx,koordinaty,koordinatz):
    x= koordinatx
    y= koordinaty
    z= koordinatz

    A = (x**2 + y**2 + z**2 - l1**2) /(2*l1**2)
    B = math.sqrt(1-(A**2))
    tetha3 = math.degrees(math.atan2(B,A))
    buff1 = l2*math.cos(tetha3) + l1
    buff2 = math.sqrt(x**2 + y**2)
    buff3 = l2*math.sin(tetha3)

    C = z*buff1 - buff2*buff2
    D = buff1*buff2 + z*buff3
    tetha2 = math.degrees(math.atan2(C,D))
    tetha1 = math.degrees(math.atan2(x,y))
    print("x : %.2d , y : %.2d , z : %.2d , tetha1 : %.3f , tetha2 : %.3f , tetha1 : %.3f " % (x,y,z,tetha1,tetha2,tetha3))

"""
A= ((x*x)+(y*y)+(z*z)-(L1*L1)-(L2*L2))/(2*L1*L2); 
        B=sqrt(1-(A*A));   
        tetha_3= atan2(B,A);   
        buff_1= (L2*cos(tetha_3))+L1;
        buff_2= sqrt((x*x)+(y*y));  
        buff_3= L2*sin(tetha_3);
        C= (z*buff_1)-(buff_2*buff_3);
        D= (buff_1*buff_2)+(z*buff_3);
        tetha_2=atan2(C,D);
        tetha_1=atan2(x,y);   

"""

ik(1,3,-5)