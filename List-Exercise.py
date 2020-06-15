'''5. Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

lst = ['abc', 'xyz', 'aba', '1221']

res = [i for i in lst if len(i) >= 2 and i[0] == i[-1]]
print(res)


tt1 =  [('a',10,34),('b',23,10),('c',12,50),('a',7,50),('b',45,7),('c',10,45)]
s = sorted(tt1, key = lambda x: (tt1[0],tt1[1]))
print(s)

''' Write a Python function that takes two lists and returns True if they have at least one common member.'''
lst0 = [1,2,3,4,5,6]
lst1 = [7,8,0,9,10,1]

def onecommon(lst0,lst1):
    res = True if (len([i for i in lst0 if i in lst1])) == 1 else False
    print("result {}".format(res))

onecommon(lst0,lst1)

'''Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]'''


