def fibo(n: int) -> list:
    nums = [0] * (n + 1)
    nums[1] = 1

    if n <= 1:
        return n
    else:
        for i in range(2, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[i]


"""0 1 1 2 3 5 8 """
print(fibo(10))
