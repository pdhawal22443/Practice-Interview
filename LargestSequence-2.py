'''
Given an array of integers, find the length of the longest sub-sequence such that
elements in the subsequence are consecutive integers, the consecutive numbers
can be in any order.
Examples:

Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4
The subsequence 1, 3, 4, 2 is the longest subsequence
of consecutive elements
'''
import pdb
pdb.set_trace()
arr = (1, 9, 3, 10, 4, 20, 2)
ans =0
for i in range(len(arr)):
    if (arr[i] - 1 not in arr):
        j = arr[i]
        while (j in arr):
            j += 1
        ans = max(ans , j - arr[i])

print(ans)



