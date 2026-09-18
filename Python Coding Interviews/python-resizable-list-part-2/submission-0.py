from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr = arr1.copy()
    for i, num in enumerate(arr2):
        arr.append(num)
    return arr
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    res: List[int] = list()
    for i, num in enumerate(arr1):
        if num in arr2:
            continue
        res.append(num)        
    return res


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
