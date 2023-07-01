first = input('first name: ')
last = input('last name: ')
print('your name is '+first +last)

name = input('your input: ')
print('capitalized: '+name.upper())

num= int(input('input a number:'))
print('squared num: '+num**2 )

for i in range(3, 13, 1):
    print (i)

n= int(input('input a number: '))
for i in range(0,n+1,1):
    print(i)

a= int(input('number: '))
if a > 13:
    print('this number is larger than 13')
else:
    print('this number isnt larger than 13')

a= int(input('number: '))
if a%2 == 0:
    print('this number is even')
else:
    print('this number is not even')

username = input('username: ')
password= input('pass: ')
email= input('email: ')
print('Registered successfully.')

print('== Registration ==')
username = input('username: ')
password= input('pass: ')
re_pass= input('re enter your pass word: ')
if re_pass == password:
    print(input('email: '))
    print('Registered successfully.')
else:
    print('Passwords not match. Please input again.')

