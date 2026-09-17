from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    raise ValueError("you said we couldn't get here")


print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

