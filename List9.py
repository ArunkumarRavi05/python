#List
#Write a Python program to find the list of words that are longer than n from a given list of words
a=['Arun','Varun','Kumar','Tharun','ram']
for i in a:
    if len(i)>=4:
        print(i)

'''
n=4
str="Find the List of Words that are Longer than n from a given List of Words"
new_list = []
text = str.split(" ")
for x in text:
	if len(x) > n:
		new_list.append(x)
print(new_list'''