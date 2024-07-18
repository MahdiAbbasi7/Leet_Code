A = []
size=int(input("enter size of array-"))

print("enter elements of array to be sorted-")

for i in range(size):
    A.append(int(input()))

for i in range(len(A)):
    min_ = i
    for j in range(i+1, len(A)):
        if A[min_] > A[j]:
            min_ = j
    A[i], A[min_] = A[min_], A[i]

print('sorted array')
for i in range(len(A)):
    print('%d' %A[i])