"""
Search in a rotated or partially sorted array.

Use Case: Finding an element in rotated arrays.
Example: Search for a target in a rotated sorted array.
"""


def search(nums: list, target: int):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 71
result = search(nums, target)
print(result)  # Output: 3 (index of the target)
