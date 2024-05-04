ditr = {
    'mehrshad': '12345',
    'hamta': '56789'
}
enterUserName = input(str('entry your user name :  '))
enterPassword = input(str('entry your Password :  '))
x = enterUserName

while enterUserName not in ditr or ditr[enterUserName] != enterPassword:
    print('your user or password is wrong')
    enterUserName = input('entry again your user name :  ')
    enterPassword = input('entry again your Password :  ')
else:
    print("welcome", x)
