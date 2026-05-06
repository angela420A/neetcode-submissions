class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l, r = 0, 0
        window = 0

        while r < len(nums):
            window += nums[r]
            while window >= target:
                res = min(res, r - l + 1)
                window -= nums[l]
                l += 1
            r += 1
        return res if res != float("inf") else 0
            