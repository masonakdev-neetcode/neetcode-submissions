from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    arr = list()
    n = len(my_list)

    for i in range(n - 3, n):
        arr.append(my_list[i])
    
    return arr


print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
