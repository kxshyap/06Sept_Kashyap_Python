d1={"A":1,"C":3,"D":4,"B":2,"F":6,"E":5}

i=str(input('Enter a key to check:'))

if i in d1.keys():
    print('Yes...')
else:
    print('No...')