import pdb

lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = {}

def groupAnagrams(strs):
    d = {}
    for i in strs:
        s = ''.join(sorted(i))
        if s not in d.keys():
            d[s] = []
        d[s].append(i)

    print("Dictionary {}".format(d))
    lst = []
    for i in d.keys():
        lst.append(d[i])
    return lst

res99 =  groupAnagrams(lst)
print('Result Dictionary is {}'.format(res99))
