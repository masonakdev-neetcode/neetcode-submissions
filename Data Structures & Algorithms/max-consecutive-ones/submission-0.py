class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0
        currConsecutiveOnes = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currConsecutiveOnes += 1
                maxConsecutiveOnes = max(maxConsecutiveOnes, currConsecutiveOnes)
            else:
                currConsecutiveOnes = 0
        
        return maxConsecutiveOnes
