d1={}

d={0:''}
for i in range(1,15):
    d={i:''}
    d1.update(d)
print(d1.keys())

mk={0:'',4:'',20:''}

for i in mk.keys():
    if i in d1.keys():
        print(f'Yes... {i} exists in d1.')
    else:
        print(f'No.... {i} does not exist in d1.')