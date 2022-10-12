varlist=[]
s=[]
n=int(input("Enter number of variables for list:"))
for i in range(n):
    w=str(input('Enter a variable:'))
    varlist.append(w)
print('List:',varlist)

m=str(input('Enter a variable to split:'))

i=varlist.index(m)
print('List 1:',varlist[:i])
print('List 2:',varlist[i:])

