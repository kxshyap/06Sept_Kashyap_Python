numlist=[]
s=[]

n=int(input("Enter number of elements for numlist:"))
for i in range(n):
    w=int(input("Enter a number:"))
    numlist.append(w)
print('List:',numlist)

m=int(input("Enter number of elements for sublist:"))
for j in range(m):
    w=int(input("Enter a number:"))
    s.append(w)
print('Sublist:',s)

if s==[]:
    print('List contains Sublist.')
elif s==numlist:
    print('List contains Sublist.')
elif len(s)>len(numlist):
    print('Sublist cannot be bigger than List.')
else:
    for i in range(n):
        if s[0]==numlist[i]:
            count=1
            while count<m and s[count]==numlist[i+count]:
                count=count+1
            if count==len(s):
                print('List contains Sublist.')
            else:   
                print('List does not contain Sublist.')
