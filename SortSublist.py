lst = [[1,9,2,8,3,7,4,6,5],['D','A','B','K','C'],[11,99,22,88,33,77]]

lst = [['ram', 25, 66],['ram', 24, 65],['ram1', 20, 65],['ram2', 20, 65],['ram', 25, 65]]
#o/p = [['ram', 24, 65],,['ram', 25, 65],['ram', 25, 66],['ram1', 20, 65],['ram2', 20, 65]]



def sortlist (lst):
    i =0
    while i < (len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
            i = -1
        i = i+1
    return lst

sorted_list = list(map(sortlist,lst))
print(sorted_list)





