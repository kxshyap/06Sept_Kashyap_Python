i=1

while i>0:
    try:
        x=int(input('Enter an odd integer: '))
        if x%2==0:
            raise Exception
        i+=1    
    except Exception:
        print(f'Only odd numbers are allowed. {x} is an even number.')
