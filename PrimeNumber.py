def isPrime(n,i=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if(n % i == 0):
        return False
    if (i*i > n):
        return True
    return isPrime(n,i+1)

if(isPrime(157)):
    print("Prime")
else:
    print("Not Prime")

lst = list(filter(isPrime,range(100)))
print(lst)

#print(list(range(100)))



#with open ('C:\test\test1.txt') as f:
 #   f.readlines()
