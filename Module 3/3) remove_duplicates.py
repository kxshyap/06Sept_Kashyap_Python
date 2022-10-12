wordlist=[]
original=[]
n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter a word:"))
    wordlist.append(w)
print(wordlist)

j=0
for j in range(len(wordlist)):
    if wordlist[j] not in original:
        original.append(wordlist[j])
print(original)
    