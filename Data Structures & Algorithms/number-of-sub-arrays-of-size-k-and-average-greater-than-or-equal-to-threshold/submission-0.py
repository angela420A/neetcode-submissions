class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Sliding Window - Fixed
        windowSum = sum(arr[:k-1])
        res = 0

        for L in range(len(arr) - k + 1):
            windowSum += arr[L + k - 1]
            if (windowSum / k) >= threshold:
                res+=1
            windowSum -= arr[L]
        return res



        