def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        j = i - 1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = []
size=int(input("enter size of array-"))
print("enter elements of array to be sorted-")
for i in range(size):
    data=int(input())
    arr.append(data)
# Driver code to test above
insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])

