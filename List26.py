#List
#26. Create a list by concatenating a given list which range goes from 1 to n
l = [10,30,50,10,20,60,20,60,40,40,50,50,30]
for i in range(1,l,1):
    print(i)

    '''
    ch = ['T', 'J']
n = 10
new_list = ['{}{}'.format(a, b) for b in range(1, n+1) for a in ch]
print(new_list)
 

Output

['T1', 'J1', 'T2', 'J2', 'T3', 'J3', 'T4', 'J4', 'T5', 'J5', 'T6', 'J6', 'T7', 'J7', 'T8', 'J8', 'T9', 'J9', 'T10', 'J10']

'''