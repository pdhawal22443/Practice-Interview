sten = 'This is a Nice Test String'
# o/p -> sihT si a eciN tseT gnirtS

#1st method using list comprehension
res = ' '.join(word[::-1] for word in sten.split(' '))
print(res)

sten = 'This is a Nice Test String'
# Reverse the string word by word
# ['String', 'Test', 'Nice', 'a', 'is', 'This']
arr = sten.split()
print(arr)
print(len(arr))
i = 0
while (i < len(arr)//2):
    temp = arr[len(arr) -i -1]
    arr[len(arr) - i - 1] = arr[i]
    arr[i] = temp
    i += 1

print(arr)


