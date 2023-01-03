#Dictionary
#3. Write a Python program to concatenate following dictionaries to create a new one.
'''
user1 ={
    'name':'arun',
    'age':25
}
user2 ={
    'name':'varun',
    'age':35
}

users=user1+user2
print(users)

'''
d1={"Name":"Ram" , "Age":23}
d2={"City": "Salem", "Gender": "Male"}
d3={"Mark":450}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)