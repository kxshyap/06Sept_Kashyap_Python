w=str(input("Enter a string:"))
s1=0
s=w.split()
i=0
temp=[]
for i in s:
    s1=s.count(i)
    i+=1
    print(i,'\t-',s1)
