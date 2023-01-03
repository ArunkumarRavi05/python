#Dictionary
#4. Write a Python program to check whether a given key already exists in a dictionary.
user1 ={
    'name':'arun',
    'age':25,
    'city':'salem'
}
if 'city' in user1.keys():
    print("present")
else:
    print("Not present")