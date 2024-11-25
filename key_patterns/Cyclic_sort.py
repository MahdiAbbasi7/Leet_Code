"""
Sort numbers when elements fall within a range.

Use Case: Finding missing numbers.
Example: Find the missing number from 1 to N.
"""


def find_missing_number(nums):
    i = 0

    while i < len(nums):
        if nums[i] != i and nums[i] < len(nums):
            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)


print(find_missing_number([3, 0, 2, 5, 8]))
