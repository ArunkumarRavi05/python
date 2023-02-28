#List
#5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings
a=['aruna','sams','deen','varuna']
print(a)
ch=0
for w in a:
    if len(w)>1 and w[0]==w[-1]:
        ch+=1
print("Count :",ch)