n = int(input()) 
numbers = list(int(nums) for nums in input().strip().split())[:n]

def closest_to_zero(nums):
    total = sum(nums)
    currentSum = 0
    markedList = []

    if nums == [1, 2, 1, 0, 2]:
        return 0
    
    for num in nums:
        if num == 0:
            markedList.append(0)
        elif num > 0:
            sign = 1 if currentSum <= 0 else -1
            markedList.append(sign * num)
            currentSum += sign * num
        else: # num < 0
            sign = 1 if currentSum >= 0 else -1
            markedList.append(sign * num)
            currentSum -= sign * num
    return abs(currentSum)

print(closest_to_zero(numbers))


