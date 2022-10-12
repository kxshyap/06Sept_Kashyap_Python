numlist=[]

n=int(input("Enter number of elements:"))
sum=0
for i in range(n):
    ele=int(input("Enter a number:"))
    sum+=ele
    numlist.append(ele)
print(numlist)

print(f'Largest Number: \t{max(numlist)}')
print(f'Smallest Number:\t{min(numlist)}')
print(f'Sum of all elements:\t{sum}')

