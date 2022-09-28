inp=str(input('Enter a string:'))

x = inp.find('not poor')


if x>0:
    y=inp.replace('not poor','good',1)
    print(f'"not poor" appears at index {x}.')
    print('Resulting String:',y)
else:
    print('The word "not" dose not follow the word "poor".')