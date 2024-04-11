def binary_search(arr, low, high, x):
    # Check base case
    if high >= low :
        mid = (high + low) // 2

        if arr[mid] == x :
            return mid
        
        elif arr[mid] > x :
            return binary_search(arr, low, mid - 1, x)
        
        else : 
            return binary_search(arr, low, mid + 1, x)
    else : 
        # element is not present in the array
        return -1

arr=[]
size=input("enter no of elements-")
print("enter elements in array/list-")
for i in range(int(size)):
    data=input()
    arr.append(data)
x=input("enter element to search-")
result=binary_search(arr,0,len(arr)-1,x)
if result != -1:
    print("Element is present at index", str(result+1))
else:
    print("Element is not present in array")