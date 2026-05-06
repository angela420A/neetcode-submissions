class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        res = nums[0]
        curr = 0
        for n in nums:
            curr = max(curr + n, n)
            res = max(res, curr)
        return res