from subprocess import list2cmdline
from typing import Counter

list_1=[{'item':'item1','amount':400},
{'item':'item2','amount':300},
{'item':'item1','amount':750}]

x = Counter()
for d in list_1:
    x[d['item']]+=d['amount']
print(x)
