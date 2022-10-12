def fac(n):
    fac=1
    if n==0:
        fac=1
        print(f'{n}! = {fac}')
    elif n>0:
        for i in range(1,n + 1):
            fac=fac*i
    print(f'{n}! = {fac}')


print(fac(18))

