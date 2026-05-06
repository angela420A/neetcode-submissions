class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, currSum = 0, 0
        prefixSum = { 0: 1 } # key: prefix Sum, val: count

        for i in range(len(nums)):
            currSum += nums[i]

            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res
