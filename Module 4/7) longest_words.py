fl=open('1.txt','r')

word_list=fl.read().split()

print(word_list)

max=len(max(word_list,key=len))

for word in word_list:
    if len(word)==max:
        print(word)

fl.close()