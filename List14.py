#List
#14. Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30
a=30
c=[]
for i in range(1,a+1,1):
    b=i*i
    c.append(b)
print(c)
print(c[:5])
print(c[-5:])

'''
l = list()
for i in range(11,25):
	l.append(i**2)
print(l[:5])
print(l[-5:])'''