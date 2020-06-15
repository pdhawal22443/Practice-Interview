#https://www.youtube.com/watch?v=iKjftj3p8ME    --- Explanation
# problem 287 in leetcode

lst = [1,1,4,3,2]
pfast = 0
pslow = 0

#1st while loop is to detect the cycle
while True:
    pslow = lst[pslow]
    pfast = lst[lst[pfast]]

    if (pfast == pslow):
        break

#2nd loop is to actually get the duplicate and print it
# after 1st loop keep the fast pointer as it is , initialize the slow pointer again to zero

pslow  = 0

while True:
    pslow = lst[pslow]
    pfast = lst[pfast]

    if (pfast == pslow):
        break

print("duplicate number is {}".format(pfast))