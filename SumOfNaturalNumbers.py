'''
limit=int(input("Enter the limit :"))
result=0
for i in range(1,limit):
    result=result+i
print("Sum of natural numbers :",result)

print("Sum of Natural Number using for loop ")
'''

start = int(input("Enter the starting value : "))
end   = int(input("Enter the ending value : "))

result=0

for x in range(start,end+1):
    result=result+1

print("Sum of natural number is ",result)
