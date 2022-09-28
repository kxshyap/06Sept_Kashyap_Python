s=str(input("Enter a string:"))

s1=s[:2] # First 2 Characters
s2=s[-2:] # Last 2 Characters
s3=s1+s2

if len(s)<2:
    print('Output is not possible.')
else:
    print('Result:',s3)

