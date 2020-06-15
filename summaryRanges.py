'''Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.'''

class Solution:
    def summaryRanges(self, nums):
        temp = []
        for i in nums:
            if not temp or i > temp[-1][1] +1:
                temp.append([i,i])
            else:
                temp[-1][1] = i
        res = [str(i) if i==j else str(i)+'->'+str(j) for i,j in temp]
        return res

lst = [0,2,3,4,6,8,9]
obj1 = Solution()
print(obj1.summaryRanges(lst))

#================2ND SOLUTION WITH time complexity O(n) and space complexity O(1)

class Solution1:
    def summaryRanges1(self, nums):
        res = []
        start=end=nums[0]
        for i in range(1,len(nums)+1):
            if i < len(nums) and nums[i] == end +1:
                end = nums[i]
            else:
                if start != end:
                    res.append(str(start)+"->"+str(end))
                else:
                    res.append(str(end))

                if i < len(nums):
                    start = end = nums[i]

        return res

lst = [0,2,3,4,6,8,9]
obj1 = Solution1()
print(obj1.summaryRanges1(lst))
