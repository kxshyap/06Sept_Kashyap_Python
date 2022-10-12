from math import pi


def cylinder(r,h):
    vol=round(pi*r**2*h,2)
    area=round((2*pi*r*h)+(2*pi*r**2),2)
    print('Volume of Cylinder:',vol)
    print('Surface area of Cylinder:',area)

print(cylinder(20,50))