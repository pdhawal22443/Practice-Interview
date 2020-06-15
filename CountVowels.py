str = 'Services'
m = list(str)
count = 0

while m:
    d = m.pop()
    if (d is 'a') or (d is 'e') or (d is 'i') or (d is 'o') or (d is 'u'):
        count += 1

print(count)

vowel = ['a','e','i','o','u']
res = len([i for i in str if i in vowel])
print(res)


