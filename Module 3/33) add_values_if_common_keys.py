d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}

d1v=list(d1.values())
d2v=list(d2.values())
d1k=list(d1.keys())
d2k=list(d2.keys())
x=[]
y=[]

i=0

for j in d1k or d2k:
    if d1k[i]==d2k[i]:
        d1v[i]=d1v[i]+d2v[i]
        x.append(d1v[i])
        y.append(d1k[i])
    else:
        x.append(d1v[i])
        y.append(d1k[i])
        x.append(d2v[i])
        y.append(d2k[i])
    i=i+1
d3=dict(zip(y,x))
print(d3)