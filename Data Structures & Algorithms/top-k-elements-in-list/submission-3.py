import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # range(len(nums) + 1) because if nums=[7, 7] then count[2]=7, we need freq[2] in bounds
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return [-69]
