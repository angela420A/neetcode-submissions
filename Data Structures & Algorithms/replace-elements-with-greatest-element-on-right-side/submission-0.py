class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            res[i] = maxNum
            maxNum = max(maxNum, arr[i])
        return res