class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementIdxDict = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complementIdxDict:
                return [complementIdxDict[complement], i]
            complementIdxDict[num] = i
        
        return []
