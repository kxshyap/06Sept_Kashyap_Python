fl=open('1.txt','w')

l=['Jan','Feb','Mar','Apr','May','Jun','Jul','Sep','Oct','Nov','Dec']

fl.write('******************')
fl.write('\n')
for i in l:
    fl.write(f'{i}\n')
fl.write('******************')
fl.close()
