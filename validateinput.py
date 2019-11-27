while True:
    print('Enter your age :')
    age =input()
    if age.isdecimal():
        break
    print('please age')

while True:
    print('Select a new password(letters and number only) : ')
    password = input()
    if password.isalnum():
        break
    print('password can only have letters and numbers')
