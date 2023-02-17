#List
#25. Write a Python program to get the frequency of the elements in a list.
a=[10,200,30,400,550,10,20,30]
print(a)
print(a.count(10))

'''
import collections
l = [10,30,50,10,20,60,20,60,40,40,50,50,30]
print("Original List : ",l)
f = collections.Counter(l)
print("Frequency of the Elements: ",f)
 

Output

Original List :  [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]
Frequency of the Elements:  Counter({50: 3, 10: 2, 30: 2, 20: 2, 60: 2, 40: 2})
'''