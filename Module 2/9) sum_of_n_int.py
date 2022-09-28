num=int(input('Enter a positive integer:'))
i=1
sum=0
if num==0:
    print('Input is 0.')    
if num<0:
    print('Input is negative.')
if num>0:
    print('Input is positive.')
    while i<=num:
        sum=sum+i
        i=i+1
    print(f'The sum of 1 to {num} is {sum}.')