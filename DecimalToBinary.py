import pdb
# pdb.set_trace()

# program to convert Decimal to Binary and also count the occurance of 1's

res = []
def decToBin (num):
    res = []
    if num > 1:
        decToBin(num // 2)
    print(num%2)


    #temp = num % 2
    #res.append(temp)

#print(decToBin(5))
#print(res.count(1))
import pdb
pdb.set_trace()

def find( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 *
                find(int(decimal_number // 2)))

print(find(10))







