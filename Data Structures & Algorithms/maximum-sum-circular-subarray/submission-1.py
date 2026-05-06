class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # to check if no values
        if not nums or len(nums) == 0:
            return 0

        currMax, currMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = sum(nums)
        
        for n in nums:
            currMax = max(currMax + n, n)
            globalMax = max(currMax, globalMax)
            currMin = min(currMin + n, n)
            globalMin = min(currMin, globalMin)
        return  globalMax if globalMax < 0 else max(globalMax, total - globalMin)