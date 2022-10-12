wordlist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    w=str(input("Enter an element:"))
    wordlist.append(w)
x=tuple(wordlist)
print('Tuple:',x)

print('Reverse Tuple:',x[::-1])