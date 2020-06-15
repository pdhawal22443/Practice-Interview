import re
text = '''The wise men told the two sons to switch
10.11.64.99 camels.Come back 10.11.64.91
next week for another riddle!'''

pattern = re.compile(r'\d{1,2}[0-20]\.\d{1,2}[0-20]\.\d{1,2}\.\d{1,2}')
matches = pattern.finditer(text)

for match in matches:
    #print(match.group())
    test = match.group()

test = re.search('wise',text)
#print(test)

te = "my name is dhawal"
fileobj = open('D:\Personal\Interview\Questions_Incedo.txt',mode='r')
pattern1 = re.compile(r'Python')

for line in fileobj:
    test5 = pattern1.findall(line)
    for hit in test5:
        print(hit)






