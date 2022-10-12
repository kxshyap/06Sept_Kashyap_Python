wordlist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter an element:"))
    wordlist.append(w)
print('Required Tuple:',tuple(wordlist))