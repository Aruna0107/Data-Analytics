'''
day-10
DICTIONARY
-->DICT is a collection of key : value pair
-->key must be unique and it should be immutable datatype(int,str,tuple)
-->dict is represented in {}
eg:
details={1:2,'name':'anu',(1,2):[1,2]}
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y'}
print(data_['adr'])

1.Accessing:-
-->dict can access by calling key,we will get value from that key
syntax->dict['key']
get():
-->get() method is also used to get the value from that key
syntax:->dict.get(key)
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_['adr'])
print(data_.get('panc'))
print(data_.get(2))
eg:
update:
-->update() method is used to update a key,incase if the key is not present inside dict then it add that key:value
syntax-->dict.update({key:value})
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_)
data_.update({'name':'anu'})
data_.update({'atmpin':4567})
print(data_)

-->there is another way to update a key
syntax-->dict[key]=value
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_)
data_['name']='aruna'#it is used to change the value
print(data_)
data_['ac']=123456789#ac is not there it will create the key value pair
print(data_)

values():
-->values() method  is used to get all the values from the dict
syntax-->dict.values()#it is used to get the values from the dict
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_.values())

keys():
-->keys() method is used to get all the keys from the dict  
syntax-->dict.keys()#it is used to get the keys from the dict
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_.keys())

items():
-->item() method will get the key:value pair seperated from the dict
syntax-->dict.items()
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_.items())

clear():
-->clear() method is used to delete the all data from the dict
syntax:->dict.clear()
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_)
data_.clear()
print(data_)

del():
-->del() method is used to delete the particular key:value  data from the dict
syntax:->dict.clear()
eg:
data_={'name':'anu',
       'balance':7000,
       'adr':123456789012,
       'panc':'GPXBP890Y',
       2:[3,4]}
print(data_)
del data_['adr']
print(data_)


statements:
conditions
If:
-->if condition become true,then it will execute inside block of code
eg:
age=15
if age>=18:
    print('eligible to vote')
-->incase it becomes false, then it will never entry inside block
eg:
age=19
if age>=18:
    print('eligible to vote')
eg:
a=90
b=78
if a>b:
    print(a)


if-else:
-->else for if statement is a fall-back statement,incase if condition is false then else block will execute
eg:
age=15
if age>=18:
    print(f'your {age} eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')
eg:
'''
a=90
b=780
if a>b:
    print(a)
else:
    print(b)

