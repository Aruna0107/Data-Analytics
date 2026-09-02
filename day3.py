'''Day-3:
Interduction to Data Types & Type conversions:
-->Data Types
1.Numeric Datatype
-->Float and Integer is called as numeric datatype
-->Float:
-->A Number which contains Decimal values,we call it as a float datatype
eg:
price=56.89
-->integer(int):
-->A Normal Number without any Decimal values
eg:
num=89
num_2=6
2.String
-->String is a sequence of characters that are enclosed in ' '," ",""" """.
-->String is a immutable
eg
any_='Python is a Language'
all_='Ab,.&[)-+'
3.List
-->List is collection of different Datatypes
-->and it is represented by [] that are separated by comma(,).
-->Inside the List we call it as items
-->list is a mutable
Eg:
'''
any_=[1,'python',3,6]
for item in any_:
    print(item)
any_=[1,'python',[5,6]]
print(type(any_))
'''
4.Tuple
-->tuple is collection of different datatypes that are enclosed in() and those are seperated by comma(,).
-->tuple is immutable
eg:
'''
data_=[1,2,3]
all_=(1,2,3)
print(type(data_))
print(type(all_))
nums=(1,89.67,'python',[3,4],(8,9))
print(nums)
'''
5.Dictionary
-->Dictionary is a collection of Key:value pairs, key and values are seperated by colon(:).
-->key and value pair is call it as a item
-->and this items are seperated by a comma(,)
-->Dictionary is represented using {}
-->In key place we can use immutable datatypes
-->in values place we can use any datatype
eg:
'''
data_={1:2,'name':'aruna',
       (2,3):'tuple'}
print(data_)
'''
6.Set
-->set is collection unique elements and set can't allow any duoplecate values inside it
-->set is represented by {} and the elements are separated by comma(,)
eg:
'''
an={1,2,3}
print(an)
'''
'''
'''
Type conversion
-->float-->int,str
eg-->int(),str()
-->str()
'''
price=45.78
print(str(price))
con=str(price)
print(type(con))
'''
eg:
-->int()
'''
price=56
print(int(price))
'''
-->float()
'''
price=67
print(float(price))
'''
-->str()
'''
num=78
con_=str(num)
print(type(con_))
'''
string-->int,float
'''
do='1234'
print(int(do))
do='10.89'
print(float(do))
'''
list-->tuple,string
eg-->tuple()
'''
nums=[1,2,3,4]
print(tuple(nums))
'''
-->str()
tuple-->list,set
eg-->list()
'''
all_=(5,6,7)
print(list(all_))
'''
set-->tuple,list
eg-->tuple()
'''
all_={5,6,7}
print(tuple(all_))
'''
dictionary-->list
eg-->dict()
'''
details=[('name','teja'),('edu','b.tech')]
print(dict(details))
'''
{(key,value),()}
'''



