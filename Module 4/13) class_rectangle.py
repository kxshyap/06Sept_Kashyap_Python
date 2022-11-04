class Rectangle:
    l=int(input('Enter length of rectangle:'))
    w=int(input('Enter width of rectangle:'))

    def area(self):
        a=self.l*self.w
        print('Area of rectangle: ',a)


x=Rectangle()
x.area()
