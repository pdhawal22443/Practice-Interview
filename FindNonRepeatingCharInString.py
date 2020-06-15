string = 'ABCDEFGABCDEFABC'
# find non-Repeting Char
#method 1 (List Comprehension)
res = [i for i in string if string.count(i) == 1]
print(res)

#2nd method (Using Filter)
res1 = list(filter(lambda x : string.count(x) == 1 , string))
print(res1)

