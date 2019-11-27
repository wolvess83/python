spam = 'hello'
print(spam.isalpha)
spam = 'hello123'
print(spam.isalpha) #only 문자

spam = 'hello'
print(spam.isalnum)#only 문자 or 숫자

spam = '123'
print(spam.isdecimal)
spam = 'hello'
print(spam.decimal)#only 숫자

spam = 'hello'
print(spam.isspace)
spam = '234'
print(spam.isspace)

spam = 'hello'
print(spam.istitle)
spam = 'Hello'
print(spam.istitle) #첫번째 문자 대문자고 나머지 소문자면  True
      