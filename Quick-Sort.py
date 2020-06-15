import pdb
#arr = [10, 7, 8, 9, 1, 5]

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for elem in range(low, high):

        # If current element is smaller than the pivot
        if arr[elem] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[elem] = arr[elem], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [10, 80, 30, 90, 40, 50, 70]
pdb.set_trace()
n = len(arr)
quickSort(arr,0,n-1)
print(arr)