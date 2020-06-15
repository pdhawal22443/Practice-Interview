#lst = [1,2,3,5,4,9,1,5,4,6,9,2]
lst = [0,0,1,1,1,2,2,3,3,4]

i = 0
while True:
    if lst.count(lst[i]) > 1:
        del lst[i]
    else:
        i += 1
    if i == len(lst) - 1:
        break

print(lst)