class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        sortedNums = nums.copy()
        sortedNums.sort()
        
        prev = sortedNums[0]
        currSeq = 1
        maxSeq = 1

        for i in range(1, n):
            if sortedNums[i] == prev:
                continue
            elif sortedNums[i] == prev + 1:
                currSeq += 1
            else:
                maxSeq = max(currSeq, maxSeq)
                currSeq = 1
            prev = sortedNums[i]
        
        return max(currSeq, maxSeq)
