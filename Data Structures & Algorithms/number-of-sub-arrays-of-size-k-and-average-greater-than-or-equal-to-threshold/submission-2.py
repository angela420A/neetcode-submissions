class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        window = sum(arr[:k])
        res = 1 if (window / k) >= threshold else 0

        for R in range(k, len(arr)):
            window += arr[R]
            window -= arr[L]
            if (window / k) >= threshold:
                res+=1
            L +=1
        return res