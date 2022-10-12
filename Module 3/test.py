def account1(name,acno,actyp):
    print('Name:',name)
    print('Account no:',acno)
    print('Account type:',actyp)

def deposit(de):
    de=int(input('Enter deposit amount:'))
    return de

def withdraw(wd):
    wd=int(input('Enter withdraw amount:'))
    return wd

x=deposit(2000)
y=withdraw(1500)

def statement():
    account1('Kashyap',12345,'Current')
    print(f'Bank balance: Rs. {(x-y)}')

statement()