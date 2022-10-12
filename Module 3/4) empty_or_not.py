wordlist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter a word:"))
    wordlist.append(w)
print(wordlist)

if len(wordlist)==0:
    print('The list is empty.')
else:
    print('The list is not empty.')