from typing import Counter


a=str(input('Enter a string:'))
d={}

for i in a:
    if i in a:
        d[i] = d.get(i,0) + 1
print(d)