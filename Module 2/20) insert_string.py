i=str(input('Enter your string:'))
j=str(input('Enter a string to insert:'))
x=int(input('Enter the index:'))

beg_str=i[:x]
end_str=i[x:]

insert_str=beg_str+j+end_str


print('New String:',insert_str)
