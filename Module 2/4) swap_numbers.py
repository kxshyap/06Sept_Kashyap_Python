from tempfile import tempdir


num1=int(input('Enter a number:'))
num2=int(input('Enter a number:'))

print('Before swapping.....')
print(f'A = {num1} \nB = {num2}')
temp=num1
num1=num2
num2=temp
print(f'After swapping.....\nA = {num1} \nB = {num2}')