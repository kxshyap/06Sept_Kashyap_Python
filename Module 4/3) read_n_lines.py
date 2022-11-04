fl=open('1.txt','w')

for i in range(2,51,2):
    fl.write(f'{str(i)}\n')
fl.close()


fl=open('1.txt','r')

for i in range(1,11):
    fl.readline(i)
    print(i)

fl.close()