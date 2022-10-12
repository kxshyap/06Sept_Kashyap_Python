def inrange(a,b,n):
    if n in range(a,b):
        print(f'{n} is in range{(a,b)}.')
    else:
        print(f'{n} is not in range{(a,b)}.')


print(inrange(10,20,18))