from math import pi


class Circle:
    r=int(input('Enter radius of circle: '))

    def area(self):
        a=pi*self.r**2
        print('Area of circle: ',round(a,2))
    def perimeter(self):
        p=2*pi*self.r
        print('Perimeter of circle: ',round(p,2))

x=Circle()

x.area()
x.perimeter()
