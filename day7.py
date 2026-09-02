'''
Day-7
LIST
-->collection of different datatypes that seperated by, and it is represented by[]
INDEXING:
positive indexing:
-->
negative indexing:
eg:
so=[1,2,3,4,'python']
print(so[4])
print(so[4][2])
print(so[4][-1])
print(so[-1][-3])
all_=[12,[1,'python',[1,4],(78,[6,7])],['java',78]]
print(all_[1][3][1])
print(all_[1])
data_=['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(data_[1][2][1][2])
len()
-->the function is used to find the number of items present inside list
syntax:-->len(variable_name)
eg:
data_=['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(len(data_[1][2]))
slicing
-->
eg:
data_=[1,2,3,4,5,6,7]
print(data_[2:6])
Eg:
a=[1,2]
b=[3,4]
print(a+b)
METHODS:
append()
-->append method will add new items into the list at last index position
syntax:-->variable_name.append(item)
eg:
go=[1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)
#list is mutable means we can modify permantly
extend()
-->extend() will add the items into a list at last index position,but it will give each value as one index inside
syntax-->variable_name.extend(items)
eg:
go=[1,2]
go.append(9)
print(go)
go=[1,2]
go.extend(9)
print(go)
#int is not iterable
eg:
go=[1,2]
go.extend('python')
print(go)
go=[1,2]
go.extend([3,[3,4]])
print(go)
#str is iterable
POP()
-->POP() is used to remove items from the list and it will delete based on the index position
syntax-->variable_name.pop(index_position)
eg:
m=[5,1,2,3,4,'python']
m.pop(5)
print(m)
remove()
-->it will delete items based on the value given init 
syntax-->variable_name.remove(value)
eg
m=[5,1,2,3,4,'python']
m.remove(5)
print(m)
