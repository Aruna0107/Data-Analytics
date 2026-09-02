'''
Day-6
Strings:
eg:'python','890'
operations:
1.Indexing
-->Indexing is to get the character that you are looking to access
types
1.postive indexing starts from 0 index
syntax-->print(variable_name[index_position])
eg:text='python'
print(text[3])
2.negative indexing starts from -1 index
syntax-->print(variable_name[negative index_position])
eg:text='python'
print(text[-1])
print(text[-2])
eg:txt='python is a programming language'
print(txt[-15])
print(txt[17])
len()
-->len() is built-in function that is used to get number of character present in the string
syntax:len(variable_name)
eg:
txt='python is a programming language'
print(len(txt))
print(txt[17])

2.Slicing
-->the slicing is used to access the particular part from the string
syntax-->variable_name[start:end]
eg:
txt='python is a programing language'
print(txt[12:23])
print(txt[12:])
print(txt[:23]
#txt=madam'
#rev=txt[::-1]
3.upper
-->used to convert all small char into cap
Eg:
txt='python is a programming language'
print(txt.upper())
4.lower()
-->used to convert all cap into small
eg:
txt='Python'
print(txt.lower())
EG:
name='Aruna'
user_name=input('enter user_name:').lower()
if user_name==name:
    print('user_name')
else:
    print('invalid')
5.index()
-->used to know the index position of an char
syntax-->variable_name.index('substring',start,end)
eg:
txt='python is a programming language'
print(txt.index('i'))
print(txt[7])
print(txt.index('i',9,18))
print(txt.index('i',-9,-18))
6.Replace()
-->used to replace old substring with new substring
syntax-->variable_name.replace(old,new)
eg:
txt='python is a programming language'
print(txt.replace('python','java'))

7.split()
-->this method is  used to seperate the string based on given substring
syntax-->variable_name.split(substring)
eg:
txt='python is a programming language'
print(txt.split(' '))
print(txt.split(' a '))
8.count()
-->used to count number of occurrences of an substring
syntax-->variable_name.count('substring')
eg:
txt='python is a programming language'
print(txt.count('a',1,12))






