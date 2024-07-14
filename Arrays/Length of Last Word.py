string = " y "


def sample(string):
    str_list = list(string)[::-1]
    res = 0

    for i in range(len(str_list)):
        if str_list[i] != " ":
            res+=1
        else:
            if res > 0:
                return res
    return res
print(sample(string))