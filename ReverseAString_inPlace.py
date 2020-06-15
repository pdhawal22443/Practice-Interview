str = "MY NAME IS DHAWAL"
#o/p should be DHAWAL IS NAME MY

#1st method
lst = ' '.join(reversed(str.split(' ')))
print(lst)

#2nd method [Reverse the String excluding special characters
#I/p -> Dhawal , Take Care !
#o/p -> Care , Take Dhawal !

import pdb
pdb.set_trace()

str2 = ['a','@','b','!','c','$','d','&','e']
k = 0
r = len(str2) - 1
while(k<r):
    if not str2[k].isalpha():
        k += 1
    elif not str2[r].isalpha():
        r -= 1
    else:
        str2[k],str2[r] = str2[r],str2[k]
        k += 1
        r -= 1

print(str2)

#note that 2nd code is not working bt logic is correct









