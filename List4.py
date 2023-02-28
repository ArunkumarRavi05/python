#List
#4. Write a Python program to get the smallest number from a list
a = [10,20,5,45,89,67]
t=a[0]
for i in a:
    if i<t:
        t=i
print("The largest number :",t)