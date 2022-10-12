def perfect(n):
    i=1
    sum=0
    l=[]
    if n>0:
        for i in range(1,n):
            if n%i==0:
                sum=sum+i
                l.append(i)
        if sum==n:
            print(f'{n} is a perfect number.')
            print('List of perfect divisors:',l)
        else:
            print(f'{n} is not a perfect number.')

print(perfect(6))
