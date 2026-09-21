class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeroes = 0
        zeroIdx = -1
        product = 1
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                numZeroes += 1
                zeroIdx = i
            else:
                product *= num
        
        if numZeroes > 1:
            return ans
        elif numZeroes == 1:
            ans[zeroIdx] = product
            return ans
        
        for i, num in enumerate(nums):
            ans[i] = int(product / num)
        
        return ans
