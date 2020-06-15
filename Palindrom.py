str1 = 'Dhawal'

'''1st method'''
if (str1[0:] == str1[-1::-1]):
    print("its a palindrome")
else:
    print("It is  not a palindrome")

'''2nd method'''
import pdb
#pdb.set_trace()

flag = 0
for i in range(0,int(len(str1)/2)):
    if str1[i] != str1[-i -1]:
        flag = 1
        break

if flag == 0:
    print("Palindrome")
else:
    print("Not Palindrome")

