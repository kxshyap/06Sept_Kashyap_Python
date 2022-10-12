wordlist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter a word:"))
    wordlist.append(w)
print(wordlist)

count=0
for j in wordlist:
    if len(j)>=2 and j[0]==j[-1]:
        count+=1
print('No. of strings with given condition:',count)
