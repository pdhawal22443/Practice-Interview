import pdb
pdb.set_trace()

def subset(input):
    if input == []:
        return [[]]
    else:
        a = subset(input[1:])
        return a + [[input[0]] + b for b in a]

fullList = [1,2,3]
theSubSets = subset(fullList)
print(theSubSets)