class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # 1,1,2,8

        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        # 48,24,12,8

        return res