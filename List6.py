#List
#6. Write a Python program to remove duplicates from a list
a=[10,20,30,10,20]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)