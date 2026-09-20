class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        twoN = n * 2
        concat = [0] * twoN
        for i in range(twoN):
            idx = i
            if idx >= n:
                idx -= n
            concat[i] = nums[idx]
        return concat
