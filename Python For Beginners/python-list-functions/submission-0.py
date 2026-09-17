from typing import List

def get_sum(nums: List[int]) -> int:
    _sum = 0

    for num in nums:
        _sum += num
    
    return _sum


def get_min(nums: List[int]) -> int:
    curr_min = nums[0]

    for num in nums:
        curr_min = min(num, curr_min)
    
    return curr_min


def get_max(nums: List[int]) -> int:
    curr_max = nums[0]

    for num in nums:
        curr_max = max(num, curr_max)
    
    return curr_max


print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
