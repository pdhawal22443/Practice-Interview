class Employee:
    #class Variable
    test_str = 'Mr.'

    def __init__(self,first_name,last_name):
        self.name = first_name
        self.lastname = last_name

    def display(self):
        print("first name is {}".format(self.name))
        print("last name is {}".format(self.lastname))

        #Accessing class variable
        print("My full name is {}".format(Employee.test_str + " " + self.name + " " + self.lastname))


emp1 = Employee('dhawal','pawar')
em2 = Employee('Nakul','Jain')
emp1.display()

#a class method can be called in different method
Employee.display(emp1)

#Inheritance
#created a Class Manager and inherited Emloyee method , not instance of Manager can call Employee Class methods

class Manager(Employee):
    def __init__(self,frst_name,lst_name,*emp):
        #Calling a Super class constructor
        super().__init__(frst_name,lst_name)
        if emp == None:
            self.emp = []
        else:
           self.emp = emp

    def display_emp(self):
        for elem in self.emp:            
            print("---> {}".format(elem))



mgr1 = Manager('Kapil','Sharma',[emp1,em2])
mgr1.display_emp()

#print(help(Developer))


def validparanString(test):
    temp = []
    p1 = ''
    for elem in test:
        if isopenParan(elem):
            temp.append(elem)
        else:
            if len(temp) == 0:
                return False
            p1 = temp.pop()
            res = validateparan(p1 ,elem)
            if not res:
                return False
    return len(temp) == 0



def isopenParan(char):
    if (char is '{' or char is '[' or char is '('):
        return True
    else:
        return False

def validateparan(elem1,elem2):
    if (elem1 is '{' and elem2 is '}' or elem1 is '(' and elem2 is ')' or elem1 is '[' and elem2 is ']'):
        return True
    else:
        return False


p = '{[({})]}'
if validparanString(p):
    print("It is a Valid String")
else:
    print("It is a Invalid String")

import math
import pdb
def kPrimeFactor(n, k):
    # Find the number of 2's that divide k
    while (n % 2 == 0):
        k = k - 1
        n = n / 2
        if (k == 0):
            return 2

    # n must be odd at this point. So we can
    # skip one element (Note i = i +2)
    i = 3
    while i <= math.sqrt(n):

        # While i divides n, store i and divide n
        while (n % i == 0):
            if (k == 1):
                return i

            k = k - 1
            n = n / i

        i = i + 2

    # This condition is to handle the case
    # where n is a prime number greater than 2
    if (n > 2 and k == 1):
        return n

    return -1

#pdb.set_trace()
print ("kth prime factor is {}".format(kPrimeFactor(11,2)))

str = 'hello'
print(str[::-1])


def findminMax(arr):
    min = arr[0]
    max1 = arr[0]
    i = 0

    while (i < len(arr)):
        if arr[i] <= min:
            min = arr[i]
        elif arr[i] > max1:
            max1 = arr[i]

        i += 1
    print("min and maxr are {} {}".format(min,max1))

findminMax([9,8,7,6,5,4,3,2,1,11,12,13,14,-4,15,16,17,18,19])


arr = ['a','b','c']
res = [[]]

for k in arr:
    res += [[k] + i for i in res]
print(res)

str1 = 'My Name is Dhawal'
arr = str1.split(' ')[::-1]
print(arr)


arr1 = [4,13,5,6,7,12,9,20]
arr1.sort()
print(arr1)

#4,5,6,7,9,12,13,20
list1 = []
list2 = []

for i in arr1:
    if i%2 == 0:
        list1.append(i)
    else:
        list2.append(i)

print(list1,list2)





def fact(num):
    sum =1
    if (num >= 1):
        sum = num * fact(num-1)
        num -= 1
    return sum

print(fact(5))

lsts = [(1,2),(1,3),(0,1)]
lsts.append((4,5))

print(lsts)









