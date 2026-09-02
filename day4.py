'''
Day-4
concatination:
-->the + will behave two ways for numerics it works normally and for other datatypes like string,list,tuple it will concatinate
operator
-->The operators are used to perform operations on variables and the values.
1.Arthematic operator:
+,-,*,/,//,%
eg:To add the values
'''
num=9
num_2=7
print(num+num_2)
an='python'
of='language'
print(an+of)
any_=[1,2]
how=[3,4]
print(any_+how)
'''
eg:subract two numbers
'''
a=9
b=7
print(a-b)
'''

eg:multiple of two numbers
'''
v=8
n=4
print(v*n)
'''
eg:division two numbers
'''
v=8
n=4
print(v/n)
'''
eg:floor division
'''
v=8
n=4
print(v//n)
v=8.5
n=4.4
print(v/n)
'''
eg:modulous
'''
v=8
n=4
print(v%n)
'''
2.Assignment operator:
=,+=,-=,*=,/=,%=,
eg:+=-->is increment operator
'''
a=0
print(a)
a +=1
print(a)
a=a+1#
loop_cou=0
for j in range(1,100):
    loop_cou+=1
print(loop_cou)
'''
eg:-=-->is decrement operator
'''
b=67
b-=5
print(b)
'''
Eg:*=-->is multi operator
'''
c=7
c*=2
print(c)
'''
eg:/=-->is division operator
'''
c=6
c/=2
print(c)
'''
eg:%=-->is modulous operator
'''
c=8
c%=2
print(c)
'''
3.Comparison operator:
!=,==,>,<,<=,>=
eg:
'''
num=9
num_2=5
print(num!=num_2)#9!=5
print(num==num_2)#9==5
print(num>num_2)#9>5
print(num<num_2)#9<5
'''
eg:2
'''
num=10
num_=9
print(num>=num_2)
print(num<=num_2)
'''
4.Logical operator:
and,or,not
and-->
eg:
'''
num=9
num_2=13
print(num>=num_2 and num<=10)#9>=13 and 9<=10
print(num<=num_2 and num<=10)#9<=13 and 9<=10
'''
or-->
eg:
'''
num=9
num_2=13
print(num>=num_2 or num<10)
'''
not-->
eg:
'''
num=9
num_2=13
print(not(num>=num_2 or num<10))
'''
5.Identity operator:
is,is not
is-->
eg:
'''    
num=45
num_2=45
print(id(num))
print(id(num_2))
print(num is num_2)
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is b)
a=[1,2]
b=[1,2]
print(a==b)
print(a is b)
'''
is not-->
eg:
'''
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is not b)
'''
6.Membership operator:
in,not in
in-->
eg:
'''
nums=[1,2,56,78]
print(2 in nums)
nums_2='python'
print('y' is nums_2)
print('y' not in nums_2)
'''
7.Bitwise operator
'''
