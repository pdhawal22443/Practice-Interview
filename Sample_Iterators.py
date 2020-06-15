class powerofTwo:
    def __init__(self,max1):
        self.n = 0
        self.max = max1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return 2**self.n
        else:
            print("Done")
            raise StopIteration

obj1 = powerofTwo(4)
iterobj = obj1.__iter__()
print(iterobj.__next__())
print(iterobj.__next__())
print(iterobj.__next__())
print(iterobj.__next__())


#3rd method using list comprehension
list3 = [1,2,3,4,5,6]
list4 = [4,5,6,7,8,9]

def list_diff(list1,list2):
    diff = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return diff
print(list_diff(list3,list4))




