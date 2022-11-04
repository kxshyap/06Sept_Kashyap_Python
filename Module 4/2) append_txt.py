fl=open('1.txt','a')
fl.write('\nThis is Python Programming.')
fl.close()

fl=open('1.txt','r')
print(fl.read())
fl.close()