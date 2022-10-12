l=int(input('Enter lower limit:'))
u=int(input('Enter upper limit:'))

i=l
for i in range(l,u+1):
    if i<=l+4 or i>=u-4:
        s=i**2
        print(f'{i}\t-->\t{s}')