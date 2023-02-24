#List
#Write a Python program to print a specified list after removing the 0th, 4th and
# 5th elements. (enumerate)
a=['Arun','Varun','Kumar','Tharun','Ram','Sam','sachin','dhoni']
print(a)
#a.pop(0)
#a.pop(4)
#a.pop(5)
a.remove("Arun")
print(a)
'''
#	   0	  1       2          3      4         5       6
animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
animal = [x for (i,x) in enumerate(animal) if i not in (0,4,5)]
print(animal)'''