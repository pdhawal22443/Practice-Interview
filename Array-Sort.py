# lst = [1,8,2,7,3,6,4]
lst = ['a','o','b','z','k','v']

print(len(lst))
i =0
while i < (len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i],lst[i+1] = lst[i+1],lst[i]
        i = -1
    i = i+1


print(lst)

