'''
Day-8
Tuple
-->Tuple is collection of different datatypes that separated by,and represented by ()
-->it is immutable
-->we can pass a tuple of values that can be asign to the variables, but  should match same number variables and values inside the tuple.
eg:
t=(1,'python',[3,4],(7,9))
print(t[2])
print(t[2][1])
indexing:
--> index()if item is not present in the tuple,it will raise valueerror
eg:
t=(1,'Python',[3,4],(7,9))
print(t.index('python'))
len():
-->
t=(1,'python',[3,4],(7,9))
print(t)
print(len(t))
eg:tuple third point
name,institute,age,batch=('Anu','codegnan',21,6)
print(batch)
print(name)
Max():
-->used to find out the max value from the tuple
eg:
so=(67,5,89,45)
print(max(so))
#it will not find in b/w the int and str
Min():
-->used to find out the least value from the tuple
eg:
so=(67,72,45,2)
print(min(so))
count():
-->used to count an item present in the tuple 
eg:
so=(67,5,89,45,5)
print(so.count())
concate():
eg:
'''
so=(67,5,89,45)
do=(45,89)
print(so+do)

