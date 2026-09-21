class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # product of all array elements to the left
        # [1,2,4,6] -> [1,1,2,8]
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # multiply all prefixed elements by product of all array elements to the right
        # [1,1,2,8] -> [48,24,12,8]
        postfix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
