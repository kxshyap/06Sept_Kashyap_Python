from typing import Counter


fl=open('1.txt','r')

word_list=fl.read().split()

f=Counter(word_list)

print(f)
fl.close()