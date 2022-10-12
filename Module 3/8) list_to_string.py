wordlist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter a word:"))
    wordlist.append(w)
print('List of words:',wordlist)

s=''
for i in range(n):
    s=s + wordlist[i] + ' '
print('Strings:',s)