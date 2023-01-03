#Dictionary
#5. Write a Python program to iterate over dictionaries using for loops.
users ={
    'user1': {
        'name':'Arun',
        'age':25,
        'city':'Tiruvallur'
    },
    'user2': {
        'name':'varun',
        'age':35,
        'city':'chennai'
    },
}
for user in users.items():
    print(user)
    #print(user["name"])
for x,y in users.items():
    print(x,y)