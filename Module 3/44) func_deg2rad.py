from cmath import pi


def deg2rad(d):
    r=d*pi/180
    print(f'{d} Degrees = {round(r,4)} Radians:')

print(deg2rad(45))