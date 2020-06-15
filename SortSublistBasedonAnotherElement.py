# Python code to sort the lists using the second element of sublists
# Inplace way to sort, use of third variable

#Input : [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
#Output : [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]
import pdb
#pdb.set_trace()

def Sort1(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][0] > sub_li[j + 1][0]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li

def Sort2(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][0] is sub_li[j + 1][0]) and (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li

def Sort3(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] is sub_li[j + 1][1]) and (sub_li[j][2] > sub_li[j + 1][2]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li

# Driver Code
sub_li = [['rishav', 10 , 20], ['ram', 10 , 50], ['rishav', 15 , 1] ,['akash', 10 , 2],['ram', 10 , 25],['akash', 5 , 16]]
#test1 = Sort(sub_li)
test2 = Sort1(sub_li)
print(test2)
test3 = Sort2(test2)
print(test3)
test4 = Sort3(test3)
print(test4)

