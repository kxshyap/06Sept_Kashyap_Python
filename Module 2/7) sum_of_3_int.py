num1=int(input('Enter 1st integer:'))
num2=int(input('Enter 2nd integer:'))
num3=int(input('Enter 3rd integer:'))

if num1==num2 or num2==num3 or num3==num1:
    print('The answer is 0')
else:
    sum=num1 + num2 + num3
print(f'The sum is {sum}')
