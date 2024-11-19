"""
Two pointers work towards a solution by converging from different ends of an array.

Use Case: Find pairs in a sorteddddd array.
Example: Find two numbers that sum up to a target.
"""


def max_sub_array(arr: list[int], target: int) -> tuple:
    "Find two numbers that sum up to a target."
    left, right = 0, len(arr) - 1
    while (left, right):
        sum_of_vals = arr[left] + arr[right]
        if sum_of_vals == target:
            return (arr[left], arr[right])
        elif sum_of_vals < target:
            left += 1
        else:
            right -= 1


print(max_sub_array([0, 2, 3, 5, 7, 8], 5))
