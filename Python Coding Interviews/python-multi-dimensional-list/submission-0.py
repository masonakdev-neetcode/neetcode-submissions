from typing import List
import sys


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    sys_min: int = -sys.maxsize - 1
    arr: List[int] = list()
    for i, sublist in enumerate(nested_arr):
        sublist_max: int = sys_min
        for j, num in enumerate(sublist):
            sublist_max = max(num, sublist_max)
        arr.append(sublist_max)
    return arr


print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
