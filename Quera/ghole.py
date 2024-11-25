"""
[
    1, 1, 1, 0
    1, 1, 0, 1
    0, 1, 1, 1
]



"""


def find_gole(input: list) -> int:
    low = 0
    high = len(input) - 1
    mid = (low + high) // 2

    if input[mid - 1] <= input[mid] >= input[mid + 1]:
        return input[mid]

    if input[mid] <= input[mid + 1]:
        mid += 1
        find_gole(input[mid:-1])

    if input[mid] >= input[mid - 1]:
        mid -= 1
        find_gole(input[:mid])


print(find_gole([1, 2, 3, 4, 5]))
