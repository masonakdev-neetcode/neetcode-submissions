from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    arr = list()

    for i in range(len(my_list)):
        if i != index:
            arr.append(my_list[i])
    
    return arr


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    arr = list()
    my_list_len = len(my_list)

    for i in range(0, my_list_len - n):
        arr.append(my_list[i])
    
    return arr


print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
