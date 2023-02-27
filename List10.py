#List
#10.Write a Program that get two lists as input and check if they have at least one common member
a=['Arun','Varun','Kumar','Tharun','ram']
b=['Arun','Sam']
for i in a:
    for j in b:
        if i == j:
            print(j)