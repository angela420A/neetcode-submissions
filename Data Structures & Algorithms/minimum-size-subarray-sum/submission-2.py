class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        window = 0
        L = 0 # Left poiner

        for R in range(len(nums)):
            window += nums[R]
            while window >= target:
                res = min(res, R - L + 1)
                window -= nums[L]
                L+=1
        return 0 if res == float("inf") else res
            