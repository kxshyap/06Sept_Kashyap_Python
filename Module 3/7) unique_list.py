wordlist=[]
unique_list=[]
n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter a word:"))
    wordlist.append(w)
print(wordlist)

j=0
for j in range(len(wordlist)):
    if wordlist[j] not in unique_list:
        unique_list.append(wordlist[j])
print('Unique List: ',unique_list)
    