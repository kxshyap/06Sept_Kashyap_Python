d1={'a':45,'b':98,'c':101,'d':29,'e':85,'f':56}

print("Given Dictionary:\n",d1)
print('Dictionary with 3 highest values:')
print('Keys : Values')

d=dict()
dv=list(d1.values())

dv.sort(reverse=True)
dv1=dv[:3]

for i in dv1:
    for j in d1.keys():
        if d1[j]==i:
            print(f'{j}    : {d1[j]}')








