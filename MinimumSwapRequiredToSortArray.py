'''An efficient algorithm to find the minimum number of swaps required to sort the array in ascending order.

Problem:
We have an unordered array consisting of consecutive distinct integers ∈ [1,2,3,...n], where n is the size of the array.
We are allowed to swap any two elements.
We need to find the minimum number of swaps required to sort the array in ascending order.

Algorithm Concept:
1. Look at each index and compare the index position with its element value if its same then move to the next index position.
2. If index position is not the same as element value then treat element value as index value for finding the next element.
3. If we come back to the visited element then there exist a cycle, then count the size of that cycle, the number of swaps for
particular cycle would be size-1, do this for all the cycles and add them together.
Ex = Input = [1,4,3,2]
output should be 1 , only 1 swap of 4 and 2 are required
'''

import pdb


# #lst = [1, 5, 4, 3, 2] o/p - 2
# lst = [4,3,2,1] o/p - 2


#lst = [1, 5, 4, 3, 2]
lst = [4,3,2,1]
#lst = [1,2,3,5,4]
hash = {}
min_swap = 0

for i in range(1,len(lst)+1):
    hash[i] = lst[i-1]

print(hash)

#pdb.set_trace()
for key,val in hash.items():
    if int(hash[key]) < 0 or hash[key] == key:
        continue

    cycle_count = 0
    val = key

    while hash[abs(val)] > 0:
        hash[abs(val)] = 0 - (hash[abs(val)])
        val = hash[abs(val)]
        cycle_count += 1

    min_swap += cycle_count -1

print(min_swap)


#<<<==============================Better Approach and simple===========================================>>>
def minimumSwaps(arr):
    dec = {}
    min_swap = 0
    for i, j in enumerate(arr):
        dec[i+1] = j
    #pdb.set_trace()
    for key, val in dec.items():
        if dec[key] < 0 or key == dec[key]:
            continue

        count = 0
        # val = key

        while dec[abs(key)] > 0:
            dec[abs(key)] = 0 - (dec[abs(key)])
            key = dec[abs(key)]
            count += 1

        min_swap += count - 1

    return min_swap

res = minimumSwaps([4,3,1,2])
print(res)




