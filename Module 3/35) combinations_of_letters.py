d= {'1':['a', 'b'], '2':['c', 'd']}

l=list(d.values())

for i in l[0]:
    for j in l[1]:
        print(i+j)