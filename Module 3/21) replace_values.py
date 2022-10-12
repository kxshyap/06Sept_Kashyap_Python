list1=[(10,20,30),(40,50,60),(70,80,90)]
print('Originial List:',list1)

for i in range(len(list1)):
    list2=list(list1[i])
    list2[-1]=101
    list1[i]=tuple(list2)
print('Changed List',list1)