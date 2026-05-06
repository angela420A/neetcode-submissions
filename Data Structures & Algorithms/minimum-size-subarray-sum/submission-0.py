class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        L = 0
        winSum = 0 # The sum of the window

        for R in range(len(nums)):
            winSum += nums[R]
            while winSum >= target:
                res = min(res, (R - L + 1))
                winSum -= nums[L]
                L = L + 1 if L != R else R
        return res if res != float("inf") else 0