numlist=[]
unique_list=[]
n=int(input("Enter number of elements:"))

for i in range(n):
    w=int(input("Enter a number:"))
    numlist.append(w)
print(numlist)

j=0
for j in range(len(numlist)):
    if numlist[j] not in unique_list:
        unique_list.append(numlist[j])
print('Unique List: ',unique_list)
    