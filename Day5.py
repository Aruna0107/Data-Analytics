'''
Day-5
input formatting
integer-->int(input())
float-->float(input())
list-->list(input())
list-->1 2 3-->[1,2,3]
tuple-->1 2 3-->(1,2,3)
String-->input()
eg:integer 
'''
num=int(input('enter a five digit of number'))
print(num)
#list
nums=list(map(int,input('enter a some numbers:')))
print(nums)
nums=list(map(int,input('enter a some numbers:').split()))
print(nums)
#map is used to add number of items
#tuple
nums=tuple(map(int,input('enter a some numbers:')))
print(nums)
nums=tuple(map(int,input('enter a some numbers:').split()))
print(nums)
#float
b=float(input("enter any decimal:"))
print(b+7)
#string
so=input('enter a string:')
print(so)
print(type(so))
#eval is used to what you will give it will take like that
data_=eval(input('enter:'))
print(type(data_))


#output formatting
#this normal seperated commas
name='Aruna'
age=21
print('my name is',name,'age is',age)
print('hello!',name)
#fstring
print(f'my name is {name} and i am {age} years old')
#%s->string,%d->digit
print('my name is %s and i am %d years old'%(name,age))

