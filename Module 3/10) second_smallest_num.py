numlist=[]
diff=[]
diff1=[]
n=int(input("Enter number of elements:"))

for i in range(n):
    w=int(input("Enter a number:"))
    numlist.append(w)
print('List of numbers:',numlist)

numlist.sort()
print('Second smallest no.:',numlist[1])