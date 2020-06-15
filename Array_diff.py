lst1 = [9,2,3,4,6,8,10]
lst2 = [2,6,10,14,9,11,3]

# this will print the combine elements of lst 1 which are which is absent in lst2 and vice versa
print(list(set(lst1) - set(lst2)) + list(set(lst2) - set(lst1)))

# ^ this operator is for synmetric difference it will do the same
print("diff is {}".format(set(lst2) ^ set(lst1)))

'''

#note : on set you can perform various opration like this
| -> Union
& -> intersection 
^ -> symmetric Difference
- -> difference 

'''

#2nd method :
print([item for item in lst1 if not item in lst2])

#3rd method using list comprehension
list3 = [1,2,3,4,5,6]
list4 = [4,5,6,7,8,9]

def list_diff(list1,list2):
    diff = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return diff
print("difference is {}".format(list_diff(list3,list4)))

import pdb
# pdb.set_trace()
# 3rd method using while
count,count1 = 0,0
res = []
while count < len(lst1):
    count1 = 0
    while count1 < len(lst2):
        flag = 0
        if lst1[count] == lst2[count1]:
            flag = 1
            break
        else:
            count1 = count1 + 1
    if (flag == 0):
        res.append(lst1[count])
    count = count+ 1

print('resutl {}'.format(res))

