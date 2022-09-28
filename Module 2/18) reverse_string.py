i=str(input('Enter your string:'))

if len(i)%4==0:
    j=i[::-1]
    print(j)
else:
    print('String Length is not a multiple of 4.')

