'''
Day-11
elif:
-->elif statement is used to check more possible outcome or more conditions
eg:
a=90
b=780
c=670
if a>b and a>c:#90>780 and 90>67
    print(a)
elif b>a and b>c:#780>90 and 780>670
    print(b)
else:
    print(c)
eg:
num=7
num_2=3
user_opt=int(input("enter \n1.add \n2.sub \n3.mul \n4.pow:"))
if user_opt==1:
     print(num+num_2)
elif user_opt==2:
    print(num-num_2)
elif user_opt:
    print(num*num_2)
else:
    print(num**num_2)


nested if
-->if insidean if statement is called nested if
eg:
app_details={'pin':1234}
import random
user_pass =int(input("enter your app password:"))
otp=random.randint(a=1000,b=9999)
if user_pass==app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp=int(input("enter 4 digit otp:"))
    if user_otp==otp:
        print('welcome to the app')
    else:
        print('incorrect otp')
else:
    print('password is incorrect')
eg:
a=int(input('enter a number'))
if a%2==0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

eg:
'''
marks_=int(input("enter a marks"))
if marks_>=90:
    print("A+")
elif marks_>=80:
    print("A")
elif marks_>=70:
    print("B+")
elif marks_>=60:
    print("B")
elif marks_>=50:
    print("C+")
elif marks_>=40:
    print("C")
else:
    print(fail)
