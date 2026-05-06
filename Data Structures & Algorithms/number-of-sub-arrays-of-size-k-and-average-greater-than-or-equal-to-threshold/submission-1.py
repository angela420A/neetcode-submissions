class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        winSum = sum(arr[:k-1])
        res = 0
        
        for L in range(0, len(arr) - k + 1):
            winSum += arr[L + k -1]
            res += 1 if (winSum / k) >= threshold else 0
            winSum -= arr[L]
        return res
