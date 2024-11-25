"""
Used to track a subset of data that shifts over time, commonly in arr, string.
Use Case: Maximum sum of subarrays.
Example: Maximum sum of subarray of size K.
"""


def max_sub_array(arr: list[int], size: int) -> int:
    "return the maximum sum of subarray of size K."
    max_sub, window_slid = 0, 0
    for i in range(len(arr)):
        window_slid += arr[i]
        if i >= size - 1:
            max_sub = max(max_sub, window_slid)
            window_slid -= arr[i - (size - 1)]
    return max_sub


print(max_sub_array([0, 7, 6, 10, 5, 2, 3], 3))
