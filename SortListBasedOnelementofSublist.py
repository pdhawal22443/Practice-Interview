# Python | Sort a list according to the second element in sublist
# Input : [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
# Output : [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]

list_ex = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
i =0
while i < len(list_ex) -1:
    if list_ex[i][1] > list_ex[i+1][1]:
        temp = list_ex[i+1][1]
        list_ex[i+1][1] = list_ex[i][1]
        list_ex[i][1] = temp
        i = -1
    i += 1

print(list_ex)