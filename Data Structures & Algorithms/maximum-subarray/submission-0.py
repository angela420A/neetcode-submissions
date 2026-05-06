class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += n
            if currSum > res:
                res = currSum
        return res