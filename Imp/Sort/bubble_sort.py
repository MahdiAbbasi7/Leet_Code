def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        # range(n) also works but the outer will repeat one time more than needed.
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]

arr = []
size=int(input("enter size of array-"))
print("enter elements of array to be sorted-")
for i in range(size):
    data=int(input())
    arr.append(data)

bubble_sort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),