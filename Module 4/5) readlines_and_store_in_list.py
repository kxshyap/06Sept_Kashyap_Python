fl=open('1.txt','w')

n=int(input('Enter no. of lines:'))

for i in range(0,n):
    t=str(input(f'Enter Line {i+1}:'))
    fl.write(f'{t}\n')
fl.close()

fl=open('1.txt','r')
l=fl.readlines()
print(l)

fl.close()