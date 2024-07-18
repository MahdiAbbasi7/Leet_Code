# This function takes last element as pivot, places
# the pivot element at its correct position in a sorted
# array, and places all smaller (smaller than pivot)
# to the left of pivot and all greater elements to the right
# of pivot
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot :
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

# The main function that implements Quicksort
# arr[] --> Array to be sorted,
# low --> Starting index
# high --> Ending index

def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr,low,high)
        
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

arr = []
size=int(input("enter size of array-"))
print("enter elements of array to be sorted-")
for i in range(size):
    data=int(input())
    arr.append(data)
    n = len(arr)

quick_sort(arr,0,n-1)

print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])
