from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    res = list()
    for i, num in enumerate(arr):
        if num == element:
            continue
        res.append(num)
    return res


arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
