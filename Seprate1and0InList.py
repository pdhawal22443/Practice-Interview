lst = [1,0,1,0,1,0,1,0]
#o/p --[0, 0, 0, 0, 1, 1, 1, 1]

i = 0;
j = len(lst) - 1

while i < j:
    if lst[i] == 1 and lst[j] == 0:
        lst[i],lst[j] = lst[j],lst[i]
    if lst[i] == 0:
        i +=1
    if lst[j] == 1:
        j -= 1

print(lst)