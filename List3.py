#List
#3. Write a Python program to get the largest number from a list
a = [10,20,56,45,89,67]
t=a[0]
for i in a:
    if i>t:
        t=i
print("The largest number :",t)