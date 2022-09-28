inp=str(input('Enter a string:'))
j='ly'
i='ing'
x=inp.endswith('ing')
y=inp.replace('ing','ly')

if x==True:
    print(y)
elif len(inp)>=3:
    print(inp+i)
else:
    print(inp)