w=str(input("Enter a string:"))



s=w.split()
max=0
temp=0

for i in s:
    if len(i)>max:
        max=len(i)
        temp=i 
print(f'The length of longest word in the string: {temp} - {max}')



"""n=int(input("Number of words:"))

for i in range(n):
    w=input("Enter a word:")
    wordlist.append(w)

print(wordlist)

for j in wordlist:
    a=
    print(a)"""