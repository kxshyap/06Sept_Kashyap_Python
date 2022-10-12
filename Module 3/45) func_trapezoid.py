def trapezoid(a,b,h):
    if (a or b or h)>0:
        area=round(((a+b)/2)*h,2)
    print('Area:',area)


print(trapezoid(12,10,15))