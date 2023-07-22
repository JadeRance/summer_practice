value_list = [1, 2, 3, 4]
powered_list = list(map(lambda x: x * x, value_list))
print(*powered_list, sep=', ')
