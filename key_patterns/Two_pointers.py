"""
Two pointers work towards a solution by converging from different ends of an array.

Use Case: Find pairs in a sorteddddd array.
Example: Find two numbers that sum up to a target.
"""


def find_two_num_in_sorted(arr: list[int], target: int) -> tuple:
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


print(find_two_num_in_sorted([0, 2, 3, 5, 7, 8], 5))

"""
What if the array is not sorted? Use hash maps.
"""


def two_sum(arr, target):
    "Find two numbers that sum up to a target."
    num_map = {}
    for index, num in enumerate(arr):
        print(index, num)
        if target - num in num_map:
            return [num_map[target - num], index]
        else:
            num_map[num] = index
    return None


print(two_sum([0, 2, 3, 5, 7, 8], 5))
