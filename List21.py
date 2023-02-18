#List
#21. Write a python program to check whether two lists are circularly identical
list1 = [8, 8, 12, 12, 8]
list2 = [8, 8, 8, 12, 12]
print(''.join(map(str,list1)) in ''.join(map(str,list2 *2)))