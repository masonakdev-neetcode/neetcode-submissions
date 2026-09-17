class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            if i == n - 1:
                arr[i] = - 1
                break

            greatestToRight = 0
            for j in range(i + 1, n):
                greatestToRight = max(arr[j], greatestToRight)

            arr[i] = greatestToRight

        return arr
