class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        openIdx = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[openIdx] = nums[i]
                openIdx += 1
        
        return openIdx
