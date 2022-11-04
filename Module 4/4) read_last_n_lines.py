fl=open('1.txt','w')
a=2
b=101
c=2
for i in range(a,b,c):
    fl.write(f'{str(i)}\n')
fl.close()


fl=open('1.txt','r')
n=int(input('Enter last n lines:'))
i=a=100

for i in range(a,a-n,-1):
    fl.readline(i)
    print(i)
fl.close()