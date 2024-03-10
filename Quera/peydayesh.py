"""
>>> find(1, 2, 3)
4

>>> find(1, 4, 3)
2
"""

def find(num1, num2, num3):
    list1 = [num1, num2, num3]
    numbers = [1,2,3,4]
    res = list(set(list1) ^ set(numbers))
    res = sorted(list(res))
    return res[0]