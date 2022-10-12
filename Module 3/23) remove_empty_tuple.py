a=[(1,2,3,4,5),(),(60,70,80,90),(),(100,200,300)]

i=0

while i<len(a):
    if len(a[i])==0:
        a.remove(a[i])
    i=i+1
print(a)