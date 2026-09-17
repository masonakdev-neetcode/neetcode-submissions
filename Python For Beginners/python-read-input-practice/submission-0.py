def add_two_numbers() -> int:
    num_strs = input()
    str_list = num_strs.split(",")

    res = 0

    for e in str_list:
        res += int(e)

    return res


print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
