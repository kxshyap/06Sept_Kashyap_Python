list_1=[]
list_2=[]

n=int(input("Enter number of elements:"))

print('List 1')

for i in range(n):
    w=str(input("Enter a word:"))
    list_1.append(w)
print(list_1)

print('List 2')

for j in range(n):
    w=str(input("Enter a word:"))
    list_2.append(w)
print(list_2)

for k in range(n):
    if list_1[k] in list_2:
        print('True')
        break
        