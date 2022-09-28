num=int(input('Enter a range:'))
n1=0
n2=1
i=2
if num<=0:
    print('Invalid input.')
elif num==1:
    print(f'Fibonacci series: {n1}')
else:
    print('Fibonacci series:')
    for i in range(num):
        print(n1,end=' ')
        nth=n1+n2
        n1=n2
        n2=nth
        i=i+1

