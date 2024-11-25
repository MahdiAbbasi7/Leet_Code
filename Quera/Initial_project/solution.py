def calculator(n, m, li):
    n1p, res, window_sum = 0, 0, 0
    sum_of_group, add_sign_to_nums = [], []
    mm = m

    while n1p < len(li):
        window_sum += li[n1p]
        n1p += 1
        if n1p == mm:
            sum_of_group.append(window_sum)
            window_sum = 0
            mm += m
            if mm > n:
                mm = n

    for i in range(len(sum_of_group)):
        if i % 2 == 0:
            add_sign_to_nums.append(sum_of_group[i] * 1)
        else:
            add_sign_to_nums.append(sum_of_group[i] * (-1))

    for i in range(len(add_sign_to_nums)):
        res += add_sign_to_nums[i]
    return res


print(calculator(10, 1, li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
