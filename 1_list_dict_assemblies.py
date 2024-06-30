def squ_num(x):
    return x ** 2


def odd_check(y):
    return y % 2


some_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
res_list = map(squ_num, filter(odd_check, some_list))

print(list(res_list))
