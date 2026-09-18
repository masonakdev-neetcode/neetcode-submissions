from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    res: Dict[str, int] = defaultdict(int)
    for i, c in enumerate(s):
        if c not in res:
            res[c] = 0
        res[c] += 1
    return res


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    res: Dict[int, List[int]] = defaultdict(list)
    for i in range(len(nums)):
        if nums[i][0] not in res:
            res[nums[i][0]] = list()
        for j in range(1, len(nums[i])):
            res[nums[i][0]].append(nums[i][j])
    return res


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
