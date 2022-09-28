i1=str(input('Enter 1st string:'))
i2=str(input('Enter 2nd string:'))

"""a=i1[0]
b=i2[0]
"""
s1=i1.replace(i1[0:2],i2[0:2],1)
s2=i2.replace(i2[0:2],i1[0:2],1)
s3=' '
s=s1+s3+s2

print(s)
