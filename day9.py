'''
Set:
-->Set is a unordered collection of elements
-->no duplicate allowed in the set
-->set is represented by {}
eg:
nums={1,2,3,2}
print(nums)


operations:
1.UNION():
-->the union() will combine two set and into a single set
syntax-->set_1.union(set_2) or set_1|set_2
eg:
data_={1,2,3,4}
nums={5,6}
print(data_.union(nums))
eg:
data_={1,2,3,4}
nums={5,6}
print(data_|nums)
2.INTERSECTION():
-->this will gives us the common elements from both sets
syntax-->set_1.intersection(set_2) or set_1 & set_2
EG:
data_={1,2,3,4}
nums={4,5,6}
print(data_.intersection(nums))
print(data_& nums)

3.DIFFERENCE():
-->it will display the different elements from set_1, but not the set_2 elements
syntax-->set_1.difference(set_2) or set_1 - set_2
EG:
data_={1,2,3,4}
nums={4,5,6}
print(nums.difference(data_))
print(nums-datya_)
4.SYMMETRIC_DIFFERENCE():
-->difference elements from the both
syntax-->set_1.symmetric_difference(set_2) or set_1^set_2
EG:
data_={1,2,3,4}
nums={4,5,6}
print(nums^data_)
print(data_.symmetric_difference(nums))
5.ADD():
-->ADD() method will add only one element at a time
syntax-->set.add(element)
eg:
data_={1,2,3,4}
print(data_)
data_.add(7)
print(data_)
6.UPDATE:
-->we can add more than one elements by using update method
syntax-->set.update([elements])or set_1.update(set_2)
eg:
data_={1,2,3,4}
nums={4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)
7.REMOVE():
-->remove() method will del the given element from the set
-->if the element is not present in the set, it will raise error
syntax-->set.remove(element)
eg:
data_={1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)
8.DISCARD():
-->the method is used to delete the elements from the set,but never raise any error even the element not inside set
syntax-->set.discard(element)
EG:
data_={1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)
9.CLEAR():
-->the method is used to delete all elements from the set it will written empty set
syntax-->set.clear()
EG:
data_={1,2,3,4}
print(data_)
data_.clear()
print(data_)
