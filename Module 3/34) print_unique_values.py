d1={'a':101,'b':102,'c':103,'d':104,'e':105,'f':103}

d1v=list(d1.values())
d2=[]
i=0
for i in range(len(d1v)):
    if d1v[i] not in d1v[i+1:]:
        print(d1v[i])
    else:
        pass
