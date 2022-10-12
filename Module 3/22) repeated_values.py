a=(1,2,'kashyap',3,4,5,1,'kashyap')

for i in range(len(a)):
    if a[i] in a[i+1:]:
        print(a[i])