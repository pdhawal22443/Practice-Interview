a='ddqdwqfwqfggqwq'
import pdb
#pdb.set_trace()
#1st method
#Occurence of each letter
i = 0
res = {}

while i < len(a):
    if a[i] not in res.keys():
        res[a[i]] = 1
    else:
        res[a[i]] = res[a[i]] + 1
    i += 1
print(res)

#2nd method
test = dict((letter,a.count(letter)) for letter in set(a))
print(test)


