import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k: nums[i], v: (freq, nums[i])
        numToFreqNumTuple = dict()
        for num in nums:
            if num not in numToFreqNumTuple:
                numToFreqNumTuple[num] = (-1, num)
            else:
                updatedFreq = numToFreqNumTuple[num][0] - 1
                numToFreqNumTuple[num] = (updatedFreq, num)
        
        maxHeap = []
        for freqNumTuple in numToFreqNumTuple.values():
            heapq.heappush(maxHeap, freqNumTuple)
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        
        return ans
