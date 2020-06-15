#time is in 24Hrs clock - HH:MM:SS
#time1 = [00,15,34]
#time2 = [6,14,12]

time1 = [00,00,00]
time2 = [23,59,00]

#1st we will convert the time in seconds
def getTimeInSeconds(arr):

    #if Hrs time is 00 that means it is 24Hrs
    if (arr[0] == 00):
        arr[0] = 24

    # Hrs to Sec
    resSum = arr[0] * 3600

    # mins to Sec
    resSum += arr[1] * 60

    # adding the seconds
    resSum += arr[2]

    return resSum


def converttimebackto24hrs(diff):
    #Sec to Hrs
    hrs = int(diff/3600)

    diff = diff%3600

    #Sec to mins
    mins = int(diff/60)

    diff = diff%60

    #diff is already in seconds
    sec = diff

    return ([hrs,mins,sec])

diff = abs(getTimeInSeconds(time1) - getTimeInSeconds(time2))


result = converttimebackto24hrs(diff)

print(result)




