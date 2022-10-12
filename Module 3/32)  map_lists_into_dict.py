keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))

print("For keys:")
for x in range(0,n):
    element=str(input(f'Enter element {x+1}:'))
    keys.append(element)

print("For values:")
for x in range(0,n):
    element=int(input(f'Enter element {x+1}:'))
    values.append(element)

d=dict(zip(keys,values))
print("The dictionary is:",d)