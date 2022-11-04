fl=open('1.txt','r')
fc=open('2.txt','w')

for i in fl:
    fc.write(i)

fl.close()
fc.close()