'''Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]'''
import pdb
#pdb.set_trace()

#1st method loop
lst = [-1, 0, 1, 2, -1, -4]
'''
for elem1 in range(0,len(lst) -2):
    for elem2 in range(elem1+1,len(lst) -1):
        for elem3 in range(elem2+1,len(lst)):
            if lst[elem1] + lst[elem2] + lst[elem3]  == 0:
                print("3 elements are {} {} {}".format(lst[elem1],lst[elem2],lst[elem3]))

'''
#2nd Method is hashing , time complexity of O(n2)
def findTriplets(arr,sum):
    found = False
    n = len(arr)
    for elem1 in range(n - 1):
        # Find all pairs with sum
        res = set()
        for elem2 in range(elem1 + 1, n):
            x = (sum -(arr[elem1] + arr[elem2]))
            if x in res:
                print(x, arr[elem1], arr[elem2])
                found = True
            else:
                res.add(arr[elem2])
    if found == False:
        print("No Triplet Found")

findTriplets(lst,3)