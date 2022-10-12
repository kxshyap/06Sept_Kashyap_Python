import random

wordlist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter a word:"))
    wordlist.append(w)
print('List of words:',wordlist)

a=random.randint(0,n)

print('Random item from list:',wordlist[a])