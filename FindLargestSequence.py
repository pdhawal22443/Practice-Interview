import pdb
#pdb.set_trace()

lst = [1,4,9,1,2,3,4,5,6,7,8,5,4,5, 6, 7 ,8,9]
#lst2 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#lst = ['a','b','c','j','k']
length = len(lst)
count,i,final_count = 1,0,0

while i <= length - 2:
    if lst[i] + 1 == lst[i+1]:
        count += 1
        if final_count < count:
            final_count = count
    else:
        count = 1

    i += 1

print(final_count)
