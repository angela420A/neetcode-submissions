class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # If the length of nums == 0
        if len(nums) == 0 or not nums:
            return None

        res = nums[0]
        currNum = 0

        for i in range(len(nums)):
            if currNum < 0:
                currNum = 0
            
            currNum += nums[i]
            res = max(res, currNum)
        return res